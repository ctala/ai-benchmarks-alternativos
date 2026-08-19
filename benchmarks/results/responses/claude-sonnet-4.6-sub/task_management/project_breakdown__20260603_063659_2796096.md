# Claude Sonnet 4.6 (suscripción) — task_management/project_breakdown

- model_id: `claude-sonnet-4-6`
- success: True  | final: 7.6 | quality: 10.0
- latency_total: 44.599s | tokens_per_second: 56.2
- input_tokens: 3 | output_tokens: 2506
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Respuesta completa

# 🚀 Plan de Lanzamiento: Landing Page SaaS Gestión de Inventario
**Equipo:** 1 Diseñador (D), 2 Developers (Dev1, Dev2), 1 Copywriter (CW) | **Deadline:** 4 semanas

---

## FASE 1 — Fundamentos (Días 1–5)
*Todos los entregables de esta fase son prerequisito para todo lo demás.*

| # | Tarea | Responsable | Duración | Depende de |
|---|-------|-------------|----------|------------|
| 1.1 | Kick-off: definir ICP, propuesta de valor, CTA principal y métricas de éxito | Todos | 2h (día 1) | — |
| 1.2 | Investigación de competidores y benchmarking visual | CW + D | 1 día | 1.1 |
| 1.3 | Definir estructura de secciones (wireframe de texto) | CW | 1 día | 1.1 |
| 1.4 | Elegir stack técnico: hosting, CMS/estático, formulario de waitlist, analytics | Dev1 | 1 día | 1.1 |
| 1.5 | Setup del repositorio, CI/CD básico y entorno de staging | Dev1 + Dev2 | 1 día | 1.4 |
| 1.6 | Briefing creativo formal entregado al diseñador | CW → D | Día 3 | 1.2, 1.3 |

**✅ Hito Fase 1:** Wireframe de texto aprobado + repo corriendo en staging.

---

## FASE 2 — Diseño y Copy (Días 6–13)
*Diseño y Copy corren en paralelo; se sincronizan al final.*

### Copy (CW) — Días 6–10
| # | Tarea | Entregable |
|---|-------|------------|
| 2.1 | Hero: headline, subheadline, CTA | Texto final aprobado |
| 2.2 | Sección de problema / dolor | Texto final |
| 2.3 | Features + beneficios (3–5 bloques) | Texto final |
| 2.4 | Social proof: testimonios placeholder o reales, logos clientes | Textos + assets |
| 2.5 | FAQ (8–10 preguntas) | Texto final |
| 2.6 | CTA final + microcopy (formulario, botones, errores) | Texto final |
| 2.7 | Meta title, meta description, OG tags | SEO copy |

### Diseño (D) — Días 6–13
| # | Tarea | Entregable | Depende de |
|---|-------|------------|------------|
| 2.8 | Moodboard y definición de paleta/tipografía | Guía de estilo v1 | 1.6 |
| 2.9 | Diseño mobile-first en Figma: Hero + Nav | Frame aprobado | 2.8 |
| 2.10 | Diseño: Features, Problema, Social proof | Frames aprobados | 2.9 |
| 2.11 | Diseño: FAQ, Footer, CTA final | Frames aprobados | 2.10 |
| 2.12 | Revisión de copy integrado en diseño | Figma con textos reales | 2.6, 2.11 |
| 2.13 | Export de assets optimizados (SVG, WebP) | Assets listos para dev | 2.12 |

**✅ Hito Fase 2 (Día 13):** Figma con copy real aprobado por stakeholders. Assets exportados.

> ⚠️ **Dependencia crítica:** Dev no empieza a maquetar hasta tener el Figma aprobado (2.13). Los developers usan los días 6–13 para infraestructura (ver Fase 2b).

### Fase 2b — Infra en paralelo (Dev1 + Dev2, Días 6–13)
| # | Tarea | Responsable |
|---|-------|-------------|
| 2b.1 | Setup de componentes base (design tokens, grid, botones) | Dev2 |
| 2b.2 | Integración formulario waitlist (email + validación + backend/servicio) | Dev1 |
| 2b.3 | Setup de analytics (GA4 / Plausible) y eventos clave | Dev1 |
| 2b.4 | Configurar dominio, SSL y pipeline deploy a producción | Dev2 |

---

## FASE 3 — Desarrollo (Días 14–21)

| # | Tarea | Responsable | Depende de |
|---|-------|-------------|------------|
| 3.1 | Maquetación Hero + Nav (pixel-perfect) | Dev2 | 2.13 |
| 3.2 | Maquetación Features + Problema | Dev1 | 2.13 |
| 3.3 | Maquetación Social proof + FAQ + Footer | Dev2 | 3.1 |
| 3.4 | Integrar formulario con maqueta final | Dev1 | 2b.2, 3.2 |
| 3.5 | Animaciones y micro-interacciones (scroll, hover) | Dev2 | 3.3 |
| 3.6 | Optimización de performance: lazy load, compresión, fonts | Dev1 | 3.1–3.3 |
| 3.7 | SEO técnico: schema.org, sitemap.xml, robots.txt, OG/Twitter cards | Dev1 | 2.7 |
| 3.8 | Revisión cross-browser y responsive (mobile/tablet/desktop) | Dev1 + Dev2 | 3.1–3.5 |

**✅ Hito Fase 3 (Día 21):** Landing completa en staging, funcional y responsive.

---

## FASE 4 — QA, Ajustes y Lanzamiento (Días 22–28)

| # | Tarea | Responsable | Duración |
|---|-------|-------------|----------|
| 4.1 | Testing funcional completo (formulario, links, analytics) | Dev1 | 1 día |
| 4.2 | Revisión de copy final en contexto real (staging) | CW | 1 día |
| 4.3 | Revisión diseño vs. implementación (pixel-perfect check) | D | 1 día |
| 4.4 | Correcciones priorizadas post-QA | Dev1 + Dev2 | 1–2 días |
| 4.5 | Test de velocidad: Lighthouse ≥90 en mobile | Dev1 | 0.5 días |
| 4.6 | Deploy a producción + verificación en vivo | Dev1 + Dev2 | Día 27 |
| 4.7 | Submit a Google Search Console + IndexNow | Dev1 | Día 28 |
| 4.8 | Anuncio de lanzamiento (redes, email, Product Hunt si aplica) | CW | Día 28 |

**✅ Hito Final (Día 28):** Landing en producción, indexada, con waitlist activa.

---

## 📊 Timeline Visual

```
Semana 1    Semana 2         Semana 3         Semana 4
|-----------|----------------|-----------------|---------|
D1-5        D6          D13  D14         D21  D22    D28
[FASE 1 ─]
            [─ COPY (CW) ─────]
            [─ DISEÑO (D) ──────────────]
            [─ INFRA (Dev) ──────────────]
                                [─ DEV (Dev1+Dev2) ─]
                                                    [QA+LAUNCH]
```

---

## ⚠️ Riesgos y Mitigaciones

| Riesgo | Probabilidad | Mitigación |
|--------|-------------|------------|
| Diseño rechazado → retraso en dev | Alta | Checkpoint de aprobación en Día 10 (no esperar al 13) |
| Copy que no encaja en diseño | Media | CW y D sincronizan diariamente en Fase 2 |
| Formulario con bugs en prod | Media | Testear en staging con emails reales en Fase 3 |
| Scope creep (agregar features last minute) | Alta | Todo lo que no esté en Fase 1 va al backlog post-lanzamiento |
| Lighthouse bajo por imágenes pesadas | Baja | D exporta en WebP ≤100KB por imagen desde el inicio |

---

## 📌 Reglas de Operación

1. **Standup diario de 15 min** — bloqueos visibles el mismo día
2. **Aprobaciones en 24h** — sin feedback en 24h = aprobado implícitamente
3. **Staging siempre actualizado** — cada merge va a staging automáticamente
4. **Feature freeze día 22** — zero features nuevas en Fase 4
5. **CW es dueño del tono**, D es dueño del visual, Dev1 es tech lead, Dev2 ejecuta