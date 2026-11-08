# GPT-6.1 Sol — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 13.572s | tokens_per_second: 57.4
- input_tokens: 186 | output_tokens: 779

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

**No daría luz verde a $10.000 para escalar con estos números.** Puedes ser rentable hoy, pero eso no significa que adquirir más clientes por este canal sea rentable.

### Recalculando tu LTV

Con churn mensual constante del 8%, la vida media esperada no es de 24 meses:

\[
\text{Vida media} = \frac{1}{0,08} = 12,5\text{ meses}
\]

Además, para compararlo con CAC debes usar **margen bruto**, no ingresos:

| Métrica | Cálculo | Resultado |
|---|---|---:|
| Margen bruto mensual por cliente | $35 × 70% | **$24,50** |
| LTV de ingresos | $35 ÷ 8% | $437,50 |
| LTV de margen bruto | $24,50 ÷ 8% | **$306,25** |
| LTV/CAC | $306,25 ÷ $290 | **1,06×** |
| Contribución esperada tras adquisición | $306,25 − $290 | **$16,25 por cliente** |

Esto supone churn y margen constantes, sin descontar los flujos futuros. Esos **$16,25 todavía tienen que cubrir cualquier coste no incluido en tu margen bruto**.

Y un detalle: incluso tu cálculo original, $840 ÷ $290 = 2,90, queda **por debajo de 3**, no por encima.

### ¿Qué pasa si inviertes los $10.000?

Si el CAC se mantiene:
- Adquieres unos **34–35 clientes**.
- Generan aproximadamente **$10.560 de margen bruto durante toda su vida**.
- Tras publicidad, quedan apenas **$560**, antes de otros costes y del valor temporal del dinero.

No es un retorno mensual: se acumula a lo largo de la vida de esos clientes. Un aumento del CAC de apenas **5,6%** eliminaría incluso ese pequeño excedente.

### La recuperación de caja también importa

El payback simple es $290 ÷ $24,50 = **11,8 meses**, pero **ignora las bajas**. Incorporando el churn del 8%, una cohorte tarda aproximadamente **36 meses** en devolver el gasto publicitario mediante su margen bruto esperado.

### Mi recomendación

**No escales fuerte todavía.** Si necesitas validar el canal, utiliza una prueba limitada y mide retención y margen de las cohortes adquiridas por publicidad.

Como referencia, para lograr un LTV/CAC de **3×**, manteniendo los demás datos, necesitarías:
- **CAC de unos $102 o menos**, o
- **Churn mensual de aproximadamente 2,8% o menos**, manteniendo CAC de $290.

**Hoy no tienes margen para escalar con seguridad: estás prácticamente comprando $1 de margen bruto futuro por $0,95 de publicidad hoy.**