# Claude Fable 5 (suscripción) — strategy/business_model_validation

- model_id: `claude-fable-5`
- success: True  | final: 7.1 | quality: 9.68
- latency_total: 53.355s | tokens_per_second: 57.0
- input_tokens: 2 | output_tokens: 3040

## Respuesta completa

Ok. Me pongo el sombrero de VC que ya vio morir 20 marketplaces B2B de food supply. Vamos.

## 1. Los 5 riesgos principales

**Riesgo #1: El 15% no existe.** Los márgenes en distribución de alimentos son 8-15% brutos. Le estás pidiendo al proveedor que te entregue TODO su margen, o al restaurante que pague 15% más caro en su costo más sensible (food cost es ~30% de sus ingresos). ¿Quién absorbe tu comisión? Nadie puede. Este es el riesgo que mata el modelo antes de empezar.

**Riesgo #2: Desintermediación inmediata.** El restaurante hace el primer pedido por tu app, conoce al proveedor, y el segundo pedido lo hace por WhatsApp directo. No tienes ningún mecanismo de retención. En B2B con compra recurrente y relación personal (el proveedor le fía, le guarda lo mejor, le entrega un domingo), tu plataforma es un directorio caro.

**Riesgo #3: Tu hipótesis confunde el problema.** "Pierden tiempo llamando a proveedores" — ¿eso es un dolor de $X/mes o una molestia? Los restaurantes pequeños no mueren por perder 40 minutos al día llamando. Mueren por flujo de caja, por crédito, por mermas. Si el dolor real es crédito y tú vendes "ahorro de tiempo", estás resolviendo el problema equivocado.

**Riesgo #4: Chicken-and-egg con densidad geográfica brutal.** Esto no es un marketplace nacional, es hiperlocal. Necesitas liquidez por barrio/comuna. 50 restaurantes en Santiago Centro y 3 proveedores que entreguen ahí. Cada ciudad nueva es empezar de cero. El CAC en ambos lados con ticket promedio bajo no cierra.

**Riesgo #5: Logística y calidad no son tu problema... hasta que lo son.** Llega el tomate podrido, ¿a quién le reclama el restaurante? A ti. Disputas, devoluciones, entregas tardías un viernes a las 7pm. O construyes operación logística (te conviertes en distribuidor con peor margen) o eres un intermediario que no controla la experiencia.

## 2. Por qué podría NO funcionar en LATAM específicamente

- **WhatsApp ya ganó.** El restaurante le manda un audio al casero: "lo de siempre más 5 kilos de cebolla". Cero fricción, cero comisión, cero curva de aprendizaje. Compites contra gratis y contra una relación de años.
- **Informalidad estructural.** Gran parte del supply de restaurantes pequeños es sin factura, en efectivo, en la vega/mercado central/central de abasto. Una plataforma con pagos digitales y comisión formaliza una transacción que ambas partes prefieren informal. Estás agregando impuestos + comisión a la vez.
- **El crédito es el verdadero lock-in.** El proveedor local fía a 15-30 días porque conoce al dueño. ¿Tu plataforma da crédito? Si no, eres peor que el status quo. Si sí, ahora eres una fintech de riesgo crediticio en el segmento con más quiebras del mercado.
- **Ya hay cadáveres y sobrevivientes con caja infinita.** Frubana (Colombia/Brasil/México) levantó $200M+ y tuvo que pivotar y recortar. Jüsto, Calii y otros sufrieron. Y los que sobreviven se volvieron distribuidores verticales (compran inventario), no marketplaces puros. Si con $200M no funcionó el marketplace puro, ¿por qué tú con seed?
- **Churn del lado demanda:** los restaurantes pequeños en LATAM tienen una tasa de mortalidad altísima (gran parte cierra antes de 3 años). Tu base de clientes se evapora sola.

## 3. Qué tendría que ser verdad (key assumptions)

1. Que el restaurante esté dispuesto a pagar **más caro o cambiar de proveedor** por conveniencia digital → casi seguro falso; tendrías que ser más barato, no solo más cómodo.
2. Que el proveedor tenga margen para ceder 15% → falso en commodities; quizás verdad en productos de nicho/especialidad con margen 40%+.
3. Que la transacción se quede en la plataforma después del match → solo si controlas pago, crédito o logística. El matchmaking solo no retiene.
4. Que el dolor sea suficientemente grande para cambiar hábito → necesitas evidencia de que hoy pagan (en dinero o pérdida medible) por este problema.
5. Que puedas alcanzar densidad en UNA zona con tu capital → si necesitas 3 ciudades para que cierre el modelo, no cierra.

Si 2 de estas 5 son falsas, el modelo muere. Mi apuesta: hoy son falsas al menos 3.

## 4. El escenario de fracaso rápido

Mes 1-2: onboardeas 30 restaurantes y 10 proveedores con esfuerzo manual brutal. Mes 3: GMV decente, te emocionas. Mes 4-5: el GMV en plataforma cae 60% pero los proveedores te cuentan que esos mismos restaurantes les siguen comprando — por WhatsApp. Hiciste el match gratis y la transacción se fue. Mes 6: para retener, bajas la comisión a 5%, luego intentas suscripción, luego "SaaS para proveedores". Te quedaste sin runway financiando pivotes de un modelo que nunca tuvo unit economics.

La causa de muerte en el certificado: **construiste un canal de descubrimiento para un mercado donde el descubrimiento no es el problema.** Todos los restaurantes ya conocen proveedores. El problema es precio, crédito y confiabilidad — y tú no resolvías ninguno.

## 5. Qué haría yo con $10K

No escribiría una línea de código. Cero app.

- **$0 — Semana 1-2:** 30 entrevistas presenciales con dueños de restaurantes pequeños. No preguntes "¿usarías una app?" (todos dicen que sí y es mentira). Pregunta: "¿cuánto pagaste de más el mes pasado por mal abastecimiento? ¿cuándo fue la última vez que cambiaste de proveedor y por qué? ¿quién te fía y a cuántos días?" Busca dinero perdido, no opiniones.
- **$500 — Semana 3-4:** Concierge MVP. Un número de WhatsApp + tú mismo tomando pedidos de 10 restaurantes y consiguiendo cotizaciones de 3 proveedores. Tú eres la app. Mides: ¿repiten? ¿cuánto ahorran realmente? ¿el proveedor acepta pagar algo por el pedido?
- **$2K — Mes 2:** Si repiten, prueba el modelo de cobro REAL: cobra la comisión (aunque sea 5%) desde la transacción #1. Si nadie paga con humanos haciendo todo el trabajo, con software pagarán menos.
- **$3K — Mes 2-3:** Prueba la hipótesis alternativa que probablemente es la verdadera: compra consolidada (agregar volumen de 10 restaurantes para negociar precio) o crédito. Mide cuál mueve la aguja.
- **$4.5K reservados:** para la segunda iteración cuando la primera hipótesis muera. Y va a morir.

**Criterio de kill:** si en 8 semanas no tienes 10 restaurantes que hayan hecho 3+ pedidos pagando comisión, el modelo marketplace puro está muerto. No lo maquilles con "engagement" ni "pipeline".

---

La verdad incómoda: tu hipótesis tal como está formulada ("pierden tiempo llamando") es la hipótesis que escriben los founders que nunca trabajaron en un restaurante. La versión que sí podría funcionar probablemente es **compra consolidada + crédito para restaurantes pequeños**, donde el software es secundario y el margen viene de volumen, no de comisión. Pero eso solo lo sabrás con las 30 entrevistas, no construyendo la app.

¿Quieres que armemos el guion de esas 30 entrevistas para que no te mientan a la cara?