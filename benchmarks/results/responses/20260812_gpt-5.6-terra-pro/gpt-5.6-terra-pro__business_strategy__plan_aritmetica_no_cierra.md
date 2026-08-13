# GPT-5.6 Terra Pro — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 18.657s | tokens_per_second: 174.9
- input_tokens: 5012 | output_tokens: 3263

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

### Cálculo del plan mensual

1. **200.000 visitas/mes**
2. Captura del **1,5%**  
   → 200.000 × 1,5% = **3.000 suscriptores/mes**
3. Compra del **2%** de esos suscriptores  
   → 3.000 × 2% = **60 ventas/mes**
4. Curso de **USD 30**  
   → 60 × USD 30 = **USD 1.800/mes**

### Resultado

El plan proyecta **USD 1.800/mes**, no USD 6.000/mes.

Faltan:

- **USD 4.200/mes**
- o un factor de aproximadamente **3,33×** sobre el resultado proyectado.

Además, un curso de pago único no genera ingresos “recurrentes” por sí mismo. Genera ventas mensuales mientras siga entrando tráfico y convirtiendo; no MRR, salvo que exista suscripción, renovaciones o recompras.

## Qué tendría que cambiar para llegar a USD 6.000/mes

Con precio de USD 30, necesitan:

- **200 ventas/mes** para llegar a USD 6.000.

Manteniendo la conversión de compra en 2%, requerirían:

- 200 / 2% = **10.000 suscriptores/mes**
- Con captura de 1,5%: 10.000 / 1,5% = **666.667 visitas/mes**

Alternativas equivalentes:

| Variable a modificar | Necesario para USD 6.000/mes |
|---|---:|
| Tráfico, manteniendo 1,5% captura y 2% compra | **666.667 visitas/mes** |
| Captura, manteniendo 200k visitas y 2% compra | **5%** |
| Conversión a compra, manteniendo 200k visitas y 1,5% captura | **6,67%** |
| Precio, manteniendo los embudos actuales | **USD 100** |
| Combinación de mejoras | Menor exigencia en cada variable |

## Matiz sobre los 6 meses

Si capturan 3.000 leads cada mes durante seis meses, acumularían **18.000 suscriptores**.

Si el 2% compra alguna vez durante ese período:

- 18.000 × 2% = **360 ventas**
- 360 × USD 30 = **USD 10.800 en seis meses**
- Promedio: **USD 1.800/mes**

Es decir: acumular lista no convierte este modelo en USD 6.000 mensuales automáticamente. Y si la conversión ocurre una sola vez por contacto, la lista acumulada tampoco permite vender el mismo curso repetidamente a las mismas personas.

## Recomendación

**No ejecutar el plan con la expectativa de llegar a USD 6.000/mes.** Sí se puede ejecutar como experimento, pero con una meta financiera corregida de aproximadamente **USD 1.800/mes** bajo esos supuestos.

Para aprobar una versión orientada a USD 6.000/mes, definiría explícitamente una de estas rutas:

1. Subir el ticket promedio a cerca de **USD 100** mediante curso premium, bundle, upsell o consultoría.
2. Llevar la captura a **5%**, manteniendo el resto.
3. Aumentar tráfico a alrededor de **667.000 visitas/mes**.
4. Usar una combinación realista de precio, conversión y tráfico.
5. Si el objetivo de verdad es ingreso recurrente, diseñar una oferta de suscripción/continuidad, no solo un curso único de USD 30.