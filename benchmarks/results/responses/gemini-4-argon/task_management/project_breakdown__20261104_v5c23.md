# Gemini 4 Argon — task_management/project_breakdown

- model_id: `google/gemini-4-argon`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 43.667s | tokens_per_second: 53.5
- input_tokens: 91 | output_tokens: 2334
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Lanzar una landing page para un SaaS en 4 semanas es un objetivo agresivo pero totalmente viable con el equipo que tienes. La clave del éxito aquí es **evitar los cuellos de botella**, haciendo que el copywriter y el diseñador trabajen en paralelo durante la primera semana, y dividiendo el trabajo de los desarrolladores en Frontend y Backend/Integraciones.

Aquí tienes el plan de proyecto desglosado.

---

### Definición de Roles
*   **Copywriter (CW):** Responsable de la estrategia de comunicación, textos persuasivos y SEO básico.
*   **Diseñador (UX/UI):** Responsable de la estructura (wireframes), diseño visual, activos gráficos (mockups del SaaS) y prototipado.
*   **Developer 1 (Dev Front):** Enfocado en maquetación (HTML/CSS/JS), animaciones y diseño responsivo.
*   **Developer 2 (Dev Back/Ops):** Enfocado en configuración de servidor, CMS (si aplica), integraciones (CRM, pasarela de pago/registro, analítica) y rendimiento.

---

### SEMANA 1: Estrategia, Copywriting y Estructura (Fase de Descubrimiento)
*El objetivo de esta semana es cerrar el contenido y el esqueleto de la página. El diseño no debe avanzar en alta fidelidad sin el copy.*

*   **Tarea 1.1: Kick-off y Definición de Propuesta de Valor (Día 1)**
    *   **Detalle:** Definir el cliente ideal (ICP), dolores que resuelve el SaaS de inventario, y el llamado a la acción principal (ej. "Prueba Gratis 14 días" vs "Agendar Demo").
    *   **Responsable:** Todo el equipo.
    *   **Dependencia:** Ninguna.
*   **Tarea 1.2: Arquitectura de la Información y Wireframes (Días 2-3)**
    *   **Detalle:** Crear el esqueleto en blanco y negro de la página (Hero, Beneficios, Cómo funciona, Precios, Testimonios, FAQ).
    *   **Responsable:** UX/UI + CW.
    *   **Dependencia:** Tarea 1.1.
*   **Tarea 1.3: Redacción del Copy (Borrador inicial) (Días 2-4)**
    *   **Detalle:** Escribir todos los textos basados en los wireframes. Enfocarse en beneficios de gestión de inventario (ej. "Evita quiebres de stock", "Sincronización en tiempo real").
    *   **Responsable:** CW.
    *   **Dependencia:** Tarea 1.2.
*   **Tarea 1.4: Configuración del Entorno Técnico (Días 3-5)**
    *   **Detalle:** Comprar dominio, configurar hosting, repositorio Git, entorno de pruebas (Staging) y elegir el stack tecnológico (ej. Next.js, Webflow, WordPress).
    *   **Responsable:** Dev 1 y Dev 2.
    *   **Dependencia:** Tarea 1.1.
*   **Tarea 1.5: Aprobación de Copy y Wireframes (Día 5)**
    *   **Responsable:** Stakeholders / Líder de proyecto.
    *   **Dependencia:** Tareas 1.2 y 1.3.

---

### SEMANA 2: Diseño UI y Preparación Técnica (Fase Creativa)
*El diseñador lleva todo el peso esta semana. Los developers preparan las integraciones.*

*   **Tarea 2.1: Diseño UI de Alta Fidelidad - Desktop y Mobile (Días 6-9)**
    *   **Detalle:** Aplicar paleta de colores, tipografías y estilo visual al wireframe aprobado.
    *   **Responsable:** UX/UI.
    *   **Dependencia:** Tarea 1.5 (Crítica: No diseñar sin el copy final).
*   **Tarea 2.2: Creación de "Product Shots" / Mockups (Días 7-9)**
    *   **Detalle:** Crear imágenes atractivas de la interfaz del SaaS (gráficos de stock, alertas de inventario) para mostrar el producto en acción.
    *   **Responsable:** UX/UI.
    *   **Dependencia:** Tarea 1.3.
*   **Tarea 2.3: Ajustes de Micro-copy y SEO (Días 6-8)**
    *   **Detalle:** Textos de botones, mensajes de error en formularios, Meta Títulos, Meta Descripciones y textos alternativos (Alt text).
    *   **Responsable:** CW.
    *   **Dependencia:** Tarea 1.5.
*   **Tarea 2.4: Desarrollo de Integraciones (Backend) (Días 6-10)**
    *   **Detalle:** Crear los endpoints o configurar webhooks para conectar los formularios de la landing con el CRM (ej. HubSpot) y el flujo de registro del SaaS.
    *   **Responsable:** Dev 2.
    *   **Dependencia:** Tarea 1.4.
*   **Tarea 2.5: Entrega de Diseño a Desarrollo (Handoff) (Día 10)**
    *   **Detalle:** Preparar el archivo de Figma con guías de estilo y activos exportables.
    *   **Responsable:** UX/UI a Dev 1.
    *   **Dependencia:** Tareas 2.1 y 2.2 aprobadas.

---

### SEMANA 3: Desarrollo e Integración (Fase de Construcción)
*Los desarrolladores toman el control total. El diseñador y el copywriter asisten y preparan materiales de lanzamiento.*

*   **Tarea 3.1: Maquetación Frontend (Desktop) (Días 11-13)**
    *   **Detalle:** Pasar el diseño de Figma a código. Estructura HTML, estilos CSS y animaciones básicas (ej. cómo se mueve el dashboard de inventario).
    *   **Responsable:** Dev 1.
    *   **Dependencia:** Tarea 2.5.
*   **Tarea 3.2: Adaptación Responsiva (Mobile/Tablet) (Días 14-15)**
    *   **Detalle:** Asegurar que la página se vea perfecta en móviles.
    *   **Responsable:** Dev 1.
    *   **Dependencia:** Tarea 3.1.
*   **Tarea 3.3: Conexión de Formularios y Tracking (Días 12-15)**
    *   **Detalle:** Conectar el Frontend con el trabajo de la Tarea 2.4. Instalar Google Analytics 4, Google Tag Manager, Píxel de Meta/LinkedIn y mapas de calor (Hotjar).
    *   **Responsable:** Dev 2.
    *   **Dependencia:** Tarea 3.1 (parcial).
*   **Tarea 3.4: Redacción de correos de seguimiento (Onboarding) (Días 11-14)**
    *   **Detalle:** Escribir el correo automático que recibe el usuario al registrarse en la landing page.
    *   **Responsable:** CW (Diseño por UX/UI si requiere plantilla HTML).
    *   **Dependencia:** Tarea 1.5.

---

### SEMANA 4: QA, Optimización y Lanzamiento (Fase de Despliegue)
*Semana crítica para pulir detalles, asegurar que la página vuele y lanzar.*

*   **Tarea 4.1: Control de Calidad (QA) Visual y de Contenido (Días 16-17)**
    *   **Detalle:** Revisar que el sitio en Staging sea idéntico al Figma (Design Review) y que no haya faltas de ortografía.
    *   **Responsable:** UX/UI y CW.
    *   **Dependencia:** Tareas 3.1 y 3.2.
*   **Tarea 4.2: Pruebas Funcionales y de Conversión (Días 16-17)**
    *   **Detalle:** Probar el registro en múltiples navegadores (Chrome, Safari, Firefox) y dispositivos (iOS, Android). Verificar que los leads lleguen al CRM y se disparen los eventos de Analytics.
    *   **Responsable:** Dev 2.
    *   **Dependencia:** Tarea 3.3.
*   **Tarea 4.3: Optimización de Rendimiento (WPO) y SEO Técnico (Día 18)**
    *   **Detalle:** Comprimir imágenes, minificar código, asegurar carga rápida (< 2 segundos), configurar Sitemap, robots.txt y etiquetas OpenGraph (cómo se ve el link al compartir en redes).
    *   **Responsable:** Dev 1 y Dev 2.
    *   **Dependencia:** Tareas 4.1 y 4.2.
*   **Tarea 4.4: Corrección de Bugs (Bug Fixing) (Día 18-19)**
    *   **Detalle:** Resolver todos los errores encontrados en QA.
    *   **Responsable:** Dev 1 y Dev 2.
    *   **Dependencia:** Tareas 4.1 y 4.2.
*   **Tarea 4.5: Lanzamiento (Go-Live) (Día 19 - Jueves)**
    *   **Detalle:** Pasar de Staging a Producción. Apuntar DNS finales. *Nota: Nunca lances un viernes, por si hay errores críticos.*
    *   **Responsable:** Dev 2.
    *   **Dependencia:** Todo lo anterior aprobado.
*   **Tarea 4.6: Monitoreo Post-Lanzamiento (Día 20 - Viernes)**
    *   **Detalle:** Revisar grabaciones de Hotjar, verificar que los primeros usuarios reales no tengan problemas al registrarse.
    *   **Responsable:** Todo el equipo.
    *   **Dependencia:** Tarea 4.5.

---

### Resumen de Ruta Crítica (Lo que NO se puede atrasar)
1. **Día 4:** El Copy debe estar listo. Si el copywriter se atrasa, el diseñador trabajará a ciegas (usando *Lorem Ipsum*), lo que causará retrabajo en la semana 2.
2. **Día 10:** El diseño debe estar aprobado. Si se atrasa, los developers tendrán menos de una semana para programar, sacrificando la calidad móvil o las pruebas.
3. **Día 15:** La página debe estar funcional en el entorno de pruebas (Staging) para dedicar la última semana exclusivamente a pruebas y correcciones.