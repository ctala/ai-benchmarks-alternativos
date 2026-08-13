# Claude Opus 5 — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.12 | quality: 8.5
- latency_total: 21.825s | tokens_per_second: 58.5
- input_tokens: 918 | output_tokens: 1277
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y práctico sobre estrategias de facturación para clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

No necesitas que consulte nada en el sistema para esto — es una decisión de política comercial. Te doy el criterio práctico:

## La regla general

**Con cliente nuevo y desconocido, nunca asumas todo el riesgo tú.** El reparto habitual es:

| Situación | Esquema recomendado |
|---|---|
| Trabajo pequeño (hasta ~1 semana) | 100% por adelantado |
| Proyecto mediano | 50% al inicio / 50% a entrega |
| Proyecto grande o largo | 30% inicio / 40% hito intermedio / 30% entrega |
| Servicio recurrente (mensual) | Adelantado, mes a mes |
| Producto físico | Adelantado o contra entrega con pago inmediato |

## Por qué el adelanto (parcial) es casi siempre mejor

1. **Filtra clientes problemáticos.** Quien se resiste a pagar un anticipo razonable suele ser el mismo que se resistirá a pagar el total.
2. **Compromiso mutuo.** Un cliente que ya puso dinero cancela menos, responde antes y cambia menos de opinión.
3. **Financias tu propio trabajo.** Si tú compras materiales o dedicas horas, no deberías prestarle capital gratis a un desconocido.
4. **Recuperar impagos cuesta muchísimo.** El tiempo y el desgaste de perseguir una factura casi nunca compensan el margen del trabajo.

## Cuándo sí tiene sentido facturar contra entrega

- **Cliente corporativo grande o administración pública.** Tienen procesos de compra rígidos y no pagan adelantos; el riesgo real de impago es bajo, pero prepárate para plazos de 30-90 días.
- **Cuando el adelanto te haría perder un contrato muy valioso** y puedes verificar solvencia por otras vías.
- **Cuando el entregable es fácilmente recuperable o inutilizable sin pago** (ej. entregas el diseño con marca de agua, o el acceso solo se activa tras el pago).

## Cómo bajar el riesgo sin pedir adelanto

- Empieza con un **encargo pequeño de prueba** antes del proyecto grande.
- **Verifica al cliente**: registro mercantil, antigüedad, referencias de otros proveedores.
- **Presupuesto firmado por escrito** con condiciones de pago, plazo e intereses de demora explícitos.
- **Entrega por fases**, cada una facturada y cobrada antes de arrancar la siguiente.
- **Retén la entrega final** (archivos fuente, código, credenciales, propiedad intelectual) hasta el cobro completo.
- Plazos cortos: **pago a 7 o 15 días**, no a 30.

## Mi recomendación por defecto

Para un cliente nuevo del que no sabes nada: **50% por adelantado y 50% contra entrega, con pago a 7 días y condiciones firmadas**. Es un estándar que casi nadie considera abusivo, y si alguien lo rechaza de plano, normalmente te está dando información valiosa sobre sí mismo.

Si quieres, dime qué tipo de trabajo haces y el importe típico y te concreto el esquema. Y si ya tienes un cliente en mente, puedo buscar su ficha en el CRM para ver si tiene historial o estado de cuenta.