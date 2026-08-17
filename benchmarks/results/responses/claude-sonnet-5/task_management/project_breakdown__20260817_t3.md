# Claude Sonnet 5 — task_management/project_breakdown

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.27 | quality: 10.0
- latency_total: 22.982s | tokens_per_second: 94.9
- input_tokens: 117 | output_tokens: 2180
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de Lanzamiento: Landing Page SaaS de Gestión de Inventario

## Resumen del equipo
- 1 Diseñador (D)
- 2 Developers (Dev1, Dev2)
- 1 Copywriter (C)
- Timeline: 4 semanas (20 días laborables)

---

## FASE 0: Discovery & Estrategia (Días 1-2)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Definir buyer persona y propuesta de valor | C + Product Owner | 1 día | Ninguna |
| Investigar 3-5 competidores (landing pages) | C + D | 1 día | Ninguna |
| Definir estructura/wireframe de secciones | D | 1 día | Buyer persona definido |
| Definir stack técnico (framework, hosting, forms) | Dev1 + Dev2 | 0.5 día | Ninguna |

**Entregable:** Brief de producto + esqueleto de secciones aprobado.

---

## FASE 1: Contenido & Diseño (Días 3-8)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Copy de hero, propuesta de valor, CTAs principales | C | 2 días | Brief aprobado |
| Copy de secciones (features, beneficios, pricing, FAQ) | C | 2 días | Estructura definida |
| Wireframes de baja fidelidad | D | 1 día | Estructura definida |
| Diseño visual (mockups alta fidelidad, mobile + desktop) | D | 3 días | Wireframes + copy inicial |
| Setup de repo, entorno dev, CI básico | Dev1 | 1 día | Stack definido |
| Configurar analytics (GA4, Hotjar/Clarity) | Dev2 | 0.5 día | Ninguna |

**⚠️ Riesgo clave:** El diseño depende del copy. Recomiendo trabajar en paralelo con "copy placeholder" para no bloquear al diseñador.

**Entregable:** Mockups finales aprobados + copy final revisado.

---

## FASE 2: Desarrollo (Días 8-15)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Maquetación estructura HTML/componentes base | Dev1 | 2 días | Mockups aprobados |
| Implementación responsive de secciones (hero, features, pricing) | Dev1 | 3 días | Estructura base |
| Integración de formularios (waitlist/demo) + CRM/email tool | Dev2 | 2 días | Estructura base |
| Integración de animaciones/microinteracciones | Dev1 + D (QA visual) | 1 día | Secciones maquetadas |
| Optimización de performance (imágenes, lazy load) | Dev2 | 1 día | Contenido cargado |
| Implementar SEO on-page (meta tags, schema, sitemap) | Dev2 | 1 día | Copy final |
| Testing cross-browser y responsive | Dev1 + Dev2 | 1 día | Desarrollo completo |

**Entregable:** Landing funcional en entorno staging.

---

## FASE 3: QA, Revisión & Optimización (Días 16-18)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Revisión de copy final (errores, tono, CTAs) | C | 0.5 día | Staging disponible |
| QA visual (pixel-perfect vs mockups) | D | 1 día | Staging disponible |
| Testing de formularios y flujos de conversión | Dev1 + Dev2 | 1 día | Staging disponible |
| Test de velocidad (PageSpeed, Core Web Vitals) | Dev2 | 0.5 día | QA visual completado |
| Revisión legal/compliance (privacy policy, cookies) | C + Product Owner | 0.5 día | Ninguna |
| Ajustes finales según feedback | Todo el equipo | 1 día | QA completo |

**Entregable:** Landing lista para producción, aprobada por stakeholders.

---

## FASE 4: Lanzamiento (Días 19-20)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Deploy a producción | Dev1 | 0.5 día | Aprobación final |
| Configurar dominio, SSL, CDN | Dev2 | 0.5 día | Deploy inicial |
| Verificación post-deploy (links, forms, analytics) | Dev1 + Dev2 + D | 0.5 día | Deploy completo |
| Preparar anuncio (redes, email, PR) | C | En paralelo | Ninguna |
| Monitoreo día 1 (errores, conversiones) | Dev2 | 0.5 día | Lanzamiento en vivo |

---

## 📅 Timeline visual (Gantt simplificado)

```
Semana 1: [Discovery][Copy/Diseño inicia]
Semana 2: [Diseño continua][Dev setup][Copy final]
Semana 3: [Desarrollo intensivo][Integraciones]
Semana 4: [QA][Ajustes][LANZAMIENTO]
```

---

## 🚨 Riesgos y recomendaciones

1. **Cuello de botella en Diseño→Dev**: considera que Dev1 empiece a maquetar secciones ya aprobadas mientras D sigue diseñando otras (trabajo por lotes).
2. **Copy es la dependencia crítica**: si el copywriter se atrasa, todo se retrasa. Bloquea tiempo dedicado en Semana 1.
3. **Buffer de 2 días**: no incluido explícitamente arriba, pero recomiendo restar 2 días de margen antes del lanzamiento real para imprevistos (así el "lanzamiento real" sería día 18-19, no día 20).
4. **Reuniones de sync diarias de 15 min** son clave dado el equipo pequeño y timeline ajustado.

¿Quieres que te prepare esto en formato de tablero (ej. estructura para Trello/Notion/Asana) o prefieres un Gantt más detallado con fechas específicas según el día de inicio real?