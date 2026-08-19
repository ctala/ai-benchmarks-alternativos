# Gemini 3.5 Flash Lite — task_management/project_breakdown

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 8.58 | quality: 9.7
- latency_total: 7.051s | tokens_per_second: 278.3
- input_tokens: 62 | output_tokens: 1962
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

¡Excelente reto! Con un equipo de 4 personas (1 diseñador, 2 developers, 1 copywriter y tú asumiendo probablemente el rol de Product Manager/Lider), 4 semanas es un tiempo ajustado pero **totalmente viable** si se aplica una metodología ágil y se enfoca el MVP (Mínimo Producto Viable) estrictamente en la conversión.

Aquí tienes el plan de proyecto detallado para el lanzamiento de la landing page.

---

### Resumen de Roles
*   **PM (Tú):** Coordinación, QA, herramientas, analítica, estrategia.
*   **Copywriter (C):** Textos, estructura de mensajes, emails (si aplica).
*   **Diseñador (D):** UX/UI, activos visuales, mockups.
*   **Developers (Devs):** Maquetación, integración, rendimiento, despliegue.

---

### Fases del Proyecto

#### **Fase 1: Semana 1 - Estrategia, Copy y Estructura (Wireframing)**
*Objetivo: Definir la propuesta de valor y tener el contenido base.*

*   **T1.1: Definición de ICP (Ideal Customer Profile) y Propuesta de Valor**
    *   *Descripción:* ¿A quién le hablamos? ¿Qué dolor principal resuelve el SaaS?
    *   *Responsable:* PM + C
    *   *Dependencias:* Ninguna
*   **T1.2: Estructura de la Landing (Wireframe en baja)**
    *   *Descripción:* Definir secciones (Hero, Dolor, Solución, Beneficios, Social Proof/Testimonios, Pricing, FAQ, CTA final).
    *   *Responsable:* PM + D
    *   *Dependencias:* T1.1
*   **T1.3: Redacción de Copys (Primer borrador completo)**
    *   *Descripción:* Escribir titulares, llamadas a la acción (CTAs), beneficios y microcopy.
    *   *Responsable:* C
    *   *Dependencias:* T1.2
*   **T1.4: Configuración de Stack Tecnológico y Herramientas**
    *   *Descripción:* Definir CMS/Framework (Next.js, Webflow, WordPress), herramienta de Email Marketing (ConvertKit, Resend), Analítica (PostHog, Google Analytics) y Herramienta de Grabación de Sesiones (Hotjar/Clarity).
    *   *Responsable:* Devs + PM
    *   *Dependencias:* Ninguna

---

#### **Fase 2: Semana 2 - Diseño UI y Configuración Técnica**
*Objetivo: Tener el diseño visual aprobado y el entorno de desarrollo listo.*

*   **T2.1: Diseño UI en Alta Fidelidad (Desktop & Mobile)**
    *   *Descripción:* Aplicar branding, elegir paleta de colores, tipografías y diseñar la interfaz final.
    *   *Responsable:* D
    *   *Dependencias:* T1.3 (Copys aprobados)
*   **T2.2: Selección/Creación de Recursos Visuales**
    *   *Descripción:* Mockups del software de inventario, iconos, ilustraciones o screenshots reales del producto.
    *   *Responsable:* D (con apoyo de Devs para screenshots del SaaS)
    *   *Dependencias:* T2.1
*   **T2.3: Configuración del Repositorio y Boilerplate**
    *   *Descripción:* Setup del proyecto, conexión con dominio, certificados SSL y herramientas de despliegue (Vercel/Netlify).
    *   *Responsable:* Devs
    *   *Dependencias:* T1.4
*   **T2.4: Revisión y Aprobación de Diseño**
    *   *Descripción:* Validación final del diseño por parte de todo el equipo.
    *   *Responsable:* PM + Equipo
    *   *Dependencias:* T2.1, T2.2

---

#### **Fase 3: Semana 3 - Desarrollo y QA (Control de Calidad)**
*Objetivo: Codificar la landing, integrar formularios y conectar analítica.*

*   **T3.1: Maquetación Front-end (Desktop & Mobile - Responsive)**
    *   *Descripción:* Programar la landing page basada en el diseño de Figma.
    *   *Responsable:* Dev 1 & Dev 2
    *   *Dependencias:* T2.4
*   **T3.2: Integración de Formularios y Base de Datos/CRM**
    *   *Descripción:* Conectar el formulario de registro (Waitlist o acceso anticipado) para guardar leads y enviar email de confirmación automático.
    *   *Responsable:* Dev 1
    *   *Dependencias:* T3.1
*   **T3.3: Implementación de Tracking y Analítica**
    *   *Descripción:* Instalar píxeles de conversión, eventos de Google Analytics/PostHog (clicks en CTA, envío de formulario).
    *   *Responsable:* Dev 2 + PM
    *   *Dependencias:* T3.1
*   **T3.4: QA y Pruebas de Rendimiento (Lighthouse, velocidad, bugs)**
    *   *Descripción:* Testear en diferentes navegadores, móviles, velocidad de carga (Core Web Vitals) y ortografía.
    *   *Responsable:* PM + Devs + C
    *   *Dependencias:* T3.1, T3.2, T3.3

---

#### **Fase 4: Semana 4 - Lanzamiento, SEO y Post-Lanzamiento**
*Objetivo: Salir ao aire y medir resultados.*

*   **T4.1: Soft Launch / Pruebas en Producción**
    *   *Descripción:* Subir la web a una URL oculta (o dominio temporal) y hacer pruebas reales de registro.
    *   *Responsable:* Devs + PM
    *   *Dependencias:* T3.4
*   **T4.2: Preparación de Campañas de Lanzamiento (Redes, Email, Product Hunt)**
    *   *Descripción:* Redactar posts para LinkedIn, Twitter/X, emails para lista de espera y preparar assets para Product Hunt.
    *   *Responsable:* C + PM
    *   *Dependencias:* T1.1
*   **T4.3: Lanzamiento Oficial (Go Live!)**
    *   *Descripción:* Apuntar el dominio principal a producción, lanzar campañas y publicar en redes/Product Hunt.
    *   *Responsable:* Todo el equipo
    *   *Dependencias:* T4.1, T4.2
*   **T4.4: Monitoreo Post-Lanzamiento (Primeras 48h)**
    *   *Descripción:* Revisar que los formularios funcionen, mirar mapas de calor (Hotjar) y tasa de conversión.
    *   *Responsable:* PM + Devs
    *   *Dependencias:* T4.3

---

### Timeline Resuelto (Vista de 4 Semanas)

| Semana | Lunes - Miércoles | Jueves - Viernes |
| :--- | :--- | :--- |
| **Semana 1** | Definición ICP, Wireframes (T1.1, T1.2) | Redacción de Copys, Stack (T1.3, T1.4) |
| **Semana 2** | Diseño UI Alta Fidelidad (T2.1) | Recursos visuales, Setup Dev, Aprobación (T2.2, T2.3, T2.4) |
| **Semana 3** | Maquetación Front-end (T3.1) | Formularios, Tracking, QA y Velocidad (T3.2, T3.3, T3.4) |
| **Semana 4** | Soft Launch y Copy de campaña (T4.1, T4.2) | **¡LANZAMIENTO!** y Monitoreo (T4.3, T4.4) |

---

### Factores críticos de éxito (Riesgos a evitar)

1.  **Bloqueo de Copys:** El diseñador no puede avanzar sin los textos (Semana 1). El copywriter debe ser estricto con los tiempos.
2.  **Scope Creep (Cambios de última hora):** Para un SaaS de inventario hay mil features que mostrar, pero la landing **solo debe vender el beneficio principal y capturar el email**. No intentes explicar todo el software.
3.  **Imágenes del producto:** Como el SaaS es nuevo, conseguir mockups atractivos del inventario en la Semana 2 es vital. Si el producto aún no está listo visualmente, el diseñador debe crear ilustraciones o pantallas UI ficticias pero limpias.