# Qwen 3.8 Flash — strategy/business_model_validation

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 93.183s | tokens_per_second: 100.5
- input_tokens: 230 | output_tokens: 9365

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

Bien. Te hablo como un VC que no te va a dar dinero hoy y que lleva 20 años viendo startups que “conectan oferta y demanda” y mueren por no entender operación, liquidez, confianza y márgenes.

Tu pitch actual, dicho brutalmente, es:

> “Los restaurantes pequeños pierden tiempo llamando proveedores; yo les hago una app marketplace con 15% de comisión.”

Eso no es una empresa todavía. Es una hipótesis débil.

El problema no es “pierden tiempo”. El problema es: **¿ese tiempo perdido les cuesta dinero, ventas, margen, stockouts, deterioro de calidad o riesgo operativo?** Si no puedes cuantificarlo, no tienes dolor monetizable.

Y peor: un marketplace con 15% de comisión sobre ingredientes locales es, en la práctica, un negocio de logística, confianza, pagos, facturación, calidad y retención. La app es la parte fácil.

Vamos por partes.

---

# 1. Los 5 riesgos principales de este modelo

## Riesgo 1: “Pierden tiempo” no significa “pagan por resolverlo”

Tu hipótesis está mal formulada.

Los dueños de restaurantes pequeños no necesariamente quieren “digitalizar compras”. Quieren:

- precio bajo,
- calidad confiable,
- entrega a tiempo,
- crédito,
- menos errores,
- menos stockouts,
- menos pérdida por deterioro,
- menos problemas con facturación,
- relaciones de confianza.

Si tu plataforma les ahorra tiempo pero les sube el precio, les complica la vida, no les da factura, no les da crédito o no mejora la calidad, no la van a usar.

**Pregunta difícil:**  
¿Cuánto dinero pierde un restaurante hoy por comprar ineficientemente? No “horas”, sino:

- ¿cuánto desperdicio?
- ¿cuántas veces se queda sin producto?
- ¿cuánto paga de sobreprecio?
- ¿cuántos pedidos llegan mal?
- ¿cuánto tarda en resolver una devolución?

Si no puedes responder esto con datos de 20 restaurantes reales, tu dolor es anecdótico.

---

## Riesgo 2: Marketplace two-sided = infierno de liquidez

No tienes un problema de software. Tienes un problema de densidad.

Necesitas simultáneamente:

- suficientes restaurantes en una zona,
- suficientes proveedores en la misma zona,
- con SKUs compatibles,
- con precios competitivos,
- con capacidad de entrega,
- con calidad aceptable,
- con frecuencia de compra suficiente.

Un marketplace de ingredientes no funciona “a nivel país”. Funciona micro por micro: barrio, zona gastronómica, ruta de entrega.

Si tienes 50 restaurantes en una ciudad y 30 proveedores dispersos, pero no se cruzan, no tienes marketplace. Tienes un directorio muerto.

**Pregunta difícil:**  
¿Cuál es tu zona mínima viable? ¿Cuántos restaurantes y cuántos proveedores necesitas en un radio realista para que un pedido promedio sea rentable?

Si tu respuesta es “todo LATAM”, estás muerto.

---

## Riesgo 3: Desintermediación brutal

Este es el riesgo clásico del marketplace B2B:

> El restaurante y el proveedor se conocen gracias a ti, y luego se van a WhatsApp.

Con 15% de comisión, la tentación de fugarse es enorme.

Para el proveedor: 15% es muchísimo si su margen neto es 5%, 10% o 15%.  
Para el restaurante: si puede comprar directo por 10% menos, lo va a intentar.  
Para ti: pierdes el ingreso justo cuando el comportamiento de compra se estabiliza.

**Pregunta difícil:**  
¿Qué hace tu plataforma para que sea más conveniente transaccionar dentro que fuera?

Si tu respuesta es “somos más fáciles”, no basta. Necesitas una razón estructural:

- pagos,
- crédito,
- logística,
- garantía,
- facturación,
- consolidación de proveedores,
- inventario,
- datos,
- contratos,
- control de calidad,
- devoluciones.

Si no tienes una de esas razones, el marketplace se filtra.

---

## Riesgo 4: La comisión de 15% probablemente no sobrevive a la economía unitaria

Veamos números fríos.

Supongamos un pedido promedio de $100.

Tú cobras 15% = $15.

Pero necesitas cubrir:

- adquisición de restaurante: CAC,
- adquisición de proveedor,
- soporte,
- cobranza,
- pasarela de pago,
- logística o coordinación,
- devoluciones,
- reembolsos,
- control de calidad,
- fraudes,
- capital de trabajo,
- impuestos/facturación.

Si el pedido promedio es $50, la comisión es $7.50. Ahí te mueres.

Los restaurantes pequeños compran cosas caras pero con márgenes finos. No son compras impulsivas tipo consumer. Son compras recurrentes, sensibles a precio y con relaciones personales.

**Pregunta difícil:**  
¿Cuál es tu GMV promedio por restaurante al mes? ¿Cuántos pedidos al mes? ¿Cuál es tu comisión capturada real después de fugas, descuentos, devoluciones y costos variables?

Si no tienes contribution margin positivo desde el pedido manual, la tecnología no te va a arreglar el negocio.

---

## Riesgo 5: Ingredientes locales = calidad inconsistente, informalidad y confianza

Ingredientes no son productos estandarizados.

Un tomate no es un iPhone. Hay:

- tamaño,
- madurez,
- frescura,
- temporada,
- transporte,
- cadena de frío,
- calidad sanitaria,
- trazabilidad,
- devoluciones,
- quejas,
- variabilidad de proveedor.

Y muchos proveedores locales pueden ser:

- pequeños productores,
- cooperativas,
- revendedores informales,
- sin factura,
- sin inventario digital,
- sin capacidad logística,
- sin capacidad de cumplimiento,
- sin confianza institucional.

Un marketplace que promete “proveedores locales” puede terminar siendo una fábrica de problemas de calidad.

**Pregunta difícil:**  
¿Quién responde si el pollo llega mal, la verdura está podrida, el proveedor no entrega, el restaurante no paga o hay un problema sanitario?

Si no tienes un modelo claro de garantía, devolución y responsabilidad, no eres marketplace. Eres un intermediario frágil.

---

# 2. ¿Por qué podría NO funcionar en LATAM específicamente?

Primero: “LATAM” no es un mercado. Es una generalización peligrosa.

Lo que funciona en Ciudad de México puede no funcionar en Lima, Bogotá, Buenos Aires, Santiago, Medellín, Guayaquil o un pueblo de provincia.

Pero hay riesgos comunes en LATAM que pueden matar tu modelo.

---

## A. La informalidad no es un detalle; es el corazón del problema

Muchos proveedores locales operan en informalidad:

- sin RUC/RFC/NIT/CUIT,
- sin factura,
- sin contabilidad,
- sin registros sanitarios claros,
- sin contratos,
- sin capacidad de emitir comprobantes,
- sin trazabilidad.

Los restaurantes, aunque pequeños, muchas veces necesitan factura por:

- IVA,
- costos,
- contabilidad,
- crédito bancario,
- cumplimiento fiscal,
- compras corporativas,
- auditorías,
- proveedores formales.

Si tu plataforma no resuelve facturación, te quedas fuera.

**Pregunta difícil:**  
¿Puedes operar con proveedores informales sin romper el modelo fiscal y de confianza? ¿O vas a limitar tu oferta a proveedores formales, reduciendo tu ventaja “local”?

---

## B. Las relaciones ya están resueltas por WhatsApp, teléfono y confianza personal

No subestimes esto.

En LATAM, mucho B2B funciona por:

- WhatsApp,
- llamadas,
- grupos de compra,
- contactos personales,
- recomendaciones,
- favores,
- crédito de palabra,
- “mañana te pago”,
- “te guardo”,
- “te lo dejo a buen precio”.

Tu plataforma tiene que ser mejor que eso. No más “digital”, sino más útil.

**Pregunta difícil:**  
¿Tu app es mejor que un grupo de WhatsApp donde el proveedor manda precios, fotos, disponibilidad y acepta transferencia?

Si no, no tienes producto.

---

## C. El crédito es parte del producto

Los restaurantes pequeños no siempre pagan al contado.

Esperan:

- 7 días,
- 15 días,
- 30 días,
- crédito,
- descuento por pronto pago,
- fiado,
- consolidación de pagos.

Si tú como marketplace cobras 15%, pero no financias, no resuelves flujo de caja, te van a odiar.

Y si financias, te conviertes en fintech, con riesgo de crédito, cobranza, fraude y capital de trabajo.

**Pregunta difícil:**  
¿Quién asume el riesgo de crédito? ¿El proveedor? ¿Tú? ¿Una fintech? ¿Nadie?

Si nadie, tu modelo puede no funcionar.

---

## D. Logística, seguridad y distribución son caros y caóticos

En muchas ciudades LATAM:

- direcciones imprecisas,
- zonas con restricciones de circulación,
- robos,
- tráfico,
- costos de flete,
- cadena de frío inestable,
- entregas fraccionadas,
- pedidos pequeños,
- ventanas de entrega rígidas.

Un restaurante necesita productos frescos a tiempo. Si llegas tarde, el negocio pierde.

**Pregunta difícil:**  
¿Vas a integrar logística o solo conectar? Si solo conectas, ¿quién entrega? ¿Quién paga el costo? ¿Quién responde si falla?

Si no controlas la entrega, no controlas la experiencia.

---

## E. Los proveedores locales pueden no tener escala ni consistencia

Un pequeño productor puede tener:

- cosecha variable,
- stock inestable,
- capacidad limitada,
- mala comunicación,
- precios que cambian semanalmente,
- calidad irregular,
- falta de empaque,
- falta de certificaciones.

Los restaurantes necesitan consistencia.

**Pregunta difícil:**  
¿Puedes garantizar que un proveedor local entregue lo mismo, al mismo precio, cada semana? Si no, el restaurante vuelve al distribuidor estable.

---

## F. Los distribuidores tradicionales ya tienen ventajas

Los restaurantes ya tienen opciones:

- mayoristas,
- distribuidores,
- mercados centrales,
- cadenas de proveedores,
- WhatsApp de proveedores,
- ferias locales,
- contactos directos.

Muchos ya ofrecen:

- entrega,
- crédito,
- descuento,
- variedad,
- relación personal,
- facturación,
- reposición.

Tú entras con 15% de comisión y promesa de “conexión local”. Eso no es diferenciación suficiente.

**Pregunta difícil:**  
¿Por qué un restaurante te paga a ti 15% si su proveedor actual le da crédito, entrega y precio?

---

# 3. ¿Qué tendría que ser verdad para que esto funcione?

Estas son tus key assumptions. Si alguna falla, el negocio se cae.

---

## Assumption 1: El problema actual es caro

Debe ser verdad que los restaurantes pierden dinero real, no solo tiempo.

Ejemplos:

- pagan sobreprecio por falta de comparación,
- pierden ventas por stockouts,
- desperdician producto por compras mal planificadas,
- pierden horas de operación,
- sufren fraudes o mala calidad,
- no acceden a mejores proveedores,
- no tienen precios transparentes,
- no pueden consolidar compras.

**Test:**  
Entrevistas con 30 restaurantes y datos de sus compras actuales.

**Señal de muerte:**  
“Sí, pierdo tiempo, pero no me importa mucho” o “ya lo resuelvo con mi proveedor de confianza”.

---

## Assumption 2: Los proveedores están dispuestos a pagar 15%

Debe ser verdad que 15% de comisión es menor que el valor que tú generas para el proveedor.

Valor puede ser:

- nuevos clientes,
- pedidos más predecibles,
- menos cobranza,
- mejor flujo,
- menos devoluciones,
- acceso a restaurantes que no conocerían,
- logística,
- pagos garantizados,
- datos de demanda.

**Test:**  
¿Un proveedor acepta pagar 15% si le llevas un pedido real y le pagas por adelantado?

**Señal de muerte:**  
Aceptan “por probar”, pero se niegan a firmar condición de pago o fugan al segundo pedido.

---

## Assumption 3: Puedes controlar la transacción

Debe ser verdad que el comprador y vendedor no se escapan fácilmente.

Necesitas al menos una de estas razones para que transaccionen contigo:

- pago,
- logística,
- garantía,
- factura,
- crédito,
- consolidación,
- inventario,
- calidad verificada,
- contratos,
- devolución,
- datos.

**Test:**  
¿Qué porcentaje de usuarios vuelve a comprar dentro de la plataforma después del primer pedido?

**Señal de muerte:**  
Primera compra contigo, segunda compra por WhatsApp.

---

## Assumption 4: La densidad inicial es alcanzable

Debe ser verdad que puedes conseguir suficientes restaurantes y proveedores en una zona pequeña.

No necesitas 1,000 usuarios. Necesitas 20-50 usuarios intensos.

**Test:**  
En un radio de 3-5 km, ¿puedes conseguir 15 proveedores y 25 restaurantes que compren recurrentemente?

**Señal de muerte:**  
Cada pedido requiere un esfuerzo manual enorme porque la oferta no coincide con la demanda.

---

## Assumption 5: El ticket promedio y la frecuencia sostienen el modelo

Debe ser verdad que el GMV por restaurante/mes es suficientemente alto.

Ejemplo:

- AOV: $150,
- pedidos/mes: 6,
- GMV/mes: $900,
- comisión 15%: $135,
- costos variables: soporte, pagos, logística, devoluciones.

Si el AOV es $50 y la frecuencia es 2 veces al mes, no hay negocio.

**Test:**  
Calcular contribution margin por pedido real.

**Señal de muerte:**  
Cada pedido deja pérdida después de costos variables.

---

## Assumption 6: Puedes resolver confianza y calidad

Debe ser verdad que puedes garantizar que el producto llegue bien.

Ejemplos:

- proveedor calificado,
- fotos reales,
- inventario actualizado,
- devoluciones simples,
- control de calidad,
- penalizaciones,
- ratings,
- escrow,
- garantía de frescura.

**Test:**  
¿Aceptarías comprar $500 de productos sin ver al proveedor?

Si tú no confiarías, el restaurante tampoco.

---

## Assumption 7: Puedes operar fiscalmente

Debe ser verdad que puedes emitir factura, cobrar comisión, registrar proveedores y cumplir normativa local.

**Test:**  
Hablar con contador/abogado antes de construir.

**Señal de muerte:**  
No puedes facturar legalmente la comisión o los proveedores no pueden emitir comprobantes.

---

## Assumption 8: Tu ventaja no es “app”, es operación

Debe ser verdad que tu diferenciador es operativo, no tecnológico.

Tu empresa podría ser:

- logística consolidada,
- calidad garantizada,
- pagos,
- crédito,
- datos de demanda,
- compras agregadas,
- devoluciones,
- trazabilidad.

**Pregunta difícil:**  
Si mañana un competidor hace la misma app, ¿por qué te ganan o te pierden?

Si tu respuesta es “porque somos más fáciles”, no tienes moat.

---

# 4. ¿Cuál es el escenario donde fracaso rápido y por qué?

El escenario de fracaso rápido es este:

## Mes 0-1

Construyes una app bonita.

- catálogo de proveedores,
- checkout,
- perfiles,
- dashboard,
- pagos,
- ratings.

Te enamoras del producto.

## Mes 2-3

Consigues 40 restaurantes y 25 proveedores “porque son amigos, contactos o early adopters”.

Haces 80 pedidos.

Parece que funciona.

## Mes 4

Descubres que:

- muchos proveedores no actualizan stock,
- los precios cambian,
- la calidad varía,
- las entregas se retrasan,
- los restaurantes no pagan a tiempo,
- los proveedores quieren cobrar directo,
- los restaurantes quieren comprar directo,
- los tickets son pequeños,
- el soporte es enorme,
- las devoluciones duelen.

## Mes 5

La comisión real capturada baja.

No cobras 15%. Cobras, por ejemplo, 3% o 5% porque:

- los proveedores descuentan,
- los usuarios negocian fuera,
- tú subsidias entregas,
- perdonas comisiones para retener,
- hay fraudes,
- hay devoluciones,
- hay pedidos fallidos.

## Mes 6

El CAC es alto, la retención es baja y el LTV no existe.

Mueres.

---

## La razón profunda del fracaso

No fracasas por falta de app.

Fracas porque:

1. **No resolviste liquidez.**  
   No tenías suficientes compradores y vendedores compatibles en la misma zona.

2. **No controlaste la transacción.**  
   Te saltaron.

3. **No mejoraste la economía del restaurante.**  
   Tu comisión no se compensó con valor.

4. **No resolviste operación.**  
   Logística, calidad, pagos, devoluciones y confianza eran demasiado duros.

5. **Subestimaste el incumbente invisible.**  
   WhatsApp, teléfono, confianza personal y distribuidores locales.

---

# 5. Si solo tuviera $10K para validar, ¿qué haría?

No construiría app.

No contrataría desarrolladores.

No haría MVP con catálogo.

No compraría dominio premium.

No haría branding.

No haría demo bonita.

Usaría los $10K para comprar una sola cosa: **evidencia de que el negocio existe sin software.**

---

## Plan de validación con $10K

### Fase 1: Elige una micro-zona, no LATAM

Elige una ciudad y una zona concreta.

Ejemplo:

- una colonia/barrio gastronómico,
- 5 km de radio,
- restaurantes pequeños independientes,
- proveedores locales cercanos.

No intentes “país”. No intentes “ciudad entera”.

Necesitas densidad.

---

### Fase 2: Consigue 20 restaurantes y 15 proveedores reales

No “leads”. Personas que te den datos de compras.

Para restaurantes, pregunta:

- ¿qué compran semanalmente?
- ¿a quién?
- ¿precio actual?
- ¿frecuencia?
- ¿método de pago?
- ¿último problema con proveedor?
- ¿cuánto pierden por stockout?
- ¿cuánto desperdician?
- ¿quién compra?
- ¿necesitan factura?
- ¿pagan al contado o crédito?

Para proveedores, pregunta:

- ¿qué venden?
- ¿stock disponible?
- ¿precio?
- ¿capacidad de entrega?
- ¿facturan?
- ¿aceptan pagos digitales?
- ¿pueden pagar comisión por pedido?
- ¿cuál es su margen?
- ¿qué porcentaje de clientes nuevos aceptan?

---

### Fase 3: Haz concierge marketplace

Usa:

- WhatsApp Business,
- teléfono,
- Google Sheets,
- links de pago,
- transferencias,
- correos,
- facturas manuales si aplica.

Tú eres el marketplace.

Recibes lista de compra del restaurante.

Buscas proveedores.

Consolidas pedido.

Cobras.

Coordinas entrega.

Verificas calidad.

Gestionas devolución.

---

### Fase 4: Cobra comisión desde el primer día

No valides con “gratis”.

Eso es una mentira.

Si no pueden pagar, no tienen dolor.

Prueba:

- 10% comisión,
- 15% comisión,
- o markup equivalente.

Puedes empezar con:

- 50% pago por adelantado,
- 50% contra entrega,
- o pago completo antes de coordinar.

Si nadie paga, tu modelo no existe.

---

### Fase 5: Mide 3 cosas

#### 1. Liquidez

¿Cuántos pedidos reales puedes cerrar en 4-6 semanas?

Meta mínima:

- 50-100 pedidos,
- 20 restaurantes activos,
- 10 proveedores activos.

#### 2. Retención

¿Vuelven a comprar?

Meta mínima:

- >30% de restaurantes vuelven a comprar dentro de 14 días.
- >40% dentro de 30 días.

#### 3. Fuga

¿Te saltan?

Meta mínima:

- >60% de los segundos pedidos siguen pasando por ti.

Si menos del 30% sigue comprando contigo después del primer pedido, el marketplace no funciona.

---

### Fase 6: Mide economía unitaria

Para cada pedido:

- GMV,
- comisión cobrada,
- descuento,
- devoluciones,
- costo de pago,
- costo de soporte,
- costo de logística,
- tiempo invertido,
- CAC,
- contribution margin.

Si después de todo esto pierdes dinero por pedido, no tienes negocio.

---

## Presupuesto sugerido para $10K

| Rubro | Monto | Para qué |
|---|---:|---|
| Validación de demanda | $1,500 | incentivos pequeños, transporte, llamadas, reuniones |
| Logística de prueba | $3,000 | coordinar entregas, pagar motorizado/flete, consolidar pedidos |
| Pagos/facturación | $1,000 | pasarela, transferencias, comprobantes, contabilidad básica |
| Control de calidad | $1,500 | muestras, fotos, verificación, devoluciones |
| Herramientas simples | $500 | WhatsApp Business, Sheets, links de pago, correo |
| Legal/contador | $1,000 | estructura fiscal, contratos, facturación |
| Colchón operativo | $1,500 | imprevistos |

No uses $10K en desarrollo.

Usa $10K para entender si puedes vender, cobrar y repetir.

---

## Kill criteria: cuándo matar la idea

Si después de 6 semanas:

1. No consigues 20 restaurantes que compren recurrentemente.
2. No consigues 10 proveedores que acepten comisión y entreguen bien.
3. El ticket promedio es demasiado bajo.
4. La mayoría de pedidos se fugan a WhatsApp.
5. Nadie paga por adelantado.
6. Los proveedores se niegan a facturar.
7. La logística te come el margen.
8. Los restaurantes dicen “está bien”, pero no vuelven.
9. Pierdes dinero por pedido.
10. Tienes que perseguir a los proveedores para que entreguen.

Entonces no sigas construyendo la app.

---

# Preguntas que te haría en un pitch, sin anestesia

## Sobre el problema

1. ¿Cuánto dinero pierde exactamente un restaurante pequeño hoy por este problema?
2. ¿Cuántos pedidos fallidos, stockouts o desperdicios tienen al mes?
3. ¿Qué porcentaje de restaurantes ya resuelve esto con WhatsApp, teléfono o distribuidor?
4. ¿Por qué no es suficiente un grupo de WhatsApp?
5. ¿Qué pasa si el dueño del restaurante no es quien compra, sino un empleado o chef?

## Sobre la comisión

6. ¿Por qué un proveedor aceptaría 15% si su margen puede ser menor?
7. ¿Quién paga la comisión: proveedor, restaurante o ambos?
8. ¿Qué valor entregas para justificar 15%?
9. ¿Qué pasa si el proveedor baja el precio y te salta?
10. ¿Cómo evitas que el restaurante compre directo después de conocerte?

## Sobre liquidez

11. ¿Cuántos proveedores necesitas por categoría?
12. ¿Cuántos restaurantes necesitas por proveedor?
13. ¿Cuál es tu densidad mínima viable por barrio?
14. ¿Cómo consigues supply consistente?
15. ¿Qué haces si el proveedor dice “no tengo stock” después de confirmar?

## Sobre operación

16. ¿Quién entrega?
17. ¿Quién paga logística?
18. ¿Quién responde si el producto llega mal?
19. ¿Cómo gestionas devoluciones?
20. ¿Cómo garantizas calidad sin ver el producto?

## Sobre LATAM

21. ¿En qué país empezarías y por qué?
22. ¿Cómo resuelves informalidad y facturación?
23. ¿Cómo resuelves crédito?
24. ¿Cómo resuelves pagos y flujo de caja?
25. ¿Cómo superas la desconfianza inicial?

## Sobre negocio

26. ¿Cuál es tu CAC actual?
27. ¿Cuál es tu AOV?
28. ¿Cuál es tu frecuencia de compra?
29. ¿Cuál es tu contribution margin por pedido?
30. ¿Cuál es tu tasa de retención a 30 días?
31. ¿Cuál es tu tasa de fuga?
32. ¿Qué pasa si un competidor ofrece 5%?
33. ¿Qué pasa si un distribuidor tradicional copia tu app?
34. ¿Cuál es tu moat real?
35. ¿Por qué esto no es una consultoría manual que escala mal?

---

# Mi opinión brutalmente honesta

Hoy tu modelo tiene tres caminos posibles:

## Camino 1: Marketplace puro con 15%

Probablemente fracase.

Demasiada fuga, demasiado margen fino, demasiada informalidad, demasiada confianza personal, demasiada logística.

## Camino 2: Marketplace + servicios

Puede funcionar si controlas:

- pagos,
- factura,
- logística,
- garantía,
- crédito,
- compras agregadas.

Pero entonces no eres solo marketplace. Eres una empresa de abastecimiento.

## Camino 3: Operador vertical o distribuidor tecnológico

Puede ser más fuerte.

En vez de “conectar”, tú:

- compras a proveedores,
- consolidas inventario,
- entregas,
- facturas,
- garantizas,
- financias,
- y usas software para eficiencia.

Eso es más duro, más caro, más operativo, pero más defendible.

Muchos marketplace B2B que “conectan” terminan siendo operadores.

---

# Qué haría yo si fuera tú con $10K

No construiría un marketplace.

Haría esto:

## Semana 1-2

Elegiría una zona.

Entrevistaría 30 restaurantes.

Pediría sus últimas 5 listas de compra.

Registraría:

- productos,
- precios,
- proveedores,
- frecuencia,
- problemas,
- método de pago,
- factura,
- entrega.

## Semana 3-4

Elegiría 10 proveedores.

Negociaría:

- comisión 10-15%,
- pago por adelantado,
- garantía,
- stock,
- entrega,
- factura.

## Semana 5-6

Cerraría 50 pedidos manualmente.

No prometería app.

Prometería:

- ahorro de tiempo,
- mejor precio,
- calidad garantizada,
- entrega,
- factura,
- solución de problemas.

## Semana 7-8

Mediría:

- pedidos,
- GMV,
- comisión,
- retención,
- fuga,
- devoluciones,
- costos,
- contribution margin.

Si el negocio manual no funciona, la app no lo arregla.

---

# La frase que deberías grabarte

> “No tengo un problema de marketplace. Tengo un problema de liquidez, confianza, logística, pagos y economía unitaria.”

Si no resuelves eso, no tienes una startup. Tienes una app con usuarios que te van a saltar.