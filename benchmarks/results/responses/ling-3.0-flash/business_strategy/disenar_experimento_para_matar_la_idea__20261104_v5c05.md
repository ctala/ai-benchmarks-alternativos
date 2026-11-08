# Ling 3.0 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 7.62 | quality: 8.0
- latency_total: 85.052s | tokens_per_second: 33.5
- input_tokens: 225 | output_tokens: 2845

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento para MATAR tu hipótesis

## La idea central

No construyes nada. Creas una **landing page falsa** con un botón de "Comprar" que mida si alguien está dispuesto a **desembolsar plata real** (aunque sea $1) por tu herramienta. Si nadie paga, estás equivocado.

---

## Qué hacer — paso a paso

### 1. Construye una landing page de "producto" (1 noche)

Usa Carrd, Webflow, o incluso Notion publico. Contenido:

- **Headline**: "Automatiza los reportes a tus clientes en 2 minutos"
- **Precio visible**: **$200/mes** (con subtítulo: "Sin contratos, cancela cuando quieras")
- **3 bullets** de beneficio (no de feature)
- **Una demo visual** (pantallazo o GIF de un reporte bonito — lo puedes hacer a mano en Canva/Google Sheets)
- **FAQ**: "¿Cómo empiezo?", "¿Qué agencias usan esto?", "¿Puedo cancelar?"
- **CTA**: Botón **"Reservar mi lugar — $200/mes"**

Al botón lo conectas a un **formulario de Stripe Checkout** o **Lemon Squeezy** con un cargo real de **$1 como depósito de reserva**. Ese $1 es el dato que te salva la vida.

> **Si alguien paga $1 por reservar un lugar en una lista de espera para pagar $200/mes, su intención de compra es real.**

### 2. Consigue tráfico donde están tus clientes (1-2 horas de trabajo)

No necesitas un presupuesto publicitario grande. Opciones en orden de costo:

| Canal | Acción | Costo |
|---|---|---|
| **Grupos de Facebook/WhatsApp** de dueños de agencias | Publica como si fuera un lanzamiento real: "Estoy construyendo X, les cobro $200/mes, si quieren reservar su lugar aquí está el link" | $0 |
| **LinkedIn personal** | Post contundente: "Estoy a punto de lanzar una herramienta que cobro $200/mes. Si eres dueño de una agencia y quieres ahorrarte 5 horas semanales en reportes, reserva tu lugar por $1" | $0 |
| **Reddit** (r/smallbusiness, r/marketing, subreddits de agencias) | Mismo enfoque, adaptado al formato | $0 |
| **Ads Facebook/Instagram** | Segmenta: dueños de agencias, marketing, small business. $100 de presupuesto | $100 |

### 3. Métricas que importan

- **Métrica primaria**: % de visitantes que pagan $1 para reservar
- **Métrica secundaria**: % de visitantes que hacen clic en "Reservar" (muestra interés superficial)
- **Métrica de contexto**: ¿Quiénes son los que interactúan? ¿Son reales dueños de agencias o curiosos?

### 4. Duración

**10-14 días**. No más. Si en 2 semanas con tráfico dirigido no logras ni una sola reserva de $1 de alguien que realmente parece dueño de agencia, no necesitas más datos.

---

## Presupuesto total

| Item | Costo |
|---|---|
| Landing page (Carrd) | $0-$19 |
| Stripe Checkout / Lemon Squeezy | $0 |
| Tu tiempo (1 noche + 1-2 horas) | Tu costo horario × ~8 hrs |
| Ads opcionales | $100 |
| **TOTAL** | **$0 - $120** (sin contar tu tiempo) |

---

## Resultado que te hace ABANDONAR la idea

🚩 **Mata la hipótesis si:**

1. **0 reservas de $1** de personas que identifiques como dueños/gestores de agencias pequeñas en 14 días.
2. **Tasa de clic en "Reservar" < 2%** del tráfico que llega (demuestra que el precio es un muro).
3. **Los que hacen clic no son tu ICP** (son freelancers, estudiantes, gente curiosa — no agencias con necesidad real).
4. **Los que preguntan "¿cómo funciona?" nunca completan el pago de $1** (demuestra que el interés se evapora al ver el precio).

### Si solo hay clics pero 0 pagos → estás en el limbo

Eso te dice que hay interés pero no disposición a pagar $200. No es una muerte concluyente, pero sí te dice que necesitas revalidar el precio ($50? $99?) o el ICP (¿quizás agencias medianas, no pequeñas?).

---

## Por qué este experimento funciona

- **Es concluyente**: plata real vs. curiosidad. La gente miente en encuestas ("sí, pagaría") pero paga con su tarjeta.
- **Es barato**: no construyes código, no diseñas UI, no integras APIs.
- **Es rápido**: 14 días vs. 2 meses de desarrollo.
- **Te protege**: si la hipótesis sobrevive (al menos 3-5 reservas de $1 de ICP real), entonces SÍ vale la pena construir. Si no, ahorraste 8 semanas y $30k en desarrollo.

---

## Lo que NO debes hacer

- ❌ Encuestas de "¿pagarías $200?" — la gente dice que sí y no paga.
- ❌ Interviews sin mostrar precio — no son datos de disposición a pagar.
- ❌ Construir MVP primero — 2 meses es demasiado tiempo para aprender algo que puedes aprender en 2 semanas por $100.
- ❌ Medir "likes" o "me gusta" en redes — engagement ≠ intención de compra.

---

**Tu asignación esta semana**: landing page + $1 de depósito + tráfico orgánico. Arranca el lunes. A más tardar el viernes siguiente tienes tu respuesta.