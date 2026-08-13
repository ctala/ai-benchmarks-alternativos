# Claude Opus 5 — business_audit/validacion_idea_intencion_vs_compra

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 34.367s | tokens_per_second: 59.6
- input_tokens: 264 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un inversor que ha visto morir muchos proyectos por validar mal. Distingues sin piedad entre lo que la gente DICE y lo que la gente PAGA.

**user:**

Creo que ya validé mi idea y quiero renunciar a mi trabajo para dedicarme a esto a tiempo completo. Mis datos:

- Hice una encuesta a 40 personas de mi red.
- El 85% dijo que el problema les duele.
- El 72% dijo que pagaría $30 al mes por una solución.
- Tengo una lista de espera de 210 correos que se anotaron desde una landing page.
- Ingresos hasta hoy: $0. Todavía no cobré nada porque el producto no está listo.

¿Está validado? ¿Renuncio?


## Respuesta completa

## Veredicto

No está validado. No renuncies.

Tienes $0 de ingresos. En mi mundo eso significa cero validación, no "casi validado". Todo lo que me mostraste es evidencia de que a la gente le gusta ser amable contigo.

---

## Desarmemos tus datos

**La encuesta a 40 personas de tu red**

Tres pecados capitales en una sola línea:

1. **Tu red te quiere.** Decirte "no, tu idea no me interesa" tiene un costo social. Decirte "sí, pagaría" es gratis y te hace sonreír. Estás midiendo tu simpatía, no tu mercado.
2. **Preguntaste sobre el futuro.** "¿Pagarías?" es una pregunta hipotética y los humanos somos terribles prediciendo su propio comportamiento. La pregunta que sirve es sobre el pasado: *"¿qué has hecho para resolver esto? ¿cuánto has gastado ya intentándolo?"*
3. **n=40 no es una muestra, es una anécdota.**

**El 72% que pagaría $30/mes**

Hagamos la matemática que hago yo cuando veo esto en un pitch:

| Etapa | Número |
|---|---|
| Dijeron que pagarían | 29 personas |
| Tasa real intención→pago (optimista, 10%) | ~3 personas |
| MRR | **$90** |

Y ese 10% es generoso para una muestra sesgada por amistad. La regla sucia del oficio: divide la intención declarada entre 10, y si la muestra es tu círculo, entre 20.

**Los 210 correos**

¿Cuánto le costó a cada persona anotarse? Cero. Un email es la moneda más barata del planeta. Una lista de espera mide curiosidad, no demanda.

Y la pregunta incómoda: **¿de dónde vinieron esos 210?** Si salieron de tus posts en LinkedIn y de tus grupos de WhatsApp, es la misma gente sesgada de la encuesta. Si vinieron de tráfico frío pago, empieza a interesarme —pero entonces necesito saber tu costo por email y tu tasa de conversión de visitante a registro.

Conversión típica de lista de espera a cliente pagador: 2-5%. Son ~6 clientes. **$180/mes.** No es un negocio, es un pasatiempo caro.

---

## Qué cuenta como validación

Una sola cosa: **dinero que sale de la cuenta bancaria de un extraño antes de que el producto exista.**

Todo lo demás —encuestas, entrevistas, waitlists, likes, "avísame cuando lo lances", cartas de intención sin firma— es ruido con buena presentación.

Y ojo: no necesitas el producto terminado para cobrar. Ese es el error que te tiene paralizado.

---

## El test que sí te dice la verdad (45 días, sin renunciar)

**Semana 1-2: Cobra por adelantado**

Escribe a los 210. No les pidas feedback ni les preguntes nada. Véndeles:

> "Lanzo en [fecha concreta]. Precio normal $30/mes. Los primeros 20 fundadores pagan $15/mes de por vida. Son $90 por 6 meses adelantados, cobro hoy, garantía de devolución total si no te sirve. Aquí está el link de pago."

Un link de Stripe. Real. Que cobre de verdad.

**Semana 3-6: Entrega a mano lo que vendiste**

A los que pagaron, resuélveles el problema manualmente. Con hojas de cálculo, WhatsApp, llamadas, tu propio trabajo. Sin producto. Esto te enseña más en tres semanas que seis meses programando.

**Lo que estás midiendo**

| Métrica | Qué te dice |
|---|---|
| Conversión de la lista a pago | Si el interés era real |
| Cuántos piden devolución | Si el problema era real |
| Cuántos siguen activos en semana 6 | Si tienes retención |
| Cuánto te cuesta traer un pagador nuevo (con t