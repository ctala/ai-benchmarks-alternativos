# GPT-6.1 Sol — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 8.12s | tokens_per_second: 59.2
- input_tokens: 198 | output_tokens: 481

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

**No lo aprobaría tal como está: sus propios números no llegan al objetivo.** Que los porcentajes parezcan razonables no significa que la multiplicación cierre.

| Paso | Cálculo | Resultado mensual |
|---|---|---:|
| Nuevos suscriptores | 200.000 × 1,5% | 3.000 |
| Compradores | 3.000 × 2% | 60 |
| Facturación | 60 × USD 30 | **USD 1.800** |

Eso es **el 30% de la meta**, antes de comisiones, devoluciones y otros costos. Faltan USD 4.200 mensuales.

### ¿Qué tendría que cambiar?
Para facturar USD 6.000 al mes, manteniendo las demás variables, necesitarían **una** de estas opciones, o una combinación:

- **Tráfico:** unas 666.667 visitas mensuales.
- **Captación:** convertir el 5% de las 200.000 visitas en suscriptores.
- **Compra:** convertir el 6,67% de los 3.000 nuevos suscriptores.
- **Ticket:** cobrar USD 100 en lugar de USD 30.

Son umbrales matemáticos, no evidencia de que sean alcanzables.

### Además, “mensual” no significa “recurrente”
Un curso de pago único genera ventas puntuales, **no ingresos recurrentes contratados**. Para sostener la facturación hay que conseguir compradores nuevos cada mes.

Y acumular lista durante seis meses no resuelve automáticamente el problema: con 18.000 suscriptores, una campaña que convierta al 2% produciría USD 10.800 **una vez**, no USD 10.800 todos los meses. No pueden asumir que los mismos suscriptores volverán a comprar el mismo curso.

**Mi decisión: aprobaría una prueba del embudo, no el plan de USD 6.000/mes.** Primero mediría captación y compra reales —con un plazo de conversión definido— y exigiría una proyección mes a mes que distinga nuevos suscriptores, compradores únicos y facturación. Con las hipótesis actuales, el ritmo previsto es **USD 1.800/mes, no USD 6.000**.