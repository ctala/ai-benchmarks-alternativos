# GPT-6 Luna — strategy/business_model_validation

- model_id: `openai/gpt-6-luna`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 28.413s | tokens_per_second: 110.2
- input_tokens: 165 | output_tokens: 3132

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

Voy a ser directo: **“los restaurantes pequeños pierden tiempo llamando a proveedores” no es todavía una tesis de negocio**. Es una molestia. No demuestra que pagarían por resolverla, que los proveedores aceptarían tu comisión ni que puedas procesar pedidos con margen.

La pregunta incómoda es: **¿por qué cambiarían una manera imperfecta de comprar, pero que ya conocen, por una plataforma que quizá les cueste más y les falle justo cuando necesitan ingredientes?**

## 1. Los 5 riesgos principales

### 1) El 15% puede destruir la economía de la transacción

Si el proveedor opera con márgenes estrechos, una comisión del 15% puede ser inaceptable. Si la paga el restaurante, tus precios pueden quedar por encima de los del canal habitual. Si la pagas tú, quizá no quede margen para soporte, pagos, devoluciones, ventas y cualquier problema de entrega.

Y si para que el modelo funcione tienes que subsidiar precios o transporte, **no tienes un marketplace rentable; tienes una operación logística financiada por capital de riesgo**.

Haz las cuentas por pedido, no por GMV:

- comisión cobrada;
- coste de cobro;
- coste de atención y resolución de incidencias;
- descuentos o subsidios;
- devoluciones, faltantes y producto dañado;
- coste de conseguir y activar al cliente.

Un 15% sobre una transacción no es un 15% de margen neto.

### 2) El problema puede no ser suficientemente doloroso

“Llamar a varios proveedores” suena ineficiente, pero tal vez no sea el principal problema del restaurante. Quizá su prioridad sea el precio, la calidad constante, el crédito, que le entreguen temprano o que le resuelvan un faltante el mismo día.

Si el dueño tarda diez minutos en hacer pedidos y considera que el sistema actual funciona, una app más cómoda no basta. **Ahorro de tiempo no implica disposición a pagar ni cambio de hábito.**

Pregunta clave: ¿qué hace el restaurante hoy cuando un proveedor falla? Si la respuesta es “llamo a mi contacto de siempre”, tu producto puede ser menos útil de lo que crees.

### 3) El marketplace necesita densidad local, no una app bonita

Un restaurante quiere variedad, disponibilidad y entrega fiable. Un proveedor quiere pedidos suficientes y predecibles. Si empiezas con pocos compradores y pocos proveedores, ambos lados encontrarán una razón para no usarlo.

Además, la liquidez tiene que existir **por zona, categoría y franja de entrega**. Tener cien proveedores registrados en una ciudad no sirve si el comprador de cierto barrio no encuentra el ingrediente que necesita para mañana.

Este negocio puede ser local y operativo mucho antes de poder ser tecnológico y escalable.

### 4) La calidad y el cumplimiento pueden comerse la experiencia

Los ingredientes no son productos perfectamente estandarizados. Hay variaciones de madurez, tamaño, frescura, peso y disponibilidad. Puede haber faltantes, sustituciones y entregas tardías. ¿Quién responde cuando llega mal el producto: tú, el proveedor o el restaurante?

Si respondes tú, asumirás trabajo y posiblemente pérdidas. Si no respondes tú, el cliente puede concluir que la plataforma no resuelve nada. **Intermediar el pedido no te libera de ser responsable de la experiencia.**

### 5) Puedes adquirir clientes que no repiten, o que te desintermedian

Un restaurante puede probar la plataforma para conseguir una cotización y luego llamar directamente al proveedor. El proveedor también puede captar al cliente y saltarse tu comisión en el siguiente pedido.

Incluso sin desintermediación, los pedidos pequeños y dispersos pueden hacer que el coste de venta y soporte por cliente sea demasiado alto. El riesgo es acabar con una base de usuarios que compra de vez en cuando, pero exige atención manual en cada pedido.

## 2. ¿Por qué podría no funcionar en LATAM específicamente?

“LATAM” no es un mercado único. La dinámica de compra en una ciudad, país o categoría puede ser muy distinta de otra. Pero hay fricciones que deberías investigar antes de asumir que un modelo probado en otro sitio se traslada:

- **Relaciones personales y confianza.** Muchos compradores ya tienen contactos de años. Ese proveedor quizá acepta pedidos por WhatsApp, conoce las preferencias del restaurante y da flexibilidad informal. Tu alternativa digital tiene que superar esa relación, no simplemente reemplazar una llamada.
- **Crédito y pagos informales.** Si el proveedor da crédito o permite arreglos que tu plataforma no puede ofrecer, podrías ser más cómoda, pero menos valiosa para el flujo de caja del restaurante.
- **Fragmentación y calidad variable.** Puede que no haya catálogo, inventario y precios actualizados de forma fiable. Entonces no estás automatizando un proceso ordenado: estás creando y manteniendo esa información proveedor por proveedor.
- **Logística difícil de estandarizar.** Tráfico, distancias, horarios de entrega y cadena de frío varían mucho. Si prometes consolidar compras de varios proveedores, pregunta quién junta los productos y quién paga ese coste.
- **Informalidad y documentación.** Facturación, impuestos, medios de pago y prácticas comerciales pueden complicar la conciliación y el servicio. No asumas que todos los proveedores podrán integrarse o trabajar bajo tus términos.
- **Alternativas ya “suficientemente buenas”.** WhatsApp, llamadas, distribuidores tradicionales, mercados mayoristas y vendedores que entregan pueden ser poco elegantes, pero baratos y conocidos. Un producto digital no gana solo por parecer moderno.

La tesis no debería ser “en LATAM no hay buena tecnología para esto”. Debería ser algo concreto, como: **“En esta ciudad y esta categoría, los restaurantes pierden X horas o dinero, y pagarán Y para evitarlo, porque nosotros resolvemos Z mejor que sus canales actuales.”**

## 3. ¿Qué tendría que ser verdad para que funcione?

Estas son las hipótesis que necesitas probar con comportamiento real, no con opiniones:

1. **El problema importa lo suficiente.** Los restaurantes cambian su proceso actual porque les reduces un coste relevante: tiempo, precio, faltantes, errores o incertidumbre.
2. **Hay frecuencia y volumen.** Compran con suficiente recurrencia y ticket para que tus ingresos por cliente cubran venta, soporte y operación.
3. **Los proveedores aceptan la comisión o el coste equivalente.** Y siguen obteniendo más valor del que pierden pagando por acceder a esos clientes.
4. **Puedes mantener precios competitivos.** El restaurante no tiene que pagar una prima que anule el beneficio de la conveniencia.
5. **La oferta es fiable.** Inventario, precios, calidad y entrega tienen una consistencia suficiente para que el restaurante vuelva.
6. **Los clientes repiten dentro de la plataforma.** No usan el marketplace solo para descubrir al proveedor y luego comprar por fuera.
7. **El pedido tiene contribución positiva.** Después de costes variables, no dependes de subsidios, de trabajo manual ilimitado o de una tarifa mayor que el mercado no toleraría.
8. **Puedes crear densidad en una zona.** Hay suficientes compradores y proveedores cerca para cumplir una promesa útil y rentable.
9. **La comisión no es tu única propuesta de valor.** Si solo conectas comprador y vendedor, ambos tienen un incentivo inmediato para excluirte.

En un pitch te preguntaría: **¿qué dato tienes que demuestre cada una de estas cosas?** “Los restaurantes nos dijeron que les interesa” no cuenta.

## 4. Escenario de fracaso rápido

El escenario más probable de fracaso rápido sería este:

Lanzas una app con varios proveedores, consigues algunos restaurantes curiosos y subsidias las primeras compras. Los proveedores cargan catálogos incompletos o cambian disponibilidad y precios. Los restaurantes hacen uno o dos pedidos, encuentran faltantes o precios menos competitivos que con sus contactos habituales y vuelven a WhatsApp. Algunos proveedores contactan directamente a los restaurantes. Para retener a los demás, tu equipo empieza a confirmar cada pedido manualmente y resolver incidencias.

Resultado: **mucho GMV aparente, poca repetición, comisión cuestionada y costes operativos altos**. Cierras cuando descubres que cada nuevo cliente añade trabajo antes de añadir margen.

Fracasa rápido si ves esto en la prueba:

- la mayoría de los restaurantes prueba una vez y no repite;
- los proveedores solo participan si no cobras comisión o les garantizas volumen;
- el cliente compra fuera de la plataforma en cuanto conoce al proveedor;
- necesitas intervenir manualmente en casi todos los pedidos;
- el pedido solo funciona si tú subvencionas precio o entrega;
- el margen por pedido es negativo incluso antes de contar el equipo y el producto.

## 5. Si solo tuviera $10K para validar, ¿qué haría?

**No construiría una app completa.** Gastaría el dinero en comprobar si hay pedidos repetidos, comisión aceptada y operación viable en un lugar muy acotado.

### Semana 1: elegir un campo de prueba

Escogería **una ciudad, una zona y una categoría de ingredientes**. No empezaría intentando abastecer a cualquier restaurante con cualquier producto. Elegiría una categoría frecuente y suficientemente estandarizable para probar la compra.

Hablaría con unos 20 restaurantes y 10 proveedores, pero no para preguntar “¿usarías esto?”. Les pediría que me enseñaran sus últimas compras, precios, problemas y método de pedido. Intentaría obtener facturas, listas o registros reales. Querría saber:

- cuánto compran y con qué frecuencia;
- a quién compran hoy y por qué;
- qué les falla en el proceso actual;
- qué condiciones de pago y entrega esperan;
- qué producto les hizo cambiar de proveedor la última vez.

### Semanas 2–6: operar manualmente

Montaría una página sencilla y un flujo por WhatsApp o formulario. El equipo haría manualmente el trabajo de catálogo, cotización, confirmación y seguimiento. Eso no es una versión vergonzosa del producto: **es la forma barata de descubrir qué producto necesitas construir**.

Buscaría reclutar aproximadamente 20–30 restaurantes y un grupo pequeño de proveedores que puedan atender la misma zona. Intentaría procesar pedidos pagados, sin fingir demanda mediante descuentos. Probaría explícitamente distintos esquemas: comisión al proveedor, tarifa al comprador o una combinación. No asumiría que el 15% es correcto.

Mediría por pedido y por restaurante:

- conversión de cotización a compra;
- repetición en 30 días;
- valor y frecuencia del pedido;
- porcentaje de productos disponibles tal como se ofrecieron;
- entregas completas y a tiempo;
- incidencias y tiempo de soporte;
- margen de contribución después de costes variables;
- cuántos compradores y proveedores intentan cerrar por fuera.

### Presupuesto ilustrativo

- **$2,000:** entrevistas, visitas y tiempo de venta en campo;
- **$3,000:** operación piloto, coordinación y soporte manual;
- **$1,500:** herramientas simples —página, formularios, CRM ligero, automatizaciones básicas—;
- **$2,000:** costes de pruebas de entrega, calidad o incidencias;
- **$1,500:** reserva para repetir pruebas o cubrir imprevistos.

Los montos dependen de la ciudad y de si pagas al equipo fundador, pero la regla sería la misma: **no gastar una parte grande en software antes de demostrar repetición y economía unitaria.**

### Qué consideraría una señal prometedora

No tomaría estos números como verdades universales, sino como puertas de decisión iniciales:

- al menos 10 restaurantes hacen pedidos pagados;
- una proporción significativa vuelve a comprar sin descuento;
- los proveedores aceptan una tarifa que deje al restaurante un precio competitivo;
- el servicio cumple de forma consistente;
- los pedidos pueden gestionarse sin que cada uno requiera una cantidad de trabajo manual incompatible con el margen;
- la contribución por pedido se acerca a positiva o muestra una ruta creíble para serlo sin subsidios permanentes.

Si no hay repetición, **no arregles eso añadiendo funciones a la app**. Averigua si el problema no duele, si la oferta es mala o si la comisión no cabe en la economía del canal.

La prueba más importante no es que un restaurante diga que la idea le gusta. Es que **cambie un pedido real a tu canal, pague, vuelva a comprar y deje suficiente margen para que tú no tengas que hacer de distribuidor gratis**.