# Gemini 3.6 Flash — task_management/project_breakdown

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.32 | quality: 9.7
- latency_total: 20.359s | tokens_per_second: 167.6
- input_tokens: 62 | output_tokens: 3412
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando un desglose detallado y estructurado del proyecto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Lanzar una landing page en 4 semanas con este equipo (**1 Copywriter, 1 Diseñador, 2 Developers**) es un objetivo perfectamente alcanzable si se trabaja de forma **ágil y paralela**, evitando cuellos de botella. 

A continuación, tienes la estructura detallada del proyecto.

---

### Asignación de Roles
*   **CW (Copywriter):** Propuesta de valor, textos, estructura de persuasión, SEO básico y micro-copy (CTAs, formularios).
*   **DES (Diseñador UX/UI):** Wireframes, diseño visual (desktop/mobile), assets gráficos (ilustraciones/mockups del SaaS).
*   **DEV 1 (Frontend Lead):** Maquetación HTML/CSS/JS, componentes interactivos, animaciones y adaptabilidad responsive.
*   **DEV 2 (Backend / Integraciones / QA):** Configuración de dominio/hosting, formularios, integración con CRM/Email Marketing, Analytics, optimización de velocidad (WPO) y SEO técnico.
*   **PM (Tú / Product Owner):** Aprobaciones rápidas, gestión de bloqueos y alineación con negocio.

---

### Plan de Trabajo Semana a Semana

#### **SEMANA 1: Estrategia, Copywriting y Estructura (Wireframing)**
*El objetivo de esta semana es definir QUÉ vamos a decir y CÓMO se va a estructurar.*

*   **Día 1: Kickoff del Proyecto (Todo el equipo - 2 horas)**
    *   Definir el Buyer Persona, propuesta de valor principal, objetivo de la landing (ej. captar leads para beta privada o prueba gratuita) y stack tecnológico.
*   **Tareas de la Semana:**
    1.  **CW:** Redacción del Framework de Mensajería y primer borrador del Copy completo (Hero section, beneficios, características, prueba social, FAQ, CTAs). *(Dep: Kickoff)*
    2.  **DES:** Crear la arquitectura de información y **Wireframes de baja fidelidad** (UX) en Figma basándose en el borrador de copy. *(Dep: Borrador de Copy en progreso)*
    3.  **DEV 2:** Configuración del entorno de desarrollo, repositorio (GitHub/GitLab), staging, hosting (Vercel/Netlify/Server) y arquitectura base. *(Dep: Ninguna)*
    4.  **DEV 1:** Creación del sistema de diseño base en código (librería de UI, variables de color, tipografías globales). *(Dep: Ninguna)*

*📌 **Hito Semana 1:** Wireframe de UX y Copy v1 aprobados.*

---

#### **SEMANA 2: Diseño UI Final y Preparación de Assets**
*El objetivo es pasar de la estructura a la interfaz visual final lista para producción.*

*   **Tareas de la Semana:**
    1.  **DES:** Diseño de **Alta Fidelidad (UI)** en Figma (Desktop y Mobile), incluyendo estados de botones, formularios y UI Kit. *(Dep: Wireframes Semana 1)*
    2.  **DES:** Creación/exportación de assets visuales (Mockups de la interfaz del SaaS, iconos, imágenes optimizadas en WebP/SVG). *(Dep: UI Desktop)*
    3.  **CW:** Pulido final del copy (corrección de estilo, ajuste de espacios según diseño visual y llamadas a la acción final). *(Dep: UI en progreso)*
    4.  **DEV 1:** Maquetación de la estructura HTML/CSS estática basada en el avance del diseño UI. *(Dep: UI Desktop parcial)*
    5.  **DEV 2:** Configuración de la base de datos/CRM (HubSpot, Mailchimp, Supabase, etc.) para la captura de leads y lógica del formulario. *(Dep: Definición de campos de formulario)*

*📌 **Hito Semana 2:** Diseño UI (Desktop + Mobile) 100% aprobado y assets exportados.*

---

#### **SEMANA 3: Desarrollo Frontend e Integraciones**
*El objetivo es transformar el diseño en un sitio web funcional y conectado.*

*   **Tareas de la Semana:**
    1.  **DEV 1:** Desarrollo del Frontend responsive (Desktop, Tablet, Mobile) alineado al diseño pixel-perfect. *(Dep: UI final y Assets)*
    2.  **DEV 1:** Implementación de micro-interacciones, efectos hover y animaciones de scroll (GSAP/Framer Motion si aplica). *(Dep: Layout base)*
    3.  **DEV 2:** Conexión del formulario con el CRM/Email Marketing (envío de webhooks, lógica de confirmación/error). *(Dep: Form en Frontend)*
    4.  **DEV 2:** Implementación de cookies, pixels de seguimiento (Google Analytics 4, Meta Pixel, Hotjar) y etiquetas SEO (OpenGraph, Meta descriptions compuestas por CW). *(Dep: Copy final)*
    5.  **CW:** Creación del email automático de bienvenida (Autoresponder) que recibe el usuario tras registrarse. *(Dep: Definición de flujo de captación)*

*📌 **Hito Semana 3:** Landing Page 100% funcional en entorno de Staging (Pruebas).*

---

#### **SEMANA 4: QA, Optimización y Lanzamiento (Go-Live)**
*El objetivo es asegurar que nada falle, que cargue rápido y publicar.*

*   **Tareas de la Semana:**
    1.  **DEV 1 & DEV 2:** Testing Cross-Browser (Chrome, Safari, Firefox, Edge) y Cross-Device (iOS, Android). *(Dep: Funcionalidad Semana 3)*
    2.  **DES & CW:** Revisión de diseño visual ("Design QA") y revisión tipográfica/ortográfica en el entorno de pruebas. *(Dep: Funcionalidad Semana 3)*
    3.  **DEV 2:** Optimización de rendimiento (WPO): compresión extrema de imágenes, lazy loading, minificación de código para lograr >90 en Google PageSpeed Insights. *(Dep: Código final)*
    4.  **DEV 2:** Configuración de DNS, certificado SSL y apuntamiento del dominio final. *(Dep: QA Aprobado)*
    5.  **TODOS:** **LANZAMIENTO OFICIAL (Día 26 u 27).**
    6.  **DEV 1 & DEV 2 (Post-Lanzamiento):** Monitoreo de 48 horas post-launch para corregir bugs de último minuto e inspeccionar tasa de conversión de formularios.

*📌 **Hito Semana 4:** Sitio Web en Producción y Funcionando.*

---

### Resumen del Cronograma y Dependencias (Matriz RACI/Gantt simplificada)

| Tarea Clave | Resp. Principal | Apoyo | Dependencia Crítica | Semana |
| :--- | :--- | :--- | :--- | :--- |
| Estrategia + Copy V1 | **CW** | PM | Kickoff | **S1** |
| Wireframes UX | **DES** | CW | Copy V1 en borrador | **S1** |
| Setup Tech & Repo | **DEV 2** | DEV 1 | N/A | **S1** |
| Diseño UI Desktop/Mobile | **DES** | PM / CW | Wireframes aprobados | **S2** |
| Integración CRM / Backend | **DEV 2** | - | Campos de formulario | **S2-S3** |
| Maquetación Frontend | **DEV 1** | DES | UI Diseñado + Assets | **S2-S3** |
| SEO Técnico & Analytics | **DEV 2** | CW | Copy final | **S3** |
| Testing / QA / Speed | **DEV 1 & 2** | DES / CW | Web en Staging | **S4** |
| **DESPLIEGUE (Go-Live)** | **DEV 2** | Todos | QA Aprobado | **S4** |

---

### Factores Críticos de Éxito (Para evitar retrasos)

1.  **Copy-First, Not Design-First:** El diseñador **no** debe empezar a diseñar en alta fidelidad sin el texto casi definitivo. Diseñar con "Lorem Ipsum" en una landing SaaS causa retrasos masivos al reajustar layout.
2.  **Freeze de Contenido en Semana 2:** A partir del final de la Semana 2, no se cambian textos ni layouts salvo que sea un error ortográfico grave.
3.  **Reuniones Diarias Cortas (Daily Standups):** 15 minutos al día para revisar: *¿Qué hice ayer?, ¿Qué haré hoy?, ¿Tengo algún bloqueo?*
4.  **Aprobación Exprés:** El PM debe aprobar los entregables (Wireframe, UI y Copy) en un plazo máximo de 24 horas para no pisar las tareas de los developers.