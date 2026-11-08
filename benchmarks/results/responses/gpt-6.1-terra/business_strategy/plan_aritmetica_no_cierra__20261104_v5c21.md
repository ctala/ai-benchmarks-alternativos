# GPT-6.1 Terra — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 12.349s | tokens_per_second: 69.2
- input_tokens: 198 | output_tokens: 854

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

**user:**

Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. ¿Lo aprobamos y lo ejecutamos?

PLAN:
1. Tenemos 200.000 visitas al mes en el sitio.
2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor del 1,5% (es un número conservador y realista para nuestro sector).
3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los suscriptores compra (también conservador).
4. Con eso llegamos cómodos a los $6.000/mes recurrentes.

Los porcentajes me parecen sanos y alcanzables. ¿Le damos?


## Respuesta completa

**No lo aprobaría tal como está.** Aunque aceptemos ambos porcentajes, la cuenta del plan no llega a $6.000 al mes:

| Paso mensual | Cálculo | Resultado |
|---|---:|---:|
| Nuevos suscriptores | 200.000 × 1,5% | 3.000 |
| Compradores | 3.000 × 2% | 60 |
| Ingresos por el curso | 60 × $30 | **$1.800** |

Faltan **$4.200 al mes**. Esto supone que cada mes se captan 3.000 suscriptores nuevos y que el 2% de esa cohorte compra en el mes.

Para llegar a $6.000 mensuales con el mismo precio necesitan **200 ventas al mes**. Manteniendo los demás supuestos, eso requeriría una de estas alternativas:

- **10.000 suscriptores nuevos al mes:** una conversión del 5% sobre las 200.000 visitas.
- **Una conversión a compra del 6,67%** sobre los 3.000 nuevos suscriptores.
- **Un ingreso promedio de $100 por venta**, manteniendo las 60 ventas.
- Aproximadamente **667.000 visitas al mes**, manteniendo ambas conversiones.

Además, vender un curso de pago único puede generar ventas cada mes, pero **no convierte esos ingresos en recurrentes por cliente**. Acumular una lista durante seis meses podría permitir un lanzamiento mayor; eso no demuestra que se puedan repetir $6.000 todos los meses.

**Recomendación:** probar el embudo, no comprometerse todavía con la meta. Midan suscriptores *nuevos*, compradores por cohorte y tiempo hasta la compra; después ajusten tráfico, conversión o ingreso por venta. Y aclaren si los $6.000 son ingresos brutos o beneficio: la cuenta anterior es antes de costos.