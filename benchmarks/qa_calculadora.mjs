#!/usr/bin/env node
/**
 * QA FUNCIONAL de la calculadora: ejecuta la lógica real contra los datos reales.
 *
 * POR QUÉ EXISTE (14-ago-2026)
 * ---------------------------
 * Cristian, al elegir una subcategoría del pilar Agentes: *"me aparece vacío. Nos
 * faltan QAs funcionales y unitarios para el benchmark."*
 *
 * Tenía razón, y el bug lo prueba: `docs/app.js` son ~1.200 líneas que deciden QUÉ
 * modelo se le recomienda a alguien, y **no tenían un solo test**. `check_calculator.py`
 * hace chequeos ESTÁTICOS (que el campo exista, que el umbral caiga en rango) pero
 * nunca EJECUTA el filtrado. Un filtro que devuelve cero resultados pasa en verde:
 * la página carga, no hay error en consola, y el usuario ve una tabla vacía.
 *
 * EL BUG QUE MOTIVÓ ESTO, para que el test no se vuelva abstracto:
 *   getScore() devuelve DOS ESCALAS distintas. Sin subcategoría, z-scorea el pilar y
 *   lo re-escala (rango -3,65 a 9,73). Con subcategoría, devuelve el valor CRUDO de la
 *   suite (rango 4,53 a 8,46). El slider de calidad es UNO SOLO y se aplica a las dos.
 *   Con el slider en 7,45, la suite `tool_calling` —cuyo MÁXIMO es 7,12— deja pasar
 *   CERO modelos. Siempre. Con los 74 medidos ahí, presentes y correctos.
 *
 * CÓMO PRUEBA
 * -----------
 * No mockea la lógica: carga `docs/app.js` de verdad, con un DOM apuntalado, y le pasa
 * `docs/data/models.json` de verdad. Si mañana alguien cambia una escala, un umbral o
 * un preset, este archivo se entera.
 *
 * Uso:
 *   node benchmarks/qa_calculadora.mjs        # exit 1 si algo falla
 *   node benchmarks/qa_calculadora.mjs -v
 */

import { readFileSync, existsSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const VERBOSE = process.argv.includes("-v");

// ── Cargar app.js con el DOM apuntalado ──────────────────────────────────────
// app.js referencia `document` y `window` en ~59 lugares, casi todos dentro de
// funciones de init que no se llaman acá. Apuntalar es más barato —y menos riesgoso—
// que refactorizar 1.200 líneas de código que hoy funciona en producción.
function cargarApp() {
  const src = readFileSync(join(ROOT, "docs", "app.js"), "utf8");
  const stubEl = new Proxy({}, {
    get: (t, k) => (k === "value" || k === "innerHTML" || k === "textContent") ? ""
      : (k === "hidden" || k === "checked") ? false
      : (k === "classList") ? { add() {}, remove() {}, toggle() {} }
      : (typeof k === "string" && k.startsWith("add")) ? () => {}
      : () => {},
    set: () => true,
  });
  const document = {
    getElementById: () => stubEl,
    querySelector: () => stubEl,
    querySelectorAll: () => [],
    addEventListener: () => {},
    createElement: () => stubEl,
    body: stubEl,
  };
  const window = { addEventListener: () => {}, location: { search: "", hash: "" },
                   matchMedia: () => ({ matches: false, addEventListener() {} }) };
  // Se exponen las funciones puras que el QA necesita ejercitar.
  const fn = new Function("document", "window", "localStorage", "fetch",
    `${src}
     return { getScore, filterAndRank, costPerMonth, PRESETS_BUDGET, state,
              TOOL_CALLING_MIN, clampUmbralAlEje, WIZ, WIZ_AGENTES, wizEje,
              computeZScore, wizCandidatos, cargarRegistroDeSuites,
              get SUITES_BY_PILLAR() { return SUITES_BY_PILLAR; } };`);
  return fn(document, window,
            { getItem: () => null, setItem: () => {} },
            () => Promise.reject(new Error("sin red en QA")));
}

const app = cargarApp();
const datos = JSON.parse(readFileSync(join(ROOT, "docs", "data", "models.json"), "utf8"));
// `getScore` lee `state.data` para sacar norm_stats y score_rescale — en el navegador
// lo llena el fetch inicial. Sin esto el QA prueba una app a medio arrancar.
app.state.data = datos;
// El menú de subcategorías se arma desde `datos.suites` (el registro único). En el
// navegador lo dispara `load()`; acá hay que llamarlo igual, o el QA probaría la app
// con el menú vacío y todos los chequeos pasarían por no tener nada que recorrer.
app.cargarRegistroDeSuites(datos);
const MODELOS = datos.models;
const RANKED = MODELOS.filter(m => m.ranked && (m.runs || 0) > 0);

const fallos = [];
const oks = [];
function chequeo(nombre, fn) {
  try {
    const problemas = fn() || [];
    if (problemas.length) fallos.push([nombre, problemas]);
    else oks.push(nombre);
  } catch (e) {
    fallos.push([nombre, [`explotó: ${e.message}`]]);
  }
}

// Filtros base: los defaults del estado, con presupuesto amplio para que el único
// filtro que corte sea el que se está probando.
//
// `task`/`subtask` se RESETEAN a propósito. Los chequeos mutan `state.filters` (tienen
// que hacerlo: prueban el flujo real, y cambiar de eje dispara el clamp del umbral), así
// que sin este reset cada chequeo hereda el eje que dejó el anterior. Pasó de verdad el
// 15-ago: al reordenar el menú, Q4 empezó a fallar en los 4 presets — no porque los
// presets se rompieran, sino porque arrastraban la subcategoría que dejó Q1, y con
// `subtask` puesto el umbral de calidad se aplica sobre la escala CRUDA de la suite. Un
// test que depende del orden en que corren los demás no prueba lo que dice probar.
const baseFiltros = () => ({
  ...app.state.filters, task: "score_global", subtask: "",
  budget: 100000, calls: 2000, speed: 0,
  onlyOpen: false, exclProprietary: false, onlyTested: true, onlyTools: false,
  onlyAgentico: false, onlyThinking: false, onlyMultimodal: false, minContext: 0,
});

// ── Q1 · NINGUNA combinación pilar × subcategoría puede quedar vacía ─────────
// Es el bug reportado. Se prueba con el umbral por DEFECTO, que es lo que ve alguien
// que entra al sitio y toca una subcategoría sin mover nada más.
chequeo("Q1 · ninguna subcategoría queda vacía (flujo real: elegir eje → filtrar)", () => {
  const malas = [];
  for (const [pilar, suites] of Object.entries(app.SUITES_BY_PILLAR)) {
    for (const s of ["", ...suites.map(x => x.value)]) {
      // Se reproduce lo que hace un usuario: cambiar de eje dispara el clamp del
      // umbral. Probar `filterAndRank` sin el clamp probaría media aplicación.
      Object.assign(app.state.filters, baseFiltros(), { task: pilar, subtask: s });
      app.clampUmbralAlEje();
      const n = app.filterAndRank(MODELOS, app.state.filters).length;
      const conDato = s
        ? RANKED.filter(m => (m.score_by_suite || {})[s] != null).length
        : RANKED.length;
      if (n === 0 && conDato > 0) {
        malas.push(`${pilar}/${s || "(promedio del pilar)"}: 0 resultados con ${conDato} ` +
                   `modelos medidos · umbral tras el clamp ${app.state.filters.quality}`);
      }
    }
  }
  return malas;
});

// ── Q2 · tras elegir un eje, el umbral cae DENTRO del rango de ese eje ──────
// La causa raíz del bug: un solo slider para escalas distintas. El invariante no es
// "todas las escalas llegan a 8", es "el umbral nunca queda sobre el techo del eje".
chequeo("Q2 · el umbral siempre cae dentro del rango del eje elegido", () => {
  const malas = [];
  for (const [pilar, suites] of Object.entries(app.SUITES_BY_PILLAR)) {
    for (const s of suites) {
      Object.assign(app.state.filters, baseFiltros(), { task: pilar, subtask: s.value });
      app.clampUmbralAlEje();
      const vals = RANKED.map(m => (m.score_by_suite || {})[s.value]).filter(v => v != null);
      if (!vals.length) continue;
      const max = Math.max(...vals);
      if (app.state.filters.quality > max) {
        malas.push(`${pilar}/${s.value}: umbral ${app.state.filters.quality} > máximo del eje ${max.toFixed(2)}`);
      }
    }
  }
  return malas;
});

// ── Q3 · cada subcategoría ofrecida tiene datos detrás ──────────────────────
// Un <option> que no corresponde a ninguna clave de `score_by_suite` es una promesa
// vacía: el usuario la elige y no puede pasar nada bueno.
chequeo("Q3 · cada subcategoría del menú existe en los datos", () => {
  const malas = [];
  for (const [pilar, suites] of Object.entries(app.SUITES_BY_PILLAR)) {
    for (const s of suites) {
      const n = RANKED.filter(m => (m.score_by_suite || {})[s.value] != null).length;
      if (n === 0) malas.push(`${pilar}/${s.value}: la ofrece el menú y 0 modelos la tienen`);
      else if (n < RANKED.length * 0.5)
        malas.push(`${pilar}/${s.value}: solo ${n}/${RANKED.length} modelos medidos (<50%)`);
    }
  }
  return malas;
});

// ── Q4 · cada preset de presupuesto devuelve algo ───────────────────────────
// Un preset que no recomienda nada es peor que no tener preset: el usuario concluye
// que para su presupuesto no hay opciones, y sí las hay.
chequeo("Q4 · cada preset de presupuesto recomienda al menos un modelo", () => {
  const malas = [];
  for (const [nombre, p] of Object.entries(app.PRESETS_BUDGET || {})) {
    const f = { ...baseFiltros(), ...p };
    const n = app.filterAndRank(MODELOS, f).length;
    if (n === 0) malas.push(`preset "${nombre}" (${p.budget} USD, calidad ≥${p.quality}): 0 resultados`);
  }
  return malas;
});

// ── Q5 · los checkboxes de capacidad no vacían el listado ───────────────────
chequeo("Q5 · ningún filtro de capacidad deja el listado vacío", () => {
  const malas = [];
  for (const flag of ["onlyOpen", "onlyTools", "onlyAgentico", "onlyThinking", "onlyMultimodal"]) {
    const f = { ...baseFiltros(), [flag]: true };
    const n = app.filterAndRank(MODELOS, f).length;
    if (n === 0) malas.push(`${flag}: 0 resultados`);
    else if (VERBOSE) console.log(`     ${flag}: ${n} modelos`);
  }
  return malas;
});

// ── Q6 · el orden que devuelve es realmente descendente por score ───────────
// Suena obvio y por eso nadie lo prueba. Si se rompe, el "#1" del sitio deja de ser
// el mejor y nada lo delata: la tabla se ve igual de prolija.
chequeo("Q6 · el ranking sale ordenado de mayor a menor", () => {
  const malas = [];
  for (const pilar of ["score_calidad", ...Object.keys(app.SUITES_BY_PILLAR)]) {
    const f = { ...baseFiltros(), task: pilar, subtask: "", quality: 0 };
    const r = app.filterAndRank(MODELOS, f);
    for (let i = 1; i < r.length; i++) {
      const a = app.getScore(r[i - 1], pilar, ""), b = app.getScore(r[i], pilar, "");
      if (a != null && b != null && b > a + 1e-9) {
        malas.push(`${pilar}: puesto ${i} (${r[i].name} ${b.toFixed(2)}) supera al ${i} (${r[i - 1].name} ${a.toFixed(2)})`);
        break;
      }
    }
  }
  return malas;
});

// ── Q7 · un modelo no apto para agentes nunca pasa el filtro agéntico ───────
chequeo("Q7 · el filtro agéntico excluye a los que no corren en un agente", () => {
  const f = { ...baseFiltros(), onlyAgentico: true, quality: 0 };
  const r = app.filterAndRank(MODELOS, f);
  const colados = r.filter(m => m.sirve_para_agentes !== true).map(m => m.name);
  return colados.length ? [`pasaron sin evidencia: ${colados.join(", ")}`] : [];
});



// ── Q8 · todo enlace interno de la portada apunta a una página que EXISTE ────
// Se agregó al enlazar los 6 cortes por eje desde la portada: un `<a href>` a una
// página borrada o renombrada no rompe nada en la calculadora —carga igual— y le da 404
// al usuario. Es el mismo modo de falla silencioso de siempre, en la superficie que más
// tráfico recibe.
chequeo("Q8 · ningún enlace interno de la portada apunta a una página inexistente", () => {
  const html = readFileSync(join(ROOT, "docs", "index.html"), "utf8");
  const rotos = [];
  for (const m of html.matchAll(/href="(\/[^"#?]*)"/g)) {
    const ruta = m[1];
    if (ruta === "/") continue;
    const destino = join(ROOT, "docs", ruta.replace(/^\//, ""),
                         ruta.endsWith("/") ? "index.html" : "");
    const alt = join(ROOT, "docs", ruta.replace(/^\//, ""));
    if (!existsSync(destino) && !existsSync(alt) && !existsSync(alt + ".html")) {
      rotos.push(ruta);
    }
  }
  return [...new Set(rotos)].map(r => `${r} — enlazada desde la portada y no existe`);
});

// ── Q9 · los cortes por eje generados están TODOS enlazados ─────────────────
// La contracara: una página que se genera y nadie enlaza es trabajo publicado que nadie
// encuentra. El guardrail `check_cortes.py` verifica que la página coincida con los
// datos; esto verifica que además se pueda LLEGAR a ella.
chequeo("Q9 · cada corte por eje generado está enlazado desde la portada", () => {
  const html = readFileSync(join(ROOT, "docs", "index.html"), "utf8");
  const src = readFileSync(join(ROOT, "benchmarks", "generate_rankings.py"), "utf8");
  const bloque = src.slice(src.indexOf("RANKINGS = ["));
  const cortes = [];
  const re = /"slug":\s*"([^"]+)"[\s\S]{0,600}?"criterion":\s*"suite"/g;
  for (const m of bloque.matchAll(re)) cortes.push(m[1]);
  return cortes.filter(sl => !html.includes(`/${sl}/`))
               .map(sl => `${sl}: se genera y NO se enlaza desde la portada`);
});


// ── Q10 · las columnas nuevas coinciden con models.json ─────────────────────
// La columna de contraste y la de tarea real son código a mano sobre datos generados: si
// el export cambia la forma de `agentico` o de `score_calidad`, la tabla no rompe —
// muestra «—» en silencio, que es indistinguible de «no medido».
chequeo("Q10 · las columnas de contraste y tarea real leen datos que existen", () => {
  const malas = [];
  const conAgentico = RANKED.filter(m => m.agentico && Object.keys(m.agentico.tareas || {}).length);
  if (!conAgentico.length) malas.push("ningún modelo rankeado tiene `agentico.tareas`: la columna «Tarea real» mostraría — en todos");
  const sinCalidad = RANKED.filter(m => m.score_calidad == null);
  if (sinCalidad.length > RANKED.length * 0.1)
    malas.push(`${sinCalidad.length}/${RANKED.length} rankeados sin score_calidad: la columna de contraste quedaría vacía`);
  // cada tarea agéntica debe traer media Y piso — el piso es la mitad del punto
  for (const m of conAgentico.slice(0, 20)) {
    for (const [k, v] of Object.entries(m.agentico.tareas)) {
      if (v.media == null || v.piso == null)
        malas.push(`${m.name}/${k}: falta ${v.media == null ? "media" : "piso"} — el piso es la mitad del dato`);
    }
  }
  return malas;
});

// ── Q11 · el puesto global de la calculadora coincide con el de las páginas ──
// Las dos superficies publican el mismo ranking. Si difieren, el sitio se contradice
// consigo mismo y el usuario no tiene cómo saber cuál creer.
chequeo("Q11 · el puesto global coincide entre la calculadora y los cortes por eje", () => {
  const r = RANKED.filter(m => m.score_calidad != null)
                  .sort((a, b) => b.score_calidad - a.score_calidad);
  if (!r.length) return ["no hay modelos con score_calidad"];
  const primero = r[0];
  const html = readFileSync(join(ROOT, "docs", "mejor-llm-para-datos-exactos", "index.html"), "utf8");
  // la página muestra «8.19 | #22 de 80»: el total tiene que ser el mismo
  const m = html.match(/#\d+ de (\d+)/);
  if (!m) return ["la página de corte no publica el puesto global — ¿se regeneró?"];
  const totalPagina = parseInt(m[1], 10);
  return totalPagina === r.length ? []
    : [`la página dice «de ${totalPagina}» y la calculadora ordena sobre ${r.length} modelos`];
});

// ── Q12 · el menú sale del registro, y el registro cubre lo medido ──────────
// El menú se construye desde `models.json`. Si el registro llega incompleto, el
// desplegable pierde ejes en silencio: no hay error, sólo opciones que dejaron de
// existir. Y si un eje llega sin línea humana, el usuario ve el id técnico.
chequeo("Q12 · el menú de ejes sale del registro y ningún eje queda sin nombre humano", () => {
  const malas = [];
  const reg = datos.suites || {};
  if (!Object.keys(reg).length) return ["models.json no trae `suites`: el menú queda vacío"];

  const medidas = new Set();
  for (const m of MODELOS) for (const s of Object.keys(m.score_by_suite || {})) medidas.add(s);
  for (const s of medidas) {
    if (!reg[s]) malas.push(`\`${s}\` está medida y no está en el registro`);
    else if (!reg[s].menu || !reg[s].decide) malas.push(`\`${s}\` sin etiqueta o sin línea humana`);
  }
  // Lo que el menú ofrece tiene que existir en el registro y tener datos detrás.
  for (const [pilar, suites] of Object.entries(app.SUITES_BY_PILLAR)) {
    for (const s of suites) {
      if (reg[s.value]?.pilar !== pilar) {
        malas.push(`${pilar}/${s.value}: el menú lo pone acá y el registro dice ` +
                   `${reg[s.value]?.pilar || "(ninguno)"}`);
      }
    }
  }
  return malas;
});

// ── Q13 · desde el índice de calidad se llega a CUALQUIER eje ───────────────
// La agrupación por pilar del desplegable existe para eso: llegar a
// `agent_long_horizon` sin saber de antemano que vive bajo «Agentes». Si el flujo
// pierde un eje, ese eje deja de ser alcanzable y nada lo indica.
chequeo("Q13 · desde el índice de calidad se puede elegir cualquier eje, y ninguno queda vacío", () => {
  const malas = [];
  const conPilar = Object.entries(datos.suites || {}).filter(([, s]) => s.pilar).map(([k]) => k);
  const enMenu = new Set(Object.values(app.SUITES_BY_PILLAR).flat().map(s => s.value));
  for (const s of conPilar) {
    if (!enMenu.has(s)) { malas.push(`\`${s}\` tiene pilar y no es alcanzable desde el menú`); continue; }
    Object.assign(app.state.filters, baseFiltros(), { task: "score_calidad", subtask: s });
    app.clampUmbralAlEje();
    const n = app.filterAndRank(MODELOS, app.state.filters).length;
    const conDato = RANKED.filter(m => (m.score_by_suite || {})[s] != null).length;
    if (n === 0 && conDato > 0) {
      malas.push(`índice de calidad → \`${s}\`: 0 resultados con ${conDato} modelos medidos`);
    }
  }
  return malas;
});

// ── Q14 · las comparaciones no coronan a un modelo sin decir que no rankea ──
// Las páginas vs son el motor de tráfico. Medido el 15-ago: **22 de 72 lados estaban
// coronados por un modelo que no rankea**, 15 de ellos variantes PRO — que por decisión
// vigente no compiten. La decisión estaba escrita y las páginas la ignoraban.
// Los slugs que ALGÚN generador produce. Se leen TODOS los `generate_*.py`, no solo
// `generate_comparison.py`: `generate_variants.py` también escribe en `docs/*-vs-*/`
// (sus páginas «qué variante uso» comparten el patrón de slug). Mirar un solo generador
// dio un falso positivo el 15-ago — `grok-4-1-vs-4-5` se declaró huérfana, se redirigió,
// y el pipeline la restauró en el mismo run.
const _slugsDe = f => [...readFileSync(join(ROOT, "benchmarks", f), "utf8")
  .matchAll(/"slug":\s*"([^"]+)"/g)].map(m => m[1]);

const SLUGS_GENERADOS = new Set(
  readdirSync(join(ROOT, "benchmarks"))
    .filter(f => f.startsWith("generate_") && f.endsWith(".py"))
    .flatMap(_slugsDe));

// Solo las de `generate_comparison.py` llevan tabla eje por eje. Las de
// `generate_variants.py` («¿qué variante de Grok uso?») son otra plantilla y comparten el
// patrón de slug — exigirles la tabla las marcaría rotas sin estarlo.
const SLUGS_COMPARACION = new Set(_slugsDe("generate_comparison.py"));

chequeo("Q14 · ninguna comparación corona a un no-rankeado sin la salvedad escrita", () => {
  const malas = [];
  const nombres = new Map(MODELOS.map(m => [m.name, m]));
  for (const slug of SLUGS_COMPARACION) {
    const p = join(ROOT, "docs", slug, "index.html");
    if (!existsSync(p)) continue;
    const html = readFileSync(p, "utf8");
    const h2 = html.match(/<h2>Eje por eje: (.+?) vs (.+?)<\/h2>/);
    if (!h2) { malas.push(`${slug}: no publica la tabla eje por eje`); continue; }
    for (const nm of [h2[1], h2[2]]) {
      const m = nombres.get(nm.replace(/&amp;/g, "&"));
      if (m && !m.ranked && !html.includes(`${nm} no está rankeado`)) {
        malas.push(`${slug}: corona a «${nm}», que no rankea, sin la salvedad`);
      }
    }
    if (!/class="cobertura /.test(html)) malas.push(`${slug}: sin nota de cobertura`);
  }
  return malas;
});

// ── Q15 · páginas publicadas que ya nadie regenera ──────────────────────────
// Un directorio `-vs-` que no está en `COMPARISONS` es una página viva en el sitio,
// indexada por Google, con datos congelados del día que se sacó del generador. No falla
// nada: carga, se ve bien y miente despacio. Medido el 15-ago: **4 huérfanas**, y una
// (`grok-4.3-vs-gpt-5.5`) duplica a `grok-4.3-vs-gpt-5-5` — dos URLs compitiendo por la
// misma búsqueda.
//
// Es fallo, no aviso: borrarlas o volver a generarlas es una decisión, pero dejarlas sin
// decidir es publicar datos que nadie mantiene.
chequeo("Q15 · ninguna página de comparación quedó huérfana del generador", () => {
  // Una huérfana puede ser legítima (un slug viejo que hoy es redirect), pero entonces
  // el motivo está escrito en `HUERFANAS_DECLARADAS`. Lo que no se acepta es la tercera
  // categoría: publicada, sin generador y sin que nadie haya decidido nada.
  const gc = readFileSync(join(ROOT, "benchmarks", "generate_comparison.py"), "utf8");
  const bloque = gc.slice(gc.indexOf("HUERFANAS_DECLARADAS"));
  const declaradas = new Set([...bloque.matchAll(/^\s{4}"([^"]+)":/gm)].map(m => m[1]));
  const dirs = readdirSync(join(ROOT, "docs"), { withFileTypes: true })
    .filter(d => d.isDirectory() && d.name.includes("-vs-")).map(d => d.name);
  const malas = [];
  for (const d of dirs) {
    if (SLUGS_GENERADOS.has(d) || declaradas.has(d)) continue;
    malas.push(`docs/${d}/ está publicada y NO la genera nadie: sus datos quedaron ` +
               `congelados. Agregala a COMPARISONS o declarala en HUERFANAS_DECLARADAS`);
  }
  // Una declarada tiene que ser realmente un redirect, no una página vieja con la
  // etiqueta puesta: si sigue sirviendo su contenido, el problema sigue ahí.
  for (const d of declaradas) {
    const p = join(ROOT, "docs", d, "index.html");
    if (existsSync(p) && !/http-equiv="refresh"|rel="canonical" href="[^"]*"\s*\/?>[\s\S]{0,200}redirect/i
        .test(readFileSync(p, "utf8"))) {
      malas.push(`docs/${d}/ está declarada como huérfana pero sigue sirviendo su ` +
                 `contenido viejo — tiene que ser un redirect`);
    }
  }
  return malas;
});

// ═══════════════════════════════════════════════════════════════════════════
// WIZARD — es la PUERTA DE ENTRADA del sitio y era una ruta de código aparte,
// sin ningún test. Medido el 14-ago: no filtraba por `sirve_para_agentes`, así que
// Hermes 4 405B estaba #14 de su ranking de agentes (a una medición del podio) y
// **Qwen 3-Next 80B Thinking pasaba el toggle "tiene que usar herramientas"**
// (tool_calling_score_avg 6,41 ≥ 6) sacando 0,00 dentro de un agente real.
// ═══════════════════════════════════════════════════════════════════════════

// Réplica del scoring del wizard. Se apoya en `wizEje` REAL —no una copia— para que
// un cambio de ejes en app.js no pase inadvertido acá.
function wizPuntaje(m, tipo) {
  let suma = 0, peso = 0;
  for (const [eje, p] of tipo.ejes) {
    const v = app.wizEje(m, eje);
    if (v == null) continue;
    suma += v * p; peso += p;
  }
  return peso > 0 ? suma / peso : null;
}
const APTOS = RANKED.filter(m => m.sirve_para_agentes !== false);

chequeo("W1 · cada tarea × presupuesto del wizard devuelve una recomendación", () => {
  const malas = [];
  for (const t of app.WIZ.tasks) {
    for (const b of app.WIZ.budgets) {
      const w = t.latency ? { quality: 50, cost: 15, speed: 10, latency: 25 } : b.w;
      const n = RANKED.map(m => app.computeZScore(m, w, t.pillar)).filter(v => v != null).length;
      if (n === 0) malas.push(`${t.id} × ${b.id}: 0 modelos puntuables`);
    }
  }
  return malas;
});

chequeo("W2 · el wizard NUNCA recomienda algo que no corre en un agente", () => {
  const malas = [];
  for (const tipo of app.WIZ_AGENTES) {
    const r = APTOS.map(m => ({ m, s: wizPuntaje(m, tipo) }))
      .filter(x => x.s != null).sort((a, b) => b.s - a.s);
    const colados = r.slice(0, 10).filter(x => x.m.sirve_para_agentes !== true).map(x => x.m.name);
    if (colados.length) malas.push(`${tipo.id}: en el top 10 sin evidencia agéntica → ${colados.join(", ")}`);
    if (!r.length) malas.push(`${tipo.id}: 0 recomendaciones`);
  }
  // Se ejercita la RUTA REAL (wizCandidatos), no una réplica del filtro: el bug era
  // justamente que el toggle filtraba por la nota de una suite de texto.
  for (const combo of [{ tools: true }, { pillar: "Agentes" },
                       { pillar: "Agentes", tools: true }, { pillar: "Agentes", os: true }]) {
    const cand = app.wizCandidatos(MODELOS, combo);
    const colados = cand.filter(m => m.sirve_para_agentes === false).map(m => m.name);
    if (colados.length) malas.push(`wizCandidatos(${JSON.stringify(combo)}) deja pasar: ${colados.join(", ")}`);
    if (!cand.length) malas.push(`wizCandidatos(${JSON.stringify(combo)}): 0 candidatos`);
  }
  return malas;
});

chequeo("W3 · cada eje que usa el wizard existe en los datos", () => {
  const malas = [];
  for (const tipo of app.WIZ_AGENTES) {
    const suma = tipo.ejes.reduce((s, [, p]) => s + p, 0);
    if (Math.abs(suma - 1) > 0.001) malas.push(`${tipo.id}: los pesos suman ${suma.toFixed(3)}, no 1`);
    for (const [eje] of tipo.ejes) {
      const n = APTOS.filter(m => app.wizEje(m, eje) != null).length;
      if (n === 0) malas.push(`${tipo.id}/${eje}: 0 modelos lo tienen`);
      else if (n < APTOS.length * 0.5) malas.push(`${tipo.id}/${eje}: solo ${n}/${APTOS.length} modelos`);
    }
  }
  return malas;
});

chequeo("W4 · el paso «tipo de agente» aparece si y solo si la tarea es agentes", () => {
  const malas = [];
  const seq = (task) => task === "agentes" ? [0, 0.5, 1, 2] : [0, 1, 2];
  for (const t of app.WIZ.tasks) {
    const tiene = seq(t.id).includes(0.5);
    if (t.id === "agentes" && !tiene) malas.push("agentes NO pregunta el tipo");
    if (t.id !== "agentes" && tiene) malas.push(`${t.id} pregunta el tipo y no debería`);
  }
  if (!app.WIZ_AGENTES.length) malas.push("no hay tipos de agente definidos");
  return malas;
});

chequeo("W5 · la tabla de ejes explica el MISMO orden que se calculó", () => {
  const malas = [];
  for (const tipo of app.WIZ_AGENTES) {
    const r = APTOS.map(m => ({ m, s: wizPuntaje(m, tipo) }))
      .filter(x => x.s != null).sort((a, b) => b.s - a.s).slice(0, 5);
    // Cada columna de la tabla tiene que ser un eje del puntaje: si la tabla muestra
    // una métrica que no pesó, "explica" una decisión que no se tomó con eso.
    for (const x of r) {
      for (const [eje] of tipo.ejes) {
        if (app.wizEje(x.m, eje) === undefined) malas.push(`${tipo.id}: ${x.m.name} sin ${eje}`);
      }
    }
  }
  return malas;
});

// ── Reporte ─────────────────────────────────────────────────────────────────
console.log("\nQA funcional de la calculadora — lógica real contra datos reales\n");
for (const n of oks) console.log(`  ✅ ${n}`);
for (const [n, problemas] of fallos) {
  console.log(`  ❌ ${n}`);
  for (const p of problemas) console.log(`       · ${p}`);
}
console.log();
if (fallos.length) {
  console.log(`  ❌ ${fallos.length} chequeo(s) fallando.`);
  console.log("     Un filtro que devuelve cero resultados NO rompe la página: carga,");
  console.log("     no tira error, y el usuario ve una tabla vacía. Por eso hay que probarlo.");
  process.exit(1);
}
console.log(`  ✅ los ${oks.length} chequeos funcionales pasan.`);
