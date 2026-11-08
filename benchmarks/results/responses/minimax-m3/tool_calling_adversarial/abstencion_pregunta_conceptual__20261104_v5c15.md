# MiniMax M3 — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.71 | quality: 8.5
- latency_total: 20.901s | tokens_per_second: 63.2
- input_tokens: 806 | output_tokens: 1321
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando una guía detallada y práctica sobre cómo manejar la facturación con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

## Recomendación corta**Contra entrega, o mejor: un punto medio.** Para un cliente nuevo al que no conozco, el riesgo real no es solo de cobranza, sino de entrega: si cobro todo por adelantado y el cliente reporta un problema o devuelve el servicio, me quedo con el dinero y sin poder defender la calidad. Si cobro contra entrega, el pago se vuelve el último paso, es decir, la confirmación de que todo salió bien.

## Cómo lo decidiría en la práctica

**Cobro por adelantado (anticipo total)** — tiene sentido cuando:
- El cliente es una empresa grande o institucional y su proceso de compras lo exige (ahí el anticipo no es un problema, es el estándar).
- El importe es bajo y el margen de producción es pequeño: anticipo del50–100 % antes de empezar.
- Estoy vendiendo servicios/acabados que no se pueden reutilizar (por ejemplo, un encargo a medida o una instalación con viaje).

**Contra entrega** — tiene sentido cuando:
- Es la primera relación y no tengo referencias ni historial de pagos.
- Quiero que el cliente pruebe el servicio sin fricción para construir confianza.
- Entrego algo intangible o estándar (mantenimiento, licencia, curso).

**El punto medio que más uso:** 50 % de anticipo para reservar el trabajo + 50 % contra entrega. Así cubro costos, tengo un cliente comprometido y no asumo el riesgo completo.

## Criterios objetivos antes de aceptar terms

- **Importe vs. tamaño del cliente:** si la factura es desproporcionada respecto a lo que veo de su negocio, el riesgo sube.
- **Datos fiscales completos y coherentes:** si no me pasa razón social, NIF/CIF, dirección y contacto real, no avanzo.
- **References o señales externas:** sector en el que trabaja, antigüedad de la empresa, si tiene web y actividad real.
- **Forma de pago:** para cliente nuevo, transferencia o tarjeta verificada; desconfío del chequeo sin fondos clear y del "te pago todo junto la próxima vez".
- **Politiza de crédito:** un cliente nuevo no debería obtener condiciones de crédito (net 15/30) solo por insistencia; eso es un descuento disfrazado y termina en mora.

## Red flags que cambian la decisión

- Rechaza el anticipo pero exige 30 días de plazo.
- Insiste en pagar "cuando lo pruebe" sin dar una fecha concreta.
- No quiere dar sus datos fiscales hasta que ya se entregó.
- Pide modificar el importe de la factura después de emitida.

## Lo que puedo hacer por ti con las herramientas

- **Buscar al cliente en el CRM** (por nombre o email) y ver si realmente es nuevo o si ya existe historial — a veces "cliente nuevo" en tu cabeza es un cliente con antecedentes.
- **Verificar si ya hay una factura emitida** para ese cliente, para no duplicar cobros ni numeración.
- **Emitir la factura** con el concepto y el importe acordados.
- **Enviar recordatorios de pago** en tono amable primero y firme después, si se emite contra entrega y no paga en la fecha pactada.

Si me das el nombre o email del cliente concreto, lo busco y te digo qué recommendaría para *ese* caso en particular, en lugar de un consejo genérico.