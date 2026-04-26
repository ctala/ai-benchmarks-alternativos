# Gemini 3.1 Flash Lite — task_management/project_breakdown

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 7.75 | quality: 9.44
- latency_total: 5.102s | tokens_per_second: 216.0
- input_tokens: 62 | output_tokens: 1102
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para lanzar una landing page de alta conversión en 4 semanas con un equipo de 4 personas, la clave es trabajar en **paralelo** y bajo una metodología **Agile (sprints semanales)**.

Aquí tienes el desglose estratégico:

### Roles
*   **Diseñador (D):** UI/UX, activos visuales, prototipo.
*   **Developers (Dev1 & Dev2):** Frontend (React/Next.js o Webflow), integración de CRM/Analytics.
*   **Copywriter (C):** Estrategia de mensajes, microcopy, SEO, CTAs.

---

### Timeline y Fases

#### Semana 1: Estrategia y Estructura (Wireframes)
*   **Objetivo:** Definir qué vendemos y a quién.
*   **Tareas:**
    *   **C:** Definir propuesta de valor, buyer persona y estructura del contenido (h1, beneficios, pruebas sociales).
    *   **D:** Wireframes de baja fidelidad (layout) basados en el copy.
    *   **Devs:** Configuración del entorno (repo, dominio, herramientas de analytics/tracking).
*   **Dependencias:** El diseño no inicia sin el copy; el desarrollo no inicia sin el diseño.

#### Semana 2: Diseño de Alta Fidelidad y Setup Técnico
*   **Objetivo:** Tener el "look & feel" final.
*   **Tareas:**
    *   **D:** Diseño UI completo (Desktop y Mobile). Creación de componentes.
    *   **C:** Redacción final de todos los textos (incluyendo landing de agradecimiento).
    *   **Devs:** Setup del CMS o framework, preparación de componentes base.
*   **Dependencias:** Diseño aprobado por el equipo antes de pasar a código.

#### Semana 3: Desarrollo e Integración
*   **Objetivo:** Landing funcional.
*   **Tareas:**
    *   **Dev1:** Maquetación de la sección Hero y navegación.
    *   **Dev2:** Integración de formularios (HubSpot/Mailchimp) y analíticas (GA4/Hotjar).
    *   **D:** Entrega de assets (iconos, imágenes, ilustraciones).
    *   **C:** Revisión de copy en contexto (¿se ve bien en la web?).
*   **Dependencias:** El diseño debe estar congelado (no hacer cambios visuales aquí).

#### Semana 4: QA, Testing y Lanzamiento
*   **Objetivo:** Cero errores y optimización de conversión.
*   **Tareas:**
    *   **Todos:** QA intensivo (responsividad, velocidad de carga, formularios).
    *   **Devs:** Optimización SEO técnico y velocidad (Lighthouse).
    *   **C:** Revisión final de ortografía y tono.
    *   **D:** Ajustes finales de UI.
    *   **Lanzamiento:** Despliegue en producción.

---

### Matriz de Responsabilidades (RACI)

| Tarea | Responsable | Soporte |
| :--- | :--- | :--- |
| Estrategia/Copy | Copywriter | Todos (Feedback) |
| Wireframes/UI | Diseñador | Copywriter |
| Desarrollo Frontend | Devs | Diseñador |
| Integraciones (CRM/Mail) | Dev 2 | Copywriter |
| QA / Testing | Todos | - |

---

### Consejos para el éxito (El "Secret Sauce")

1.  **Regla del 80/20 en el Diseño:** No diseñen desde cero. Usen una librería de componentes (ej. Tailwind UI o Shadcn/UI) para que los desarrolladores solo tengan que ajustar estilos, no programar desde cero.
2.  **Copy primero:** El error más común es diseñar y luego intentar "meter el texto". El diseño debe servir al copy, no al revés.
3.  **Analytics desde el día 1:** Asegúrense de que el botón de "Registrarse" o "Demo" tenga tracking configurado (eventos en GA4). Si no saben quién hace clic, no pueden mejorar la landing.
4.  **Congelación de cambios:** Al final de la Semana 2, se "congelan" los cambios de diseño. Cualquier cambio posterior debe pasar por un comité de urgencia.
5.  **Herramienta recomendada:** Si el equipo de desarrollo quiere velocidad, usen **Next.js + Tailwind**. Si quieren velocidad de edición futura para el Copywriter, usen **Webflow** o un CMS sencillo (Sanity/Contentful).

### Checklist de lanzamiento (Día 4, semana 4):
*   [ ] Dominio conectado y SSL activo.
*   [ ] Formulario conectado al CRM (probar que llegan los leads).
*   [ ] Google Analytics / Pixel de Meta instalados.
*   [ ] Favicon y Open Graph tags (para que se vea bien al compartir en redes).
*   [ ] Velocidad de carga probada en móvil (Google PageSpeed).