# Claude Opus 5.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.65 | quality: 8.0
- latency_total: 39.761s | tokens_per_second: 83.8
- input_tokens: 291 | output_tokens: 3330

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento para matar la hipótesis en 10 días

**Costo:** $0–$50 · **Tiempo:** 7–10 días · **Resultado:** dinero real o abandono

## Primero: descompón la hipótesis

Tu frase contiene 4 apuestas. Basta con que **una** sea falsa para que la idea muera:

1. Las agencias pequeñas sienten el dolor de los reportes (pierden horas reales).
2. No lo tienen ya resuelto. **Ojo:** existen AgencyAnalytics, DashThis, Whatagraph, Swydo y Looker Studio, que es gratis.
3. Pagarían **$200/mes**, no $30.
4. Puedes llegar a ellas a un costo razonable.

La más peligrosa es la #2 combinada con la #3: el problema existe, pero ya hay soluciones baratas. El experimento ataca eso directamente.

---

## Día 0 (1 hora, $0): el filtro de escritorio

Antes de hablar con nadie:

- Revisa los precios actuales de los 4–5 competidores (rondan entre ~$50 y ~$300/mes según el plan; verifícalo).
- Lee las reseñas de 1–3 estrellas en G2 y Capterra. Busca quejas repetidas.

**Criterio de muerte temprana:** si no encuentras **ninguna queja recurrente** que tu herramienta resolvería, no tienes un argumento para cobrar $200 cuando existe algo similar por $60. Para y replantea antes de gastar más tiempo.

Si encuentras un hueco claro (por ejemplo, "los reportes siguen requiriendo que yo escriba el análisis a mano"), ese hueco es tu propuesta. Úsalo en el paso siguiente.

---

## Escribe los criterios de muerte AHORA, antes de empezar

Escríbelos y compártelos con alguien. Si los defines después, vas a racionalizar cualquier resultado.

| Etapa | Mata la idea si... |
|---|---|
| Contacto (100 agencias) | Menos de **10** aceptan una llamada de 20 min |
| Llamadas | Menos de la mitad dedica **más de 5 h/mes** a reportes |
| Llamadas | La mayoría ya usa una herramienta y está satisfecha |
| **Pago (la definitiva)** | Menos de **3** pagan el primer mes por adelantado |

---

## Días 1–2: la lista ($0)

Arma una lista de **100 agencias de 2 a 15 personas**. Fuentes: LinkedIn (cuenta de prueba gratis de Sales Navigator), Clutch.co y Google Maps buscando "agencia marketing digital [ciudad]". Contacta directamente al dueño o fundador; en agencias de ese tamaño, es quien sufre y paga los reportes.

## Días 2–3: landing de una página (~$20)

Usa Carrd o similar, con un dominio barato. Debe incluir:

- Una sola promesa concreta (el hueco que encontraste el Día 0).
- **El precio visible: $200/mes.** No lo escondas; el precio es justamente lo que estás probando.
- Un botón: "Ser cliente fundador", que lleva a un link de pago de Stripe.

## Días 3–8: contacto y llamadas

Mensaje corto, sin pitch:

> "Hola [nombre], estoy investigando cómo las agencias pequeñas hacen los reportes mensuales a clientes. ¿Me das 20 min esta semana? No vendo nada todavía."

**En la llamada, pregunta solo por el pasado, nunca por el futuro:**

- "¿Cuándo fue la última vez que armaste un reporte? Cuéntame paso a paso qué hiciste."
- "¿Cuántas horas te tomó este mes, sumando todos los clientes?"
- "¿Qué herramientas usas hoy? ¿Cuánto pagas?"
- "¿Has buscado algo para resolver esto? ¿Por qué no te quedaste con eso?"

No preguntes "¿pagarías por...?". Todos dicen que sí y nadie paga.

**Al final, la prueba real:**

> "Estoy armando esto. Busco 5 agencias fundadoras: $200 el primer mes, pagado hoy. Mientras termino la herramienta, yo mismo les hago los reportes de 2 clientes a mano. Si no te sirve, te devuelvo el dinero."

Envíales el link de Stripe en ese momento.

La oferta manual (concierge) es clave: elimina la excusa de "avísame cuando esté listo" y además te enseña exactamente qué construir.

---

## Qué cuenta como señal y qué no

**No cuenta (es ruido):**
- "Me encanta la idea"
- "Avísame cuando esté lista"
- "Seguro lo usaría"
- Que se apunten a una lista de espera

**Sí cuenta:**
- Pago con tarjeta
- Que te den acceso a sus cuentas de Google Ads o Meta para el piloto
- Que te presenten a otro dueño de agencia

---

## Cómo leer el resultado

- **0–2 pagos de ~15 llamadas → abandona** la idea tal como está. Antes de cerrar, revisa tus notas: ¿el rechazo fue por el precio, porque no hay dolor o porque ya lo tienen resuelto? Eso te dice si hay un pivote o un cadáver.
- **3–4 pagos → zona gris.** No construyas 2 meses todavía. Sigue entregando el servicio manual 4 semanas y mira si renuevan el segundo mes. La renovación vale más que el primer pago.
- **5 o más pagos → tienes permiso para construir**, y ya tienes clientes que te dicen qué construir.

---

## Advertencias honestas

- **La muestra es chica.** Esto es una prueba para *matar* la idea, no para *demostrarla*. Un "no" contundente es muy informativo; un "sí" pequeño solo te da permiso para el siguiente experimento.
- **Si fallas en el contacto** (menos de 10 llamadas), puede ser tu mensaje y no la idea. Prueba **una** variante del mensaje con otras 50 agencias. Si vuelve a fallar, el problema de distribución también es mortal: si no puedes conseguir una llamada gratis, menos vas a conseguir $200/mes.
- **No hagas anuncios pagos** para esto. Miden clics, no disposición a pagar, y cuestan más.

**Resumen:** en 10 días y con menos de $50 sabrás si 100 dueños de agencia sacan la tarjeta. Si no la sacan cuando se lo pides con nombre y precio, no la van a sacar después de 2 meses de código.