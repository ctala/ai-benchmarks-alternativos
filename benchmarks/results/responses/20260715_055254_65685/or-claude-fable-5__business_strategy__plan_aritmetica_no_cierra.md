# Claude Fable 5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 23.931s | tokens_per_second: 56.7
- input_tokens: 318 | output_tokens: 1358
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y recomendaciones prácticas para un emprendedor.

## Respuesta completa

# No lo apruebes todavía. Los números del plan no llegan a $6.000. Ni cerca.

Hagamos la multiplicación que el plan omitió:

## La cuenta real

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas/mes | — | 200.000 |
| Suscriptores nuevos (1,5%) | 200.000 × 0,015 | 3.000/mes |
| Compradores (2%) | 3.000 × 0,02 | 60/mes |
| Ingreso | 60 × $30 | **$1.800/mes** |

**El plan genera $1.800, no $6.000. Falta un 70%.** Necesitan multiplicar el resultado por 3,33x.

## Dos problemas adicionales que el plan esconde

**1. "Recurrentes" es una palabra mal usada.** Un curso de $30 es una venta única. Si el 2% de compradores sale de los suscriptores *nuevos* de cada mes, tienen $1.800/mes mientras el tráfico se sostenga — pero eso no es ingreso recurrente, es una máquina de ventas únicas que depende del tráfico.

**2. Si la lógica era "la lista se acumula"**, hay que decirlo explícitamente y modelarlo: con 3.000 suscriptores nuevos/mes, al mes 6 tendrían ~18.000 en lista. Pero un 2% de compra *mensual sobre toda la lista* implica que la misma gente compra el mismo curso una y otra vez. No pasa. El 2% razonable aplica a suscriptores nuevos o a lanzamientos puntuales, no como tasa mensual perpetua.

## Cómo cerrar la brecha de 3,33x (elegir 1–2, no todo)

- **Precio:** subir el curso a $99 → 60 × $99 = ~$5.940. Un solo cambio casi cierra el gap. ¿El producto lo aguanta?
- **Oferta recurrente real:** membresía de $15/mes. Con retención decente, 400 miembros activos = $6.000 recurrentes de verdad. Más lento, más sólido.
- **Escalera de valor:** curso de $30 como entrada + upsell de $150-300 al 10-15% de compradores.
- **Mejorar conversiones:** llegar a 3% de captura y 3% de compra da ~$5.400. Posible, pero es apostar a duplicar dos métricas a la vez — frágil.

## Mi recomendación

Devuélvele el plan a tu socio con la cuenta de $1.800 arriba y una pregunta: **"¿cuál de estas palancas movemos para cubrir los $4.200 que faltan?"** Los porcentajes están bien (son conservadores, sí) — el problema es que nadie multiplicó hasta el final. Plan rechazado en su versión actual, rescatable con ajuste de precio u oferta.