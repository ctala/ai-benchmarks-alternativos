# Gemini 3.8 Flash — task_management/project_breakdown

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.14 | quality: 9.42
- latency_total: 24.037s | tokens_per_second: 126.3
- input_tokens: 61 | output_tokens: 3035
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Con un equipo de 4 personas (1 Diseñador, 2 Developers, 1 Copywriter) y un plazo de 4 semanas (20 días laborables), el objetivo es totalmente alcanzable si se trabaja en paralelo evitando cuellos de botella. 

Dado que tienes 2 desarrolladores para una landing page, el desarrollo puede ir muy rápido si se divide entre **Frontend/UI** e **Integraciones/Infraestructura**.

Aquí tienes el desglose completo del proyecto:

---

### Definición de Roles
* **[COPY]** Copywriter: Narrativa, textos persuasivos, microcopy y SEO on-page.
* **[DIS]** Diseñador UI/UX: Wireframes, diseño visual (Figma), sistema de diseño y assets.
* **[DEV 1]** Frontend Lead: Maquetación, animaciones, responsive design y rendimiento web.
* **[DEV 2]** Integrations & Tech: Configuración de repo/hosting, formularios, CRM/emailing, analítica y SEO técnico.

---

### Cronograma Fase por Fase (Timeline: 4 Semanas)

#### **SEMANA 1: Estrategia, Copywriting y Wireframes (Días 1 a 5)**
*El objetivo de esta semana es cerrar la estructura y los textos antes de pasar a la fase visual.*

* **Día 1:** Kickoff de alineación. Definición de propuesta de valor, buyer persona (ej. jefes de almacén, eCommerce) y objetivo de conversión (¿Prueba gratis, lista de espera o demo?). *(Todo el equipo)*
* **Día 1 - 3:** Arquitectura de información y redacción del primer borrador del copy (Hero, problemas/soluciones del inventario, features clave, pricing, FAQs). **[COPY]**
* **Día 2 - 3:** Setup técnico: Repositorio (GitHub), boilerplate (ej. Next.js/Tailwind o Astro), entorno de staging y dominio/DNS. **[DEV 2]**
* **Día 3 - 5:** Wireframes en baja fidelidad basados en el borrador de copy. **[DIS]** *(Dependencia: Estructura del Copy)*
* **Día 4 - 5:** Revisión de textos con stakeholders y versión final de copy. **[COPY]**

---

#### **SEMANA 2: Diseño UI y Preparación Frontend (Días 6 a 10)**
*El objetivo es aprobar el diseño visual completo y avanzar la base del código.*

* **Día 6 - 8:** Diseño de alta fidelidad (UI) en Figma para Desktop (Hero, módulos interactivos, tablas comparativas de inventario). **[DIS]** *(Dependencia: Wireframes aprobados y Copy final)*
* **Día 6 - 8:** Configuración de componentes base (botones, tipografías, colores) según los avances del diseñador. **[DEV 1]**
* **Día 7 - 9:** Configuración del backend/servicios: conexión del formulario con el CRM (HubSpot/Mailchimp/Notion), API de emails transaccionales (Resend/SendGrid). **[DEV 2]**
* **Día 8 - 10:** Adaptación del diseño a Mobile y Tablet + exportación de assets (iconos, mockups del software SaaS, ilustraciones). **[DIS]**
* **Día 9 - 10:** Creación de meta-descripciones, OpenGraph copy y microcopys (estados de error en formularios, mensajes de éxito). **[COPY]**

---

#### **SEMANA 3: Desarrollo en Paralelo e Integraciones (Días 11 a 15)**
*Semana más intensa de desarrollo. Diseñador y Copy quedan en soporte y revisión.*

* **Día 11 - 14:** Maquetación completa de la landing (Desktop + Mobile) en código píxel-perfect. **[DEV 1]** *(Dependencia: UI Figma finalizado)*
* **Día 11 - 13:** Integración del formulario de captación, validaciones en frontend/backend y lógica de negocio (ej. reCAPTCHA para evitar bots). **[DEV 2]**
* **Día 13 - 15:** Implementación de analítica y tracking: Google Analytics 4, Tag Manager, Hotjar/Clarity y píxeles de conversión. **[DEV 2]**
* **Día 14 - 15:** Micro-interacciones y animaciones suaves (aparición de elementos, sliders, hover states). **[DEV 1] + [DIS]**
* **Día 15:** Congelación de código funcional (Feature Freeze). Despliegue en entorno de Staging. **[DEV 1 y 2]**

---

#### **SEMANA 4: Testing, Optimización y Lanzamiento (Días 16 a 20)**
*Cero desarrollos nuevos. Enfoque total en calidad, conversión y velocidad.*

* **Día 16 - 17: QA Funcional y Visual:**
  * Cross-browser y cross-device testing (Chrome, Safari, iOS, Android). **[DEV 1]**
  * Revisión de textos y ortografía en entorno real. **[COPY]**
  * Design QA (espaciados, tamaños de fuente, fidelidad). **[DIS]**
  * Test de extremo a extremo: enviar formulario -> verificar que llega al CRM -> verificar email de confirmación. **[DEV 2]**
* **Día 18: Optimización y Performance:**
  * Optimización de imágenes (WebP/AVIF), Core Web Vitals, accesibilidad y velocidad (PageSpeed 90+). **[DEV 1]**
  * Verificación de SEO técnico (sitemap, robots.txt, canonicals, schema markup de SoftwareApplication). **[DEV 2]**
* **Día 19: Pre-lanzamiento (Soft Launch):**
  * Apuntar dominio definitivo, verificación de certificados SSL.
  * Pruebas en el entorno de producción cerrado o bajo contraseña. *(Todo el equipo)*
* **Día 20: DÍA DE LANZAMIENTO (Hard Launch):**
  * Abrir la página al público.
  * Monitoreo en tiempo real de analítica, errores en consola (Sentry/LogRocket) y formularios entrantes. **[DEV 1 y 2]**

---

### Resumen de Dependencias Críticas (El "Camino Crítico")

```text
[Copy Final] ──► [Wireframes / UI Design] ──► [Maquetación Frontend (DEV 1)] ──► [QA] ──► [Lanzamiento]
                                         └─► [Integración Backend (DEV 2)] ──┘
```

1. **El Copy no puede retrasarse más allá del Día 4:** Si el diseñador usa *Lorem Ipsum*, habrá que rediseñar cajas y espacios la semana 2.
2. **El UI no puede pasar del Día 10:** Los desarrolladores necesitan mínimo 5-6 días completos para maquetar responsive y pulir detalles.

### Consejos Clave para este Proyecto
* **El rol de DEV 2:** Dado que 2 devs para una sola landing page puede generar conflictos de git, **DEV 1** debe ser el dueño del layout visual y CSS, mientras que **DEV 2** debe adueñarse de la infraestructura, lógica de APIs, analítica, accesibilidad y rendimiento.
* **Mockups del SaaS:** Para la Semana 2, el Diseñador necesitará capturas o pantallas prototipo del software de inventario para colocarlas dentro de "marcos de navegador" atractivos en la landing. Asegúrate de tener este material listo.