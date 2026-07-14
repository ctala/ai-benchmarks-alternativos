# Claude Opus 4.8 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 20.09s | tokens_per_second: 56.3
- input_tokens: 295 | output_tokens: 1132
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, abordando errores clave y ofreciendo estrategias prácticas.

## Respuesta completa

No. Tu aritmética tiene tres errores que, corregidos, cambian la decisión.

## Los tres errores

**1. La vida del cliente no son 24 meses.**

Con churn de 8% mensual, la vida promedio es `1 / 0.08 = 12,5 meses`, no 24. Estás inflando la vida más del doble. Tu "unos 2 años" es una intuición optimista, no lo que dice tu churn.

**2. Ignoraste el margen bruto.**

LTV se calcula sobre margen, no sobre revenue. Cada mes te deja $35 × 0.70 = **$24,50**, no $35. Cobrar $35 y quedarte $24,50 es la diferencia entre un negocio y una obra de caridad para tu procesador de pagos.

**3. Combinando ambos:**

```
LTV = ARPU × margen × vida
LTV = 35 × 0.70 × 12,5 = $306
```

## El número real

| Métrica | Tu cálculo | Real |
|---|---|---|
| Vida | 24 meses | 12,5 meses |
| LTV | $840 | $306 |
| LTV/CAC | 2,9 | **1,05** |

Tu ratio real es **1,05**, no 2,9. Estás casi empatado: por cada $290 que gastas, recuperas ~$306 en margen a lo largo de más de un año.

## Por qué eso mata el plan

- **Payback:** recuperar $290 a $24,50/mes de margen toma **~12 meses**. Pero la vida promedio es 12,5 meses. Recuperas el CAC justo cuando el cliente se va. No hay ganancia, hay reciclaje de capital.
- **Los $10.000** te compran ~34 clientes. Vas a adelantar $10.000 hoy para recuperarlos, sin margen real, a lo largo de un año. Eso no es escalar; es prestarte plata a ti mismo con riesgo de churn.

## Qué haría antes de meter un peso

1. **Verifica el churn de 8%.** Un ratio de 1,05 es tan frágil que si el churn real es 10%, pierdes plata en cada cliente.
2. **Ataca el churn primero.** Bajar de 8% a 5% sube la vida a 20 meses y el LTV a $490 → ratio 1,7. El churn es tu palanca más barata, no la publicidad.
3. **Baja el CAC o sube el ARPU.** A CAC $150 tu ratio real sube a 2,0. Un plan anual o un tier más alto también mueve la aguja.
4. **Prueba con $1.000, no $10.000.** Valida el CAC real con dinero pagado (suele ser peor que el estimado) antes de escalar 10x un ratio dudoso.

**Conclusión:** ser rentable hoy con clientes que ya tienes no significa que puedas comprar clientes nuevos con ganancia. Tu economía de adquisición está en el filo. No le des a los $10.000. Arregla el churn, valida el CAC con una prueba chica, y recalcula.

¿Tienes el dato de churn desglosado por cohorte? Si los clientes viejos churnean mucho menos que los nuevos, el promedio de 8% te está engañando en la otra dirección y vale la pena verlo.