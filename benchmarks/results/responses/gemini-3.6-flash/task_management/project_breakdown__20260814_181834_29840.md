# Gemini 3.6 Flash — task_management/project_breakdown

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.1 | quality: 9.24
- latency_total: 13.099s | tokens_per_second: 156.0
- input_tokens: 62 | output_tokens: 2044
- judge_score: 4.6 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Este es un plan de proyecto estructurado para lanzar la landing page de tu SaaS de gestión de inventario en **4 semanas**, optimizando los recursos del equipo (1 Diseñador, 2 Developers, 1 Copywriter).

Para lograrlo a tiempo, utilizaremos un enfoque **ágil-secuencial**: el copy y diseño lideran las primeras 2 semanas, mientras que el desarrollo se concentra en las semanas 3 y 4.

---

### **Asignación de Roles y Responsabilidades**
*   **Copywriter (CW):** Estrategia de contenido, textos, propuesta de valor y SEO básico.
*   **Diseñador (UX/UI):** Wireframes, UI final, assets visuales (mockups del SaaS) y diseño responsive.
*   **Dev 1 (Lead Frontend):** Estructura del sitio, componentes UI, animaciones y maquetación responsive.
*   **Dev 2 (Tech/Ops & Integraciones):** Setup de entorno, formularios, conexión con CRM/Email, Analytics y SEO técnico.

---

### **Cronograma Fase por Fase (Timeline de 4 Semanas)**

#### **FASE 1: Estrategia, Wireframing y Setup (Semana 1)**
> **Objetivo:** Definir la estructura, la propuesta de valor y tener la base técnica lista.

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| **1.1 Briefing & Arquitectura:** Definir objetivo (ej. Registro a Waitlist o Agendar Demo). | Todos | Ninguna | Documento de estructura (Sitemap) |
| **1.2 Propuesta de Valor y Copy Inicial:** Redactar titulares, beneficios y secciones clave. | Copywriter | 1.1 | Borrador de Copy (Google Doc) |
| **1.3 Wireframes Low-Fi:** Crear esqueleto estructural de la página. | Diseñador | 1.1 | Wireframe en Figma |
| **1.4 Setup del Proyecto:** Selección del Stack (ej. Next.js, Tailwind / Webflow), repositorio y dominio. | Dev 2 | Ninguna | Repo inicial listo / Entorno Staging |

---

#### **FASE 2: Diseño UI y Copy Final (Semana 2)**
> **Objetivo:** Tener el diseño visual 100% aprobado y el copy pulido antes de tirar la primera línea de código visual.

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| **2.1 UI Design High-Fi (Desktop & Mobile):** Diseñar la interfaz final con sistema de diseño. | Diseñador | 1.2, 1.3 | UI en Figma (Desktop/Mobile) |
| **2.2 Asests y Mockups del SaaS:** Crear capturas/ilustraciones del software de inventario. | Diseñador | 2.1 | Assets exportados (SVG/WebP) |
| **2.3 Copywriting Definitivo & UX Writing:** Ajustar textos según el espacio real del diseño. | Copywriter | 1.2, 2.1 | Copy final aprobado |
| **2.4 Preparación de la base de datos/CRM:** Configurar Hubspot, Mailchimp o DB para captar leads. | Dev 2 | 1.4 | API Keys y endpoints listos |

---

#### **FASE 3: Desarrollo Frontend e Integraciones (Semana 3)**
> **Objetivo:** Maquetar la landing page y conectar la lógica de captación de usuarios.

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| **3.1 Maquetación Frontend (Hero, Features, Pricing):** Crear componentes visuales. | Dev 1 | 2.1, 2.2 | Interfaz construida en St