# Claude Opus 5.5 — task_management/project_breakdown

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.92 | quality: 9.8
- latency_total: 67.844s | tokens_per_second: 105.4
- input_tokens: 119 | output_tokens: 7151
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de proyecto: landing page SaaS de gestión de inventario

**Duración:** 4 semanas (20 días hábiles)
**Equipo:** 1 Diseñador (DIS) · 2 Developers (DEV1 frontend, DEV2 integraciones/infra) · 1 Copywriter (COPY) · **PM/Product Owner** (asumo que eres tú; alguien debe aprobar y desbloquear)

---

## 1. Supuestos y decisiones del día 1

Para que el plan funcione, el **día 1** deben quedar definidos estos puntos:

| Decisión | Por qué es crítica |
|---|---|
| **Objetivo y CTA principal** (free trial, demo, waitlist) | Define estructura, copy, formulario e integraciones |
| **KPI de éxito** (ej. tasa de conversión, nº de signups) | Define qué se mide en analytics |
| **Stack** (Next.js/Astro + Vercel, o Webflow/Framer) | Un no-code acelera, un framework da más control |
| **Herramientas** (CRM, email, analytics) | DEV2 necesita accesos desde la semana 1 |
| **Aprobador único** de diseño y copy | Evita ciclos de revisión infinitos |
| **Insumos disponibles**: screenshots del producto, pricing, testimonios o logos de clientes beta, brand guidelines | Si no existen, se convierten en tareas nuevas |

---

## 2. Fases y tareas

### Fase 0: Kickoff (Día 1-2)

| ID | Tarea | Responsable | Duración | Depende de |
|---|---|---|---|---|
| 0.1 | Kickoff: objetivos, audiencia (ICP), CTA, KPIs, alcance | PM + todos | D1 | — |
| 0.2 | Recopilar insumos: features, pricing, screenshots, testimonios, marca | PM | D1-2 | 0.1 |
| 0.3 | Dar accesos: dominio, hosting, CRM, analytics, Figma | PM | D1-2 | 0.1 |

### Fase 1: Estrategia y contenido (Día 1-9)

| ID | Tarea | Responsable | Duración | Depende de |
|---|---|---|---|---|
| 1.1 | Brief de mensaje: dolores del ICP, propuesta de valor, diferenciadores, benchmark de 3-5 competidores | COPY (+DIS) | D1-2 | 0.1 |
| 1.2 | Arquitectura de la página: secciones y orden (hero, problema, solución, features, cómo funciona, social proof, pricing, FAQ, CTA final) | COPY + DIS + PM | D3 | 1.1 |
| 1.3 | Copy v1 de todas las secciones | COPY | D3-5 | 1.2 |
| 1.4 | Revisión y feedback del copy | PM | D6 | 1.3 |
| 1.5 | Copy final + microcopy (formularios, errores, thank-you page, email de confirmación) + meta tags SEO | COPY | D7-9 | 1.4 |

### Fase 2: Diseño (Día 2-12)

| ID | Tarea | Responsable | Duración | Depende de |
|---|---|---|---|---|
| 2.1 | Moodboard y dirección visual | DIS | D2-3 | 0.2 |
| 2.2 | Wireframes desktop + mobile | DIS | D3-5 | 1.2 |
| 2.3 | Revisión de wireframes | PM + DEV1 | D5 | 2.2 |
| 2.4 | UI alta fidelidad desktop (con copy v1 real, sin lorem ipsum) | DIS | D6-9 | 2.3, 1.3 |
| 2.5 | Versión mobile + estados (hover, focus, errores, éxito) | DIS | D9-10 | 2.4 |
| 2.6 | **✅ Aprobación final de diseño** | PM | D10 | 2.5 |
| 2.7 | Assets: mockups del producto, iconos, ilustraciones, OG image, favicon | DIS | D9-12 | 2.4 |

### Fase 3: Desarrollo (Día 2-16)

| ID | Tarea | Responsable | Duración | Depende de |
|---|---|---|---|---|
| 3.1 | Setup: repo, framework, hosting, staging, dominio, SSL, CI/CD | DEV2 | D2-4 | 0.3 |
| 3.2 | Plan de tracking: eventos, conversiones, UTMs, píxeles | DEV2 + PM | D4-5 | 0.1 |
| 3.3 | Base del sistema: tokens (colores, tipografía, espaciado), grid, componentes base | DEV1 | D6-9 | 2.1, 2.4 (parcial) |
| 3.4 | Formulario + integración CRM/email + emails transaccionales | DEV2 | D6-11 | 3.1, 0.3 |
| 3.5 | Maquetación de todas las secciones (responsive) | DEV1 | D10-14 | 2.6 |
| 3.6 | Analytics, banner de cookies (RGPD), SEO técnico (sitemap, robots, schema, OG) | DEV2 | D11-14 | 3.2, 3.1 |
| 3.7 | Integración del copy final y los assets | DEV1 | D13-15 | 1.5, 2.7, 3.5 |
| 3.8 | Páginas legales: privacidad, términos, cookies | DEV2 (contenido: PM/legal) | D14-15 | contenido legal |
| 3.9 | Animaciones y microinteracciones (*nice-to-have*) | DEV1 | D15-16 | 3.5 |
| 3.10 | Design QA: revisión visual sobre staging | DIS | D13-16 | 3.5 |

### Fase 4: QA y optimización (Día 15-18)

| ID | Tarea | Responsable | Duración | Depende de |
|---|---|---|---|---|
| 4.1 | QA funcional cross-browser y dispositivos (Chrome, Safari, Firefox, iOS, Android) | DEV1 y DEV2 cruzados | D16-17 | 3.7 |
| 4.2 | Performance (Lighthouse >90, LCP <2.5s) y accesibilidad (contraste, alt, teclado) | DEV1 | D16-17 | 3.7 |
| 4.3 | Proofreading final sobre la página real | COPY | D16 | 3.7 |
| 4.4 | Test end-to-end de conversión: formulario → CRM → email → evento en analytics | DEV2 + PM | D17 | 3.4, 3.6 |
| 4.5 | Corrección de bugs | DEV1 + DEV2 | D17-18 | 4.1-4.4 |
| 4.6 | **🔒 Code freeze + Go/No-Go** | PM | Fin D18 | 4.5 |

### Fase 5: Lanzamiento (Día 19-20+)

| ID | Tarea | Responsable | Duración | Depende de |
|---|---|---|---|---|
| 5.1 | Deploy a producción + smoke test | DEV2 | D19 | 4.6 |
| 5.2 | Soft launch: compartir con equipo y clientes beta, verificar datos reales | PM | D19 | 5.1 |
| 5.3 | **🚀 Lanzamiento público** | Todos | D20 | 5.2 |
| 5.4 | Monitorización 48-72h (errores, conversiones, velocidad) + hotfixes | DEV2 | D20-22 | 5.3 |

### Track paralelo: materiales de lanzamiento

| ID | Tarea | Responsable | Duración |
|---|---|---|---|
| L.1 | Copy para emails de anuncio, posts en redes y, si aplica, Product Hunt | COPY | D10-15 |
| L.2 | Creatividades para redes y anuncios | DIS | D13-16 |

---

## 3. Timeline visual

```
                  SEMANA 1         SEMANA 2         SEMANA 3         SEMANA 4
                  D1 ─────── D5    D6 ─────── D10   D11 ────── D15   D16 ────── D20
PM         ██ Kickoff/insumos  ▲Rev.WF  ▲Rev.copy  ▲Aprob.diseño          ▲Go/No-Go  🚀
COPY       ████ Brief+Estructura+Copy v1 │██ Copy final │████ Materiales launch │█ Proof
DIS        ██ Mood ████ Wireframes │████████ UI Desktop+Mobile │██ Assets+DesignQA │ Creat.
DEV1       ░░ (apoyo/revisión WF)  │████ Componentes base │████████ Maquetación │██ QA/Fix
DEV2       ████ Setup+Tracking     │████████ Form+CRM │████ Analytics/SEO/Legal │██ QA/Deploy
```

### Hitos semanales

| Fin de… | Hito | Criterio de "hecho" |
|---|---|---|
| **Semana 1** | Estrategia cerrada | Copy v1 + wireframes aprobados + entorno técnico funcionando |
| **Semana 2** | Diseño cerrado | UI desktop + mobile aprobada, copy final listo, formulario conectado al CRM |
| **Semana 3** | Feature complete | Página completa en staging con contenido real, tracking y legales |
| **Semana 4** | Live | QA pasado, en producción, conversiones verificadas |

---

## 4. Ruta crítica

Si alguna de estas tareas se retrasa, **se retrasa el lanzamiento**:

```
Brief (1.1) → Estructura (1.2) → Wireframes (2.2) → Aprobación WF (2.3) → UI hi-fi (2.4/2.5)
→ Aprobación diseño (2.6) → Maquetación (3.5) → Integración contenido (3.7) → QA (4.x) → Launch
```

**El cuello de botella es el diseñador:** es el único recurso sin redundancia y está en la ruta crítica desde el día 2 hasta el día 10. Protege su agenda: nada de tareas ajenas al proyecto durante esas dos semanas.

**Holgura real:** solo hay unos 2 días (D18-19). Las tareas de DEV2 tienen más margen que las de DEV1.

---

## 5. Cómo se reparte la carga

- **DEV1** tiene poco trabajo en la semana 1. Úsalo para revisar los wireframes (viabilidad técnica), montar componentes base desde la dirección visual y prototipar el hero.
- **DEV2** puede adelantar todo lo que no depende del diseño: infraestructura, formulario, CRM, analytics y SEO técnico.
- **COPY** termina el copy principal en la semana 2. Pasa luego a materiales de lanzamiento, que suelen olvidarse hasta el último momento.
- **DIS** no debe esperar al copy final: diseña con el copy v1, que ya es el 80% del contenido.

---

## 6. Priorización del alcance (MoSCoW)

Si hay retrasos, recorta desde abajo:

| Prioridad | Elementos |
|---|---|
| **Must** | Hero + CTA, problema/solución, features clave, formulario funcional, mobile, analytics, legales/cookies |
| **Should** | Social proof, FAQ, pricing, SEO técnico completo, OG images |
| **Could** | Animaciones, video demo, calculadora de ROI, integración de chat |
| **Won't (v1)** | Blog, multi-idioma, A/B testing (pasa a post-lanzamiento) |

---

## 7. Riesgos principales y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Ciclos de feedback largos en diseño/copy | Alta | Alto | Aprobador único, máximo 2 rondas, feedback en 24h |
| No hay screenshots del producto o el producto cambia | Media | Alto | Mockups estilizados en vez de capturas literales, pedirlos en D1 |
| Faltan testimonios o logos | Alta | Medio | Usar métricas de beta, citas de usuarios piloto, o retirar la sección |
| Retraso en accesos (CRM, dominio, DNS) | Media | Medio | Pedirlos en D1. La propagación DNS puede tardar, configurar en semana 1 |
| Textos legales sin redactar | Media | Alto (bloquea el lanzamiento) | Asignar a legal o usar un generador validado desde la semana 2 |
| Scope creep ("¿y si añadimos…?") | Alta | Alto | Todo lo nuevo va a la lista post-lanzamiento |
| El diseñador se enferma o se bloquea | Baja | Crítico | DEV1 puede maquetar desde wireframes y un design system básico |

---

## 8. Ritual de seguimiento

- **Daily de 15 min** (asíncrono por Slack si el equipo lo prefiere): qué hice, qué haré, qué me bloquea.
- **Review semanal los viernes**: verificar el hito de la semana y ajustar el plan.
- **Herramienta**: tablero en Linear, Jira, Trello o Notion con estas tareas y sus dependencias.

---

## 9. Post-lanzamiento (Semana 5+)

- Heatmaps y grabaciones de sesión (Hotjar o Microsoft Clarity)
- Primer A/B test sobre el hero o el CTA
- Análisis del funnel: visitas → scroll → clic en CTA → signup
- Iteración del copy según las objeciones reales de los leads

---

**Recomendación final:** si el día 20 cae en viernes, haz el soft launch el jueves y el lanzamiento público el **martes siguiente**. No conviene lanzar con el equipo fuera durante el fin de semana, y los martes y miércoles suelen tener mejor tráfico B2B.

Puedo convertir esto en una plantilla importable (CSV para Jira/Notion) o detallar la estructura de secciones y el enfoque de copy de la landing.