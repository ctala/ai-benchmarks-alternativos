# Mercury 3 — task_management/project_breakdown

- model_id: `inception/mercury-3`
- success: True  | final: 9.35 | quality: 10.0
- latency_total: 4.55s | tokens_per_second: 370.1
- input_tokens: 66 | output_tokens: 1684
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

¡Excelente! Un lanzamiento en 4 semanas es agresivo pero totalmente factible si se prioriza un **MVP de página** (no un sitio gigante). Aquí tienes un plan de ejecución quirúrgico, con fases, dependencias y roles claros.

---

### 🎯 Estrategia General (Clave para el Éxito)
- **Enfoque "Mobile-First" y "Conversion-First"**: La página debe tener **una sola llamada a la acción (CTA)** principal (ej: "Solicitar Demo" o "Únete a la Lista de Espera").
- **Herramientas**: Usa **Webflow, Framer o Next.js + Tailwind** (si los developers prefieren código). Evita construir un CMS complejo; el contenido será estático.
- **Contenido "Evergreen"**: El copywriter debe escribir el texto **antes** de que el diseñador termine los mockups, para evitar cuellos de botella.

---

### 📅 Timeline Realista (4 Semanas / 28 Días)

**Semanas 1 y 2: Fundación y Diseño (Paralelo)**
**Semana 3: Desarrollo y Contenido Final**
**Semana 4: QA, Lanzamiento y Post-Lanzamiento**

---

### 🗂️ Desglose por Fases, Tareas y Responsables

| Fase | Tarea | Responsable | Dependencia | Días (Estimado) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Estrategia** | Definir propuesta de valor única (USP) y tono de voz. | Copywriter + PM | Ninguna | Día 1 |
| | Definir estructura de la página (Hero, Features, Testimonios, FAQ, CTA). | Diseñador + PM | Ninguna | Día 1 |
| | **Recopilar activos**: Logo, screenshots del producto, logos de clientes (si hay). | PM | Ninguna | Día 1-2 |
| **2. Contenido** | Escribir **todos** los textos (Hero, secciones, FAQ, meta descripción). | Copywriter | Fase 1 (Estrategia) | Día 2-4 |
| | Crear copy para el formulario de captura (email, nombre, empresa). | Copywriter | Fase 1 | Día 4 |
| | **Enviar copy final al diseñador y developers.** | Copywriter | Ninguna | **Día 5 (Deadline crítico)** |
| **3. Diseño UI/UX** | Crear wireframes de baja fidelidad (bocetos). | Diseñador | Fase 1 (Estructura) | Día 2-3 |
| | Diseñar mockups de alta fidelidad (desktop + mobile). | Diseñador | Copy final (Día 5) | Día 5-9 |
| | Diseñar el sistema de componentes (botones, colores, tipografía). | Diseñador | Mockups | Día 8-10 |
| | **Exportar assets (SVG, imágenes) y entregar a developers.** | Diseñador | Mockups | **Día 10 (Deadline crítico)** |
| **4. Desarrollo** | Configurar el proyecto (repo, framework, CI/CD). | Dev 1 | Ninguna | Día 2-3 |
| | Desarrollar el layout base (header, footer, secciones). | Dev 1 | Assets de diseño (Día 10) | Día 10-14 |
| | Implementar el formulario de captura (integración con Email Marketing / CRM). | Dev 2 | Copy final | Día 12-15 |
| | Hacer la página **responsive** (mobile, tablet, desktop). | Dev 2 | Layout base | Día 14-16 |
| | Integrar analítica (Google Analytics / Plausible) y tracking de conversiones. | Dev 1 | Formulario | Día 16-17 |
| **5. QA y Revisión** | Revisión visual y de contenido (bugs de diseño, typos). | Diseñador + PM | Desarrollo completo | Día 18-19 |
| | Test de funcionalidad del formulario (envío de emails, validación). | Dev 2 + PM | Formulario | Día 18-19 |
| | Optimización de rendimiento (velocidad de carga, imágenes). | Dev 1 | Desarrollo completo | Día 19-20 |
| | **Congelación de código (Code Freeze).** | Todos | QA | **Día 20** |
| **6. Lanzamiento** | Deploy a producción (dominio, hosting, SSL). | Dev 1 | Code Freeze | Día 21 |
| | Prueba final en producción (smoke test). | PM + Dev 2 | Deploy | Día 21 |
| | **Lanzamiento público** (anuncio en redes, email a lista). | PM + Copywriter | Deploy | **Día 22** |
| **7. Post-Lanzamiento** | Monitoreo de errores y analítica (primeras 24-48h). | Dev 1 + PM | Lanzamiento | Día 23-24 |
| | Iteración rápida (fix de bugs menores, ajustes de copy si el CTR es bajo). | Todos | Datos de analítica | Día 24-28 |

---

### 🔗 Dependencias Críticas (Los "Cuellos de Botella")
1.  **El Copy es el Rey**: El diseñador **no puede** hacer mockups finales sin el copy final. Por eso, el copywriter debe entregar **antes del Día 5**.
2.  **El Diseño es el Gatillo**: Los developers **no pueden** construir la página sin los assets finales. El diseñador debe entregar **antes del Día 10**.
3.  **El Formulario es el Corazón**: La integración del formulario con el CRM (ej: HubSpot, Mailchimp) debe probarse **antes** del lanzamiento.

---

### 🚨 Plan de Contingencia (Si algo se retrasa)
- **Si el copy se retrasa**: El diseñador crea mockups con **texto placeholder (Lorem Ipsum)** y el copy se inserta en la fase de desarrollo.
- **Si el diseño se retrasa**: Los developers construyen el layout base con **CSS puro** y un sistema de grid simple, y el diseño visual se aplica después.
- **Si el formulario falla**: Usa un **enlace directo a Calendly o un formulario de Google Forms** como respaldo temporal.

---

### 🛠️ Herramientas Recomendadas (Para Acelerar)
- **Diseño**: Figma (para colaboración en tiempo real).
- **Desarrollo**: Next.js (para SEO y velocidad) o Framer (para lanzamiento ultra-rápido).
- **Email Marketing**: Mailchimp, ConvertKit o HubSpot (para capturar leads).
- **Analítica**: Google Analytics 4 + Hotjar (para ver el comportamiento del usuario).

---

### ✅ Checklist Final Antes del Lanzamiento
- [ ] La página carga en <3 segundos (test en GTmetrix).
- [ ] El formulario envía un email de confirmación al usuario.
- [ ] La página se ve perfecta en iPhone y Android.
- [ ] El SEO básico está configurado (title, meta description, Open Graph).
- [ ] Tienes un plan de qué hacer si el tráfico es alto (el hosting aguanta).

**¿Quieres que profundice en alguna fase específica (ej: la estructura de la página o el copy del Hero)?** Estoy aquí para ayudarte a pulir cada detalle. ¡Mucho éxito con el lanzamiento! 🚀