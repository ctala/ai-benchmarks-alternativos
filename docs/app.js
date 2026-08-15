// Calculadora de modelos IA — Cristian Tala
// Lee docs/data/models.json y aplica filtros con sliders

const TOKENS_IN = 300;
const TOKENS_OUT = 1500;

// Sub-categorías (suites) por pilar — sincronizado con SUITE_TO_PILLAR del export.
// Las labels son user-facing en español neutro.
const SUITES_BY_PILLAR = {
  Razonamiento: [
    { value: "reasoning", label: "Razonamiento general (lógica, decisiones)" },
    { value: "deep_reasoning", label: "Razonamiento profundo (matemática, Fermi)" },
    { value: "hallucination", label: "Anti-hallucination (citas, contexto)" },
    { value: "customer_support", label: "Soporte al cliente (clasificación)" },
  ],
  Coding: [
    { value: "code_generation", label: "Generación de código (Python, SQL, debug)" },
    { value: "structured_output", label: "JSON estructurado (extracción, schemas)" },
    { value: "string_precision", label: "Precisión strings (hex, JWT, configs)" },
  ],
  Contenido: [
    { value: "content_generation", label: "Contenido genérico (blog, email, social)" },
    { value: "creativity", label: "Creatividad (hooks, analogías, narrativa)" },
    { value: "startup_content", label: "Contenido startup (newsletter, blog actualidad)" },
    { value: "summarization", label: "Resúmenes y extracción de datos" },
    { value: "presentation", label: "Presentaciones (slides, reportes)" },
    { value: "task_management", label: "Gestión de tareas (action items, plans)" },
    { value: "translation", label: "Traducción (es↔en, problemas idioma)" },
    { value: "news_seo_writing", label: "News + SEO (artículos completos)" },
    { value: "sales_outreach", label: "Sales outreach (cold email, campañas)" },
    { value: "strategy", label: "Estrategia (pricing, planning)" },
    { value: "ocr_extraction", label: "OCR / extracción de imágenes" },
  ],
  Agentes: [
    { value: "agent_long_horizon", label: "Tareas largas (sostener el hilo 8-12 turnos)" },
    { value: "tool_calling_adversarial", label: "No inventar herramientas (abstenerse cuando no hay)" },
    { value: "tool_calling", label: "Tool calling (function calls)" },
    { value: "orchestration", label: "Orquestación (workflows complejos)" },
    { value: "multi_turn", label: "Multi-turn (debugging, requirements)" },
    { value: "agent_capabilities", label: "Capacidades agente (delegación, skills)" },
    { value: "policy_adherence", label: "Policy adherence (límites, idioma)" },
  ],
};

// Presets de presupuesto — calibrados para emprendedores hispanohablantes.
// Cada preset configura los 4 sliders de filtros + tarea principal.
// Umbral de tool calling para el filtro "sirve para agentes". 6,0 sobre la nota MEDIDA,
// no sobre el flag de capacidad declarada (que declaran los 82 y por eso no filtraba nada).
const TOOL_CALLING_MIN = 6.0;

const PRESETS_BUDGET = {
  personal: {
    budget: 5,
    calls: 300,        // ~10 calls/día
    quality: 7.8,      // aceptable para chat personal (escala absoluta)
    speed: 0,
    task: "score_calidad",
  },
  solopreneur: {
    budget: 25,
    calls: 3000,       // ~100 calls/día (1-2 agentes N8N pequeños)
    quality: 8.0,
    speed: 0,
    task: "score_calidad",
  },
  pyme: {
    budget: 100,
    calls: 30000,      // ~1000 calls/día (varios workflows en paralelo)
    quality: 8.2,      // calidad relevante para producto (escala absoluta: 36 de 82)
    speed: 50,         // latencia importa
    task: "score_calidad",
  },
  produccion: {
    budget: 500,
    calls: 300000,     // ~10K calls/día (tráfico de producto SaaS)
    quality: 8.2,
    speed: 100,        // alta velocidad crítica
    task: "score_calidad",
  },
};

// Presets por caso de uso — ajustan pesos del score y la tarea principal.
const PRESETS_USE_CASE = {
  calidad: {
    label: "Calidad sobre todo",
    weights: { quality: 90, cost: 5, speed: 2.5, latency: 2.5 },
    task: "score_calidad",
    quality: 8.4,   // "calidad sobre todo": solo el cuartil alto
  },
  barato_rapido: {
    label: "Barato y rápido",
    weights: { quality: 40, cost: 35, speed: 15, latency: 10 },
    task: "score_calidad",
    quality: 7.8,   // "barato y rápido": la calidad cede, pero con piso real
  },
  chat_vivo: {
    label: "Chat en vivo (baja latencia)",
    weights: { quality: 50, cost: 15, speed: 10, latency: 25 },
    task: "score_calidad",
    quality: 8.2,
    speed: 100,
  },
  coding: {
    label: "Coding",
    weights: { quality: 70, cost: 15, speed: 7.5, latency: 7.5 },
    task: "Coding",
    quality: 8.4,
  },
  contenido: {
    label: "Contenido / Marketing",
    weights: { quality: 70, cost: 15, speed: 7.5, latency: 7.5 },
    task: "Contenido",
    quality: 8.4,
  },
  agentes: {
    label: "Agentes / Tools",
    weights: { quality: 70, cost: 15, speed: 7.5, latency: 7.5 },
    task: "Agentes",
    quality: 8.2,
  },
  razonamiento: {
    label: "Razonamiento profundo",
    weights: { quality: 90, cost: 5, speed: 2.5, latency: 2.5 },
    task: "Razonamiento",
    quality: 8.4,
  },
};

const PROPRIETARY_GROUPS = {
  anthropic: m => m.id?.includes("anthropic/") || m.id?.startsWith("claude"),
  openai: m => m.id?.startsWith("gpt-") || m.id?.startsWith("openai/") || m.provider === "openai_direct" || m.provider === "openai_responses",
  // Google propietarios: Gemini Flash/Pro (NO Gemma open-source)
  google_proprietary: m => /gemini[-_/]/i.test(m.id || "") && !m.open_source,
};

// Opciones del filtro de contexto efectivo (NIAH-es mide retrieval real).
// "0" = sin restricción, resto = tokens mínimos de effective_context.
const CONTEXT_OPTIONS = [
  { value: "0",      label: "Cualquier contexto" },
  { value: "64000",  label: "≥64K tokens" },
  { value: "128000", label: "≥128K tokens" },
  { value: "256000", label: "≥256K tokens" },
  { value: "512000", label: "≥512K tokens" },
  { value: "800000", label: "≥800K tokens" },
];

const state = {
  data: null,
  filters: {
    budget: 500,        // Default para emprendedor con producto en producción
    calls: 2000,
    quality: 8.0,   // escala absoluta: deja pasar 58 de 82. Antes 6.5, que en
                    // la escala nueva no filtra a nadie (el peor mide 7,26).
    speed: 0,
    task: "score_calidad",
    subtask: "",  // suite específica (opcional). Vacío = promedio del pilar
    onlyOpen: false,
    exclProprietary: false,
    onlyTested: true,         // Default ON (3 jun 2026): muestra solo cobertura completa (≥50 runs).
                              // Evita que parciales/smoke-tests (ej. V4 Pro cloud 10 runs) confundan.
                              // Toggle "sólo cobertura completa" lo desactiva para ver parciales.
    onlyTools: false,         // Solo modelos con tool calling
    onlyAgentico: false,      // Solo los que completan una tarea real dentro de un agente
    onlyThinking: false,      // Solo thinking models
    onlyMultimodal: false,    // Solo multimodal (texto + imagen/audio)
    minContext: 0,            // Contexto efectivo mínimo (0 = sin restricción)
  },
  // Pesos del score global (v3.0 z-score). Siempre se normalizan a suma=1 antes de aplicar.
  // v3.0: quality sube a 70%, costo baja a 15%, speed/latency 7.5% cada uno.
  // tool_calling quedó en 0 — sigue como columna informativa pero no pondera el score.
  weights: { quality: 70, cost: 15, speed: 7.5, latency: 7.5 },
  // Sorting state — null usa el orden default (por _task_score desc)
  sort: { column: null, direction: "desc" },
};

async function load() {
  try {
    const res = await fetch("data/models.json", { cache: "no-store" });
    state.data = await res.json();
  } catch (e) {
    console.error("Error loading models.json", e);
    document.getElementById("results-summary").textContent =
      "Error cargando datos. Verifica que docs/data/models.json esté generado.";
    return;
  }
  // Hero stats — esfuerzo total de medición: TODOS los modelos catalogados y TODOS
  // los runs ejecutados (incluidos los descartados en la limpieza). El conocimiento
  // costó todas esas corridas, no solo las que quedaron rankeadas. Fallback al conteo
  // vivo si el export no trae los campos nuevos.
  const totalModels = state.data.total_models
    || state.data.models.filter(m => (m.runs || 0) > 0).length;
  const totalRuns = state.data.total_runs_measured
    || state.data.models.reduce((acc, m) => acc + (m.runs || 0), 0);
  document.getElementById("hero-runs").textContent = totalRuns.toLocaleString("es");
  document.getElementById("hero-models").textContent = totalModels;
  document.getElementById("hero-updated").textContent =
    state.data.generated_at?.replace("T", " ") || "—";

  // Structured data en sync con la data viva: dateModified + versión + conteos.
  // Señal de frescura para Google (sabe que la página se actualizó) y evita que el
  // schema caduque — todo dinámico desde models.json, nada hardcodeado que envejezca.
  syncStructuredData(state.data, totalModels, totalRuns);

  bindFilters();
  applyUrlContext();   // el usuario llega con un caso de uso ya declarado: respetarlo
  bindAnalytics();
  render();
  wizInit();           // wizard guiado (usa state.data + computeZScore)
}

// Eventos del funnel en la calculadora. Sin esto no hay forma de saber si la
// herramienta se usa o solo se mira: había 0 analytics en las 57 páginas.
function bindAnalytics() {
  window.dataLayer = window.dataLayer || [];
  const push = (event, extra = {}) => window.dataLayer.push({ event, ...extra });

  // Llegó con contexto desde una página pSEO (?preset=…)
  const p = new URLSearchParams(location.search);
  if (p.get("preset")) {
    push("calculadora_con_contexto", { preset: p.get("preset"), calls: p.get("calls") || "" });
  }

  document.querySelectorAll(".preset-usecase-btn, .preset-budget-btn").forEach(btn => {
    btn.addEventListener("click", () => push("usa_preset", { preset: btn.dataset.preset }), { passive: true });
  });

  // Mover un peso = el usuario entendió que el score es opinable y lo está ajustando
  // a su caso. Es la señal más fuerte de intención que da esta herramienta.
  let weightSent = false;
  document.querySelectorAll('input[type="range"][id^="w-"]').forEach(sl => {
    sl.addEventListener("change", () => {
      if (weightSent) return;
      weightSent = true;
      push("ajusta_pesos");
    }, { passive: true });
  });

  document.addEventListener("click", (e) => {
    const a = e.target.closest?.("a");
    if (a && (a.getAttribute("href") || "").includes("skool.com")) {
      push("cta_comunidad", { cta_ubicacion: "calculadora" });
    }
  }, { passive: true });
}

// Lee ?preset= y ?calls= de la URL.
//
// Las páginas pSEO mandan al usuario acá con su caso de uso ("agentes", "coding")
// ya elegido. Antes el CTA era href="/" a secas y esto ni se leía: aterrizaba en
// "score global" con el presupuesto default y tenía que reconstruir a mano el caso
// que YA había declarado al hacer click. Ahora la calculadora abre configurada y
// scrolleada a los resultados.
function applyUrlContext() {
  const p = new URLSearchParams(location.search);
  const preset = p.get("preset");
  const calls = parseInt(p.get("calls"), 10);
  let applied = false;

  if (preset) {
    const btn = document.querySelector(`.preset-usecase-btn[data-preset="${CSS.escape(preset)}"]`)
             || document.querySelector(`.preset-budget-btn[data-preset="${CSS.escape(preset)}"]`);
    if (btn) { btn.click(); applied = true; }
  }
  if (Number.isFinite(calls) && calls > 0) {
    const el = document.getElementById("calls");
    if (el) {
      el.value = calls;
      el.dispatchEvent(new Event("input", { bubbles: true }));
      applied = true;
    }
  }
  if (applied) {
    // Sin esto el usuario clickea y "no pasa nada": la tabla se re-renderiza
    // fuera de pantalla, debajo de los filtros.
    requestAnimationFrame(() => {
      document.getElementById("results")?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }
}

// ============================================================
// Z-SCORE SCORING (v2.9)
// Computes a composite score using standardized (z-scored) dimensions
// so each weight truly represents influence, not variance dominance.
//
// Formula:
//   z(dim) = (model[col] - mean) / std       [from norm_stats in JSON]
//   z_comp = Σ w_dim * z(dim)                [weights normalized to sum=1]
//   score  = clamp(offset + slope * z_comp, 0, 10)  [from score_rescale in JSON]
//
// If any required dimension is missing, falls back to precomputed score_global.
// ============================================================

// Compone el score con los pesos del usuario.
//
// `pillar` (opcional): si viene, compone DENTRO de ese pilar usando las
// dimensiones crudas del pilar (dims_by_pillar) y sus norm_stats propias.
//
// Antes esto no existía y getScore() devolvía score_by_pillar, que viene
// pre-horneado con los pesos fijos 70/15/7.5/7.5. Resultado: al elegir un pilar
// los sliders del usuario se ignoraban en silencio — la UI movía los pesos y
// mostraba un ranking calculado con OTROS pesos. Con esto, "coding, y la
// latencia me da igual" por fin es expresable.
function computeZScore(model, weightsRaw, pillar) {
  const rs = state.data.score_rescale;
  if (!rs) return model.score_global;

  const ns = pillar
    ? (state.data.norm_stats_by_pillar || {})[pillar]
    : state.data.norm_stats;
  const src = pillar
    ? (model.dims_by_pillar || {})[pillar]
    : model;

  // Sin datos del pilar para este modelo → caemos al score pre-horneado.
  if (!ns || !src) return pillar ? (model.score_by_pillar?.[pillar] ?? null) : model.score_global;

  const dims = [
    { col: "quality_avg",       w: weightsRaw.quality  || 0 },
    { col: "cost_score_avg",    w: weightsRaw.cost     || 0 },
    { col: "speed_score_avg",   w: weightsRaw.speed    || 0 },
    { col: "latency_score_avg", w: weightsRaw.latency  || 0 },
  ];

  const fallback = pillar ? (model.score_by_pillar?.[pillar] ?? null) : model.score_global;
  for (const d of dims) {
    if (src[d.col] == null || !ns[d.col]) return fallback;
  }

  // Normalize weights to sum=1
  const total = dims.reduce((s, d) => s + d.w, 0);
  if (total <= 0) return fallback;

  let z_comp = 0;
  for (const d of dims) {
    const stat = ns[d.col];
    const z = (src[d.col] - stat.mean) / stat.std;
    z_comp += (d.w / total) * z;
  }

  const raw = rs.offset + rs.slope * z_comp;
  return Math.max(0, Math.min(10, raw));
}

function bindFilters() {
  const sliders = [
    ["budget", v => `$${v}`],
    ["calls", v => Number(v).toLocaleString()],
    ["quality", v => Number(v).toFixed(1)],
    ["speed", v => v],
  ];
  sliders.forEach(([id, fmt]) => {
    const el = document.getElementById(id);
    const out = document.getElementById(id + "-out");
    out.textContent = fmt(el.value);
    el.addEventListener("input", () => {
      state.filters[id] = parseFloat(el.value);
      out.textContent = fmt(el.value);
      render();
    });
  });

  // Weight sliders (solo aplican cuando task === "score_global")
  const weightSliders = ["w-quality", "w-cost", "w-speed", "w-latency"];
  const weightKeys    = ["quality",   "cost",   "speed",   "latency"];
  weightSliders.forEach((id, idx) => {
    const el  = document.getElementById(id);
    const out = document.getElementById(id + "-out");
    if (!el || !out) return;
    out.textContent = el.value + "%";
    el.addEventListener("input", () => {
      state.weights[weightKeys[idx]] = parseInt(el.value, 10);
      out.textContent = el.value + "%";
      updateWeightWarning();
      render();
    });
  });

  document.getElementById("task").addEventListener("change", e => {
    state.filters.task = e.target.value;
    state.filters.subtask = "";  // reset al cambiar pilar
    clampUmbralAlEje();
    updateSubtaskOptions();
    render();
  });

  document.getElementById("min-context").addEventListener("change", e => {
    state.filters.minContext = parseInt(e.target.value, 10) || 0;
    render();
  });

  document.getElementById("subtask").addEventListener("change", e => {
    state.filters.subtask = e.target.value;
    clampUmbralAlEje();
    render();
  });

  const checkboxMap = {
    onlyOpen: "only-open",
    exclProprietary: "excl-prop",
    onlyTested: "only-tested",
    onlyTools: "only-tools",
    onlyAgentico: "only-agentico",
    onlyThinking: "only-thinking",
    onlyMultimodal: "only-multimodal",
  };
  Object.entries(checkboxMap).forEach(([key, id]) => {
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener("change", e => {
      state.filters[key] = e.target.checked;
      render();
    });
  });

  // Presets de presupuesto
  document.querySelectorAll(".preset-budget-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const presetKey = btn.dataset.preset;
      const preset = PRESETS_BUDGET[presetKey];
      if (!preset) return;
      applyPresetValues(preset);
      markActive(btn, ".preset-budget-btn");
    });
  });

  // Presets por caso de uso
  document.querySelectorAll(".preset-usecase-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const presetKey = btn.dataset.preset;
      const preset = PRESETS_USE_CASE[presetKey];
      if (!preset) return;
      applyPresetValues(preset);
      // Aplicar pesos del score global
      if (preset.weights) {
        ["w-quality", "w-cost", "w-speed", "w-latency"].forEach((id, idx) => {
          const key = ["quality", "cost", "speed", "latency"][idx];
          const el = document.getElementById(id);
          const out = document.getElementById(id + "-out");
          if (el) {
            el.value = preset.weights[key];
            state.weights[key] = preset.weights[key];
          }
          if (out) out.textContent = preset.weights[key] + "%";
        });
        updateWeightWarning();
      }
      markActive(btn, ".preset-usecase-btn");
      render();
    });
  });

  function applyPresetValues(preset) {
    ["budget", "calls", "quality", "speed"].forEach(k => {
      if (preset[k] == null) return;
      const el = document.getElementById(k);
      const out = document.getElementById(k + "-out");
      if (!el) return;
      el.value = preset[k];
      state.filters[k] = preset[k];
      const formatters = {
        budget: v => `$${v}`,
        calls: v => Number(v).toLocaleString(),
        quality: v => Number(v).toFixed(1),
        speed: v => v,
      };
      if (out) out.textContent = formatters[k](preset[k]);
    });
    const taskEl = document.getElementById("task");
    if (taskEl && preset.task) {
      taskEl.value = preset.task;
      state.filters.task = preset.task;
      updateSubtaskOptions();
    }
  }

  function markActive(btn, selector) {
    document.querySelectorAll(selector).forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
  }
}

// Shows a subtle warning when all weight sliders are at 0 (no score computed)
function updateWeightWarning() {
  const warn = document.getElementById("weight-warn");
  if (!warn) return;
  const total = Object.values(state.weights).reduce((s, v) => s + v, 0);
  warn.hidden = total > 0;
}

function costPerMonth(model, calls) {
  const ci = model.cost_input_per_M || 0;
  const co = model.cost_output_per_M || 0;
  return ((TOKENS_IN * ci) + (TOKENS_OUT * co)) * calls / 1_000_000;
}

function getScore(model, taskKey, subtaskKey) {
  // Si hay sub-categoría seleccionada, usar score por suite específica —
  // PUESTO EN LA ESCALA COMÚN.
  //
  // Antes devolvía el valor CRUDO y eso mezclaba dos escalas bajo un solo slider:
  // el pilar viene z-scoreado y re-escalado (rango −3,65 a 9,73), la suite cruda va
  // de 4,53 a 8,46. Con el umbral por defecto en 8,0 la suite `tool_calling` —máximo
  // 7,12— devolvía CERO modelos siempre, con los 74 medidos ahí. Lo mismo
  // `news_seo_writing`. La página cargaba sin error y mostraba una tabla vacía, que
  // es exactamente el modo de falla que no se nota. Lo reportó Cristian; lo caza
  // ahora `qa_calculadora.mjs`.
  // Se devuelve el valor CRUDO, a propósito: es la escala absoluta que v4.1 adoptó
  // (`score_calidad` = `quality_avg` sin z-scorear) porque el z-score estiraba 1,39
  // puntos reales a 8 publicados. Z-scorear la suite acá lo reintroduciría por la
  // puerta de atrás — probado: arreglaba `tool_calling` y rompía `structured_output`,
  // donde todos puntúan alto y juntos, mostrando como mediocre a un eje en el que
  // todos son buenos.
  //
  // Lo que se adapta es el SLIDER, en `clampUmbralAlEje()`.
  if (subtaskKey) {
    return model.score_by_suite?.[subtaskKey] ?? null;
  }
  // Índice de calidad (v4.1): el titular. Es calidad SOLA — no mezcla precio ni
  // velocidad, que van como columnas. Se sirve pre-horneado desde el JSON para que
  // coincida exactamente con lo que publican README y MODELOS.md.
  if (taskKey === "score_calidad") return model.score_calidad ?? null;
  // Score compuesto: recomputar con z-score y los pesos del usuario. Dejó de ser el
  // titular publicado (correlacionaba r=0,943 con calidad) pero acá SÍ tiene sentido,
  // porque el usuario mueve los pesos y deja de ser "calidad con ruido de precio".
  if (taskKey === "score_global") return computeZScore(model, state.weights);
  // Pilar: TAMBIÉN se recompone con los pesos del usuario. Antes se devolvía
  // score_by_pillar (pesos fijos) y los sliders quedaban de adorno.
  return computeZScore(model, state.weights, taskKey);
}

// Ajusta el umbral de calidad al RANGO REAL del eje que se está mirando.
//
// POR QUÉ (14-ago-2026, bug reportado por Cristian). Cada eje vive en su propia escala
// absoluta: el índice de calidad va de 7,0 a 8,6; la suite `tool_calling` de 4,53 a
// 7,12; `orchestration` de 2,99 a 8,23. El slider es UNO SOLO. Con el umbral por
// defecto en 8,0, elegir «Tool calling» dejaba pasar CERO modelos —siempre— porque el
// mejor de esa suite saca 7,12. La página cargaba, no tiraba error, y mostraba una
// tabla vacía: el modo de falla que no se nota.
//
// La alternativa era z-scorear las suites para que todas compartieran escala. Se probó
// y se descartó: reintroduce exactamente lo que v4.1 eliminó (el z-score estiraba 1,39
// puntos reales a 8 publicados) y en `structured_output` —donde todos puntúan alto y
// juntos— mostraba como mediocre a un eje en el que todos son buenos.
//
// Así que la escala se deja absoluta y honesta, y **se mueve el slider**: su tope pasa
// a ser el máximo real del eje, y si el valor actual quedó por encima se baja a la
// mediana. Se prefiere la mediana y no el máximo para que el listado arranque con
// opciones, no con un solo modelo.
function clampUmbralAlEje() {
  const f = state.filters;
  const modelos = (state.data?.models || []).filter(m => m.ranked && (m.runs || 0) > 0);
  if (!modelos.length) return;

  const vals = modelos
    .map(m => f.subtask ? (m.score_by_suite || {})[f.subtask] : getScore(m, f.task, ""))
    .filter(v => v != null)
    .sort((a, b) => a - b);
  if (!vals.length) return;

  const max = vals[vals.length - 1];
  const mediana = vals[Math.floor(vals.length / 2)];
  const slider = document.getElementById("quality");
  if (slider) {
    slider.max = Math.ceil(max * 10) / 10;
    slider.min = Math.floor(vals[0] * 10) / 10;
  }
  if (f.quality > max) {
    f.quality = Math.round(mediana * 100) / 100;
    if (slider) slider.value = f.quality;
    const out = document.getElementById("quality-val");
    if (out) out.textContent = f.quality.toFixed(2);
  }
}

function updateSubtaskOptions() {
  const wrap = document.getElementById("subtask-wrap");
  const select = document.getElementById("subtask");
  const pillar = state.filters.task;

  // Solo mostrar el sub-select cuando hay un pilar específico (no global)
  if (pillar === "score_global" || pillar === "score_calidad" || !SUITES_BY_PILLAR[pillar]) {
    wrap.hidden = true;
    select.value = "";
    state.filters.subtask = "";
    return;
  }

  // Poblar opciones del pilar correspondiente
  const suites = SUITES_BY_PILLAR[pillar];
  select.innerHTML = `<option value="">Todas (promedio del pilar)</option>` +
    suites.map(s => `<option value="${s.value}">${s.label}</option>`).join("");
  select.value = state.filters.subtask || "";
  wrap.hidden = false;
}

function isProprietary(model) {
  return Object.values(PROPRIETARY_GROUPS).some(check => check(model));
}

function filterAndRank(models, f) {
  const passes = models.filter(m => {
    // DEPRECADOS: fuera SIEMPRE, sin importar qué filtros toque el usuario.
    //
    // Un modelo cuyo endpoint ya no existe no es un candidato: no lo podés llamar.
    // Recomendarlo es peor que no recomendar nada — alguien lee "el #5, barato", lo
    // integra, y se estrella. Devstral Small llegó a estar #5 del ranking meses
    // después de que Mistral apagara su endpoint.
    //
    // Sus números NO se borran: siguen en el repo y en models.json como estadística
    // histórica (son mediciones reales). Pero no compiten y no se pueden elegir acá.
    if (m.retired) return false;

    // VARIANTES DE PROVEEDOR: el mismo modelo servido por otra infra. Su fila canónica
    // ya está en el ranking; dejarlas competir haría que un modelo se enfrente a sí
    // mismo en dos puestos. Se conservan para la comparación entre proveedores.
    if (m.provider_variant) return false;

    // SELF-HOSTED: corre en la máquina del autor, no en un datacenter. Su velocidad es
    // la de ESA GPU. Dejarlo competir acá sería comparar un Spark contra un cluster.
    // Responde otra pregunta ("¿puedo correrlo yo?") y merece su propia vista.
    if (m.self_hosted) return false;

    // "Sólo cobertura completa" filtra a los RANKEABLES (>=50 runs).
    //
    // Antes chequeaba `m.tested` (>=20 runs) mientras este mismo comentario decía
    // ">=50" y el resto del sitio exigía 50 para rankear. O sea: la calculadora
    // dejaba competir a un modelo de 20 runs contra uno de 133 como si fueran
    // comparables. Con muestra chica un modelo lidera por azar — que es exactamente
    // lo que el piso de 50 existe para evitar. Ahora usa `ranked`.
    if (f.onlyTested && !m.ranked) return false;
    // Modelos con runs=0 (en cola) no tienen score real — los ocultamos
    // siempre del ranking porque no se pueden ordenar.
    if ((m.runs || 0) === 0) return false;

    const score = getScore(m, f.task, f.subtask);
    if (score == null && m.runs > 0) return false;
    if (score != null && score < f.quality) return false;

    if (f.speed > 0 && (m.tokens_per_second || 0) < f.speed) return false;

    const cost = costPerMonth(m, f.calls);
    if (cost > f.budget) return false;

    if (f.onlyOpen && !m.open_source) return false;
    if (f.exclProprietary && isProprietary(m)) return false;

    // Filtros por capacidad
    // `tool_calling` es un flag de capacidad DECLARADA, y lo declaran los 82 rankeados:
    // filtrando por ahí el checkbox no ocultaba a nadie — era decorativo. Lo que importa
    // para un agente no es si el modelo dice soportar herramientas, es si las usa bien.
    // Con la nota medida y umbral 6,0 quedan fuera 12, entre ellos DeepSeek R1: #3 en
    // calidad y 4,23 en tool calling. Excelente, barato, e inservible en un harness.
    if (f.onlyTools && (m.tool_calling_score_avg ?? 0) < TOOL_CALLING_MIN) return false;

    // "Completa una tarea real dentro de un agente" — el filtro más duro que hay acá,
    // y el único que no sale de una nota sino de haberlo VISTO ejecutar. La tarea corre
    // en Docker, el modelo lee archivos, decide y escribe la cotización; un pytest la
    // verifica. Un modelo sin medición NO pasa: mismo criterio conservador que el filtro
    // de contexto efectivo — no medido no es lo mismo que aprobado.
    //
    // Por qué no basta con el filtro de tool calling de arriba: son dos preguntas
    // distintas y la diferencia se midió. Hermes 4 405B declara herramientas y tiene
    // 8,20 de calidad; adentro de un agente saca 0,00 porque NO EXISTE endpoint que se
    // las dé. Qwen 3-Next 80B en versión `instruct` saca 0,81 y en versión `thinking`
    // saca 0,00: mismo modelo, mismo tamaño, y el que razona no sostiene el bucle.
    if (f.onlyAgentico && m.sirve_para_agentes !== true) return false;
    if (f.onlyThinking && !m.thinking) return false;
    if (f.onlyMultimodal && !m.multimodal) return false;

    // Filtro por contexto efectivo (NIAH-es): si minContext > 0, el modelo
    // debe tener effective_context medido Y >= al umbral pedido.
    // Modelos con null (no medidos) no pasan — conservador por diseño.
    if (f.minContext > 0) {
      const ec = m.effective_context;
      if (ec == null || ec < f.minContext) return false;
    }

    return true;
  });

  // Calcula costo mensual + score + ratio costo-beneficio para cada modelo
  passes.forEach(m => {
    const cost = costPerMonth(m, f.calls);
    const score = getScore(m, f.task, f.subtask) ?? 0;
    m._cost_month = cost;
    m._task_score = score;
    // Eficiencia: puntos de score por dólar mensual.
    // Mayor = mejor costo-beneficio. Usamos score² para penalizar
    // modelos con score muy bajo aunque sean baratos.
    // Para modelos gratis (cost=0) usamos un valor alto fijo (best efficiency).
    if (cost <= 0.01) {
      m._efficiency = score >= 6 ? 999 : 0;  // Free + score decente = top
    } else {
      m._efficiency = (score * score) / cost;
    }
    // _match queda como referencia interna pero ya no es el sort key
    const budgetRatio = cost > 0 ? (f.budget - cost) / f.budget : 1;
    m._match = score * (0.7 + 0.3 * Math.max(0, budgetRatio));
  });

  // Default: ordenar por score puro (mayor → menor). El usuario quiere ver
  // los mejores primero. La columna "$/score" muestra eficiencia para
  // que cada uno juzgue costo-beneficio según su contexto.
  return passes.sort((a, b) => {
    const scoreA = a._task_score ?? 0;
    const scoreB = b._task_score ?? 0;
    return scoreB - scoreA;
  });
}

function scorePill(score) {
  if (score == null) return `<span class="score-pill low">—</span>`;
  let cls = "low";
  if (score >= 7) cls = "";
  else if (score >= 6) cls = "mid";
  return `<span class="score-pill ${cls}">${score.toFixed(2)}</span>`;
}

// Pill genérico para componentes (Quality, Cost, Tools, Speed, Latency).
// Mismo color-coding que scorePill: ≥7 verde, ≥6 amarillo, <6 rojo.
function componentPill(value) {
  if (value == null || value === undefined) {
    return `<span class="score-pill low">—</span>`;
  }
  let cls = "low";
  if (value >= 7) cls = "";
  else if (value >= 6) cls = "mid";
  return `<span class="score-pill ${cls}">${value.toFixed(2)}</span>`;
}

// Formatea tokens a string legible (64000 → "64K", 800000 → "800K")
function fmtCtx(tokens) {
  if (tokens == null) return null;
  if (tokens >= 1_000_000) return `${(tokens / 1_000_000).toFixed(1)}M`;
  return `${Math.round(tokens / 1000)}K`;
}

// Badge que explica POR QUÉ un modelo no está en el ranking. La etiqueta importa:
// una variante con 130 runs NO es "muestra chica" — está fuera por otra razón.
function notRankedBadge(m) {
  if (m.ranked) return "";
  let label, title;
  if (m.provider === "claude_code") {
    label = "vía suscripción";
    title = "Medido por la suscripción de Claude Code (camino con ~8.8K tokens de scaffolding del CLI). La calidad es un piso conservador (por API midió +0.15/+0.22 en los pares medidos) y la latencia no es comparable. Comparable contra los otros 'vía suscripción', no contra el ranking.";
  } else if (m.self_hosted) {
    label = "self-hosted";
    title = "Corre en hardware propio: su velocidad es la de esa máquina, no la del modelo. No compite en el ranking.";
  } else if (m.provider_variant) {
    label = "variante de proveedor";
    title = "El mismo modelo servido por otra infraestructura. La comparación entre proveedores vive en /mismo-modelo-distinto-proveedor/.";
  } else {
    label = "muestra chica";
    title = "Menos de 50 ejecuciones: con muestra chica un modelo lidera por azar. Score indicativo, no comparable.";
  }
  return ` <span class="ctx-badge ctx-nd" title="${title}">${label}</span>`;
}

// Badge de contexto efectivo (NIAH-es). Destaca vs contexto declarado.
function ctxBadge(m) {
  const ec = m.effective_context;
  if (ec == null) return `<span class="ctx-badge ctx-nd" title="No medido en NIAH-es">n/d</span>`;
  const label = fmtCtx(ec);
  // Color por tamaño: verde >=512K, cyan >=128K, amarillo >=64K, gris <64K
  let cls = "ctx-low";
  if (ec >= 512000)      cls = "ctx-high";
  else if (ec >= 128000) cls = "ctx-mid";
  else if (ec >= 64000)  cls = "ctx-ok";
  return `<span class="ctx-badge ${cls}" title="Contexto usable real: hasta ${label} con retrieval ≥7 en NIAH-es. Puede ser menor al contexto declarado por el proveedor.">${label}</span>`;
}

// Badge de seguridad (resistencia a fuga de credenciales — suite prompt_injection_es).
// Alto = rehúsa filtrar secretos; bajo = los filtra.
function secBadge(m) {
  const s = m.security_score;
  if (s == null) return `<span class="sec-badge sec-nd" title="No medido en prompt_injection_es">n/d</span>`;
  let label, cls, tip;
  if (s >= 7) {
    label = "Seguro";
    cls = "sec-high";
    tip = `Score ${s.toFixed(1)}/10 — rehúsa filtrar credenciales plantadas en documentos. Alta resistencia a inyección de prompt.`;
  } else if (s >= 4) {
    label = `${s.toFixed(1)}/10`;
    cls = "sec-mid";
    tip = `Score ${s.toFixed(1)}/10 — resistencia moderada. Puede filtrar secretos en algunos contextos.`;
  } else {
    label = "Filtra";
    cls = "sec-low";
    tip = `Score ${s.toFixed(1)}/10 — filtra credenciales con facilidad. No usar con documentos que contengan secretos sin sanitizar.`;
  }
  return `<span class="sec-badge ${cls}" title="${tip}">${label}</span>`;
}

// Sorting: aplica state.sort sobre un array ya rankeado.
// Si sort.column === null, deja el orden original (default por _task_score).
function applySort(rows) {
  const { column, direction } = state.sort;
  if (!column) return rows;

  const getter = {
    final: m => m._task_score ?? -Infinity,
    quality: m => m.quality_avg ?? -Infinity,
    cost: m => m.cost_score_avg ?? -Infinity,
    tools: m => m.tool_calling_score_avg ?? -Infinity,
    cost_month: m => m._cost_month ?? Infinity,  // menos = mejor para costo total
    cb: m => m._efficiency ?? -Infinity,
    tps: m => m.tokens_per_second ?? -Infinity,
    ctx: m => m.effective_context ?? -Infinity,
    sec: m => m.security_score ?? -Infinity,
  }[column];

  if (!getter) return rows;
  const mult = direction === "asc" ? 1 : -1;
  return [...rows].sort((a, b) => (getter(a) - getter(b)) * mult);
}

// Click handler para sortable columns. Toggle direction si misma columna,
// reset a desc si es columna distinta.
window.toggleSort = function(column) {
  if (state.sort.column === column) {
    state.sort.direction = state.sort.direction === "asc" ? "desc" : "asc";
  } else {
    state.sort.column = column;
    state.sort.direction = "desc";
  }
  render();
};

function sortIndicator(column) {
  if (state.sort.column !== column) return "<span class='sort-ind'>↕</span>";
  return state.sort.direction === "asc"
    ? "<span class='sort-ind active'>↑</span>"
    : "<span class='sort-ind active'>↓</span>";
}

function modelTags(m) {
  const tags = [];
  // Solo mostrar tag de OSS cuando aplica — "propietario" es default implícito
  // (si no es OS), no necesita tag explícito que agrega ruido visual
  if (m.open_source) tags.push(`<span class="tag os">${m.license || "OSS"}</span>`);
  // Frontera de Pareto (v4.1): ningún otro modelo lo supera a la vez en calidad,
  // precio Y latencia. De 82 rankeados solo 13 lo logran — el resto está dominado.
  if (m.pareto) tags.push(`<span class="tag pareto" title="Frontera de Pareto: ningún otro modelo es a la vez mejor, más barato y más rápido">⭐ frontera</span>`);
  // Capabilities (vienen del JSON, inferidas en export_for_pages.py)
  // Ojo: `tool_calling` es capacidad DECLARADA (la declaran los 82 rankeados). El tag
  // informa que existe; el filtro usa la nota MEDIDA, que es otra cosa.
  if (m.tool_calling) tags.push(`<span class="tag tools" title="Declara soporte de tool calling. La nota medida está en la columna Tools">🔧 tools</span>`);
  // Agéntico: se muestra SIEMPRE, no solo con el filtro activo. Quien está eligiendo
  // modelo para un agente necesita ver "este no puede" aunque no haya tocado el filtro
  // — es justo el dato que el índice de calidad esconde.
  if (m.sirve_para_agentes === false) {
    const mot = Object.values(m.agentico?.tareas || {}).find(t => t.motivo)?.motivo || "";
    tags.push(`<span class="tag tag-danger" title="Probado dentro de un agente real: ${mot}">⛔ no corre en agente</span>`);
  } else if (m.agentico?.estado === "irregular") {
    // Distinto de ⛔: éste SÍ completa alguna tarea agéntica y falla otra. Colapsarlo con
    // «no puede» ocultaría justo la diferencia que decide una elección.
    const f = (m.agentico.falla_en || []).map(x => x.replace("harbor-", "")).join(", ");
    tags.push(`<span class="tag tag-warn" title="Completa unas tareas agénticas y falla otras. Falla en: ${f}">⚠️ agente irregular</span>`);
  } else if (m.sirve_para_agentes === true) {
    const t = m.agentico?.tareas || {};
    const det = Object.entries(t).map(([k, v]) =>
      `${k.replace("harbor-", "")} ${v.media} (piso ${v.piso})`).join(" · ");
    tags.push(`<span class="tag agentico" title="Completó tareas de negocio de punta a punta dentro de un agente. ${det}">🤖 agente ✓</span>`);
  }
  if (m.thinking) tags.push(`<span class="tag thinking" title="Razonamiento interno">🧠 thinking</span>`);
  if (m.multimodal) tags.push(`<span class="tag multimodal" title="Texto + imagen/audio">🎨 multimodal</span>`);
  // Tag de cobertura: sólo cuando es <50 runs (parcial). El default oculta estos
  // del listado, pero si el usuario activó "incluir no probados" aparecen.
  // Mejor mostrar runs reales que un genérico "sin medir" — más informativo
  // y evita confusión cuando el mismo modelo está medido en otra variante.
  const runs = m.runs || 0;
  if (!m.tested) {
    if (runs === 0) {
      tags.push(`<span class="tag tag-warn" title="Pendiente de benchmarkear (en cola para próximo lote)">en cola</span>`);
    } else if (runs < 10) {
      tags.push(`<span class="tag tag-warn" title="Smoke test — pocos runs, score con alta variación">smoke test (${runs} runs)</span>`);
    } else {
      tags.push(`<span class="tag tag-warn" title="Cobertura parcial — score puede variar al completar 91 tests">parcial (${runs}/91)</span>`);
    }
  }
  return tags.join("");
}

function render() {
  const f = state.filters;
  const ranked = filterAndRank(state.data.models, f);
  const tableWrap = document.getElementById("results-table-wrap");
  const empty = document.getElementById("empty-state");

  const summary = document.getElementById("results-summary");
  if (ranked.length === 0) {
    tableWrap.innerHTML = "";
    empty.hidden = false;
    summary.textContent = "0 modelos cumplen tus criterios";
    return;
  }
  empty.hidden = true;
  // Decir CUÁNTOS de cuántos, y qué filtro es el que más corta.
  // Antes decía solo "24 modelos cumplen tus criterios": el usuario veía 24 sobre un
  // catálogo que anuncia 82 y no tenía forma de saber por qué. El umbral de calidad
  // por defecto (6,5) deja pasar el top 29% — no está roto, pero era invisible, y un
  // filtro invisible se lee como un dato faltante. Peor: modelos conocidos
  // desaparecían sin explicación (Claude Opus 5 sale por calidad 3,03).
  const universo = state.data.models.filter(m => m.ranked && (m.runs || 0) > 0);
  const cortes = [
    { nombre: `calidad ≥${f.quality}`, n: universo.filter(m => (getScore(m, f.task, f.subtask) ?? 0) < f.quality).length },
    { nombre: `presupuesto $${f.budget}/mes`, n: universo.filter(m => costPerMonth(m, f.calls) > f.budget).length },
    { nombre: "usan bien las herramientas", n: f.onlyTools ? universo.filter(m => (m.tool_calling_score_avg ?? 0) < TOOL_CALLING_MIN).length : 0 },
    { nombre: "completan la tarea en un agente", n: f.onlyAgentico ? universo.filter(m => m.sirve_para_agentes !== true).length : 0 },
    { nombre: "solo open source", n: f.onlyOpen ? universo.filter(m => !m.open_source).length : 0 },
  ].filter(c => c.n > 0).sort((a, b) => b.n - a.n);
  const detalle = cortes.length
    ? ` · el que más corta: ${cortes[0].nombre} (deja fuera ${cortes[0].n})`
    : "";
  summary.textContent =
    `${ranked.length} de ${universo.length} modelos rankeados cumplen tus criterios${detalle}.`;

  // Sin límite — mostramos todos los que pasan los filtros.
  const top = ranked;
  // Etiqueta de la columna Score: subtask > pillar > global
  let taskLabel = "Global";
  if (f.subtask) {
    const suite = (SUITES_BY_PILLAR[f.task] || []).find(s => s.value === f.subtask);
    taskLabel = suite ? suite.label.split(" (")[0] : f.subtask;
  } else if (f.task === "score_calidad") {
    taskLabel = "Calidad";
  } else if (f.task !== "score_global") {
    taskLabel = f.task;
  }

  // Costo-beneficio: clasifica cada modelo según su eficiencia (score² / costo)
  // relativa al mejor de la lista filtrada actual. Etiquetas semánticas con
  // contexto del provider — "gratis" no es honesto sin aclarar el límite.
  const maxEfficiency = Math.max(...top.map(m => m._efficiency || 0));

  // Etiqueta para modelos sin costo per-call según provider (más honesta que "Gratis").
  // Si el modelo está en una suscripción del catálogo, mostramos su precio mensual.
  const freeLabel = (m) => {
    // Modelos en suscripción mensual: priorizar el más barato (más accesible)
    if (m.subscriptions && m.subscriptions.length > 0) {
      const cheapest = m.subscriptions.reduce((a, b) =>
        a.price_month_usd <= b.price_month_usd ? a : b
      );
      const allSubs = m.subscriptions
        .map(s => `${s.name} ($${s.price_month_usd}/mes)`)
        .join(", ");
      return {
        label: `★ Sub $${cheapest.price_month_usd}/mes`,
        tip: `Incluido en: ${allSubs}. NO es gratis — requiere pagar la suscripción mensual.`,
      };
    }
    // NIM gratis: realmente $0 con rate limit
    if (m.provider === "nvidia_nim") {
      return {
        label: "★ NIM 40rpm",
        tip: "Sin costo por call vía NVIDIA NIM. Límite: 40 requests/minuto en free tier. Apto para benchmarks secuenciales y producción de bajo volumen.",
      };
    }
    // Local: corre en hardware propio
    if (m.tier === "local") {
      return {
        label: "★ Local",
        tip: "Corre en hardware propio (DGX Spark, Mac M-series, etc). Sin costo por call, requiere setup Ollama. Costo real: electricidad + amortización del hardware.",
      };
    }
    return {
      label: "★ Sin pago",
      tip: "Sin costo per-call. Verificar límites del provider antes de producción.",
    };
  };

  // ── `formatEfficiency` ya NO se usa en la tabla (13-ago-2026) ────────────────
  // La columna "Rinde" (score² ÷ costo) se sacó porque **ordenaba igual que ordenar
  // por precio**: r = 0,999 contra el orden por costo puro, con 0,7 puestos de
  // desplazamiento medio sobre 82 modelos.
  //
  // No es un defecto de la fórmula, es aritmética: la calidad de los rankeados varía
  // 1,19× (7,26 a 8,65) y el costo varía **772×** ($0,10 a $78). Con esa asimetría
  // "valor" ES precio, y la columna repetía la de al lado con otro nombre.
  //
  // Encima confundía: "0% del mejor" para Claude Opus 4.8 se leía como si no valiera
  // nada, cuando su calidad es 7,45 de 10 — solo que cuesta $78/mes.
  //
  // Se deja la función por si vuelve a servir con un examen más discriminante (ver
  // las 5 suites saturadas). Si la calidad vuelve a dispersarse, esta columna
  // recupera sentido; hoy no lo tiene.
  const formatEfficiency = (m) => {
    if (!m._efficiency || maxEfficiency === 0) return "—";
    if (m._cost_month <= 0.01 && m._task_score >= 6) {
      const f = freeLabel(m);
      return `<span class="cb-badge cb-free" title="${f.tip}">${f.label}</span>`;
    }
    // Etiquetas RELATIVAS, no veredictos. Antes decían "Excelente / Bueno /
    // Aceptable / Caro" sobre una medida que es relativa al mejor de la lista, y eso
    // producía dos mentiras a la vez:
    //
    //   1. Un acantilado. Tencent Hy3 (29%) salía "Aceptable" y GPT-5.6 Luna (24%)
    //      "Caro" — un punto porcentual de diferencia, dos categorías que suenan
    //      opuestas. Sus costos: $1,66 y $1,86 al mes.
    //   2. Peor: llamarle "Caro" a un modelo de $1,86/mes es falso en cualquier
    //      lectura normal. Solo significaba "rinde menos por peso que el más barato
    //      de la lista". Un outlier barato define el 100% y pinta de caros a todos.
    //
    // Ahora el badge dice el número y contra qué se compara. Sin acantilado: dos
    // modelos parecidos muestran cifras parecidas, que es lo que son.
    const pct = Math.round((m._efficiency / maxEfficiency) * 100);
    const cls = pct >= 75 ? "cb-excellent" : pct >= 40 ? "cb-good"
              : pct >= 15 ? "cb-ok" : "cb-poor";
    const etiqueta = pct >= 100 ? "el mejor" : `${pct}% del mejor`;
    return `<span class="cb-badge ${cls}" title="Calidad por peso gastado, comparada con la mejor opción de ESTA lista (no en absoluto): score² ÷ costo mensual. ${pct}% significa que rinde ${(100/Math.max(pct,1)).toFixed(1)}× menos calidad por peso que el líder — no que sea caro.">${etiqueta}</span>`;
  };

  // Mostrar columnas de componentes (Quality + Cost score + Tools) solo en
  // vista global. Cuando el usuario filtra por pilar/suite específica, esas
  // columnas no aplican y agregaríamos ruido visual.
  const showComponents = (f.task === "score_global" && !f.subtask);

  // Sorting custom del usuario (si seleccionó una columna haciendo click en header)
  const sorted = applySort(top);

  const html = `
    <table class="results-table">
      <thead>
        <tr>
          <th>#</th>
          <th>Modelo</th>
          <th class="num sortable" onclick="toggleSort('final')" title="Click para ordenar">Score ${taskLabel} ${sortIndicator("final")}</th>
          ${showComponents ? `
            <th class="num sortable" onclick="toggleSort('quality')" title="Quality (70% del score global por default): score automático + LLM-as-Judge Phi-4. 10 = excelente, 0 = malo. Click para ordenar">Quality ${sortIndicator("quality")}</th>
            <th class="num sortable" onclick="toggleSort('cost')" title="Cost score (15% por default): INVERSO al precio — 10 = gratis o muy barato, 5 = $0.01/call, 2 = $0.10/call, 0 = $1.00+/call. Más alto = más barato. Click para ordenar">Costo↓ ${sortIndicator("cost")}</th>
            <th class="num sortable" onclick="toggleSort('tools')" title="Tool calling (badge, no pondera el score global): adherencia al schema OpenAI tools. 10 = perfecto, 7 = N/A (test sin tools). Click para ordenar">Tools ${sortIndicator("tools")}</th>
          ` : ""}
          <th class="num sortable" onclick="toggleSort('cost_month')" title="Costo total/mes según presupuesto y calls. Click para ordenar">Costo/mes ${sortIndicator("cost_month")}</th>
          <th>Tier</th>
        </tr>
      </thead>
      <tbody>
        ${sorted.map((m, i) => `
          <tr>
            <td class="num">${i + 1}</td>
            <td>
              <span class="model-name">${m.name}</span>${notRankedBadge(m)}
              <div class="model-meta">${modelTags(m)} · ${m.id}</div>
            </td>
            <td class="num">${scorePill(m._task_score)}</td>
            ${showComponents ? `
              <td class="num">${componentPill(m.quality_avg)}</td>
              <td class="num">${componentPill(m.cost_score_avg)}</td>
              <td class="num">${componentPill(m.tool_calling_score_avg)}</td>
            ` : ""}
            <td class="num">$${m._cost_month.toFixed(2)}</td>
            <td>${m.tier}</td>
          </tr>
        `).join("")}
      </tbody>
    </table>
  `;

  tableWrap.innerHTML = html;
}

// ============================================================
// WIZARD GUIADO (v4.0)
// 3 preguntas de negocio → recomendación concreta. Reusa el motor real
// (computeZScore + models.json congelado). La calculadora completa queda abajo.
// ============================================================
// Tipos de agente. Aparecen SOLO si el usuario eligió "Agentes / automatizar", porque
// "agente" no es una cosa: un asistente conversacional y un workflow desatendido fallan
// distinto y se eligen con ejes distintos.
//
// POR QUÉ (14-ago-2026). Cristian, mirando la tabla que le armé a mano en el chat:
// *"la calculadora me tiene que ayudar a decidir esto"*. La tabla comparaba adherencia,
// tool calling, multiturno y el reward de Harbor — y el wizard mostraba UN compuesto que
// esconde justo esos ejes. Peor: el orden del pilar Agentes ponía a Qwen 3.7 Flash
// primero, que es **el más bajo en adherencia** de ese grupo, y la adherencia es
// exactamente el eje del fallo real que Cristian vivió ("le pedí algo e hizo otra cosa").
const WIZ_AGENTES = [
  {
    id: "asistente", ic: "💬", ot: "Asistente conversacional",
    od: "Estilo Hermes/Nyx: le hablás, hace facturas, cotiza, lee correo",
    // Pesa lo que hace fallar a un asistente: que NO haga lo que le pediste.
    // La VELOCIDAD pesa acá y NO en el workflow. Es una asimetría deliberada: a un
    // asistente personal le hablás y esperás la respuesta mirando; un workflow
    // asíncrono se toma el tiempo que necesite y nadie lo nota. Sin este eje, DeepSeek
    // V4 Pro entraba #3 de esta lista con **58 segundos de latencia media** — correcto
    // por calidad, inusable como asistente.
    // `agentic_quality` en vez de `multiturno_score`: las dos salen de
    // `agent_long_horizon`, pero la primera es la CALIDAD pura y la segunda el score
    // final, que mezcla costo y velocidad. El repo decidió en v4.1 que la calidad va
    // sola y el precio al lado — acá aplica igual. Y es el eje que explicó lo que
    // Cristian ya sabía por usarlo: Gemini 3.6 Flash es #3 de 80 ahí y #76 en el
    // índice general.
    ejes: [["policy_adherence", 0.30], ["agentic_quality", 0.25], ["harbor_media", 0.20],
           ["latencia", 0.15], ["tool_calling_adversarial", 0.10]],
    nota: "Para un asistente, el fallo caro no es que no sepa: es que haga otra cosa. " +
          "Por eso pesa más la <b>adherencia</b> que el tool calling — y pesa la " +
          "<b>latencia</b>, porque acá la espera se siente.",
  },
  {
    id: "workflow", ic: "⚙️", ot: "Workflow desatendido",
    od: "N8N o cron: se dispara solo, nadie mira el resultado",
    // Acá se usa el PISO de Harbor, no la media: sin humano revisando, lo que importa
    // no es cómo sale en promedio sino qué tan mal puede salir. Un modelo que promedia
    // 0,89 con piso 0,78 factura mal una de cada tantas veces, y nadie se entera.
    ejes: [["harbor_piso", 0.35], ["tool_calling_adversarial", 0.25],
           ["policy_adherence", 0.20], ["structured_output", 0.20]],
    nota: "Nadie revisa la salida, así que se prioriza <b>constancia</b>: pesa el " +
          "<b>peor</b> resultado de la tarea real, no el promedio. La velocidad " +
          "<b>no</b> entra: si corre asíncrono, que tarde no le cuesta nada a nadie.",
  },
  {
    id: "codigo", ic: "💻", ot: "Agente de código",
    od: "Lee y escribe archivos, corre comandos, itera",
    ejes: [["code_generation", 0.35], ["tool_calling_adversarial", 0.30],
           ["harbor_media", 0.20], ["multiturno_score", 0.15]],
    nota: "Se combina capacidad de código con el bucle de herramientas: un agente de " +
          "código que programa bien pero no sostiene el bucle no sirve.",
  },
];

// Los ejes se leen de lugares distintos del modelo. Una sola función para que el
// puntaje y la tabla NO puedan discrepar — si divergen, la tabla "explica" un orden
// que no es el que se calculó, que es peor que no mostrar nada.
// Harbor viene 0-1 y se lleva a 0-10 para promediarlo con las suites.
function wizEje(m, eje) {
  if (eje === "multiturno_score") return m.multiturno_score ?? null;
  if (eje === "agentic_quality") return m.agentic_quality ?? null;
  const h = m.agentico?.tareas?.["harbor-cotizar"];
  if (eje === "harbor_media") return h?.media != null ? h.media * 10 : null;
  if (eje === "harbor_piso") return h?.piso != null ? h.piso * 10 : null;
  // `latency_score_avg` va de 1,06 a 4,69 (más alto = más rápido). Se estira a 0-10
  // para que promedie con las suites sin quedar aplastado: un eje que solo se mueve
  // entre 1 y 4,7 aportaría un quinto de lo que dice su peso.
  if (eje === "latencia") {
    const v = m.latency_score_avg;
    return v == null ? null : Math.max(0, Math.min(10, (v - 1) * (10 / 3.7)));
  }
  return (m.score_by_suite || {})[eje] ?? null;
}

const WIZ = {
  step: 0, task: null, budget: null, os: false, tools: false, agente: null,
  tasks: [
    { id: "general", ic: "🧭", ot: "Un poco de todo", od: "No estoy seguro / uso general", pillar: null, page: null },
    { id: "coding", ic: "💻", ot: "Programar", od: "Código, debugging, scripts", pillar: "Coding", page: "/mejor-llm-para-programar/" },
    { id: "contenido", ic: "✍️", ot: "Escribir contenido", od: "Blogs, copy, emails, marketing", pillar: "Contenido", page: "/mejor-llm-para-contenido/" },
    { id: "agentes", ic: "🔧", ot: "Agentes / automatizar", od: "N8N, flujos multi-paso, tareas", pillar: "Agentes", page: "/mejor-llm-para-agentes/" },
    { id: "razonamiento", ic: "🧠", ot: "Razonar / analizar", od: "Análisis, decisiones, matemática", pillar: "Razonamiento", page: "/mejor-llm-para-razonamiento/" },
    { id: "chat", ic: "💬", ot: "Chat en vivo", od: "Respuesta rápida, conversación", pillar: null, page: null, latency: true },
  ],
  budgets: [
    { id: "personal", ic: "🧑", ot: "Poco", od: "~$5/mes · uso personal", w: { quality: 85, cost: 5, speed: 5, latency: 5 } },
    { id: "solopreneur", ic: "🚀", ot: "Medio", od: "~$25/mes · solopreneur", w: { quality: 70, cost: 15, speed: 7.5, latency: 7.5 } },
    { id: "pyme", ic: "🏢", ot: "Bastante", od: "~$100/mes · PyME", w: { quality: 55, cost: 30, speed: 8, latency: 7 } },
    { id: "produccion", ic: "⚙️", ot: "Mucho", od: "~$500/mes · producción", w: { quality: 40, cost: 40, speed: 12, latency: 8 } },
  ],
};

function wizInit() {
  const wiz = document.getElementById("wizard");
  if (!wiz || !state.data) return;

  // Render opciones de tarea y presupuesto
  const optHtml = (o, group) =>
    `<button class="wiz-opt" data-group="${group}" data-id="${o.id}" type="button">
       <span class="ic">${o.ic}</span><span><span class="ot">${o.ot}</span><span class="od">${o.od}</span></span>
     </button>`;
  document.getElementById("wiz-tasks").innerHTML = WIZ.tasks.map(o => optHtml(o, "task")).join("");
  document.getElementById("wiz-budgets").innerHTML = WIZ.budgets.map(o => optHtml(o, "budget")).join("");
  document.getElementById("wiz-agentes").innerHTML = WIZ_AGENTES.map(o => optHtml(o, "agente")).join("");

  wiz.addEventListener("click", (e) => {
    const opt = e.target.closest(".wiz-opt");
    if (opt) {
      const g = opt.dataset.group;
      wiz.querySelectorAll(`.wiz-opt[data-group="${g}"]`).forEach(b => b.classList.remove("sel"));
      opt.classList.add("sel");
      WIZ[g] = opt.dataset.id;
      document.getElementById("wiz-next").disabled = false;
      return;
    }
    const tog = e.target.closest(".wiz-toggle");
    if (tog) {
      const on = tog.getAttribute("aria-pressed") !== "true";
      tog.setAttribute("aria-pressed", on ? "true" : "false");
      WIZ[tog.id === "wiz-tog-os" ? "os" : "tools"] = on;
    }
  });

  // El paso 0.5 (tipo de agente) SOLO existe si la tarea elegida es "agentes".
  // Se navega por una secuencia calculada en vez de step++ para que preguntar de más
  // —o de menos— sea imposible por construcción.
  const secuencia = () => WIZ.task === "agentes" ? [0, 0.5, 1, 2] : [0, 1, 2];
  document.getElementById("wiz-next").addEventListener("click", () => {
    const seq = secuencia(), i = seq.indexOf(WIZ.step);
    if (i < seq.length - 1) { WIZ.step = seq[i + 1]; wizRenderStep(); }
    else wizResult();
  });
  document.getElementById("wiz-back").addEventListener("click", () => {
    const seq = secuencia(), i = seq.indexOf(WIZ.step);
    if (i > 0) { WIZ.step = seq[i - 1]; wizRenderStep(); }
  });
  window.dataLayer = window.dataLayer || [];
}

function wizRenderStep() {
  const wiz = document.getElementById("wizard");
  wiz.querySelectorAll(".wiz-step").forEach(s => { s.hidden = parseFloat(s.dataset.step) !== WIZ.step; });
  const seq = WIZ.task === "agentes" ? [0, 0.5, 1, 2] : [0, 1, 2];
  const idx = Math.max(0, seq.indexOf(WIZ.step));
  wiz.querySelectorAll(".wiz-steps span").forEach((s, i) => s.classList.toggle("on", i <= idx));
  document.getElementById("wiz-back").hidden = WIZ.step === 0;
  const next = document.getElementById("wiz-next");
  next.textContent = WIZ.step === 2 ? "Ver mi recomendación ✨" : "Siguiente →";
  // el último paso (restricciones) es opcional: siempre habilitado
  next.disabled = WIZ.step === 2 ? false
    : WIZ.step === 0 ? !WIZ.task
    : WIZ.step === 0.5 ? !WIZ.agente
    : !WIZ.budget;
  document.getElementById("wiz-result").hidden = true;
}

// Candidatos del wizard. Función aparte para que el QA pruebe la ruta REAL.
//
// FILTRO DURO (14-ago-2026): si el usuario viene a montar un agente, no se le
// recomienda algo que NO PUEDE correr dentro de uno. Medido: 5 modelos quedan fuera, y
// Hermes 4 405B estaba **#14** de esta misma lista, a una medición del podio.
//
// Y el toggle "tiene que usar herramientas" mentía: filtraba por
// `tool_calling_score_avg`, que es la nota de una suite de TEXTO. Qwen 3-Next 80B
// Thinking saca 6,41 ahí —pasa el umbral— y **0,00 dentro de un agente real**, porque
// no sostiene el bucle. Marcar esa casilla y recibir ese modelo era el peor resultado
// posible del wizard: el usuario pidió explícitamente lo único que ese modelo no puede.
function wizCandidatos(todos, { os = false, tools = false, pillar = null } = {}) {
  let models = todos.filter(m => m.ranked);
  if (os) models = models.filter(m => m.open_source);
  if (pillar === "Agentes" || tools) models = models.filter(m => m.sirve_para_agentes !== false);
  if (tools) models = models.filter(m => (m.tool_calling_score_avg || 0) >= TOOL_CALLING_MIN);
  return models;
}

function wizResult() {
  const t = WIZ.tasks.find(x => x.id === WIZ.task);
  const b = WIZ.budgets.find(x => x.id === WIZ.budget);
  let w = { ...b.w };
  if (t.latency) w = { quality: 50, cost: 15, speed: 10, latency: 25 }; // chat prioriza latencia
  const pillar = t.pillar;

  // Los candidatos salen de wizCandidatos() — la MISMA función que ejercita el QA.
  // Replicar el filtro en el test sería una copia que se desincroniza, que es el bug
  // que este repo ya pagó varias veces.
  let models = wizCandidatos(state.data.models, { os: WIZ.os, tools: WIZ.tools, pillar });

  // Con tipo de agente elegido se puntúa por SUS ejes, no por el compuesto del pilar.
  const tipo = pillar === "Agentes" ? WIZ_AGENTES.find(a => a.id === WIZ.agente) : null;
  const puntaje = (m) => {
    if (!tipo) return computeZScore(m, w, pillar);
    // Media ponderada de los ejes crudos del tipo. Escala absoluta, sin z-scorear:
    // misma decisión que v4.1 y que `getScore` para subcategorías.
    let suma = 0, peso = 0;
    for (const [eje, p] of tipo.ejes) {
      const v = wizEje(m, eje);
      if (v == null) continue;
      suma += v * p; peso += p;
    }
    return peso > 0 ? suma / peso : null;
  };

  const scored = models
    .map(m => ({ m, s: puntaje(m) }))
    .filter(x => x.s != null)
    .sort((a, b2) => b2.s - a.s);

  const wrap = document.getElementById("wiz-result");
  if (!scored.length) {
    wrap.innerHTML = `<div class="empty" style="margin-top:16px">No hay modelos que cumplan esas restricciones. Prueba quitando alguna.</div>`;
    wrap.hidden = false;
    return;
  }
  const top = scored[0].m;
  // alternativa más barata con calidad >= 8 (la tesis: no pagues de más)
  const cheap = scored.map(x => x.m).filter(m => (m.quality_avg || 0) >= 8 && m.name !== top.name)
    .sort((a, c) => (a.cost_input_per_M ?? 999) - (c.cost_input_per_M ?? 999))[0];

  const price = (m) => m.cost_input_per_M != null ? `$${m.cost_input_per_M}/M in` : "—";
  const per1k = (m) => m.cost_per_1k_calls_usd != null ? `$${m.cost_per_1k_calls_usd}` : "—";
  const badges = (m) => [
    m.open_source ? `<span class="wiz-bdg os">Open source</span>` : "",
    `<span class="wiz-bdg price">${price(m)}</span>`,
    `<span class="wiz-bdg q">Calidad ${m.quality_avg ?? "—"}/10</span>`,
  ].join("");

  const taskLabel = t.id === "general" ? "uso general" : t.ot.toLowerCase();
  const why = tipo
    ? `Es el mejor para un <b>${tipo.ot.toLowerCase()}</b> con tu presupuesto. ${tipo.nota}`
    : pillar
    ? `Es el mejor en <b>${t.ot}</b> para tu presupuesto. La calidad se mide con los tests reales de ese pilar, no un promedio genérico.`
    : `Es el que mejor equilibra calidad y precio para <b>${taskLabel}</b> con tu volumen.`;

  // Tabla de EJES: los números con los que se tomó la decisión, a la vista.
  // Un compuesto solo te dice el orden; esto te deja discutirlo. Es exactamente la
  // tabla que hubo que armar a mano en un chat para poder decidir — si la calculadora
  // no la muestra, la decisión se toma afuera y la calculadora sobra.
  const ejesTabla = () => {
    if (!tipo) return "";
    const ETIQ = {
      policy_adherence: "Adherencia", multiturno_score: "Multiturno",
      agentic_quality: "Calidad agéntica",
      tool_calling_adversarial: "Tool calling", structured_output: "JSON estructurado",
      code_generation: "Código", harbor_media: "Tarea real", harbor_piso: "Tarea real (peor)",
      latencia: "Rapidez",
    };
    const cols = tipo.ejes.map(e => e[0]);
    const fila = (m, destacado) => `<tr${destacado ? ' class="wiz-top"' : ""}>
        <td>${m.name}</td>
        ${cols.map(c => {
          const v = wizEje(m, c);
          return `<td>${v == null ? "—" : v.toFixed(2)}</td>`;
        }).join("")}
        <td>$${(m.cost_per_1k_calls_usd ?? 0).toFixed(2)}</td>
      </tr>`;
    const top5 = scored.slice(0, 5).map((x, i) => fila(x.m, i === 0)).join("");
    return `
      <div class="wiz-ejes">
        <div class="dh">Con qué números se decidió <small>(peso: ${
          tipo.ejes.map(([e, p]) => `${ETIQ[e]} ${Math.round(p * 100)}%`).join(" · ")})</small></div>
        <div class="wiz-tabla-wrap">
        <table class="wiz-tabla">
          <thead><tr><th>Modelo</th>${cols.map(c => `<th>${ETIQ[c]}</th>`).join("")}<th>$/1k</th></tr></thead>
          <tbody>${top5}</tbody>
        </table>
        </div>
        <p class="wiz-nota">«Tarea real» = una cotización de punta a punta dentro de un agente
        (Docker + herramientas), verificada por tests. 1,00 = la resolvió entera, en los 3 intentos.</p>
      </div>`;
  };

  const deeper = [];
  if (t.page) deeper.push(`<a href="${t.page}">Ranking completo: ${t.ot} <span class="ar">→</span></a>`);
  const cmpSlug = wizCmpSlug(top.name);
  if (cmpSlug) deeper.push(`<a href="${cmpSlug}">Comparación cara a cara <span class="ar">→</span></a>`);
  const rankedN = (state.data.ranked_count) || state.data.models.filter(m => m.ranked).length;
  deeper.push(`<a href="#results">Explorar los ${rankedN} modelos con filtros <span class="ar">→</span></a>`);

  wrap.innerHTML = `
    <div class="wiz-rec">
      <p class="wiz-eyebrow">Tu recomendación</p>
      <div class="wiz-hero">
        <div class="wiz-pick-name">${top.name}</div>
        <div class="wiz-badges">${badges(top)}</div>
        <p class="wiz-why">${why}</p>
        <div class="wiz-cost">
          <div><div class="k">Precio entrada</div><div class="v green">${price(top)}</div></div>
          <div><div class="k">~1.000 llamadas</div><div class="v">${per1k(top)}</div></div>
          <div><div class="k">Calidad</div><div class="v">${top.quality_avg ?? "—"}</div></div>
        </div>
      </div>
      ${cheap ? `
      <div class="wiz-deeper" style="border-color:rgba(0,212,255,.28)">
        <div class="dh" style="color:var(--cyan)">💡 Si quieres gastar menos (misma tesis: la calidad top no cuesta caro)</div>
        <a href="#results"><b>${cheap.name}</b> — calidad ${cheap.quality_avg}/10 a ${price(cheap)} <span class="ar">→</span></a>
      </div>` : ""}
      ${ejesTabla()}
      <div class="wiz-deeper">
        <div class="dh">Profundiza</div>
        ${deeper.join("")}
      </div>
      <button class="wiz-restart" id="wiz-restart" type="button">↺ Empezar de nuevo</button>
    </div>`;
  wrap.hidden = false;
  document.querySelectorAll(".wiz-step").forEach(s => s.hidden = true);
  document.querySelector(".wiz-steps").style.display = "none";
  document.querySelector(".wiz-nav").style.display = "none";
  document.getElementById("wiz-restart").addEventListener("click", () => {
    WIZ.step = 0; WIZ.task = null; WIZ.budget = null; WIZ.os = false; WIZ.tools = false;
    document.querySelectorAll(".wiz-opt.sel").forEach(o => o.classList.remove("sel"));
    document.querySelectorAll(".wiz-toggle").forEach(o => o.setAttribute("aria-pressed", "false"));
    document.querySelector(".wiz-steps").style.display = "";
    document.querySelector(".wiz-nav").style.display = "";
    wizRenderStep();
  });
  window.dataLayer.push({ event: "wizard_recomendacion", task: WIZ.task, budget: WIZ.budget, pick: top.name });
}

// Mantiene el JSON-LD (Dataset + SoftwareApplication) en sync con la data viva:
// dateModified = fecha del dataset, versión y conteos. Señal de frescura para Google
// y garantía de que el schema no caduca (todo sale de models.json, nada hardcodeado).
function syncStructuredData(data, totalModels, totalRuns) {
  try {
    const genDate = (data.generated_at || "").slice(0, 10);
    const ver = data.scoring_version || "v4.0";
    const runsRounded = (Math.floor(totalRuns / 1000) * 1000).toLocaleString("es");
    document.querySelectorAll('script[type="application/ld+json"]').forEach(s => {
      let j;
      try { j = JSON.parse(s.textContent); } catch { return; }
      const nodes = j["@graph"] || [j];
      let touched = false;
      nodes.forEach(n => {
        if (n["@type"] === "Dataset") {
          if (genDate) n.dateModified = genDate;
          n.version = ver;
          n.description = `Benchmark abierto de ${totalModels} modelos de IA (LLMs) con ${runsRounded}+ tests reales organizados en 4 pilares (Razonamiento, Coding, Contenido, Agentes) + long-context y seguridad como dimensiones separadas. Evaluación con LLM-as-Judge Phi-4 local.`;
          touched = true;
        } else if (n["@type"] === "SoftwareApplication") {
          if (genDate) n.dateModified = genDate;
          n.softwareVersion = ver;
          n.description = `Calculadora interactiva para encontrar el mejor modelo IA según presupuesto, calidad, velocidad, tarea y caso de uso. Filtra entre ${totalModels} modelos benchmarkeados con pesos ajustables.`;
          touched = true;
        }
      });
      if (touched) s.textContent = JSON.stringify(j, null, 2);
    });
  } catch (e) { console.warn("structured data sync skipped", e); }
}

// Mapea un modelo a una página de comparación existente si la hay (hub-and-spoke).
function wizCmpSlug(name) {
  const n = name.toLowerCase();
  if (n.includes("fable")) return "/fable-5-vs-gpt-5-6-sol/";
  if (n.includes("opus")) return "/claude-haiku-sonnet-opus/";
  if (n.includes("deepseek")) return "/deepseek-vs-claude/";
  if (n.includes("gemini")) return "/gemini-vs-claude/";
  if (n.includes("gpt-5") || n.includes("gpt5")) return "/claude-vs-chatgpt/";
  if (n.includes("qwen") || n.includes("llama")) return "/qwen-vs-llama/";
  return null;
}

document.addEventListener("DOMContentLoaded", load);
