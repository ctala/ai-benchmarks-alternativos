# Qwen 3.8 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 90.092s | tokens_per_second: 90.2
- input_tokens: 256 | output_tokens: 8124

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

**Veredicto: No, no lo apruebo tal como está.**  
El plan tiene una buena intuición de funnel, pero **no llega al objetivo por un error de multiplicación**.

## 1. La multiplicación del plan

La fórmula del negocio es:

**Visitas × conversión a suscriptor × conversión a comprador × precio = ingresos**

Aplicando los números del plan:

- 200.000 visitas/mes  
- 1,5% se convierte en suscriptor  
- 2% de suscriptores compra  
- Curso de $30  

Cálculo:

**200.000 × 1,5% = 3.000 suscriptores nuevos/mes**

**3.000 × 2% = 60 ventas/mes**

**60 × $30 = $1.800/mes**

Entonces el plan genera:

> **$1.800 USD/mes**, no $6.000 USD/mes.

Falta un factor de **3,33x**.

Para llegar a $6.000 con un curso de $30, necesitas:

**$6.000 / $30 = 200 ventas/mes**

Pero el plan solo produce:

**60 ventas/mes**

Gap:

**200 - 60 = 140 ventas adicionales/mes**

---

## 2. El problema no es necesariamente “conservador”, es que no cuadra

Dices que los porcentajes te parecen sanos y alcanzables. Puede que sí.  
Pero incluso si fueran realistas, el resultado no es $6.000.

El plan está diciendo:

> “Con 3.000 suscriptores nuevos/mes y 2% de conversión a venta, llegamos cómodos a $6.000.”

Eso es falso aritméticamente.

Con esos números:

- Si el curso cuesta $30, necesitas **6,67% de conversión de suscriptor a comprador**.
- Si la conversión a compra es 2%, necesitas **10.000 suscriptores nuevos/mes**.
- Si mantienes 1,5% de conversión a suscriptor, necesitas **666.667 visitas/mes**.
- Si mantienes 200.000 visitas, 1,5% y 2%, necesitas un ticket promedio de **$100**.

---

## 3. Tabla de ajustes posibles para llegar a $6.000

| Escenario | Visitas/mes | Conversión a suscriptor | Conversión a compra | Precio | Ingresos |
|---|---:|---:|---:|---:|---:|
| Plan actual | 200.000 | 1,5% | 2% | $30 | $1.800 |
| Subir precio | 200.000 | 1,5% | 2% | $100 | $6.000 |
| Subir conversión a compra | 200.000 | 1,5% | 6,67% | $30 | $6.000 |
| Subir conversión a suscriptor | 200.000 | 5% | 2% | $30 | $6.000 |
| Subir tráfico | 666.667 | 1,5% | 2% | $30 | $6.000 |
| Necesidad real | 200.000 | 1,5% | 2% | $30 | Necesita 200 ventas |

---

## 4. Ojo con “recurrentes”

El plan dice:

> “Con eso llegamos cómodos a los $6.000/mes recurrentes.”

Eso también está mal si el curso cuesta $30 una sola vez.

Un curso de $30 no es recurrente a menos que sea:

- membresía mensual,
- suscripción,
- comunidad,
- acceso continuo,
- servicio recurring.

Si es curso one-time, entonces es revenue, no MRR.

Si es una suscripción de $30/mes, la matemática sigue igual:

- 3.000 suscriptores nuevos/mes
- 2% compra membresía
- 60 miembros nuevos/mes
- $1.800 MRR

Para tener $6.000 MRR necesitas 200 miembros activos, no 60.

---

## 5. Posible confusión: ¿2% de suscriptores nuevos o de la lista acumulada?

Hay una ambigüedad importante.

### Si el 2% aplica a suscriptores nuevos cada mes

Resultado:

- Mes 1: 3.000 leads → 60 ventas → $1.800
- Mes 2: 3.000 nuevos leads → 60 ventas → $1.800
- Mes 3: 3.000 nuevos leads → 60 ventas → $1.800

No crece.

### Si el 2% aplica a la lista acumulada cada mes

Entonces:

| Mes | Leads acumulados | 2% compra | Ventas | Ingresos |
|---|---:|---:|---:|---:|
| 1 | 3.000 | 2% | 60 | $1.800 |
| 2 | 6.000 | 2% | 120 | $3.600 |
| 3 | 9.000 | 2% | 180 | $5.400 |
| 4 | 12.000 | 2% | 240 | $7.200 |
| 5 | 15.000 | 2% | 300 | $9.000 |
| 6 | 18.000 | 2% | 360 | $10.800 |

Pero esto tiene un problema serio:

Si el curso es de compra única, no puedes venderle el mismo curso a la misma persona cada mes.  
Si el 2% mensual aplica a toda la lista acumulada, estás asumiendo que cada mes un 2% distinto compra.

En el mes 6, eso implicaría que 1.260 personas compraron sobre una base de 18.000 leads:

**1.260 / 18.000 = 7% de conversión acumulada**

Eso ya no suena “conservador”.  
Es un funnel muy agresivo.

Además, ignora:

- bajas,
- spam,
- no apertura,
- fatiga de lista,
- compradores repetidos,
- estacionalidad,
- churn.

---

## 6. La mejor corrección probable: subir el ticket promedio

Si ya tienes 200.000 visitas/mes, la palanca más rápida no suele ser triplicar tráfico.

Es subir el valor capturado por comprador.

Con los números actuales:

- 3.000 suscriptores/mes
- 2% compra
- 60 compradores/mes

Para llegar a $6.000:

**$6.000 / 60 compradores = $100 de ticket promedio**

Es decir:

> Necesitas que cada comprador promedio gaste $100, no $30.

Eso puede lograrse con:

- curso + plantillas,
- curso + mentoría,
- curso + comunidad,
- upsell a $70,
- order bump de $20,
- bundle de productos,
- oferta de $99,
- membresía de $30/mes con permanencia promedio de 3-4 meses,
- venta de servicios de alto ticket.

Ese es el camino más razonable si no quieres depender de tráfico nuevo.

---

## 7. Lo que yo le pediría al socio antes de aprobar

Necesito que responda esto:

1. **¿Las 200.000 visitas son actuales o proyectadas?**
2. **¿El 1,5% es conversión a suscriptor nuevo o promedio histórico?**
3. **¿El 2% se aplica a suscriptores nuevos, a lista total o a compradores acumulados?**
4. **¿El curso es one-time o recurring?**
5. **¿Hay churn estimado?**
6. **¿Cuál es el ticket promedio actual?**
7. **¿Qué se vende exactamente por $30?**
8. **¿Qué porcentaje de los compradores compra sin oferta, descuento o campaña?**
9. **¿El objetivo es $6.000 de revenue o $6.000 de beneficio?**
10. **¿Qué pasa en los meses 1, 2 y 3 del funnel?**

---

## 8. Mi recomendación

**No ejecutar todavía.**

El plan tiene sentido como estructura, pero está mal calibrado.

Yo lo devolvería con esta corrección:

> “El funnel de 200.000 visitas → 1,5% → 2% → $30 genera $1.800/mes, no $6.000/mes. Para aprobarlo, necesitamos llegar a 200 ventas/mes o subir el ticket promedio a $100.”

Después, aprobaría solo una de estas rutas:

### Ruta A: Ticket promedio

- 200.000 visitas
- 1,5% → 3.000 suscriptores
- 2% → 60 compradores
- AOV de $100
- **$6.000/mes**

### Ruta B: Más tráfico

- 666.667 visitas
- 1,5% → 10.000 suscriptores
- 2% → 200 compradores
- $30
- **$6.000/mes**

### Ruta C: Mejor conversión a compra

- 200.000 visitas
- 1,5% → 3.000 suscriptores
- 6,67% → 200 compradores
- $30
- **$6.000/mes**

### Ruta D: Mejor captura

- 200.000 visitas
- 5% → 10.000 suscriptores
- 2% → 200 compradores
- $30
- **$6.000/mes**

---

## Conclusión

**No, no lo aprobamos y ejecutamos como está.**

El plan no muere por ambición, muere por multiplicación.

Con sus propios números:

> **$1.800/mes, no $6.000/mes.**

Para aprobarlo, que el socio elija una palanca realista:

- subir tráfico,
- subir captura,
- subir conversión a compra,
- o, mejor aún, **subir el ticket promedio a $100**.