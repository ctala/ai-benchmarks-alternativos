# GLM 5.2 — task_management/project_breakdown

- model_id: `z-ai/glm-5.2`
- success: True  | final: 7.76 | quality: 9.44
- latency_total: 117.597s | tokens_per_second: 24.6
- input_tokens: 80 | output_tokens: 2892
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para lanzar una landing page de calidad en 4 semanas con un equipo de 4 personas (1 Diseñador, 2 Developers y 1 Copywriter), el éxito radica en **trabajo en paralelo** y **alcance controlado** (MVP de la landing). 

Aquí tienes el desglose del proyecto estructurado en fases, tareas, dependencias, responsables y un timeline realista.

### 👥 Definición de Roles
*   **Diseñador (D):** UX/UI, wireframes, diseño final, assets.
*   **Copywriter (C):** Mensaje de valor, headlines, textos de secciones, microcopy.
*   **Developer 1 (Dev1 - Lead/Front):** Estructura principal, Hero, animaciones, integración de formularios/CRM.
*   **Developer 2 (Dev2 - Front/Layout):** Secciones estáticas (Features, Pricing, FAQ, Footer), responsive design, SEO técnico básico.

---

### 📅 TIMELINE (4 Semanas)

#### SEMANA 1: Descubrimiento, Planeación y Wireframes
El objetivo de esta semana es alinear la visión, definir las secciones de la landing y tener una estructura visual básica (wireframes) y el mensaje central listo.

*   **Tarea 1.1: Kick-off y Definición de Alcance**
    *   *Responsables:* Todo el equipo.
    *   *Dependencias:* Ninguna.
    *   *Duración:* Día 1.
*   **Tarea 1.2: Wireframes (Baja fidelidad)**
    *   *Responsables:* Diseñador.
    *   *Dependencias:* Tarea 1.1.
    *   *Duración:* Días 2-3.
*   **Tarea 1.3: Copywriting Core (Hero, Value Proposition, CTA)**
    *   *Responsables:* Copywriter.
    *   *Dependencias:* Tarea 1.1 (entrevista con fundadores/producto).
    *   *Duración:* Días 2-4.
*   **Tarea 1.4: Setup Técnico y Entorno**
    *   *Responsables:* Dev1 y Dev2.
    *   *Dependencias:* Tarea 1.1.
    *   *Duración:* Días 2-3. (Repo, hosting, dominio, framework, integración de analítica básica).

#### SEMANA 2: Diseño UI y Desarrollo Inicial
El objetivo es tener el diseño final de alta fidelidad (Desktop y Mobile) y que los developers empiecen a montar la estructura base con el contenido preliminar.

*   **Tarea 2.1: Diseño UI Final (Desktop & Mobile)**
    *   *Responsables:* Diseñador.
    *   *Dependencias:* Wireframes (Tarea 1.2) + Copy Core (Tarea 1.3).
    *   *Duración:* Días 5-7.
*   **Tarea 2.2: Copywriting de Secciones Secundarias (Features, Pricing, Testimonios, FAQ)**
    *   *Responsables:* Copywriter.
    *   *Dependencias:* Wireframes (Tarea 1.2).
    *   *Duración:* Días 5-8.
*   **Tarea 2.3: Desarrollo de Componentes Base y Header/Hero**
    *   *Responsables:* Dev1.
    *   *Dependencias:* Diseño UI Final (Tarea 2.1).
    *   *Duración:* Días 8-10.
*   **Tarea 2.4: Desarrollo de Layout y Secciones de Contenido**
    *   *Responsables:* Dev2.
    *   *Dependencias:* Diseño UI Final (Tarea 2.1) + Copy Secundario (Tarea 2.2).
    *   *Duración:* Días 9-10.

#### SEMANA 3: Desarrollo Completo e Integraciones
El objetivo es tener la landing page totalmente funcional (estados de hover, formularios, responsive) y lista para pruebas.

*   **Tarea 3.1: Integración de Formularios y CRM/Email**
    *   *Responsables:* Dev1.
    *   *Dependencias:* Tarea 2.3.
    *   *Duración:* Días 11-12.
*   **Tarea 3.2: Pulido de Animaciones e Interacciones (Micro-interacciones)**
    *   *Responsables:* Dev1.
    *   *Dependencias:* Tarea 2.3.
    *   *Duración:* Días 13-14.
*   **Tarea 3.3: Responsive Design (Mobile, Tablet)**
    *   *Responsables:* Dev2.
    *   *Dependencias:* Tarea 2.4.
    *   *Duración:* Días 11-14.
*   **Tarea 3.4: Exportación de Assets y QA Visual de Diseño**
    *   *Responsables:* Diseñador.
    *   *Dependencias:* Build preliminar de los Devs.
    *   *Duración:* Día 14.
*   **Tarea 3.5: Revisión de Copy Implementado**
    *   *Responsables:* Copywriter.
    *   *Dependencias:* Build preliminar de los Devs.
    *   *Duración:* Día 14.

#### SEMANA 4: QA, Optimización y Lanzamiento
El objetivo es cazar bugs, optimizar rendimiento y hacer el deploy a producción.

*   **Tarea 4.1: Cross-Browser Testing y Bug Fixing**
    *   *Responsables:* Dev1 y Dev2.
    *   *Dependencias:* Fin de Semana 3.
    *   *Duración:* Días 15-16.
*   **Tarea 4.2: Optimización de Performance y SEO Técnico**
    *   *Responsables:* Dev2 (compresión de imágenes, lazy load, meta tags, schema).
    *   *Dependencias:* Tarea 4.1.
    *   *Duración:* Día 17.
*   **Tarea 4.3: QA Final (UAT - User Acceptance Testing)**
    *   *Responsables:* Todo el equipo (revisión final cruzada).
    *   *Dependencias:* Tarea 4.2.
    *   *Duración:* Día 18.
*   **Tarea 4.4: Deploy a Producción**
    *   *Responsables:* Dev1.
    *   *Dependencias:* Aprobación de QA (Tarea 4.3).
    *   *Duración:* Día 19.
*   **Tarea 4.5: Smoke Test Post-Deploy y Monitoreo**
    *   *Responsables:* Dev2 + Diseñador.
    *   *Dependencias:* Tarea 4.4.
    *   *Duración:* Día 20. (Verificar que todo se ve bien en el dominio real, que los formularios lleguen al CRM).

---

### 🚦 Dependencias Críticas (Cuellos de botella a evitar)
1.  **El Copy no puede bloquear el Diseño:** En la Semana 1, el Copywriter y el Diseñador deben trabajar en paralelo. El Copywriter entrega el "Copy Core" (Hero) para que el Diseñador calcule el espacio tipográfico en los wireframes.
2.  **El Diseño no puede bloquear a los Devs por completo:** En la Semana 2, el Diseñador debe entregar el diseño de la parte superior (Header + Hero) el día 7, para que Dev1 empiece a codear inmediatamente, mientras el Diseñador termina las partes inferiores (Features, Pricing).
3.  **Assets:** El Diseñador debe entregar todas las imágenes y iconos optimizados (SVG o WebP) al final de la semana 2, no durante la semana 3.

### 💡 Recomendaciones para el equipo
*   **Herramientas:** Usen Figma (con modo Dev/Inspect) para diseño, Notion/Asana para gestión de tareas y Slack para comunicación diaria.
*   **Reuniones:** Hagan un *Daily Stand-up* de 15 minutos cada mañana para sincronizar bloqueos.
*   **Alcance (Scope):** Si se atrasan, recorten animaciones complejas o secciones de "Pricing" detallado, y usen un simple formulario de "Únete a la lista de espera" o "Agenda una demo". El objetivo es captar leads, no tener la web perfecta.