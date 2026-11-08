# Claude Haiku 5.5 — strategy/business_model_validation

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 27.962s | tokens_per_second: 176.4
- input_tokens: 290 | output_tokens: 4932

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

# Pitch brutal: marketplace restaurantes-proveedores

Antes de las preguntas: tu hipótesis es "pierden mucho tiempo", pero eso no es lo mismo que "pagarían por no perderlo". Mucha gente se queja de su tiempo y luego no cambia nada. Y el restaurante no compra tiempo, compra precio, calidad y confianza. Si lo que resuelves es tiempo, tu propuesta de valor es débil.

## 1. Los 5 riesgos principales

**a) Desintermediación.** Restaurante y proveedor se conocen, se hablan por WhatsApp y después negocian directo para no pagarte el 15%. Tu comisión es la razón por la que te saltan. Si no tienes retención real (crédito, logística, facturación, garantías), sobrevives solo mientras no te conozcan.

**b) El 15% pesa mucho sobre un margen que ya es delgado.** Un restaurante pequeño tiene margen neto de 3-8% y su food cost ronda 28-35%. Un 15% sobre compras de $1,000 USD al mes son $150 que salen de su utilidad. Pregúntate quién absorbe esa comisión: si la paga el proveedor, reduce su margen (que ya es 10-20% en el mejor caso). Si la paga el restaurante, la adopción se cae. Si la pagan los dos, cada lado siente que paga por ti sin razón clara.

**c) Economía de volumen pequeño y logística cara.** Un restaurante pequeño compra poco, con pedidos frecuentes, perecederos, en horarios de mercado. Cada entrega cuesta casi lo mismo sin importar el tamaño del pedido. Si no tienes densidad en una zona (muchos restaurantes cerca de los mismos proveedores), el costo de logística se come tu comisión.

**d) Cadena de frío, calidad y disputas.** Verduras, pescado, lácteos. Si llega mal, ¿quién responde? ¿Quién hace el reembolso? ¿Quién arbitra? Cada disputa mal resuelta te cuesta el restaurante y, peor, el proveedor. Y tú no controlas la calidad de lo que no tocas.

**e) Cold start de dos lados.** Necesitas proveedores para atraer restaurantes y restaurantes para atraer proveedores. Si arrancas con 5 proveedores y 20 restaurantes en una zona, la red no tiene efecto de red todavía; solo tienes dos grupos de clientes que se aburren.

## 2. ¿Por qué podría NO funcionar en LATAM específicamente?

- **Informalidad.** Mucho proveedor opera sin facturas, con efectivo, o sin cuenta bancaria formal. Tu marketplace, si pide datos fiscales, excluye a tus mejores proveedores locales. Si no los pide, tienes un problema de cumplimiento y de confianza.
- **Facturación electrónica obligatoria** (CFDI en México, NF-e en Brasil, factura electrónica en Colombia, etc.). Cada país tiene reglas distintas y costosas. Esto es un proyecto en sí mismo.
- **Crédito informal ("fiado").** El proveedor le fía al restaurante y se paga a fin de semana o de mes. Tu modelo de pago al momento rompe esa relación, que es precisamente lo que mantiene vivos a ambos. Si lo copias, asumes riesgo de crédito. Si no, pierdes a la mitad de la demanda real.
- **Inflación y volatilidad de precios.** En Argentina, Turquía o en momentos de alta inflación, los precios de insumos cambian semanalmente. Tu catálogo y tus márgenes se desfasan constantemente.
- **Restaurantes con margen mínimo y poca digitalización.** Muchos dueños no usan apps de forma regular y gestionan todo por WhatsApp y teléfono. La fricción de adopción es más alta de lo que se ve en Silicon Valley.
- **Los distribuidores tradicionales ya hacen esto bien**, con relación personal, entrega diaria y crédito. Tu ventaja tiene que ser concreta, no "digital".
- **Competencia de plataformas grandes.** Si Mercado Libre, Rappi u otra plataforma con logística y base de usuarios entra al vertical, tu nicho de "ingredientes para restaurantes" se vuelve un feature. Verifica el estado actual del mercado en tu país antes de pitchear.

## 3. ¿Qué tendría que ser verdad para que funcione?

Estas son las suposiciones clave que tendrías que probar, en orden de importancia:

1. **Los restaurantes pagan por la solución, no solo la aprueban.** Medido en pedidos recurrentes, no en encuestas.
2. **El ahorro de tiempo (o de precio) es suficiente para justificar el 15%.** Necesitas que el restaurante reciba más valor que el costo de la comisión.
3. **Los proveedores aceptan la comisión sin desintermediar** durante al menos 12 meses. Esto requiere que tú les des algo que no puedan hacer solos (clientes nuevos, cobranza, financiamiento, logística).
4. **Hay densidad geográfica suficiente.** Un número mínimo de restaurantes y proveedores por zona de entrega, para que la logística sea rentable.
5. **El ticket promedio por restaurante es suficiente.** Ejemplo: si la comisión media es de $100-150 USD/mes por restaurante, necesitas un CAC muy bajo y retención alta para que el LTV justifique todo.
6. **Puedes cobrar y pagar sin asumir un riesgo de crédito insostenible.**
7. **La calidad y la cadena de frío se pueden controlar** con un costo razonable.
8. **Puedes operar legalmente** (fiscal, sanitario, logística) sin que tu margen se vaya en cumplimiento.

Si no puedes probar la 1 y la 3 en los primeros 3 meses, todo lo demás es teoría.

## 4. El escenario de fracaso rápido

Lo más probable: lanzas en una ciudad, consigues 15-30 restaurantes que hacen 2-3 pedidos al mes cada uno. Los proveedores se dan cuenta de que el restaurante les llama directo después del primer pedido, y empiezan a cobrar por fuera. Tu comisión se evapora, el restaurante vuelve a su proveedor de siempre porque es más confiable y le fía, y tú te quedas con un GMV de $15K USD al mes, una logística que cuesta más que tu comisión, y un equipo que tiene que decidir si pivotea o cierra.

Señales de alarma tempranas que deberías ver en semanas, no meses:
- Pedidos que se hacen una vez y no se repiten.
- Restaurantes que piden pero no pagan por el servicio, o piden "solo esta vez".
- Proveedores que preguntan por fuera cómo cobrar sin tu comisión.
- Devoluciones o disputas por calidad en más del 5% de pedidos.
- Costo de adquisición de restaurante mayor a 3-4 meses de comisiones.

## 5. Si solo tuviera $10K para validar

No construiría la app. Haría un **concierge MVP** en 8-10 semanas:

**Semana 1-2: Entrevistas (sin presupuesto relevante).** 30 dueños de restaurantes pequeños y 10 proveedores. Pregunta por el último pedido que hicieron, cuánto tiempo les tomó, qué pasó cuando algo salió mal, cuánto pagan hoy por los insumos, y qué harían si tuvieran que pagarte una comisión. Si la mayoría no tiene un dolor específico y reciente, para aquí.

**Semana 2-6: Operación manual.** Elige una sola zona y una sola categoría (por ejemplo, verduras y hierbas para 15-20 restaurantes). Tú haces de plataforma: recibes pedidos por WhatsApp o un formulario, los distribuyes entre 3-5 proveedores, cobras y entregas tú o contratas un mensajero. Cobras la comisión de verdad desde el primer pedido.

**Métricas que defines antes de empezar:**
- Pedidos por restaurante por semana (meta: al menos 1-2 semanas consecutivas de pedidos sin que tengas que insistir).
- Tasa de retención a 4 semanas (meta: >60%).
- % de pedidos que se hacen directo entre restaurante y proveedor después de conocerse (si es >30% en el mes 2, tienes un problema de desintermediación).
- Disposición a pagar: ¿aceptan la comisión sin negociar? ¿Qué porcentaje aceptan en la primera vez?
- Costo logístico por pedido vs. comisión cobrada (debe ser viable en escala, aunque no lo sea en el piloto).
- Número de proveedores que aceptan la comisión sin pedirte exclusividad ni descuentos.

**Distribución aproximada de los $10K:**
- $2K: entregas y mensajería durante el piloto.
- $1.5K: herramientas (WhatsApp Business, formularios, facturación básica, pagos).
- $1K: asesoría legal y fiscal para entender el marco en tu país.
- $1K: tiempo de entrevistas, incentivos para restaurantes del piloto.
- $2K: reserva para inventario o pagos anticipados si tienes que garantizar el pedido.
- $2.5K: colchón para imprevistos y para el mes siguiente si los resultados son buenos.

**Criterio de decisión al final de 8-10 semanas:**
- **Sigue** si hay pedidos recurrentes, proveedores que se quedan y restaurantes que pagan la comisión sin que la negocies.
- **Pivota** si el valor está en otra parte (por ejemplo, crédito a restaurantes, o precio consolidado de compra en vez de logística).
- **Cierra o archiva** si los restaurantes aprecian la idea pero no pagan, o si la desintermediación aparece en la primera mitad del piloto.

---

## Las preguntas que te harán en la sala

1. ¿Cuál es tu evidencia de que el restaurante paga por esto, no solo lo aprueba?
2. ¿Quién paga la comisión y por qué no te la van a saltar?
3. ¿Cuál es tu take rate efectivo después de logística y mermas?
4. ¿Cuántos restaurantes necesitas por zona para que la logística tenga sentido?
5. ¿Qué pasa cuando el proveedor y el restaurante se conocen?
6. ¿Cómo manejas el crédito y la cobranza sin ser un banco?
7. ¿Qué te impide que un distribuidor tradicional o una plataforma grande haga esto mañana?
8. ¿Cuánto cuesta adquirir un restaurante y cuánto tiempo tarda en recuperarse?
9. ¿Cuál es tu plan para la informalidad de tus proveedores?
10. Si el piloto sale bien en una ciudad, ¿qué tan difícil es replicarlo? ¿Qué se rompe al escalar?

Si no puedes responder bien las 3 primeras con datos reales de tu piloto, no estás listo para pitchear. Estás listo para validar.