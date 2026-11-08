# Claude Haiku 5.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 11.006s | tokens_per_second: 191.0
- input_tokens: 320 | output_tokens: 2102

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

**No lo aprobaría tal como está.** Los porcentajes pueden ser razonables, pero el plan no llega a $6.000/mes, y tiene un problema conceptual.

## 1. La cuenta

| Paso | Cálculo | Resultado |
|---|---|---|
| Suscriptores nuevos/mes | 200.000 × 1,5% | **3.000** |
| Compras/mes | 3.000 × 2% | **60** |
| Ingreso/mes | 60 × $30 | **$1.800** |

Eso es **30% de la meta**.

## 2. El problema de "recurrente"

El curso de $30 es una **venta única**. Cada suscriptor compra una vez y no vuelve a pagar. Si el ingreso mensual depende de que entren 3.000 suscriptores nuevos cada mes, el ingreso no se acumula: se reinicia cada mes. Con este diseño no hay ingreso recurrente, solo ventas puntuales.

## 3. Qué tendría que ser verdad para llegar a $6.000/mes

Con el curso a $30 necesitás **200 ventas/mes**. Con los porcentajes del plan:

- Necesitarías **10.000 suscriptores nuevos/mes** (no 3.000).
- Eso requiere **~670.000 visitas/mes**, más de 3 veces el tráfico actual.

O bien, mantener el tráfico y cambiar el precio o el modelo:

- Curso a $97: ~62 ventas/mes
- Curso a $300: ~20 ventas/mes
- Membresía a $20/mes: 300 suscriptores pagos activos (con churn, bastante más)

## 4. Sobre los porcentajes

Llamarlos "conservadores" no alcanza. Son supuestos sin datos:

- **1,5% de conversión a suscriptor** es optimista para un formulario genérico en un sitio de contenido. Muchos sitios están entre 0,3% y 1%. Hay que medirlo, no asumirlo.
- **2% de compra sobre la lista** depende mucho de la frecuencia de email, la calidad de la lista y la oferta. Sin datos previos, es una hipótesis.
- **200.000 visitas**: ¿son sesiones o usuarios únicos? ¿Cuántos son de tu público objetivo y no rebotan?

## 5. Lo que propondría

No ejecutar el plan completo. Hacer una prueba de 2 a 4 semanas para medir:

1. **Conversión real del formulario** (suscriptores / visitas únicas).
2. **Tasa de compra real** de la lista, con 2 o 3 emails de venta, no con una sola oferta.
3. **Costo de adquisición** si evaluás pagar tráfico.

Con esos números se puede calcular de nuevo qué precio, qué volumen de tráfico y qué modelo (único, membresía, o ambos) hacen falta para $6.000. Si el resultado da, se escala. Si no, se cambia el modelo antes de invertir seis meses.

¿Tienen datos actuales de conversión del sitio o de emails previos? Con eso el cálculo sale mucho más preciso.