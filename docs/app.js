// Calculadora de modelos IA — Cristian Tala
// Lee docs/data/models.json y aplica filtros con sliders

const TOKENS_IN = 300;
const TOKENS_OUT = 1500;

const PROPRIETARY_GROUPS = {
  anthropic: m => m.id?.includes("anthropic/") || m.id?.startsWith("claude"),
  openai: m => m.id?.startsWith("gpt-") || m.id?.startsWith("openai/") || m.provider === "openai_direct" || m.provider === "openai_responses",
  // Google propietarios: Gemini Flash/Pro (NO Gemma open-source)
  google_proprietary: m => /gemini[-_/]/i.test(m.id || "") && !m.open_source,
};

const state = {
  data: null,
  filters: {
    budget: 50,
    calls: 2000,
    quality: 6.5,
    speed: 0,
    task: "score_global",
    onlyOpen: false,
    exclProprietary: false,
    includeIncomplete: false, // Default OFF: solo cobertura completa (≥50 runs)
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
  // Hero stats
  document.getElementById("hero-runs").textContent =
    state.data.models.reduce((acc, m) => acc + (m.runs || 0), 0).toLocaleString();
  document.getElementById("hero-models").textContent = state.data.tested_count;
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
    includeIncomplete: "include-incomplete",
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
    // Default: solo modelos con cobertura completa (≥50 runs).
    // Si el usuario activa "incluir no probados", se muestran todos.
    if (!f.includeIncomplete && !m.tested) return false;

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

  // Score "match": balance calidad / costo. Usamos quality * (1 + budget_room).
  passes.forEach(m => {
    const cost = costPerMonth(m, f.calls);
    const score = getScore(m, f.task) ?? 0;
    const budgetRatio = cost > 0 ? (f.budget - cost) / f.budget : 1;
    m._cost_month = cost;
    m._task_score = score;
    m._match = score * (0.7 + 0.3 * Math.max(0, budgetRatio));
  });

  return passes.sort((a, b) => (b._match - a._match));
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
  if (m.open_source) tags.push(`<span class="tag os">${m.license || "OSS"}</span>`);
  else tags.push(`<span class="tag">propietario</span>`);
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
  summary.textContent = `${ranked.length} modelos cumplen tus criterios. Top 15 ordenados por mejor balance calidad/costo.`;

  const top = ranked.slice(0, 15);
  const taskLabel = f.task === "score_global" ? "Global" : f.task;

  const html = `
    <table class="results-table">
      <thead>
        <tr>
          <th>#</th>
          <th>Modelo</th>
          <th class="num">Score ${taskLabel}</th>
          <th class="num">Costo/mes</th>
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
