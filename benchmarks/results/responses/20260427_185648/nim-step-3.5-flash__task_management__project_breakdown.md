# Step 3.5 Flash (NIM) — task_management/project_breakdown

- model_id: `stepfun-ai/step-3.5-flash`
- success: True  | final: 7.23 | quality: 9.52
- latency_total: 44.283s | tokens_per_second: 46.2
- input_tokens: 82 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

Excelente planteamiento. Un lanzamiento en 4 semanas con un equipo de 4 personas es un desafío realista pero que requiere una **focalización extrema en un MVP (Producto Mínimo Viable) de la landing page** y una comunicación constante.

Aquí tienes un desglose detallado, priorizando la velocidad y la calidad sobre la perfección.

---

### **Filosofía del Plan:**
*   **MVP Landing Page:** Una página que cumpla su función principal: **explicar el valor, generar confianza y captar leads (emails)**. Nada de funcionalidades extra.
*   **Parallelismo Máximo:** Las tareas de diseño y copy deben avanzar en paralelo, alimentándose mutuamente.
*   **Dependencias Críticas:** Identificadas y gestionadas activamente. El desarrollador no puede empezar sin el diseño视觉 y el copy final.
*   **Buffer de 2-3 días:** Incluidos en la última semana para imprevistos, testeo y ajustes.

---

### **Fase 0: Alineación y Planificación (Día 1)**
**Objetivo:** Todo el equipo debe tener la misma visión y entender el "por qué" de cada elemento.

| Tarea | Responsable(s) | Duración | Dependencias | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| **Kick-off Meeting** | Todos | 2h | Ninguna | Consensus en: <br>• Público objetivo (buyer persona).<br>• Propuesta de valor única (UVP).<br>• Objetivo principal de la página (ej: 100 leads).<br>• Ejemplos de competencia/benchmark. |
| Definir la estructura (sitemap) | Copy + Diseñador | 2h | Kick-off | Lista de secciones en orden lógico (Hero, Problema/Solución, Features, Social Proof, Pricing, CTA final). |
| Definir el flujo de captura | Todos | 1h | Estructura | ¿Dónde y cómo se captura el email? (Formulario en hero, en pricing, pop-up?). ¿Con qué herramienta se integra? (Ej: Mailchimp, HubSpot). |

---

### **Fase 1: Creación de Contenidos & Diseño Visual (Días 2-5)**
**Objetivo:** Tener todos los *assets* listos para que desarrollo pueda construir sin bloqueos.

| Tarea | Responsable(s) | Duración | Dependencias | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| **Copywriting - Borrador completo** | Copywriter | 2 días | Estructura | Textos para **todas** las secciones, incluyendo: <br>• Títulos y subtítulos (H1, H2).<br>• Párrafos de cuerpo.<br>• Textos de botones (CTAs).<br>• Microcopy (del formulario, placeholders).<br>**Nota:** Se entrega en un doc compartido (Google Docs). |
| **Diseño de Wireframes (baja fidelidad)** | Diseñador | 1.5 días | Estructura + Borrador copy (suficiente con los títulos) | Wireframes en **Figma/Adobe XD** que definen: <br>• Layout de cada sección.<br>• Jerarquía visual.<br>• Ubicación de elementos clave (CTAs, imágenes, iconos). |
| **Revisión conjunta Wireframes + Copy** | Todos | 1h | Wireframes + Borrador copy | Feedback rápido. Ajustar layout si el copy es muy largo/corto. **Aprobación para pasar a diseño visual.** |
| **Diseño Visual (alta fidelidad)** | Diseñador | 2 días | Wireframes aprobados + Paleta de marca (si existe) | **Mockups completos en Figma:** <br>• Cada sección al 100%.<br>• Estados de :hover, :focus.<br>• Versionado responsive (mobile-first).<br>• Assets listos (iconos, imágenes de stock/placeholder). |
| **Copy - Versión Final** | Copywriter | 0.5 días | Diseño visual (para ajustar longitud) | Copy pulido, listo para implementar. Texto exacto en un archivo o en el mismo Figma (comentarios). |

---

### **Fase 2: Desarrollo & Integración (Días 6-11)**
**Objetivo:** Construir una landing page funcional, responsive y rápida.

| Tarea | Responsable(s) | Duración | Dependencias | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| **Setup proyecto & componentes base** | Dev 1 | 0.5 días | Diseño visual (para paleta, tipografías) | Estructura de archivos, variables CSS, componentes base (botón, input, contenedor). |
| **Desarrollo Hero & Sección Features** | Dev 1 | 2 días | Componentes base + Copy/Diseño de esas secciones | Hero y Features codificadas y responsive. |
| **Desarrollo Social Proof & Pricing** | Dev 2 | 1.5 días | Componentes base + Copy/Diseño | Secciones con logos, testimonios y tablas de precios. |
| **Desarrollo formulario & lógica de captura** | **AMBOS DEVS** (en pair) | 1 día | Copy/Diseño del formulario + **Decisión de herramienta de email** | Formulario funcional con validación frontend y conexión a la API de la herramienta de email (Mailchimp, etc.). |
| **Desarrollo Footer & CTA final** | Dev 2 | 0.5 días | Copy/Diseño | Pie de página y último llamado a la acción. |
| **Integración total & responsive check** | Ambos Devs | 1 día | Todas las secciones | Página completa, probada en breakpoints clave (mobile, tablet, desktop). |
| **Optimización de rendimiento básica** | Dev 1 | 0.5 días | Página completa | Compresión de imágenes, lazy loading, minimización de CSS/JS. |

---

### **Fase 3: Testing, Revisión y Ajustes (Días 12-14)**
**Objetivo:** Asegurar que la página funciona perfectamente en todos los aspectos antes del lanzamiento.

| Tarea | Responsable(s) | Duración | Dependencias | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| **Testing funcional (cross-browser/device)** | Ambos Devs | 1 día | Página en staging | Lista de bugs (en Notion/Trello). Chrome, Safari, Firefox, iOS, Android. |
| **Testing de copy & UX** | Copywriter + Diseñador | 0.5 días | Página en staging | Feedback sobre claridad del mensaje, tono, fluidez de lectura. |
| **Testing de formulario & lead capture** | Copywriter + **UN DEV** | 0.5 días | Formulario integrado | Prueba de envío, confirmación, llegada del email a la lista. |
| **Sprint de bugs & ajustes** | Ambos Devs | 1.5 días | Lista de bugs priorizada | Todos los bugs críticos y mayores corregidos. |
| **Revisión final de SEO básico** | Copywriter + Dev 1 | 0.5 días | Página corregida | Meta title, meta description, etiquetas H1/H2, alt text en imágenes. URL amig