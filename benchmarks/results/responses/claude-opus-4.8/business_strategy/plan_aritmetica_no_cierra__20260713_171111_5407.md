# Claude Opus 4.8 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 20.251s | tokens_per_second: 45.7
- input_tokens: 318 | output_tokens: 926
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y práctico del plan.

## Respuesta completa

Antes de darle, hagamos la multiplicación que el plan evita hacer.

## Los números reales

- 200.000 visitas × 1,5% = **3.000 suscriptores/mes**
- 3.000 × 2% = **60 compradores/mes**
- 60 × $30 = **$1.800/mes**

El plan promete $6.000. Genera **$1.800**. Falta el 70%.

No llega "cómodo". No llega ni de lejos. El punto 4 ("con eso llegamos cómodos a los $6.000") es una afirmación que nunca fue multiplicada. Es donde murió el plan.

## Un segundo problema, más grave

Dicen **"$6.000/mes recurrentes"** vendiendo un **curso de pago único de $30**.

Un curso no genera ingreso recurrente. Cada mes tenés que conseguir 60 (o 200) compradores *nuevos*. El mes que baja el tráfico o se satura la lista, baja el ingreso. Llamarlo "recurrente" es un error conceptual que infla la sensación de solidez del plan.

Para $6.000 reales con este modelo necesitarías **200 compradores/mes, todos los meses**, sostenidos.

## Qué tendría que ser verdad para llegar a $6.000

Elegí una palanca (o combiná):

| Palanca | De → A | Realismo |
|---|---|---|
| Conversión a suscriptor | 1,5% → 5% | Difícil, el 1,5% ya lo llamaste conservador |
| Conversión a compra | 2% → 6,7% | Muy optimista para lista fría |
| Precio del curso | $30 → $100 | Posible, cambia la propuesta |
| Tráfico | 200k → 667k | 3,3x el tráfico, meses de trabajo |

Ninguna sola es trivial. Y "conservador" es la palabra que más me preocupa: si el 1,5% y el 2% ya son conservadores, no tenés margen para arriba, tenés el techo.

## Veredicto

**No se aprueba como está.** No porque la idea sea mala —el embudo es sensato— sino porque los números del propio plan entregan $1.800, no $6.000, y confunde ingreso único con recurrente.

Preguntas para tu socio antes de reescribirlo:
1. ¿De dónde salió el "$6.000 cómodos"? Mostrame la multiplicación.
2. ¿El curso se puede vender a más de $30, o agregamos algo verdaderamente recurrente (membresía, suscripción)?
3. ¿El 1,5% y 2% de dónde salen — dato propio o intuición?

Traeme eso y volvemos a correr los números.