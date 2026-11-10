# Tencent Hy4 — noticias_verificacion/bloquea_clip_quien_invierte

- model_id: `tencent/hy4`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 61.627s | tokens_per_second: 97.2
- input_tokens: 1198 | output_tokens: 5993

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el verificador de datos de una redacción. Recibes una FUENTE (en español o en inglés) y una lista numerada de AFIRMACIONES que alguien quiere publicar citándola. Decide, para CADA afirmación, si la fuente la respalda.

Responde SOLO con JSON válido, con un veredicto por cada afirmación y el mismo id:
{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}]}

RESPALDADO: la fuente afirma lo mismo, aunque con otras palabras, en otro idioma o con la cifra escrita en otro formato («US$1.500 millones» = «$1.5 billion»).
NO_RESPALDADO: la fuente no dice nada sobre eso, o lo que dice no alcanza para afirmarlo. La AUSENCIA nunca es contradicción.
CONTRADICE: la fuente afirma algo incompatible: otra cifra, otra fecha, otra entidad haciendo la acción (quién lideró, quién paga, quién confirma), o lo opuesto.

Reglas:
- Usa SOLO la fuente. No uses lo que sabes del mundo, aunque estés seguro.
- Si la fuente está truncada (muro de pago, «Suscríbete para seguir leyendo»), lo que no aparece en el fragmento es NO_RESPALDADO, nunca CONTRADICE.
- La atribución es parte del dato: «según Reuters» no es «la empresa confirmó».
- Lee la fuente completa, hasta el último párrafo, antes de decidir.
- Devuelve exactamente un veredicto por afirmación: ni menos, ni repetidos.

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

AFIRMACIONES A VERIFICAR (6):
1. Clip recibió US$250 millones de SoftBank y Viking Global.
2. General Atlantic lideró la inversión de US$250 millones en Clip.
3. Clip es el primer unicornio de pagos de México.
4. Clip procesa más de US$5.000 millones al año en pagos.
5. Según Bloomberg, Clip contratará a 320 personas en los próximos 18 meses.
6. Babatz dijo que Clip saldría a bolsa durante 2021.


## Respuesta completa

{"veredictos":[{"id":1,"veredicto":"RESPALDADO"},{"id":2,"veredicto":"CONTRADICE"},{"id":3,"veredicto":"RESPALDADO"},{"id":4,"veredicto":"NO_RESPALDADO"},{"id":5,"veredicto":"RESPALDADO"},{"id":6,"veredicto":"CONTRADICE"}]}