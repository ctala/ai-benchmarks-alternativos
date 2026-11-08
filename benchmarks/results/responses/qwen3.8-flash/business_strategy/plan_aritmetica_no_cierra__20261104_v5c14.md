# Qwen 3.8 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 33.506s | tokens_per_second: 80.9
- input_tokens: 256 | output_tokens: 2709

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

No. **No lo apruebo como está.** El plan no llega al objetivo con sus propios números; el error está en la multiplicación.

## 1. Verificación del plan

**Paso 1: Captura de suscriptores**

- Visitas: **200.000/mes**
- Conversión a suscriptor: **1,5%**

\[
200.000 \times 0,015 = 3.000 \text{ suscriptores/mes}
\]

**Paso 2: Ventas del curso**

- Suscriptores: **3.000**
- Conversión a compra: **2%**

\[
3.000 \times 0,02 = 60 \text{ ventas/mes}
\]

**Paso 3: Ingreso**

- Precio del curso: **$30 USD**

\[
60 \times 30 = 1.800 \text{ USD/mes}
\]

## Resultado real del plan

El plan genera:

> **$1.800 USD/mes**

El objetivo es:

> **$6.000 USD/mes**

Es decir, el plan está corto por:

\[
6.000 - 1.800 = 4.200
\]

O en términos de brecha:

\[
6.000 / 1.800 = 3,33
\]

El plan necesita multiplicar por **3,33 veces** su resultado actual.

---

## 2. Para llegar a $6.000 con curso de $30

Necesitas:

\[
6.000 / 30 = 200 \text{ ventas/mes}
\]

Si solo **2% de los suscriptores compra**, necesitas:

\[
200 / 0,02 = 10.000 \text{ suscriptores/mes}
\]

Con **200.000 visitas/mes**, para conseguir 10.000 suscriptores necesitas una conversión de captura de:

\[
10.000 / 200.000 = 0,05 = 5\%
\]

Entonces, con el plan actual, una de estas cosas debe ser verdadera:

| Variable | Plan actual | Necesitas para $6.000 |
|---|---:|---:|
| Visitas/mes | 200.000 | 666.667 |
| Conversión a suscriptor | 1,5% | 5% |
| Conversión suscriptor → compra | 2% | 6,67% |
| Precio del curso | $30 | $100 |
| Ventas/mes | 60 | 200 |

---

## 3. Hay otro problema conceptual: “recurrentes”

El plan dice:

> “Con eso llegamos cómodos a los $6.000/mes recurrentes.”

Pero un curso de $30 normalmente es una venta **única**, no recurrente.

Para que sea recurrente, necesitas algo como:

- membresía mensual,
- suscripción a contenido,
- acceso continuo,
- upsell recurrente,
- renovación automática,
- comunidad paga,
- servicio mensual,
- o una nueva oferta cada mes.

Si el curso es una compra única, no puedes llamarlo “$6.000/mes recurrentes” salvo que cada mes haya una nueva cohorte de compradores, y eso no es recurrencia, es crecimiento de ventas mensuales.

---

## 4. La ambigüedad peligrosa

Hay una interpretación que podría hacer parecer que el plan sí funciona:

Si cada mes capturas 3.000 suscriptores nuevos, después de 6 meses tendrías 18.000 suscriptores totales. Si vendes a todo el listado cada mes y 2% compra, tendrías:

\[
18.000 \times 0,02 = 360 \text{ ventas/mes}
\]

\[
360 \times 30 = 10.800 \text{ USD/mes}
\]

Pero eso es muy improbable porque implica que la misma lista compra repetidamente el mismo curso todos los meses.

Lo realista es:

- 2% de los **nuevos suscriptores** compra una vez, o
- 2% de la lista compra una oferta específica una sola vez, no mensualmente.

Por eso el cálculo limpio del plan es:

> **$1.800/mes**, no $6.000/mes.

---

## 5. Decisión

**No aprobar el plan como está.**

El plan no llega al objetivo con sus propios supuestos. Los porcentajes pueden ser “conservadores”, pero la multiplicación no cierra.

### Opción A: Ajustar el plan

Para que el plan sea aprobable, necesita una de estas correcciones:

1. **Subir conversión de captura de 1,5% a 5%**  
   Muy difícil si 1,5% ya se considera conservador.

2. **Subir conversión de compra de 2% a 6,67%**  
   También muy difícil para un curso frío desde lista.

3. **Subir precio de $30 a $100**  
   Más razonable, pero requiere justificar el valor.

4. **Aumentar visitas de 200.000 a 666.667**  
   Necesitarías un plan de tráfico fuerte.

5. **Añadir upsells o recurrencia**  
   Por ejemplo: curso de $30 + membresía de $30/mes + upsell de $99.

### Opción B: Aprobar una versión corregida

Un plan más realista sería:

- 200.000 visitas/mes
- 1,5% captura = 3.000 suscriptores
- 2% compra curso = 60 ventas
- 60 × $30 = $1.800

Para llegar a $6.000, necesitas agregar **$4.200 más** desde otra fuente:

Ejemplo:

| Fuente | Ventas | Ticket | Ingreso |
|---|---:|---:|---:|
| Curso $30 | 60 | $30 | $1.800 |
| Upsell $99 | 20 | $99 | $1.980 |
| Membresía $49 | 20 | $49 | $980 |
| Servicio/producto adicional | 3 | $213 | $639 |
| **Total** |  |  | **$6.399** |

O algo más simple:

- 100 ventas de curso a $30 = $3.000
- 30 ventas de upsell a $100 = $3.000
- Total = $6.000

Eso sí requiere que el 30% de los compradores del curso acepte el upsell, lo cual también necesita validación.

---

## Conclusión

**No le demos.**

El plan actual genera:

> **$1.800/mes**

No:

> **$6.000/mes**

Y además confunde venta puntual con ingreso recurrente.

Para aprobarlo, el socio debe corregir la multiplicación y mostrar cómo llega a 200 ventas/mes, o cómo sube el ticket promedio, o cómo añade recurrencia real.