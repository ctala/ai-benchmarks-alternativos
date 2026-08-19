# Nemotron 3 Ultra 550B — task_management/project_breakdown

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 37.195s | tokens_per_second: 120.1
- input_tokens: 83 | output_tokens: 4466
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y realista del proyecto con principios clave y un desglose detallado por tareas.

## Respuesta completa

Este es un plan de ejecución **realista y agresivo** para 4 semanas (20 días laborables). La clave para cumplir la fecha es **paralelizar al máximo** (Copy + Design simultáneo desde Día 1) y **evitar el "waterfall" estricto** (esperar a que todo el diseño esté listo para codear).

---

### 🎯 Principios Clave para 4 Semanas
1.  **Mobile-First & Component-Based:** Diseñan y desarrollan por componentes (Hero, Features, Pricing, Footer), no por páginas completas.
2.  **Content-First:** El Copywriter entrega *wireframes de contenido* (texto real) antes de que el Diseñador abra Figma.
3.  **Code Review Diario:** 15 min al final del día para evitar deuda técnica.
4.  **Definición de "Done":** Código en `main`, deployado en Staging, validado en móvil/desktop, accesibilidad básica (AA), analytics disparando.

---

## 📦 FASES Y TIMELINE (Visión General)

| Semana | Foco Principal | Entregable Clave (Viernes) |
| :--- | :--- | :--- |
| **Semana 1** | **Estrategia, Copy & Arquitectura** | Wireframes validados + Copy final (Desktop/Mobile) + Design System base + Repo inicializado |
| **Semana 2** | **Diseño UI & Desarrollo Core** | Página completa en Figma (Desktop/Mobile) + Hero + Features + Nav/Footer codeados en Staging |
| **Semana 3** | **Desarrollo Completo & Integraciones** | Landing 100% funcional en Staging (Formularios, SEO, Analytics, A/B ready) |
| **Semana 4** | **QA, Performance, Launch Prep** | **PRODUCCIÓN LIVE** (Lunes/Martes) + Buffer (Miér/Juev) + Post-Launch (Viernes) |

---

## 📋 DESGLOSE DETALLADO POR TAREAS

### FASE 1: FUNDACIÓN Y CONTENIDO (Semana 1 - Días 1-5)
*Objetivo: Saber **qué** decimos y **cómo** se estructura antes de pintar píxeles.*

| ID | Tarea | Responsable | Dependencias | Entregable / Criterio de Aceptación |
| :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Kickoff & Definición de MVP Scope** | **Todos (Lead: PM/Founder)** | Ninguna | Doc 1-pager: Value Prop, ICP, 3 Key Features, Objetivo conversión (Demo/Waitlist), Competidores. |
| **1.2** | **Keyword Research & SEO Structure** | **Copywriter** | 1.1 | Mapa de keywords (Head/Long-tail), Meta Title/Desc propuestos, H1/H2 structure. |
| **1.3** | **Copywriting: Wireframes de Contenido (Low-Fi)** | **Copywriter** | 1.1, 1.2 | **FigJam/Notion:** Texto real para: Hero, Value Props, Features (3-5), Social Proof (logos/testimonios placeholder), Pricing/Plans, FAQ, Footer, CTA states. *Validación con stakeholders antes del Día 3.* |
| **1.4** | **Arquitectura Técnica & Setup Repo** | **Dev 1 (Lead)** | 1.1 | Repo GitHub (Next.js/Astro/Remix + Tailwind/Shadcn), CI/CD (Vercel/Netlify), Staging env, ESLint/Prettier, Husky, Component Library base (Button, Input, Card, Container). |
| **1.5** | **Design System Base (Tokens & Primitivos)** | **Diseñador** | 1.1 | Figma: Color palette (Light/Dark), Tipografía (Escala), Espaciado, Border Radius, Sombras, **Componentes base** (Button states, Input states, Icon set). *Validar con Dev 1 naming conventions.* |
| **1.6** | **Wireframing Estructural (Low-Fi)** | **Diseñador** | 1.3 (Copy), 1.5 | Figma: Layouts Mobile/Desktop para todas las secciones. Focus en *Jerarquía* y *Flow*, no estética. Revisión rápida con Copywriter/Devs. |

> **🚀 Hito Viernes S1:** Copy "Freezed" (congelado), Design System listo para usar, Repo corriendo en Staging con `npm run dev`.

---

### FASE 2: DISEÑO ALTO NIVEL & DESARROLLO PARALELO (Semana 2 - Días 6-10)
*Objetivo: Diseñador pinta UI final; Devs codean componentes "estáticos" y estructura.*

| ID | Tarea | Responsable | Dependencias | Entregable / Criterio de Aceptación |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | **UI Design: Hero & Nav/Footer** | **Diseñador** | 1.5, 1.6 | Frames Mobile/Desktop finales. Estados: Hover, Focus, Loading (skeleton). Hand-off notes (assets exportados a `/public` o SVG components). |
| **2.2** | **Dev: Implement Hero + Nav + Footer** | **Dev 1, Dev 2** | 1.4, 2.1 (Parcial) | Componentes responsive, accesibles (ARIA), SEO meta tags dinámicos. Deploy Staging Día 7. |
| **2.3** | **UI Design: Features & Benefits (Grid/Cards)** | **Diseñador** | 1.3, 1.5 | Sistema de Iconos/Ilustraciones definido. Estados empty/loading si aplica. |
| **2.4** | **Dev: Component Library & Features Section** | **Dev 1, Dev 2** | 1.4, 2.3 (Parcial) | `<FeatureCard />`, `<IconWrapper />`, Grid responsive. **Storybook/Chromatic** opcional pero recomendado. |
| **2.5** | **UI Design: Social Proof, Pricing, FAQ, CTA Final** | **Diseñador** | 1.3, 1.5 | Tablas de pricing complejas (toggle Monthly/Annual), Acordeón FAQ, Logos partners. |
| **2.6** | **Dev: Pricing Table, FAQ Accordion, Forms** | **Dev 1, Dev 2** | 1.4, 2.5 (Parcial) | `<PricingTable />` con toggle, `<Accordion />` headless (Radix/Headless UI), `<Form />` con validación (Zod/React Hook Form). |
| **2.7** | **Copy Review & Microcopy en UI** | **Copywriter** | 2.1, 2.3, 2.5 | Revisión en Figma/Staging: Tooltips, Error states, Empty states, Button labels, Legal links. |

> **🚀 Hito Viernes S2:** Landing **completa visualmente en Staging** (puede faltar lógica backend real de formularios). Diseñador libera assets finales.

---

### FASE 3: INTEGRACIONES, LOGICA & HARDENING (Semana 3 - Días 11-15)
*Objetivo: Conectar la "cáscara" con la realidad (CRM, Analytics, Email, Pagos/Waitlist).*

| ID | Tarea | Responsable | Dependencias | Entregable / Criterio de Aceptación |
| :--- | :--- | :--- | :--- | :--- |
| **3.1** | **Integración Formularios -> CRM/Email (HubSpot/Salesforce/ConvertKit)** | **Dev 1** | 2.6 | Server Actions / API Routes. Manejo errores de red, *honeypot* / Turnstile (anti-bot), Double Opt-in si newsletter. Test end-to-end. |
| **3.2** | **Analytics & Tracking Setup (GA4, Mixpanel/Posthog, Pixel Ads)** | **Dev 2** | 1.4, 2.2 | `data-layer` events: `view_hero`, `click_cta_hero`, `start_checkout`, `submit_form_success`, `faq_open`. Consent Mode v2 (Cookie Banner). |
| **3.3** | **SEO Técnico & Performance** | **Dev 1, Dev 2** | 1.2, 2.2 | `sitemap.xml`, `robots.txt`, Open Graph / Twitter Cards dinámicos, JSON-LD (SoftwareApplication + FAQPage), **Lighthouse > 90** (Perf, A11y, SEO, Best Practices). Optimización Imágenes (next/image / Astro assets). |
| **3.4** | **A/B Testing Setup (Optional pero recomendado)** | **Dev 1 / PM** | 3.2 | Configurar flags (LaunchDarkly/ConfigCat/Edge Middleware) para testear Headline Hero o CTA Principal día 1. |
| **3.5** | **Cross-browser & Device QA (BrowserStack/Real devices)** | **Diseñador + Devs** | 2.6, 3.1 | Checklist: iOS Safari, Android Chrome, Firefox, Edge, Desktop 1440px/1920px. Fix visual regressions. |
| **3.6** | **Content Migration & Legal Pages (Privacy, Terms, Cookies)** | **Copywriter + Dev 2** | 1.3 | Páginas legales creadas (MDX/Static) y linkeadas en Footer/Cookie Banner. Revisión legal si aplica. |

> **🚀 Hito Viernes S3:** **Feature Complete en Staging.** Todo funciona. Solo queda pulir y aprobar.

---

### FASE 4: LANZAMIENTO Y ESTABILIZACIÓN (Semana 4 - Días 16-20)
*Objetivo: Cero sorpresas en producción.*

| ID | Tarea | Responsable | Dependencias | Entregable / Criterio de Aceptación |
| :--- | :--- | :--- | :--- | :--- |
| **4.1** | **Pre-Launch Checklist & Sign-off** | **Todos (Lead: PM)** | 3.5 | Checklist firmado: DNS, SSL, Env Vars Prod, Analytics ID Prod, CRM Prod Keys, Error Tracking (Sentry), Uptime Monitor. |
| **4.2** | **Deploy a Producción (Soft Launch)** | **Dev 1** | 4.1 | **Martes AM:** Deploy a `main` -> Prod. Verificación humo (Smoke test) en vivo: Formulario, Tracking, Velocidad. |
| **4.3** | **Monitoring Activo & Hotfixes** | **Dev 1, Dev 2** | 4.2 | Martes-Miércoles: Alertas Sentry/LogRocket. Fix críticos < 2h. |
| **4.4** | **DNS Switch / Go Live Oficial (Marketing Push)** | **PM / Marketing** | 4.3 | **Miércoles/Jueves:** Anuncio Social, Email, Product Hunt, Newsletter. |
| **4.5** | **Post-Launch Retro & Docs Handoff** | **Todos** | 4.4 | Viernes: Retro 30 min. Doc: "Cómo editar copy", "Cómo añadir FAQ", "Cómo ver métricas", Runbook incidencias. |

> **🎉 Hito Final: LIVE & ESTABLE.**

---

## 🔗 MATRIZ DE DEPENDENCIAS CRÍTICAS (Cuello de Botella)

| Bloqueador | Quien lo genera | Quien lo sufre | Mitigación |
| :--- | :--- | :--- | :--- |
| **Copy Final (1.3)** | Copywriter | Diseñador (2.1, 2.3, 2.5), Devs (SEO, JSON-LD) | **Entrega escalonada:** Hero/Nav Día 2 -> Features Día 3 -> Pricing/FAQ Día 4. No esperar "todo". |
| **Design System (1.5)** | Diseñador | Dev 1, Dev 2 (Setup componentes) | **Pair Design-Dev Día 1-2:** Definir naming tokens (`color-primary-500` vs `brand-blue`) y estructura carpetas Figma/Code *juntos*. |
| **Assets/Imágenes (2.1, 2.3, 2.5)** | Diseñador | Devs (Performance, LCP) | Diseñador exporta **WebP/AVIF** optimizados + SVGs como componentes React. Usar `@svgr` o similar. |
| **API Keys Prod (CRM, Analytics)** | PM/Marketing | Dev 1 (3.1, 3.2) | **Pedir accesos Semana 1.** Usar `.env.example` y secretos en Vercel/Cloudflare desde Staging. |
| **Revisión Legal (3.6)** | Legal Externo | Copywriter, Dev 2 (Deploy Legal) | Enviar borrador **Semana 2**. Si no hay legal interno, usar plantillas estándar (Termly/Iubenda) y marcar como "Pendiente revisión". |

---

## 👥 ASIGNACIÓN DE CARGA (Workload Balance)

| Rol | Semana 1 | Semana 2 | Semana 3 | Semana 4 | Notas de Capacidad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Diseñador** | **ALTA** (System + Wireframes + Inicio UI) | **MUY ALTA** (UI Completa 5-6 secciones Mobile/Desktop) | **BAJA** (QA Visual, Assets, Micro-interacciones) | **BAJA** (Validación Prod, Retro) | *Riesgo: Cuello de botella S2. Solución: Priorizar secciones "Above the fold" primero.* |
| **Copywriter** | **ALTA** (Research + Todo el Copy) | **MEDIA** (Microcopy en Figma/Staging, Legal) | **BAJA** (Revisión FAQ/Error states) | **BAJA** | *Entregar por secciones, no todo al final.* |
| **Dev 1 (Lead/Backend)** | **ALTA** (Arch, Repo, CI/CD, Design System Code) | **ALTA** (Hero, Nav, Forms, API Routes, CRM) | **ALTA** (Integraciones, SEO Tech, Performance, A/B) | **ALTA** (Deploy, Monitoring, Hotfixes) | *Es el bus factor. Proteger de reuniones innecesarias.* |
| **Dev 2 (Frontend/UI)** | **MEDIA** (Setup, Componentes Base, Storybook) | **ALTA** (Features Grid, Pricing, FAQ, Animaciones) | **ALTA** (Analytics, Cookie Banner, Cross-browser, Legal Pages) | **MEDIA** (QA, Hotfixes, Docs) | *Debe poder codear UI sin esperar diseño pixel-perfect (usar Design System).* |

---

## 🛠 STACK TECNOLÓGICO RECOMENDADO (Para velocidad)
*   **Framework:** **Astro** (Mejor rendimiento SEO/Performance out-of-the-box, islas de interactividad) **o Next.js 14+ (App Router)** si necesitan SSR/Auth complejo luego.
*   **Styling:** **Tailwind CSS** + **Shadcn/UI** (Componentes accesibles copiables, cero dependencias UI pesadas).
*   **Forms/Val:** **React Hook Form + Zod**.
*   **Analytics:** **PostHog** (Open source, session replay, feature flags, analytics todo en uno) + GA4.
*   **Deploy:** **Vercel** / **Cloudflare Pages** (Edge, gratis, preview deployments automáticos).
*   **Gestión:** **Linear** / **GitHub Projects** (Issues vinculadas a PRs).

---

## ⚠️ RIESGOS Y PLANES DE CONTINGENCIA

| Riesgo | Probabilidad | Impacto | Plan B |
| :--- | :--- | :--- | :--- |
| **Diseñador no termina UI Semana 2** | Media | Crítico | **Recortar scope:** Lanzar "Single Page" solo con Hero, Features, 1 CTA, Footer. Pricing/FAQ a Fase 2 (Post-launch). |
| **Integración CRM falla / API keys tardan** | Media | Alto | **Mock API / Serverless Function temporal:** Guardar leads en DB (Vercel KV / Supabase / Airtable) y sincronizar manualmente/zapier primera semana. |
| **Performance Lighthouse < 90 (LCP/CLS)** | Media | Medio | **Budget estricto:** Hero image < 50kb (AVIF), `priority` load, `font-display: swap`, evitar JS pesado en Hero. |
| **Cambios de copy de última hora (Stakeholders)** | Alta | Medio | **Congelar Copy Viernes S1.** Cambios posteriores solo via PR en código (Markdown/Contentlayer) o CMS (Sanity/Contentful) si ya está integrado. |
| **Enfermedad Dev 1 (Bus Factor)** | Baja | Crítico | **Documentación técnica viva (README/ADR).** Dev 2 sabe levantar repo y deploy. Pair programming obligatorio Semana 1. |

---

## ✅ CHECKLIST DE "DEFINITION OF READY" PARA EMPEZAR (Día 0)
Antes de dar el pistoletazo de salida el **Lunes Semana 1**, confirma:
- [ ] **Accesos:** Figma (Edit), GitHub (Admin), Vercel/Cloudflare, CRM (Admin), Analytics (Edit), Domain/DNS (Access).
- [ ] **Brand Assets:** Logo (SVG), Paleta colores (Hex), Fuentes (Archivos .woff2 o link Google Fonts/Adobe).
- [ ] **Product Clarity:** Demo video/gifs del producto para sección "Features" (si no hay, usar placeholders y definir quién graba).
- [ ] **Testimonios/Logos:** ¿Tenemos 3 logos clientes / 2 testimonios reales? Si no, diseñar estado "Próximamente" o placeholders genéricos.
- [ ] **Legal:** ¿Quién aprueba Privacy/Terms? ¿Plantilla lista?

---

### 💡 Consejo de Oro para el PM/Lead
**Haz un "Standup Async" diario (Slack/Linear) + 1 Sync semanal (30 min Lunes).**
*   **Lunes:** Planificación semana (Sprint Goal).
*   **Martes-Jueves:** Async updates (Bloqueadores, PRs abiertos).
*   **Viernes:** Demo en Staging + Retro rápida (Start/Stop/Continue).

**¡Éxito con el lanzamiento!** Si necesitas plantillas de issues para Linear/GitHub o el checklist de QA detallado, avísame.