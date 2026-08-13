# Claude Sonnet 5 (suscripción) — customer_support/multi_issue_conversation

- model_id: `claude-sonnet-5`
- success: True  | final: 8.13 | quality: 9.8
- latency_total: 39.472s | tokens_per_second: 57.6
- input_tokens: 2 | output_tokens: 2272
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando pasos detallados y organizados para abordar cada problema, con un enfoque en resolver el problema de cobro duplicado de inmediato.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Identifica TODOS los problemas y aborda cada uno.

**user:**

Tengo varios problemas:
1. Mi pedido #ORD-7788 debio llegar hace 3 dias y no ha llegado
2. Me cobraron dos veces por el pedido #ORD-7790 ($45 cada cargo)
3. La app se cierra sola cuando intento ver mis pedidos en el iPhone
4. Quiero saber si tienen envio express para mi proximo pedido

Necesito resolver al menos lo del cobro doble hoy.


## Respuesta completa

Reviso tu caso y son **4 problemas distintos**, no relacionados entre sí. Los ordeno por prioridad, con foco en resolver hoy el cobro duplicado como pediste.

## Aclaración importante
No tengo acceso a tu sistema de pedidos, pagos ni backend de la app — solo puedo guiarte sobre cómo resolver cada punto y qué información necesitas tener a mano para escalarlo con el equipo correspondiente.

---

### 1. Cobro duplicado #ORD-7790 ($45 × 2) — **Prioridad hoy**
Esto es un error de facturación, se resuelve independiente del estado del pedido.
- Ten a mano: número de pedido, los dos IDs de transacción/cargo (aparecen en tu resumen de tarjeta o email de confirmación de pago) y las fechas exactas de cada cargo.
- Contacta al canal de soporte de pagos (o "Facturación") citando ambos cargos como duplicados — no como disputa genérica, para que no lo enruten a revisión de fraude, que tarda más.
- Pide número de ticket y tiempo estimado de reverso (normalmente 3-10 días hábiles según el medio de pago).

### 2. Pedido #ORD-7788 retrasado (3 días)
- Verifica el tracking con el número de guía en el email de despacho.
- Si no hay movimiento en el tracking en 3+ días, es un caso de "pedido extraviado en tránsito" — repórtalo directo, no esperes más días.
- Al reportarlo, pide que evalúen reenvío o reembolso si el retraso ya superó el SLA prometido.

### 3. App se cierra sola al ver pedidos (iPhone)
- Esto es un bug técnico, no afecta el reclamo de los pedidos 1 y 2 (usa la web o el email si necesitas revisar algo mientras se resuelve).
- Dato útil para reportarlo: modelo de iPhone, versión de iOS y versión de la app (Ajustes → App → Info). Si puedes, intenta reproducirlo y anota si pasa siempre o solo a veces — eso acelera el diagnóstico del equipo técnico.

### 4. Envío express para tu próximo pedido
- Esto depende de tu ubicación y del catálogo — normalmente se confirma en el checkout antes de pagar, seleccionando el pedido y viendo las opciones de envío disponibles.
- Dado que aún tienes un pedido con retraso sin resolver, vale la pena confirmar primero que el problema de #1 no sea sistémico (ej. transportista con incidencias) antes de elegir express para el próximo.

---

**Resumen de acción inmediata:** escala el cobro duplicado (#1) ahora mismo con los datos de ambos cargos — es lo más rápido de resolver y lo que pediste priorizar. En paralelo, reporta el pedido atrasado (#2) porque ya está fuera de plazo.