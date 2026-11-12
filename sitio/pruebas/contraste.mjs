// Contraste WCAG 2 AA de lo compilado, medido con axe (12-nov-2026, change `motor-sitio`).
//
// POR QUÉ EXISTE
// --------------
// Ningún guardrail medía contraste. El sitio pasó de oscuro a claro (2.2) cambiando los tokens
// de `:root`, y un color pensado para fondo oscuro puede quedar claro sobre claro sin que nada
// falle: el magenta de «riesgo», por ejemplo. axe (Deque, el motor que usan Lighthouse y las
// DevTools de Chrome) calcula el contraste de cada texto contra su fondo real, con el CSS ya
// aplicado, que es justo lo que no se puede ver leyendo los tokens.
//
// En cada URL pedida, a 390 px (teléfono) y a 1280 px (escritorio):
//   K0  axe corre: una página de control con texto gris claro sobre blanco tiene que dar una
//       violación. Si no la da, la medición no vale y sale con 2.
//   K1  ninguna violación de `color-contrast` (WCAG 2 AA: 4,5:1 en texto normal, 3:1 en grande).
// Los degradados de fondo del legado se quitan antes de medir (axe no mide sobre un degradado). Lo que axe igual no puede decidir (un ícono fuera del plano básico de Unicode, texto
// sobre una imagen) sale como «a revisar» y no cuenta como verde ni como rojo: se informa.
//
// Uso:  node pruebas/contraste.mjs --dist dist --url / --url /modelo/x/ …
// Sale con 0 si todo cumple, 1 si alguna página falla, 2 si no pudo medir.

import { createServer } from "node:http";
import { readFile, stat } from "node:fs/promises";
import { join, extname, resolve } from "node:path";
import { createRequire } from "node:module";
import { chromium } from "playwright";

const require = createRequire(import.meta.url);
const AXE = require.resolve("axe-core/axe.min.js");
const TIPOS = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript",
  ".woff2": "font/woff2", ".woff": "font/woff", ".svg": "image/svg+xml", ".png": "image/png",
  ".jpg": "image/jpeg", ".json": "application/json", ".xml": "application/xml", ".txt": "text/plain" };
const ANCHOS = [
  ["390", { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 }],
  ["1280", { viewport: { width: 1280, height: 800 }, deviceScaleFactor: 1 }],
];

function args() {
  const a = process.argv.slice(2), o = { dist: "dist", urls: [] };
  for (let i = 0; i < a.length; i++) {
    if (a[i] === "--dist") o.dist = a[++i];
    else if (a[i] === "--url") o.urls.push(a[++i]);
    else { console.error(`argumento desconocido: ${a[i]}`); process.exit(2); }
  }
  return o;
}

function servidor(dist) {
  return createServer(async (req, res) => {
    let f = join(dist, decodeURIComponent(new URL(req.url, "http://x").pathname));
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

async function medir(pg) {
  await pg.addScriptTag({ path: AXE });
  return pg.evaluate(async () => {
    // El legado pinta fondos con degradados (el `body` y las tarjetas de la calculadora), y axe no
    // mide texto sobre un degradado: lo deja «a revisar». Con ellos, 1.891 textos de 13 páginas
    // quedaban sin medir y el chequeo era casi ciego. Se mide contra el color de fondo de cada
    // caja, sin el degradado: son tintes suaves sobre ese mismo fondo.
    for (const el of [document.documentElement, ...document.querySelectorAll("*")]) {
      if (getComputedStyle(el).backgroundImage.includes("gradient")) el.style.backgroundImage = "none";
    }
    const r = await window.axe.run(document, { runOnly: { type: "rule", values: ["color-contrast"] },
      resultTypes: ["violations", "incomplete"] });
    const nodos = (lista) => lista.flatMap((v) => v.nodes.map((n) => ({
      selector: n.target.join(" "), texto: (document.querySelector(n.target[0])?.textContent || "")
        .trim().replace(/\s+/g, " ").slice(0, 40),
      datos: n.any.find((x) => x.id === "color-contrast")?.data || {} })));
    return { violaciones: nodos(r.violations), revisar: nodos(r.incomplete).length };
  });
}

async function main() {
  const o = args();
  const dist = resolve(o.dist);
  if (!o.urls.length) { console.error("  ❌ no hay páginas que medir: un verde sobre cero páginas no vale"); return 2; }
  const srv = servidor(dist);
  await new Promise((r) => srv.listen(0, "127.0.0.1", r));
  const origen = `http://127.0.0.1:${srv.address().port}`;
  let nav;
  try {
    nav = await chromium.launch({ channel: "chrome" });
  } catch (e) {
    srv.close();
    console.error(`  ❌ no se pudo abrir Chrome: ${e.message.split("\n")[0]}`);
    return 2;
  }
  // K0: axe corre y ve lo que tiene que ver.
  {
    const p0 = await nav.newPage();
    await p0.setContent('<html lang="es"><body style="background:#fff"><p style="color:#bbb">gris claro</p></body></html>');
    const m0 = await medir(p0);
    await p0.close();
    if (m0.violaciones.length !== 1) {
      await nav.close(); srv.close();
      console.error(`  ❌ K0 axe no corrió como se espera: el control dio ${m0.violaciones.length} violaciones, no 1`);
      return 2;
    }
  }
  const fallos = [];
  let medidas = 0, revisar = 0;
  for (const [ancho, opts] of ANCHOS) {
    const ctx = await nav.newContext(opts);
    for (const url of o.urls) {
      const p = await ctx.newPage();
      // Chrome lanza un error ante un 404 sin cuerpo: se informa como página que falta, no revienta.
      const r = await p.goto(origen + url, { waitUntil: "load" }).catch(() => null);
      if (!r || r.status() !== 200) {
        fallos.push(`${url} a ${ancho} px: no existe en ${o.dist} (HTTP ${r ? r.status() : "?"})`);
        await p.close();
        continue;
      }
      await p.evaluate(() => document.fonts.ready);
      const m = await medir(p);
      medidas++;
      revisar += m.revisar;
      for (const v of m.violaciones) {
        const d = v.datos;
        fallos.push(`${url} a ${ancho} px: K1 «${v.texto}» (${v.selector}) contraste ${d.contrastRatio}:1, ` +
          `pide ${d.expectedContrastRatio} — texto ${d.fgColor} sobre ${d.bgColor}`);
      }
      await p.close();
    }
    await ctx.close();
  }
  await nav.close();
  srv.close();
  console.log(`CONTRASTE WCAG 2 AA (axe) — ${o.urls.length} páginas a 390 y 1280 px (${medidas} mediciones)\n`);
  if (revisar) console.log(`  ·  ${revisar} texto(s) que axe no puede decidir (un ícono fuera del plano básico, texto sobre una imagen): no cuentan`);
  // Una página con 30 celdas del mismo color da 30 líneas: se agrupa por página y regla de color.
  for (const f of fallos.slice(0, 40)) console.log(`  ❌ ${f}`);
  if (fallos.length > 40) console.log(`  … y ${fallos.length - 40} más`);
  if (!fallos.length) console.log(`  ✅ ningún texto bajo el contraste AA en las ${o.urls.length} páginas`);
  else {
    const bajos = fallos.filter((f) => f.includes(" K1 ")).length;
    console.log(`\n  ❌ ${fallos.length} problema(s)` + (bajos ? `: ${bajos} texto(s) bajo el contraste AA, se arregla en los ` +
      "tokens de :root, no página por página" : ": páginas que no se pudieron medir"));
  }
  return fallos.length ? 1 : 0;
}

main().then((c) => process.exit(c), (e) => { console.error(`  ❌ ${e.stack || e}`); process.exit(2); });
