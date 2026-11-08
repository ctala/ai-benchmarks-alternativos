# Seed 2.0 Code — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 5.84 | quality: 5.7
- latency_total: 6.772s | tokens_per_second: 64.7
- input_tokens: 768 | output_tokens: 438
- judge_score: 3.0 | justificación: La respuesta reconoce correctamente las limitaciones de las funciones disponibles y sigue un enfoque lógico, pero no inventa parámetros inexistentes, manteniendo la precisión. Es relevante y clara, pero carece de profundidad y utilidad práctica debido a la falta de una función para listar facturas por cliente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

El usuario quiere facturas impagas del cliente Andes, ordenadas por monto. Primero, necesito buscar al cliente Andes para obtener su ID o datos, ya que las funciones de facturas necesitan el ID del cliente o número de factura. La función buscar_cliente puede buscar por nombre "Andes". No puedo buscar facturas directamente por nombre de cliente con las funciones disponibles, así que primero busco el cliente para luego poder consultar sus facturas (aunque no hay una función específica para listar facturas por cliente, pero tal vez al obtener el cliente, sus datos incluyan las facturas? Wait, no, las funciones son: buscar_cliente devuelve datos de contacto y estado de cuenta, buscar_factura es por número. Hmm, el usuario quiere facturas impagas de Andes. Entonces primero necesito identificar al cliente correcto usando buscar_cliente con query "Andes", porque tal vez hay varios clientes con ese nombre o necesito su ID. Luego, ¿cómo obtengo sus facturas impagas? Wait, las funciones disponibles no tienen una para listar facturas por cliente. Pero el usuario pide buscarlas. Wait, tal vez la función buscar_cliente devuelve el estado de cuenta, que incluye las facturas impagas? O tal vez necesito primero buscar el cliente, luego usar su ID para... pero no hay una función de listar facturas por cliente. Wait, las funciones dadas son: buscar_cliente (por nombre/email, devuelve contacto y estado de cuenta), buscar_factura (por número), emitir_factura, enviar_recordatorio. Entonces, para obtener las facturas impagas del cliente Andes, primero tengo que buscar al cliente Andes para obtener su información, incluyendo posiblemente su estado de cuenta que mencione facturas impagas. Así que el primer paso es llamar a buscar_cliente con query "Andes".