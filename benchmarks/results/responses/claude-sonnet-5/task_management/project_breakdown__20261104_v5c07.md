# Claude Sonnet 5 — task_management/project_breakdown

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 26.869s | tokens_per_second: 93.3
- input_tokens: 117 | output_tokens: 2508
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de Lanzamiento: Landing Page SaaS Inventario

## Resumen del equipo y restricciones
- 1 diseñador, 2 developers, 1 copywriter
- 4 semanas (20 días laborales)
- Supuesto: el copywriter y diseñador pueden empezar en paralelo desde el día 1

---

## FASE 0: Preparación y definición (Días 1-3)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Definir propuesta de valor, buyer persona, mensajes clave | Copywriter + Product Owner | 2 días | Ninguna |
| Research de competencia (otras landings SaaS inventario) | Diseñador + Copywriter | 1 día | Ninguna |
| Definir estructura de la landing (wireframe de secciones: hero, features, pricing, testimonios, CTA) | Diseñador | 2 días | Research |
| Setup técnico: repo, stack (ej. Next.js + Tailwind), hosting, dominio | Dev 1 | 1 día | Ninguna |
| Definir analytics/tracking (GA4, Hotjar, pixel) | Dev 2 | 1 día | Ninguna |

**Entregable:** Brief aprobado + wireframe low-fi + entorno técnico listo

---

## FASE 1: Contenido y diseño visual (Días 4-9)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Copy completo (headlines, subtítulos, CTAs, bullets de features) | Copywriter | 3 días | Wireframe aprobado |
| Diseño UI alta fidelidad (desktop + mobile) en Figma | Diseñador | 4 días | Wireframe + copy inicial |
| Banco de assets (iconos, mockups del producto, ilustraciones) | Diseñador | 2 días (paralelo) | — |
| Setup de componentes base / design system (botones, tipografía, grid) | Dev 1 | 2 días (paralelo) | Diseño UI (parcial) |
| Revisión y aprobación interna del diseño | Equipo completo | 1 día | Diseño UI terminado |

**Entregable:** Diseño final aprobado en Figma + copy final + specs técnicas

**⚠️ Punto crítico:** Diseño y copy deben cerrarse antes de día 9, sino se retrasa todo el desarrollo.

---

## FASE 2: Desarrollo (Días 8-15)

> Empieza en paralelo con el final de la Fase 1 (dev puede ir maquetando con diseño ~80% listo)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Maquetación de secciones principales (hero, features, pricing) | Dev 1 | 4 días | Diseño alta fidelidad |
| Maquetación de secciones secundarias (testimonios, FAQ, footer) | Dev 2 | 3 días | Diseño alta fidelidad |
| Integración de formulario (waitlist / demo request) + CRM/email tool | Dev 2 | 2 días | Maquetación base |
| Responsive (mobile/tablet) | Dev 1 + Dev 2 | 2 días | Maquetación desktop |
| Integración de analytics y eventos de conversión | Dev 1 | 1 día | Maquetación completa |
| Optimización de performance (imágenes, lazy load, Lighthouse) | Dev 2 | 1 día | Desarrollo casi completo |
| Copy final cargado y revisado en contexto real | Copywriter | 1 día | Maquetación avanzada |

**Entregable:** Landing funcional en staging, responsive, con formulario operativo

---

## FASE 3: QA, pulido y pre-lanzamiento (Días 16-18)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| QA cross-browser y cross-device | Dev 1 + Dev 2 | 1 día | Staging listo |
| Revisión de copy (ortografía, tono, consistencia) | Copywriter | 0.5 día | Staging listo |
| Ajustes visuales finales (spacing, alineación, microinteracciones) | Diseñador | 1 día | QA inicial |
| Test de formulario end-to-end (confirmación, emails automáticos) | Dev 2 | 0.5 día | Integraciones listas |
| SEO on-page (meta tags, OG tags, sitemap, alt texts) | Copywriter + Dev 1 | 1 día | Copy final |
| Test de velocidad y Core Web Vitals | Dev 1 | 0.5 día | Optimización hecha |

**Entregable:** Landing en staging aprobada por todo el equipo, sin bugs críticos

---

## FASE 4: Lanzamiento (Días 19-20)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Deploy a producción | Dev 1 | 0.5 día | QA aprobado |
| Verificación post-deploy (links, forms, tracking) | Dev 2 + Diseñador | 0.5 día | Deploy |
| Preparar anuncios (redes, email, comunidad) | Copywriter | 1 día (paralelo con fase 3) | — |
| Go-live oficial | Todo el equipo | Día 20 | Verificación OK |
| Monitoreo primeras 24-48h (errores, conversión) | Dev 1 + Dev 2 | Continuo | Go-live |

---

## Timeline visual (semanas)

```
Semana 1: [Fase 0: Prep/Brief] -------> [Fase 1: Contenido/Diseño inicia]
Semana 2: [Fase 1: Contenido/Diseño termina] -> [Fase 2: Dev inicia]
Semana 3: [Fase 2: Desarrollo completo]
Semana 4: [Fase 3: QA] -> [Fase 4: Lanzamiento]
```

---

## Riesgos y recomendaciones

1. **Cuello de botella en diseño (días 4-9):** si el diseño se retrasa, todo el desarrollo se corre. Mitigación: aprobar wireframe rápido y avanzar con diseño high-fi por secciones (no esperar el 100%).
2. **Copy como bloqueante:** idealmente el copywriter entrega headlines y estructura de texto ANTES del diseño final, no después.
3. **Buffer:** no hay días de colchón en este plan. Recomiendo robar 1-2 días de la Fase 2 (sacrificando alcance, no calidad) como buffer de seguridad antes del lanzamiento.
4. **Daily standups de 15 min** son clave dado lo ajustado del timeline, especialmente entre devs y diseñador en la semana 2-3.
5. **Alcance mínimo viable:** si hay atrasos, las primeras secciones a recortar deberían ser: testimonios (usar placeholders), FAQ extenso, animaciones complejas.

¿Quieres que te arme esto en formato de **Gantt** o como **board de Trello/Notion** con tareas y fechas específicas calculadas desde hoy?