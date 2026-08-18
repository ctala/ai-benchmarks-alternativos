# Claude Opus 5 Fast — strategy/business_model_validation

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.75 | quality: 10.0
- latency_total: 76.844s | tokens_per_second: 81.3
- input_tokens: 288 | output_tokens: 6244

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

# VC escéptico — 20 minutos, tu reloj corre

Antes de las 5 preguntas, las tres que te haría en el minuto 4 y que probablemente terminarían el pitch:

1. **"Si el problema es que pierden tiempo llamando, ¿por qué el sustituto no es un grupo de WhatsApp gratis?"** Porque eso es tu competencia real, no otro marketplace.
2. **"¿Qué margen bruto tiene un distribuidor de abarrotes o de verdura en tu ciudad?"** Si no sabes ese número de memoria, no entiendes el negocio. (Pista: en fresco suele andar entre 12% y 25%.) Tu 15% no es una comisión, es *casi toda la utilidad del proveedor*.
3. **"¿Qué porcentaje de tus transacciones piloto siguen pasando por la plataforma en la semana 10?"** Esta es la única métrica que importa y la que ningún fundador de este espacio tiene lista.

---

## 1. Los 5 riesgos principales

**R1 — Desintermediación (leakage). El asesino #1.**
Estás en el peor cuadrante posible para un marketplace: transacciones de **alta frecuencia** (3-6 veces por semana), **bajo ticket**, **contraparte repetida** y **relación personal**. El restaurante y el proveedor se conocen en el pedido #1 y en el #4 ya se pasaron el número. Tú les cobras 15% por presentarlos una sola vez. Airbnb sobrevive al leakage porque el match es aleatorio y esporádico; tú tienes el caso opuesto exacto. Sin control de logística o de pago, tu leakage a 90 días puede ser de 50-70%.

**R2 — El take rate es matemáticamente insostenible.**
Si el proveedor gana 18% bruto y le quitas 15%, le queda 3% para financiar entrega, mermas y crédito. No lo va a absorber. Solo hay dos salidas: (a) lo sube al precio → el restaurante compara con su proveedor de siempre, ve 10-15% más caro y se va; (b) lo absorbes tú → no hay negocio. **El 15% no es una decisión de pricing, es una hipótesis no validada de que estás creando 15% de valor nuevo.** ¿Lo estás creando?

**R3 — Tu hipótesis del dolor probablemente está mal.**
"Pierden tiempo llamando" es un dolor de **conveniencia**, y la conveniencia rara vez paga 15%. Los dolores reales, por los que sí pagan, son:
- **Crédito**: el proveedor actual le fía a 15-30 días. Ese es el switching cost real, y es financiero, no digital.
- **Fill rate**: que llegue lo que pidió, completo, a las 6am.
- **Precio y volatilidad**: el jitomate cambia de precio diario.
- **Calidad consistente** en producto fresco no estandarizado.

Tú resuelves el #5 de su lista. El dueño del restaurante que "pierde 40 minutos al día llamando" muchas veces también es quien cocina; ese tiempo no tiene un costo de oportunidad monetizable.

**R4 — Vas a terminar siendo un distribuidor con logística propia, y no lo tienes presupuestado.**
El patrón en LATAM es consistente: Frubana, Chiper, Muni, Merqueo y otros arrancaron con tesis marketplace-asset-light y todos migraron hacia inventario propio, bodega y flota, porque el fill rate y la calidad no se pueden garantizar con oferta fragmentada. Varios de ellos, con cientos de millones levantados, tuvieron reestructuras o cierres. Si el mejor caso de tu tesis es "convertirme en distribuidor", estás pitcheando un negocio de márgenes de 8-15% intensivo en capital, no software.

**R5 — Churn del lado de la demanda.**
Una fracción muy alta de restaurantes pequeños cierra en los primeros 12-24 meses. Súmale leakage y tienes un LTV que no aguanta CAC de venta en campo (que es la única que funciona en este segmento: nadie descarga una app por un anuncio de Meta para cambiar a su proveedor de carne).

---

## 2. Por qué podría NO funcionar en LATAM específicamente

**a) La informalidad fiscal es un antifeature de tu producto.**
Una porción grande de restaurantes pequeños compra en efectivo, sin factura, y opera parcialmente fuera del radar. Tu plataforma **genera un registro digital de cada compra**. Le estás pidiendo a tu cliente que se formalice para ahorrarse llamadas. En México eso puede significar IVA e ISR nuevos; el "costo" de tu producto no es 15%, es 15% + su arbitraje fiscal. Esto ha matado más marketplaces B2B en la región que la competencia.

**b) El crédito informal es el verdadero producto.**
La relación con el proveedor de la esquina no es transaccional, es un contrato de deuda no escrito. "Me fía la semana, si tengo mala racha me espera." Tú no puedes competir con eso sin balance. Y si vas a dar crédito, no estás levantando para un marketplace, estás levantando para una fintech con riesgo crediticio en el segmento más frágil que existe.

**c) La central de abastos ya es el marketplace.**
Corabastos, Central de Abasto, CEAGESP, Mercado Modelo: agregación física con descubrimiento de precios en tiempo real y crédito. Tu propuesta es digitalizar una capa que ya funciona, aunque sea fea.

**d) Cobranza.**
Pago contra entrega en efectivo sigue siendo dominante. Si el efectivo lo toca el repartidor del proveedor, nunca tocas el dinero, y si nunca tocas el dinero **no puedes cobrar comisión**: puedes facturarla, no cobrarla. Un marketplace que factura pero no retiene tiene morosidad estructural.

**e) Densidad y logística.**
Tu unit economics dependen de densidad por zona. Tráfico, direcciones informales, ventanas de entrega de madrugada, inseguridad en ciertas rutas. El costo por entrega en LATAM no baja tanto con escala como en el modelo de tu spreadsheet.

---

## 3. Qué tendría que ser verdad (key assumptions)

Ordenadas de más frágil a menos:

| # | Supuesto | Cómo se ve el fracaso |
|---|---|---|
| A1 | El take rate combinado real es ≥8% **cobrado**, no facturado | Terminas en 3-4% y no cubres ni el CAC |
| A2 | ≥60% de los pares restaurante-proveedor siguen transaccionando **en la plataforma** al mes 3 | Leakage; te vuelves un directorio |
| A3 | Existe una razón estructural para no salirse: pago, crédito, logística o precio agregado | Sin esto, A2 es imposible |
| A4 | El restaurante concentra ≥40% de su gasto de insumos en tu plataforma | Si eres el 8% de su compra, eres un juguete |
| A5 | Puedes garantizar fill rate >92% sin inventario propio | Si no, vas a 1P y cambias el modelo de negocio |
| A6 | CAC en campo < $150-200 USD con payback < 4 meses | Ventas B2B en la calle es caro y lento |
| A7 | Los proveedores prefieren volumen incremental sobre margen | Solo cierto si les traes clientes **nuevos**, no si les reciclas los suyos |

**A3 es la madre de todas.** Si no puedes articular en una frase por qué es *irracional* que se salten la plataforma, no tienes negocio, tienes una feature.

---

## 4. El escenario de fracaso rápido

**Mes 0-2:** Consigues 40 restaurantes y 15 proveedores en una zona. GMV crece bonito. Slide de hockey stick.

**Mes 3-4:** El GMV se aplana. No porque no crezcan los usuarios, sino porque **la frecuencia por usuario cae**. Un restaurante que pedía 12 veces/mes ahora pide 3: usa la plataforma solo para el proveedor nuevo que no conocía y para todo lo demás vuelve a WhatsApp. Tu "usuario activo mensual" se ve bien; tu GMV por usuario se derrumba.

**Mes 5:** Un pedido grande llega incompleto o con producto en mal estado. El restaurante te culpa a ti, no al proveedor. Empiezas a contratar gente para "supervisar calidad". Tus costos variables se vuelven fijos.

**Mes 6-8:** Para defender el fill rate compras inventario de los 20 SKUs más pedidos. Ya eres un distribuidor subescalado compitiendo contra distribuidores con 30 años de rutas. Tu margen bruto real es 9%. Quemas caja en camionetas.

**Mes 9:** Vas a levantar Serie A con retención de cohortes M3 del 22% y un take rate efectivo de 4.5%. Nadie firma.

**El indicador temprano que te va a avisar en la semana 8:** GMV por cuenta activa, no GMV total. Si tu narrativa depende de agregar logos, ya perdiste.

---

## 5. Con $10K: qué haría

**Regla dura: $0 a desarrollo de producto.** Si gastas en una app, gastaste el dinero en la pregunta equivocada.

**Semanas 1-2 — Diagnóstico de dolor real ($500).**
30 entrevistas con dueños de restaurantes de 1-3 sucursales en **una sola zona densa**. No preguntes "¿te gustaría una app?" — todos dicen que sí. Pregunta:
- "Muéstrame tus últimos 5 pedidos. ¿A quién? ¿Cuánto? ¿Cómo pagaste?"
- "¿Cuándo fue la última vez que cambiaste de proveedor y por qué?"
- "¿Quién te fía y a cuántos días?"
Si <30% menciona el tiempo de llamadas espontáneamente en el top-3 de dolores, **tu hipótesis está muerta** y acabas de ahorrarte 18 meses.

**Semanas 3-4 — Test de take rate del lado oferta ($0).**
15 conversaciones con proveedores. Pregunta directo por su margen bruto y ofrece 15%. Si más de 10 dicen que no o piden subirlo al precio, tu modelo no cierra. Esta conversación cuesta cero y responde el riesgo R2.

**Semanas 5-12 — Concierge manual, sin producto ($6,500).**
Tú y un operador, con WhatsApp y Google Sheets, brokereas pedidos reales para 20-25 restaurantes. Tú tomas el pedido, tú lo colocas, tú **cobras** y tú le pagas al proveedor menos comisión. Controlar el flujo de dinero es lo que estás probando, no la UX.

Presupuesto: $4,000 operador + $2,000 subsidio de descuentos/entrega para desbloquear los primeros pedidos + $500 herramientas.

**Semana 12-14 — Los 4 números que decides ($0).**

| Métrica | Umbral de continuar | Umbral de matar |
|---|---|---|
| % de pedidos en semana 10 que aún pasan por ti | >65% | <40% |
| Take rate **cobrado** (no facturado) | >8% | <5% |
| Pedidos/mes por restaurante activo | >8 | <4 |
| Restaurantes que pagarían aunque exista la alternativa directa | >50% | <25% |

**$3,000 de reserva** para probar la variante que probablemente sea el negocio real: ofrecer a 5 restaurantes pago a 15 días financiado por ti. Si eso mueve la retención de 40% a 80%, acabas de descubrir que tu negocio es crédito B2B con capa de compras, no un marketplace de conveniencia. Eso sí es un negocio defendible en LATAM — y es un pitch completamente distinto.

---

**Lo que te diría al salir:** tu tesis actual describe una *vitamina* en un mercado que compra *analgésicos y crédito*. Vuelve cuando tengas el dato de la semana 10 de leakage. Ese número, y no tu TAM, decide si esto existe.