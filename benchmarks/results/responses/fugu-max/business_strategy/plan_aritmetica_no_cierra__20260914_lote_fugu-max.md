# Fugu Max — business_strategy/plan_aritmetica_no_cierra

- model_id: `sakana/fugu-max`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 14.687s | tokens_per_second: 87.6
- input_tokens: 271 | output_tokens: 1286

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

### Cálculo real del embudo

- Visitas: **200.000/mes**
- Suscriptores: 200.000 × 1,5% = **3.000**
- Compradores: 3.000 × 2% = **60**
- Ingresos: 60 × USD 30 = **USD 1.800/mes**

Faltan **USD 4.200/mes**. El plan alcanza apenas el **30% del objetivo**.

Además, hay dos problemas conceptuales:

1. **Un curso de USD 30 no es ingreso recurrente** salvo que sea una suscripción o exista una recompra periódica.
2. Si el 1,5% y el 2% se aplican mensualmente, el resultado esperado es **USD 1.800 mensuales**, no USD 6.000. Si la lista se acumula durante seis meses, eso puede generar más ventas en un lanzamiento, pero no convierte automáticamente el ingreso en recurrente.

### Qué tendría que cambiar

Para llegar a USD 6.000/mes manteniendo el precio de USD 30:

- Necesitan **200 compradores/mes**.
- Con una conversión de suscriptor a comprador del 2%, necesitan **10.000 suscriptores/mes**.
- Con una captura del 1,5%, eso exige aproximadamente **666.667 visitas/mes**.

O bien:

- Mantener 3.000 suscriptores y subir la conversión a compra al **6,67%**; o
- Mantener 60 compradores y subir el precio medio a **USD 100**; o
- Combinar precio mayor, mejor conversión y productos adicionales.

### Veredicto

**No ejecutaría este plan como plan para USD 6.000/mes.** Sí lo usaría como experimento inicial del embudo, pero con un objetivo explícito de validación: medir captación, conversión a compra, ingresos netos y recompra. Antes de aprobarlo como plan financiero, deben corregir la aritmética y definir si buscan **USD 6.000 de facturación puntual, mensual o recurrente**.