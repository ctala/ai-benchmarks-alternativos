# Tencent Hy4 — task_management/project_breakdown

- model_id: `tencent/hy4`
- success: True  | final: 8.5 | quality: 9.8
- latency_total: 29.708s | tokens_per_second: 91.3
- input_tokens: 96 | output_tokens: 2713
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Perfecto. Aquí tienes un plan de trabajo realista, ajustado a 4 semanas, con un equipo pequeño (1 diseñador, 2 devs, 1 copywriter), pensado para evitar cuellos de botella y llegar al lanzamiento con calidad sin quemar al equipo.

Te lo estructuro en **fases → tareas → dependencias → responsables → timeline**, más un par de recomendaciones críticas al final.

---

## 🎯 Supuestos previos (ajustables)
- Producto ya tiene **nombre, propuesta de valor y pricing definidos**.
- Se usa un stack simple (Next.js / Astro + Tailwind + CMS opcional tipo Sanity o incluso Markdown).
- No se integra aún con backend real de inventario (la landing es **captación + demo / waitlist**).
- Formulario conectado a HubSpot / Mailchimp / Supabase (API simple).
- Dominio y hosting ya disponibles o se gestionan en paralelo.

---

## 🗺️ Visión general del timeline (4 semanas)

| Semana | Foco | Entregable clave |
|------|------|------------------|
| 1 | Estrategia + Copy + Wireframes | Copy aprobado + wireframe + sistema visual |
| 2 | Diseño UI + Arquitectura técnica | Diseño final + repo + componentes base |
| 3 | Implementación + Integraciones | Landing funcional en staging |
| 4 | QA, performance, SEO, launch | 🚀 Producción + analítica activa |

---

# FASE 1 · Definición & Contenido (Semana 1)

| # | Tarea | Responsable | Depende de | Output |
|---|-------|-------------|------------|--------|
| 1.1 | Kick-off: objetivo, audiencia, CTA principal (Demo / Waitlist) | Todo el equipo + Producto | — | 1-pager de brief |
| 1.2 | Mapa de mensajes (Hero, dolor, beneficios, prueba social, FAQ, CTA) | Copywriter | 1.1 | Message map |
| 1.3 | Copy completo (ES, tono B2B claro, sin jargon) | Copywriter | 1.2 | `copy.md` v1 |
| 1.4 | Revisión copy con Producto + Devs (viabilidad técnica de claims) | Copywriter + Devs | 1.3 | Copy v2 aprobado |
| 1.5 | Wireframe low-fi (estructura de secciones + jerarquía) | Diseñador | 1.2, 1.4 | Figma wireframe |
| 1.6 | Definición de tokens visuales (color, tipografía, botones, espaciado) | Diseñador | 1.1 | Style tile |
| 1.7 | Setup repo, entorno local, convenciones (Git, branches, lint) | Dev 1 | 1.1 | Repo + `README` |

📌 **Hito Semana 1**: ✅ Copy aprobado + wireframe validado + repo listo.

💡 *Tip*: El copy se aprueba **antes** del diseño final. Evita rediseños por cambios de texto.

---

# FASE 2 · Diseño & Arquitectura (Semana 2)

| # | Tarea | Responsable | Depende de | Output |
|---|-------|-------------|------------|--------|
| 2.1 | UI high-fi desktop (Hero, Features, Cómo funciona, Pricing, FAQ, Footer) | Diseñador | 1.5, 1.6 | Figma v1 |
| 2.2 | Variantes mobile + tablet | Diseñador | 2.1 | Responsive specs |
| 2.3 | Assets: iconos, ilustración abstracta / mockup del dashboard | Diseñador | 2.1 | SVG / WebP optimizados |
| 2.4 | Handoff a devs (especificaciones, estados hover, breakpoints) | Diseñador + Devs | 2.2, 2.3 | Figma Dev Mode listo |
| 2.5 | Arquitectura de componentes (Header, Hero, FeatureCard, CTAForm, FAQ Accordion) | Dev 1 | 1.7, 2.4 | Estructura `components/` |
| 2.6 | Implementación sistema de diseño (Tailwind config / CSS vars) | Dev 1 | 2.4, 2.5 | `theme.ts` |
| 2.7 | Elección + setup de formulario (endpoint, validación, spam) | Dev 2 | 1.1 | API route / webhook test |
| 2.8 | Definición eventos de analítica (click CTA, scroll, form submit) | Dev 2 + Copy | 1.4 | `analytics.md` |

📌 **Hito Semana 2**: ✅ Diseño final + componentes base + formulario funcionando en local.

💡 *Tip*: Dev 2 trabaja en paralelo con Dev 1 (form + analítica) para no bloquear la UI.

---

# FASE 3 · Implementación (Semana 3)

| # | Tarea | Responsable | Depende de | Output |
|---|-------|-------------|------------|--------|
| 3.1 | Maquetación Hero + Header + CTA sticky | Dev 1 | 2.6 | Sección 1 live |
| 3.2 | Secciones Features / Cómo funciona (con assets) | Dev 1 | 2.3, 3.1 | Secciones 2–3 |
| 3.3 | Pricing + FAQ (accesible, accordion keyboard-friendly) | Dev 2 | 2.4, 2.6 | Secciones 4–5 |
| 3.4 | Integración real del formulario + estados (loading, error, success) | Dev 2 | 2.7, 3.1 | CTA funcional |
| 3.5 | SEO técnico: meta, OG, schema `SoftwareApplication`, sitemap, robots | Dev 2 | 1.4 | `head.tsx` + `sitemap.xml` |
| 3.6 | Analítica (GA4 / Plausible) + eventos definidos | Dev 2 | 2.8 | Dashboard test |
| 3.7 | Deploy a staging (Vercel / Netlify preview) | Dev 1 | 3.1–3.6 | URL staging |
| 3.8 | Revisión visual cross-browser (Chrome, Safari, Firefox) | Diseñador | 3.7 | Lista de fixes |

📌 **Hito Semana 3**: ✅ Landing completa en staging, formulario y analítica funcionando.

💡 *Tip*: No dejes SEO ni analítica para el último día. Son silenciosos pero críticos.

---

# FASE 4 · QA, Optimización & Launch (Semana 4)

| # | Tarea | Responsable | Depende de | Output |
|---|-------|-------------|------------|--------|
| 4.1 | Fixes visuales del diseñador | Dev 1 | 3.8 | UI pulida |
| 4.2 | QA funcional: form, validaciones, mobile real, teclado | Dev 2 | 3.7 | Checklist OK |
| 4.3 | Performance: LCP < 2.5s, imágenes next/image, lazy load | Dev 1 | 4.1 | Lighthouse ≥ 90 |
| 4.4 | Accesibilidad básica (contraste, aria, focus visible) | Diseñador + Dev 2 | 4.1 | Axe sin errores críticos |
| 4.5 | Copy final review (typos, CTA coherente, legal / privacidad) | Copywriter | 1.4, 4.1 | Copy vFinal |
| 4.6 | Textos legales + link a política de privacidad | Copywriter + Dev 2 | 4.5 | Footer OK |
| 4.7 | Config dominio, SSL, redirects, env vars prod | Dev 1 | 3.7 | Prod ready |
| 4.8 | Smoke test en producción (form real, evento analítico real) | Dev 2 + Copy | 4.7 | ✅ Confirmado |
| 4.9 | 🚀 Launch + comunicado interno / email / LinkedIn | Todo el equipo | 4.8 | Live |
| 4.10 | Monitorización 24–48h (errores, conversions, logs) | Dev 2 | 4.9 | Reporte post-launch |

📌 **Hito Semana 4**: ✅ **Landing en producción con métricas activas**.

---

## 🔗 Mapa de dependencias (resumen)

```
Brief → Copy → Wireframe → UI → Componentes → Secciones → Staging → QA → Prod
          ↓        ↓          ↓         ↓            ↓
       Tokens   Assets   Form API   SEO/Analytics   Fixes
```

**Cadena crítica**: `Copy → Wireframe → UI → Dev 1 → Staging → QA → Launch`  
**Paralelo seguro**: Dev 2 (form + SEO + analítica) desde Semana 2.

---

## 👥 Carga de trabajo por rol (realista)

| Rol | Sem 1 | Sem 2 | Sem 3 | Sem 4 |
|----|-------|-------|-------|-------|
| Copywriter | 🔴 Alto | 🟡 Revisión | 🟢 Bajo | 🟡 Final + legal |
| Diseñador | 🟡 Wire | 🔴 UI + assets | 🟡 Review | 🟡 QA visual / a11y |
| Dev 1 | 🟢 Setup | 🔴 Sistema + Hero | 🔴 Secciones + perf | 🔴 Fixes + deploy |
| Dev 2 | 🟢 Setup | 🟡 Form + eventos | 🔴 Pricing + SEO + analytics | 🔴 QA + monitoring |

---

## ⚠️ Riesgos & mitigaciones (importante)

| Riesgo | Mitigación |
|------|-----------|
| Cambios de copy en Semana 3 | Congelar copy al final Semana 1 (versionar `copy.md`) |
| Mockup del producto “bonito” pero falso | Usar UI real capturada o ilustración abstracta, no prometer lo que no hay |
| Formulario falla el día del launch | Test con endpoint real en Semana 3 + smoke test 4.8 |
| Diseñador bloqueado por devs | Handoff en Dev Mode + tokens desde Semana 2 |
| Scope creep (“y si añadimos blog…”) | ❌ Fuera de scope. Post-launch backlog |

---

## 🧩 Recomendación extra (muy SaaS)

Añade **una sola micro-interacción con valor**, no más:
> Un mini “calculadora de ahorro” (ej. *“¿Cuántas horas pierdes al mes reconteando stock?”* → input → resultado estimado → CTA).

- Dev 2 lo puede hacer en ~½ día en Semana 3.
- Sube conversión más que un slider de logos inventados.

---

## ✅ Entregables finales checklist

- [ ] Landing responsive (mobile-first)
- [ ] Formulario captando leads reales
- [ ] SEO + OG para compartir en LinkedIn
- [ ] Analítica con eventos de CTA
- [ ] Lighthouse ≥ 90 (Perf / A11y / SEO)
- [ ] Política de privacidad enlazada
- [ ] URL prod + monitorización activa

---

Si quieres, en el siguiente paso te puedo:
- 📄 Pasar esto a **Notion / Jira / Trello-ready** (con tickets y estimaciones en horas)
- 🧪 Redactar el **copy base del Hero + CTA** para que el copywriter arranque ya
- 📊 Definir los **6 eventos exactos de GA4** para medir conversión

Dime cuál prefieres y lo armamos. 🚀