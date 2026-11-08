# Qwen 3.8 Max 0902 — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.89 | quality: 10.0
- latency_total: 256.637s | tokens_per_second: 45.9
- input_tokens: 256 | output_tokens: 11769

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

**No. No lo aprueben ni lo ejecuten así.**  
Los porcentajes pueden sonar “sanos”, pero la multiplicación no llega al objetivo.

## 1) La matemática del plan

Plan propuesto:

- Visitas/mes: **200.000**
- Conversión visita → suscriptor: **1,5%**
- Conversión suscriptor → compra: **2%**
- Precio del curso: **$30**

Cálculo:

| Paso | Cálculo | Resultado |
|---|---:|---:|
| Suscriptores/mes | 200.000 × 1,5% | **3.000** |
| Compras/mes | 3.000 × 2% | **60** |
| Ingresos/mes | 60 × $30 | **$1.800/mes** |

Objetivo: **$6.000/mes**  
Resultado del plan: **$1.800/mes**  
Cobertura del objetivo: **30%**  
Faltante: **$4.200/mes**  
Necesitan multiplicar el resultado por **3,33x**.

**Conclusión rápida:** el plan no llega ni cerca si el curso es un pago único de $30.

---

## 2) El error conceptual: “curso de $30” no es igual a “ingreso recurrente”

Dicen:

> “Con eso llegamos cómodos a los $6.000/mes recurrentes.”

Pero si el curso cuesta **$30** y se paga una sola vez, no hay ingreso recurrente. Hay ventas mensuales nuevas.

Con tráfico constante, cada mes entrarían aproximadamente:

**3.000 suscriptores × 2% × $30 = $1.800**

No importa que la lista se acumule si el curso se vende una sola vez. La lista acumulada puede ayudar a lanzamientos futuros, pero no convierte automáticamente esas ventas en ingresos recurrentes.

### Si piensan en la lista acumulada a 6 meses

Suponiendo que capturan 3.000 suscriptores por mes durante 6 meses:

- Suscriptores acumulados: **18.000**
- Compras totales al 2%: **360**
- Facturación total: **360 × $30 = $10.800**

Eso sería **$10.800 en 6 meses**, no $6.000/mes.

Promediado:

**$10.800 / 6 = $1.800/mes**

Sigue sin llegar.

---

## 3) ¿Cuándo sí podría funcionar?

Solo si el producto de $30 es una **suscripción mensual**, no un curso de pago único.

Si fuera una membresía de **$30/mes**, cada mes necesitarían sumar clientes activos. Con los números actuales:

- Nuevos suscriptores/mes: 3.000
- Nuevos clientes pagos/mes: 3.000 × 2% = **60**
- Nuevo MRR mensual: 60 × $30 = **$1.800**

Sin churn, la proyección sería:

| Mes | Nuevos clientes | Clientes activos | MRR |
|---|---:|---:|---:|
| 1 | 60 | 60 | $1.800 |
| 2 | 60 | 120 | $3.600 |
| 3 | 60 | 180 | $5.400 |
| 4 | 60 | 240 | $7.200 |
| 5 | 60 | 300 | $9.000 |
| 6 | 60 | 360 | $10.800 |

En ese escenario, sí superarían los $6.000/mes alrededor del mes 4.

Pero para aprobar eso necesitan aclarar:

1. El producto es **$30/mes**, no un curso de pago único.
2. El churn mensual no es alto.
3. La cobranza funciona bien.
4. No están contando la misma venta varias veces.
5. El 2% de conversión a suscripción es realista y validado.

Con churn mensual, el escenario cambia. Por ejemplo, si el churn fuera 25%, hacia el mes 6 se quedarían cerca de los $6.000/mes. Así que “recurrente” no significa automático.

---

## 4) Qué tendría que cambiar si el curso sigue siendo pago único

Para llegar a **$6.000/mes** con un producto de **$30**, necesitan:

**$6.000 / $30 = 200 ventas/mes**

Hoy el plan produce:

**60 ventas/mes**

Faltan **140 ventas/mes**.

Para cerrar la brecha manteniendo el precio de $30, necesitan una de estas opciones:

### Opción A: Más tráfico

Con 1,5% de captura y 2% de compra:

- Suscriptores necesarios: **10.000/mes**
- Visitas necesarias: **666.667/mes**

Es decir, necesitan **3,33 veces más tráfico**.

### Opción B: Mejor captura

Manteniendo 200.000 visitas y 2% de compra:

- Suscriptores necesarios: **10.000/mes**
- Tasa de captura necesaria: **5%**

Eso es más del triple del 1,5% propuesto.

### Opción C: Mejor conversión de venta

Manteniendo 200.000 visitas y 1,5% de captura:

- Suscriptores/mes: 3.000
- Ventas necesarias: 200
- Tasa de compra necesaria: **6,67%**

Eso es más del triple del 2% propuesto.

### Opción D: Subir precio o ticket promedio

Manteniendo 60 ventas/mes:

- Precio necesario: **$100**

O sea, curso más caro, bundle, upsell, order bump, consultoría, comunidad, plantilla premium, etc.

### Opción E: Combinación

La conversión combinada actual es:

**1,5% × 2% = 0,03%** de visita → venta.

Para llegar a $6.000 con 200.000 visitas y precio de $30, necesitan:

**0,10%** de visita → venta.

Ejemplos combinados:

| Captura | Venta | Resultado |
|---:|---:|---:|
| 5% | 2% | Llega |
| 3% | 3,33% | Llega |
| 2,5% | 4% | Llega |
| 1,5% | 6,67% | Llega |
| 2% | 5% | Llega |

---

## 5) Lo que no deberíamos aceptar como “conservador” sin evidencia

Decir “1,5% es conservador” y “2% es conservador” puede ser razonable en algunos contextos, pero no podemos aprobarlo sin datos.

Necesitan validar:

1. **¿De dónde vienen las 200.000 visitas?**  
   No vale lo mismo tráfico orgánico intencional que tráfico frío de redes sociales.

2. **¿Dónde se pondrá el formulario?**  
   No convierte igual un popup, una landing dedicada, un contenido gated, una salida de blog o una home.

3. **¿Hay una secuencia de emails?**  
   Un 2% de compra puede requerir nurturing, lanzamiento, prueba social, urgencia, etc.

4. **¿El producto es pago único o suscripción?**  
   Cambia completamente el modelo.

5. **¿Cuál es el costo de adquisición?**  
   Si el tráfico es pagado, con estos números el ingreso por visita es muy bajo.

Con el funnel actual:

- Ingreso por visita: **$0,009**
- Ingreso por suscriptor: **$0,60**

Si están pagando más de $0,009 por visita para un producto de pago único, pierden dinero antes de costos.

Para llegar a $6.000 con 200.000 visitas, necesitan:

**$6.000 / 200.000 = $0,03 por visita**

Es decir, triplicar el ingreso por visita.

---

## 6) Mi recomendación ejecutiva

**No ejecutar el plan completo todavía.**

Lo que haría:

### Paso 1: Corregir la matemática

Devolverle el plan a tu socio con esta pregunta:

> “¿Cómo cerramos la brecha de 3,33x?”

Las respuestas válidas son:

- Subir tráfico a ~667.000 visitas/mes.
- Subir captura a ~5%.
- Subir conversión de venta a ~6,7%.
- Subir ticket promedio a ~$100.
- Convertirlo en suscripción de $30/mes con churn controlado.
- Una combinación realista de las anteriores.

### Paso 2: Hacer un piloto de 30 días

No ejecuten todo el plan. Prueben una parte.

Por ejemplo:

- Llevar 20.000 o 50.000 visitas a una landing.
- Medir conversión real a suscriptor.
- Enviar secuencia de venta.
- Medir conversión real a compra.
- Calcular ingreso por visita, ingreso por suscriptor y CAC.

Si el piloto confirma:

- Captura ≥ 1,5%
- Compra ≥ 2%
- Producto recurrente o ticket suficiente
- CAC compatible con margen

entonces sí pueden escalar.

### Paso 3: Aprobar solo si el modelo llega por sí mismo

No aprueben un plan que depende de esperanza. Aprueben un plan que llegue con números.

---

## 7) Respuesta corta para tu socio

> “Los porcentajes podrán ser razonables, pero la cuenta no da: 200.000 visitas × 1,5% × 2% × $30 = $1.800/mes. Para llegar a $6.000/mes necesitamos 3,33 veces más tráfico, o 5% de captura, o 6,7% de conversión de venta, o un ticket promedio de $100, o convertirlo en una suscripción real de $30/mes. No lo ejecutemos hasta corregir esa brecha y validar el funnel con un piloto.”

**Veredicto final: no aprobar tal como está.**