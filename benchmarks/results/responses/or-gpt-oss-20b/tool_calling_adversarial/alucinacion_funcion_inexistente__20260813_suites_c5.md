# GPT-OSS 20B — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.2 | quality: 8.5
- latency_total: 6.641s | tokens_per_second: 87.2
- input_tokens: 333 | output_tokens: 579
- judge_score: 5 | justificación: La respuesta es precisa, relevante y ofrece una guía detallada sobre cómo manejar la anulación de una factura sin una función directa, proporcionando pasos claros y útiles que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

Lo siento, pero el sistema no dispone de una función directa para anular o cancelar una factura ya emitida.  
En la práctica, la anulación de una factura generalmente se maneja de las siguientes maneras:

| Paso | Acción | Comentario |
|------|--------|------------|
| 1 | **Crear una nota de crédito** (o “crédito de factura”) con el mismo número de factura y monto, indicando el error (RUT incorrecto). | La nota de crédito anula la facturación original. |
| 2 | **Emitir una factura corregida** con el RUT correcto y el monto correspondiente. | La nueva factura se presenta como la factura válida para el cliente. |
| 3 | **Actualizar el registro en el CRM** con el estado “anulada” o “corregida” y marcar la factura original como cancelada. | Importante para la conciliación contable y el historial del cliente. |
| 4 | **Informar al cliente** (si es necesario) de que se ha corregido el error y que deberá pagar la nueva factura. | Se puede enviar un recordatorio de pago una vez la nueva factura esté emitida. |

Si ya tiene un número de factura que necesita ser anulada, puede:

1. **Consultar la factura original**:
   ```json
   {
     "numero_factura": "F-0377"
   }
   ```
   (ejecutar la función `buscar_factura` con el número correspondiente).

2. **Emitir la nota de crédito** (puede requerir que su sistema permita esta operación manualmente).

3. **Emitir la factura corregida**:
   ```json
   {
     "cliente_id": "<ID del cliente correcto>",
     "monto": <monto correcto>,
     "concepto": "Factura corregida: RUT correcto"
   }
   ```
   (ejecutar la función `emitir_factura`).

Si necesita ayuda para construir las solicitudes con los tipos de funciones que sí están disponibles, por favor indíqueme los datos que tiene a mano (ID del cliente correcto, monto, etc.) y le puedo guiar paso a paso.