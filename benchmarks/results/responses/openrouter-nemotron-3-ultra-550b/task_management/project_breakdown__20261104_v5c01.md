# Nemotron 3 Ultra 550B — task_management/project_breakdown

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.38 | quality: 10.0
- latency_total: 95.454s | tokens_per_second: 54.3
- input_tokens: 83 | output_tokens: 5185
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto con tareas, responsables y dependencias.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Este es un plan de ejecución **realista y agresivo** para 4 semanas (20 días laborables) con tu equipo. La clave para cumplir el plazo es **paralelizar al máximo** y **congelar el scope (alcance) al final de la Semana 1**.

---

### 🎯 PRINCIPIOS CLAVE PARA ÉXITO
1.  **Mobile-First & Performance:** El 60%+ del tráfico B2B SaaS inicial suele ser móvil/escritorio mixto; Core Web Vitals afectan SEO y Ads.
2.  **Copy-First Design:** El copywriter entrega *wireframes de contenido* (texto real, no "Lorem Ipsum") antes de que el diseñador abra Figma.
3.  **Component-Driven Dev:** Developers construyen una **Design System ligero** (Botones, Inputs, Cards, Grid) en Semana 1 para no reescribir CSS en Semana 3.
4.  **Un solo "Hero" CTA:** Una sola acción principal arriba (ej. "Iniciar prueba gratis 14 días") y una secundaria en footer.

---

### 📦 FASES Y TIMELINE (4 SEMANAS)

#### **SEMANA 1: FUNDACIÓN & ESTRATEGIA (Días 1-5) — *CRÍTICO: NO RETRASAR***
*Objetivo: Tener aprobado: Copy final, Sitemap, Wireframes Low-Fi, Stack técnico y Design System base.*

| Día | Tarea | Responsable | Dependencias | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| **Lunes (D1)** | **Kickoff & Definición de MVP Scope** (Qué entra/qué NO entra en v1) | **Todos (Lead: PM/Founder)** | - | Doc `Scope_v1.md` firmado |
| **Lunes (D1)** | Investigación: Competencia, Keywords SEO, Dolor del cliente (Jobs-to-be-done) | **Copywriter** | - | Doc `Research_Insights.md` |
| **Martes (D2)** | **Copywriting Estructural:** Headlines, Value Props, Estructura de secciones (Hero, Features, Social Proof, Pricing, FAQ, Footer), Microcopy (botones, errores, empty states) | **Copywriter** | Research | **`Wireframe_Content_v1.docx` (Texto real por sección)** |
| **Miércoles (D3)** | Revisión Copy + Ajustes + **Freeze Copy Estructural** | **Copywriter + PM** | Copy D2 | **`Copy_Approved_v1` (Bloqueado para cambios mayores)** |
| **Miércoles (D3)** | Setup Repo + CI/CD (Vercel/Netlify + GitHub Actions) + **Design System Base** (Tokens: colores, tipografía, spacing, breakpoints + Componentes: Button, Input, Card, Container, Grid) | **Dev 1 (Lead)** | Scope D1 | Repo funcionando + `Storybook` o carpeta `/components/ui` |
| **Jueves (D4)** | **Wireframes Low-Fi (Mobile/Desktop)** basados *exclusivamente* en `Copy_Approved_v1` | **Diseñador** | Copy Aprobado D3 | Figma `Wireframes_v1` |
| **Viernes (D5)** | Revisión Wireframes + **Aprobación Estructura/UX** | **Todos** | Wireframes D4 | **`Wireframes_Approved`** |
| **Viernes (D5)** | Definición de **Data Layer / Eventos Analytics** (GA4, Meta Pixel, Hotjar/Clarity): `view_item`, `begin_checkout`, `sign_up`, `demo_request` | **Dev 1 + Copywriter** | Scope D1 | Doc `Analytics_Plan.md` |

> ⚠️ **HITO VIERNES D5:** *Copy Estructural Aprobado + Wireframes Aprobados + Design System Base en Repo.* Si esto se mueve, la fecha de lanzamiento se mueve.

---

#### **SEMANA 2: DISEÑO VISUAL (HI-FI) & BACKEND/INTEGRACIONES (Días 6-10)**
*Objetivo: UI Kit completo en Figma + Páginas estáticas "Storybook" listas + Integraciones de formularios/email funcionando en staging.*

| Día | Tarea | Responsable | Dependencias | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| **Lunes (D6)** | **UI Design System (Hi-Fi):** Estilos finales (Botones estados, Inputs errores, Tablas, Tooltips, Iconografía, Ilustraciones/3D placeholders) | **Diseñador** | Wireframes Ap. | Figma `UI_Kit_v1` (Auto-layout listo para dev) |
| **Martes (D7)** | **Diseño Páginas Completas (Hi-Fi):** Home, Pricing, Features/Comparativa, About/Trust, Thank You Page, 404. *Mobile + Desktop.* | **Diseñador** | UI Kit D6 | Figma `Pages_HiFi_v1` |
| **Miércoles (D8)** | **Revisión Diseño + Aprobación Visual** (Check: Accesibilidad AA, Consistencia, Copy encaja) | **Todos** | Hi-Fi D7 | **`Design_Approved`** |
| **Jueves (D9)** | **Dev: Implementación Design System en Código** (Tokens CSS/TS, Componentes base accesibles, Responsive Grid) | **Dev 1 & Dev 2** | Design System Figma D6 + Repo D3 | Librería componentes `/ui` 100% testeada visualmente (Chromatic/Storybook) |
| **Viernes (D10)** | **Dev: Integraciones "Invisibles"** <br>• Formularios (React Hook Form + Zod) → API Route → **Email Provider (Resend/SendGrid) + CRM (HubSpot/Salesforce/Pipedrive)** <br>• Double Opt-in / Lead Magnet delivery <br>• **Analytics Events** (Data Layer push) | **Dev 1 (Lead API)** | Design System Code D9 | Endpoints `/api/lead`, `/api/demo` funcionales en Staging + Eventos en GA4 DebugView |

> 💡 **Paralelismo Crítico:** Mientras Diseñador hace Hi-Fi (D6-D8), **Devs NO esperan**. Empiezan D6/D7 con el Design System base (tokens, spacing, componentes genéricos) y la arquitectura de integraciones. Solo necesitan el Hi-Fi final para "maquetar páginas" en Semana 3.

---

#### **SEMANA 3: MAQUETADO AGRESIVO & QA INTERNO (Días 11-15)**
*Objetivo: Landing completa en Staging, pixel-perfect, responsive, accesible y trackeando.*

| Día | Tarea | Responsable | Dependencias | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| **Lunes (D11)** | **Dev: Maquetado Secciones Estáticas** (Hero, Features, Social Proof, Footer) usando componentes `/ui` | **Dev 1 & Dev 2** | Design Approved D8 + UI Code D9 | `/` (Home) funcional en Staging |
| **Martes (D12)** | **Dev: Maquetado Páginas Secundarias** (Pricing - *complejo*, Features Detail, About, Thank You, 404) | **Dev 1 & Dev 2** | Secciones D11 | Todas las rutas `/pricing`, `/features`... en Staging |
| **Miércoles (D13)** | **Copywriter: Microcopy Final & SEO On-Page** (Title tags, Meta descriptions, H1-H3, Alt text, Schema.org `Product`/`FAQPage`/`Breadcrumb`) | **Copywriter** | Design Approved D8 | Doc `SEO_Meta_Tags.csv` + Textos finales en Figma/Notion |
| **Jueves (D14)** | **Dev: Inyección Contenido Final + SEO Técnico** (Meta tags dinámicos, JSON-LD, Sitemap.xml, Robots.txt, Open Graph/Twitter Cards) | **Dev 1** | Copy SEO D13 + Páginas D12 | Staging con contenido real + SEO técnico completo |
| **Viernes (D15)** | **QA Interno Cruzado (Bug Bash)** <br>• Checklist: Responsive (320px, 768px, 1440px), Navegadores (Chrome, FF, Safari), Accesibilidad (Tab, Screen reader, Contraste), Formularios (Validación, Envío, Thank You, Emails), Analytics (Eventos disparan), Performance (Lighthouse > 90), Links rotos. | **Todos (Rotativo)** | Staging Completo D14 | **`Bug_Report_v1` en Linear/Jira/GitHub Issues** |

---

#### **SEMANA 4: PULIDO, HARDENING & LANZAMIENTO (Días 16-20)**
*Objetivo: Cero bugs críticos, Performance < 2.5s LCP, DNS/SSL listos, Rollback plan.*

| Día | Tarea | Responsable | Dependencias | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| **Lunes (D16)** | **Bug Fixing Sprint 1** (Críticos / Altos: Formularios rotos, Layout shift móvil, CLS, LCP > 2.5s, Errores JS) | **Dev 1 & Dev 2** | Bug Report D15 | Staging `Release_Candidate_1` |
| **Martes (D17)** | **QA Regresión + Validación Copy/Design Final** (Diseñador: Pixel perfect. Copy: Ortografía, tono, links legales. Dev: Console limpia, Network ok) | **Todos** | RC1 D16 | **`Sign-Off_Staging`** |
| **Miércoles (D18)** | **Pre-Prod / Freeze Código** <br>• Merge a `main`/`production` branch <br>• Deploy a **Producción Real** (Vercel/Netlify/Cloudflare Pages) *bajo subdominio `launch.tudominio.com` o `preview`* <br>• Configuración DNS final (A/AAAA/CNAME), SSL, Headers Seguridad (CSP, HSTS), Redirects (www -> non-www), 404 page. | **Dev 1 (Lead Ops)** | Sign-Off D17 | **URL Producción Funcional (Oculta/Preview)** |
| **Jueves (D19)** | **Smoke Test Producción Real** (Formularios reales -> CRM, Emails reales, Analytics Real, Velocidad Real, Pago/Stripe si aplica) + **Checklist Go/No-Go** | **Todos** | Prod Deploy D18 | **`GO / NO-GO` Decision** |
| **Viernes (D20)** | **🚀 LANZAMIENTO OFICIAL** (Switch DNS principal / Anuncio) <br>• Monitoreo intensivo (Sentry, GA4 Realtime, UptimeRobot, Server Logs) <br>• Comunicación interna/equipo soporte listo para leads | **Todos** | GO Decision D19 | **LIVE** |
| **Viernes (D20) PM** | **Post-Launch Retro (30 min)** + Documentar deuda técnica / Backlog v1.1 | **Todos** | Launch | `Retro_Notes.md` |

---

### 🔗 MATRIZ DE DEPENDENCIAS CRÍTICAS (Riesgo Alto)

| Dependencia | Si se retrasa... | Mitigación |
| :--- | :--- | :--- |
| **Copy Estructural (D2-D3) → Wireframes (D4)** | **Todo el proyecto se desplaza.** Diseñador y Devs bloqueados. | Copywriter trabaja **Solo Copy Estructural** Lunes/Martes. No escribe blog posts ni emails aún. |
| **Design System Figma (D6) → Dev UI Code (D9)** | Devs maquetan "a ciegas" o esperan. | Devs empiezan **D6** con tokens genéricos (Tailwind/Shadcn/Radix config) y refactorizan D9. |
| **Design Approved (D8) → Maquetado (D11)** | Semanas 3 y 4 se comprimen. | **Reunión 15 min Miércoles D8** para aprobar. Si hay dudas, CEO/PM decide *ya*. No iterar indefinidamente. |
| **Integraciones CRM/Email (D10) → QA Formularios (D15)** | No se puede probar el flujo completo "Lead -> CRM -> Email". | Dev 1 prioriza **API Routes + Webhooks + Secrets** en Semana 2. Mockear CRM en local si falta credenciales. |
| **DNS/SSL (D18)** | Lanzamiento imposible el Viernes. | **Configurar DNS (TTL bajo 300s) y Certificados el Lunes D16 como muy tarde.** Verificar propagación Miércoles. |

---

### 👥 RACI RESUMIDO POR ROL

| Actividad Clave | **Copywriter** | **Diseñador** | **Dev 1 (Lead/Fullstack)** | **Dev 2 (Frontend)** | **PM / Founder** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Scope & Strategy** | C | I | C | I | **R/A** |
| **Copy Estructural (Wireframe)** | **R/A** | C | I | I | C |
| **Wireframes UX** | C | **R/A** | C | I | C |
| **UI Design System (Figma)** | I | **R/A** | C | C | I |
| **Hi-Fi Pages** | C (Copy fit) | **R/A** | I | I | C |
| **Design System Code** | I | C | **R** | **R** | I |
| **API / Integraciones / SEO Tech** | C (Schema) | I | **R/A** | C | I |
| **Maquetado Páginas (Fe)** | I | C (Review) | **R** | **R** | I |
| **QA / Bug Bash** | **R** (Copy/Links) | **R** (Visual/UX) | **R** (Func/Perf) | **R** (Func/Perf) | A |
| **Deploy / DNS / Go-Live** | I | I | **R/A** | C | **A** |

*(R=Responsable, A=Aprobador, C=Consultado, I=Informado)*

---

### 🛠 STACK TECNOLÓGICO RECOMENDADO (Velocidad + Calidad)
*   **Framework:** **Next.js 14+ (App Router)** + TypeScript (Estándar SaaS, SEO nativo, ISR/SSG).
*   **Styling:** **Tailwind CSS** + **Shadcn/UI** (o Radix UI) -> *Componentes accesibles, copiables, 0 dependencias UI kit pesadas.*
*   **Forms:** **React Hook Form** + **Zod** (Validación compartida cliente/servidor).
*   **CMS/Contenido (Opcional pero recomendado):** **Sanity.io / Contentful / Prismic** *Solo para secciones que marketing tocará mucho (Blog, Changelog, Help Center).* **Para Landing v1: Hardcodeado en componentes / JSON local = Cero dependencia externa, deploy instantáneo.**
*   **Analytics:** **GA4 + Google Tag Manager (GTM)** -> *No hardcodear eventos en código, usar Data Layer + GTM.*
*   **Email/CRM:** **Resend (React Email)** + **HubSpot / Pipedrive / Attio** (API nativa).
*   **Hosting:** **Vercel** (Preview deployments automáticos en cada PR, Edge, Analytics, Speed Insights).
*   **Error Tracking:** **Sentry** (DSN en env vars desde Día 1).
*   **Design:** **Figma** (Dev Mode ON para handoff).

---

### ⚡ 5 TRUCOS PARA AHORRAR DÍAS (NO HACER EN V1)
1.  **NO Blog / CMS complejo.** Hardcodea el contenido. Añade CMS en v1.1.
2.  **NO Animaciones complejas (Framer Motion/GSAP) en toda la página.** Solo `fade-in` en scroll (Intersection Observer) en Hero y Cards. *Riesgo CLS/Performance alto.*
3.  **NO Pricing Table interactiva compleja (Toggle Mensual/Anual con animación).** Dos tablas estáticas + `display: none` controlado por estado simple. Accesible y rápido.
4.  **NO Ilustraciones custom por sección.** Usa una librería cohente (undraw, Figma Community, Blush) o patrones CSS/SVG simples. El diseñador pierde días ilustrando.
5.  **NO A/B Testing setup.** Lanza *una* versión ganadora basada en research. Testear con tráfico real post-lanzamiento.

---

### 📋 CHECKLIST "GO / NO-GO" (Jueves D19 - Mañana)
*Solo se lanza si TODO esto es ✅ VERDE*

| Categoría | Check |
| :--- | :--- |
| **Funcional** | Formulario Demo/Lead -> Llega a CRM + Email confirmación usuario + Email notificación Sales |
| **Funcional** | Botones CTA principales navegan correctamente (Scroll anchor / Nueva pestaña / Link externo) |
| **Contenido** | 0 Typos. Copy legal (Privacy, Terms, Cookies) en Footer links funcionando. |
| **Visual** | Pixel-perfect vs Figma (Mobile / Desktop). No overflow horizontal. Fuentes cargadas (FOUT/FOIT controlado). |
| **Performance** | Lighthouse Mobile **Performance > 90**, **LCP < 2.5s**, **CLS < 0.1**, **TB < 200ms**. Imágenes `next/image` (WebP/AVIF, sizes correctos). |
| **SEO Técnico** | `sitemap.xml` / `robots.txt` accesibles. Meta tags únicos por página. Schema.org válido (Rich Results Test). Canónicas correctas. |
| **Analytics** | `page_view`, `click_cta_hero`, `form_submit_success`, `form_submit_error` visibles en **GA4 DebugView / Realtime**. |
| **Seguridad/Infra** | HTTPS forzado. Headers `Content-Security-Policy` (report-only ok), `X-Frame-Options`, `Referrer-Policy`. DNS propagado. |
| **Errores** | **Sentry 0 errores** en flujo crítico (Home -> Form -> Thank You). Console limpia (0 warnings/errors). |
| **Rollback** | `git tag launch-v1.0.0` creado. Saber hacer `vercel rollback` o `git revert` en < 5 min. |

---

### 🗓 RESUMEN VISUAL TIMELINE

```text
SEMANA 1: FUNDACIÓN          SEMANA 2: DISEÑO + BACKEND       SEMANA 3: BUILD + QA           SEMANA 4: LAUNCH
┌─────────────────────────┐  ┌─────────────────────────┐      ┌─────────────────────────┐    ┌─────────────────────────┐
│ LUN: Kickoff + Scope    │  │ LUN: UI Kit Hi-Fi       │      │ LUN: Build Sections     │    │ LUN: Fix Bugs Críticos  │
│ MAR: Copy Estructural ✍️│  │ MAR: Hi-Fi Pages        │      │ MAR: Build Pages        │    │ MAR: QA Regresión + ✅  │
│ MIE: Copy FREEZE + Repo │  │ MIE: DESIGN APPROVAL 🛑 │      │ MIE: SEO + Content Inj. │    │ MIE: DEPLOY PROD (Hide) │
│ JUE: Design System Code │  │ JUE: Dev UI Code + API  │      │ JUE: QA Bug Bash 🐛     │    │ JUE: SMOKE TEST + GO/NO │
│ VIE: Wireframes + ✅    │  │ VIE: Integraciones OK   │      │ VIE: Bug Report         │    │ VIE: 🚀 LAUNCH + Monitor│
└─────────────────────────┘  └─────────────────────────┘      └─────────────────────────┘    └─────────────────────────┘
      🛑 HITO: Copy/UX Lock           🛑 HITO: Design Lock                 🛑 HITO: Staging Ready          🛑 HITO: GO/NO-GO
```

---

### 💬 CONSEJO FINAL PARA EL PM/FOUNDER
**Tu trabajo esta semana es QUITAR TRABAJO, no añadirlo.**
1.  **Di "NO" a cualquier feature request** que no esté en `Scope_v1.md` (ej. "Añadamos un chatbot", "Hagamos el pricing interactivo", "Quiero una animación de confeti").
2.  **Protege al Copywriter** el Lunes/Martes de la Semana 1. Sin copy aprobado, el diseñador diseña cajas vacías y los devs maquetan cajas vacías = **Rehacer el doble de trabajo**.
3.  **Reunión diaria de 15 min (Standup) obligatoria.** Bloqueadores se resuelven *ese día*.
4.  **Viernes D5 y Miércoles D8 son "Puertas de Calidad".** Si no se aprueba, no se avanza. Es mejor lanzar una semana tarde con una página que convierte, que a tiempo con una página rota/confusa.

¡Mucha suerte con el lanzamiento! 🚀 Si necesitas plantillas para el `Scope_v1.md`, `Analytics_Plan.md` o el `Bug_Report`, avísame.