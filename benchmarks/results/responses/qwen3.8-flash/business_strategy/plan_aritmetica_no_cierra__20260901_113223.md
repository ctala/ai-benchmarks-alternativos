# Qwen 3.8 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 57.817s | tokens_per_second: 85.6
- input_tokens: 256 | output_tokens: 4952

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

No, **tal como está no lo aprobamos**. El plan no llega a $6.000/mes con sus propios números.

## 1. La multiplicación del plan

Con los supuestos del plan:

**200.000 visitas/mes**  
× **1,5% conversión a suscriptor**  
= **3.000 suscriptores nuevos/mes**

**3.000 suscriptores**  
× **2% conversión a compra**  
= **60 ventas/mes**

**60 ventas**  
× **$30 por curso**  
= **$1.800/mes**

No $6.000.

El plan cierra con **$1.800/mes**, no con $6.000/mes.

---

## 2. Qué hace falta realmente para $6.000/mes

Para generar **$6.000/mes** con un producto de **$30**:

**$6.000 ÷ $30 = 200 ventas/mes**

Si solo el **2%** de los suscriptores compra:

**200 ÷ 2% = 10.000 suscriptores/mes**

Si solo el **1,5%** de las visitas se convierte en suscriptor:

**10.000 ÷ 1,5% = 666.667 visitas/mes**

Entonces, con las conversiones actuales, necesitarían:

> **666.667 visitas/mes**, no 200.000.

O mantener 200.000 visitas, pero mejorar otra palanca.

---

## 3. Opciones para que el plan sí cierre

Con **200.000 visitas/mes**, para llegar a **$6.000/mes** necesitan una combinación de estas:

| Opción | Qué cambiaría |
|---|---|
| Más tráfico | Pasar de 200.000 a **666.667 visitas/mes** |
| Mejor captura | Pasar de 1,5% a **5% de conversión a suscriptor** |
| Mejor compra | Pasar de 2% a **6,67% de conversión a compra** |
| Precio más alto | Pasar de $30 a **$100 por curso** |
| Mix | Por ejemplo: 300.000 visitas + 2,5% captura + 2,7% compra + $30 |

La versión actual necesita **3,33x más resultado** para llegar a $6.000.

---

## 4. Problema adicional: “recurrente”

Un curso de $30 normalmente es una venta **única**, no recurrente.

Si cada mes venden 60 cursos, eso es:

> **$1.800/mes de ventas nuevas**, no ingresos recurrentes.

Para que sea recurrente necesitarían algo como:

- suscripción mensual,
- comunidad de pago,
- membresía,
- coaching recurrente,
- upsells mensuales,
- o recompra constante.

Si el modelo es curso de pago único, el plan debería decir “$1.800/mes en ventas”, no “$6.000/mes recurrentes”.

---

## 5. Si la lista crece cada mes, ¿cambia algo?

Aunque la lista crezca, hay que definir el supuesto.

### Si venden a los suscriptores nuevos del mes:

Cada mes:

- 3.000 suscriptores nuevos,
- 2% compra,
- 60 ventas,
- $1.800/mes.

No mejora por acumulación.

### Si venden al total de la lista cada mes:

Mes 1: 3.000 suscriptores → 60 ventas → $1.800  
Mes 2: 6.000 suscriptores → 120 ventas → $3.600  
Mes 3: 9.000 suscriptores → 180 ventas → $5.400  
Mes 4: 12.000 suscriptores → 240 ventas → $7.200

Pero eso asume que la misma lista compra **2% cada mes**, lo cual es muy poco realista para un curso de pago único. La gente normalmente no compra el mismo curso varias veces.

Entonces, si el plan usa la lista acumulada, está inflando la proyección.

---

## 6. Veredicto

**No aprobaría la ejecución todavía.**

El plan tiene una buena base, pero el cálculo final está mal.

No es que los porcentajes sean necesariamente imposibles. El problema es que **los porcentajes elegidos no producen $6.000/mes**.

Antes de decir “le damos”, el socio debería responder una de estas:

1. ¿De dónde salen otras **466.667 visitas/mes**?
2. ¿Cómo pasan la captura de 1,5% a **5%**?
3. ¿Cómo pasan la conversión de compra de 2% a **6,67%**?
4. ¿Cómo suben el ticket de $30 a **$100**?
5. ¿Qué oferta recurrente, upsell o membresía convierte esto en $6.000/mes reales?
6. ¿Cuál es el modelo de lista: compradores nuevos, lista acumulada, recompra, churn?

---

## Mi recomendación

No aprueben el plan como está.

Aprueben una **revisión urgente del modelo de ingresos** y pidan una versión corregida.

El plan actual debería decir:

> “Con 200.000 visitas, 1,5% de captura, 2% de compra y curso de $30, llegamos a $1.800/mes.”

Para llegar a $6.000/mes, necesitan **3,33x más tráfico, conversión, precio o una combinación**.

Sin esa corrección, el plan muere en la multiplicación.