# Claude Opus 5 (suscripción) — task_management/project_breakdown

- model_id: `claude-opus-5`
- success: True  | final: 7.62 | quality: 9.7
- latency_total: 123.481s | tokens_per_second: 67.6
- input_tokens: 2 | output_tokens: 8343
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y práctico del proyecto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Landing SaaS de inventario — plan de 4 semanas

Antes del plan, tres cosas que definen si esto sale bien:

**1. El riesgo no es la landing.** Una landing de 6-8 secciones la construyen 2 devs en 4 días. Lo que se atrasa es: la oferta sin definir, el copy sin aprobar y **los screenshots del producto**. Si el producto no está presentable en la semana 2, el diseñador se bloquea y arrastra a todos.

**2. La ruta crítica es una sola:** `Oferta → Copy → Diseño → Build → QA`. Todo lo demás es paralelo. Cuidar esa línea es cuidar el proyecto.

**3. Lanzas el día 18, no el 20.** Miércoles de la semana 4. Los últimos 2 días son colchón y fixes en caliente, no desarrollo. Nadie lanza un viernes.

**Supuestos que necesito que confirmes o corrijas** (cambian el plan):
- Hay una versión del producto usable para capturar pantallas (aunque sea con datos semilla).
- Existe logo y una base de marca mínima. Si no, súmale 3 días al diseñador.
- El CTA es *trial gratis* o *demo agendada*, no ambos.
- Hay alguien que decide y aprueba en menos de 24h. Sin esto, ninguna estimación se sostiene.

---

## Asignación de roles (importante)

Dos devs en una landing es sobrecapacidad. La división que rinde:

| Rol | Foco |
|---|---|
| **Dev 1 — Frontend** | Maquetado, componentes, responsive, performance, accesibilidad |
| **Dev 2 — Plataforma** | Infra, formularios, CRM, emails, analítica, SEO técnico, **instancia demo con datos semilla** |
| **Diseñadora** | Dirección visual, landing desktop+mobile, mockups de producto, assets sociales y de ads |
| **Copywriter** | Investigación, mensaje, copy de landing, emails post-signup, copy de ads y posts |

Esa "instancia demo con datos semilla" del Dev 2 es la que desactiva el riesgo #1: le da al diseñador pantallas reales y bonitas del producto en la semana 1, no en la 3.

---

## Fase 0 — Descubrimiento y oferta (Días 1-3)

| Tarea | Responsable | Dep. | Duración |
|---|---|---|---|
| Definir ICP y dolor principal (¿bodega? ¿retail multi-sucursal? ¿e-commerce?) | Fundador + Copy | — | 1d |
| 3-5 entrevistas con prospectos o beta users | Copy | ICP | 2d |
| Teardown de 5 competidores (Sortly, inFlow, Katana, Cin7, Zoho Inventory) | Copy + Diseño | — | 1d |
| **Congelar oferta: precio, trial vs demo, CTA único** | Fundador | — | 1d |
| Auditoría de assets: marca, logo, ¿hay producto que mostrar? | Diseño | — | 0.5d |
| Setup: repo, dominio, hosting, CI, entorno staging | Dev 2 | — | 1d |
| Elegir stack y armar esqueleto del proyecto | Dev 1 | — | 1d |
| **Instancia demo con datos semilla creíbles** (SKUs, bodegas, alertas de stock) | Dev 2 | — | 1.5d |

> **Gate 1 — fin del día 3:** oferta y CTA congelados por escrito. Si esto se mueve después, se mueve todo. No es negociable.

---

## Fase 1 — Mensaje y copy (Días 3-7)

| Tarea | Responsable | Dep. | Duración |
|---|---|---|---|
| Messaging house: promesa, 3 pilares, pruebas | Copy | Gate 1 | 1d |
| Estructura de secciones + wireframe de baja fidelidad | Copy + Diseño | Messaging | 1d |
| Copy v1 completo (hero, problema, cómo funciona, beneficios, prueba social, precios, FAQ, CTA) | Copy | Wireframe | 2d |
| Revisión y **copy v2 congelado** | Fundador + Copy | Copy v1 | 1d |
| *Paralelo:* design system base (tokens, tipografía, componentes) | Dev 1 | Stack | 2d |
| *Paralelo:* analítica (GA4 + PostHog), píxeles, staging protegido | Dev 2 | Setup | 2d |

> **Gate 2 — fin del día 7:** copy v2 aprobado. **No se diseña sobre texto de relleno.** Diseñar con *lorem ipsum* garantiza rehacer el diseño cuando llegue el texto real.

---

## Fase 2 — Diseño (Días 6-11)

| Tarea | Responsable | Dep. | Duración |
|---|---|---|---|
| Moodboard y dirección visual | Diseño | Wireframe | 1d |
| Mockups de producto desde la instancia demo | Diseño | Instancia demo | 1.5d |
| Diseño desktop completo | Diseño | Gate 2 | 3d |
| Adaptación mobile | Diseño | Desktop | 1d |
| OG image, favicon, assets sociales | Diseño | Dirección visual | 0.5d |
| Entrega a desarrollo con specs | Diseño | Mobile | 0.5d |

**Truco de agenda:** que la diseñadora entregue el **hero aprobado el día 9**, antes que el resto. Dev 1 arranca el maquetado dos días antes y le quita presión a la semana 3.

> **Gate 3 — fin del día 11:** diseño aprobado. Desde acá, cualquier sección nueva sale del alcance.

---

## Fase 3 — Construcción (Días 9-16)

| Tarea | Responsable | Dep. | Duración |
|---|---|---|---|
| Maquetado hero y above-the-fold | Dev 1 | Hero aprobado (d9) | 1.5d |
| Resto de secciones | Dev 1 | Gate 3 | 3d |
| Responsive y cross-browser | Dev 1 | Secciones | 1d |
| Performance: imágenes modernas, lazy load, Lighthouse ≥90 | Dev 1 | Maquetado | 1d |
| Formulario de captura: validación, estados, errores | Dev 2 | Diseño form | 1.5d |
| Integraciones: CRM, email de bienvenida, notificación a Slack | Dev 2 | Formulario | 1.5d |
| SEO técnico: metas, schema (SoftwareApplication + FAQPage), sitemap, robots | Dev 2 | Copy v2 | 1d |
| Página de gracias + evento de conversión | Dev 2 | Formulario | 0.5d |
| Legales: privacidad, términos, banner de cookies | Dev 2 + Copy | — | 0.5d |

> **Gate 4 — día 16: feature freeze.** Después de este punto solo se corrigen errores. Cualquier idea nueva va a una lista de "semana 5".

---

## Fase 4 — QA y munición de lanzamiento (Días 15-18)

| Tarea | Responsable | Dep. | Duración |
|---|---|---|---|
| QA funcional en matriz de dispositivos y navegadores | Todos | Build | 1d |
| QA de contenido: erratas, enlaces, consistencia de precios | Copy | Build | 0.5d |
| **Prueba end-to-end del embudo**: form → CRM → email → gracias → evento en analítica | Dev 2 | Integraciones | 0.5d |
| Accesibilidad básica: contraste, alt, foco, semántica | Dev 1 | Build | 0.5d |
| Secuencia de 4 emails post-registro | Copy | Copy v2 | 2d |
| Creativos y copy de ads (si hay pauta) | Diseño + Copy | Dirección visual | 2d |
| Posts de lanzamiento (LinkedIn, X, Product Hunt) | Copy | — | 1d |
| Checklist pre-launch: quitar `noindex`, DNS, SSL, backups | Dev 2 | Gate 4 | 0.5d |

---

## Fase 5 — Lanzamiento (Día 18) + colchón (19-20)

| Tarea | Responsable | Momento |
|---|---|---|
| Deploy a producción + smoke test | Dev 2 | Día 18, 9:00 |
| Publicación de posts, emails y ads | Copy | Día 18, 11:00 |
| Guardia de monitoreo primeras 24h | Dev 1 + Dev 2 | Día 18-19 |
| Ronda de fixes en caliente | Dev 1 | Día 19 |
| Revisión de métricas y primeras hipótesis de mejora | Todos | Día 20 |

---

## Timeline visual

```
              SEM 1          SEM 2          SEM 3          SEM 4
              D1..D5        D6..D10       D11..D15      D16..D20
Oferta/Desc.  ███──────
Copy            ──█████
Diseño              ─██████████
Build                    ─████████████──
QA                                  ─██████
Emails/Ads                          ─██████
Lanzamiento                                    ▲D18  ░░ colchón

Gates:          ▲G1(d3)  ▲G2(d7)   ▲G3(d11)  ▲G4(d16)
```

---

## Carga por persona (dónde está el cuello)

| | Sem 1 | Sem 2 | Sem 3 | Sem 4 |
|---|---|---|---|---|
| **Diseño** | Baja | **Saturada** | Media | Media |
| **Copy** | **Saturado** | Media | Baja | **Saturado** |
| **Dev 1** | Media | Media | **Saturado** | Media |
| **Dev 2** | Media | Media | Alta | Media |

La semana 2 la diseñadora es el único cuello de botella del proyecto. **Protégele la agenda:** sin reuniones, sin pedidos de assets para redes, sin "aprovechando, ¿me haces el pitch deck?". Cada interrupción en esa semana atrasa el lanzamiento un día.

---

## Riesgos reales y qué hacer

| Riesgo | Prob. | Mitigación |
|---|---|---|
| El producto no está presentable para capturas | **Alta** | Instancia demo con datos semilla en semana 1 (Dev 2). Plan B: mockups ilustrados de la interfaz |
| La oferta o el precio cambian en semana 3 | Media | Gate 1 firmado. Si cambia, se mueve la fecha de lanzamiento — se dice en voz alta el mismo día |
| Aprobaciones lentas del fundador | **Alta** | Regla de 24h: sin respuesta, se avanza con la propuesta del equipo |
| Cero prueba social (sin clientes aún) | Alta | Sustituir con: logos de integraciones, cifras del beta, garantía, capturas del producto |
| Alcance que crece ("agreguemos un blog") | **Alta** | Lista "semana 5" visible. Nada entra después del día 16 |
| Copy genérico de SaaS ("optimiza tu inventario") | Media | Las entrevistas de la fase 0 son obligatorias. El copy sale del lenguaje del cliente, no del equipo |

---

## Si se atrasan, esto se corta (en este orden)

1. Animaciones y micro-interacciones
2. Ilustraciones personalizadas → banco de imágenes o capturas
3. Posts de blog y contenido SEO → semana 5
4. Test A/B del hero → semana 5
5. Video demo → semana 6
6. Página de precios separada → sección dentro de la landing
7. Tour interactivo del producto → semana 6

**Lo que nunca se corta:** formulario funcionando, embudo instrumentado, mobile, velocidad de carga.

---

## Definición de "lanzado"

No es "la página está arriba". Es:

- [ ] Formulario probado end-to-end desde 3 dispositivos distintos
- [ ] El lead llega al CRM y recibe el email de bienvenida en menos de 2 minutos
- [ ] Evento de conversión disparando en GA4 y en el píxel
- [ ] Lighthouse ≥90 en mobile
- [ ] Legales publicados y enlazados
- [ ] OG image correcta al compartir en LinkedIn, WhatsApp y X
- [ ] `noindex` retirado, sitemap enviado a Search Console
- [ ] Alguien de guardia las primeras 24h

---

## Qué medir desde el día 1

Una landing sin instrumentación es un volante caro. Mínimo:

| Métrica | Para qué |
|---|---|
| Visitantes únicos por fuente | Saber qué canal trae gente |
| Scroll depth por sección | Dónde abandonan (casi siempre justo después del hero) |
| Clics en CTA / visitantes | Si el mensaje convence |
| Registros completados / clics en CTA | Si el formulario tiene fricción |
| **Registros / visitantes** | El número que importa. Benchmark SaaS B2B: 2-5% |

Dos semanas después del lanzamiento tendrás datos para la primera iteración real. Ahí es donde se gana, no en el día 18.

---

**Lo primero que haría hoy:** sentarte 2 horas con el copywriter a cerrar la oferta y el CTA único. Todo lo demás depende de eso, y es la decisión que más se posterga.

¿Quieres que profundice en alguna fase, o armo la estructura de secciones y el ángulo de mensaje para una landing de gestión de inventario?