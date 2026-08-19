# Qwen 3.5 (Ollama Cloud default) — task_management/project_breakdown

- model_id: `qwen3.5:cloud`
- success: True  | final: 8.08 | quality: 9.24
- latency_total: 17.019s | tokens_per_second: 120.3
- input_tokens: 76 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

Este es un plan de proyecto detallado y realista para lanzar una Landing Page de alta conversión en 4 semanas. Dado que el equipo es pequeño pero equilibrado para este alcance (1 Diseño, 2 Devs, 1 Copy), la clave será el trabajo en paralelo y la aprobación rápida de entregables.

### 1. Roles y Responsabilidades

*   **Diseñador (UX/UI):** Wireframes, prototipos de alta fidelidad, assets gráficos, optimización de imágenes.
*   **Developers (2):**
    *   *Dev 1 (Frontend Lead):* Estructura HTML, CSS/Tailwind, responsividad, performance.
    *   *Dev 2 (Integraciones/Logic):* Formularios, CRM/Email marketing, Analytics, SEO técnico, Deploy.
*   **Copywriter:** Propuesta de valor, textos de la web, emails de confirmación, SEO on-page, legales básicos.
*   **Coordinación (Importante):** No hay Project Manager asignado. Se recomienda que el **Dev 1** o el **Copywriter** actúe como facilitador para desbloquear decisiones y gestionar el calendario.

---

### 2. Fases del Proyecto

#### Fase 1: Estrategia, Contenido y Estructura (Semana 1)
*Objetivo: Definir qué se vende, a quién y tener el esqueleto del contenido listo.*

| Tarea | Responsable | Dependencias | Entrega |
| :--- | :--- | :--- | :--- |
| Definición de Buyer Persona y USP (Propuesta Única) | Copy + Equipo | Ninguna | Doc de Estrategia |
| Estructura del sitio (Sitemap/Secciones) | Designer + Copy | Estrategia | Wireframe Low-Fi |
| Redacción de borradores (Headlines, Beneficios, CTA) | Copywriter | Estrategia | Doc de Copy V1 |
| Setup de repositorio y entorno de desarrollo | Devs | Ninguno | Repo Git + Staging |
| Selección de Stack (ej. Next.js, Webflow, WordPress) | Devs | Estrategia | Decisión Técnica |

#### Fase 2: Diseño Visual y Desarrollo Base (Semana 2)
*Objetivo: Tener el diseño final aprobado y la base del código lista.*

| Tarea | Responsable | Dependencias | Entrega |
| :--- | :--- | :--- | :--- |
| Diseño UI de Alta Fidelidad (Desktop & Mobile) | Designer | Wireframe + Copy V1 | Figma Final |
| Revisión y ajuste de Copy sobre el diseño | Copywriter | Diseño UI | Copy V2 (Final) |
| Maquetación de componentes base (Header, Hero, Footer) | Dev 1 | Diseño UI | Componentes React/HTML |
| Configuración de CMS o estructura de páginas | Dev 2 | Diseño UI | Estructura Base |
| Creación de assets (iconos, ilustraciones) | Designer | Diseño UI | Carpeta de Assets |

#### Fase 3: Desarrollo Funcional e Integraciones (Semana 3)
*Objetivo: La página funciona, captura leads y se ve bien en todos los dispositivos.*

| Tarea | Responsable | Dependencias | Entrega |
| :--- | :--- | :--- | :--- |
| Maquetación de secciones internas (Features, Pricing, etc.) | Dev 1 | Componentes Base | Página completa |
| Integración de Formular