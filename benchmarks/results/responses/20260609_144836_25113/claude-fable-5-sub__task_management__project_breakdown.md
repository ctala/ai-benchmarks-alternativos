# Claude Fable 5 (suscripción) — task_management/project_breakdown

- model_id: `claude-fable-5`
- success: True  | final: 7.48 | quality: 10.0
- latency_total: 41.598s | tokens_per_second: 75.0
- input_tokens: 2 | output_tokens: 3121

## Respuesta completa

# Plan de lanzamiento: Landing Page SaaS Gestión de Inventario

**Duración:** 4 semanas | **Equipo:** 1 diseñador (D), 2 developers (Dev1, Dev2), 1 copywriter (C)

---

## Fase 1 — Descubrimiento y Estrategia (Semana 1, días 1-3)

| # | Tarea | Responsable | Duración | Dependencias |
|---|---|---|---|---|
| 1.1 | Definir propuesta de valor, ICP y mensaje principal | C + todos (workshop 2h) | 1 día | — |
| 1.2 | Benchmark de 5-8 landings de competidores (Sortly, Cin7, Katana, etc.) | C + D | 1 día | — |
| 1.3 | Definir estructura/wireframe de la página (hero, features, social proof, pricing, FAQ, CTA) | D | 1 día | 1.1 |
| 1.4 | Definir stack técnico y hosting (ej. Next.js/Astro + Vercel/Cloudflare Pages) | Dev1 + Dev2 | 0.5 día | — |
| 1.5 | Setup repo, CI/CD, entorno staging, dominio + DNS + SSL | Dev2 | 1 día | 1.4 |
| 1.6 | Definir métricas de éxito y plan de tracking (conversión, scroll depth, formularios) | Dev1 + C | 0.5 día | 1.1 |

**Entregable:** brief aprobado + wireframe low-fi + repo funcionando con deploy automático.

> ⚠️ Punto crítico: la tarea 1.1 bloquea casi todo. Hacerla el día 1, sin excepción.

---

## Fase 2 — Contenido y Diseño (Semana 1 día 4 → Semana 2)

| # | Tarea | Responsable | Duración | Dependencias |
|---|---|---|---|---|
| 2.1 | Copy v1 completo: hero, beneficios, features, objeciones, FAQ, CTAs | C | 3 días | 1.1, 1.3 |
| 2.2 | Diseño UI hi-fi desktop (sobre el copy real, NO lorem ipsum) | D | 3 días | 1.3, 2.1 parcial |
| 2.3 | Diseño responsive (mobile + tablet) | D | 2 días | 2.2 |
| 2.4 | Assets: screenshots/mockups del producto, ilustraciones, OG image | D | 2 días | 2.2 (en paralelo con 2.3) |
| 2.5 | Copy de emails transaccionales (confirmación de registro/demo/waitlist) | C | 1 día | 2.1 |
| 2.6 | Microcopy: formularios, errores, estados vacíos, meta tags SEO | C | 1 día | 2.2 |
| 2.7 | Componentes base del frontend (design system mínimo: botones, tipografía, grid) | Dev1 | 3 días | 2.2 parcial |
| 2.8 | Backend del formulario: captura de leads → CRM/email tool + validaciones | Dev2 | 3 días | 1.5, 1.6 |

**Entregable:** diseño hi-fi aprobado + copy final v1 + infraestructura de captura de leads lista.

> 💡 Clave de paralelización: los devs NO esperan el diseño final. Dev1 arma componentes con el wireframe; Dev2 trabaja backend que es independiente del diseño.

---

## Fase 3 — Desarrollo e Integración (Semana 3)

| # | Tarea | Responsable | Duración | Dependencias |
|---|---|---|---|---|
| 3.1 | Maquetado de secciones (hero, features, pricing, FAQ) | Dev1 | 3 días | 2.2, 2.3, 2.7 |
| 3.2 | Integración formulario frontend ↔ backend + emails | Dev2 | 1.5 días | 2.8, 3.1 parcial |
| 3.3 | Analytics + pixels (GA4/Plausible, Meta/LinkedIn si hay ads) + eventos de conversión | Dev2 | 1 día | 3.2 |
| 3.4 | SEO técnico: meta tags, OG, schema.org (SoftwareApplication), sitemap, robots.txt | Dev2 | 1 día | 3.1 |
| 3.5 | Animaciones/interacciones y pulido visual | Dev1 + D | 1.5 días | 3.1 |
| 3.6 | Revisión de copy en contexto real (en staging, no en doc) | C | 1 día | 3.1 |
| 3.7 | Performance: imágenes optimizadas, Lighthouse ≥90, Core Web Vitals | Dev1 | 1 día | 3.1, 3.5 |

**Entregable:** landing completa en staging, funcional end-to-end.

---

## Fase 4 — QA, Optimización y Lanzamiento (Semana 4)

| # | Tarea | Responsable | Duración | Dependencias |
|---|---|---|---|---|
| 4.1 | QA cross-browser/dispositivos (Chrome, Safari, Firefox, iOS, Android) | Dev1 + Dev2 | 1.5 días | Fase 3 completa |
| 4.2 | Test end-to-end del funnel: formulario → email → CRM (con datos reales) | Dev2 + C | 0.5 día | 4.1 |
| 4.3 | QA de diseño (pixel review vs Figma) y de copy (typos, consistencia) | D + C | 1 día | 4.1 |
| 4.4 | Correcciones de QA | Dev1 + Dev2 | 1.5 días | 4.1-4.3 |
| 4.5 | Preparar assets de lanzamiento: posts redes, email a lista, Product Hunt si aplica | C + D | 2 días (paralelo) | 2.4 |
| 4.6 | Setup A/B test del hero (si la herramienta lo permite; si no, anotar para post-launch) | Dev1 | 0.5 día | 4.4 |
| 4.7 | **Go-live**: deploy a producción, verificar DNS, analytics, formulario en prod | Dev2 | 0.5 día | 4.4 |
| 4.8 | Monitoreo post-launch 48h: errores, conversión, velocidad | Todos | 2 días | 4.7 |

**Entregable:** landing en producción + kit de distribución listo.

---

## Timeline visual

```
Semana 1: [Estrategia+Wireframe][Copy v1.........][Setup técnico....]
Semana 2: [Diseño hi-fi + responsive + assets][Componentes + Backend leads]
Semana 3: [Maquetado][Integraciones][Analytics+SEO][Pulido]
Semana 4: [QA][Fixes][Assets launch][GO-LIVE jue/vie ❌→ mar/mié ✅][Monitoreo]
```

## Dependencias críticas (camino crítico)

**1.1 → 2.1 → 2.2 → 3.1 → 4.1 → 4.4 → 4.7**

Si algo se atrasa en esta cadena, todo se atrasa. Lo demás tiene holgura.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Copy y diseño en loop infinito de revisiones | Máximo 2 rondas de feedback por entregable, con dueño de decisión definido (1 persona, no comité) |
| No hay screenshots del producto listos | Usar mockups estilizados del UI; el diseñador los prepara en 2.4 |
| Sin social proof (producto nuevo) | Sustituir testimonios por cifras del problema, logos de beta users, o garantía/trial sin tarjeta |
| Scope creep ("agreguemos un blog, un chat...") | Todo lo no esencial para convertir va a backlog post-launch |
| Lanzar un viernes | No. Lanzar martes o miércoles de la semana 4, deja 2-3 días de buffer para imprevistos |

## Recomendaciones finales

1. **Daily de 15 min** los primeros 3 días y luego 3×/semana. Con 4 personas no necesitas más ceremonia.
2. **El buffer real es de ~3 días** en este plan. Protégelo: no lo gastes en semana 1.
3. **Define el CTA único antes que nada**: ¿trial gratis, demo agendada o waitlist? Cambia el copy, el formulario y el backend. Decidirlo tarde es el error más caro de este tipo de proyectos.