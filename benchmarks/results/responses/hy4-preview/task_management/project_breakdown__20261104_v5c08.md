# Tencent Hy4 preview — task_management/project_breakdown

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 34.818s | tokens_per_second: 50.3
- input_tokens: 96 | output_tokens: 1752
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y realista del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Lanzar una landing page de alta calidad en 4 semanas con ese equipo es un objetivo **muy realista**, siempre y cuando se evite el "cuello de botella" (esperar a que diseño termine todo para que desarrollo empiece, o que copy espere al diseño).

La clave aquí es trabajar en **paralelo** utilizando un sistema de diseño ágil (Content-first o Design Systems).

Aquí tienes el desglose del proyecto optimizado para tu equipo (1 Diseñador, 2 Devs, 1 Copywriter).

---

### 🗓️ Resumen del Timeline (4 Semanas)

*   **Semana 1: Estrategia y Estructura (Content & Wireframes)**
*   **Semana 2: Diseño Visual y Setup Técnico**
*   **Semana 3: Desarrollo y Maquetación**
*   **Semana 4: Integración, QA y Lanzamiento**

---

### 📅 Desglose Detallado por Fases

#### Semana 1: Estrategia, Copy y Estructura
*El objetivo es tener el esqueleto (Wireframe) y el texto (Copy) listos antes de pasar a pixel-perfect.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| **Kick-off & Value Proposition** | Todos | Brief del Producto | Documento de acuerdo sobre el mensaje central. |
| **Investigación y Entrevistas** | Copywriter | N/A | Insights de dolor del cliente (Pain points). |
| **Wireframes (Low-Fi)** | Diseñador | Acuerdo de Valor | Esqueleto en blanco/negro de la página (Figma). |
| **Redacción de Copy (Borrador)** | Copywriter | Wireframes | Textos para Hero, Beneficios, Features, FAQ, CTA. |
| **Setup del Entorno** | Dev 1 | N/A | Repositorio creado, stack definido (Next.js, React, etc.), CI/CD inicial. |
| **Definición de Stack/Componentes** | Dev 2 | N/A | Elección de librería UI (Tailwind, MUI) y hosting (Vercel/AWS). |

#### Semana 2: Diseño UI y Maquetación Base
*Diseño crea la interfaz visual mientras desarrollo prepara la estructura del código.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| **Diseño Visual (High-Fi)** | Diseñador | Wireframes + Copy | Diseño final en Figma (Desktop y Mobile). |
| **Creación de Componentes Base** | Dev 1 & Dev 2 | Setup | Botones, Inputs, Navbar, Footer genéricos en código. |
| **Revisión y Ajuste de Copy** | Copywriter + Team | Diseño Visual | Copy final ajustado a los espacios de diseño. |
| **Preparación de Assets** | Diseñador | Diseño Visual | Exportación de iconos, ilustraciones, logos optimizados. |
| **Maquetación Estática (HTML/CSS)** | Dev 1 | Diseño Visual | Estructura visual sin lógica de negocio. |

#### Semana 3: Desarrollo y Funcionalidad
*Se arma el rompecabezas. Dev 2 se enfoca en la lógica del formulario y animaciones.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| **Maquetación Secciones Complejas** | Dev 1 | Assets + Diseño | Secciones de Features, Pricing, Testimonios. |
| **Lógica de Formularios (Leads)** | Dev 2 | Setup | Conexión con base de datos o CRM (HubSpot/Mailchimp). |
| **Implementación de Animaciones** | Dev 1 & Dev 2 | Diseño | Micro-interacciones, scroll effects (Framer Motion/GSAP). |
| **Responsive Design (Móvil/Tablet)** | Dev 1 & Dev 2 | Maquetación | Ajustes CSS para todos los dispositivos. |
| **Copy SEO (Metatags)** | Copywriter | N/A | Títulos, descripciones y Open Graph tags. |

#### Semana 4: QA, Optimización y Launch
*Pruebas de estrés, corrección de errores y salida a producción.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| **Integración Final** | Dev 1 & Dev 2 | Todo el código | Landing unificada en entorno de Staging (pre-producción). |
| **QA / Testing (Bugs)** | Todos | Staging | Lista de errores (visuales, ortográficos, funcionales). |
| **Optimización de Performance** | Dev 2 | Staging | Optimización de imágenes (WebP), minificación JS/CSS. |
| **Setup Analítica** | Dev 1 | N/A | Google Analytics 4, Google Tag Manager, Pixel (Meta/LinkedIn). |
| **Corrección de Última Hora** | Diseñador / Copy | QA | Ajustes finales de diseño o texto. |
| **🚀 GO LIVE** | Dev 1 | QA Aprobado | Página en producción y DNS configurado. |

---

### 💡 Estrategias Clave para el Éxito

1.  **Diseño "Content-First":**
    *   **Error común:** El diseñador hace cajas de texto vacías (Lorem Ipsum) y luego el copy no cabe.
    *   **Solución:** El Copywriter debe entregar los textos en la **Semana 1**. El Diseñador debe diseñar *alrededor* del texto real.

2.  **División de Developers (El "Slicing"):**
    *   **Dev 1 (Frontend):** Se enfoca en la estructura visual (HTML/CSS/React components).
    *   **Dev 2 (Backend/Lógica):** Se enfoca en dónde van los datos del formulario, la configuración del servidor y la velocidad de carga.
    *   *Nota:* Ambos deben usar la misma librería de estilos para no pisarse.

3.  **Herramientas Recomendadas:**
    *   **Gestión:** Trello, Jira o Linear (Tablero Kanban simple: To Do, Doing, Review, Done).
    *   **Diseño:** Figma (permite pasar estilos a código fácilmente).
    *   **Comunicación:** Slack o canal dedicado en Discord/Teams.

4.  **El rol del Copywriter en la Semana 4:**
    *   No lo dejes fuera. En la última semana debe leer la página *en vivo* (en el móvil y desktop) para cazar errores ortográficos o frases que se cortan visualmente.

### 🚩 Posibles Riesgos (y mitigación)

*   **Riesgo:** El Diseñador se retrasa y los Devs no tienen qué hacer.
    *   *Mitigación:* Los Devs empiezan haciendo el "Header", "Footer" y el sistema de diseño base, que son estándar y no cambian drásticamente.
*   **Riesgo:** Indecisión sobre el precio o el mensaje principal.
    *   *Mitigación:* El Lunes de la Semana 1 se debe firmar el "Valor Central". Si el miércoles de la semana 2 cambian el mensaje de venta, el timeline se rompe.

¿Necesitas que detalle alguna de las tareas técnicas o de copy específicamente?