// Calculadora de modelos IA — Cristian Tala
// Lee docs/data/models.json y aplica filtros con sliders

const TOKENS_IN = 300;
const TOKENS_OUT = 1500;

// Presets de uso — calibrados para emprendedores hispanohablantes.
// Cada preset configura los 4 sliders + tarea principal.
const PRESETS = {
  personal: {
    budget: 5,
    calls: 300,        // ~10 calls/día
    quality: 6.0,      // aceptable para chat personal
    speed: 0,
    task: "score_global",
  },
  solopreneur: {
    budget: 25,
    calls: 3000,       // ~100 calls/día (1-2 agentes N8N pequeños)
    quality: 6.5,
    speed: 0,
    task: "score_global",
  },
  pyme: {
    budget: 100,
    calls: 30000,      // ~1000 calls/día (varios workflows en paralelo)
    quality: 7.0,      // calidad relevante para producto
    speed: 50,         // latencia importa
    task: "score_global",
  },
  produccion: {
    budget: 500,
    calls: 300000,     // ~10K calls/día (tráfico de producto SaaS)
    quality: 7.0,
    speed: 100,        // alta velocidad crítica
    task: "score_global",
  },
};

const PROPRIETARY_GROUPS = {
  anthropic: m => m.id?.includes("anthropic/") || m.id?.startsWith("claude"),
  openai: m => m.id?.startsWith("gpt-") || m.id?.startsWith("openai/") || m.provider === "openai_direct" || m.provider === "openai_responses",
  // Google propietarios: Gemini Flash/Pro (NO Gemma open-source)
  google_proprietary: m => /gemini[-_/]/i.test(m.id || "") && !m.open_source,
};

const state = {
  data: null,
  filters: {
    budget: 500,        // Default para emprendedor con producto en producción
    calls: 2000,
    quality: 6.5,
    speed: 0,
    task: "score_global",
    onlyOpen: false,
    exclProprietary: false,
    onlyTested: false,        // Default OFF: muestra todos. Si marca, filtra a ≥50 runs
    onlyTools: false,         // Solo modelos con tool calling
    onlyThinking: false,      // Solo thinking models
    onlyMultimodal: false,    // Solo multimodal (texto + imagen/audio)
  },
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
  // Hero stats — mostramos modelos con AL MENOS 1 run (excluye los en cola)
  // para que el conteo coincida con lo que se muestra en el ranking
  const benchmarkedCount = state.data.models.filter(m => (m.runs || 0) > 0).length;
  document.getElementById("hero-runs").textContent =
    state.data.models.reduce((acc, m) => acc + (m.runs || 0), 0).toLocaleString();
  document.getElementById("hero-models").textContent = benchmarkedCount;
  document.getElementById("hero-updated").textContent =
    state.data.generated_at?.replace("T", " ") || "—";

  bindFilters();
  render();
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

  document.getElementById("task").addEventListener("change", e => {
    state.filters.task = e.target.value;
    render();
  });

  const checkboxMap = {
    onlyOpen: "only-open",
    exclProprietary: "excl-prop",
    onlyTested: "only-tested",
    onlyTools: "only-tools",
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

  // Presets de uso
  document.querySelectorAll(".preset-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const presetKey = btn.dataset.preset;
      const preset = PRESETS[presetKey];
      if (!preset) return;
      // Aplicar valores a los sliders + state
      ["budget", "calls", "quality", "speed"].forEach(k => {
        const el = document.getElementById(k);
        const out = document.getElementById(k + "-out");
        if (!el) return;
        el.value = preset[k];
        state.filters[k] = preset[k];
        // Re-format del output según el slider
        const formatters = {
          budget: v => `$${v}`,
          calls: v => Number(v).toLocaleString(),
          quality: v => Number(v).toFixed(1),
          speed: v => v,
        };
        if (out) out.textContent = formatters[k](preset[k]);
      });
      // Aplicar tarea
      const taskEl = document.getElementById("task");
      if (taskEl) {
        taskEl.value = preset.task;
        state.filters.task = preset.task;
      }
      // Marcar visualmente el preset activo
      document.querySelectorAll(".preset-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      render();
    });
  });
}

function costPerMonth(model, calls) {
  const ci = model.cost_input_per_M || 0;
  const co = model.cost_output_per_M || 0;
  return ((TOKENS_IN * ci) + (TOKENS_OUT * co)) * calls / 1_000_000;
}

function getScore(model, taskKey) {
  if (taskKey === "score_global") return model.score_global;
  return model.score_by_pillar?.[taskKey] ?? null;
}

function isProprietary(model) {
  return Object.values(PROPRIETARY_GROUPS).some(check => check(model));
}

function filterAndRank(models, f) {
  const passes = models.filter(m => {
    // Default: muestra todos los modelos (incluye parciales y en cola).
    // Si "Sólo cobertura completa" está marcado, filtra a >=50 runs.
    if (f.onlyTested && !m.tested) return false;
    // Modelos con runs=0 (en cola) no tienen score real — los ocultamos
    // siempre del ranking porque no se pueden ordenar.
    if ((m.runs || 0) === 0) return false;

    const score = getScore(m, f.task);
    if (score == null && m.runs > 0) return false;
    if (score != null && score < f.quality) return false;

    if (f.speed > 0 && (m.tokens_per_second || 0) < f.speed) return false;

    const cost = costPerMonth(m, f.calls);
    if (cost > f.budget) return false;

    if (f.onlyOpen && !m.open_source) return false;
    if (f.exclProprietary && isProprietary(m)) return false;

    // Filtros por capacidad
    if (f.onlyTools && !m.tool_calling) return false;
    if (f.onlyThinking && !m.thinking) return false;
    if (f.onlyMultimodal && !m.multimodal) return false;

    return true;
  });

  // Calcula costo mensual + score + ratio costo-beneficio para cada modelo
  passes.forEach(m => {
    const cost = costPerMonth(m, f.calls);
    const score = getScore(m, f.task) ?? 0;
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

function modelTags(m) {
  const tags = [];
  // Solo mostrar tag de OSS cuando aplica — "propietario" es default implícito
  // (si no es OS), no necesita tag explícito que agrega ruido visual
  if (m.open_source) tags.push(`<span class="tag os">${m.license || "OSS"}</span>`);
  // Capabilities (vienen del JSON, inferidas en export_for_pages.py)
  if (m.tool_calling) tags.push(`<span class="tag tools" title="Soporta tool calling">🔧 tools</span>`);
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
  summary.textContent = `${ranked.length} modelos cumplen tus criterios, ordenados por score (mayor a menor).`;

  // Sin límite — mostramos todos los que pasan los filtros.
  const top = ranked;
  const taskLabel = f.task === "score_global" ? "Global" : f.task;

  // Costo-beneficio: clasifica cada modelo según su eficiencia (score² / costo)
  // relativa al mejor de la lista filtrada actual. Etiquetas semánticas en
  // lugar de % para que el lector entienda de un vistazo si pagar la pena.
  const maxEfficiency = Math.max(...top.map(m => m._efficiency || 0));
  const formatEfficiency = (m) => {
    if (!m._efficiency || maxEfficiency === 0) return "—";
    if (m._cost_month <= 0.01 && m._task_score >= 6) {
      return `<span class="cb-badge cb-free" title="Cero costo + score decente — la mejor compra del mercado">★ Gratis</span>`;
    }
    const pct = Math.round((m._efficiency / maxEfficiency) * 100);
    let label, cls;
    if (pct >= 75)      { label = "Excelente"; cls = "cb-excellent"; }
    else if (pct >= 50) { label = "Bueno";     cls = "cb-good"; }
    else if (pct >= 25) { label = "Aceptable"; cls = "cb-ok"; }
    else                { label = "Caro";      cls = "cb-poor"; }
    return `<span class="cb-badge ${cls}" title="Costo-beneficio relativo a la mejor opción de la lista (eficiencia ${pct}%). Score² ÷ costo mensual.">${label}</span>`;
  };

  const html = `
    <table class="results-table">
      <thead>
        <tr>
          <th>#</th>
          <th>Modelo</th>
          <th class="num">Score ${taskLabel}</th>
          <th class="num">Costo/mes</th>
          <th class="num" title="Costo-beneficio relativo: score² / costo. 100% = mejor de la lista.">C/B</th>
          <th class="num">tok/s</th>
          <th>Tier</th>
        </tr>
      </thead>
      <tbody>
        ${top.map((m, i) => `
          <tr>
            <td class="num">${i + 1}</td>
            <td>
              <span class="model-name">${m.name}</span>
              <div class="model-meta">${modelTags(m)} · ${m.id}</div>
            </td>
            <td class="num">${scorePill(m._task_score)}</td>
            <td class="num">$${m._cost_month.toFixed(2)}</td>
            <td class="num">${formatEfficiency(m)}</td>
            <td class="num">${m.tokens_per_second?.toFixed(0) ?? "—"}</td>
            <td>${m.tier}</td>
          </tr>
        `).join("")}
      </tbody>
    </table>
  `;

  tableWrap.innerHTML = html;
}

document.addEventListener("DOMContentLoaded", load);
