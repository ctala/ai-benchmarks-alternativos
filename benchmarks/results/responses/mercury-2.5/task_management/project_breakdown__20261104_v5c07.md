# Mercury 2.5 — task_management/project_breakdown

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 4.559s | tokens_per_second: 297.4
- input_tokens: 63 | output_tokens: 1356
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Aquí tienes un desglose realista para el lanzamiento de la landing page en 4 semanas, optimizado para un equipo de 5 personas (1 diseñador, 2 devs, 1 copywriter, + tú como PM/Lead implícito).

### **Fase 1: Definición y Estrategia (Semana 1 - Días 1-2)**
*Objetivo: Tener claros los mensajes y la estructura antes de diseñar o programar.*

| Tarea | Descripción | Responsable | Dependencias |
| :--- | :--- | :--- | :--- |
| **Definir User Persona y Propuesta de Valor** | Clarificar qué problema de inventario resuelve y para quién. | Product/Lead | Ninguna |
| **Definir "Cualidad de Salida" (CTA)** | ¿Quedamos demo, registro free o newsletter? | Product/Lead | -
| **Briefing Creativo** | Documento con tone of voice, referencias visuales y requisitos técnicos. | PM/Lead | - |

### **Fase 2: Copywriting y Wireframes (Semana 1 - Días 3-5)**
*Objetivo: Tene el contenido escrito y el esqueleto de la página.*

| Tarea | Descripción | Responsable | Dependencias |
| :--- | :--- | :--- | :--- |
| **Redacción de Copy (Esquema)** | Titulares, subtítulos, bullets de beneficios, CTA. | Copywriter | Briefing |
| **Creación de Wireframes** | Estructura visual en baja fidelidad (Figma/Whimsical). | Diseñador | Copy Esquema |
| **Revisión de Copy y Wireframes** | Asegurar que el diseño comunica lo que dice el texto. | Equipo completo | Copy + Wireframes |

### **Fase 3: Diseño UI y Desarrollo (Semana 2 y 3)**
*Objetivo: Diseño visual de alta fidelidad y construcción del sitio.*

#### **Semana 2: Diseño UI y Configuración Técnica**
| Tarea | Descripción | Responsable | Dependencias |
| :--- | :--- | :--- | :--- |
| **Diseño de Alta Fidelidad** | Diseño final (mobile-first) con paleta de colores y tipografía. | Diseñador | Wireframes |
| **Setup de Repositorio/Entorno** | Configuración de hosting, dominio, analytics y CRM. | Dev 1 | - |
| **Componentes Base** | Crear sistema de componentes en código (botones, inputs, navbar). | Dev 1 | Diseño UI |

#### **Semana 3: Implementación y Funcionalidad**
| Tarea | Descripción | Responsable | Dependencias |
| :--- | :--- | :--- | :--- |
| **Implementación de Secciones** | Montar Hero, Features, Social Proof, Pricing (si aplica). | Dev 1 & 2 | Componentes Base |
| **Formulario y Backend** | Conectar formulario a herramienta de email (Mailchimp, HubSpot). | Dev 2 | Setup técnico |
| **Integraciones** | Pixel de LinkedIn/FB, Google Analytics. | Dev 1 | Setup técnico |
| **Diseño de Estado Vacío/Sucesos** | Mensajes de "Gracias por registrarte". | Diseñador & Dev | - |

### **Fase 4: QA, Contenido y Lanzamiento (Semana 4)**
*Objetivo: Asegurar calidad, contenido real y publicar.*

| Tarea | Descripción | Responsable | Dependencias |
| :--- | :--- | :--- | :--- |
| **Generación de Assets** | Capturas del software (UI), iconos personalizados, ilustraciones. | Diseñador | - |
| **QA (Control de Calidad)** | Revisión en móviles, tablets, browsers, carga, enlaces rotos. | Dev 1 & 2 | Sitio en staging |
| **Copy Final y SEO** | Meta tags, alt text en imágenes, revisión final de textos en vivo. | Copywriter | QA |
| **Lanzamiento (Go Live)** | Despliegue a producción y anuncio en canales internos/externos. | PM/Dev | QA Aprobado |

---

### **Cronograma Visual (Timeline)**

| Semana | Lunes | Martes | Miércoles | Jueves | Viernes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sem 1** | Estrategia/Brief | Copy Draft 1 | Wireframes | Copy Final + Aprobación | Kickoff Dev |
| **Sem 2** | Diseño UI | Diseño UI | Setup Técnico + Componentes | Desarrollo Hero/Nav | Desarrollo Features |
| **Sem 3** | Desarrollo Pricing/Footer | Formulario/Integraciones | Assets Gráficos | Integración Assets | QA Interno |
| **Sem 4** | Correcciones QA | SEO/Optimización | Copy en vivo | Go Live | Post-Launch |

---

### **Riesgos y Mitigaciones**

1.  **Bloqueo de Diseño:** Si el diseño UI tarda más de 3 días, el dev pierde tiempo.
    *   *Mitigación:* Usar una librería de componentes existente (Tailwind UI, Shadcn) y solo personalizar lo esencial.
2.  **Assets de Producto:** Si el producto aún no tiene capturas de pantalla de alta calidad.
    *   *Mitigación:* Usar placeholders genéricos y animaciones abstractas mientras el Diseñador genera los assets finales en la Semana 3.
3.  **Dependencias de Copy:** Si el copy no llega el Jueves de la Semana 1.
    *   *Mitigación:* El Copywriter debe entregar un borrador completo al inicio de la Semana 2 para que el Diseñador trabaje con textos reales, no Lorem Ipsum.

### **Recomendación de Herramientas**
*   **Diseño:** Figma (para diseñar y prototipar).
*   **Gestión:** Linear, Asana o Trello (para tareas y sprints).
*   **Desarrollo:** Next.js o Astro (para velocidad y SEO) + Tailwind CSS.
*   **Hosting:** Vercel o Netlify (despliegue rápido).