# GPT-OSS 120B — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.75 | quality: 8.5
- latency_total: 105.354s | tokens_per_second: 15.9
- input_tokens: 337 | output_tokens: 1672
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

### Facturar por adelantado vs. contra entrega con un cliente nuevo

| **Aspecto** | **Facturar por adelantado (prepago)** | **Facturar contra entrega (post‑pago)** |
|-------------|----------------------------------------|------------------------------------------|
| **Riesgo de impago** | Muy bajo: recibes el dinero antes de entregar el bien/servicio. | Más alto: entregas primero y esperas el pago. |
| **Barreras de venta** | Puede frenar la decisión del cliente, especialmente si no tiene confianza en ti. | Más atractivo para el comprador, facilita cerrar la venta. |
| **Flujo de caja** | Mejora tu liquidez inmediatamente, útil si necesitas cubrir costes de producción o compra de insumos. | El efectivo llega después; podrías necesitar financiar el ciclo de producción/servicio. |
| **Percepción de confianza** | Transmite que confías en el cliente y que tu producto/servicio tiene valor garantizado. | Muestra confianza en el cliente, lo que puede generar buena voluntad y una relación más “humana”. |
| **Gestión administrativa** | Menor riesgo de cobros tardíos → menos tiempo dedicado a seguimiento y recordatorios. | Necesitas un proceso de seguimiento, envío de recordatorios y posible gestión de morosidad. |
| **Costes de financiación** | Si el cliente necesita financiación (ej. tarjeta de crédito), puede haber cargos que él asuma; tú recibes el neto. | Si tú ofreces crédito implícito, estarías financiando al cliente (costo implícito de capital). |
| **Tipo de producto/servicio** | Muy recomendable para bienes de alto valor, productos personalizados, servicios de consultoría con entregables claros, o cuando requieres material o tiempo previo. | Adecuado para bienes de bajo riesgo, entregas rápidas, o cuando el cliente tiene historial de pago puntual (aunque sea nuevo). |

---

## 1. Preguntas que debes contestar antes de decidir

| Pregunta | Por qué importa | Qué respuesta indica prepago vs. post‑pago |
|----------|----------------|-------------------------------------------|
| **¿Cuál es el valor de la operación?** | A mayor importe, mayor riesgo. | > USD 1 000–2 000 → suele inclinarse a prepago. |
| **¿ Cuánto tiempo tardas en entregar?** | Un proceso largo implica mayor exposición. | > 1 semana → prepago o al menos un anticipo. |
| **¿Tienes costos fijos o materiales que comprarás antes?** | Necesitas financiar esos gastos. | Sí → anticipo o prepago. |
| **¿Cómo es la reputación del mercado y del cliente?** | Si el cliente proviene de una referencia confiable, el riesgo disminuye. | Referencia fuerte → post‑pago posible. |
| **¿Cuál es la política de tu empresa?** | Algunas compañías ya tienen normas (ej. 30 % de anticipo). | Política existente → seguirla. |
| **¿Qué tan competitivo es el sector?** | En mercados muy competitivos, ofrecer pago contra entrega puede ser diferenciador. | Alta competencia → considerar post‑pago. |

---

## 2. Estrategias intermedias (lo mejor de ambos mundos)

1. **Anticipo parcial + Pago restante contra entrega**  
   - Ejemplo: 30 % al ordenar, 70 % al recibir.  
   - Reduce tu exposición y sigue manteniendo atractivo para el cliente.

2. **Facturación por hitos** (muy útil en proyectos de consultoría o desarrollo).  
   - Cada fase entregada genera una factura; el cliente paga antes de la siguiente fase.

3. **Uso de plataformas de pago con retención** (ej. escrow).  
   - El dinero queda bloqueado y se libera al cumplir los criterios de entrega.  
   - Genera confianza mutua, aunque añade una comisión.

4. **Condiciones de pago netas 15/30 días con descuento por pronto pago**  
   - Ofreces 2 % de descuento si paga en 10 días; de lo contrario, plazo neto 30 días.  
   - Incentiva el pago rápido sin obligar al cliente a pagar antes.

---

## 3. Buenas prácticas para clientes nuevos

| Acción | Por qué es importante |
|--------|-----------------------|
| **Solicita referencias** | Incluso un breve contacto con un proveedor anterior reduce incertidumbre. |
| **Realiza una pequeña verificación de crédito** (bases de datos públicas, LinkedIn, etc.) | No implica costo y te da una pista del historial financiero. |
| **Emite una **orden de compra** (OP) o contrato sencillo** | Formaliza el acuerdo y deja constancia de los términos. |
| **Define claramente los entregables y los plazos** | Evita disputas que retrasen el pago. |
| **Incluye cláusulas de penalidad por retraso** | Señala un interés (ej. 1,5 % mensual) que el cliente verá como incentivo para pagar a tiempo. |
| **Utiliza facturas electrónicas con códigos QR o links de pago inmediato** | Facilita el proceso de pago y reduce la fricción. |
| **Mantén una comunicación proactiva** (confirmación de recepción del pedido, aviso de envío, recordatorio de pago) | Refuerza la relación y disminuye la probabilidad de “olvido” del pago. |

---

## 4. Recomendación práctica para un cliente **totalmente nuevo** y sin referencia

1. **Si el valor supera los 1 000 USD** (o su equivalente local) **y/o la entrega requiere trabajo previo (materiales, producción, tiempo de desarrollo)** → **exige al menos un anticipo** (30‑50 %).  
2. **Si el valor es bajo (