# Nemotron 3 Super — business_strategy/plan_aritmetica_no_cierra

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 47.0s | tokens_per_second: 59.9
- input_tokens: 219 | output_tokens: 2815

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

**No se aprueba.** Los números no llegan al objetivo y el plan tiene un fallo estructural en la palabra “recurrentes”.

Aquí está la multiplicación que tu socio omitió:

### 1. La aritmética del embudo
- Visitas al mes: 200.000
- Captura al 1,5%: **3.000 nuevos suscriptores/mes**
- Compra al 2% sobre esos nuevos suscriptores: **60 compradores/mes**
- Ingreso: 60 × $30 = **$1.800/mes**

Te faltan **$4.200 mensuales** (un 70% por debajo del objetivo).

### 2. El trampa de la “lista acumulada”
Si tu socio asume que cada mes le vende al 2% de *toda* la lista acumulada, el cuadro se ve así (sin contar bajas):

| Mes | Suscriptores acumulados | Compradores (2%) | Ingreso |
|-----|------------------------|------------------|---------|
| 1 | 3.000 | 60 | $1.800 |
| 2 | 6.000 | 120 | $3.600 |
| 3 | 9.000 | 180 | $5.400 |
| 4 | 12.000 | 240 | $7.200 |

Parece que llegan en el mes 4, pero **esto solo funciona si el mismo suscriptor compra el mismo curso de $30 todos los meses**, lo cual es imposible. Un curso es una transacción única. Una vez que los 60 compradores del mes 1 ya tienen el curso, no vuelven a pagar el mes 2. Los ingresos se estabilizan en torno a los **nuevos leads**: $1.800/mes.

### 3. “Recurrentes” es falso
Un curso de $30 no genera ingresos recurrentes. Para que sean recurrentes necesitarías:
- Una membresía/suscripción de $30/mes, o
- Un upsell/cross-sell mensual, o
- Que los clientes compren otro producto cada mes.

Nada de eso está en el plan.

### 4. Lo que se necesitaría realmente para $6.000/mes
Solo con tráfico orgánico y este curso:
- Necesitas **200 compradores/mes** a $30.
- Al 2% de conversión, eso significa **10.000 nuevos suscriptores/mes**.
- Al 1,5% de captura, eso significa **666.667 visitas/mes** (más de 3x lo que tienen hoy).

O bien:
- Subir el precio del producto (ej. $150 → solo necesitas 40 compradores/mes).
- Agregar un embudo con upsell (curso + mentoría + plantillas).
- Cambiar a membresía recurrente y trabajar retención/churn.

### Veredicto
**Rechazado.** El plan confía en una conversión mágica sobre una lista que se agota y en ingresos recurrentes de un producto de pago único. Antes de ejecutar, tu socio debe rehacer el modelo: definir si es membresía, agregar un segundo producto, o subir el precio. Vuelve a presentar cuando la multiplicación cierre solo con los nuevos suscriptores del mes.