# Muse Ember — task_management/project_breakdown

- model_id: `meta/muse-ember`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 10.124s | tokens_per_second: 488.1
- input_tokens: 70 | output_tokens: 4941
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y realista del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Para una landing SaaS en 4 semanas (20 días laborables) es viable, pero **solo si el copy y el diseño van en paralelo al desarrollo y hay un freeze de alcance en el Día 5**. El camino crítico no es el código, son las aprobaciones.

Asumo: Landing en 1 idioma, 1 CTA principal `Solicitar demo`, desarrollo custom (Next.js/React). Si es Webflow/WordPress, la Fase 3 se acorta 4-5 días.

### 1. Equipo y carga realista

| Rol | Semana 1 | Semana 2 | Semana 3 | Semana 4 |
| :--- | :--- | :--- | :--- | :--- |
| **Copywriter** | 100% - Estrategia y copy | 50% - Ajustes a UI y SEO | 20% - Revisión en staging | 10% - Erratas |
| **Diseñador (1)** | 80% - Wireframe | 100% - UI Desktop/Mobile | 30% - Soporte a devs | 20% - Correcciones QA |
| **Dev 1 - Frontend** | 30% - Setup y arquitectura | 100% - Maquetación | 100% - Responsive y animaciones | 80% - QA y fixes |
| **Dev 2 - Integraciones** | 30% - Setup y tracking plan | 80% - Formulario/CRM | 100% - Analytics, SEO técnico, performance | 80% - QA y deploy |

**Regla de oro:** Standup diario 15 min + aprobación en máximo 24h. Si una aprobación se retrasa 2 días, el lanzamiento se retrasa 2 días.

### 2. Timeline por Fases

**FASE 0 - Kickoff y Estrategia (Días 1-2)**
**FASE 1 - Copy + Wireframe (Días 2-5)**
**FASE 2 - Diseño UI (Días 6-11)**
**FASE 3 - Desarrollo (Días 6-16)**
**FASE 4 - QA y Pre-lanzamiento (Días 16-18)**
**FASE 5 - Lanzamiento (Día 19)**

> Recomendación: Lanzar **jueves Día 19**, no viernes. Dejas el viernes Día 20 como buffer post-lanzamiento.

### 3. Desglose Detallado: Tareas, Responsables y Dependencias

| # | Tarea | Responsable | Depende de | Días | Entregable |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FASE 0** | | | | | |
| 0.1 | Kickoff: audiencia, propuesta de valor, CTA, KPIs | Copywriter | Input Producto/Marketing | 1 | Brief de 1 página |
| 0.2 | Recopilar assets: logo, screenshots del producto, pricing, testimonios, integraciones | Copywriter coordina | Producto | 1-2 | Carpeta de assets |
| 0.3 | Definir estructura de la página: Hero, Beneficios, Features, Cómo funciona, Integraciones, Pricing, Testimonios, FAQ, CTA final | Copywriter + Diseñador | 0.1 | 2 | Outline aprobado |
| **FASE 1** | | | | | |
| 1.1 | Borrador completo de copy por sección | Copywriter | 0.3 | 2-3 | Doc v1 |
| 1.2 | Wireframe low-fi Desktop + Mobile | Diseñador | 0.3 | 3-4 | Wireframes en Figma |
| 1.3 | **HITO 1: Aprobación Copy v1 + Wireframe** | Aprobador externo | 1.1 + 1.2 | 5 | **Freeze de alcance** |
| 1.4 | Setup técnico: Repo, hosting, dominio, SSL, CI/CD, entorno staging | Dev1 + Dev2 | - | 1-2 | Staging online |
| **FASE 2** | | | | | |
| 2.1 | Copy final + Title/Meta description SEO + microcopy formularios | Copywriter | 1.3 | 6-7 | Copy final |
| 2.2 | Diseño UI Alta Fidelidad - Desktop | Diseñador | 2.1 | 6-9 | Diseño v1 |
| 2.3 | Diseño UI - Mobile + Prototipo clicable | Diseñador | 2.2 | 9-10 | Prototipo |
| 2.4 | **HITO 2: Aprobación Diseño** + Handoff (assets exportados, specs, tipografías) | Aprobador externo | 2.3 | 11 | Diseño aprobado |
| **FASE 3** | | | | | |
| 3.1 | Maquetación frontend: componentes, estilos, responsive | Dev1 | 1.3 (puede empezar con wireframe) | 6-13 | Landing en staging |
| 3.2 | Animaciones, interacciones, menú mobile, acordeón FAQ | Dev1 | 2.4 | 11-14 |  |
| 3.3 | Formulario Demo -> CRM/Email (HubSpot, etc.) + validaciones + página de gracias | Dev2 | 2.1 | 8-12 | Formulario funcional |
| 3.4 | Integraciones: GA4, GTM, Meta Pixel, Chat, Calendly/HubSpot Meeting | Dev2 | 1.4 | 10-13 | Tracking verificado |
| 3.5 | SEO técnico: sitemap.xml, robots, Schema, OpenGraph, favicon. Performance Core Web Vitals >90 | Dev2 + Dev1 | 3.1 | 13-15 | Checklist SEO |
| **FASE 4** | | | | | |
| 4.1 | QA interna: cross-browser, responsive, formularios, enlaces rotos, accesibilidad | Dev1 + Dev2 | 3.5 | 16 | Bugs listados |
| 4.2 | QA de contenido/diseño sobre staging real | Diseñador + Copywriter | 3.5 | 16-17 | Feedback |
| 4.3 | Correcciones y pulido final | Todos | 4.1 + 4.2 | 17-18 | Versión final |
| 4.4 | Checklist pre-launch: backup, plan rollback, 404, legal/cookies | Dev1 | 4.3 | 18 | OK Go-Live |
| **FASE 5** | | | | | |
| 5.1 | **HITO 3: Despliegue a Producción** | Dev1 + Dev2 | 4.4 | 19 | Web online |
| 5.2 | Monitorización 48h: uptime, formulario, analytics, velocidad | Devs | 5.1 | 19-20 | Reporte post-launch |

### 4. Dependencias y Camino Crítico

```
Input Producto (0.1/0.2) -> Copy (1.1) -> Copy Aprobado (1.3) -> UI Final (2.2) -> Dev Final (3.1) -> QA (4.1) -> Launch (5.1)
Input Producto (0.3) -> Wireframe (1.2) -> Copy Aprobado (1.3) -----^
Setup Técnico (1.4) es INDEPENDIENTE -> puede empezar Día 1
```

**Camino crítico:** Copy aprobado -> Diseño aprobado -> Desarrollo final -> QA.
Todo lo que no esté en ese camino (setup, tracking plan) se hace en paralelo para no bloquear.

### 5. Riesgos principales en 4 semanas

1.  **Screenshots del producto no listos:** Mitigación: Diseñador crea mockups en Figma el Día 2. No esperar al producto final.
2.  **Pricing / mensaje no definido:** Mitigación: Freeze el Día 5. Si no hay pricing, la sección sale con "Contacta con ventas".
3.  **Aprobaciones lentas de Legal/Producto:** Mitigación: SLA de 24h por escrito en el kickoff. Un solo aprobador, no comité.
4.  **Cambios de alcance en Semana 3:** Prohibido. Cualquier sección nueva va a una v2 post-lanzamiento.

Con este plan, el diseñador y el copywriter terminan su trabajo pesado en la Semana 2, y los devs tienen 10 días limpios de desarrollo + 3 días de QA sin interrupciones.