# Mercury 3 — strategy/business_model_validation

- model_id: `inception/mercury-3`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 11.357s | tokens_per_second: 309.2
- input_tokens: 183 | output_tokens: 3512

## Entrada exacta (lo que recibió el modelo)

**user:**

Quiero crear una app que conecta restaurantes pequenos con proveedores de ingredientes locales. El modelo es marketplace con 15% de comision por transaccion.

Mi hipotesis: los restaurantes pequenos pierden mucho tiempo llamando a multiples proveedores y quieren una solucion digital.

Actua como un VC esceperico. Hazme las preguntas dificiles que me harian en un pitch:
1. Identifica los 5 riesgos principales de este modelo
2. Por que podria NO funcionar en LATAM especificamente?
3. Que tendria que ser verdad para que funcione? (key assumptions)
4. Cual es el escenario donde fracaso rapido y por que?
5. Si solo tuviera $10K para validar, que harias?

No seas amable. Se brutalmente honesto.


## Respuesta completa

Ok, vamos a dejar de lado los cumplidos. Tu pitch es exactamente el tipo de idea que suena lógica en papel pero que muere en la realidad. Te voy a hacer las preguntas que te haría un socio de fondo en un comité, y te las respondo con la misma brutalidad con la que te las haría.

---

## 1. Los 5 riesgos principales de este modelo

**Riesgo #1: El problema no es lo suficientemente doloroso.**  
Estás asumiendo que los restaurantes pequeños "pierden tiempo llamando a múltiples proveedores". Pero la mayoría de los restaurantes pequeños ya tienen proveedores fijos con los que trabajan hace años. Llamar a tres proveedores les toma 20 minutos al día. Eso no es un dolor que haga que alguien cambie su operación y pague 15% de comisión.

**Riesgo #2: El margen de 15% no cubre tus costos.**  
Un marketplace B2B de alimentos perecederos tiene costos de adquisición de clientes altísimos, costos de soporte, disputas por calidad, y logística. El margen bruto de un restaurante pequeño es de 5-10%. Si tú les cobras 15% sobre la transacción, estás comiéndote todo su margen. O el restaurante sube sus precios (y pierde clientes) o te deja de usar.

**Riesgo #3: El problema del "huevo y la gallina" es letal.**  
Sin proveedores, no hay restaurantes. Sin restaurantes, no hay proveedores. Y los proveedores son el lado más difícil: son negocios tradicionales, no digitalizados, que no ven razón para pagar una comisión a una app cuando ya venden todo lo que producen. Tu plataforma no tiene valor para ellos si no les traes demanda incremental, y no les traes demanda incremental si no tienes restaurantes.

**Riesgo #4: La calidad y la confianza no se pueden digitalizar.**  
Los restaurantes compran con los ojos. Necesitan ver, tocar, oler el pescado, la verdura, la carne. Cuando compran en línea, reciben producto que no cumple sus estándares, lo rechazan, y te odian. El costo de devoluciones y disputas en alimentos frescos es altísimo. No eres un marketplace de productos genéricos; eres un intermediario de productos que se pudren.

**Riesgo #5: La logística te va a matar.**  
Los ingredientes frescos requieren cadena de frío, entregas rápidas, y manejo cuidadoso. Si tú no controlas la logística, la experiencia del usuario será horrible. Si la controlas, ya no eres un marketplace, eres una empresa de logística con márgenes de 3-5%. Ese no es tu modelo.

---

## 2. Por qué NO funcionaría en LATAM específicamente

**Porque el mercado ya tiene un intermediario que funciona: el mercado municipal.**  
En LATAM, los restaurantes pequeños compran en mercados locales. Van personalmente, eligen el producto, negocian, y se llevan todo el mismo día. Eso ya resuelve el problema de calidad, precio, y logística. Tu app compite contra una institución que lleva décadas funcionando.

**Porque la informalidad es la norma.**  
La mayoría de los proveedores locales no facturan, no tienen inventario digital, y no tienen precios estandarizados. Si les pides que se registren en una plataforma, que actualicen su catálogo, y que acepten pagos digitales, la mayoría te va a decir que no. No tienen el tiempo ni la capacidad técnica.

**Porque el efectivo y el crédito informal son el rey.**  
Los restaurantes pagan en efectivo o con crédito a 15-30 días. Los proveedores les dan "fiado" porque se conocen de años. Tu plataforma exige pagos digitales o tarjetas, y eso rompe la relación de confianza y el flujo de caja que ya tienen.

**Porque la densidad y la logística son un infierno.**  
En ciudades como CDMX, Bogotá, o Lima, el tráfico es terrible. La entrega de alimentos frescos a múltiples restaurantes pequeños en diferentes zonas tiene un costo por entrega altísimo. Los restaurantes no te van a pagar por eso. Y tú no puedes absorberlo con 15% de comisión.

**Porque hay competidores gigantes que ya tienen la infraestructura.**  
Rappi, iFood, y DiDi Food ya tienen redes logísticas, pagos digitales, y relaciones con restaurantes. Si este modelo fuera viable, ellos ya lo habrían hecho. De hecho, algunos lo intentaron y lo abandonaron.

---

## 3. Qué tendría que ser verdad para que funcione (key assumptions)

1. **Los restaurantes pequeños están dispuestos a cambiar su proceso de compra y pagar más por conveniencia.** No solo decir que "quieren" una solución, sino pagar por ella de forma recurrente.

2. **Los proveedores pueden y quieren digitalizar sus operaciones, aceptar comisiones, y cumplir con estándares de calidad y entrega.** Esto es muy poco probable en LATAM.

3. **La frecuencia y el volumen de pedidos por restaurante es suficiente para generar ingresos que superen el costo de adquisición y retención.** Si cada restaurante gasta $500 USD al mes en insumos, tu comisión es de $75 USD. Necesitas miles de restaurantes para que sea negocio.

4. **La calidad del producto se puede mantener sin inspección física.** Si esto no es verdad, tu plataforma se llena de disputas y devoluciones.

5. **La logística se puede resolver a un costo que no destruya el margen.** O tienes una red de proveedores que entregan ellos mismos, o tienes una red de repartidores que sale cara.

6. **El problema del tiempo perdido es realmente doloroso y no está resuelto por WhatsApp.** Porque hoy, los restaurantes ya piden por WhatsApp. Es gratis, es fácil, y ya lo usan.

---

## 4. El escenario donde fracaso rápido y por qué

**Escenario: Lanzas en una ciudad mediana de LATAM con $50K. Atraes 30 restaurantes y 10 proveedores. Los restaurantes hacen pedidos, pero los proveedores no cumplen con los tiempos de entrega ni con la calidad. Los restaurantes se quejan, piden reembolsos, y dejan de usar la plataforma. Te quedas sin restaurantes, los proveedores se van, y te quedas con una app que nadie usa.**

**Por qué fracasa:** No validaste el lado de la oferta. Asumiste que los proveedores iban a comportarse como empresas digitalizadas, pero son negocios familiares que no tienen procesos. También asumiste que los restaurantes iban a tolerar errores, pero un restaurante no puede esperar 2 horas por un pedido de pescado. Un solo error de calidad destruye la confianza. Sin confianza, el marketplace muere.

**Otra variante:** Atraes proveedores, pero los restaurantes siguen usando WhatsApp porque es más rápido y no confían en la app. Te quedas sin demanda, y los proveedores se van.

---

## 5. Si solo tuviera $10K para validar, qué haría

**No construiría nada.** Cero código, cero app, cero landing page.

**Haría un "concierge" manual.** Me pondría en el lugar del intermediario. Usaría WhatsApp y teléfono.

- Hablaría con 30 restaurantes pequeños y les preguntaría: "¿Cómo compran hoy? ¿Cuánto tiempo gastan? ¿Qué es lo que más odian?"  
- Luego les diría: "Te voy a conseguir tus ingredientes mañana por el mismo precio o más barato, y te los llevo. Solo pago 10% de comisión."  
- Durante 2 semanas, recibiría pedidos por WhatsApp, iría al mercado, compraría, y entregaría.  
- Mediría: ¿Cuántos restaurantes realmente hacen pedidos? ¿Con qué frecuencia? ¿Cuánto gastan? ¿Siguen usando el servicio después de la primera semana? ¿Están dispuestos a pagar la comisión?

**Si en 2 semanas no tienes al menos 10 restaurantes que hagan pedidos recurrentes, aborta.** No hay negocio. Si los tienes, entonces tienes evidencia de que el problema existe y que la gente está dispuesta a pagar. Solo entonces construirías un MVP simple: un catálogo en Google Sheets, pedidos por WhatsApp, y una pasarela de pagos.

---

## Conclusión brutal

Tu hipótesis probablemente es falsa. El problema no es que los restaurantes pierdan tiempo llamando; es que ya tienen relaciones establecidas, compran en mercados, y usan WhatsApp. Estás compitiendo contra la costumbre, la informalidad, y un sistema que ya funciona. El 15% de comisión no cubre los costos de un marketplace de alimentos frescos, y la logística te va a comer vivo. Si no validas con $10K antes de construir, vas a perder tiempo y dinero en una solución que nadie quiere.

**La pregunta que deberías hacerte no es "¿cómo construyo la app?" sino "¿por qué este problema no se ha resuelto ya?"** Si no tienes una respuesta convincente, no tienes negocio.