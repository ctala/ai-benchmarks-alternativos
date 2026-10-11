# MiMo V2.6 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 6.97 | quality: 8.0
- latency_total: 773.407s | tokens_per_second: 6.1
- input_tokens: 199 | output_tokens: 4718

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El experimento: "Puerta falsa con precio real" — 7 días, ~$30–105, ~14h

## Antes: qué estás poniendo en juego

Tu hipótesis es en realidad **tres** apuestas apiladas. Un buen test las separa, porque si muere una y no las otras, no sabes qué has aprendido:

| # | Supuesto | Si es falso |
|---|---|---|
| A | El reporting les duele de verdad (≥4h/mes por cliente) | El producto no tiene razón de ser |
| B | Pagarían **$200** (no $50, no $0) | La idea puede vivir, el precio muere |
| C | Pagarían a **un desconocido** en vez de usar AgencyAnalytics/DashThis | Mercado ya tomado |

El error clásico es hacer un test que solo mide A ("¿te duele el reporting?" → todos dicen sí → sigues construyendo). **El precio tiene que estar en pantalla desde el primer minuto.**

---

## Qué haces, día a día

### Día 1–2 — Montar el engaño honesto (4h, $29)

Una sola página en **Carrd ($19)** + dominio ($10) + **link de pago en Stripe ($0)**.

Contenido mínimo, sin mentir sobre que el producto existe todavía:
- 3 bullets de lo que hace: *conecta Google Ads + Meta + GA4 → genera el PDF mensual con tu logo y tus comentarios, listo para enviar al cliente*
- **Precio visible en grande: $200/mes**
- Botón "Empezar ahora — primer mes" → checkout de Stripe de $200
- Nota al pie: *"Beta: 10 plazas. Si en 30 días no te ahorra horas, te devuelvo los $200."*

Ese botón es **el instrumento de medición**. Todo lo demás es decorado.

### Día 1 — Construir la lista (2h, $0)

**150 agencias de 3–25 personas**, filtrables en 2h con LinkedIn Sales Navigator (trial 1 mes) o simplemente Clutch + LinkedIn. Solo agencias de tu idioma/mercado. Guardas email + LinkedIn.

Cualificación dura: que tengan clientes con cuentas de Ads/Social que reportan mensualmente. Nada de "agencias de branding" que no reportan métricas.

### Días 2–6 — Outbound frío (45 min/día, $0)

Secuencia de 3 toques, **sin vender en el mensaje** — solo llevarlos al precio:

- **Email 1:** *"¿Cuántas horas al mes te come el reporte de [Cliente]?"* → 2 líneas + link
- **LinkedIn (día 2):** misma pregunta, 1 mensaje
- **Email 2 (día 5):** *"Pregunta directa: ¿lo reportáis a mano o lo automatizáis?"* → link

**Regla adaptativa:** si al día 4 llevas <30 visitas a la landing, mete **$75 en anuncios de LinkedIn/Meta** segmentados a dueños de agencias en tu mercado. No cambies el mensaje, solo aceleras el tráfico. Necesitas llegar a 100 visitas con precio visible o el test no sirve.

### Días 6–7 — Las llamadas (10 × 20 min, 4h)

Con los que respondan. Guion de **4 preguntas**, en este orden:

1. *¿Cómo entregáis el reporte hoy y quién lo hace?* → cronometra las horas
2. *¿Qué herramienta usáis para esto?* → si dicen AgencyAnalytics/DashThis/Whatagraph, apunta el nombre
3. *¿Cuánto pagáis hoy al mes por herramientas de reporting? ¿Y $200 te parece caro, justo o barato?*
4. **"Tengo el link de pago aquí mismo. ¿Lo abrimos?"** → silencio. Que él hable primero.

---

## Coste y tiempo real

| Concepto | Coste |
|---|---|
| Carrd (1 mes) | $19 |
| Dominio | $10 |
| Stripe / analytics / email / Sales Nav trial | $0 |
| Ads (solo si hace falta acelerar) | $0–75 |
| **Total** | **$29–$105** |

| Fase | Horas |
|---|---|
| Montaje landing + Stripe | 4 |
| Lista de 150 | 2 |
| Outbound (5 días) | 4 |
| Llamadas | 4 |
| **Total** | **~14h en 7 días** |

---

## Los umbrales — escríbelos HOY, antes de enviar el primer email

Esto es lo que hace que el test pueda fallar de verdad. Si los defines después de ver los datos, te autoengañas.

### 🔴 ABANDONAS LA IDEA SI SE CUMPLE CUALQUIERA:

**1. Mueren las compras** (mide A + C a la vez)
> **0 pagos en Stripe de 100 visitas con precio visible**, Y además **<5 peticiones** de "reserva mi plaza / avísame".

Nadie ha sacado la tarjeta ni siquiera para que le reserves sitio. El dolor no es urgente.

**2. Mueren las horas** (mata A)
> **Menos de 8 de 15 llamadas** reportan ≥4h/mes por cliente en reporting.

Si lo hacen en <2h, $200/mes es un ahorro de $100 de trabajo. No cuadra.

**3. Muere el precio** (mata B)
> **10 de 15 llamadas** dicen que $200 es >2× lo que pagan hoy, o ponen su techo en ≤$80.

### 🟢 CONSTRUYES SI:

- **≥2 pagos reales** de Stripe (o ≥5 tarjetas puestas para el depósito), **Y**
- **≥8 de 15 llamadas** confirman ≥4h/mes de dolor, **Y**
- ≤3 dicen "ya lo resuelvo con [competidor]".

Dos pagos reales de frío es una señal brutal. Es más informativa que 50 encuestas de "sí, lo compraría".

---

## Los 3 errores que invalidarían tu test

1. **Poner el precio solo en la llamada.** Si el precio aparece tarde, mides curiosidad, no disposición a pagar.
2. **Cambiar los umbrales en el día 5** cuando ves que vas mal. Es el momento exacto en que no debes hacerlo.
3. **Contar "me gustaría probarlo" como señal positiva.** Es ruido. Solo cuenta la tarjeta y las horas.

---

## Qué NO te va a decir (para que no te confíes si pasa)

- **No valida el producto.** Solo valida que alguien paga por la promesa. Puedes cobrar $200 y que el producto sea una mierda.
- **No valida retención.** El churn a mes 2 es un test distinto y más caro.
- **Un canal frío puede subestimar el dolor.** Si el resultado es gris (ni mata ni valida), el problema es el canal, no la idea — repite con 150 contactos *warm* (ex-colegas, tu red) antes de concluir nada.

---

## La distinción que más te va a servir

Si **muere A** (nadie sufre lo suficiente) → cierra, dedica los 2 meses a otra cosa. Has gastado $50 y una semana.

Si **solo muere B** (el dolor es real pero $200 es inalcanzable) → **no has matado la idea, has matado el precio.** Y eso es un problema muchísimo más barato de resolver: bajas a $79, cambias el packaging a "10 reportes/mes", y vuelves a correr el mismo test por otros $50. No construyas hasta que sepas cuál de los dos ha pasado.

> **El objetivo no es que el test te dé la razón. Es que, cuando falle, te cueste $50 y una semana en vez de dos meses y tu cordial.**