# Nemotron 3 Super — strategy/business_model_validation

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 15.847s | tokens_per_second: 195.7
- input_tokens: 191 | output_tokens: 3101

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

Aquí tienes la ducha de agua fría que pediste. Sin palmaditas en la espalda.

---

### 1. Los 5 riesgos principales de este modelo

**1. Disintermediación inmediata**
Tu producto no es tecnología; es una presentación. En cuanto un restaurante y un proveedor se conocen a través de tu plataforma, tienen un incentivo económico masivo para nunca volver a usarla: ahorrarse tu 15%. En mercados de insumos, donde la confianza se basa en relaciones personales, el marketplace se vuelve un directorio caro que se salta al segundo pedido.

**2. El 15% le come la utilidad al restaurante**
Un restaurante pequeño opera con márgenes netos del 3% al 5%. Tú le pides el 15% sobre el *costo de los bienes vendidos* (COGS), que suele ser el 30%-35% de sus ingresos. Eso significa que le estás quitando una porción enorme de su utilidad neta. No es una "tarifa de conveniencia"; es un impuesto que puede hacer que el negocio deje de ser viable.

**3. El problema del pollo y el huevo, multiplicado por geografía**
Un marketplace de insumos no funciona a nivel nacional; funciona por barrio o ciudad. Necesitas restaurantes y proveedores en la misma zona, con los mismos horarios, rutas de entrega y categorías de producto. Conseguir liquidez en dos lados simultáneamente en un solo código postal es mucho más difícil que conseguir usuarios para una app de consumo.

**4. Te conviertes en el responsable de todo lo que sale mal**
Si el pollo llega en mal estado, la lechuga está podrida o la entrega se retrasa y el restaurante tiene que cerrar el servicio, ¿a quién culpan? A ti. No eres solo un software; eres el intermediario de productos perecibles. El control de calidad, la logística de cadena de frío y los reclamos te comerán vivo operativamente.

**5. Pagos y regulación financiera en un sector informal**
Manejar el flujo de dinero entre comprador y vendedor te expone a contracargos, regulación de servicios de pago, lavado de activos y cumplimiento fiscal. En LATAM, convertirte en un "procesador de pagos" no intencionado es un dolor legal y operativo enorme.

---

### 2. Por qué podría NO funcionar en LATAM específicamente

- **Informalidad endémica:** Muchos proveedores locales no emiten factura, no tienen cuenta bancaria empresarial y operan en efectivo. Si no pueden facturar digitalmente, tu plataforma no les sirve. Y si tú intentas formalizarlos, te conviertes en un recolector de datos para la autoridad tributaria, lo que espanta a ambos lados.

- **La relación gana al precio:** En LATAM, el dueño del restaurante compra al proveedor de "toda la vida" porque le da crédito, le acepta devoluciones, le avisa si falta un producto y le hace favores. Tu plataforma ofrece eficiencia, pero el restaurante valora confianza y flexibilidad más que ahorrar dos horas en llamadas.

- **Logística fragmentada:** No existe una red de entrega confiable y barata para productos perecibles a pequeña escala. Si el proveedor tiene que hacer el delivery él mismo, tu plataforma no resuelve el problema físico. Si lo hace un tercero, el costo de envío destruye el margen.

- **Precios volátiles:** Los precios de los insumos en LATAM cambian semanalmente (o diariamente) por inflación, tipo de cambio y estacionalidad. Mantener un catálogo con precios actualizados es un infierno operativo. Si los precios en la app no coinciden con la realidad, la plataforma pierde credibilidad en una semana.

- **Pagos en efectivo:** La gran mayoría de transacciones entre restaurantes y proveedores en LATAM se pagan en efectivo o transferencia directa, con plazos de 30 días. Forzar un pago digital con retención de comisión es una fricción que nadie quiere asumir.

---

### 3. Qué tendría que ser verdad para que funcione (key assumptions)

Para que esto no sea una quema de dinero, necesitas que **todo** lo siguiente sea cierto:

- Los restaurantes pequeños están dispuestos a asumir un costo del 15% sobre sus compras de insumos sin que eso destruya su margen.
- Los proveedores locales tienen inventario digitalizado, capacidad de respuesta en tiempo real y flota de entrega propia o confiable.
- Existe una densidad suficiente de oferta y demanda en una zona geográfica reducida para generar transacciones repetidas sin subsidios.
- Los usuarios no buscan al proveedor fuera de la plataforma después del primer contacto.
- Los restaurantes confían en un tercero para la calidad y seguridad alimentaria de lo que sirven a sus clientes.
- Puedes operar legalmente como intermediario de pagos sin convertirte en una entidad financiera regulada.

Si una sola de estas es falsa, el modelo colapsa.

---

### 4. El escenario donde fracasas rápido y por qué

Lanzas la app en una ciudad. Consigues 15 restaurantes y 8 proveedores mediante llamadas frías y eventos. Los restaurantes hacen sus primeros pedidos. Un par de entregas llegan tarde o con productos en mal estado. Los restaurantes empiezan a escribir directamente por WhatsApp a los proveedores para pedirles precios "fuera de la plataforma" y evitar tu comisión. Los proveedores, que tampoco quieren pagar tu 15%, aceptan.

En 60 días tienes cero transacciones activas, una app vacía y una reputación quemada con ambos lados. O peor: nunca logras cruzar los dos lados en la misma zona y terminas con una herramienta que nadie usa porque no hay suficiente oferta para los restaurantes ni suficiente demanda para los proveedores.

**Por qué:** Subestimaste que este es un negocio de relaciones y confianza, no de software. El 15% es una barrera, no un incentivo.

---

### 5. Si solo tuvieras $10K para validar, ¿qué harías?

**No construyas una app.** Eso es tirar el dinero.

Con $10K haces un "concierge de mercado" manual:

1. **Elige una sola ciudad y una sola categoría** (ej. solo carnes o solo vegetales en una zona específica).
2. **Consigue 5 restaurantes y 3 proveedores** mediante llamadas y visitas personales. No pagues publicidad.
3. **Usa herramientas gratuitas o casi gratuitas:** WhatsApp Business, Google Forms, Airtable o Excel, y una cuenta de pagos (Stripe, PayPal o transferencia bancaria).
4. **Tú eres la plataforma:** El restaurante te manda el pedido por WhatsApp. Tú llamas al proveedor, confirmas precio y disponibilidad, coordinas la entrega y cobras al restaurante. Luego le pagas al proveedor y te quedas con tu comisión (si es que alguien acepta pagarla).
5. **Mide solo dos cosas:**
   - ¿Cuántos pedidos se repiten en 8 semanas?
   - ¿Cuántos restaurantes o proveedores intentan saltarse la plataforma para evitar tu comisión?

Si al final de las 8 semanas no tienes repetición y disposición real a pagar el 15%, **mata la idea**. No construyas nada. Si sí hay tracción, entonces piensa en tecnología.

Pero lo más probable es que descubras que el problema no es "falta de una app", sino que nadie quiere pagar el 15% por algo que resuelve con una llamada y una relación de años.