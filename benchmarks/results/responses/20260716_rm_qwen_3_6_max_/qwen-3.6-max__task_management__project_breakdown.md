# Qwen 3.6 Max — task_management/project_breakdown

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 8.08 | quality: 10.0
- latency_total: 99.204s | tokens_per_second: 44.6
- input_tokens: 76 | output_tokens: 4424
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Respuesta completa

Aquí tienes un plan de proyecto realista, optimizado para un equipo de 4 personas y un plazo de 4 semanas (20 días hábiles). Está estructurado para minimizar cuellos de botella, permitir trabajo en paralelo y mantener márgenes de seguridad.

---
## 📅 CRONOGRAMA GENERAL (4 SEMANAS / 20 DÍAS HÁBILES)

| Semana | Foco Principal | Entregables Clave |
|--------|----------------|-------------------|
| **1** | Estrategia, estructura y contenidos base | Sitemap, wireframes, copy v1, repo & CI/CD listo |
| **2** | Diseño UI y maquetación inicial | UI final (desktop/mobile), copy v2, estructura frontend |
| **3** | Integraciones, optimización y QA | Formularios, analíticas, SEO técnico, Lighthouse ≥90, QA cruzado |
| **4** | Pulido, staging y lanzamiento | Deploy producción, verificación post-lanzamiento, documentación |

---
## 🧩 DESGLOSE POR FASES, TAREAS, DEPENDENCIAS Y RESPONSABLES

### 🔹 SEMANA 1: Planificación, Estructura y Contenidos Base (Días 1-5)
| Tarea | Días | Dependencias | Responsable | Notas |
|-------|------|--------------|-------------|-------|
| Kickoff: objetivos, audiencia, KPIs, stack técnico, hosting | D1 | - | Todo el equipo | Definir métricas de éxito y alcance mínimo viable |
| Sitemap + wireframes low-fidelity | D1-2 | Kickoff | Diseñador | Foco en jerarquía de conversión, no en estética |
| Copy v1: Hero, beneficios, features, pricing, CTA, FAQs, meta SEO | D1-3 | Kickoff | Copywriter | Usar framework PAS o AIDA. Incluir tono y voz |
| Revisión cruzada copy ↔ wireframes + ajustes v1 | D3 | Wireframes + copy v1 | Diseñador + Copywriter | Máximo 1 ronda de feedback |
| Setup técnico: repo, CI/CD, estructura de proyecto, stubs de analíticas | D3-5 | Kickoff | Developers (2) | Elegir framework ligero (Next.js, Astro, o HTML/CSS/JS) |

**✅ Gate de aprobación D5:** Wireframes + copy v1 + entorno dev listos.

---

### 🔹 SEMANA 2: Diseño UI y Desarrollo Inicial (Días 6-10)
| Tarea | Días | Dependencias | Responsable | Notas |
|-------|------|--------------|-------------|-------|
| UI high-fidelity (desktop + mobile) + design system básico | D6-8 | Wireframes aprobados | Diseñador | Exportar assets optimizados. Evitar animaciones complejas |
| Copy v2 (final) + textos legales/privacidad/cookies | D6-7 | Copy v1 + feedback | Copywriter | Incluir microcopy para formularios y estados de error |
| Aprobación formal de diseño + copy | D8 | UI + copy v2 | Todo el equipo | **Punto de no retorno para cambios mayores** |
| Maquetación responsive + integración de copy + componentes base | D6-10 | Setup técnico + UI/copy aprobados | Developers | Dev1: estructura/componentes. Dev2: responsive/assets |

**✅ Gate de aprobación D10:** Landing maquetada al 70%, diseño y copy congelados.

---

### 🔹 SEMANA 3: Integraciones, Optimización y QA (Días 11-15)
| Tarea | Días | Dependencias | Responsable | Notas |
|-------|------|--------------|-------------|-------|
| Integraciones: formularios, CRM/email, enlaces pricing/demo, cookies | D11-13 | Maquetación base | Developers | Usar servicios serverless o SaaS (Formspree, HubSpot, etc.) |
| Optimización: imágenes WebP/AVIF, lazy load, minificación, caching | D12-14 | Integraciones en curso | Developers | Objetivo: Lighthouse Performance ≥90, CLS <0.1 |
| SEO técnico: meta tags, Open Graph, schema.org, sitemap.xml, robots.txt | D13 | Copy final + estructura | Developers + Copywriter | Validar con Rich Results Test |
| QA cross-browser/device + accesibilidad básica (WCAG 2.1 AA) | D13-15 | Maquetación + integraciones | Developers + Diseñador | BrowserStack o similares. Checklist de contraste y focus |
| Revisión final de contenido, microcopy y estados UI | D14-15 | QA en curso | Copywriter + Diseñador | Corregir typos, alineación, espaciado, mensajes de error |

**✅ Gate de aprobación D15:** QA firmado, rendimiento validado, listo para staging.

---

### 🔹 SEMANA 4: Pulido, Staging y Lanzamiento (Días 16-20)
| Tarea | Días | Dependencias | Responsable | Notas |
|-------|------|--------------|-------------|-------|
| Fixes de QA + ajustes finales de diseño/copy | D16-17 | Reporte QA | Todo el equipo | Solo cambios críticos. Congelar alcance |
| Deploy a staging + revisión final interna | D18 | Fixes completados | Developers + Todo el equipo | Validar flujos, analíticas, responsive, velocidad |
| Deploy a producción + DNS/SSL + verificación analíticas | D19 | Staging aprobado | Developers | Configurar redirecciones, HTTPS, GA4/Meta Pixel |
| Smoke test post-lanzamiento + documentación + monitoreo 48h | D20 | Producción live | Todo el equipo | Registrar KPIs iniciales, plan de iteración v1.1 |

**🚀 Lanzamiento:** Día 19-20. Incluye 1-2 días de colchón para imprevistos.

---
## 🔗 MATRIZ DE DEPENDENCIAS CRÍTICAS
```
Kickoff → Wireframes + Copy v1 → UI + Copy v2 → Aprobación D8
                                      ↓
Setup Técnico → Maquetación → Integraciones → Optimización → QA → Fixes → Staging → Producción
```
- **Cuellos de botella típicos:** Revisiones infinitas de diseño/copy, integraciones de terceros mal documentadas, QA tardío.
- **Mitigación:** Congelar alcance en D8, usar servicios SaaS para formularios/CRM, iniciar QA en paralelo con desarrollo final.

---
## 🛡️ RECOMENDACIONES PARA CUMPLIR EL PLAZO

1. **Alcance mínimo viable (MVP Landing):**
   - Hero + propuesta de valor
   - 3-4 beneficios/features con iconos
   - Pricing o CTA a demo
   - Testimonios/logos (opcional pero recomendado)
   - FAQ breve
   - Footer + legal
   - *Excluir en v1:* Animaciones complejas, blog, multiidioma, dashboard embebido.

2. **Herramientas recomendadas para velocidad:**
   - Framework: Astro o Next.js (SSG/ISR) + Tailwind CSS
   - Hosting: Vercel, Netlify o Cloudflare Pages (deploy automático)
   - Formularios/CRM: Formspree, Tally, HubSpot Free o Make/Zapier
   - Analíticas: GA4 + Plausible/Fathom (ligero) + Meta Pixel
   - QA: BrowserStack, Lighthouse CI, WAVE Accessibility

3. **Gestión de trabajo:**
   - Daily sync de 15 min (bloqueos, progreso, siguientes pasos)
   - Tablero Kanban (Notion/Jira/Trello) con columnas: `Backlog → En progreso → Revisión → Aprobado → Done`
   - Regla de oro: **Máximo 2 rondas de feedback por entregable**. Cambios después de D8 solo si son críticos para conversión o legales.

4. **Plan de contingencia:**
   - Si el diseño se retrasa: usar UI kit profesional (Tailwind UI, Shadcn, o Figma Community) y adaptar.
   - si las integraciones fallan: lanzar con formulario estático + email forwarding y conectar CRM en semana 5.
   - Si QA revela problemas de rendimiento: desactivar animaciones, comprimir assets, diferir scripts no críticos.

---
## 📊 ENTREGABLES FINALES ESPERADOS
- Landing page responsive, optimizada y accesible
- Copy final alineado a propuesta de valor SaaS
- Analíticas y píxeles verificados
- Documentación técnica y de contenido
- Reporte Lighthouse ≥90 en Performance/SEO/Best Practices
- Plan de iteración post-lanzamiento (A/B testing, heatmaps, CRO)

¿Quieres que te genere una plantilla de Kanban lista para importar en Notion/Jira, o un checklist de QA específico para landing pages SaaS?