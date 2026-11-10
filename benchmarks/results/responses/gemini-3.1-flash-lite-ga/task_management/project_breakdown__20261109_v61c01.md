# Gemini 3.1 Flash Lite (GA) — task_management/project_breakdown

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 9.16 | quality: 10.0
- latency_total: 4.303s | tokens_per_second: 249.2
- input_tokens: 61 | output_tokens: 1072
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Para lanzar una landing page de alta conversión en 4 semanas con un equipo pequeño, la clave es el **enfoque iterativo**. No busques la perfección, busca la validación.

Aquí tienes el desglose del proyecto:

### Estructura del Equipo
*   **Diseñador (D):** UI/UX, activos gráficos, prototipado.
*   **Developers (Dev 1 y 2):** Implementación, integración de CRM/Analytics, despliegue.
*   **Copywriter (C):** Mensajería, estructura de ventas, SEO.

---

### Timeline de 4 Semanas

| Fase | Semana | Foco Principal |
| :--- | :--- | :--- |
| **1: Estrategia y Copy** | 1 | Definición de propuesta de valor y wireframes. |
| **2: Diseño y Setup** | 2 | UI final y configuración de entorno de desarrollo. |
| **3: Desarrollo** | 3 | Codificación y carga de contenido. |
| **4: QA y Lanzamiento** | 4 | Pruebas, SEO, analíticas y Go-Live. |

---

### Desglose de Tareas y Dependencias

#### Semana 1: Estrategia y Estructura
*   **Tareas:**
    *   **C:** Definir *User Persona*, dolores (pain points) y propuesta de valor única.
    *   **C:** Escribir el copy completo (Hero, beneficios, caso de uso, FAQ, CTA).
    *   **D:** Crear wireframes (baja fidelidad) basados en el copy.
*   **Dependencias:** El diseño depende del copy.
*   **Responsables:** C (Líder), D (Apoyo).

#### Semana 2: Diseño y Setup Técnico
*   **Tareas:**
    *   **D:** Diseño de alta fidelidad (UI) en Figma (Mobile y Desktop).
    *   **Dev 1:** Configuración del stack (ej. Next.js, Webflow o Framer) y hosting.
    *   **Dev 2:** Configuración de herramientas de terceros (CRM como HubSpot/Mailchimp, Google Analytics 4, Hotjar).
*   **Dependencias:** El desarrollo técnico puede empezar en paralelo al diseño UI.
*   **Responsables:** D (UI), Dev 1 (Infra), Dev 2 (Integraciones).

#### Semana 3: Desarrollo e Implementación
*   **Tareas:**
    *   **Dev 1 & 2:** Montaje de la página (Frontend).
    *   **C:** Revisión del copy dentro del diseño real (ajustes de longitud).
    *   **D:** Exportación de assets (iconos, imágenes, ilustraciones).
*   **Dependencias:** El frontend depende del diseño aprobado.
*   **Responsables:** Dev 1 & 2 (Frontend), C (Revisión).

#### Semana 4: QA, Ajustes y Lanzamiento
*   **Tareas:**
    *   **Equipo completo:** QA (Pruebas en navegadores, dispositivos móviles, test de formularios).
    *   **Dev 1:** Optimización de velocidad (Core Web Vitals) y SEO técnico (meta tags, sitemap).
    *   **Dev 2:** Configuración de dominio, SSL y puesta en producción.
    *   **C:** Redacción de email de lanzamiento y post de redes sociales.
*   **Responsables:** Todos.

---

### Recomendaciones Estratégicas para el éxito

1.  **Herramientas recomendadas:**
    *   Si necesitan velocidad de cambios futuros: **Framer o Webflow**.
    *   Si necesitan escalabilidad extrema: **Next.js + Tailwind CSS**.
    *   Gestión de tareas: **Trello o Notion** (usa un tablero Kanban).
2.  **La Regla del "Mobile First":** El 70-80% de tu tráfico probablemente vendrá de móviles. Diseñen primero para móvil.
3.  **No busques el "Feature Creep":** En 4 semanas, la landing debe enfocarse en **una sola acción**: capturar un lead (correo electrónico) o una demo. No intentes explicar cada detalle del software.
4.  **Tracking es vital:** Asegúrate de que el día 1 del lanzamiento tengas configurado el seguimiento de conversiones. Si no mides quién hace clic en el CTA, no sabrás qué ajustar en la semana 5.

### Riesgos a mitigar:
*   **Bloqueo de Copy:** Si el copywriter se retrasa, el diseño no avanza. Establezcan una fecha límite estricta para la versión final del texto.
*   **Scope Creep:** Los developers suelen querer añadir animaciones complejas. Limiten las animaciones a algo básico para no retrasar el lanzamiento. **Lanzar a tiempo es mejor que lanzar perfecto.**