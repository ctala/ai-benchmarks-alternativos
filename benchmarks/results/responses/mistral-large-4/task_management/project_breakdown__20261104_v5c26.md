# Mistral Large 4.0 — task_management/project_breakdown

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 48.541s | tokens_per_second: 112.7
- input_tokens: 77 | output_tokens: 5470
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto con tareas, responsables y un cronograma realista.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Aquí tienes un plan de proyecto **MVP (one-page focused)** realista para 4 semanas. Asumo que la landing es una **single-page** con secciones ancladas (Hero → Features → Social Proof → Pricing → FAQ → CTA Final), ya que con 4 personas y 4 semanas no da para un sitio multi-página complejo.

**Stack recomendado para velocidad:** Next.js + Tailwind CSS (o Webflow si prefieren no-code) desplegado en Vercel. Esto permite iterar rápido y tener SEO técnico sólido desde el día 1.

---

### Pre-requisitos (antes de la Semana 1)
- Dominio comprado y acceso a DNS
- Cuentas creadas: Google Analytics 4, Search Console, Hotjar (o similar), herramienta de email (Mailchimp/ConvertKit/HubSpot)
- Brand básico definido (logo, paleta de colores, tipografía)
- Acceso a screenshots reales del producto o decisión de usar mockups

---

## Fase 1: Estrategia, Arquitectura y Copy (Semana 1)
**Objetivo:** Tener el mensaje claro y la estructura aprobada para que diseño no se bloquee.

| Tarea | Responsable | Dependencias | Entregable | Duración |
|-------|-------------|--------------|------------|----------|
| Kickoff: definir KPI principal (ej: 5% conversión a waitlist) y ICP (ej: pymes de retail con 1-3 almacenes) | Todo el equipo | - | Documento de objetivos | Día 1 |
| Análisis competitivo (3-5 SaaS competidores: ej. Zoho Inventory, Cin7, TradeGecko) | Copywriter + Diseñador | Kickoff | Matriz de features y mensajes diferenciadores | Día 1-2 |
| Keyword research (SEO) para "gestión de inventario", "control de stock", etc. | Copywriter | - | Lista de keywords primarias/secundarias | Día 2 |
| Arquitectura de información (sitemap de secciones y jerarquía H1-H3) | Copywriter + Diseñador | Análisis competitivo | Wireframe de estructura (bajo nivel) | Día 2-3 |
| **Copywriting completo**: Headline principal (H1), value prop, 3-4 features con beneficios, testimonios (si hay clientes beta; si no, placeholders), pricing (3 tiers), FAQ (5-6 preguntas), CTAs | Copywriter | Arquitectura aprobada | Documento de copy final (Google Doc) | Día 3-5 |
| Meta titles, meta descriptions, textos de Open Graph | Copywriter | Copy final | Hoja SEO | Día 5 |
| **Brief de diseño** al Diseñador (moodboard, referencias visuales, tono) | Copywriter | Copy final | Brief en Figma/Notion | Día 5 |

**Checkpoint Semana 1:** Copy aprobado y congelado (freeze). Cualquier cambio después impacta diseño.

---

## Fase 2: Diseño UX/UI (Semana 2)
**Objetivo:** Tener diseño pixel-perfect aprobado para desarrollo. El copywriter puede apoyar en micro-copy de UI (botones, errores de formulario) esta semana.

| Tarea | Responsable | Dependencias | Entregable | Duración |
|-------|-------------|--------------|------------|----------|
| Wireframes low-fi (desktop + mobile) de todas las secciones | Diseñador | Brief + Copy estructura | Wireframes en Figma | Día 1-2 |
| Aprobación interna de wireframes (con devs para validar viabilidad técnica) | Todo el equipo | Wireframes | Aprobación documentada | Día 2 |
| Diseño hi-fi desktop (todas las secciones) | Diseñador | Wireframes aprobados + Copy final | Pantallas Figma desktop | Día 3-4 |
| Diseño responsive mobile (breakpoints: 375px, 768px) | Diseñador | Hi-fi desktop | Pantallas Figma mobile | Día 4 |
| Creación de mockups del producto (si no hay screenshots reales: dashboard de inventario, tabla de stock, alertas) | Diseñador | - | Assets de UI mockup | Día 3-4 (paralelo) |
| Design System básico: componentes (botones, inputs, cards), variables de color/tipografía, espaciado | Diseñador | Hi-fi | Librería de componentes Figma + tokens CSS | Día 5 |
| Exportación y optimización de assets (SVG para iconos, WebP para imágenes, compresión) | Diseñador | Diseño final | Carpeta de assets optimizados | Día 5 |
| **Handoff a desarrollo**: reunión de entrega, documentación de estados (hover, active, error), especificaciones de animaciones | Diseñador + Devs | Todo lo anterior | Proyecto Figma listo + reunión grabada | Día 5 |

**Nota:** Mientras el diseñador trabaja, **Dev 1** puede preparar el repositorio, configurar CI/CD y crear la estructura base del proyecto (semana 2, paralelo).

---

## Fase 3: Desarrollo (Semana 3)
**Objetivo:** Landing funcional en staging, responsive y con integraciones básicas.

| Tarea | Responsable | Dependencias | Entregable | Duración |
|-------|-------------|--------------|------------|----------|
| Setup proyecto (Next.js + Tailwind), configuración de Vercel staging, variables de entorno | Dev 1 | - | Repo listo, deploy automático en push | Día 1 |
| Maquetación semántica HTML (estructura de secciones según arquitectura) | Dev 1 | Diseño aprobado | Estructura base | Día 1-2 |
| Implementación visual desktop (pixel-perfect según Figma) | Dev 1 | Assets + estructura | Vista desktop completa | Día 2-3 |
| Implementación responsive mobile + tablet | Dev 2 | Vista desktop | Responsive completo | Día 3 |
| Funcionalidades interactivas: smooth scroll, menú móvil, animaciones on-scroll (Framer Motion o CSS), hover states | Dev 2 | Diseño implementado | Interacciones funcionando | Día 3-4 |
| Formulario de waitlist/contacto → integración API (Mailchimp/ConvertKit/HubSpot) + validación + mensaje de éxito/error | Dev 2 | Cuenta de email lista | Formulario enviando datos reales | Día 4 |
| Implementación de Analytics (GA4), Pixel de Meta/LinkedIn (si aplica), Hotjar | Dev 2 | Cuentas creadas | Tracking funcionando en staging | Día 4 |
| SEO técnico: schema.org (SoftwareApplication), Open Graph tags, sitemap.xml, robots.txt, canonical tags | Dev 1 | Copy SEO de semana 1 | SEO on-page completo | Día 5 |
| Optimización de performance: imágenes lazy loading, font-display swap, minificación, Lighthouse > 90 | Dev 1 + Dev 2 | Todo implementado | Score de velocidad alto | Día 5 |
| Cross-browser testing (Chrome, Safari, Firefox, Edge) y testing en dispositivos reales | Dev 2 | Funcionalidades listas | Reporte de bugs | Día 5 |

**Checkpoint Semana 3:** "Feature complete" en staging. URL de prueba compartida.

---

## Fase 4: QA, Legal y Lanzamiento (Semana 4)
**Objetivo:** Landing en producción, sin errores críticos, lista para recibir tráfico.

| Tarea | Responsable | Dependencias | Entregable | Duración |
|-------|-------------|--------------|------------|----------|
| QA funcional exhaustivo: todos los links, formularios (envío real de test), botones, CTAs en móvil y desktop | Todo el equipo (cada uno prueba parte) | Staging estable | Lista de bugs en Notion/Jira | Día 1 |
| Corrección de bugs críticos y medios | Dev 1 + Dev 2 | Lista de bugs | Staging sin bugs críticos | Día 1-2 |
| Revisión de copy final (typos, ortografía, consistencia de tono) | Copywriter | - | Copy validado | Día 2 |
| Páginas legales mínimas: Privacy Policy y Terms of Service (usar templates de SaaS adaptados, revisar con legal si es posible) | Copywriter + Dev 2 | - | Páginas legales publicadas (pueden ser /privacy y /terms) | Día 2-3 |
| Configuración de dominio en producción (DNS apuntando a Vercel), SSL automático, redirects www → non-www (o viceversa) | Dev 1 | Dominio listo | Dominio accesible | Día 3 |
| Smoke test en producción: formulario, velocidad real, analytics recibiendo datos | Dev 2 | Deploy producción | Confirmación de funcionamiento | Día 3 |
| Preparación de plan de lanzamiento: lista de emails para anunciar, post en redes sociales, coordinación con equipo de ventas | Copywriter | - | Kit de lanzamiento | Día 4 |
| **Deploy a producción final** (con todas las correcciones) | Dev 1 | Todo aprobado | Landing live en dominio final | Día 4 |
| Monitoreo intensivo primeras 24h: errores en consola, tasa de conversión, velocidad real (Core Web Vitals) | Dev 2 | Landing live | Dashboard de monitoreo | Día 4-5 |
| Hotfixes si es necesario | Dev 1 + Dev 2 | Errores detectados | Versión estable | Día 5 |
| **Lanzamiento oficial** (anuncio en redes, email a lista, etc.) | Todo el equipo | Landing estable | Anuncio público | Día 5 |

---

## Matriz de Dependencias Críticas (Ruta Crítica)

```
Kickoff → Copy Final (Día 5 S1) → Diseño Hi-Fi (Día 4 S2) → Dev Implementación (Día 3 S3)
→ QA (Día 1 S4) → Deploy Producción (Día 4 S4) → Launch (Día 5 S4)
```

**Puntos de fallo comunes:**
1. **Copy no congelado:** Si el copywriter cambia textos el día 3 de la semana 2, el diseño se retrasa. *Mitigación:* Usar placeholders de longitud similar y hacer "copy freeze" estricto al inicio de semana 2.
2. **Falta de assets reales:** Si esperan screenshots del producto y el producto no está listo, pierden 3-4 días. *Mitigación:* El diseñador crea mockups de alta fidelidad en Figma desde el día 3 de la semana 2.
3. **Integración de email falla:** Si la API de Mailchimp/HubSpot da problemas el día 4 semana 3. *Mitigación:* Tener fallback listo (formulario que envía a un Google Sheet vía Zapier o mailto temporal).

---

## Distribución de Carga por Rol

| Rol | Semana 1 | Semana 2 | Semana 3 | Semana 4 |
|-----|----------|----------|----------|----------|
| **Copywriter** | 100% (copy completo) | 20% (micro-copy UI, legal) | 10% (revisión) | 40% (QA copy, kit lanzamiento) |
| **Diseñador** | 30% (research, arquitectura) | 100% (diseño completo) | 10% (soporte dev) | 10% (ajustes visuales) |
| **Dev 1 (Frontend Lead)** | 20% (setup inicial) | 30% (preparación técnica) | 90% (desarrollo desktop, SEO) | 60% (QA, deploy, hotfixes) |
| **Dev 2 (Fullstack/Integrations)** | 10% (config cuentas) | 20% (setup CI/CD) | 90% (mobile, integraciones, analytics) | 70% (QA, monitoreo, legal pages) |

---

## Riesgos y Mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| El producto no tiene UI lista para screenshots | Alta | Alto | Diseñador crea mockups realistas en Figma (día 3-4 S2) |
| Cambios de última hora en features/pricing | Media | Alto | Freeze de contenido semana 2; cambios solo en semana 4 si son críticos |
| Problemas de performance (imágenes pesadas de dashboards) | Media | Medio | Usar next/image, formatos WebP/AVIF, lazy loading obligatorio |
| Formulario no envía emails en producción | Baja | Crítico | Probar en staging con email real; tener plan B (Zapier → Google Sheets) |
| No cumple velocidad móvil (Core Web Vitals) | Media | Alto | Lighthouse en CI/CD; no pasar a producción si LCP > 2.5s |

---

## Definition of Done (Listo para lanzar)

- [ ] Landing carga en < 2 segundos (LCP) en 4G móvil
- [ ] 100% responsive (probado en iPhone SE, iPhone 14, iPad, Desktop 1440px)
- [ ] Formulario envía datos a CRM/email y muestra confirmación
- [ ] Todos los links funcionan (internos y externos)
- [ ] Meta tags OG correctos (se ve bien al compartir en WhatsApp/LinkedIn)
- [ ] Páginas /privacy y /terms accesibles desde footer
- [ ] Analytics recibiendo datos (verificar en tiempo real de GA4)
- [ ] Sin errores en consola del navegador
- [ ] SEO básico: title, description, h1 único, schema markup

---

## Herramientas Recomendadas para este equipo pequeño

- **Gestión:** Notion (todo en una página: brief, copy, diseño, bugs) o Linear (más ágil para devs)
- **Diseño:** Figma (colaborativo, handoff automático a devs)
- **Desarrollo:** GitHub + Vercel (deploy automático en cada push a main)
- **Comunicación:** Slack/Discord con canales #landing-launch
- **QA:** BrowserStack (si tienen presupuesto) o dispositivos físicos propios + Chrome DevTools

**Tip final:** En la semana 4, hagan un **"soft launch"** el miércoles: compartan la URL solo con amigos/familia/colegas para que prueben el formulario y den feedback antes del anuncio público el viernes. Esto evita vergüenzas públicas.