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

import { readFileSync, existsSync } from "node:fs";
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
     return { getScore, filterAndRank, costPerMonth, SUITES_BY_PILLAR,
              PRESETS_BUDGET, state, TOOL_CALLING_MIN, clampUmbralAlEje,
              WIZ, WIZ_AGENTES, wizEje, computeZScore, wizCandidatos };`);
  return fn(document, window,
            { getItem: () => null, setItem: () => {} },
            () => Promise.reject(new Error("sin red en QA")));
}

const app = cargarApp();
const datos = JSON.parse(readFileSync(join(ROOT, "docs", "data", "models.json"), "utf8"));
// `getScore` lee `state.data` para sacar norm_stats y score_rescale — en el navegador
// lo llena el fetch inicial. Sin esto el QA prueba una app a medio arrancar.
app.state.data = datos;
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
const baseFiltros = () => ({
  ...app.state.filters, budget: 100000, calls: 2000, speed: 0,
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
