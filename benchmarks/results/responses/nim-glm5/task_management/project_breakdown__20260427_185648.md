# GLM 5 (NIM) — task_management/project_breakdown

- model_id: `z-ai/glm5`
- success: True  | final: 7.1 | quality: 9.44
- latency_total: 99.942s | tokens_per_second: 18.1
- input_tokens: 73 | output_tokens: 1813
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para lanzar una landing page en 4 semanas con un equipo de 4 personas, la clave está en la **paralelización de tareas** (hacer cosas al mismo tiempo) y la **sincronización** (que nadie bloquee a otro). 

Dado que es un SaaS de inventario, el copywriter debe entender el valor del producto (ahorro de tiempo, evitar roturas de stock, multisede, etc.), el diseñador debe traducir eso en una UI limpia y confiable (es software de gestión), y los devs deben priorizar la funcionalidad sobre el exceso de animaciones.

Aquí tienes el plan de proyecto detallado.

---

### 👥 Roles y Abreviaturas
*   **CW:** Copywriter
*   **DS:** Diseñador/a
*   **DV1:** Developer 1 (Enfoque en Front-end / UI)
*   **DV2:** Developer 2 (Enfoque en Back-end / Integraciones y DevOps)

---

### 📋 FASE 1: Estrategia y Arquitectura (Semana 1)
*El objetivo es tener el mensaje claro, el texto base y la estructura listas para que el diseñador y los devs empiecen sin bloqueos.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| 1.1 Definir propuesta de valor y público objetivo | CW | Ninguna | Documento de posicionamiento |
| 1.2 Redacción del copy primario (Hero, Beneficios, CTA) | CW | 1.1 | Documento de Copy (Google Docs) |
| 1.3 Definir estructura y secciones de la LP (Wireframe low-fi) | DS, CW | 1.2 | Wireframe estructural |
| 1.4 Setup del repositorio (Git) y entorno de desarrollo | DV2 | Ninguna | Repo inicial, framework elegido |
| 1.5 Definir stack tecnológico y proveedor de email (Mailchimp, etc.) | DV1, DV2 | Ninguna | Stack definido (Ej: Next.js + Tailwind) |

---

### 🎨 FASE 2: Diseño y Preparación de Desarrollo (Semana 2)
*El diseñador crea los archivos finales, el CW profundiza en el micro-copy y los devs preparan la infraestructura y componentes base.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| 2.1 Diseño UI de la Landing Page (Desktop) | DS | 1.3 | Archivo Figma completo |
| 2.2 Diseño UI de la Landing Page (Mobile) | DS | 2.1 | Archivo Figma responsive |
| 2.3 Redacción de micro-copy (botones, formularios, errores) | CW | 2.1 | Micro-copy integrado en Figma/Doc |
| 2.4 Búsqueda/selección de imágenes o ilustraciones | DS | 1.3 | Banco de imágenes |
| 2.5 Maquetación de componentes base (Header, Footer, Botones) | DV1 | 1.5 | Componentes UI en código |
| 2.6 Configuración de dominio, hosting (Vercel/Netlify) y SSL | DV2 | 1.5 | Entorno staging online |
| 2.7 Setup del proveedor de Email Marketing y bases de datos | DV2 | 1.5 | API keys y listas creadas |

---

### 💻 FASE 3: Desarrollo e Integración (Semana 3)
*Esta es la semana más intensa. Ambos devs trabajan en paralelo para montar la página y conectar la lógica.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| 3.1 Desarrollo Front-end de secciones estáticas | DV1 | 2.1, 2.5 | Maquetación HTML/CSS completa |
| 3.2 Desarrollo e integración del formulario de captación | DV2 | 2.7, 2.3 | Formulario conectado a BD/Email |
| 3.3 Integración de imágenes y assets optimizados | DV1 | 2.4, 3.1 | Imágenes en WebP/avif cargadas |
| 3.4 Animaciones sutiles e interacciones (Hover, scroll) | DV1 | 3.1 | UI interactiva |
| 3.5 Integración de Analytics (GA4, Meta Pixel, etc.) | DV2 | 2.6 | Píxeles rastreando eventos |
| 3.6 Pruebas internas de flujo de usuario (Registro -> Email) | CW, DV2 | 3.2 | Flujos validados |

---

### 🚀 FASE 4: QA, Pulido y Lanzamiento (Semana 4)
*Semana de pulido, pruebas cruzadas y preparación para el lanzamiento.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| 4.1 Revisión visual (Comparar Figma vs Navegador) | DS | 3.1, 3.4 | Lista de bugs visuales |
| 4.2 Revisión de copy en contexto (Revisión final) | CW | 3.1 | Ajustes de texto en código |
| 4.3 Fix de bugs visuales y responsive | DV1 | 4.1 | UI pixel-perfect |
| 4.4 Pruebas de rendimiento (Core Web Vitals) y SEO técnico | DV2 | 3.3, 3.5 | Lighthouse score > 90 |
| 4.5 Pruebas cruzadas de navegador (Safari, Chrome, Firefox) | Todos | 4.3 | Navegadores validados |
| 4.6 Configuración de emails de bienvenida automatizados | CW, DV2 | 3.2 | Secuencia de emails activa |
| 4.7 **LANZAMIENTO (Go Live)** | DV2 | 4.4, 4.5 | Página pública |
| 4.8 Monitoreo post-lanzamiento (primeras 24-48 hrs) | DV1, DV2 | 4.7 | Estabilidad asegurada |

---

### ⚠️ Riesgos y Consejos de Gestión

1. **El bloqueo del Diseñador (Semana 2):** El DS suele ser el cuello de botella. Para evitarlo, el CW debe tener el copy *aprobado* al final de la Semana 1, y el DS debe hacer el diseño Mobile-first o entregar el Desktop a mitad de la Semana 2 para que DV1 empiece a maquetar ya.
2. **El síndrome del "Pixel Perfect":** En una landing de lanzamiento, la velocidad importa más que una sombra de 2px vs 4px. Si el diseño está al 90%, los devs deben avanzar.
3. **Integración de Email Marketing:** Suele dar problemas (CORS, APIs, doble opt-in). Haz que DV2 empiece a probar la conexión del formulario con Mailchimp/SendGrid en la Semana 2 con un formulario feo, así en la Semana 3 solo hay que conectarle la UI bonita.
4. **Optimización de imágenes:** Al ser un SaaS de inventario, probablemente usaréis capturas de pantalla del dashboard. **Ojo con el peso.** Pasadlas por TinyPNG o usad formato WebP antes de subirlas al código.
5. **Reunión diaria de 15 mins:** Al ser solo 4 personas y 4 semanas, haced un check-in diario (Lunes a Viernes) de 15 minutos para responder a: *Qué hice ayer, qué haré hoy, qué me bloquea.*

### 📈 Post-Lanzamiento (Inmediato)
El trabajo del CW no termina al lanzar. Debe preparar los emails de seguimiento para los leads captados y los textos para las redes sociales/ads, mientras los devs monitorizan que la página no caiga ante el tráfico inicial.