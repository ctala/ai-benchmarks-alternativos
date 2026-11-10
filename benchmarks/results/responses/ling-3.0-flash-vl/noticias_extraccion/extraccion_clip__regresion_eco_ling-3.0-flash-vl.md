# Ling 3.0 Flash VL — noticias_extraccion/extraccion_clip

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 8.89 | quality: 9.05
- latency_total: 3.445s | tokens_per_second: 338.1
- input_tokens: 1189 | output_tokens: 1165

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el extractor de afirmaciones de una redacción que publica noticias de startups, inversión y tecnología en español. Recibes una FUENTE (en español o en inglés). Tu trabajo es sacar TODAS las afirmaciones verificables que la fuente hace sobre la noticia, para que un verificador las contraste una por una antes de publicar.

Responde SOLO con JSON válido:
{"claims": [{"texto": "<una afirmación, en español, autocontenida>", "nucleo": true}]}

QUÉ ES UNA AFIRMACIÓN VERIFICABLE (sí se extrae):
- cifras, montos, porcentajes, valoraciones, cantidades;
- fechas de HECHOS relatados (cuándo se cerró, cotizó o aprobó algo);
- entidades y quién hizo qué: quién lideró, quién participó, quién compró, quién aprobó;
- atribuciones: si la fuente dice «según la empresa» o «según Reuters», la afirmación conserva la atribución («Según la empresa, …»).

QUÉ NO SE EXTRAE:
- conocimiento de dominio (cómo funciona una Serie B, qué es un marketplace), opiniones y adjetivos sin dato;
- la fecha de publicación de la propia nota;
- nada que la fuente no diga: no conviertas monedas, no sumes, no restes, no calcules.

nucleo=true → el hecho de la noticia misma: qué pasó, quién, cuánto, cuándo, con quién.
nucleo=false → contexto: rondas anteriores, historia de la empresa, tamaño de mercado, comparaciones, planes y declaraciones accesorias.

Cada afirmación debe nombrar a la entidad de la que habla (nada de «la empresa» sin nombre). Una afirmación por dato. Lee la fuente COMPLETA, hasta el último párrafo: los datos del final cuentan igual que los del principio.

**user:**

FUENTE:
Clip recibe US$250 millones de SoftBank y Viking y se convierte en unicornio

Ciudad de México — Clip, la fintech mexicana que vende lectores de tarjetas y servicios de cobro a pequeños comercios, recibió en junio de 2021 una inversión de US$250 millones del SoftBank Latin America Fund y de Viking Global Investors. La operación valora a la empresa en cerca de US$2.000 millones, según la propia compañía.

Clip se convierte así en el primer unicornio de pagos de México.

Para un comercio pequeño, aceptar tarjetas era hasta hace pocos años un trámite largo: había que abrir una cuenta con un banco, firmar un contrato de adquirencia y rentar una terminal con costo fijo mensual. Las empresas como Clip simplificaron ese proceso con un lector barato que se conecta al teléfono y una comisión por venta, sin plazo forzoso. El modelo se apoya en el volumen, porque el margen por cada transacción es pequeño.

El fundador y director ejecutivo de la compañía, Adolfo Babatz, dijo que el dinero permitirá seguir creciendo de forma agresiva. Según Bloomberg, la empresa planea contratar a 320 personas en los próximos 18 meses.

Antes de esta ronda, Clip había recibido cerca de US$100 millones de inversionistas como General Atlantic, su mayor accionista. General Atlantic y SoftBank habían invertido en 2019, en una operación que, según reportes de la época, valoró a la empresa en US$400 millones.

El mercado sigue siendo amplio. Babatz estimó que de los casi 11 millones de negocios que hay en México, solo alrededor de 1 millón acepta pagos con tarjeta.

La competencia, sin embargo, también creció. Bancos, billeteras digitales y las terminales de grandes plataformas de comercio electrónico buscan a los mismos comerciantes, y la guerra de comisiones presiona los márgenes de todo el sector.

Para el pequeño comerciante, aceptar tarjetas tiene beneficios que van más allá de la venta inmediata. Los pagos digitales dejan un registro que puede servir para pedir un crédito, reducen el riesgo de manejar efectivo y permiten vender a clientes que ya no cargan billetes. Las empresas del sector aprovechan ese historial para ofrecer préstamos a sus comerciantes, un negocio con mejores márgenes que el cobro por transacción y que se ha vuelto central en la estrategia de casi todas las plataformas de adquirencia de la región.

Babatz dijo además que la empresa evalúa una oferta pública inicial para captar más capital y dar liquidez a sus inversionistas, aunque aclaró que no ocurriría durante 2021.



## Respuesta completa

```json
{"claims": [{"texto": "Clip recibió en junio de 2021 una inversión de US$250 millones del SoftBank Latin America Fund y de Viking Global Investors.", "nucleo": true}, {"texto": "Según la propia compañía, la operación valora a Clip en cerca de US$2.000 millones.", "nucleo": true}, {"texto": "Clip se convierte en el primer unicornio de pagos de México.", "nucleo": true}, {"texto": "Adolfo Babatz, fundador y director ejecutivo de Clip, dijo que el dinero permitirá seguir creciendo de forma agresiva.", "nucleo": true}, {"texto": "Según Bloomberg, Clip planea contratar a 320 personas en los próximos 18 meses.", "nucleo": true}, {"texto": "Antes de esta ronda, Clip había recibido cerca de US$100 millones de inversionistas como General Atlantic, su mayor accionista.", "nucleo": true}, {"texto": "General Atlantic y SoftBank habían invertido en Clip en 2019, en una operación que, según reportes de la época, valoró a la empresa en US$400 millones.", "nucleo": true}, {"texto": "Según Babatz, de los casi 11 millones de negocios que hay en México, solo alrededor de 1 millón acepta pagos con tarjeta.", "nucleo": true}, {"texto": "Babatz dijo que Clip evalúa una oferta pública inicial para captar más capital y dar liquidez a sus inversionistas, aunque aclaró que no ocurriría durante 2021.", "nucleo": true}]}
```