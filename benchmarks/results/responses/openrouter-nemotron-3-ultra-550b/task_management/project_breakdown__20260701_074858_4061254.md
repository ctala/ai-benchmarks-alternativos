# Nemotron 3 Ultra 550B — task_management/project_breakdown

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 38.43s | tokens_per_second: 126.5
- input_tokens: 83 | output_tokens: 4862

## Respuesta completa

Este es un plan de ejecución **realista y agresivo** para 4 semanas (20 días laborables). La clave para cumplir el plazo es **paralelizar al máximo** (diseño y copy simultáneos) y **evitar el "waterfall" estricto** (esperar a que todo el diseño termine para empezar a codear).

---

### 🎯 Principios Clave para 4 Semanas
1.  **Mobile-First & Componentes:** Diseñar sistema de componentes, no páginas enteras pixel-perfect.
2.  **Copy First (Wireframe Copy):** El copywriter define estructura y mensajes *antes* de que el diseñador pinte UI final.
3.  **Dev Handoff Temprano:** Developers maquetan estructura/HTML semántico con *placeholder content* mientras se pulen textos e imágenes finales.
4.  **Scope Freeze Día 10:** Nada de features nuevas después de la Semana 2. Solo bugs y pulido.

---

### 📅 TIMELINE RESUMIDO (4 Semanas / 20 Días)

| Semana | Foco Principal | Hito Clave (Milestone) |
| :--- | :--- | :--- |
| **Sem 1 (D1-D5)** | **Estrategia, Copy & Arquitectura** | **M1: Wireframes + Copy Final Aprobado + Setup Repo/Design System** |
| **Sem 2 (D6-D10)** | **UI Design & Frontend Core** | **M2: Diseño Sistema Completo + Homepage Maquetada (Responsive) + CMS/Forms Conectados** |
| **Sem 3 (D11-D15)** | **Secciones Internas, Integraciones & QA** | **M3: Landing Completa Funcional (Staging) + Tracking/Analytics OK** |
| **Sem 4 (D16-D20)** | **Hardening, Performance, Launch** | **M4: Go-Live Producción + Monitorización 48h** |

---

### 📋 DESGLOSE DETALLADO POR FASES

#### FASE 1: FUNDACIÓN & CONTENIDO (Semana 1 - Días 1-5)
*Objetivo: Saber QUÉ decimos y CÓMO se estructura antes de pintar píxeles.*

| ID | Tarea | Descripción / Entregable | Dependencias | Responsable | Día Objetivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Kickoff & Definición de Valor** | Definir: ICP, 3 Key Benefits, Diferenciador vs Competencia, Objetivo primario (Demo? Trial? Waitlist?), Métrica de éxito. | - | **Todos (Lead: PM/Founder)** | D1 (AM) |
| **1.2** | **Arquitectura de Información & Sitemap** | Definir secciones: Hero, Problem/Solution, Features (3-5), Social Proof, Pricing/CTA, Footer, Legal. | 1.1 | **Copywriter + Designer** | D1 (PM) |
| **1.3** | **Copywriting: Wireframe Copy (Prioridad ALTA)** | Entregar: Headlines, Subheads, Bullets de features, Testimonios (placeholders reales), FAQ, Microcopy (botones, forms, errores). *Texto plano en Figma/Notion, sin diseño visual.* | 1.2 | **Copywriter** | **D2 EOD** |
| **1.4** | **Wireframing UX (Low-Fi)** | Estructura de secciones en Figma (Auto-layout), jerarquía visual, estados vacíos/error, responsive breakpoints (Mobile/Tablet/Desktop). Usar copy real del 1.3. | 1.2, 1.3 | **Designer** | **D3 EOD** |
| **1.5** | **Revisión y Aprobación Wireframes + Copy** | Revisión stakeholder. **FREEZE COPY ESTRUCTURAL** (cambios menores de wording permitidos luego, cambios de estructura NO). | 1.3, 1.4 | **PM + Stakeholders** | D4 (AM) |
| **1.6** | **Setup Técnico & Design System Base** | Repo (Next.js/Astro/Remix + Tailwind/Shadcn), CI/CD (Vercel/Netlify), Storybook (opcional), Tokens (Colores, Tipografía, Espaciado, Border Radius), Componentes base (Button, Input, Card, Container, Grid). | 1.1 | **Dev 1 (Lead) + Dev 2** | **D5 EOD** |
| **1.7** | **Setup Analytics & Tracking Plan** | Definir eventos: `view_hero`, `click_cta_hero`, `scroll_features`, `submit_form_demo`, `click_pricing`. Configurar GA4/Posthog/Mixpanel + GTM en repo. | 1.6 | **Dev 1** | D5 EOD |

> **🚨 HITO M1 (Fin Día 5): Wireframes Aprobados + Copy Estructural Congelado + Repo Base + Design System Tokens/Componentes Base Listos.**

---

#### FASE 2: UI DESIGN & FRONTEND CORE (Semana 2 - Días 6-10)
*Objetivo: Diseño visual final del sistema + Maquetación de la página principal (Above the fold + Features).*

| ID | Tarea | Descripción / Entregable | Dependencias | Responsable | Día Objetivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2.1** | **UI Design: High-Fi Design System** | Estilos finales: Botones (estados hover/active/disabled/loading), Inputs (estados error/success), Cards, Badges, Tooltips, Modals, Tablas (si hay pricing complejo). Documentado en Figma (Variants/Properties). | 1.5, 1.6 | **Designer** | **D8 EOD** |
| **2.2** | **UI Design: Homepage Completa (Desktop + Mobile)** | Aplicar Design System a wireframes. Hero, Features, Social Proof, Pricing, Footer. **Entregar assets optimizados (SVG/WebP) en carpeta compartida/Figma Dev Mode.** | 1.5, 2.1 (paralelo) | **Designer** | **D9 EOD** |
| **2.3** | **Dev: Maquetación Componente a Componente (Atomic Design)** | Construir átomos/moléculas en código real (Button, Input, Card, Section, Grid) usando tokens del 1.6. **No maquetar página completa aún, solo componentes aislados en Storybook/página de test.** | 1.6, 2.1 (tokens) | **Dev 1 + Dev 2** | **D8 EOD** |
| **2.4** | **Dev: Ensamblaje Homepage (Above Fold + Features)** | Montar Hero + Sección Features en `page.tsx`. Responsive estricto (Mobile First). Accesibilidad (ARIA, semántica, focus visible). **Usar copy final del 1.3.** | 2.3, 1.3 | **Dev 1 (Hero) + Dev 2 (Features)** | **D9 EOD** |
| **2.5** | **Dev: Formularios & Backend Integration** | Formulario Demo/Contacto/Trial: Validación cliente (Zod/Yup) + Servidor (Server Actions/API Route) + Integración CRM (HubSpot/Salesforce/Pipedrive) / Email (Resend/SendGrid) + Honeypot/Recaptcha. Toast notifications. | 1.6, 1.7 | **Dev 1** | **D10 EOD** |
| **2.6** | **Copywriter: Microcopy Final & SEO** | Meta titles/descriptions, Open Graph tags, JSON-LD Schema (SoftwareApplication), Alt texts para imágenes, Textos legales (Privacy/Terms links). | 1.3 | **Copywriter** | D9 EOD |
| **2.7** | **Designer: Asset Export & QA Visual Pares** | Exportar assets finales (WebP/AVIF), revisar implementación Dev vs Figma (Figma Dev Mode), reportar discrepancias visuales (spacing, fonts, shadows). | 2.2, 2.4 | **Designer** | **D10 EOD** |

> **🚨 HITO M2 (Fin Día 10): Design System Codeado + Homepage Core Responsive + Formularios Conectados a CRM/Email + SEO On-page Listo. SCOPE FREEZE TOTAL.**

---

#### FASE 3: SECCIONES RESTANTES, INTEGRACIONES & QA (Semana 3 - Días 11-15)
*Objetivo: Completar página, conectar todo, testear duro.*

| ID | Tarea | Descripción / Entregable | Dependencias | Responsable | Día Objetivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3.1** | **Dev: Maquetación Secciones Restantes** | Social Proof (Carousel/Grid), Pricing Table (Toggle Monthly/Anual), FAQ (Accordion), Footer, Páginas Legales (/privacy, /terms). | 2.3, 2.2 | **Dev 1 + Dev 2** | **D12 EOD** |
| **3.2** | **Dev: Tracking & Analytics Implementation** | Implementar `data-layer` events definidos en 1.7. Testear en GTM Preview / Posthog Live View. Verificar `purchase`/`sign_up` events si hay checkout embebido. | 1.7, 2.5 | **Dev 1** | D12 EOD |
| **3.3** | **Dev: Performance & Core Web Vitals** | Optimizar imágenes (`next/image`), Fonts (`next/font` / preload), Code Splitting, Eliminar JS innecesario, Prefetch links críticos. Target: LCP < 2.5s, CLS < 0.1, INP < 200ms (Mobile 4G throttling). | 3.1 | **Dev 2 (Lead Perf)** | **D13 EOD** |
| **3.4** | **Dev: Accesibilidad (a11y) Audit** | Audit axe-core / Lighthouse: Contraste, Navegación teclado, Labels ARIA, Skip links, Focus management en modales. | 3.1 | **Dev 2** | D13 EOD |
| **3.5** | **Designer: QA Visual Cross-Browser/Device** | Test: Chrome, Firefox, Safari, Edge. iOS Safari (real device), Android Chrome. iPad/Tablet. Check: Font rendering, Scroll behavior, Form inputs zoom (16px min), Safe areas (notch/Dynamic Island). | 3.1 | **Designer** | **D14 EOD** |
| **3.6** | **Copywriter: QA Contenido & Links** | Revisar ortografía/gramática en staging. Verificar **TODOS** los links (anchor, externos, CTA, footer, legal). Verificar emails de confirmación (copy, formato, deliverability test). | 3.1 | **Copywriter** | D14 EOD |
| **3.7** | **Bug Bash & Triage (Equipo Completo)** | Sesión 1h: Romper la web. Lista priorizada: P0 (Bloqueador Launch), P1 (Visual/Funcional grave), P2 (Nice to fix). Fix P0/P1 inmediatos. | 3.3, 3.4, 3.5, 3.6 | **Todos** | **D15 EOD** |

> **🚨 HITO M3 (Fin Día 15): Staging URL Estable. Zero P0 Bugs. Performance Verde. Tracking Verificado. Contenido Aprobado.**

---

#### FASE 4: HARDENING & LAUNCH (Semana 4 - Días 16-20)
*Objetivo: Cero sorpresas en producción.*

| ID | Tarea | Descripción / Entregable | Dependencias | Responsable | Día Objetivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4.1** | **Fix P1 Bugs & Polish** | Resolver bugs P1 restantes. Pulidos visuales finales (micro-interacciones, loading states). | 3.7 | **Devs + Designer** | **D17 EOD** |
| **4.2** | **Configuración Producción & DNS** | Configurar Dominio custom (Apex + www), SSL, Headers Seguridad (CSP, HSTS, X-Frame-Options), Redirects (www -> non-www o viceversa), Edge Middleware (Geo/IP block si aplica). | 1.6 | **Dev 1 (Lead)** | **D17 EOD** |
| **4.3** | **Smoke Test Pre-Launch (Checklist)** | Checklist: Formularios envían a CRM PROD, Emails llegan a Inbox (no Spam), Tracking dispara en Prod, Sitemap.xml / Robots.txt ok, 404 page bonita, Favicons/App icons todos los tamaños. | 4.2 | **Dev 1 + Copywriter** | **D18 (AM)** |
| **4.4** | **🚀 DEPLOY PRODUCCIÓN** | Merge `main` -> `production` / Promote en Vercel/Netlify. Verificar DNS propagado. | 4.3 | **Dev 1** | **D18 (PM) - DÍA L** |
| **4.5** | **Post-Launch Monitoring (48h)** | Monitor: Uptime (BetterUptime/Pingdom), Error Tracking (Sentry), Analytics Real-time, Form submissions CRM, Core Web Vitals (RUM). Rollback plan listo. | 4.4 | **Dev 1 (Lead) + PM** | **D19 - D20** |
| **4.6** | **Retrospectiva & Documentación** | Qué funcionó, qué no. Documentar arquitectura, credenciales (1Password/Vault), Runbooks (Cómo cambiar copy, cómo añadir feature). | 4.5 | **Todos** | D20 |

> **🏁 HITO M4 (Día 18): LIVE. Día 20: Proyecto Cerrado.**

---

### 🔗 MATRIZ DE DEPENDENCIAS CRÍTICAS (Cuello de Botella)

| Dependencia Crítica | Riesgo si falla | Mitigación |
| :--- | :--- | :--- |
| **Copywriter (1.3) -> Designer (1.4/2.2)** | Diseñador maquetando con "Lorem Ipsum" = Rehacer layout luego. | **Copywriter entrega D2 EOD innegociable.** Designer maquetando wireframes D3. |
| **Designer (2.1 Design System) -> Devs (2.3 Componentes)** | Devs codean componentes "ad-hoc" = Deuda técnica / Inconsistencias. | **Devs esperan tokens Figma (D8) para codear átomos.** Usan placeholders genéricos D6-D7. |
| **Dev 1 (2.5 Forms/Backend) -> Launch** | Formulario no envía a CRM = Leads perdidos Día 1. | **Dev 1 foco exclusivo Forms D6-D10.** Test real con cuenta CRM staging D9. |
| **Scope Freeze D10** | Stakeholders piden "pequeños cambios" Semana 3/4 = No se lanza. | **Contrato firme:** Cambios post-D10 = Post-Launch (Fase 5). Solo P0 bugs entran. |

---

### ⚙️ ASIGNACIÓN DE RECURSOS Y CARGA (Capacity Planning)

| Rol | Semana 1 | Semana 2 | Semana 3 | Semana 4 | Notas Clave |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Copywriter** | **ALTA** (Estructura, Wireframe Copy, SEO Plan) | **MEDIA** (Microcopy final, Alt text, Legal, OG tags) | **BAJA** (QA Contenido, Email testing) | **BAJA** (Smoke test post-launch) | **Crítico D1-D3.** Libre resto para apoyar QA. |
| **Designer** | **ALTA** (Wireframes, Design System Base) | **ALTA** (UI Final Homepage, Design System Completo, Assets) | **MEDIA** (QA Visual Cross-browser, Asset iteration) | **BAJA** (Polish final, Favicons) | **Bloquea a Devs si Design System tarde (D8).** |
| **Dev 1 (Lead/Backend)** | **ALTA** (Repo, CI/CD, Design System Code, Forms/Backend, Analytics) | **ALTA** (Hero/Features Assembly, Forms Integration, Prod Config) | **ALTA** (Performance, Tracking, Bug Fixing, Prod Deploy) | **ALTA** (Launch, Monitoring, Rollback) | **Single Point of Failure en Backend/Infra.** Proteger foco. |
| **Dev 2 (Frontend/UI)** | **MEDIA** (Ayuda Setup, Componentes Base) | **ALTA** (Component Library Code, Features Section, Pricing/FAQ/Footer) | **ALTA** (Performance, a11y, Secciones restantes, Bug Fixing) | **MEDIA** (Bug Fix P1, Smoke Test) | **Paralelizable con Dev 1 en componentes/secciones.** |

---

### 🛠 STACK TECNOLÓGICO RECOMENDADO (Para Velocidad)
*   **Framework:** **Next.js 14+ (App Router)** o **Astro** (Mejor performance out-of-the-box, menos JS).
*   **Styling:** **Tailwind CSS** + **Shadcn/UI** (Componentes accesibles copiables, no dependencia librería pesada).
*   **CMS/Content:** **Contentlayer** (MDX local) o **Sanity/Contentful** (Si marketing necesita editar sin deploy). *Para 4 semanas: Contentlayer/Archivos locales es más rápido.*
*   **Forms/Backend:** **Next.js Server Actions** + **Zod** + **Resend** (Email) + **HubSpot/Salesforce API** (CRM).
*   **Analytics:** **PostHog** (Open source, session replay, feature flags gratis) o **GA4 + GTM**.
*   **Deploy:** **Vercel** (Integración Next.js perfecta, Edge, Analytics, Speed Insights).
*   **Design:** **Figma** (Dev Mode obligatorio para Devs).

---

### ✅ CHECKLIST DE "DEFINITION OF DONE" PARA LAUNCH (Día 18)
1.  [ ] **Funcional:** Hero CTA -> Form -> CRM Lead creado -> Email Confirmación enviado -> Redirect Thank You.
2.  [ ] **Tracking:** `sign_up` event en PostHog/GA4 con `plan_type`, `source`.
3.  [ ] **Performance:** Lighthouse Mobile > 90 (Perf, Acc, Best Practices, SEO).
4.  [ ] **a11y:** axe-core 0 violations (WCAG 2.1 AA).
5.  [ ] **SEO:** Sitemap.xml, Robots.txt, Meta tags, JSON-LD, Canonicals, Hreflangs (si multi-idioma).
6.  [ ] **Seguridad:** CSP Header, HSTS, Rate limiting en Forms, Secrets en Env Vars (no en repo).
7.  [ ] **Legal:** Links Privacy/Terms/ Cookie Policy funcionando.
8.  [ ] **Rollback:** `git revert` probado / Vercel Instant Rollback verificado.

---

### 💡 CONSEJOS DE SUPERVIVENCIA PARA EL PM/LÍDER
1.  **Daily Standup 15min estrictos:** Bloqueadores > Qué hice ayer.
2.  **Slack Channel #launch-landing:** Solo alertas, deploys, blockers. Sin ruido.
3.  **Staging URL actualizada cada noche (Auto-deploy `main`):** Stakeholders revisan *ahí*, no en Figma.
4.  **Designer revisa en Figma Dev Mode, NO en Zeplin/Abstract.** Devs copian valores CSS directos.
5.  **Viernes Semana 2 (D10) = Code Freeze para features.** Solo `fix/` branches permitidos.
6.  **Celebra el Día 18 (Launch).** Día 20 Retro + Cerveca/Café.