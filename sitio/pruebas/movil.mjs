// La vista de teléfono, medida y no mirada (11-nov-2026, change `motor-sitio`).
//
// POR QUÉ EXISTE
// --------------
// La revisión a 390 px se hacía a mano con una captura de Chrome sin interfaz, y esa captura
// mentía: con `--window-size=390,…` Chrome renderiza a ~500 px y recorta, así que parecía un
// desborde que no existía. Una revisión a mano tampoco se repite en el próximo cambio de CSS.
// Esto emula un teléfono de verdad (viewport 390×844, `isMobile`, táctil, DPR 3) con Playwright
// y exige:
//   M0  que la emulación corra: una página en blanco con viewport de móvil mide 390 de ancho.
//       Si no, nada de lo que sigue vale y sale con 2.
// En cada página compilada que no es un redirect:
//   M1  declara `<meta name="viewport" content="width=device-width…">`: sin ella el teléfono
//       la dibuja a 980 px y la achica;
//   M2  nada desborda a lo ancho. Como en un teléfono real, un contenido de 600 px agranda el
//       viewport de diseño a 600 (innerWidth) además del scroll: cualquiera de los dos > 390 es
//       desborde. Una tabla ancha puede desplazarse DENTRO de su caja, no empujar la página.
//   M3  en cada tabla, el primer valor de cada fila se ve sin desplazar (12-nov-2026: en la ficha,
//       las etiquetas de fila ocupaban lo visible y los valores quedaban fuera, sin pista).
// Con `--capturas <dir>` guarda capturas por tramos de cada URL para revisarlas.
//
// Uso:  node pruebas/movil.mjs --dist dist [--capturas ../.capturas-movil] [--solo /slug/]
// Sale con 0 si todo cumple, 1 si alguna página falla, 2 si no pudo medir.

import { createServer } from "node:http";
import { readFile, readdir, stat, mkdir } from "node:fs/promises";
import { join, extname, resolve } from "node:path";
import { chromium } from "playwright";

const ANCHO = 390, ALTO = 844;
const TIPOS = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript",
  ".woff2": "font/woff2", ".woff": "font/woff", ".svg": "image/svg+xml", ".png": "image/png",
  ".jpg": "image/jpeg", ".json": "application/json", ".xml": "application/xml", ".txt": "text/plain" };

function args() {
  const a = process.argv.slice(2), o = { dist: "dist", capturas: null, solo: [] };
  for (let i = 0; i < a.length; i++) {
    if (a[i] === "--dist") o.dist = a[++i];
    else if (a[i] === "--capturas") o.capturas = a[++i];
    else if (a[i] === "--solo") o.solo.push(a[++i]);
    else { console.error(`argumento desconocido: ${a[i]}`); process.exit(2); }
  }
  return o;
}

async function paginas(dist, base = "") {
  const out = [];
  for (const e of await readdir(join(dist, base), { withFileTypes: true })) {
    if (e.isDirectory()) out.push(...await paginas(dist, join(base, e.name)));
    else if (e.name === "index.html") out.push("/" + (base ? base.split("\\").join("/") + "/" : ""));
  }
  return out.sort();
}

function servidor(dist) {
  return createServer(async (req, res) => {
    let ruta = decodeURIComponent(new URL(req.url, "http://x").pathname);
    let f = join(dist, ruta);
    try {
      if ((await stat(f)).isDirectory()) f = join(f, "index.html");
      const cuerpo = await readFile(f);  // se lee antes de la cabecera: un 404 después de un 200 revienta
      res.writeHead(200, { "content-type": TIPOS[extname(f)] || "application/octet-stream" });
      res.end(cuerpo);
    } catch {
      res.writeHead(404); res.end();
    }
  });
}

async function main() {
  const o = args();
  const dist = resolve(o.dist);
  try { await stat(join(dist, "index.html")).catch(() => stat(dist)); } catch {
    console.error(`  ❌ no existe ${dist}: correr \`npm run build\``); return 2;
  }
  let urls = await paginas(dist);
  if (o.solo.length) urls = urls.filter((u) => o.solo.includes(u));
  if (!urls.length) { console.error("  ❌ no hay páginas que medir: un verde sobre cero páginas no vale"); return 2; }

  const srv = servidor(dist);
  await new Promise((r) => srv.listen(0, "127.0.0.1", r));
  const origen = `http://127.0.0.1:${srv.address().port}`;
  let nav;
  try {
    nav = await chromium.launch({ channel: "chrome" });
  } catch (e) {
    srv.close();
    console.error(`  ❌ no se pudo abrir Chrome para emular el teléfono: ${e.message.split("\n")[0]}`);
    return 2;
  }
  const ctx = await nav.newContext({ viewport: { width: ANCHO, height: ALTO }, deviceScaleFactor: 3,
    isMobile: true, hasTouch: true, javaScriptEnabled: true });
  // Las capturas van en otro contexto, en tramos de 390×TRAMO desplazando la página: una página
  // de 11.000 px en un solo PNG no se puede revisar. El CSS del sitio solo depende del ancho, así
  // que un viewport alto se ve igual; la MEDICIÓN corre arriba, a 390×844 con `isMobile`.
  const TRAMO = 4000;
  let ctxFoto = null;
  if (o.capturas) {
    await mkdir(o.capturas, { recursive: true });
    ctxFoto = await nav.newContext({ viewport: { width: ANCHO, height: TRAMO }, deviceScaleFactor: 1 });
  }

  // M0: la emulación corre. Una página vacía con viewport de móvil tiene que medir 390.
  {
    const p0 = await ctx.newPage();
    await p0.setContent('<meta name="viewport" content="width=device-width, initial-scale=1"><p>x</p>');
    const w = await p0.evaluate(() => window.innerWidth);
    await p0.close();
    if (w !== ANCHO) {
      await nav.close(); srv.close();
      console.error(`  ❌ M0 la emulación no corrió: una página vacía mide ${w} px, no ${ANCHO}`);
      return 2;
    }
  }

  const fallos = [];
  let medidas = 0, redirects = 0;
  for (const url of urls) {
    const html = await readFile(join(dist, url, "index.html"), "utf-8");
    if (/<meta[^>]+http-equiv=["']refresh["']/i.test(html)) { redirects++; continue; }
    const vp = html.match(/<meta[^>]+name=["']viewport["'][^>]*>/i);
    if (!vp || !/width\s*=\s*device-width/i.test(vp[0])) {
      fallos.push(`${url}: M1 no declara viewport de móvil (width=device-width): el teléfono la dibuja a 980 px`);
      medidas++;
      continue;
    }
    const p = await ctx.newPage();
    await p.goto(origen + url, { waitUntil: "load" });
    await p.evaluate(() => document.fonts.ready);
    const m = await p.evaluate(() => {
      const ancho = 390, diseno = window.innerWidth, doc = document.documentElement.scrollWidth;
      // Quién empuja: el elemento visible más ancho que sale por la derecha, fuera de una caja
      // que se desplaza sola.
      let culpable = null;
      for (const el of document.body.querySelectorAll("*")) {
        const r = el.getBoundingClientRect();
        if (r.width === 0 || r.right <= ancho + 0.5) continue;
        let caja = el.parentElement, contenido = false;
        while (caja && caja !== document.body) {
          const ox = getComputedStyle(caja).overflowX;
          if (ox === "auto" || ox === "scroll" || ox === "hidden" || ox === "clip") { contenido = true; break; }
          caja = caja.parentElement;
        }
        if (!contenido && (!culpable || r.right > culpable.right)) {
          culpable = { right: Math.round(r.right), tag: el.tagName.toLowerCase(),
            clase: el.className && typeof el.className === "string" ? el.className : "",
            texto: (el.textContent || "").trim().slice(0, 50) };
        }
      }
      // M3: en cada tabla, el primer valor de la fila se ve sin desplazar. Una tabla ancha puede
      // desplazarse dentro de su caja, pero si la etiqueta de la fila ocupa todo lo visible, el
      // lector ve etiquetas sin valores y nada le dice que hay más a la derecha.
      const tapadas = [];
      for (const tb of document.querySelectorAll("table")) {
        if (!tb.getBoundingClientRect().width) continue;
        let caja = tb.parentElement, borde = ancho;
        while (caja && caja !== document.body) {
          if (getComputedStyle(caja).overflowX !== "visible") {
            borde = Math.min(borde, caja.getBoundingClientRect().right);
            break;
          }
          caja = caja.parentElement;
        }
        for (const tr of tb.querySelectorAll("tbody tr")) {
          const td = tr.querySelector("td");
          if (!td || !td.getBoundingClientRect().width) continue;
          const izq = td.getBoundingClientRect().left;
          if (izq > borde - 24) {
            let h = tb, titulo = "";
            while (h && !titulo) {
              let s = h.previousElementSibling;
              while (s && !titulo) { const x = s.matches("h2, h3") ? s : s.querySelector("h2, h3"); if (x) titulo = x.textContent; s = s.previousElementSibling; }
              h = h.parentElement;
            }
            tapadas.push({ titulo: titulo.trim().replace(/\s+/g, " ").slice(0, 60),
              fila: (tr.textContent || "").trim().replace(/\s+/g, " ").slice(0, 40),
              izq: Math.round(izq), borde: Math.round(borde) });
            break;
          }
        }
      }
      return { diseno, doc, culpable, tapadas };
    });
    medidas++;
    if (m.diseno > ANCHO || m.doc > ANCHO) {
      const c = m.culpable;
      fallos.push(`${url}: M2 desborda a lo ancho (${Math.max(m.diseno, m.doc)} px > ${ANCHO})` +
        (c ? ` — <${c.tag}${c.clase ? ` class="${c.clase}"` : ""}> llega a ${c.right} px: «${c.texto}»` : ""));
    }
    for (const x of m.tapadas) {
      fallos.push(`${url}: M3 la tabla «${x.titulo}» deja el valor fuera de la vista: en «${x.fila}» ` +
        `el primer valor empieza en ${x.izq} px y lo visible termina en ${x.borde}`);
    }
    await p.close();
    if (ctxFoto) {
      const nombre = url === "/" ? "inicio" : url.replace(/^\/|\/$/g, "").replace(/\//g, "__");
      const f = await ctxFoto.newPage();
      await f.goto(origen + url, { waitUntil: "load" });
      await f.evaluate(() => document.fonts.ready);
      const alto = await f.evaluate(() => document.documentElement.scrollHeight);
      for (let y = 0, i = 1; y < alto; y += TRAMO, i++) {
        await f.evaluate((y) => window.scrollTo(0, y), y);
        const real = await f.evaluate(() => window.scrollY);  // el último tramo no baja de más
        const sufijo = alto > TRAMO ? `-${String(i).padStart(2, "0")}` : "";
        await f.screenshot({ path: join(o.capturas, `${nombre}${sufijo}.png`),
          clip: { x: 0, y: y - real, width: ANCHO, height: Math.min(TRAMO, alto - y) } });
      }
      await f.close();
    }
  }
  await nav.close();
  srv.close();

  console.log(`VISTA DE TELÉFONO — ${ANCHO}×${ALTO}, isMobile, DPR 3\n`);
  console.log(`  ${medidas} páginas medidas (${redirects} redirects no se miden: no muestran nada)`);
  if (!medidas) {
    console.error("  ❌ no se midió ninguna página: un verde sobre cero páginas no vale");
    return 2;
  }
  for (const f of fallos) console.log(`  ❌ ${f}`);
  if (!fallos.length) console.log(`  ✅ ninguna página desborda a ${ANCHO} px, y en cada tabla el primer valor se ve sin desplazar`);
  if (o.capturas) console.log(`  capturas en ${resolve(o.capturas)}`);
  return fallos.length ? 1 : 0;
}

main().then((c) => process.exit(c), (e) => { console.error(`  ❌ ${e.stack || e}`); process.exit(2); });
