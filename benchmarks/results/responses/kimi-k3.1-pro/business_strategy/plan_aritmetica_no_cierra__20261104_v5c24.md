# Kimi K3.1 Pro — business_strategy/plan_aritmetica_no_cierra

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 7.84 | quality: 10.0
- latency_total: 156.32s | tokens_per_second: 26.5
- input_tokens: 321 | output_tokens: 4142

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

**No lo aprobaría tal cual.** Los porcentajes pueden ser razonables, pero **sus propios números solo llegan al 30% del objetivo**.

### La multiplicación del plan

- **200.000 visitas × 1,5%** = **3.000 suscriptores/mes**
- **3.000 suscriptores × 2%** = **60 compradores/mes**
- **60 compradores × $30** = **$1.800/mes brutos**

No son $6.000: faltan **$4.200/mes**. Para llegar al objetivo haría falta multiplicar el resultado por **3,33**.

### Tampoco serían $6.000 “recurrentes”

Un curso de $30 parece una **venta única**, no una suscripción. Por tanto, esos $1.800 dependerían de generar nuevas ventas cada mes; no son MRR demostrado.

Bajo el supuesto de 3.000 altas nuevas mensuales y un 2% de compra por cohorte, en seis meses tendrían:

- **18.000 suscriptores acumulados**
- **360 compradores**
- **$10.800 acumulados**, no $36.000 ni $6.000 mensuales recurrentes

Además, no se puede volver a aplicar indefinidamente ese 2% a toda la lista como si cada mes aparecieran compradores nuevos para el mismo curso.

### Qué tendría que cambiar para llegar a $6.000/mes

Se necesitan **200 ventas mensuales**:

$$6.000 \div 30 = 200$$

Algunas combinaciones matemáticas posibles:

| Palanca | Condición necesaria |
|---|---|
| Mantener tráfico y captura | Conversión de suscriptor a comprador de **6,67%**, no 2% |
| Mantener tráfico y compra del 2% | Captura de **5%**, no 1,5% |
| Mantener ambas conversiones | Aproximadamente **666.667 visitas/mes** |
| Mantener tráfico y conversiones | Precio de **$100**, aunque probablemente cambiaría la conversión |

También podrían combinar mejoras más moderadas en captura, conversión y precio.

### Decisión recomendada

**No aprobarlo como plan para $6.000 MRR. Sí aprobaría un piloto acotado** para medir altas nuevas reales, compra por cohorte, reembolsos e ingreso neto. El forecast inicial debería ser **$1.800/mes brutos bajo sus supuestos**, y el plan tendría que rehacerse con una palanca concreta que cierre la brecha de **3,33×**.

En resumen: **las tasas no son el problema aritmético; la conclusión sí.**