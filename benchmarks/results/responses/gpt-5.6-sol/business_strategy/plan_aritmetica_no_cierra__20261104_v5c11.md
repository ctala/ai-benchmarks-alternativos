# GPT-5.6 Sol — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 9.59s | tokens_per_second: 88.3
- input_tokens: 198 | output_tokens: 847

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

**No lo aprobaría tal como está: la multiplicación no llega al objetivo.**

### Números reales del plan

- 200.000 visitas/mes × 1,5% = **3.000 suscriptores nuevos/mes**
- 3.000 × 2% = **60 compradores/mes**
- 60 × $30 = **$1.800/mes brutos**

El plan alcanza solo el **30% de la meta de $6.000**. Faltan **$4.200/mes**.

Además, un curso de pago único no genera ingresos “recurrentes”: cada comprador normalmente compra una sola vez. En seis meses, manteniendo esas tasas, serían aproximadamente **$10.800 acumulados**, no $6.000 mensuales recurrentes.

### Qué tendría que cambiar

Para facturar $6.000 a $30 se necesitan **200 ventas mensuales**. Algunas combinaciones:

- Mantener 1,5% de captura y 2% de compra: hacen falta **~667.000 visitas/mes**.
- Con 200.000 visitas y 2% de compra: la captura debe subir a **5%**.
- Con 200.000 visitas y 1,5% de captura: la conversión a compra debe ser **6,67%**.
- Mantener ambas conversiones: el precio tendría que ser **$100**.
- O combinar mejoras en captura, conversión, precio y upsells hasta multiplicar el ingreso por **3,33**.

Y eso es antes de descontar reembolsos, comisiones, impuestos y costos de adquisición/operación.

**Decisión:** no aprobarlo como plan para llegar a $6.000/mes. Sí aprobaría un piloto para validar el 1,5% y el 2%, pero con una reformulación económica clara y distinguiendo ingresos puntuales de ingresos recurrentes.