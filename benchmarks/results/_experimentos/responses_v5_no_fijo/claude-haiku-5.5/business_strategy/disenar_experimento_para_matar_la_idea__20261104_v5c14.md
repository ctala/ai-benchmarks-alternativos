# Claude Haiku 5.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.5 | quality: 8.0
- latency_total: 22.414s | tokens_per_second: 170.7
- input_tokens: 291 | output_tokens: 3825

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento para matar la hipótesis

Tu hipótesis tiene cuatro supuestos encadenados. Si cualquiera es falso, la idea muere. Conviene probar primero el más letal y el más barato de medir:

1. **Dolor:** las agencias pequeñas gastan mucho tiempo en reportes y les duele.
2. **Solución actual:** no tienen algo "suficientemente bueno" (Looker Studio, Sheets, hacerlo a mano) que resuelva el problema.
3. **Disposición a pagar:** $200/mes les parece razonable frente al tiempo que ahorran.
4. **Canal:** puedes llegar a ellas y convertirlas a un costo que haga sostenible el negocio.

El supuesto que más suele fallar es el 3, y es el que probamos primero, porque lo que la gente dice no sirve y lo que paga, sí.

---

## Fase 1: Preventa con dinero real (semana 1-3)

**Qué haces:**
- Una landing de una página (Carrd, Framer o Webflow). Titular: *"Automatiza los reportes de tus clientes. Ahorra 10+ horas al mes."* Incluye precio ($200/mes) y un botón que dice *"Reservar acceso fundador: depósito de $50 reembolsable"*.
- El botón va a un Stripe Payment Link. Cobras $50 reembolsables (o $200 si te atreves, pero $50 baja la fricción sin perder la señal). Si nadie paga ni un dólar, la señal es igual de válida.
- Lanzas tráfico dirigido: anuncios de búsqueda en Google (*"reportes automáticos para agencias de marketing"*) y, en paralelo, 150 correos o mensajes de LinkedIn a dueños de agencias de 5 a 30 personas.

**Costo:** ~$400–600 en anuncios + ~$30 en dominio y herramientas. Stripe no cobra nada si nadie paga.
**Tiempo:** 2 días para montar, 2–3 semanas para tener datos.

## Fase 2: Entrevistas de comportamiento (en paralelo, semana 1-2)

Habla con 10–15 personas que respondieron o pagaron. No preguntes "¿te serviría?". Pregunta por hechos:
- "¿Cuántas horas al mes te toma hacer los reportes? ¿Quién los hace?"
- "¿Qué herramientas usas hoy? ¿Cuánto pagas por ellas?"
- "¿Qué fue lo último que intentaste para resolver esto y por qué lo dejaste?"
- "Si mañana esto no existiera, ¿qué harías?"

Si dicen que su problema es grave pero no han gastado tiempo ni dinero en resolverlo, el dolor es menor de lo que parece.

## Fase 3 (opcional, si la Fase 1 sobrevive): Servicio manual

Ofrece a 3–5 agencias que te paguen $200 al mes para que tú hagas sus reportes a mano (con Sheets, scripts o lo que sea). Esto prueba si el dolor es real y pagable antes de escribir una línea de software. Costo: tu tiempo, unas 5–8 horas por cliente al mes.

---

## Criterios de muerte (defínelos ANTES de empezar y escríbelos)

Mata la idea si ocurre **cualquiera** de estos:

| Señal | Umbral de muerte |
|---|---|
| Conversión a clic en "reservar" | Menos de 1 de cada 100 visitantes que llegan por anuncios o links directos |
| Depósitos pagados | 0 pagos después de ~150 contactos calificados (agencias reales, no curiosos) |
| Dolor en entrevistas | Menos de 5 de 15 entrevistadas dicen que reportes son de sus 3 principales dolores *y* gastan >5 h/mes en ellos |
| Alternativa actual | Más de la mitad ya usa algo gratis o barato que consideran "suficiente" |
| Servicio manual (Fase 3) | Ninguna de 5 agencias paga $200/mes después de ver un ejemplo de reporte |
| Costo de adquisición | Si el costo por depósito pagado supera $150, el canal no es viable a $200/mes |

Si pasas los umbrales, eso **no** prueba que la idea funcione: solo que no la mataste barato. El siguiente paso sería validar retención con los que pagaron.

---

## Trampas que arruinan el experimento

- **Confundir interés con dinero.** "Me encantaría" no cuenta. Solo cuentan tarjeta, firma o tiempo concreto (por ejemplo, darte acceso a los datos de sus clientes).
- **Mover la meta.** Si con 0 pagos dices "es que el tráfico era malo", ya no estás experimentando. Por eso los umbrales van escritos antes.
- **Tráfico de mala calidad.** Si los anuncios traen estudiantes o freelancers solos, el resultado no sirve. Filtra en el formulario por tamaño de agencia y número de clientes.
- **Pedir opinión a amigos.** Gente que te quiere te dirá que sí. Busca compradores fríos.

---

## Resumen

- **Costo total:** ~$500 y, con suerte, cero tiempo de ingeniería.
- **Duración:** 2–3 semanas.
- **Qué te haría abandonar:** 0 depósitos tras ~150 contactos calificados, o menos de 1% de conversión de clic a pago, o que las agencias digan que el problema no les duele lo suficiente como para gastar tiempo o dinero en resolverlo.

Si tu hipótesis sobrevive a esto, ya tienes una razón concreta para construir. Si no, acabas de ahorrarte dos meses de trabajo y probablemente un lanzamiento fallido.