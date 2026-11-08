# MiniMax M2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 11.009s | tokens_per_second: 88.5
- input_tokens: 188 | output_tokens: 974

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

# Tu cálculo tiene un error crítico

Tu LTV real no es $840. Es **$306**.

---

## Por qué tu cálculo está mal

| Tu cálculo | Cálculo correcto |
|------------|------------------|
| $35 × 24 meses = $840 | ($35 × 70% margen) ÷ 8% churn = **$306** |

Dos errores:

1. **No aplicaste el margen bruto**: El LTV se calcula con margen, no con ingreso bruto. Estás sobrestimando por 70%.

2. **Asumiste 24 meses de vida útil**: Con 8% de churn mensual, la vida media real es `1/churn = 12.5 meses`. Después de 24 meses solo te queda ~13% de los clientes.

---

## Tu métrica real

```
LTV/CAC = $306 / $290 = 1.06
```

Esto está **muy lejos de 3**. Estás apenas cubriendo el costo de adquisición.

## Payback

```
$290 CAC ÷ ($35 × 70% margen) = 11.8 meses para recuperar
```

Con churn de 8%, muchos clientes se fueron antes de que recuperes la inversión.

---

## Conclusión

**No le des.** Con $10,000 vas a captar ~34 clientes que te costaron $10,000 pero solo te generarán ~$10,400 en margen total. Estás operando con margen casi nulo.

## Qué necesitas para que funcione

Con las mismas métricas, necesitas una de estas:

- **Subir precio**: $55/mes → LTV/CAC = 1.67
- **Bajar churn a 4%**: LTV/CAC = 2.1
- **Bajar CAC a $100**: LTV/CAC = 3.06

Con 8% de churn y $290 de CAC, el unit economics no soporta escala.