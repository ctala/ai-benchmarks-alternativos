# Step 3.5 Flash — task_management/project_breakdown

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.97 | quality: 10.0
- latency_total: 37.932s | tokens_per_second: 54.0
- input_tokens: 82 | output_tokens: 2048
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

## **Plan de Lanzamiento de Landing Page para SaaS de Gestión de Inventario**  
**Duración total:** 4 semanas (20 días laborables)  
**Equipo:** 1 Diseñador UX/UI, 2 Desarrolladores (Frontend + Backend básico), 1 Copywriter.  
**Objetivo:** Landing page funcional, optimizada para conversión (captación de leads), lista para lanzamiento.

---

### **Fase 1: Investigación y Planificación (Días 1-3)**
**Objetivo:** Alinear visión, definir estructura y mensaje clave.  
**Responsable principal:** Copywriter + Diseñador (liderazgo compartido).  
**Tareas:**  
1. **Briefing del producto** (Día 1): Reunión con stakeholders para entender funcionalidades, ventajas competitivas y buyer persona.  
2. **Análisis de competencia** (Día 1-2): Revisar 3-5 landing pages de competidores directos (ej: Zoho Inventory, TradeGecko).  
3. **Definición de estructura y flujo** (Día 2):  
   - Esquema de secciones: Hero, Problema/Solución, Features, Precios, Testimonios, FAQ, CTA.  
   - Mapa de journey del usuario (desde entrada a conversión).  
4. **Definición de KPIs** (Día 3): Métricas de éxito (ej: tasa de conversión > 3%, tiempo en página > 2 min).  
**Entregable:** Documento de especificaciones + esquema de wireframes en baja fidelidad (Figma/Whimsical).

---

### **Fase 2: Diseño UX/UI (Días 4-8)**
**Objetivo:** Prototipo de alta fidelidad listo para desarrollo.  
**Responsable principal:** Diseñador.  
**Tareas:**  
1. **Wireframes detallados** (Día 4-5): Layouts por sección, jerarquía visual, placements de CTAs.  
2. **Diseño de interfaz (UI)** (Día 6-7):  
   - Paleta de colores, tipografía, iconografía.  
   - Mockups en Figma para desktop y mobile (responsive优先).  
   - Microinteracciones (hover, scroll animations).  
3. **Validación interna** (Día 8): Revisión con equipo (copy + devs) para factibilidad técnica y coherencia de mensaje.  
**Dependencias:**  
- Requiere especificaciones de Fase 1.  
- Copywriter debe proporcionar textos preliminares (ver Fase 3) para integrar en mockups.  
**Entregable:** Prototipo interactivo en Figma (link compartido).

---

### **Fase 3: Desarrollo Frontend y Backend Básico (Días 5-15)**
**Objetivo:** Implementación técnica de la landing page.  
**Responsables principales:** 2 Desarrolladores (división de tareas).  
**Tareas (en paralelo donde sea posible):**  
1. **Setup inicial** (Día 5):  
   - Repositorio Git, estructura de proyecto (React/Next.js o HTML/CSS/JS estático).  
   - Configuración de entorno de desarrollo.  
2. **Desarrollo de componentes** (Días 6-12):  
   - Developer 1: Header, Hero, Sección Problema/Solución, Features.  
   - Developer 2: Formulario de captación leads, integración con CRM/email (ej: HubSpot, Mailchimp), Precios, Testimonios, FAQ, Footer.  
   - Ambos: Responsive design (mobile-first), accesibilidad (WCAG 2.1).  
3. **Integración de textos** (Día 13):  
   - Implementar copy final (entregado por copywriter en Fase 2/3).  
   - Asegurar SEO básico (meta tags, headings, alt text).  
4. **Backend mínimo** (Día 14-15):  
   - API simple para envío de formulario (validación, almacenamiento en BD o servicio tercero).  
   - Configuración de analytics (Google Analytics 4, Hotjar para heatmaps).  
**Dependencias:**  
- Requiere prototipo de diseño (Fase 2) para iniciar.  
- Copywriter debe entregar textos finales **antes del Día 13**.  
**Entregable:** Landing page desplegada en entorno de staging (Netlify/Vercel + backend en Heroku/Railway).

---

### **Fase 4: Copywriting y Optimización de Conversión (Días 4-12)**
**Objetivo:** Textos persuasivos y alineados con la marca.  
**Responsable principal:** Copywriter.  
**Tareas:**  
1. **Redacción de textos por sección** (Día 4-7):  
   - Headlines, subheadlines, descripciones de features, bullets de beneficios.  
   - CTAs (ej: “Prueba Gratis 14 Días”, “Agenda una Demo”).  
2. **Optimización para SEO** (Día 8):  
   - Palabras clave primarias (ej: “software gestión inventario”, “control stock PYMES”).  
   - Meta descriptions, URLs amigables.  
3. **Creación de contenido social proof** (Día 9-10):  
   - Testimonios ficticios/realistas (si no hay clientes reales still).  
   - Logos de “empresas que usan el producto” (placeholders si es necesario).  
4. **Revisión con diseñador** (Día 11): Ajustar longitud de textos a layouts.  
**Dependencias:**  
- Coordinación constante con diseñador (Fase 2) y desarrolladores (Fase 3).  
**Entregable:** Documento Google Docs con todos los textos + listado de keywords.

---

### **Fase 5: Pruebas y Ajustes (Días 16-18)**
**Objetivo:** Asegurar calidad técnica, UX y de rendimiento.  
**Responsables:** Todo el equipo (testing colaborativo).  
**Tareas:**  
1. **QA técnico** (Día 16):  
   - Devs: Funcionalidad de formulario, velocidad de carga (Lighthouse > 90), compatibilidad navegadores.  
2. **QA de UX/UI** (Día 17):  
   - Diseñador: Revisión pixel-perfect, consistencia, breakpoints.  
3. **Pruebas de copy** (Día 17):  
   - Copywriter: Revisión de textos en contexto, calls-to-action claros.  
4. **Correcciones** (Día 18): Ajustes priorizados (críticos > menores).  
**Entregable:** Lista de bugs resueltos + informe de testing.

---

### **Fase 6: Lanzamiento y Medición (Días 19-20)**
**Objetivo:** Despliegue en producción y monitorización inicial.  
**Responsables:** Desarrolladores (lideran), Copywriter (monitoriza contenido).  
**Tareas:**  
1. **Despliegue en producción** (Día 19):  
   - Migración desde staging a dominio oficial.  
   - Configurar SSL, CDN (Cloudflare), backups.  
2. **Configuración de analíticas** (Día 19):  
   - Google Analytics 4 (eventos: clics en CTA, scroll depth).  
   - Hotjar/PureClick para grabaciones de sesiones.  
3. **Pruebas finales en vivo** (