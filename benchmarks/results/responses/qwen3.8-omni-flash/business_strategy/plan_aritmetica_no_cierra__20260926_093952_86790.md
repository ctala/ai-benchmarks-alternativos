# Qwen 3.8 Omni Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-omni-flash`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 182.772s | tokens_per_second: 58.8
- input_tokens: 256 | output_tokens: 10756

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

**Veredicto: no lo aprobamos tal cual.**  
Este plan muere exactamente donde tú dices: **en la multiplicación**. Los porcentajes pueden parecer razonables, pero el resultado no llega a la meta.

---

## 1. La cuenta real del plan

```text
200.000 visitas/mes
× 1,5% conversión a suscriptor
= 3.000 suscriptores/mes

3.000 suscriptores/mes
× 2% conversión a compra
= 60 compras/mes

60 compras/mes
× $30 por curso
= $1.800/mes brutos
```

**Meta:** $6.000/mes.  
**Resultado del plan:** $1.800/mes.  
**Brecha:** faltan $4.200/mes.  
**Factor que falta:** necesitas multiplicar por **3,33x**.

Dicho por visitante:

```text
Ingreso actual por visita = $1.800 / 200.000 = $0,009
Ingreso necesario por visita = $6.000 / 200.000 = $0,03
```

Hoy el plan genera **0,9 centavos por visita**. Necesitas **3 centavos por visita**.

---

## 2. Segundo problema: no es “recurrente”

Si el producto es un **curso de $30 de pago único**, eso **no genera ingresos recurrentes**. Genera ventas mensuales si cada mes repites tráfico, captura y conversión.

Es decir: no es MRR. Es revenue dependiente de mantener el embudo funcionando todos los meses.

Y además, esos $1.800 son brutos. Después de:

- comisiones de pasarela,
- reembolsos,
- impuestos,
- soporte,
- costos de email/plataforma,
- posible caída de conversión,

el número real será menor.

---

## 3. Si fuera realmente una suscripción de $30/mes, el plan igual está mal redactado

Si tu socio quisiera decir que no es un curso de $30, sino una **membresía de $30/mes**, entonces el modelo cambia.

Para llegar a **$6.000 MRR** con un plan de $30/mes necesitas:

```text
$6.000 / $30 = 200 miembros activos
```

Con el plan actual:

```text
200.000 visitas × 1,5% = 3.000 nuevos suscriptores/mes
3.000 × 2% = 60 nuevas compras/mes
```

Eso suma **60 miembros nuevos por mes**, no 200 activos inmediatos.

Sin churn, llegarías a 200 miembros activos en el mes 4:

```text
Mes 1: 60 miembros = $1.800 MRR
Mes 2: 120 miembros = $3.600 MRR
Mes 3: 180 miembros = $5.400 MRR
Mes 4: 240 miembros = $7.200 MRR
```

Pero eso asume:

- que el producto es recurrente, no un curso;
- que no hay churn;
- que no hay cobros fallidos;
- que los 60 nuevos miembros/mes se mantienen;
- que el tráfico y las conversiones se sostienen;
- que la operación aguanta la entrega.

Con churn real, la cosa se complica. Por ejemplo, con 30% de churn mensual, 60 altas/mes tienden a un techo de unos 200 miembros, justo el mínimo para $6.000 MRR, y tardarías bastante en acercarte.

Entonces: **si es recurrente, hay que reescribir el plan como suscripción, no como curso.**

---

## 4. Lo que tendría que cambiar para que los números lleguen a $6.000

Con las mismas 200.000 visitas, alguna de estas palancas tiene que moverse.

| Escenario | Visitas | Captura | Compra | Ticket | Resultado |
|---|---:|---:|---:|---:|---:|
| Plan actual | 200.000 | 1,5% | 2% | $30 | **$1.800/mes** |
| Subir ticket | 200.000 | 1,5% | 2% | $100 | **$6.000/mes** |
| Subir captura | 200.000 | 5% | 2% | $30 | **$6.000/mes** |
| Subir conversión de compra | 200.000 | 1,5% | 6,7% | $30 | **$6.000/mes** |
| Subir tráfico | 667.000 | 1,5% | 2% | $30 | **$6.000/mes** |
| Combinación moderada | 200.000 | 3% | 3,33% | $30 | **$6.000/mes** |

La opción más realista normalmente no es pedir 5% de captura o 6,7% de compra desde frío. Suele ser combinar:

- mejor oferta,
- ticket más alto,
- upsell,
- order bump,
- backend,
- membresía,
- o lista acumulada con secuencias de email.

Por ejemplo, con el plan actual tienes 60 compradores/mes. Para llegar a $6.000 necesitas un **ticket promedio de $100 por comprador**, no $30.

Eso podría lograrse con algo como:

```text
Curso base: $30
Upsell/membresía/coaching/order bump: contribuye $70 promedio por comprador
AOV final: $100
60 compradores × $100 = $6.000
```

Pero eso hay que modelarlo, no asumirlo.

---

## 5. Qué exigiría antes de aprobarlo

No aprobaría la ejecución hasta que el plan responda esto:

### A. ¿Es venta única o suscripción?

Si es venta única, hay que hablar de **ventas/mes**, no de recurrentes.

Si es suscripción, hay que hablar de:

- miembros activos,
- MRR,
- churn,
- cobros fallidos,
- LTV,
- payback,
- capacidad de soporte.

### B. ¿De dónde salen las 200.000 visitas?

No es lo mismo tener 200.000 visitas orgánicas calificadas que 200.000 visitas frías de blog, redes o tráfico genérico.

Hay que verificar:

- intención de búsqueda,
- fuente de tráfico,
- páginas donde aparece el formulario,
- calidad del lead magnet,
- historial de conversión,
- estacionalidad.

### C. ¿Están probadas las tasas del 1,5% y 2%?

Pueden ser sanas, pero “pueden ser” no es un plan. Necesitaríamos al menos:

- un test pequeño,
- benchmarks del sector,
- datos históricos,
- o una prueba con una cohorte real.

### D. ¿Cuál es la ruta concreta para cerrar el hueco de 3,33x?

El plan actual no cierra. Entonces hay que elegir una corrección explícita:

- subir precio,
- mejorar captura,
- mejorar conversión,
- añadir upsells,
- aumentar tráfico,
- o aceptar una meta menor.

### E. ¿Qué pasa en el escenario malo?

Si en vez de 1,5% capturamos 1%, y en vez de 2% compran 1%:

```text
200.000 × 1% = 2.000 suscriptores
2.000 × 1% = 20 compras
20 × $30 = $600/mes
```

Eso es un riesgo real. Un plan decente debería tener margen para aguantar escenarios conservadores.

---

## Conclusión

**No le damos todavía.**

Los porcentajes no son necesariamente locos, pero el plan no llega a $6.000/mes. Llega a **$1.800/mes brutos** y, además, usa mal el concepto de “recurrente”.

La versión corregida debería decir algo como:

> “Con 200.000 visitas/mes, capturamos 3.000 suscriptores. Vendemos 60 cursos de $30, lo que da $1.800/mes. Para llegar a $6.000 necesitamos subir el ticket promedio a $100, mejorar la captura al 5%, mejorar la conversión al 6,7%, aumentar el tráfico a 667.000 visitas/mes, o combinar varias de esas palancas.”

Si el socio trae ese plan corregido, con supuestos defendibles y una ruta clara para cerrar la brecha, entonces sí lo revisamos para aprobar. Pero **tal como está, no se ejecuta**.