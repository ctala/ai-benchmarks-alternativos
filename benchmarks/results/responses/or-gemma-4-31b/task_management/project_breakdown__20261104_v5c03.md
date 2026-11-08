# Gemma 4 31B — task_management/project_breakdown

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.05 | quality: 10.0
- latency_total: 18.326s | tokens_per_second: 62.8
- input_tokens: 74 | output_tokens: 1151
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en el desglose del proyecto, ofreciendo un plan detallado y utilizable para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Para lanzar una landing page en 4 semanas con un equipo de 4 personas, la clave es el **desarrollo paralelo**. No podemos esperar a que el copy esté terminado para que el diseñador empiece, ni que el diseño esté cerrado para que los devs monten la estructura.

Aquí tienes el plan maestro.

### 🛠️ Matriz de Responsabilidades (RACI)
*   **Copywriter (CW):** Mensajes, propuesta de valor, CTAs, SEO on-page.
*   **Diseñador (UI/UX):** Wireframes, prototipo high-fidelity, assets visuales.
*   **Developers (Dev 1 y Dev 2):** Setup técnico, maquetación, integraciones, despliegue.

---

### 📅 Timeline y Desglose de Fases

#### Semana 1: Definición y Estructura (El "Blueprint")
*El objetivo es definir QUÉ vamos a decir y CÓMO se organizará la información.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| Definición de Buyer Persona y Propuesta de Valor | CW | - | Documento de Estrategia |
| Mapa del sitio y Wireframe de baja fidelidad (UX) | UI/UX | Estrategia CW | Esquema de bloques (Lo-Fi) |
| Setup de repositorio, hosting y entorno de staging | Dev 1 | - | Entorno listo |
| Redacción de Copy Final (Hero, Beneficios, FAQ, Footer) | CW | Wireframe Lo-Fi | Documento de Copy |

#### Semana 2: Diseño Visual y Maquetación Base
*El objetivo es convertir el esquema en una experiencia visual y empezar a codificar la estructura.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| Diseño de UI High-Fidelity (Mockups) | UI/UX | Copy Final | Figma/Adobe XD |
| Creación de assets (iconos, capturas de pantalla del SaaS) | UI/UX | Diseño UI | Exportables (.svg, .png) |
| Maquetación de la estructura HTML/CSS (Shell) | Dev 1 | Wireframe Lo-Fi | Estructura base |
| Configuración de formularios y base de datos de leads | Dev 2 | - | Endpoint de captura |

#### Semana 3: Desarrollo Full y Conectividad
*El objetivo es ensamblar el diseño final con la funcionalidad.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| Implementación de diseño final y estilos (CSS/Tailwind) | Dev 1 | Diseño UI | Landing visualmente fiel |
| Integración de Copy final en el código | Dev 2 | Copy Final | Página con contenido real |
| Integración de herramientas de marketing (GA4, Pixel, Hotjar) | Dev 2 | Setup Hosting | Tracking activo |
| Revisión de UX y ajustes de diseño sobre el código | UI/UX | Maquetación | Feedback de ajustes |

#### Semana 4: QA, Optimización y Lanzamiento
*El objetivo es asegurar que nada se rompa y que la conversión sea máxima.*

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| Testing Responsivo (Mobile, Tablet, Desktop) | Dev 1 & 2 | Desarrollo | Reporte de bugs |
| Optimización de velocidad de carga (LCP, Core Web Vitals) | Dev 1 | Desarrollo | Página rápida (<2s) |
| Prueba de flujo de conversión (Lead $\rightarrow$ Email de confirmación) | CW & Dev 2 | Formulario | Flujo validado |
| **LANZAMIENTO (Push to Production)** | Equipo | Todo lo anterior | **URL Pública** |

---

### ⚠️ Dependencias Críticas (Riesgos)

1.  **El "Cuello de Botella" del Copy:** El diseñador no puede hacer el diseño final sin saber cuánto texto hay. El Copywriter debe entregar los bloques clave en la Semana 1.
2.  **Aprobaciones:** Para evitar retrabajos en la Semana 3, el diseño de la Semana 2 debe ser aprobado y "congelado" (no más cambios estéticos).
3.  **Assets del Producto:** Si el SaaS aún no tiene capturas de pantalla reales, el Diseñador debe crear *mockups* conceptuales para no detener el desarrollo.

### 🚀 Recomendaciones para el equipo:

*   **Devs:** Usen un framework moderno (Next.js, Astro o Tailwind) para acelerar el despliegue y asegurar que sea SEO-friendly.
*   **Diseñador:** Trabaja con un sistema de componentes en Figma para que los Devs puedan extraer colores y espaciados rápidamente.
*   **Copywriter:** Enfócate en el "dolor" del cliente (ej: *"Deja de perder dinero por errores de inventario"*) más que en las características técnicas.
*   **Reuniones:** Hagan un *Daily Stand-up* de 15 minutos cada mañana para desbloquear tareas inmediatamente.