# Bonsai 2 27B — business_strategy/plan_aritmetica_no_cierra

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 61.675s | tokens_per_second: 30.5
- input_tokens: 256 | output_tokens: 1882

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



No. **No lo aprobamos tal cual.**

El plan **no llega a $6.000 USD/mes** con los números que pusiste.

## Cálculo

1. **Visitas:** 200.000  
2. **Conversión a suscriptor:** 1,5%  
   - 200.000 × 0,015 = **3.000 suscriptores/mes**

3. **Compra del curso:** 2% de los suscriptores  
   - 3.000 × 0,02 = **60 compradores/mes**

4. **Ingreso por curso:** $30  
   - 60 × $30 = **$1.800/mes**

Es decir, con este plan obtendríamos aproximadamente:

> **$1.800 USD/mes**, no $6.000.

La brecha es de **$4.200/mes**.

---

## El problema

El error está en la multiplicación final.

Muchos planes mueren aquí: se asume que 2% de 3.000 es suficiente para llegar al objetivo, pero 2% de 3.000 son solo **60 personas**.

Para llegar a **$6.000/mes** con un curso de **$30**, necesitarías:

> 6.000 / 30 = **200 compradores/mes**

Con 200.000 visitas y 1,5% de conversión a suscriptor, tendrías 3.000 suscriptores. Para llegar a 200 compradores, necesitarías una conversión de compra de:

> 200 / 3.000 = **6,67%**

Eso no es imposible, pero **no es igual a 2%**.

---

## Opciones para que el plan funcione

### Opción A: Mantener 200.000 visitas, 1,5% y 2%

Necesitarías vender:

> 6.000 / 60 = **$100 por curso**

Es decir, con los mismos flujos, el precio tendría que ser aproximadamente **$100**, no $30.

---

### Opción B: Mantener precio de $30 y 2% de compra

Necesitarías:

> 200 compradores / 0,02 = **10.000 suscriptores/mes**

Con 200.000 visitas, la conversión a suscriptor tendría que ser:

> 10.000 / 200.000 = **5%**

Eso es posible, pero **no es 1,5%**.

---

### Opción C: Mantener 1,5% y precio de $30

Necesitarías:

> 200 compradores / 0,015 = **13.333 suscriptores**

Espera, ahí hay un error conceptual: si la conversión a suscriptor es 1,5%, necesitas más visitas.

Para tener 10.000 suscriptores con 1,5% de conversión:

> 10.000 / 0,015 = **666.667 visitas/mes**

Eso ya es un plan muy distinto.

---

### Opción D: Mantener 200.000 visitas y 1,5%

Necesitarías una conversión de compra de:

> 200 / 3.000 = **6,67%**

Eso es la vía más simple de corregir el plan sin cambiar tráfico ni precio.

---

## Otra señal importante

El plan dice:

> “llegamos cómodos a los $6.000/mes recurrentes”

Pero si el curso cuesta **$30**, no queda claro si es:

1. **Venta única** de $30.
2. **Suscripción recurrente** de $30/mes.
3. **Suscriptor gratuito** que luego compra un curso.
4. **Curso con acceso mensual**.

Eso cambia completamente el modelo.

Si es una **venta única**, no son ingresos recurrentes.  
Si son recurrentes, hay que modelar retención, churn y LTV.

---

## Veredicto

**No lo aprobamos.**

Con los números presentados, el plan da:

> **$1.800/mes**

No $6.000.

Para aprobarlo, el plan necesita corregirse a una de estas versiones:

### Versión A: precio de $100

- 200.000 visitas
- 1,5% a suscriptor: 3.000
- 2% compra: 60
- Precio: $100
- Ingreso: **$6.000/mes**

### Versión B: conversión de compra del 6,67%

- 200.000 visitas
- 1,5% a suscriptor: 3.000
- 6,67% compra: 200
- Precio: $30
- Ingreso: **$6.000/mes**

### Versión C: más tráfico

- 666.667 visitas
- 1,5% a suscriptor: 10.000
- 2% compra: 200
- Precio: $30
- Ingreso: **$6.000/mes**

### Versión D: mejor embudo

- 200.000 visitas
- 3% a suscriptor: 6.000
- 3,34% compra: 200
- Precio: $30
- Ingreso: **$6.000/mes**

---

## Mi recomendación

No ejecutemos el plan original.

Les pido al socio que revise tres cosas:

1. **Precio del curso:** ¿realmente es $30?
2. **Tipo de ingreso:** ¿es venta única o recurrente?
3. **Conversión de compra:** ¿por qué 2%? ¿Tiene base o es solo una estimación?

Con esos tres puntos, podemos reconstruir el plan y decir si tiene sentido.

Pero con lo que está hoy, **no llega al objetivo**.