# Tencent Hy3 — task_management/project_breakdown

- model_id: `tencent/hy3`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 120.406s | tokens_per_second: 32.4
- input_tokens: 90 | output_tokens: 3903
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Para lanzar una landing page SaaS en 4 semanas (aprox. 20 días hábiles) con un equipo reducido (1 Diseñador, 2 Developers, 1 Copywriter), la clave es **trabajar en paralelo siempre que sea posible y no crear cuellos de botella**. 

*Nota: Asumiré que tú actúas como Project Manager (PM) o Product Owner para dar el "OK" final y alinear la visión.*

Aquí tienes el desglose del proyecto, organizado por fases, con responsables y dependencias:

---

### 📅 FASE 1: Estrategia y Arquitectura (Semana 1)
**Objetivo:** Alinear al equipo sobre qué se va a construir y para quién.

| Tarea | Responsable | Dependencias | Días (S1) |
| :--- | :--- | :--- | :--- |
| **1.1 Kick-off y Objetivos:** Definir métrica de éxito (ej. demos agendadas vs. emails capturados). | PM (Tú) + Equipo | Ninguna | 1 |
| **1.2 Investigación:** Análisis de competidores SaaS de inventario y definición de Buyer Persona. | Copywriter | 1.1 | 1-2 |
| **1.3 Sitemap y Estructura:** Definir secciones (Hero, Problema/Solución, Features, Precios, FAQ, CTA). | Diseñador + Copy | 1.2 | 3-4 |
| **1.4 Aprobación de Estructura:** Validar el flujo de la página antes de empezar a crear. | PM | 1.3 | 5 |

---

### 🎨 FASE 2: Contenido y Diseño (Semana 2)
**Objetivo:** Tener el texto y el diseño visual (Figma) 100% aprobados.

| Tarea | Responsable | Dependencias | Días (S2) |
| :--- | :--- | :--- | :--- |
| **2.1 Redacción de Copy:** Headlines persuasivos, beneficios, CTAs y meta-tags SEO. | Copywriter | 1.4 | 6-9 |
| **2.2 Diseño UI (Figma):** El diseñador maqueta Desktop y Mobile. *Tip: Puede usar textos temporales ("Lorem Ipsum") para no esperar al copywriter y agilizar.* | Diseñador | 1.4 | 6-9 |
| **2.3 Revisión y Aprobación:** El equipo revisa el diseño final con el copy ya integrado. | PM + Equipo | 2.1, 2.2 | 10 |

---

### 💻 FASE 3: Desarrollo (Semana 3)
**Objetivo:** Construir la página en el entorno de staging (pruebas).

| Tarea | Responsable | Dependencias | Días (S3) |
| :--- | :--- | :--- | :--- |
| **3.1 Setup Técnico:** Crear repo, configurar dominio/staging, elegir stack (Next.js, Webflow, etc.). | Dev 1 | 2.3 | 11 |
| **3.2 Maquetación Frontend:** Pasar el diseño de Figma a código (HTML/CSS/JS). | Dev 1 + Dev 2 | 2.3, 3.1 | 12-15 |
| **3.3 Integraciones:** Conectar formularios, Google Analytics 4, Meta Pixel, y CRM (ej. HubSpot). | Dev 2 | 3.1 | 12-14 |
| **3.4 Optimización:** Comprimir imágenes, lazy loading para que la página cargue rápido (<2s). | Dev 1 | 3.2 | 14-15 |

---

### 🚀 FASE 4: QA, Pulido y Lanzamiento (Semana 4)
**Objetivo:** Probar todo, corregir errores y poner la página en vivo.

| Tarea | Responsable | Dependencias | Días (S4) |
| :--- | :--- | :--- | :--- |
| **4.1 QA (Control de Calidad):** Probar en distintos navegadores (Chrome, Safari) y móviles. Buscar bugs visuales. | Diseñador + Devs | 3.2, 3.3 | 16-17 |
| **4.2 Revisión Final en Staging:** El Copywriter y PM leen la página real para cazar errores de ortografía o formato. | Copy + PM | 4.1 | 17 |
| **4.3 Checklist SEO/Técnico:** Verificar que los pixels funcionen y los meta-tags estén puestos. | Dev 2 | 4.1 | 18 |
| **4.4 GO-LIVE (Lanzamiento):** Desplegar a producción. | Dev 1 + Dev 2 | 4.2, 4.3 | 19 |
| **4.5 Monitoreo:** Revisar que no haya caídas del servidor y que los formularios lleguen al correo/CRM. | Equipo | 4.4 | 20 |

---

### 💡 Recomendaciones para no fallar en el intento:

1. **Comunicación Asíncrona:** Usa una herramienta como **Trello, Asana o Notion** para que el diseñador sepa qué sección ya tiene texto listo y los devs sepan qué componentes están aprobados.
2. **El Diseñador y el Copy no se bloqueen:** En la Semana 2, el diseñador debe entregar el "look & feel" y la disposición de los elementos sin esperar a que el copywriter termine la última palabra. El copy se "vuelca" al Figma el día 9.
3. **Enfoque MVP (Minimum Viable Product):** Para un SaaS de inventario, no intentes meter 20 features en la landing. Céntrate en **3 dolores principales** del cliente y **1 CTA claro** (ej. "Prueba Gratis 14 días").
4. **Staging antes de Producción:** Nunca desarrollen directo en la URL final. El día 18 debe haber una versión oculta para que el PM y el Copywriter la prueben sin estrés.