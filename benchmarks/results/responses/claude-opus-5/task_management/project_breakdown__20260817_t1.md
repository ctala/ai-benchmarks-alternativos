# Claude Opus 5 — task_management/project_breakdown

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.68 | quality: 9.7
- latency_total: 81.746s | tokens_per_second: 74.5
- input_tokens: 117 | output_tokens: 6088
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de lanzamiento — Landing page SaaS de inventario (4 semanas)

## Supuestos (confírmalos antes del kickoff — cambian el plan)

| Supuesto | Si cambia… |
|---|---|
| Es **una landing page** (1 página larga + legales + gracias), no un sitio de 6 páginas | +1 semana o recortar secciones |
| El CTA principal es **captura de lead / lista de espera o demo**, no self-serve signup con onboarding | Signup + billing = otro proyecto, no cabe en 4 semanas |
| Ya existe producto con UI presentable para screenshots/GIFs | Sin visuales reales, el diseñador tiene que inventar mockups (+3 días) |
| Ya hay dominio, cuenta de hosting y herramienta de email/CRM decididas | Compras y aprobaciones legales suelen comer 3-5 días |
| Stack simple: Next.js/Astro + Tailwind + deploy en Vercel/Netlify + CMS ligero o contenido en repo | Un CMS pesado o WordPress custom cambia el reparto de devs |

**Nomenclatura:** DIS = diseñador · DEV1 = frontend · DEV2 = infra/integraciones · CW = copywriter · PM = tú

---

## Fase 0 — Definición (Días 1-2)

Nada de diseño ni código hasta cerrar esto. Es el 80% del riesgo del proyecto.

| # | Tarea | Resp. | Depende de | Días |
|---|---|---|---|---|
| 0.1 | Kickoff: objetivo, métrica de éxito, alcance congelado | PM + todos | — | 0.5 |
| 0.2 | ICP, propuesta de valor, 3 diferenciadores vs. competencia | CW + PM | 0.1 | 1 |
| 0.3 | Definir CTA único y flujo post-conversión (email, CRM, calendario) | PM | 0.1 | 0.5 |
| 0.4 | Estructura de secciones acordada (wireframe en texto/bloques) | PM + DIS + CW | 0.2, 0.3 | 0.5 |
| 0.5 | Decisiones técnicas: stack, hosting, CMS, herramientas de analítica | DEV1 + DEV2 | 0.3 | 0.5 |

**Hito 1 (fin día 2): alcance y mensaje congelados.** Cambios posteriores entran a backlog post-lanzamiento, no al scope.

Estructura recomendada de secciones (base para estimar): Hero · Problema · Cómo funciona (3 pasos) · Features clave (4-6) · Prueba social · Comparativa o integraciones · Pricing · FAQ · CTA final · Footer.

---

## Fase 1 — Contenido y diseño en paralelo (Días 3-9)

El error clásico es diseñar primero y meter texto después. Aquí el copy va **medio paso adelante**.

| # | Tarea | Resp. | Depende de | Días |
|---|---|---|---|---|
| 1.1 | Copy v1: hero, problema, cómo funciona | CW | 0.4 | 2 (D3-D4) |
| 1.2 | Copy v1: features, pricing, FAQ, CTAs, microcopy de formulario | CW | 1.1 | 2 (D5-D6) |
| 1.3 | Revisión de copy + ajustes | PM → CW | 1.2 | 1 (D7) |
| 1.4 | Wireframes de alta fidelidad (desktop + mobile) | DIS | 0.4 | 2 (D3-D4) |
| 1.5 | Design system mínimo: tipografía, color, botones, espaciado | DIS | 0.5 | 1 (D5) |
| 1.6 | Diseño visual mitad superior (hero → cómo funciona) | DIS | 1.1, 1.5 | 2 (D6-D7) |
| 1.7 | Diseño visual mitad inferior (features → footer) | DIS | 1.2, 1.6 | 2 (D8-D9) |
| 1.8 | Assets: screenshots del producto, iconos, ilustración/gráfico de dashboard | DIS | 1.6 | 1 (paralelo D8) |
| 1.9 | Setup repo, CI/CD, entornos staging/prod, dominio y DNS | DEV2 | 0.5 | 2 (D3-D4) |
| 1.10 | Maquetar sistema de componentes base (botones, grid, tipografía, layout) | DEV1 | 1.5 | 3 (D5-D7) |
| 1.11 | Backend de formulario: validación, anti-spam, envío a CRM/email, página de gracias | DEV2 | 0.3, 1.9 | 3 (D5-D7) |
| 1.12 | Analítica y tracking: GA4/Plausible + eventos de conversión + banner de consentimiento | DEV2 | 1.9 | 2 (D8-D9) |
| 1.13 | Maquetar secciones con copy y diseño ya aprobados (hero → cómo funciona) | DEV1 | 1.6, 1.10 | 2 (D8-D9) |

**Hito 2 (fin día 9): diseño completo aprobado + mitad de la página maquetada + formulario funcionando en staging.**

---

## Fase 2 — Construcción y contenido de soporte (Días 10-14)

| # | Tarea | Resp. | Depende de | Días |
|---|---|---|---|---|
| 2.1 | Maquetar secciones restantes (features → footer) | DEV1 | 1.7, 1.13 | 3 (D10-D12) |
| 2.2 | Responsive y ajuste fino en mobile/tablet | DEV1 + DIS | 2.1 | 1.5 (D13-D14) |
| 2.3 | Micro-interacciones y animaciones on-scroll (solo donde aporten) | DEV1 | 2.1 | 0.5 (D14) |
| 2.4 | SEO técnico: metas, OG/Twitter cards, sitemap, robots, schema, canonical | DEV2 | 2.1 | 1.5 (D10-D11) |
| 2.5 | Optimización: imágenes en WebP/AVIF, lazy load, fuentes, presupuesto de peso | DEV2 | 2.1 | 1.5 (D12-D13) |
| 2.6 | Legales: privacidad, cookies, términos (plantilla + revisión) | PM + CW | 0.3 | 1 (D10) |
| 2.7 | Secuencia de email de bienvenida (2-3 correos) y autorespuesta | CW | 1.11 | 2 (D11-D12) |
| 2.8 | Copy de soporte al lanzamiento: posts sociales, email a lista, Product Hunt si aplica | CW | 1.3 | 2 (D13-D14) |
| 2.9 | Recolectar prueba social real (testimonios, logos, beta users, cifras) | PM | 0.2 | continuo D3-D12 |
| 2.10 | QA de accesibilidad: contraste, foco, alt text, navegación por teclado | DIS + DEV1 | 2.2 | 1 (D14) |

**Hito 3 (fin día 14): página completa en staging, responsive, con legales y analítica.**

---

## Fase 3 — QA, freeze y lanzamiento (Días 15-18)

| # | Tarea | Resp. | Depende de | Días |
|---|---|---|---|---|
| 3.1 | Revisión cruzada completa del equipo + stakeholders (sesión de 90 min) | Todos | Hito 3 | 0.5 (D15) |
| 3.2 | QA cross-browser y dispositivos reales (Chrome, Safari, Firefox, iOS, Android) | DEV1 + DEV2 | 3.1 | 1 (D15) |
| 3.3 | Test end-to-end de conversión: form → CRM → email → gracias → evento en analítica | DEV2 + PM | 3.2 | 0.5 (D15) |
| 3.4 | Corrección de bugs P1/P2 | DEV1 + DEV2 | 3.2 | 1.5 (D16-D17) |
| 3.5 | Lighthouse ≥90 en performance y accesibilidad, Core Web Vitals | DEV2 | 3.4 | 0.5 (D16) |
| 3.6 | **Content freeze** — cero cambios de copy o diseño | PM | 3.1 | fin D16 |
| 3.7 | Checklist pre-lanzamiento (abajo) | PM | 3.4, 3.5 | 0.5 (D17) |
| 3.8 | **Deploy a producción** | DEV2 | 3.7 | 0.5 (D18 mañana) |
| 3.9 | Smoke test en prod + activar campañas y publicaciones | Todos | 3.8 | 0.5 (D18 tarde) |

**Hito 4 (día 18): en vivo.** Lanza **miércoles**, no viernes: te quedan 2 días hábiles para reaccionar con el equipo completo.

---

## Fase 4 — Días 19-20: colchón y post-lanzamiento

Estos dos días **no son buffer de desarrollo**, son la reserva contra imprevistos. Si todo va bien:

- Monitoreo de errores, conversión y comportamiento (heatmap/grabaciones)
- Fixes rápidos de fricción detectada en datos reales
- Definir primer experimento A/B (headline o CTA) para la semana 5
- Retrospectiva de 45 min

---

## Ruta crítica

```
0.2 mensaje → 1.1/1.2 copy → 1.6/1.7 diseño → 1.13/2.1 maquetación → 2.2 responsive → 3.2 QA → 3.4 fixes → 3.8 deploy
```

Todo lo que hace DEV2 (infra, formulario, SEO, performance) está **fuera** de la ruta crítica por diseño: puede avanzar sin esperar al diseño. Si algo se atrasa, el retraso viene del copy o del diseño, no del código.

**El diseñador es el cuello de botella real:** 1 persona con 7 días de trabajo de diseño en 7 días de calendario, sin margen. Mitigación:

- Design system mínimo (1.5), no un sistema completo
- Aprobación por bloques (1.6 y 1.7 separados), no un big-bang al final
- Máximo **2 rondas** de feedback por bloque, cerradas en 24h
- DEV1 empieza a maquetar el día 8 con la mitad superior ya aprobada

---

## Riesgos y mitigaciones

| Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|
| Stakeholders cambian el mensaje en semana 3 | Alta | Alto | Hito 1 firmado + content freeze en D16 documentado |
| No hay prueba social real (producto nuevo) | Alta | Medio | Empezar a pedir testimonios de beta el día 3; plan B: métricas de producto, logos de integraciones, garantía |
| Screenshots del producto no listos o con UI vieja | Media | Alto | Confirmar el día 1 quién los provee y para qué fecha |
| Ciclos de feedback interminables | Alta | Alto | Máx. 2 rondas, 24h de plazo; silencio = aprobado |
| Diseñador enfermo o ausente | Media | Crítico | Plantilla/UI kit comprado como respaldo; diseño en herramienta compartida, nunca local |
| Problemas de DNS/SSL el día del lanzamiento | Media | Alto | Resolver DNS en semana 1 (tarea 1.9), no el día 18 |
| Aprobación legal de textos se atrasa | Media | Medio | Enviar borradores el día 10, no el 16 |

---

## Checklist pre-lanzamiento (tarea 3.7)

- [ ] Formulario probado desde 3 dispositivos distintos; leads llegan al CRM
- [ ] Email de autorespuesta llega y no cae en spam (test con Gmail, Outlook)
- [ ] Eventos de conversión disparando correctamente en analítica
- [ ] Meta title/description y OG image verificados con validador de LinkedIn/Twitter
- [ ] 404 y página de gracias existen y tienen diseño
- [ ] SSL activo, redirección www ↔ raíz, http → https
- [ ] Sin enlaces roto, sin texto placeholder, sin "Lorem"
- [ ] Legales enlazadas desde el footer y accesibles
- [ ] Lighthouse ≥90 mobile en performance y accesibilidad
- [ ] Backup/rollback probado: se puede revertir el deploy en <5 min
- [ ] Alguien de guardia el día 18 hasta el cierre

---

## Carga por persona (días hábiles de 20)

| Persona | Carga | Comentario |
|---|---|---|
| Diseñador | ~9 días | **Ruta crítica, sin holgura.** Protégelo de reuniones |
| DEV1 (frontend) | ~11 días | Concentrada D5-D17 |
| DEV2 (infra) | ~11 días | Distribuida, mucha holgura al inicio |
| Copywriter | ~10 días | Libre desde D15 — úsalo para contenido post-lanzamiento |
| PM | continuo | Tu trabajo real es desbloquear y proteger el freeze |

---

## Recortes si te atrasas (en este orden)

1. Animaciones y micro-interacciones (2.3)
2. Sección comparativa / integraciones
3. FAQ reducida de 8 a 4 preguntas
4. Ilustraciones custom → screenshots directos del producto
5. Secuencia de emails a 1 solo correo de bienvenida

**Nunca recortes:** QA del formulario, tracking de conversión, legales, performance mobile.

---

¿Quieres que profundice en alguno de estos puntos? Puedo detallar la estructura de secciones con el ángulo de mensaje para inventario B2B, el desglose técnico del stack, o convertir esto a un formato importable a Jira/Linear/Notion.