# GPT-5.6 Terra — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 11.644s | tokens_per_second: 100.5
- input_tokens: 198 | output_tokens: 1170

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

No lo aprobaría tal como está. Los porcentajes pueden ser razonables, pero la multiplicación no llega al objetivo.

### Matemática del embudo mensual

| Etapa | Cálculo | Resultado |
|---|---:|---:|
| Visitas | — | 200.000 |
| Suscriptores | 200.000 × 1,5% | 3.000 |
| Compradores | 3.000 × 2% | 60 |
| Ingresos | 60 × USD 30 | **USD 1.800/mes** |

El plan produce **USD 1.800/mes**, no USD 6.000/mes.

Falta un factor de:

\[
6.000 / 1.800 = 3,33x
\]

Para llegar a USD 6.000/mes a USD 30, necesitan **200 ventas mensuales**, no 60.

### Qué tendría que cambiar para llegar a USD 6.000/mes

Manteniendo las otras variables constantes, cualquiera de estas opciones funcionaría:

- **Más tráfico:**  
  \[
  666.667\ visitas/mes \times 1,5\% \times 2\% \times USD30 \approx USD6.000
  \]

- **Mayor captura:** subir del **1,5% al 5%**, manteniendo 200.000 visitas y 2% de compra.

- **Mayor conversión de suscriptor a comprador:** subir del **2% al 6,67%**, manteniendo el 1,5% de captura.

- **Mayor precio/ticket promedio:** pasar de USD 30 a **USD 100**, manteniendo el resto igual.

- O una combinación de mejoras moderadas en tráfico, conversión y ticket.

### Ojo con “recurrentes”

Un curso de USD 30 normalmente es una venta única, no ingreso recurrente mensual.

Con 200.000 visitas mensuales, al cabo de 6 meses captarían:

\[
200.000 \times 1,5\% \times 6 = 18.000\ suscriptores
\]

Al 2% de conversión, eso equivale a:

\[
18.000 \times 2\% = 360\ ventas
\]

\[
360 \times USD30 = USD10.800
\]

Pero serían **USD 10.800 acumulados en seis meses** si cada lead compra una vez, no USD 6.000 mensuales recurrentes.

### Veredicto

**No ejecutar como plan aprobado para lograr USD 6.000/mes**, porque no cumple su propia meta financiera.

Sí aprobaría un experimento para validar los supuestos de 1,5% y 2%, pero con una meta correcta: aproximadamente **USD 1.800/mes** bajo las condiciones actuales. Antes de comprometerse con la meta de USD 6.000/mes, deben definir cuál palanca va a aportar el 3,33x faltante y aclarar si el producto es pago único o una suscripción real.