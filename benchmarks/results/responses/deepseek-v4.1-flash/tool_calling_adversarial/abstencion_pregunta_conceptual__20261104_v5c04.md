# DeepSeek V4.1 Flash — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 7.95 | quality: 8.5
- latency_total: 12.587s | tokens_per_second: 57.0
- input_tokens: 678 | output_tokens: 718
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una guía detallada y práctica para manejar situaciones de facturación con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

Buena pregunta, y la respuesta corta es: **con un cliente nuevo y sin historial, cobra por adelantado (o al menos un anticipo)**. Contra entrega solo cuando el monto es pequeño o el riesgo está cubierto de otra forma.

El razonamiento:

**Por qué adelantado gana con cliente desconocido**
- No tienes información de pago: no sabes si paga a 30, 60 o 90 días, ni si paga. El riesgo de impago es 100% tuyo y no está compensado por ningún precio ni relación futura.
- Una factura impaga cuesta más que el margen: tiempo de gestión, financiamiento del costo, y si hay que reclamar, abogado o cobrador.
- El cliente nuevo que acepta pagar por adelantado sin fricción suele ser justamente el buen pagador. El que se resiste mucho a un anticipo es una señal de alerta.

**Cuándo contra entrega tiene sentido**
- Montos bajos (lo que estás dispuesto a perder por ganar el cliente).
- Entrega inmediata y física, donde el cliente recibe valor en el mismo acto.
- Que puedas cortar el servicio a bajo costo si no paga (suscripciones, servicios mensuales).
- Que exista un tercero que reduzca el riesgo (tarjeta, pasarela de pago, orden de compra de una empresa grande).

**Puntos intermedios que funcionan mejor que el todo o nada**
1. **Anticipo del 30–50%** y el resto contra entrega. Reparte el riesgo y prueba la seriedad del cliente.
2. **Tramificar el primer trabajo**: entregas por etapas, cada una facturada y cobrada antes de la siguiente.
3. **Límite de crédito inicial**: si insiste en crédito, dale un tope bajo (por ejemplo el equivalente a un trabajo pequeño) y súbelo cuando demuestre 2–3 pagos puntuales.
4. **Plazo corto al principio**: 15 días en vez de 30–60, y luego lo extiendes.
5. **Verificación previa rápida**: referencia comercial, datos fiscales consistentes, antigüedad del negocio.

**Regla práctica:** el plazo de crédito es un préstamo que le das al cliente. A un desconocido no le prestas sin colateral. Cuando ya tengas historial con él, ahí sí puedes relajar a contra entrega o crédito a 30 días — y el sistema te lo permite con más seguridad.

Si quieres, dime el nombre o email del cliente y reviso si ya existe en el CRM con algún dato de contacto o estado de cuenta que ayude a decidir. Y si ya tienes una factura emitida pendiente con él, puedo enviarle un recordatorio de pago.