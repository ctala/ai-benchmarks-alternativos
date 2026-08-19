# Gemini 3.7 Flash — task_management/project_breakdown

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.43 | quality: 9.52
- latency_total: 15.667s | tokens_per_second: 130.5
- input_tokens: 61 | output_tokens: 2044
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Aquí tienes un plan de trabajo detallado y realista para lanzar la landing page de tu SaaS de gestión de inventario en **4 semanas**.

---

### **Resumen del Equipo y Roles**
*   **Copywriter (CW):** Mensajes clave, propuesta de valor, textos de conversión y SEO on-page.
*   **Diseñador UI/UX (UI):** Wireframes, diseño visual, assets gráficos, prototipo y responsive design.
*   **Developer 1 (Dev 1 - Frontend Lead):** Maquetación, animaciones, responsive design y rendimiento (Core Web Vitals).
*   **Developer 2 (Dev 2 - Integraciones/Back/Tracking):** Formulario/Lead capture, integración con CRM/Email marketing, analytics, SEO técnico y despliegue/DNS.

---

### **Timeline Semana a Semana**

```
Semana 1: Estrategia, Copywriting y Wireframes
Semana 2: Diseño UI Final y Setup Técnico
Semana 3: Desarrollo Frontend e Integraciones
Semana 4: QA, Analítica, Optimización y Lanzamiento
```

---

### **Desglose de Fases y Tareas**

#### **SEMANA 1: Estrategia, Estructura y Contenido Base**
*Objetivo: Tener la estructura validada y el 80% del copy aprobado.*

| Tarea | Responsable | Dependencia |
| :--- | :--- | :--- |
| **Briefing & Propuesta de Valor:** Definir público objetivo (B2B/e-commerce), dolores principales y diferenciador del SaaS. | Todo el equipo | - |
| **Estructura/Arquitectura de la Landing:** Definir secciones (Hero, Problema, Solución/Features, Demo/Capturas, Precios/Waitlist, FAQ). | CW + UI | Briefing |
| **Copywriting v1:** Redacción de titulares, CTAs, beneficios y FAQs. | CW | Arquitectura |
| **Wireframes (Low-Fidelity):** Estructura visual básica en escala de grises (Desktop + Mobile). | UI | Arquitectura |
| **Definición de Stack Técnico:** Elección de tecnologías (ej. Next.js/Astro + Tailwind) y servicios (HubSpot, Mailchimp, Supabase, etc.). | Dev 1 + Dev 2 | - |

---

#### **SEMANA 2: Diseño UI de Alta Fidelidad y Setup Técnico**
*Objetivo: Diseños aprobados y entorno de desarrollo listo para codificar.*

| Tarea | Responsable | Dependencia |
| :--- | :--- | :--- |
| **Diseño UI (High-Fidelity):** Look & feel final, UI kit/componentes, mockups del software de inventario. | UI | Wireframes + Copy v1 |
| **Copywriting Final:** Ajustes del copy adaptados al diseño visual. | CW | Wireframes |
| **Diseño Responsive:** Adaptaciones para Mobile y Tablet. | UI | UI Desktop |
| **Setup de Repositorio y Boilerplate:** Configuración del proyecto, Tailwind/CSS y librerías de UI. | Dev 1 | Stack técnico |
| **Arquitectura de Datos / Backend:** Configuración de API para captura de leads, CRM y webhook de emails de confirmación. | Dev 2 | Stack técnico |
| **Exportación de Assets:** Exportar SVGs, optimizar imágenes (WebP) y mockups. | UI | UI Final |

---

#### **SEMANA 3: Desarrollo Frontend e Integraciones**
*Objetivo: Landing funcional en entorno de Staging/Pruebas.*

| Tarea | Responsable | Dependencia |
| :--- | :--- | :--- |
| **Maquetación Frontend (Hero + Secciones):** Hero, Features, Testimonios/Social Proof y Footer. | Dev 1 | UI Final + Assets |
| **Maquetación Frontend (Interacciones):** Sección de precios (toggle mensual/anual), FAQ (acordeón), animaciones sutiles. | Dev 2 | UI Final + Assets |
| **Integración de Formularios / Waitlist:** Conectar inputs con base de datos/CRM con validación de campos. | Dev 2 | Setup Backend |
| **Adaptabilidad Mobile y Cross-Browser:** Asegurar consistencia en Chrome, Safari, Firefox y dispositivos móviles. | Dev 1 | Maquetación |
| **Revisión de Diseño en Desarrollo (Design QA):** Chequeo visual y ajustes de espaciado/tipografía. | UI + Dev 1 | Maquetación |

---

#### **SEMANA