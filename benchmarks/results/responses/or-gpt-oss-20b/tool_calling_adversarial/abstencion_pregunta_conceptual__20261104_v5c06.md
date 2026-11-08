# GPT-OSS 20B — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.26 | quality: 8.5
- latency_total: 12.61s | tokens_per_second: 124.7
- input_tokens: 326 | output_tokens: 1573
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y estructurado que un emprendedor puede aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

### Facturar por adelantado vs. Contra entrega: ¿qué opción elegir con un cliente nuevo?

La decisión depende de varios factores que se deben ponderar antes de cerrar la operación. A continuación te dejo un esquema práctico para que tomes la decisión más adecuada para tu negocio y tu relación con el cliente.

| Factor | Facturar por adelantado | Facturar contra entrega |
|--------|------------------------|------------------------|
| **Liquidez inmediata** | Enhorabuena: el efectivo ya llega antes de que le entregues el producto o servicio. | Solo recibes el dinero cuando la entrega se ha completado, lo que puede retrasar tu flujo de caja. |
| **Riesgo financiero** | Reduces el riesgo de incobrable, pero: si el cliente se rehúsa a pagar después de entregarte, tienes un recupero complicado. | Riesgo mayor porque podrías entregar y no recibir pago. |
| **Relación con el cliente** | Demuestra grande confianza o, si es la primera vez, **una exigencia de tu parte**. Puede que el cliente se sienta presionado. | Muestra confianza en el cliente, pero también implica que el cliente debe cumplir con la timidez al momento de la entrega. |
| **Tipo de producto/servicio** | Muy aplicable a entregas de alto valor, proyectos complejos, o cuando el tiempo de producción es largo (software, construcción, diseños). | Adecuado para productos de bajo costo, servicios rápidos, donde la entrega es simultánea a una demostración. |
| **Condiciones del mercado / normativas fiscales** | Algunas industrias o jurisdicciones exigen una factura por adelantado como requisito de CTA/IX (Sales tax, VAT, etc.). | En otros casos el impuesto se cobra sobre la entrega (por ejemplo, IVA sobre venta en tiempo de entrega). |
| **Capacidad de configurar un crédito** | Si dispones de sistemas CT/Credit-Score, puedes hacer un “avanzado crédito” (situación que podrías definir a través de `buscar_cliente(query)` para saber su activo de crédito). | Si no cuentas con un scoring interno, se vuelve más fácil registrar en tu contabilidad la deuda. |
| **Práctica de la industria** | En industrias portafolios de 1‑2 años (consultoría, marketing, desarrollo de software) es común el “pre‑invoice” a 30‑60 días. | En minoristas de bienes de consumo, siempre se factura en manejo de caja (contrareembolso). |
| **Tamaño de la empresa** | Pequeñas startups suelen optar por facturación anticipada por falta de liquidez propia. | Grandes corporaciones suelen usar contra entrega porque gestiones de cobro están internas. |

---

## Pasos recomendados cuando no conoces al cliente

1. **Investiga el cliente**  
   - Usa tu CRM: `buscar_cliente(query="correo@cliente.com")` o el nombre de la empresa para ver si ya está registrado y cuál es su historial de pagos.  
   - Si no aparece, es un cliente completamente nuevo.  
   
2. **Revisa tu política interna de crédito**  
   - Lo que la política dicta (pago net 30, 60, depósito 50%) puede ayudarte a decidir el modelo de facturación.  

3. **Definir un depósito**  
   - Si el riesgo es alto, solicítale un 20‑50 % de adelanto (o un depósito) antes de iniciar la producción o la entrega.  
   - Este depósito se contabiliza con `emitir_factura` como una “nota de crédito o valor descontado” si tu sistema lo permite.  

4. **Contrato y términos claros**  
   - Establece claramente cuándo se enviará la factura final y la fecha de vencimiento.  
   - Si optas por contra entrega, aclara el puerto de aceptación (escaneo de firma, recepción de producto, etc.).  

5. **Monitorea el flujo de entrega**  
   - Utiliza tu sistema de inventario y logística: si facturas contra entrega, tu ERP debe marcar la factura como “pendiente de cobro” hasta que la entrega confirme el pago.  

6. **Evalúa la liquidez real**  
   - Si tu negocio necesita rapidez en el flujo de caja, facturar por adelantado te da un “hummingbird” económico.  
   - Si ya tienes suficiente efectivo y tu objetivo es ganar confianza con el cliente, la contra entrega puede ser una herramienta de desarrollo de relación.  

---

## Resumen de recomendaciones

| Tipo de cliente | Recomendación típica |
|-----------------|----------------------|
| **Negocio nuevo + alto riesgo** | Solicita *adelanto* o *depósito*. |
| **Negocio nuevo + bajo riesgo** (ej. proveniente de recomendaciones) | Puedes optar por la *contrareembolso* o un pago neto a 30‑60 días. |
| **Proyecto de alto valor (software, construcción, etc.)** | Factura *por adelantado* y adelanta pagos parciales. |
| **Venta de bienes de consumo** | Generalmente *contra entrega* (en tienda, livification). |
| **Servicios recurrentes y contratos a largo plazo** | Define plazos netos; la entrega y facturación suelen alinearse a la obra. |

---

### Conclusión

Si desconoces al cliente y tu prioridad es proteger tu liquidez, lo más seguro es facturar por adelantado (o pedir un depósito). Si tu valor añadido es la **confianza y el compromiso**, y tu empresa cuenta con un buen control interno, puedes dar una “carta de confianza” y facturar contra entrega.

Recuerda que la elección también sobre cómo gestionarás el riesgo de impago: auditorías de crédito, límites de crédito, y garantías cambiantes son herramientas esenciales para mitigar el riesgo sin depender únicamente de la forma de facturación.

¡Espero que esta guía te ayude a tomar la decisión correcta!