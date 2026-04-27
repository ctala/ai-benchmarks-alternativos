# Agentes del proyecto

Agentes pre-hechos descargados a `.claude/agents/` que sirven como **plantillas/referencia** para invocar via `Agent` tool. En esta versión de Claude Code los `.md` locales no se registran auto como `subagent_type` invocable hasta reload — mientras tanto se invocan via `general-purpose` pasando el contenido del agente como contexto.

## SEO + Marketing (7 agentes)

Para optimización del repositorio, contenido SEO, y marketing del benchmark.

| Agente | Para qué |
|---|---|
| **seo-content-writer** | Escribir blog posts SEO optimizados sobre los hallazgos del benchmark |
| **seo-content-auditor** | Auditar contenido existente (README, MODELOS, landing pages) y proponer mejoras |
| **seo-keyword-strategist** | Identificar keywords del nicho "AI benchmarks", "LLM comparison", "alternativas LLM" |
| **seo-structure-architect** | Estructurar README + MODELOS + DESCUBRIMIENTOS para SEO + escaneabilidad |
| **seo-meta-optimizer** | Optimizar meta tags HTML de la calculadora (Open Graph, schema.org) |
| **content-marketer** | Posts para LinkedIn, Skool, newsletter, redes desde los benchmarks |
| **search-specialist** | Research competitivo + scout de modelos nuevos del mercado |

## Análisis y Documentación (4 agentes — abril 2026)

Para análisis cuantitativo del benchmark y documentación profunda.

| Agente | Para qué |
|---|---|
| **data-scientist** | Análisis estadístico de los JSON results: correlaciones, outliers, regresiones cross-lote, Pareto frontier calidad/costo. Genera `INSIGHTS.md` |
| **business-analyst** | Convierte hallazgos cuantitativos en decisiones de negocio para emprendedores: break-even por perfil, ROI por caso de uso, frameworks de decisión |
| **docs-architect** | Documentación técnica de profundidad. Genera `ARQUITECTURA.md` con explicación deep del runner, scoring v2, LLM-as-Judge, decisiones de diseño |
| **tutorial-engineer** | Tutoriales paso a paso para emprendedores: replicar benchmark, agregar modelo, diseñar tests custom, configurar Phi-4 judge |

## Estrategia y Curación (4 agentes custom — abril 26)

Específicos al repo (no en wshobson/agents). Escritos desde cero con contexto profundo del proyecto, marca personal de Cristian, audiencia LATAM.

| Agente | Para qué |
|---|---|
| **repo-strategist** | Decisiones de roadmap, priorización entre features competing, alineación con marca personal y comunidad Skool. Análisis multi-lente (user/repo/brand/competition). Modelo: Opus |
| **test-designer** | Diseña nuevos tests basados en casos REALES (no académicos). Identifica gaps (multimodal, long context, tool use real con búsqueda web). Decide re-correr modelos. Modelo: Opus |
| **model-curator** | Decide qué modelos del mercado vale agregar al benchmark, cuáles deprecar, cómo balancear cobertura. Pareto frontier check + gap analysis. Modelo: Opus |
| **calculator-optimizer** | UX/CRO/performance de la calculadora en benchmarks.cristiantala.com. Lighthouse audits, friction analysis, drill-down, mobile-first. Modelo: Sonnet |

Todos los agentes tienen `Use PROACTIVELY` en su description — Claude Code los invocará automáticamente cuando el contexto matchee (post-reload).

## Estrategia de uso por fase

### Fase 1 — Inteligencia del benchmark
Trigger: cuando se modifica `benchmarks/results/*.json`
- **data-scientist** → `INSIGHTS.md` (análisis cuantitativo)
- **business-analyst** → traduce insights a recomendaciones accionables

### Fase 2 — Documentación de profundidad
Trigger: cambio de arquitectura, providers, scoring
- **docs-architect** → `ARQUITECTURA.md`
- **tutorial-engineer** → `tutoriales/` con guías step-by-step

### Fase 3 — Contenido SEO desde insights
Trigger: cuando hay INSIGHTS.md nuevo
- **seo-keyword-strategist** → research keywords objetivo
- **seo-content-writer** → blog posts desde hallazgos
- **content-marketer** → adapta a LinkedIn / Skool / newsletter / Twitter

### Fase 4 — Optimización continua
Trigger: pre-commit cuando cambia README/landing pages
- **seo-content-auditor** → audits cada 2 semanas
- **seo-meta-optimizer** → optimiza meta tags HTML
- **seo-structure-architect** → reorganiza si docs crecen mucho

## Cómo invocarlos

**Hoy** (sin reload, via general-purpose):

```python
Agent({
  description: "Análisis cuantitativo benchmark",
  subagent_type: "general-purpose",
  prompt: "Sos un data-scientist. [pegar prompt + contexto]..."
})
```

**Post-reload de Claude Code** (cuando registre los .md locales):

```python
Agent({
  description: "Análisis cuantitativo benchmark",
  subagent_type: "data-scientist",
  prompt: "Generá INSIGHTS.md con análisis de los 7 lotes consolidados..."
})
```

## Próximos agentes que se ajustarían

| Agente potencial | Categoría wshobson | Para qué |
|---|---|---|
| `social-media-content-creator` | (custom) | Posts X/Twitter, IG, TikTok desde insights |
| `youtube-script-writer` | (custom) | Scripts para canal YouTube de Cristian |
| `email-marketer` | (custom) | Newsletter automation desde insights |
| `code-reviewer` | code-documentation | Review pre-commit del código del benchmark |
| `python-pro` | python-development | Refactor del runner cuando crezca |
| `community-manager` | (custom) | Engagement de comunidad Skool desde benchmark insights |

## Fuentes

- **Pre-hechos**: <https://github.com/wshobson/agents> (78+ plugins, 25 categorías)
- Catálogos alternativos:
  - <https://github.com/hesreallyhim/awesome-claude-code-agents> — más limitado (6 agentes)
  - SEO específicos están solo en wshobson/agents
