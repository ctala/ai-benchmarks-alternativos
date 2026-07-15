# Claude Fable 5 — strategy/business_model_validation

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.96 | quality: 10.0
- latency_total: 35.522s | tokens_per_second: 57.7
- input_tokens: 288 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación crítica y detallada que un emprendedor podría aplicar directamente.

## Respuesta completa

# Vale. Modo VC escéptico activado.

Antes de empezar: tu hipótesis ni siquiera está bien formulada. "Pierden mucho tiempo llamando" no es un problema por el que alguien paga. La gente odia muchas cosas y no paga por resolverlas. Pero vamos por partes.

---

## 1. Los 5 riesgos principales

**Riesgo #1: La comisión del 15% es una fantasía.**
Los márgenes en distribución de alimentos son de 5-15%. Le estás pidiendo al proveedor que te dé *todo su margen* o al restaurante (que opera con márgenes del 3-9%) que absorba un sobreprecio. ¿Quién paga tu 15%? Nadie tiene ese dinero en esta cadena. Este solo punto puede matar el negocio.

**Riesgo #2: Desintermediación inmediata.**
Conecto al restaurante con el proveedor de tomates. Primera compra por tu app. Segunda compra: se mandan un WhatsApp directo y te saltan. No tienes ningún mecanismo de retención. La compra de ingredientes es *recurrente y con el mismo proveedor* — el peor escenario posible para un marketplace transaccional.

**Riesgo #3: El problema del huevo y la gallina en un mercado hiperlocal.**
No te sirve tener 500 proveedores en todo el país. Necesitas densidad *por barrio/ciudad*. Un marketplace de logística de alimentos frescos es N marketplaces locales que tienes que arrancar uno por uno. CAC brutal, escalabilidad lenta.

**Riesgo #4: No resuelves la logística, y la logística ES el negocio.**
Conectar es lo fácil. ¿Quién entrega? ¿Quién garantiza calidad? ¿Qué pasa cuando llegan aguacates podridos? ¿Quién maneja devoluciones de producto perecedero? Si no tocas logística, eres un directorio glorificado. Si la tocas, eres una empresa de logística con márgenes de terror.

**Riesgo #5: Este cementerio ya está lleno.**
Frubana, Chiper, Jüsto B2B, Cayena en Brasil... levantaron cientos de millones y varios pivotaron o murieron intentando exactamente esto. ¿Qué sabes tú que ellos no sabían con $100M+ en el banco? Necesitas una respuesta real a esto o no pasas del primer slide.

---

## 2. Por qué podría NO funcionar en LATAM específicamente

- **La relación proveedor-restaurante es personal y basada en crédito informal.** El proveedor le fía al restaurante 15-30 días porque lo conoce hace años. Tu app no da crédito → tu app pierde contra el "fiado". Este es probablemente EL factor cultural que te destruye.
- **WhatsApp ya resolvió el problema que crees que existes para resolver.** El restaurantero manda un audio: "Don José, lo de siempre y 2 cajas extra de limón". Diez segundos. Tu app tiene que ser mejor que eso. No lo es.
- **Informalidad fiscal masiva.** Muchas transacciones son en efectivo, sin factura. Tu plataforma formaliza y deja rastro fiscal. Para muchos, eso es una razón para NO usarte.
- **El "tiempo perdido llamando" no le duele al dueño.** Le duele al empleado, que no decide. Y en LATAM la mano de obra es barata — el dueño prefiere que el chico llame a pagar 15%.
- **Fragmentación extrema del supply.** Muchos proveedores son señores en un mercado de abastos sin smartphone dedicado al negocio, sin inventario digitalizado, sin precios fijos (¡el precio cambia diario y se negocia!). Digitalizar catálogos con precios dinámicos de perecederos es un infierno operativo.

---

## 3. Qué tendría que ser verdad (key assumptions)

Para que esto funcione, TODAS estas cosas deben ser ciertas:

1. Los restaurantes valoran ahorrar tiempo/dinero **más de lo que valoran la relación y el crédito** con su proveedor actual.
2. Existe un take rate viable — probablemente **no 15%, sino 3-7%**, o el valor viene de otro lado (fintech, crédito, agregación de compra).
3. Hay una razón estructural para **no desintermediarte**: crédito, precios agregados por volumen, logística consolidada, o pagos.
4. Puedes lograr **densidad de liquidez en UNA ciudad** con capital razonable.
5. Los proveedores pueden y quieren **mantener catálogo y precios actualizados** (spoiler: no quieren).
6. La frecuencia de compra + tu retención generan LTV que justifica el CAC de vender puerta a puerta a restaurantes.

Si la #3 falla, todo lo demás es irrelevante. **Tu verdadero producto probablemente no es el marketplace — es el crédito o la logística consolidada.** El marketplace es solo el canal.

---

## 4. Escenario de fracaso rápido

**Mes 1-3:** Consigues 30 restaurantes y 15 proveedores con esfuerzo heroico. Todos dicen que "la idea es buenísima".

**Mes 4:** GMV inicial decente. Celebras.

**Mes 5-6:** Retención se desploma. Los restaurantes hicieron 1-2 pedidos y volvieron a WhatsApp con el proveedor que conocieron *gracias a ti*. Los proveedores no actualizan