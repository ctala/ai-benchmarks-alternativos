# MiMo V2.6 Pro — business_audit/teardown_competidor_sin_inventar

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 2.72 | quality: 2.0
- latency_total: 251.9s | tokens_per_second: 35.6
- input_tokens: 203 | output_tokens: 8959

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa

# TEARDOWN DEL COMPETIDOR
## Comunidad de pago sobre automatización · $39/mes · 2.400 miembros

---

## 0. Marco de certeza

Antes de los números: de los 6 datos que me diste, **todos son hechos observados**. Todo lo demás que vas a leer es inferencia. Lo marco explícitamente.

| Etiqueta | Significado |
|---|---|
| **[HECHO]** | Lo que viste en la página pública |
| **[INF-ALTA]** | Patrón típico del sector, probabilidad >75% |
| **[INF-MEDIA]** | Probabilidad 40-75% |
| **[INF-BAJA]** | Escenario alternativo, <40% |

**Dato faltante crítico:** no sabemos si "2.400 miembros" es *suscriptores que pagan hoy* o *acumulado histórico de registros*. Eso cambia la facturación en un factor 2x. Lo trato con escenarios.

---

## 1. ¿Cuánto factura?

### 1.1 Descomponiendo el número "2.400"

**[HECHO]** La portada muestra 2.400 miembros.

**[INF-ALTA]** En plataformas tipo Skool / Circle / Kajabi / Whop, ese número suele ser el **total de miembros del grupo**, incluyendo trials, planes gratuitos y cancelados que nunca se purgan. Solo en comunidades puramente de pago (sin tier free) se acerca al número real de suscriptores activos.

Dos lecturas posibles:

| Lectura | Qué implica | Miembros pagando hoy | MRR | ARR |
|---|---|---|---|---|
| **A: Acumulado histórico** | 35-65% son pagos activos | 840 – 1.560 | **$32.800 – $60.800** | **$393k – $730k** |
| **B: Suscriptores activos** | 85-95% son pagos activos | 2.040 – 2.280 | **$79.500 – $88.900** | **$954k – $1,067k** |
| **Techo literal** | 100% pagan | 2.400 | $93.600 | $1.123k |

**→ Estimación central: $50k-70k MRR · $600k-840k ARR brutos.** **[INF-MEDIA]**

### 1.2 Descuentos obligatorios

**[INF-ALTA]** A esa cifra bruta hay que restar:

| Concepto | Impacto estimado |
|---|---|
| Procesamiento de pago (Stripe/PayPal) | 3-5% → **−$2k a −$4k/mes** |
| Reembolsos / chargebacks (info-productos) | 1-3% → **−$1k a −$2k/mes** |
| Comisión de plataforma | Variable: Skool ~$99/mes fijo; Circle/Kajabi 0-5%; marketplaces 3-10% |
| Impuestos a ventas / VAT si venden B2C | Puede ser trasladado al cliente o absorberse |

**[INF-MEDIA]** Margen bruto típico de este modelo: **75-85%** si el equipo es el fundador + 1-2 freelancers.

**[INF-BAJA]** Si hay 3-5 empleados (editores, moderadores, soporte), margen operativo cae a **45-60%** → beneficio neto de **$25k-45k/mes**.

### 1.3 Lo que NO podemos saber desde fuera

**[HECHO]** No se ve plan anual ni descuentos.

**[INF-ALTA]** Si efectivamente no lo ofrecen, significa:
- **Ingreso 100% mes a mes** → sin cash por adelantado, sin colchón
- **Churn se traduce directo en caída de ingreso** (no hay anual "protegiendo")
- **LTV con techo claro**: 12 meses × $39 ≈ **$468** por miembro

**[INF-BAJA]** Es posible que exista un upsell no visible (mentorías $500-2.000, implementación done-for-you) que esté inflando el ticket real. Habría que mirar el checkout y el email de bienvenida.

---

## 2. ¿Qué tan sano está el negocio?

### 2.1 Lo que luce sólido

| Dimensión | Señal | Certeza |
|---|---|---|
| Modelo | Suscripción recurrente = ingreso predecible | **[INF-ALTA]** |
| Cadencia | 3 posts/semana constante = retención + coste marginal bajo | **[INF-ALTA]** |
| Tracción | 2.400 miembros en nicho de automatización es señal de demanda real, no vanity | **[INF-MEDIA]** |
| Precio | $39/mes es sweet spot: accesible para B2C, sin fricción para B2B-pyme | **[INF-MEDIA]** |
| Producto | 12 cursos listados = alta percepción de valor | **[INF-ALTA]** |

### 2.2 Lo que es riesgo

| Riesgo | Impacto | Certeza |
|---|---|---|
| **Dependencia de un solo canal** (audiencia personal del fundador, 60k) | **ALTO** — si el algoritmo cambia o él se quema, se corta la adquisición | **[INF-ALTA]** |
| **12 cursos con estado desconocido** | **MEDIO-ALTO** — cursos a medias es la causa #1 de churn en info-productos | **[INF-MEDIA]** |
| **Un solo tier de precio** | **MEDIO** — sin upsell, el LTV tiene techo duro | **[INF-ALTA]** |
| **Sin plan anual** | **MEDIO** — sin cash adelantado ni reducción estructural de churn | **[INF-ALTA]** |
| **Key-person risk** | **ALTO** — "la comunidad de [fundador]" no es transferible ni vendible | **[INF-MEDIA]** |
| **Posible pico de miembros** | **BAJO-MEDIO** — 2.400 podría ser máximo histórico, no actual | **[INF-BAJA]** |

### 2.3 Unit economics estimados

**[INF-MEDIA]** Si la adquisición es orgánica desde audiencia del fundador:

```
CAC efectivo:        $2 – $10  (coste de contenido, no ads)
Churn mensual típico: 6 – 10%  (comunidades de contenido)
Vida media:          10 – 16 meses
LTV bruto:           12 meses × $39 = $468
LTV neto:            ~$400 – $420 tras fees y refunds
LTV:CAC:             > 40x  → altamente rentable
```

**[INF-MEDIA]** PERO: el momento en que escalen con paid ads (y tendrán que hacerlo para salir de la dependencia del fundador), el CAC sube a **$80-200** y el ratio cae a **2-5x**. Sigue siendo sano, pero el margen cambia estructuralmente y eso abre una ventana de ataque para ti.

### 2.4 Veredicto

> **Salud: 7/10.** Negocio rentable, predecible, con márgenes altos y demanda validada. Pero estructuralmente frágil: concentración en un canal, una persona, un tier de precio y sin anual. Es el clásico *"negocio bueno, activo malo"* — difícil de vender, fácil de copiar por un competidor más enfocado.

---

## 3. Cómo competir

### 3.1 Dónde NO competir

| ❌ Evitar | Por qué |
|---|---|
| Volumen de cursos | Ellos ya tienen 12 listados |
| Precio más bajo | Guerra de precios te destruye primero a ti |
| Tamaño de audiencia | 60k seguidores no se iguala rápido |
| Copiar formato "3 posts/semana" | Estás jugando su juego |

### 3.2 Vectores de ataque

**A) Profundidad sobre amplitud** · **[INF-ALTA]**
Si sus 12 cursos están a medias (probable), tu oferta: **3-4 cursos 100% terminados + acompañamiento en implementación.**
Comunica: *"Menos promesas, más entregas terminadas."*
Esto convierte su punto más débil en tu punto más fuerte sin que ellos puedan responder rápido (cerrar 12 cursos les toma meses).

**B) Verticalización** · **[INF-ALTA]**
"Automatización" es horizontal y genérica. Gana un subsegmento:
- Automatización para **agencias de marketing**
- Automatización para **e-commerce**
- Automatización para **despachos contables / fiscal**
- Automatización para **inmobiliarias**
- Automatización para **clínicas / salud**

> **Un nicho de 500 personas pagando $99/mes > 2.400 genéricos pagando $39.**
> (500 × 99 = $49.500 MRR vs. 2.400 × 39 = $93.600 MRR — pero el nicho convierte 5-10x mejor, retiene mejor y compite contra cero.)

**C) Arquitectura de precios** · **[INF-ALTA]**
Introduce lo que ellos no tienen visible:

| Tier | Precio | Qué incluye |
|---|---|---|
| **Base** | $39-49/mes · $390-490/año | Comunidad + cursos |
| **Pro** | $99-149/mes | + plantillas, sesiones grupales, revisión de workflows |
| **Done-with-you** | $300-500/mes o proyecto | + implementación 1:1 |
| **Fundador (limitado)** | $29/mes de por vida | Early adopters, escasez real |

El plan anual con 2 meses gratis **reduce churn 30-50%** y **mejora tu cash flow** — dos cosas que ellos no están haciendo.

**D) Cambia la conversación: de contenido a resultado** · **[INF-MEDIA-ALTA]**
Automatización tiene ROI cuantificable. Ellos venden cursos. Tú vendes: **"Te devolvemos 20 horas/mes o te devolvemos el dinero."**
Esto te saca del ring de "quién tiene más videos" y te pone en el de "quién me resuelve el problema".

**E) Diversifica canales desde el día 1** · **[INF-MEDIA]**
Ellos dependen del fundador. Tú desde el principio:
- **SEO programático** (comparaciones, "alternativas a X", plantillas)
- **YouTube** (el nicho de automatización tiene demanda estructural de tutorial)
- **Partnerships con tool-makers** (Zapier, Make, n8n, Airtable, Notion → programas de partners/escuelas)
- **Marketplace de comunidades** (Whop, Skool Discovery) — tráfico frío que ellos no están usando

**F) Comunidad curada sobre comunidad grande** · **[INF-MEDIA]**
2.400 miembros es más ruido que valor para muchos. Tú: aplicación de ingreso, filtro por perfil, onboarding personalizado. Comunica: *"Cerramos a 200 miembros activos, no a 2.000 suscriptores."* Sube percepción de exclusividad, baja churn por "nadie responde".

---

## 4. Playbook de entrada (primeros 12 meses)

| Fase | Objetivo | Métrica |
|---|---|---|
| **Semanas 1-2** | Elegir vertical + promesa de resultado medible | 1 nicho, 1 promesa |
| **Semanas 3-6** | Lanzar 1 curso completo + comunidad abierta + precio fundador | 20-30 miembros |
| **Semanas 7-12** | Validar con casos reales (horas ahorradas documentadas) | **100 miembros pagando** |
| **Mes 4-6** | Tier Pro + plan anual + primer canal de adquisición pagado | 300 miembros |
| **Mes 7-12** | Diversificar canales (SEO/YouTube/partners) + 2º curso terminado | 500-800 miembros |

**Hitos críticos:**
- **100 miembros** = validación real
- **300 miembros** = puedes contratar soporte/editar
- **500 miembros** = igualas su MRR probable con un nicho, a menor coste de soporte

---

## 5. Cómo responder si te atacan

**[INF-MEDIA]** Lo más probable: cuando te vean, bajen precio o lancen "plan VIP". Prepara desde ya:

| Su jugada | Tu contra |
|---|---|
| Bajan precio a $29/mes | Sube a $49 con ROI demostrado. El precio barato refuerza tu narrativa de "más seriedad" |
| Lanzan "academia VIP" | Ya tienes tiers. Muestra casos de resultado, no promesas de más contenido |
| Aumentan cursos | Sigue en profundidad: *"Tienen 25 cursos, tenemos 4 que se terminan"* |
| Copian tu nicho | Ya tienes comunidad vertical establecida. La comunidad es el moat, no el contenido |

---

## 6. Datos que necesitas para afinar este análisis

1. **Wayback Machine** → ¿2.400 subió o bajó en 6 meses? Distingue crecimiento de pico.
2. **Meta Ads Library + Google Ads Transparency** → ¿Están corriendo ads? Si sí, su CAC es $80-200 y la dependencia del fundador es menor de lo que parece.
3. **Reviews en Trustpilot, Reddit, Twitter** → Busca menciones de churn, cursos incompletos, "no lo vale".
4. **Checkout (Wayback o incógnito)** → ¿Descuento anual escondido? ¿Upsell post-compra?
5. **LinkedIn del fundador** → ¿Equipo visible? Contradice la tesis de "one-person show".
6. **Plataforma usada** (Skool vs Circle vs Kajabi vs Whop) → Determina comisión real y si el número de miembros es público o privado.

---

## Resumen ejecutivo

| Pregunta | Respuesta | Certeza |
|---|---|---|
| **¿Cuánto factura?** | **$600k – $840k ARR brutos** (~$50-70k MRR) | **[INF-MEDIA]** |
| **¿Cuánto se queda?** | Margen bruto 75-85%, neto probable $25-50k/mes | **[INF-MEDIA]** |
| **¿Está sano?** | **7/10** — rentable pero frágil (1 canal, 1 persona, 1 tier) | **[INF-MEDIA]** |
| **¿Cómo gano?** | Vertical + profundidad + pricing arquitectura + resultado medible + multi-canal | **[INF-ALTA]** |
| **¿Dónde es vulnerable?** | Cursos a medias, sin anual, dependencia del fundador | **[INF-ALTA]** |

**Mi lectura estratégica final:** no compitas con ellos de frente. Compites contra su **estructura**, no contra su contenido. Ellos tienen tracción y eso es respetable — pero están expuestos en exactamente los cuatro lugares donde un entrante enfocado puede construir ventaja en 12 meses: nicho, profundidad, precios y canales.