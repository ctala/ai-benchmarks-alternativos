# GPT-6 Astra — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-6-astra`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 14.227s | tokens_per_second: 44.5
- input_tokens: 198 | output_tokens: 633

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

**No lo aprobaría tal como está.** Los porcentajes pueden ser alcanzables, pero su multiplicación no llega al objetivo.

### La cuenta mensual

| Paso | Cálculo | Resultado |
|---|---|---:|
| Nuevos suscriptores | 200.000 visitas × 1,5% | 3.000 |
| Compradores | 3.000 suscriptores × 2% | 60 |
| Facturación | 60 compras × $30 | **$1.800/mes** |

El plan produce **el 30% de los $6.000 buscados**, antes de comisiones, devoluciones y otros costos. Falta multiplicar el resultado por **3,33**.

### ¿Acumular la lista durante seis meses lo resuelve?

No automáticamente. En seis meses tendrían **18.000 suscriptores**, suponiendo captaciones nuevas y sin bajas.

- Si el **2% compra una sola vez**, serían 360 ventas y **$10.800 acumulados en seis meses**, no $6.000 mensuales.
- Si esperan que compre el **2% de toda la lista cada mes**, están planteando una hipótesis distinta: deben demostrar que pueden sostener esa conversión sobre quienes todavía no compraron. No basta con reutilizar el 2% inicial.

Además, **un curso de pago único no genera ingresos recurrentes por sí mismo**. Puede generar ventas todos los meses, pero hay que conseguirlas de nuevo.

### ¿Qué tendría que cambiar?

Para facturar $6.000 mensuales necesitan **200 ventas de $30**. Manteniendo las demás variables, podrían alcanzar ese nivel con **una** de estas alternativas:

| Variable que cambia | Nivel necesario |
|---|---:|
| Visitas mensuales | ≈666.667 |
| Conversión de visita a suscriptor | 5% |
| Conversión de nuevo suscriptor a comprador | 6,67% |
| Precio del curso | $100 |

También podría funcionar una combinación, pero habría que validarla.

**Mi decisión: aprobar una prueba, no el plan de $6.000.** Mediría las conversiones reales y el tiempo hasta la compra por cohorte, y exigiría una proyección mes a mes que llegue al objetivo sin contar dos veces al mismo comprador. Que cada porcentaje parezca “sano” no significa que el resultado alcance.