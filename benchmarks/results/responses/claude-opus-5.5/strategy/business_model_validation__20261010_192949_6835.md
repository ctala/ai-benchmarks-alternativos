# Claude Opus 5.5 — strategy/business_model_validation

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.95 | quality: 10.0
- latency_total: 63.17s | tokens_per_second: 88.3
- input_tokens: 290 | output_tokens: 5581

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

# Modo VC escéptico: activado

Antes de las 5 preguntas, el problema de fondo: **tu hipótesis ya trae la solución adentro.** "Quieren una solución digital" no es un problema, es lo que tú quieres venderles. El dueño de una fonda en Bogotá o CDMX ya resolvió "llamar a múltiples proveedores": se llama WhatsApp, le toma 15 minutos y es gratis. ¿Por qué pagaría por reemplazarlo?

---

## 1. Los 5 riesgos principales

**Riesgo #1: El 15% de comisión no sobrevive a la aritmética del food service**
- Un restaurante pequeño opera con márgenes netos de 3-8%. El costo de ingredientes es 28-35% de sus ventas.
- Un distribuidor de alimentos opera con márgenes brutos de 15-25% y márgenes operativos de 2-5%.
- **Le estás pidiendo 15% a una industria que vive de 3%.** Si cobras al proveedor, sube precios o se va. Si cobras al restaurante, compra directo.
- Pregunta de pitch: *"¿Quién paga exactamente ese 15%? ¿Y por qué no se iría mañana?"*

**Riesgo #2: Desintermediación (leakage). Este es el que te mata.**
- Tu marketplace es útil exactamente una vez: cuando el restaurante descubre al proveedor. Después intercambian números de WhatsApp y te cortan.
- Las compras de ingredientes son recurrentes, predecibles y relacionales. Es el peor caso posible para un marketplace. A Upwork y Thumbtack les cuesta lo mismo, y su relación comprador-vendedor es mucho menos repetitiva que la tuya.
- Pregunta de pitch: *"¿Qué valor das en la orden número 10 que justifique tu comisión?"*

**Riesgo #3: Logística. ¿Quién entrega?**
- Si los proveedores entregan, la calidad del servicio no la controlas tú. Cuando un sábado no lleguen los tomates, el restaurante te culpa a ti.
- Si entregas tú, ya no eres marketplace: eres distribuidor con márgenes de distribuidor y necesidades de capital de distribuidor.
- Los productores locales pequeños tienen volúmenes inconsistentes, calidad variable y casi nunca cadena de frío.

**Riesgo #4: Liquidez hiperlocal y cold start**
- Esto no escala como software. Cada ciudad, y en la práctica cada zona, es un marketplace nuevo que tienes que encender desde cero con ventas en campo.
- Necesitas suficientes proveedores para que el restaurante encuentre todo lo que busca, y suficientes restaurantes para que el proveedor se moleste en usarte. Si el restaurante igual tiene que llamar a 3 proveedores por fuera para completar su lista, no le resolviste nada.

**Riesgo #5: Tu cliente se muere**
- Los restaurantes pequeños tienen tasas de cierre altísimas en los primeros años. Tu churn tiene un piso estructural que no depende de tu producto.
- Combinado con un CAC alto (venta en campo, persona por persona) y un ticket bajo, el LTV/CAC se ve feo antes de empezar.

---

## 2. ¿Por qué podría NO funcionar en LATAM específicamente?

1. **El crédito es el producto real.** En LATAM el proveedor le da crédito al restaurante: fiado, 15-30 días, "me pagas el viernes". Esa relación de confianza es el verdadero lock-in. Si tu app exige pago upfront, pierdes. Si das crédito tú, ahora eres una fintech con riesgo de cartera sobre negocios que cierran seguido.

2. **La informalidad.** Muchos proveedores locales no facturan, cobran en efectivo y no quieren aparecer en una plataforma que deja rastro de cada transacción. Tu proveedor ideal, el pequeño productor local, es justamente el más informal.

3. **WhatsApp ya ganó.** No compites contra la nada. Compites contra una herramienta gratis, universal, que ambos lados ya dominan y que incluye fotos, audios y negociación.

4. **Las centrales de abasto.** Corabastos, la Central de Abasto de CDMX y la CEAGESP en São Paulo fijan precios que difícilmente vas a igualar si le sumas un 15%. Muchos dueños van ellos mismos a las 5am. Es parte de su rutina y de su ventaja de precio.

5. **El precedente.** Frubana (Colombia) levantó más de $200M para atacar algo muy parecido, con modelo de inventario y logística propia. Después hizo despidos masivos y se retiró de México y Brasil. Hay otros jugadores B2B de food supply en la región que sufrieron igual. Un VC te va a preguntar: *"Si ellos con cientos de millones no lo lograron, ¿qué sabes tú que ellos no sabían?"* Necesitas una respuesta muy buena.

6. **Macro.** Inflación, volatilidad cambiaria (Argentina es el caso extremo) y precios de productos frescos que cambian semanalmente hacen que los catálogos con precios fijos queden obsoletos rápido.

---

## 3. ¿Qué tendría que ser verdad? (Key assumptions)

Ordenadas de más a menos peligrosa:

| # | Supuesto | Cómo se ve si es falso |
|---|----------|------------------------|
| 1 | El dolor real es **tiempo**, y no precio, crédito o confiabilidad | Te dicen "me interesa si es más barato" |
| 2 | Alguien está dispuesto a pagar **~15%** de forma sostenida | Aceptan 2-5% como máximo, o nada |
| 3 | Puedes **evitar la desintermediación** con valor continuo (crédito, consolidación, garantía de entrega, facturación) | El GMV por restaurante cae después del mes 2 |
| 4 | Los proveedores locales pueden ofrecer **volumen y calidad consistentes** | Faltantes frecuentes y quejas de calidad |
| 5 | La **frecuencia y el ticket** dan unit economics positivos | Ver el cálculo abajo |
| 6 | Puedes adquirir restaurantes con **CAC bajo**, no solo con vendedores en la calle | CAC mayor a 6 meses de margen de contribución |

**El cálculo que te van a hacer en el pitch:**
- Restaurante pequeño en LATAM: compra quizás $2,000-5,000 USD al mes en insumos.
- Tú no capturas el 100%, con suerte un 20-30% (una o dos categorías). Digamos $800/mes.
- 15% de $800 = **$120/mes de ingreso bruto por restaurante.**
- Réstale pagos, soporte, incidentes y logística si la absorbes. Te quedan quizás $40-70 de margen de contribución.
- Con un CAC de $150-300 por venta en campo y un churn de 4-6% mensual... *"muéstrame cuándo recuperas el CAC."*

---

## 4. El escenario de fracaso rápido

Así es como se ve, mes a mes:

- **Mes 1-2:** Gastas tu presupuesto en construir una app bonita. Haces onboarding de 40 restaurantes y 15 proveedores con trabajo de calle. Llegan las primeras órdenes y celebras el GMV.
- **Mes 3:** Un proveedor falla una entrega un viernes. Dos restaurantes se van. Otro proveedor te dice que el 15% le come el margen y sube precios dentro de la app. Los restaurantes notan que es más caro que por WhatsApp.
- **Mes 4:** Los pares restaurante-proveedor que funcionaban bien empiezan a hacer pedidos por fuera. Tu GMV por cliente cae 60% y la retención de cohortes se desploma.
- **Mes 5-6:** Bajas la comisión al 5% para retener. Ahora tu modelo no paga ni tu equipo. Te quedas sin runway.

**La causa raíz:** construiste la app antes de validar que alguien pagaría la comisión de forma recurrente, y elegiste un modelo cuyo valor se agota después de la primera transacción exitosa.

---

## 5. Si solo tuviera $10K para validar

**Regla #1: No construyas una app.** Ni un dólar en desarrollo hasta tener evidencia de recurrencia y de que alguien paga.

**Fase 1: Descubrimiento (semanas 1-3, ~$500)**
- Entrevista a 40+ dueños de restaurantes. Usa preguntas tipo *The Mom Test*: no preguntes "¿usarías una app?". Pregunta "cuéntame cómo hiciste tu último pedido de verduras", "¿cuánto tiempo te tomó?", "¿qué salió mal la última vez?", "¿a quién le pagas y cuándo?".
- Entrevista a 15 proveedores: ¿qué margen tienen? ¿Cuánto pagarían por un cliente nuevo? ¿Cuánto les cuesta cobrar?
- **Qué buscas:** que el dolor dominante aparezca solo, sin que tú lo sugieras. Si nadie menciona tiempo y todos mencionan precio o crédito, tu hipótesis murió y te ahorraste $9,500.

**Fase 2: Concierge MVP (semanas 4-12, ~$7,000)**
- Una zona, una categoría (por ejemplo, frutas y verduras), 15-25 restaurantes y 5-8 proveedores.
- Todo manual: un número de WhatsApp Business, una hoja de cálculo, tú coordinando pedidos y resolviendo problemas.
- **Cobra desde el día 1.** Prueba take rates distintos (5%, 10%, 15%) o un fee fijo mensual con distintos clientes.
- Presupuesto: transporte y tiempo en campo (~$2,000), un asistente operativo part-time (~$3,000), un colchón para cubrir incidentes o garantías de entrega (~$1,500), herramientas (~$500).

**Fase 3: Medir y decidir (~$2,500 de reserva)**

Métricas que importan:
- **Retención semana 8:** ¿qué % sigue pidiendo a través de ti?
- **Leakage:** ¿cuántos pares restaurante-proveedor se fueron por fuera?
- **Take rate real tolerado:** ¿en qué comisión dejan de comprar?
- **Wallet share:** ¿qué % de su compra total pasa por ti?

**Criterios de muerte (defínelos ANTES de empezar):**
- Si la retención a 8 semanas es menor al 40% → el modelo no funciona.
- Si nadie acepta más de 5% → el marketplace con 15% no existe, considera pivotar.
- Si el leakage es mayor al 30% → necesitas otro modelo de captura de valor.

---

## Lo que un VC querría oír al final

Si la validación sale mal (y es probable), estos son los pivotes que suelen tener más sentido en este espacio:

- **SaaS para proveedores:** herramienta de pedidos, cobranza e inventario con fee mensual. Choco, en Europa, se movió de marketplace a software para distribuidores.
- **Crédito embebido:** si el dolor real es liquidez, financiar las compras del restaurante es el producto y la comisión del marketplace es secundaria.
- **Compras agrupadas:** agregar la demanda de muchos restaurantes pequeños para negociar precios de restaurante grande. Ahí sí hay valor recurrente que justifica una comisión.

**La pregunta final que te haría en el pitch:** *"Después del pedido número 10, ¿qué le das al restaurante que no le da WhatsApp, y por qué le vale más que tu comisión?"*

Si no tienes una respuesta clara y validada con datos de clientes reales, no tienes negocio todavía. Tienes una hipótesis, y los $10K son para descubrir si vale la pena.