# Tencent Hy3 — task_management/project_breakdown

- model_id: `tencent/hy3`
- success: True  | final: 8.75 | quality: 9.72
- latency_total: 21.01s | tokens_per_second: 60.1
- input_tokens: 93 | output_tokens: 1262
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Aquí tienes un plan de proyecto estructurado para lanzar la landing page en 4 semanas (20 días hábiles aprox.) con tu equipo actual:

**Equipo:**
*   **D** (Diseñador UI/UX): 1 persona
*   **Dev1 / Dev2** (Developers Frontend/Backend): 2 personas
*   **C** (Copywriter): 1 persona
*   **PM** (Tú / Project Manager): Coordinación (asumido)

---

### Fase 1: Estrategia y Arquitectura (Semana 1)
*Objetivo: Definir qué decimos y cómo lo estructuramos antes de diseñar.*

| Tarea | Responsable | Dependencias | Días (Sem 1) |
| :--- | :--- | :--- | :--- |
| **1.1 Definición de Propuesta Única (USP) y Buyer Persona** | C + PM | - | D1-D2 |
| **1.2 Mapeo de la estructura de la Landing (Secciones: Hero, Features, Pricing, FAQ, CTA)** | C + D | 1.1 | D2-D3 |
| **1.3 Redacción del Borrador de Copy (Textos largos)** | C | 1.2 | D3-D5 |
| **1.4 Wireframes de baja fidelidad (Esqueleto visual)** | D | 1.2 | D3-D4 |

---

### Fase 2: Diseño Visual y Contenido Final (Semana 2)
*Objetivo: Hacer que se vea bien y pulir los textos.*

| Tarea | Responsable | Dependencias | Días (Sem 2) |
| :--- | :--- | :--- | :--- |
| **2.1 Diseño de UI (High Fidelity) en Figma** | D | 1.4 | D6-D9 |
| **2.2 Revisión y Aprobación de Diseño** | PM + C | 2.1 | D10 |
| **2.3 Copy final (Optimización SEO y persuasión)** | C | 1.3, 2.2 | D8-D10 |
| **2.4 Preparación de Assets (Imágenes, logos, íconos)** | D | 2.1 | D9-D10 |

---

### Fase 3: Desarrollo Frontend y Backend (Semana 3)
*Objetivo: Construir la página y conectar la lógica.*

| Tarea | Responsable | Dependencias | Días (Sem 3) |
| :--- | :--- | :--- | :--- |
| **3.1 Setup técnico (Dominio, Hosting, Repo, CMS/Stack)** | Dev1 | 2.2 | D11-D12 |
| **3.2 Desarrollo Frontend (HTML/CSS/JS según diseño)** | Dev2 | 2.1, 2.4 | D11-D15 |
| **3.3 Integración de Formularios/Leads (Backend/Email)** | Dev1 | 3.1 | D13-D15 |
| **3.4 Carga de Contenido (Textos de C)** | Dev2 | 2.3, 3.2 | D14-D15 |

---

### Fase 4: QA, Pulido y Lanzamiento (Semana 4)
*Objetivo: Asegurar calidad y publicar.*

| Tarea | Responsable | Dependencias | Días (Sem 4) |
| :--- | :--- | :--- | :--- |
| **4.1 Testing (Mobile/Desktop, velocidad, bugs)** | Dev1 + Dev2 | 3.4 | D16-D17 |
| **4.2 Ajustes de diseño post-dev (si hay desvíos)** | D | 4.1 | D17-D18 |
| **4.3 Configuración Analytics y Pixel de Marketing** | Dev1 | 3.1 | D17 |
| **4.4 Revisión Final de Contenido y CTA** | C | 3.4 | D18 |
| **4.5 LANZAMIENTO (Go Live)** | Dev1 | 4.1-4.4 | D19 |
| **4.6 Monitorización post-lanzamiento (24h)** | Dev2 + PM | 4.5 | D20 |

---

### Cronograma Visual (Resumen)
*   **Semana 1:** Estrategia (C) + Wireframes (D).
*   **Semana 2:** Diseño (D) + Copy Final (C).
*   **Semana 3:** Código (Dev1/Dev2) + Carga datos.
*   **Semana 4:** Pruebas (QA) + Lanzamiento.

### Notas Críticas de Gestión:
1.  **Cuello de botella:** El Diseñador (D) es el recurso más crítico en Semana 2. No retrases la aprobación de wireframes en Semana 1.
2.  **Parallelización:** Dev1 puede empezar a configurar el servidor (3.1) apenas se apruebe el diseño el Día 10, mientras Dev2 maqueta.
3.  **Buffer:** Se ha dejado D18-D20 como margen para imprevistos (cambios de última hora o bugs graves). Si todo va perfecto, puedes lanzar el Día 18.