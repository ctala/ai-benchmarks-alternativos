# Gemini 3.5 Flash Lite — task_management/project_breakdown

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 8.78 | quality: 10.0
- latency_total: 6.985s | tokens_per_second: 286.5
- input_tokens: 61 | output_tokens: 2001
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

¡Felicidades por el lanzamiento! 4 semanas es un tiempo ajustado pero **totalmente factible** para una landing page de SaaS, siempre y cuando se adopte un enfoque ágil y se evite la parálisis por análisis.

Aquí tienes el plan de proyecto detallado, optimizado para tu equipo (1 Diseñador, 2 Desarrolladores, 1 Copywriter, y asumiendo que tú o alguien más actúa como Product Owner/Gestor de Proyecto).

---

### **Estrategia General (El enfoque "MVP")**
Para cumplir con las 4 semanas, la landing no debe tener animaciones complejas ni 10 secciones. Debe centrarse en: **Propuesta de valor clara, dolor del cliente, cómo funciona, prueba social (o simulada/futura) y un fuerte CTA (Llamado a la acción) para lista de espera o registro.**

---

### **Desglose por Fases, Tareas y Responsables**

#### **FASE 1: Estrategia, Copy y Estructura (Semana 1)**
*Objetivo: Definir qué vamos a decir, a quién y cómo se va a estructurar la página.*

*   **T1.1: Definición de ICP (Perfil de Cliente Ideal) y Mensaje Clave.**
    *   *Descripción:* Acotar el dolor principal que resuelve el SaaS de inventario (ej: pérdida de stock, exceso de hojas de cálculo).
    *   *Responsable:* Todos (Liderado por PO/Copy).
    *   *Dependencias:* Ninguna.
*   **T1.2: Estructura de la Página (Wireframe en baja fidelidad / Esquema).**
    *   *Descripción:* Definir el orden de las secciones: Hero, Dolor, Solución, Beneficios, Social Proof, FAQ, Footer + CTA principal.
    *   *Responsable:* Diseñador + Copywriter.
    *   *Dependencias:* T1.1.
*   **T1.3: Redacción del Copy completo (Texto persuasivo).**
    *   *Descripción:* Titulares, subtítulos, beneficios, FAQs y textos de los botones (CTAs).
    *   *Responsable:* Copywriter.
    *   *Dependencias:* T1.2.
*   **T1.4: Definición de Stack Tecnológico y Herramientas.**
    *   *Descripción:* Elegir CMS/Framework (ej: Next.js, Webflow, o WordPress), pasarela de captura de leads (Typeform, ConvertKit, o DB propia) y analítica (Google Analytics/Plausible).
    *   *Responsable:* Developers.
    *   *Dependencias:* Ninguna.

#### **FASE 2: Diseño UI y Preparación Técnica (Semana 2)**
*Objetivo: Crear el diseño visual de alta fidelidad y preparar el entorno de desarrollo.*

*   **T2.1: Diseño UI (Interfaz de Usuario) en Figma.**
    *   *Descripción:* Diseño de la landing basada en el copy de la Fase 1. Versión Desktop y Mobile.
    *   *Responsable:* Diseñador.
    *   *Dependencias:* T1.3 (Copy aprobado).
*   **T2.2: Creación de Recursos Gráficos.**
    *   *Descripción:* Mockups del producto (pantallas del SaaS), iconos, ilustraciones o selección de imágenes de stock.
    *   *Responsable:* Diseñador.
    *   *Dependencias:* T2.1.
*   **T2.3: Configuración del Repositorio y Entorno.**
    *   *Descripción:* Setup del proyecto, conexión con dominio (subdominio o principal), herramientas de analítica y sistema de captura de emails.
    *   *Responsable:* Developers (Dev 1 y Dev 2).
    *   *Dependencias:* T1.4.
*   **T2.4: Aprobación de Diseño (Figma Review).**
    *   *Descripción:* Validación final del diseño por parte del equipo.
    *   *Responsable:* PO / Todo el equipo.
    *   *Dependencias:* T2.1 y T2.2.

#### **FASE 3: Desarrollo y QA / Pruebas (Semana 3)**
*Objetivo: Codificar la landing, integrarla con la base de datos/captura de leads y asegurar que funcione perfecto.*

*   **T3.1: Maquetación Front-end (HTML/CSS/JS o Framework).**
    *   *Descripción:* Convertir el diseño de Figma en código responsive. (Dev 1 toma Desktop, Dev 2 toma Mobile o se dividen por secciones).
    *   *Responsable:* Developer 1 y Developer 2.
    *   *Dependencias:* T2.4 (Diseño aprobado).
*   **T3.2: Integración de Formularios y Base de Datos (Backend/API).**
    *   *Descripción:* Asegurar que los registros de la lista de espera lleguen al CRM o herramienta de email marketing.
    *   *Responsable:* Developer 1.
    *   *Dependencias:* T3.1.
*   **T3.3: SEO On-Page y Optimización de Velocidad.**
    *   *Descripción:* Meta tags, Open Graph (para redes sociales), compresión de imágenes, velocidad de carga (Core Web Vitals).
    *   *Responsable:* Developer 2.
    *   *Dependencias:* T3.1.
*   **T3.4: Control de Calidad (QA) y Pruebas en Dispositivos.**
    *   *Descripción:* Probar en diferentes navegadores (Chrome, Safari, Firefox), móviles (iOS, Android) y verificar que los formularios funcionen.
    *   *Responsable:* Todo el equipo.
    *   *Dependencias:* T3.1, T3.2, T3.3.

#### **FASE 4: Pulido, Lanzamiento y Post-Lanzamiento (Semana 4)**
*Objetivo: Lanzar al mundo y medir los primeros resultados.*

*   **T4.1: Corrección de Bugs detectados en QA.**
    *   *Descripción:* Solucionar cualquier fallo visual o técnico reportado en la Fase 3.
    *   *Responsable:* Developers.
    *   *Dependencias:* T3.4.
*   **T4.2: Despliegue a Producción (Go Live).**
    *   *Descripción:* Apuntar el dominio oficial a la nueva landing page.
    *   *Responsable:* Developers.
    *   *Dependencias:* T4.1.
*   **T4.3: Campaña de Lanzamiento (Social Media, Email, Anuncios).**
    *   *Descripción:* Publicar en Product Hunt, LinkedIn, Twitter/X, enviar emails a waitlist previa (si la hay).
    *   *Responsable:* Copywriter + PO.
    *   *Dependencias:* T4.2 (Landing online).
*   **T4.4: Monitoreo de Conversión y Analítica.**
    *   *Descripción:* Revisar tasa de rebote, conversiones de formularios y errores 404 durante las primeras 48 horas.
    *   *Responsable:* Desarrollador principal / PO.
    *   *Dependencias:* T4.2.

---

### **Timeline Realista (Vista Gantt Simplificada)**

| Fase / Semana | Semana 1 | Semana 2 | Semana 3 | Semana 4 |
| :--- | :---: | :---: | :---: | :---: |
| **Fase 1: Estrategia y Copy** | **[████]** | | | |
| **Fase 2: Diseño UI & Setup** | | **[████]** | | |
| **Fase 3: Desarrollo y QA** | | | **[████]** | |
| **Fase 4: Lanzamiento** | | | | **[████]** |

---

### **Reglas de Oro para cumplir el plazo de 4 semanas:**

1.  **"Done is better than perfect" (Lo hecho es mejor que lo perfecto):** Si una sección o animación compleja está retrasando el desarrollo, **corte de tajo**. Es mejor una landing simple que funcione y convierta, que una perfecta que se lance tarde.
2.  **Congelación de Copy y Diseño (Fin de Semana 2):** Una vez que el diseño se aprueba al final de la Semana 2, **no se aceptan cambios de texto ni de estructura**. Los desarrolladores necesitan estabilidad para codificar rápido.
3.  **Daily Standups de 10 minutos:** Al ser un equipo pequeño (4-5 personas contando al gestor), una reunión diaria de 10 minutos por Slack o Zoom para responder: *¿Qué hice ayer? ¿Qué haré hoy? ¿Tengo bloqueos?* salvará el proyecto.