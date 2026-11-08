# Muse Wonder — task_management/project_breakdown

- model_id: `meta/muse-wonder`
- success: True  | final: 8.06 | quality: 9.7
- latency_total: 20.66s | tokens_per_second: 114.6
- input_tokens: 70 | output_tokens: 2368
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Aquí tienes un plan realista para lanzar en 4 semanas sin quemar al equipo. Está pensado para una landing de captación de leads / lista de espera / reserva de demo, no para un producto completo.

**Equipo:**
* **D:** Diseñador (UX/UI)
* **Dev 1:** Frontend
* **Dev 2:** Backend / DevOps / Integraciones
* **C:** Copywriter
* **Tú:** Actúas como PM / Product Owner. Apruebas todo. Sin esto, el proyecto se bloquea.

### Ruta Crítica
Esta es la cadena que NO se puede retrasar:
`Propuesta de valor -> Copy -> Wireframe -> Diseño UI -> Desarrollo Frontend -> QA -> Lanzamiento`

Todo lo demás va en paralelo.

---

### FASE 1: Estrategia y Contenido (Semana 1)
**Objetivo:** Que no se diseñe ni se programe nada sin tener claro qué vender.
**Hito al viernes:** Wireframe + Copy v1 aprobados

| Tarea | Responsable | Depende de | Duración |
| :--- | :--- | :--- | :--- |
| Kickoff: definir objetivo (¿waitlist, demos, registro?), ICP, competidores | Tú + C + D | - | Día 1 |
| Definir propuesta de valor, mensaje principal y CTA único | C | Kickoff | Día 1-2 |
| Estructura de la landing: Hero, Problema, Solución, Features, Cómo funciona, Pricing, FAQ, CTA final | C + D | Propuesta de valor | Día 2 |
| Copy borrador completo v1 (sin pulir) | C | Estructura | Día 2-4 |
| Wireframe en baja fidelidad en Figma | D | Estructura | Día 3-5 |
| Pedir accesos: dominio, hosting, Google Analytics, CRM/Email (HubSpot, Mailchimp, etc.), redes | Dev 2 | Kickoff | Día 1-2 |
| Setup técnico: repo, entorno staging, dominio temporal | Dev 2 + Dev 1 | Accesos | Día 3-5 |

### FASE 2: Diseño y Copy Final (Semana 2)
**Objetivo:** Cerrar diseño al 100%. No más cambios de estructura después.
**Hito al viernes:** Diseño UI aprobado y entregado a devs

| Tarea | Responsable | Depende de | Duración |
| :--- | :--- | :--- | :--- |
| Diseño UI Desktop en alta fidelidad | D | Wireframe aprobado + Copy v1 | Día 6-9 |
| Diseño UI Mobile (responsive) | D | Diseño Desktop | Día 9-10 |
| Ilustraciones, iconos, mockups del producto, assets | D | Diseño UI | Día 8-10 |
| Copy final pulido v2 adaptado al diseño | C | Diseño UI v1 | Día 8-10 |
| Revisión legal básica: Privacidad, Cookies, Términos | C + Tú | - | Día 9-10 |
| Maquetación base: setup de framework (Next.js/Astro/Webflow), sistema de diseño, fuentes/colores | Dev 1 | Wireframe aprobado | Día 6-10 |
| Definir backend del formulario: a dónde van los leads, email de confirmación | Dev 2 | Estructura | Día 6-8 |

> **Congelación de alcance: Fin del Día 10.** A partir de aquí no entran secciones nuevas.

### FASE 3: Desarrollo (Semana 3)
**Objetivo:** Landing funcional en staging, idéntica al Figma.
**Hito al viernes:** Feature Freeze

| Tarea | Responsable | Depende de | Duración |
| :--- | :--- | :--- | :--- |
| Maquetación completa Desktop + Mobile | Dev 1 | Diseño UI final | Día 11-15 |
| Animaciones básicas e interactividad | Dev 1 | Maquetación | Día 14-16 |
| Integración formulario -> CRM/Email + email automático | Dev 2 | Backend definido | Día 11-13 |
| Integración Analytics GA4, Pixel, Tag Manager | Dev 2 | - | Día 13-14 |
| SEO técnico: titles, meta descriptions, OG images, sitemap | Dev 1 + C | Copy final | Día 14-15 |
| Optimización performance: imágenes, carga <2.5s, Lighthouse >90 | Dev 1 | Maquetación | Día 15-17 |

### FASE 4: QA, Ajustes y Lanzamiento (Semana 4)
**Objetivo:** No lanzar con errores.
**Hito:** Go / No-Go el Día 19 por la mañana

| Tarea | Responsable | Depende de | Duración |
| :--- | :--- | :--- | :--- |
| QA funcional: probar formulario, links, CTA en Chrome/Safari/Firefox, iOS/Android | Todo el equipo | Feature Freeze | Día 16-17 |
| QA de contenido: ortografía, precios, claims legales | C + Tú | Staging completo | Día 16-17 |
| Corrección de bugs (deja 2 días completos, siempre salen) | Dev 1 + Dev 2 | QA | Día 17-19 |
| Accesibilidad y responsive final | D + Dev 1 | QA | Día 18 |
| Config producción: dominio final, SSL, CDN, backups | Dev 2 | Aprobación final | Día 19 |
| **LANZAMIENTO** | Dev 2 | Go / No-Go | **Día 20 por la mañana** |
| Monitorización post-lanzamiento 48h: errores, leads entrando | Dev 2 + Tú | Lanzamiento | Día 20-22 |

### Timeline Visual

```
Semana 1: [Estrategia][Copy v1][Wireframe][Setup técnico]
Semana 2:          [Diseño UI......][Copy Final][Dev base]
Semana 3:                      [Desarrollo Frontend/Backend...]
Semana 4:                                   [QA][Bugs][LANZAMIENTO]
```

### Riesgos Reales y Cómo Evitarlos

1.  **El copy llega tarde:** Es el bloqueo nº1. Por eso el diseñador trabaja con copy v1, no espera al final.
2.  **Cambios infinitos de diseño:** Solo 2 rondas de revisión: una en wireframe (Día 5) y una en UI (Día 9).
3.  **Integraciones que fallan:** Dev 2 debe probar el formulario el Día 13, no el Día 19. Pide las API keys el Día 1.
4.  **Falta de assets del producto:** Si aún no hay screenshots reales, el diseñador crea mockups en la Semana 2. No esperéis al producto.

### Qué dejar FUERA para llegar a tiempo (Backlog Post-Lanzamiento)

Blog, multi-idioma, A/B testing complejo, chat en vivo, animaciones 3D, testimonios en video. Todo eso es Semana 5+.

**Reuniones mínimas:**
Lunes 30min: planificación semanal. Miércoles 15min: bloqueo. Viernes 30min: demo en staging y aprobación del hito.

Si cumples los hitos del Día 5, 10 y 15, lanzas el Día 20 sin problema.