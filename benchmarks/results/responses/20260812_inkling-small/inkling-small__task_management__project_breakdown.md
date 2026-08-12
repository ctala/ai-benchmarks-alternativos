# Inkling Small — task_management/project_breakdown

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 263.711s | tokens_per_second: 20.4
- input_tokens: 77 | output_tokens: 5368
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y realista del proyecto.

## Respuesta completa

Sí es posible lanzar una landing page de alta conversión en 4 semanas con ese equipo, pero **debes tratarlo como un MVP de marketing, no como una web corporativa completa**. Con 1 diseñador, 2 devs y 1 copywriter, el riesgo principal es el cuello de botella del diseñador y los cambios de copy a última hora.

Aquí tienes el plan desglosado por fases, con tareas, responsables, dependencias y un timeline realista (asumiendo inicio **Lunes**).

---

### 1. Supuestos críticos para que esto funcione
*   **Scope fijo:** Landing de una sola página (one-page) con Hero, Problema/Solución, 3-4 features clave, Social Proof (logos/testimonio), CTA de demo/trial, y FAQ básico.
*   **Producto visual disponible:** El diseñador debe tener screenshots/mockups del SaaS de inventario **antes de la Semana 2**; si no, se pierde 3-4 días inventando UI del producto.
*   **No hay backend complejo:** Solo captura de leads (formulario + integración a HubSpot/Calendly/Notion/CRM). No se construye el SaaS, solo la landing.
*   **Aprobaciones rápidas:** El copywriter y diseñador deben tener autoridad para aprobar sin comités de 3 personas.
*   **Framework rápido:** Usa Astro, Next.js con un kit de UI (Tailwind/Shadcn) o un builder (Webflow/Framer) si los devs lo dominan, para no perder tiempo en CSS desde cero.

---

### 2. Timeline por semanas (4 semanas)

| Semana | Objetivo | Entregable clave |
| :--- | :--- | :--- |
| **1** | **Estrategia + Copy + Wireframes** | Copy v1, wireframes, setup técnico, mockups |
| **2** | **Diseño final + Setup Dev + Copy definitivo** | Figma aprobado, repo listo, copy final, maquetación base |
| **3** | **Desarrollo + Integraciones + SEO** | Landing completa funcional |
| **4** | **QA + Ajustes + Lanzamiento** | Live, formulario probado, monitorización |

---

### 3. Desglose por fases, tareas y responsables

#### FASE 1 — Estrategia y Arquitectura (Semana 1: Días 1-5)
**Objetivo:** Que nadie empiece a diseñar o codear sin saber qué mensaje vende.

| Días | Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Kickoff + Brief de producto (audiencia, propuesta de valor, KPIs) | **Todos** | — | Documento de brief (1 página) |
| 1-2 | Setup técnico: repo, hosting, dominio, CMS/estático, analytics básico | **Dev 1 + Dev 2** | — | Entorno en producción (staging) |
| 2-3 | Investigación de mensaje: headlines, objeciones, propuesta de valor | **Copywriter** | Brief aprobado | Documento de mensaje / Messaging |
| 2-3 | Wireframes de baja fidelidad (mobile/desktop): Hero, Features, Social Proof, CTA, Footer | **Diseñador** | Estructura de secciones definida | Wireframes en Figma/Whimsical |
| 3-4 | **Copy v1:** Hero, H2, bullets de features, testimonios, textos de formulario, meta descripción | **Copywriter** | Wireframes (para ajustar longitudes) | Copy doc v1 |
| 4-5 | Mockups / Screenshots del producto para la landing y assets visuales (iconos, ilustraciones) | **Diseñador** | Producto visual disponible | Assets en carpeta compartida |

> **Nota de dependencia:** El copywriter y diseñador deben trabajar en paralelo, pero el diseñador no debe pasar a alta fidelidad hasta que el copy v1 esté aprobado (o al menos el 80%).

---

#### FASE 2 — Diseño Visual y Setup Dev (Semana 1-2: Días 4-10)
**Objetivo:** Diseño final aprobado y desarrollo iniciado sin bloqueos.

| Días | Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| 6-9 | **UI alta fidelidad:** Hero, Features, Social Proof, CTA, Footer, responsive | **Diseñador** | Copy v1 + wireframes aprobados | Figma final (desktop + mobile) |
| 6-8 | Copy definitivo + SEO básico (H1, meta tags, OG tags, alt text) | **Copywriter** | Wireframes | Copy final + SEO doc |
| 9 | Revisión y **sign-off** de diseño + copy con todo el equipo | **Todos** | Diseño + Copy | Aprobación formal (evita cambios) |
| 9-10 | Maquetación base (Header, Hero, Footer, sistema de grid) | **Dev 1** | Diseño aprobado | Componentes base |
| 9-10 | Configuración de formularios / integración CRM / Calendly / webhook | **Dev 2** | — | Endpoint / integración funcionando |

> **Truco de velocidad:** El diseñador debe usar un **design system existente** (ej. componentes de shadcn/ui, Ant Design, o un kit de landing) para no diseñar botones y cards desde cero.

---

#### FASE 3 — Desarrollo y Producción (Semana 2-3: Días 8-15)
**Objetivo:** La landing está completa y funcional.

| Días | Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| 11-13 | Maquetación de secciones restantes (Features, Social Proof, FAQ, CTA) | **Dev 1** | Diseño final + componentes base | Landing maquetada |
| 11-13 | Inserción de copy final, imágenes, mockups y assets | **Dev 1 + Copywriter** | Copy final | Contenido integrado |
| 12-14 | Integración de formularios (demo request / trial), validación, mensajes de error | **Dev 2** | Endpoint listo | Formulario 100% funcional |
| 14-15 | SEO técnico: velocidad (Core Web Vitals), responsive, meta, sitemap, robots.txt | **Dev 2** | Landing maquetada | Informe de velocidad |
| 15 | Animaciones ligeras (fade-in, scroll reveal) y micro-interacciones | **Dev 1** | Landing completa | Interactividad |

> **Dependencia crítica:** Si el copywriter llega tarde con cambios en la Semana 3, se rompe todo. El copy debe ser **final** al inicio de esta fase.

---

#### FASE 4 — QA, Ajustes y Lanzamiento (Semana 4: Días 16-20)
**Objetivo:** Nada roto, todo probado, live.

| Días | Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- | :--- |
| 16-17 | **QA completo:** Cross-browser (Chrome, Safari, Firefox), mobile (iOS/Android), formularios, links rotos, copy final | **Todos** | Landing completa | Lista de bugs + fixes |
| 17-18 | Ajustes finales de diseño (espaciados, colores) y copy de última hora | **Diseñador + Copywriter** | QA | Versión final |
| 18 | Prueba de carga y velocidad final; verificación de OG tags y meta | **Dev 2** | Ajustes | Confirmación técnica |
| 19 | **Lanzamiento:** Deploy a producción, DNS, SSL, redirección | **Dev 1 + Dev 2** | Todo aprobado | Landing live |
| 20 | Monitorización inicial (formulario, tráfico, errores 404/500), backup | **Dev 2** | Live | Dashboards activos |

---

### 4. Mapa de dependencias (flujo crítico)

```
Kickoff / Brief
     │
     ├──► Copywriter ──► Copy v1 ──► Copy Final ──► Inserción (Semana 3)
     │
     ├──► Diseñador ──► Wireframes ──► UI Alta (Semana 2) ──► Sign-off ──► Maquetación (Semana 3)
     │
     └──► Devs ──► Setup Repo/Staging ──► Maquetación Base (D9-10) ──► Desarrollo (D11-15) ──► QA (D16)
```

**El cuello de botella es el Diseñador.** Si tarda más de 2 días en pasar a alta fidelidad, se retrasa todo. Mitigación: usar templates de landing de alta conversión (ej. de Tailwind UI, Landings de Framer, o kits de Figma) y adaptar, no diseñar desde cero.

---

### 5. Asignación de roles por persona

| Persona | Rol principal | Rol secundario |
| :--- | :--- | :--- |
| **Diseñador** | UI/UX, mockups, responsive, assets | Revisión de copy en layout |
| **Dev 1 (Lead)** | Maquetación frontend, arquitectura, animaciones, deploy | QA técnico básico |
| **Dev 2** | Integraciones (CRM/formulario), SEO técnico, backend de formularios, monitorización | Soporte en responsive |
| **Copywriter** | Estrategia de mensaje, copy de todas las secciones, SEO textual, textos de formulario | Ajustes finales de microcopy |

---

### 6. Riesgos y cómo mitigarlos

| Riesgo | Impacto | Mitigación |
| :--- | :--- | :--- |
| **El producto no tiene screenshots/mockups** | Alto | El diseñador debe crear mockups realistas en Figma en la Semana 1. No esperar al producto final. |
| **Cambios de copy en Semana 3** | Alto | Lock de copy al final de Semana 2. Solo micro-ajustes permitidos. |
| **Diseñador se bloquea** | Alto | Usar kit de UI / template de landing. No diseñar sistema de diseño completo. |
| **Formularios no capturan leads** | Medio | Prueba con datos reales en Staging desde el Día 12. No esperar al final. |
| **No hay tráfico para validar** | Medio | Configurar Google Analytics 4 y eventos de conversión (demo request) antes del lanzamiento. |

---

### 7. Checklist del día del lanzamiento (Día 20)

- [ ] Landing accesible en dominio principal.
- [ ] Formulario envía datos al CRM/Email y muestra mensaje de éxito.
- [ ] Meta tags, OG image y H1 correctos.
- [ ] Responsive probado en móvil (iPhone + Android).
- [ ] Velocidad aceptable (LCP < 2.5s, CLS < 0.1).
- [ ] Tracking de conversión activo (GA4 + evento de formulario).
- [ ] Copy final revisado sin errores de ortografía.
- [ ] Links internos/externos funcionando.

---

### Recomendación final para acelerar
Si tu objetivo es captar leads de inventario, **no intentes que sea perfecta**. Prioriza:
1. **Hero con propuesta clara** (qué resuelve para inventario).
2. **3 features con iconos y una línea de texto** (no párrafos largos).
3. **Social proof** (aunque sea 1 testimonio real o 2 logos de clientes).
4. **CTA visible y repetido** (Demo / Trial / Hablar con ventas).

Si necesitas que te detalle los textos específicos para un SaaS de inventario (headline, objections, etc.) o que te sugiera la estructura exacta de secciones, dímelo y lo desarrollo.