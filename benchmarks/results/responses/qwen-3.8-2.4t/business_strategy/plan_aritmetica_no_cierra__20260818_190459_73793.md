# Qwen 3.8 2.4T (A95B) — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 196.659s | tokens_per_second: 39.7
- input_tokens: 256 | output_tokens: 7807

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

**No. Yo no lo aprobaría ni lo ejecutaría así.**

El problema no es que los porcentajes sean “malos”. El problema es que **la multiplicación no llega a la meta**. El plan dice llegar “cómodos” a $6.000 USD/mes, pero los números actuales dan **$1.800 USD/mes**.

---

## 1. La matemática fría del plan

Plan propuesto:

1. **200.000 visitas/mes**
2. Conversión a suscriptor: **1,5%**
3. Conversión de suscriptor a compra: **2%**
4. Precio del curso: **$30**

Cálculo:

| Paso | Cálculo | Resultado |
|---|---:|---:|
| Visitas → suscriptores | 200.000 × 1,5% | 3.000 suscriptores/mes |
| Suscriptores → compradores | 3.000 × 2% | 60 compradores/mes |
| Compradores → ingresos | 60 × $30 | **$1.800/mes** |

Meta: **$6.000/mes**  
Resultado actual: **$1.800/mes**  
Faltante: **$4.200/mes**

Es decir: el plan actual solo llega al **30% del objetivo**.

Para llegar a $6.000/mes con un curso de $30, necesitan:

\[
\$6.000 / \$30 = 200 \text{ ventas/mes}
\]

Hoy el plan produce:

\[
60 \text{ ventas/mes}
\]

Necesitan **3,33 veces más** de lo que el funnel actual genera.

---

## 2. El error principal: confunde ventas nuevas con ingreso recurrente

El plan dice:

> “Con eso llegamos cómodos a los $6.000/mes recurrentes.”

Pero si el curso cuesta $30 y es un curso normal, probablemente sea un **pago único**, no un ingreso recurrente.

Si es pago único:

- Cada mes entran 3.000 suscriptores nuevos.
- Compra el 2%: 60 compradores.
- Ingreso mensual: $1.800.

Eso no se vuelve “recurrente” automáticamente.

---

## 3. Si lo miran acumulado a 6 meses, tampoco llega como ellos creen

Suponiendo que mantienen 200.000 visitas/mes durante 6 meses:

| Concepto | Cálculo | Resultado |
|---|---:|---:|
| Suscriptores nuevos por mes | 200.000 × 1,5% | 3.000 |
| Suscriptores acumulados en 6 meses | 3.000 × 6 | 18.000 |
| Compradores totales si compra el 2% | 18.000 × 2% | 360 |
| Ingreso total si cada uno paga $30 | 360 × $30 | $10.800 |

Eso sería **$10.800 en total durante 6 meses**, no $6.000 recurrentes cada mes.

Promedio mensual:

\[
\$10.800 / 6 = \$1.800/mes
\]

Otra vez: **$1.800/mes**, no $6.000/mes.

Si en el mes 6 le venden a toda la lista acumulada y consiguen que el 2% compre, podrían hacer un pico de:

\[
18.000 × 2% × \$30 = \$10.800
\]

Pero eso sería:

- un pico puntual,
- no recurrente,
- y asumiendo que el 2% de toda la lista acumulada compra en ese momento.

No es un MRR sano.

---

## 4. ¿Qué tendría que ser cierto para llegar a $6.000/mes?

Con el precio actual de **$30**, necesitan **200 ventas/mes**.

Eso significa que alguna de estas variables tiene que cambiar.

### Opción A: Mantener todo y subir tráfico

Si mantienen:

- conversión a suscriptor: 1,5%
- conversión a compra: 2%
- precio: $30

Necesitarían:

\[
200.000 × 3,33 = 666.667 \text{ visitas/mes}
\]

Es decir: **más de 666.000 visitas/mes**, no 200.000.

---

### Opción B: Mantener tráfico y subir conversión a suscriptor

Con:

- 200.000 visitas/mes
- conversión a compra: 2%
- precio: $30

Necesitarían capturar:

\[
1,5% × 3,33 = 5%
\]

Es decir: **5% de conversión de visita a suscriptor**.

Cálculo:

| Paso | Cálculo | Resultado |
|---|---:|---:|
| Visitas → suscriptores | 200.000 × 5% | 10.000 |
| Suscriptores → compradores | 10.000 × 2% | 200 |
| Ingresos | 200 × $30 | $6.000 |

---

### Opción C: Mantener captura y subir conversión de venta

Con:

- 200.000 visitas
- 1,5% de captura
- precio: $30

Necesitarían que compre:

\[
2% × 3,33 = 6,67%
\]

Es decir: **6,67% de los suscriptores**.

Cálculo:

| Paso | Cálculo | Resultado |
|---|---:|---:|
| Visitas → suscriptores | 200.000 × 1,5% | 3.000 |
| Suscriptores → compradores | 3.000 × 6,67% | 200 |
| Ingresos | 200 × $30 | $6.000 |

---

### Opción D: Subir el precio

Si mantienen el funnel actual:

- 3.000 suscriptores/mes
- 2% compra
- 60 ventas/mes

Para llegar a $6.000/mes, el precio debería ser:

\[
\$6.000 / 60 = \$100
\]

Es decir: necesitarían vender el curso a **$100**, no a $30.

Pero ojo: subir el precio puede bajar la conversión. No es automático.

---

## 5. Combinaciones posibles para llegar a $6.000/mes

Algunos escenarios que sí cerrarían la matemática:

| Visitas | Captura | Suscriptores | Venta | Compradores | Precio | Ingreso |
|---:|---:|---:|---:|---:|---:|---:|
| 200.000 | 5% | 10.000 | 2% | 200 | $30 | $6.000 |
| 200.000 | 1,5% | 3.000 | 6,67% | 200 | $30 | $6.000 |
| 200.000 | 2% | 4.000 | 2,5% | 100 | $60 | $6.000 |
| 200.000 | 2,5% | 5.000 | 3% | 150 | $40 | $6.000 |
| 200.000 | 3% | 6.000 | 2% | 120 | $50 | $6.000 |
| 200.000 | 1,5% | 3.000 | 2% | 60 | $100 | $6.000 |

Cualquiera de esas combinaciones puede ser válida, pero hay que probarla.

---

## 6. Si el curso fuera una suscripción de $30/mes, cambia la conversación

Si el producto no es un curso de pago único, sino una membresía de **$30/mes**, entonces sí se puede hablar de recurrente.

Con el plan actual:

- 3.000 suscriptores nuevos/mes
- 2% se convierte a pago recurrente
- 60 nuevos clientes pagos/mes

Si no hubiera churn, en 6 meses tendrían:

\[
60 × 6 = 360 \text{ clientes activos}
\]

\[
360 × \$30 = \$10.800 \text{ MRR}
\]

Pero eso asume:

1. que el 2% de cada cohorte mensual se suscribe,
2. que nadie cancela,
3. que el producto realmente tiene retención.

Con churn mensual, el número baja rápido.

Ejemplo aproximado con 60 nuevos clientes pagos por mes:

| Churn mensual | Clientes activos aprox. al mes 6 | MRR aprox. |
|---:|---:|---:|
| 0% | 360 | $10.800 |
| 10% | 281 | $8.430 |
| 20% | 221 | $6.640 |
| 25% | 197 | $5.920 |

Para sostener $6.000 MRR con 60 altas mensuales, necesitarían un churn mensual aproximadamente menor a **24-25%**.

No es imposible, pero hay que modelarlo. No se puede asumir “llegamos cómodos”.

---

## 7. Mi lectura como analista de crecimiento

El plan tiene tres problemas:

### Problema 1: La cuenta no da

El funnel actual produce $1.800/mes, no $6.000/mes.

### Problema 2: Usa la palabra “recurrente” sin un modelo recurrente

Un curso de $30, salvo que sea suscripción, no genera MRR automático.

### Problema 3: Supone porcentajes “conservadores” sin validación

1,5% de captura puede ser razonable.  
2% de venta por email puede ser razonable.  

Pero “razonable” no es lo mismo que “validado para nuestro tráfico, oferta y audiencia”.

---

## 8. ¿Qué deberían hacer antes de ejecutar?

No ejecuten el plan completo todavía. Hagan un piloto medible.

### Piloto recomendado de 30 días

Objetivo: validar si el funnel real se parece al plan.

Métricas mínimas:

1. Visitas reales al mes.
2. Tasa real de captura del formulario.
3. Tasa de apertura/click de emails.
4. Tasa real de compra.
5. Ingreso real generado.
6. Si es suscripción: churn y retención.

### Criterios de decisión

Si después de 30 días ven algo como:

- captura cercana a 5%, o
- conversión de venta cercana a 6,67%, o
- precio real sostenible de $100, o
- modelo recurrente con retención suficiente,

entonces sí pueden pensar en escalar.

Si el piloto confirma el escenario actual:

- 1,5% captura
- 2% venta
- precio $30

el resultado esperado será **$1.800/mes**, no $6.000/mes.

---

## 9. Versión corregida del objetivo

Para que el plan sea aprobable, debería decir algo así:

> “Para llegar a $6.000/mes con un producto de $30, necesitamos 200 ventas/mes.  
> Con 200.000 visitas, eso requiere una de estas condiciones:  
> - 5% de captura manteniendo 2% de venta,  
> - 6,67% de venta manteniendo 1,5% de captura,  
> - subir el precio a $100 manteniendo el funnel actual,  
> - o una combinación de captura, conversión y precio.  
> Validaremos en 30 días cuál de estas palancas es realista antes de escalar.”

Eso sí es un plan.

---

## Veredicto final

**No lo aprueben así.**

La idea puede ser buena, pero la matemática actual no sostiene el objetivo.

Con los números propuestos:

\[
200.000 × 1,5% × 2% × \$30 = \$1.800/mes
\]

Para llegar a $6.000/mes necesitan multiplicar el resultado por **3,33**.

Mi recomendación:

1. **No ejecutar el plan completo.**
2. Corregir el modelo.
3. Definir si el producto es pago único o suscripción.
4. Hacer un piloto de 30 días.
5. Recién aprobar el escalado si los datos reales muestran que pueden llegar a 200 ventas/mes o construir un MRR equivalente.

En resumen: **los porcentajes pueden ser sanos, pero la cuenta no llega. Así como está, no.**