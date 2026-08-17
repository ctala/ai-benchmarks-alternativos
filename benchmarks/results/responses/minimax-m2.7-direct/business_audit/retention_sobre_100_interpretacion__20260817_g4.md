# MiniMax M2.7 (directo) — business_audit/retention_sobre_100_interpretacion

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.26 | quality: 8.0
- latency_total: 24.412s | tokens_per_second: 45.2
- input_tokens: 128 | output_tokens: 1104

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, y hay que ser claro con esto: **tienes un problema de churn del 10%** (4 clientes perdidos de 40). La retención de ingresos te está ocultando el problema, no resolviéndolo.

## Por qué estás confundido

**Retención de ingresos (114%)** responde: *¿Los clientes que tengo me generan más o menos dinero que antes?*

**Retención de clientes** responde: *¿Cuántos clientes se fueron?*

Son métricas independientes. Puedes tener:
- Retención de ingresos > 100% (ganas más con menos clientes)
- Y retención de clientes < 90% (pierdes clientes rápido)

En tu caso: perdiste 4 clientes pero los 32 restantes gastaron más. El equipo de expansión hizo un buen trabajo, pero eso **no compensa** que se fueron 4.

## Por qué no puedes despreocuparte

Piénsalo con números:

| Escenario | Ingresos | Clientes | Ingreso por cliente |
|-----------|----------|----------|---------------------|
| Mes pasado | $100 | 40 | $2.50 |
| Este mes | $114 | 36 | $3.17 |

Cada cliente que se va ahora vale $3.17/mes que necesitas reemplazar. Si pierdes 4 clientes al mes:

- Mes 1: Necesitas 4 nuevos solo para mantener ingresos
- Mes 2: Otros 4 nuevos
- En 6 meses: 24 clientes nuevos solo para cubrir pérdidas

El crecimiento por upsell puede sostenerte un tiempo, pero **no es infinito**. Eventualmente la expansión de los que quedan se estanca o el mercado se agota.

## Qué hacer

1. **Reduce el churn primero**: 10% mensual es alto (en SaaS saludable suele ser < 5% mensual)
2. **Mantén la captación**: Necesitas seguir captando para compensar
3. **Celebrar la expansión, sí**: 114% de NRR es excelente. Pero no es excusa para ignorar los 4 clientes que se fueron

**En resumen**: No mires una métrica ignorando la otra. La retención de ingresos te dice que *creces bien*, pero la pérdida de clientes te dice que *pierdes base*. Necesitas las dos.