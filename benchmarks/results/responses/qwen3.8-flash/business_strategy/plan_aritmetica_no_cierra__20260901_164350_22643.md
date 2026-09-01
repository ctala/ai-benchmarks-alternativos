# Qwen 3.8 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 56.161s | tokens_per_second: 114.5
- input_tokens: 256 | output_tokens: 6433

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

**Veredicto: No lo aprobamos tal cual. El plan no llega a $6.000 USD/mes; llega a $1.800 USD/mes.**

Los porcentajes pueden sonar “sanos”, pero el problema no está en el porcentaje individual: está en la multiplicación final.

---

## 1. Revisemos los números del plan

Plan:

1. **200.000 visitas/mes**
2. Conversión a suscriptor: **1,5%**
3. Conversión de suscriptor a comprador: **2%**
4. Precio del curso: **$30**

Cálculo:

```text
200.000 visitas × 1,5% = 3.000 suscriptores nuevos/mes
3.000 suscriptores × 2% = 60 compradores/mes
60 compradores × $30 = $1.800/mes
```

**Resultado del plan: $1.800 USD/mes.**

Objetivo: **$6.000 USD/mes.**

Faltan:

```text
$6.000 - $1.800 = $4.200
```

O sea, el plan cubre solo el **30%** del objetivo.

---

## 2. La multiplicación real del plan

El plan dice:

- 1,5% de las visitas se suscriben.
- 2% de los suscriptores compran.

La conversión efectiva desde visita hasta compra es:

```text
1,5% × 2% = 0,03%
```

No es 3,5%. No se suman. Se multiplican.

Con 200.000 visitas:

```text
200.000 × 0,03% = 60 compras
```

Para llegar a $6.000 con un producto de $30, necesitas:

```text
$6.000 / $30 = 200 compras/mes
```

Tu plan produce **60 compras/mes**, no 200.

Te faltan **140 compras/mes**.

La conversión visita → compra que necesitas es:

```text
200 compras / 200.000 visitas = 0,1%
```

Tu plan asume:

```text
0,03%
```

Necesitas multiplicar por:

```text
0,1% / 0,03% = 3,33x
```

**El plan está a 3,33 veces menos de lo necesario.**

---

## 3. ¿Qué tendría que cambiar para que sí llegue a $6.000?

Hay varias combinaciones posibles. Pero hay que decidir cuál.

### Opción A: Mantener tráfico y captura, mejorar conversión a compra

Si mantenemos:

- 200.000 visitas
- 1,5% de captura
- Precio $30

Necesitas:

```text
3.000 suscriptores × X = 200 compradores
X = 200 / 3.000 = 6,67%
```

Entonces la conversión de suscriptor a comprador debería ser:

```text
6,67%
```

No 2%.

---

### Opción B: Mantener tráfico y conversión a compra, mejorar captura

Si mantenemos:

- 200.000 visitas
- 2% de conversión a compra
- Precio $30

Necesitas:

```text
200 compradores / 2% = 10.000 suscriptores
```

Y para conseguir 10.000 suscriptores desde 200.000 visitas:

```text
10.000 / 200.000 = 5%
```

Entonces la conversión de visita a suscriptor debería ser:

```text
5%
```

No 1,5%.

---

### Opción C: Mantener captura y conversión, subir precio

Si mantenemos:

- 200.000 visitas
- 1,5% de captura
- 2% de compra

Tendrás:

```text
60 compras/mes
```

Para llegar a $6.000:

```text
$6.000 / 60 = $100
```

El producto debería costar:

```text
$100
```

No $30.

---

### Opción D: Mantener todo igual y aumentar tráfico

Si mantenemos:

- 1,5% captura
- 2% compra
- $30 producto

Necesitas:

```text
200 compras/mes
```

Pero cada 200.000 visitas te dan 60 compras.

Entonces necesitas:

```text
200 / 60 = 3,33x más tráfico
```

Es decir:

```text
200.000 × 3,33 = 666.667 visitas/mes
```

Aproximadamente:

```text
667.000 visitas/mes
```

---

## 4. Tabla rápida de escenarios

| Escenario | Visitas | Captura | Compra | Precio | Resultado |
|---|---:|---:|---:|---:|---:|
| Plan actual | 200.000 | 1,5% | 2% | $30 | $1.800 |
| Subir conversión a compra | 200.000 | 1,5% | 6,67% | $30 | $6.000 |
| Subir captura | 200.000 | 5% | 2% | $30 | $6.000 |
| Subir precio | 200.000 | 1,5% | 2% | $100 | $6.000 |
| Subir tráfico | 667.000 | 1,5% | 2% | $30 | $6.000 |
| Combinación moderada | 200.000 | 2,5% | 4% | $30 | $6.000 |

Esa última es interesante: con 2,5% de captura y 4% de conversión a compra, ya llegarías:

```text
200.000 × 2,5% = 5.000 suscriptores
5.000 × 4% = 200 compradores
200 × $30 = $6.000
```

Pero eso implica subir ambas conversiones.

---

## 5. Hay otro problema: “recurrentes”

El plan dice:

> “Con eso llegamos cómodos a los $6.000/mes recurrentes.”

Eso no es correcto si el curso cuesta $30 como venta única.

Un curso de $30 no es necesariamente recurrente. Es ingreso puntual.

Si quieres $6.000 USD **recurrentes**, necesitas algo así:

- membresía,
- suscripción mensual,
- comunidad,
- acceso continuo,
- servicio recurrente,
- o un modelo donde los clientes paguen cada mes.

Si es un curso de pago único, lo que tienes es:

```text
$1.800 de ingresos este mes
```

No:

```text
$1.800 de ingresos recurrentes garantizados
```

Cada mes necesitarás volver a conseguir 60 compras nuevas.

---

## 6. Si están vendiendo a una lista acumulada, el plan también está incompleto

Hay una posible defensa del plan: “pero los suscriptores se acumulan”.

Por ejemplo:

- Mes 1: 3.000 suscriptores
- Mes 2: 6.000 suscriptores
- Mes 3: 9.000 suscriptores
- Mes 4: 12.000
- Mes 5: 15.000
- Mes 6: 18.000

Si cada mes vendieran a toda la lista acumulada y un 2% comprara:

```text
18.000 × 2% = 360 compradores
360 × $30 = $10.800
```

Pero eso asume cosas muy fuertes:

1. Que todos los suscriptores siguen activos.
2. Que no hay fatiga de email.
3. Que el 2% compra todos los meses.
4. Que no hay churn.
5. Que no necesitas campañas nuevas.
6. Que los compradores no ya compraron antes.
7. Que la lista no se quema.
8. Que puedes monetizar toda la lista cada mes con la misma conversión.

Eso no está en el plan.

Como está escrito, el plan parece decir:

```text
cada mes capturas 3.000 suscriptores nuevos
y vendes a esos 3.000 suscriptores nuevos
```

En ese caso, el resultado es $1.800.

---

## 7. Lo que yo aprobaría vs. lo que no aprobaría

### No aprobaría:

> “200.000 visitas, 1,5% captura, 2% compra, $30 curso = $6.000 recurrentes.”

Eso está mal calculado.

### Sí aprobaría condicionalmente si el plan demuestra una de estas rutas:

1. Que pueden conseguir **más tráfico**.
2. Que pueden subir la **captura a 5%**.
3. Que pueden subir la **conversión a compra a 6,67%**.
4. Que pueden vender un producto de **$100**.
5. Que pueden combinar: por ejemplo, 2,5% captura + 4% compra + $30.
6. Que pueden crear un modelo **recurrente** con 200 suscriptores pagando $30/mes.
7. Que pueden monetizar una lista acumulada con un modelo realista de campañas, churn y repeat purchase.

---

## 8. Mi recomendación

No ejecutemos el plan como está.

Pediría una versión corregida con esta pregunta central:

> ¿Cómo llegamos exactamente a 200 compras de $30 al mes, o al equivalente en precio/recurrencia?

También pediría que desglosen:

- ¿Visitas reales o uniques?
- ¿Qué porcentaje del tráfico es cualificado?
- ¿El formulario estará visible en 200.000 visitas o solo en algunas?
- ¿1,5% de captura es sobre todas las visitas o sobre sesiones específicas?
- ¿2% de compra es sobre suscriptores nuevos o sobre toda la lista?
- ¿Cada suscriptor puede comprar más de una vez?
- ¿El curso es venta única o suscripción?
- ¿Hay upsells, bundles, coaching, membresía o order bump?
- ¿Cuál es el precio promedio real, no solo el headline?
- ¿Qué pasa con devoluciones?
- ¿Qué pasa con churn?
- ¿Qué pasa con entregabilidad de email?
- ¿Qué pasa con la frecuencia de ofertas?

---

## 9. Resumen brutal

El plan actual produce:

```text
$1.800/mes
```

El objetivo es:

```text
$6.000/mes
```

Para llegar a $6.000 con un producto de $30, necesitas:

```text
200 compras/mes
```

El plan produce:

```text
60 compras/mes
```

Por lo tanto:

```text
No está aprobado.
```

La versión “conservadora” del plan no es conservadora en el resultado: es insuficiente. Y encima confunde ingreso puntual con ingreso recurrente.