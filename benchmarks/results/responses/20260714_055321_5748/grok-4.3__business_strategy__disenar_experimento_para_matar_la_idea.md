# Grok 4.3 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.25 | quality: 8.0
- latency_total: 12.458s | tokens_per_second: 85.4
- input_tokens: 351 | output_tokens: 1064
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan detallado y práctico para probar la hipótesis de manera económica y rápida.

## Respuesta completa

**Experimento más barato y rápido para matar la hipótesis:**

### Experimento: "Pre-venta manual con outreach frío" (Concierge pre-sell)

**Qué vas a hacer:**

1. Identificas **30 agencias pequeñas de marketing** (idealmente 5-15 empleados, que gestionen entre 5-20 clientes).
2. Les envías un mensaje **directo y concreto** ofreciéndoles exactamente lo que dices que van a pagar:
   - "Tengo un sistema que les genera reportes automáticos para sus clientes. ¿Les interesa que les arme los reportes de este mes por $200 USD para probar?"
3. Si responden que sí, les cobras **por adelantado** (transferencia o Stripe) y les entregas los reportes **manualmente** (usando lo que sea: Looker Studio, Google Sheets + scripts, Copy-paste de plataformas, etc.).
4. Repites hasta haber contactado a 30 agencias.

### Detalles de ejecución

| Aspecto              | Detalle                                      | Costo     | Tiempo estimado |
|----------------------|----------------------------------------------|-----------|-----------------|
| Encontrar agencias   | LinkedIn + Google                            | $0        | 3-4 horas       |
| Outreach             | 30 mensajes personalizados (LinkedIn o email)| $0        | 6-8 horas       |
| Seguimiento          | 2-3 mensajes de follow-up                    | $0        | 4-5 horas       |
| **Total**            | -                                            | **$0**    | **2-3 días**    |

### Criterio claro para matar la hipótesis

**Abandonas la idea si:**

- Contactas **30 agencias** y consigues **0 agencias** que te paguen los $200 por adelantado.

O, más estricto aún (recomendado):

- Consigues **menos de 2 agencias** que paguen por adelantado después de contactar a 30.

### Por qué este experimento es el que más rápido te puede matar la idea

- No estás midiendo "interés" ni "me gusta". Estás midiendo **disposición a pagar $200**.
- Es extremadamente barato (casi gratis).
- Tarda días, no semanas.
- Si nadie paga por adelantado, la hipótesis está muerta independientemente de lo buena que sea la herramienta.

### Notas importantes

- El mensaje tiene que ser **directo** (no "te gustaría una demo"). Tienes que pedirles que paguen.
- Si te dicen que sí pero "después" o "quiero ver primero", **no cuenta**. Solo cuenta el que paga.
- Si logras 2-3 que paguen, ya tienes señal (y hasta podrías seguir cobrándoles manualmente un par de meses mientras decides si construir).

¿Quieres que te arme los mensajes exactos de outreach que maximizan la tasa de respuesta?