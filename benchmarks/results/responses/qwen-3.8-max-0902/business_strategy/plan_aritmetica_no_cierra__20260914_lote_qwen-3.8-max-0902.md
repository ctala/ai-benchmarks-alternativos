# Qwen 3.8 Max 0902 — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 8.05 | quality: 10.0
- latency_total: 118.451s | tokens_per_second: 42.9
- input_tokens: 256 | output_tokens: 5081

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

No. **Con esos números no lo aprueben todavía.**  
Los porcentajes pueden parecer razonables, pero la multiplicación no da.

## Cálculo real del plan

Plan propuesto:

1. **200.000 visitas/mes**
2. Conversión a suscriptor: **1,5%**
3. Conversión de suscriptor a compra: **2%**
4. Precio del curso: **$30**

### Paso 1: suscriptores

200.000 × 1,5% = **3.000 suscriptores/mes**

### Paso 2: compradores

3.000 × 2% = **60 compradores/mes**

### Paso 3: ingresos

60 × $30 = **$1.800/mes**

Resultado:

> **El plan genera $1.800/mes, no $6.000/mes.**

Faltan **$4.200/mes**.  
Necesitan vender **3,3 veces más** de lo que estima el plan.

---

## El problema principal

La fórmula actual es:

> Visitas × captura × conversión de compra × precio = ingresos

Para llegar a $6.000/mes con estos números:

> 200.000 × 1,5% × 2% × $30 = $1.800

No hay forma de que “cómodamente” llegue a $6.000.

---

## Además: no es recurrente si es un curso de $30

Un curso de $30 normalmente es una venta única.  
Si cada mes necesitan volver a conseguir 200 compradores nuevos para mantener $6.000/mes, eso no es realmente un ingreso recurrente.

Para hablar de **$6.000 USD/mes recurrentes**, necesitarían una de estas opciones:

- Suscripción mensual.
- Membresía.
- Producto con renovación.
- Ingresos por cohortes acumuladas, pero ahí hay que modelar churn, fatiga de lista y repetición de compra.

Si el curso es una venta única, lo correcto sería decir:

> “Queremos facturar $6.000 este mes vendiendo cursos.”

No:

> “Llegamos a $6.000/mes recurrentes.”

---

## ¿Qué tendría que cambiar para llegar a $6.000/mes?

Con el curso de $30, necesitan:

> $6.000 / $30 = **200 ventas/mes**

Hoy el plan estima **60 ventas/mes**.

Les faltan **140 ventas/mes**.

---

## Opciones para cerrar la brecha

### Opción 1: subir tráfico manteniendo conversiones

Si mantienen:

- Captura: 1,5%
- Compra: 2%
- Precio: $30

Necesitan:

> 666.667 visitas/mes aproximadamente.

Cálculo:

666.667 × 1,5% = 10.000 suscriptores  
10.000 × 2% = 200 compradores  
200 × $30 = $6.000

Es decir: necesitan **3,3 veces más tráfico**.

---

### Opción 2: subir la captura de emails

Manteniendo:

- 200.000 visitas
- 2% de compra
- Precio $30

Necesitan capturar:

> **5% de las visitas**

Cálculo:

200.000 × 5% = 10.000 suscriptores  
10.000 × 2% = 200 compradores  
200 × $30 = $6.000

Pasar de 1,5% a 5% de captura es posible, pero no se puede asumir sin cambiar fuerte el mecanismo: lead magnet, popup, intención de tráfico, landing específica, etc.

---

### Opción 3: subir la conversión de compra

Manteniendo:

- 200.000 visitas
- 1,5% captura
- Precio $30

Necesitan que compre:

> **6,67% de los suscriptores**

Cálculo:

200.000 × 1,5% = 3.000 suscriptores  
3.000 × 6,67% = 200 compradores  
200 × $30 = $6.000

Un 6,67% de compra puede ser posible si la lista está muy caliente o el producto es muy atractivo, pero asumirlo como “conservador” es peligroso.

---

### Opción 4: subir el precio

Manteniendo:

- 200.000 visitas
- 1,5% captura
- 2% compra

Con 60 ventas/mes, necesitarían un precio de:

> **$100**

Cálculo:

60 × $100 = $6.000

Esto puede ser más realista si agregan más valor, bonos, asesoría, plantillas, comunidad, etc.

---

### Opción 5: combinación de varias palancas

Por ejemplo:

- 200.000 visitas
- 2,5% captura
- 2,5% compra
- Precio promedio $96

Cálculo:

200.000 × 2,5% = 5.000 suscriptores  
5.000 × 2,5% = 125 compradores  
125 × $96 = $12.000

O una versión más moderada:

- 200.000 visitas
- 3% captura
- 2,5% compra
- Precio $40

Cálculo:

200.000 × 3% = 6.000 suscriptores  
6.000 × 2,5% = 150 compradores  
150 × $40 = $6.000

Esa combinación puede ser más alcanzable que depender de una sola variable.

---

## Mi recomendación como analista

No lo ejecuten como está porque el plan tiene un error estructural:

> **Confunde conversiones razonables con ingresos suficientes.**

Los porcentajes pueden ser sanos, pero la aritmética no llega.

### Yo no aprobaría este plan para llegar a $6.000/mes.

Lo aprobaría solo si lo reformulan así:

1. **Reconocen que el escenario base da $1.800/mes.**
2. **Eligen la palanca principal para multiplicar por 3,3:**
   - Más tráfico.
   - Mejor captura.
   - Mejor conversión de venta.
   - Mayor precio.
   - Producto recurrente.
   - Upsells/order bumps.
3. **Validan con datos reales antes de escalar.**

---

## Prueba rápida antes de ejecutar

Antes de comprometerse a 6 meses, hagan un test de 30 días con una muestra pequeña.

Por ejemplo, con 20.000 visitas:

Si esperan 1,5% captura:

20.000 × 1,5% = 300 suscriptores

Si esperan 2% compra:

300 × 2% = 6 ventas

Ingreso esperado:

6 × $30 = $180

Si ese test no da cerca de esas cifras, el plan grande tampoco dará.

---

## Versión corregida del objetivo

Con los números actuales, el plan realista es:

> “Con 200.000 visitas, 1,5% de captura, 2% de compra y un curso de $30, esperamos alrededor de $1.800/mes.”

Para llegar a $6.000/mes necesitan una de estas combinaciones:

| Escenario | Visitas | Captura | Compra | Precio | Ventas | Ingreso |
|---|---:|---:|---:|---:|---:|---:|
| Plan actual | 200.000 | 1,5% | 2% | $30 | 60 | $1.800 |
| Más tráfico | 666.667 | 1,5% | 2% | $30 | 200 | $6.000 |
| Mejor captura | 200.000 | 5% | 2% | $30 | 200 | $6.000 |
| Mejor compra | 200.000 | 1,5% | 6,67% | $30 | 200 | $6.000 |
| Mayor precio | 200.000 | 1,5% | 2% | $100 | 60 | $6.000 |
| Mix moderado | 200.000 | 3% | 2,5% | $40 | 150 | $6.000 |

---

## Respuesta final

**No le den todavía.**

Ejecutarlo así sería aprobar un plan que, según sus propios números, llega a **$1.800/mes**, no a **$6.000/mes**.

Si quieren llegar a $6.000/mes, necesitan corregir la fórmula:

> **200.000 × captura × conversión × precio = $6.000**

Y hoy:

> **200.000 × 1,5% × 2% × $30 = $1.800**

Mi veredicto:

> **No aprobar como plan definitivo. Aprobar solo como piloto de validación si aceptan que el objetivo real de corto plazo es $1.800/mes y definen qué palanca van a mover para multiplicar por 3,3.**