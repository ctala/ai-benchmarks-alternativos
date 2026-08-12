# DeepSeek V4 Flash 0731 — business_strategy/plan_aritmetica_no_cierra

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.74 | quality: 10.0
- latency_total: 94.532s | tokens_per_second: 24.2
- input_tokens: 208 | output_tokens: 2288

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

**Veredicto: NO aprobamos este plan. La matemática no cuadra, y los supuestos esconden errores graves de lógica comercial.**

Hagamos la multiplicación que tu socio omitió:

- **Suscriptores:** 200.000 visitas × 1,5% = **3.000 suscriptores/mes**.
- **Compradores:** 3.000 suscriptores × 2% = **60 compradores/mes**.
- **Ingresos:** 60 compradores × $30 = **$1.800 USD/mes**.

**Estás a $4.200 USD de la meta.** El plan solo cubre el 30% del objetivo. Si lo ejecutamos tal cual, fracasaremos estrepitosamente frente a la meta de $6.000.

---

### Análisis crítico de los supuestos (más allá de la aritmética):

1. **El 2% de conversión a compra NO es conservador, es optimista.**  
   Para una lista recién capturada (sin historial de engagement), una tasa de conversión del 0,5% - 1% a un producto de $30 es lo realista. El 2% suele lograrse con listas calientes, secuencias de emails maduras y ofertas de alto valor percibido. Si usamos un 1% realista, los ingresos caen a **$900/mes**.

2. **El concepto de "recurrente" está mal aplicado.**  
   Un curso de $30 es un producto de compra única, no una suscripción. Para tener $6.000/mes *recurrentes*, necesitas vender $6.000 en *nuevos* clientes cada mes (porque los anteriores no vuelven a pagar). Con tu ticket promedio, eso implicaría **200 ventas mensuales**, no 60.

3. **El tráfico de 200.000 visitas es una trampa si no es calificado.**  
   ¿Es tráfico orgánico, de pago o viral? Si es de pago, el CAC (Costo de Adquisición por Cliente) puede comerse el margen. Si es tráfico frío (blog genérico), la conversión a suscriptor del 1,5% podría caer al 0,5%.

---

### Plan de corrección (antes de ejecutar):

Tienes 3 palancas para llegar a $6.000/mes. Debes ajustar al menos una:

| Palanca | Valor actual | Valor necesario para $6.000/mes |
| :--- | :--- | :--- |
| **Ticket promedio** | $30 | **$100** (si mantienes 60 ventas/mes) |
| **Volumen de ventas** | 60/mes | **200 ventas/mes** (si mantienes $30) |
| **Conversión a compra** | 2% | **6,6%** (extremadamente difícil en frío) |

**Mi recomendación como analista:**

1. **Rehacer el plan con el ticket correcto:** Si el curso cuesta $30, necesitas vender 200 unidades/mes. Eso implica que el 2% de conversión debe ser sobre **10.000 suscriptores/mes**, lo que requiere **666.666 visitas/mes** al 1,5%. ¿Tienes ese tráfico?
2. **Revisar la oferta:** Si el objetivo son $6.000/mes, considera subir el precio a $99 o $149 (justifica el valor con contenido premium). Con 60 ventas a $100, llegas a $6.000.
3. **Implementar un embudo de recurrencia:** En lugar de un curso único, crea una membresía mensual de $30. Necesitarías 200 miembros activos. Eso es más sostenible.

---

### Conclusión:

Devuélvele el plan a tu socio con esta nota: *"La aritmética nos da $1.800/mes, no $6.000. Necesitamos ajustar el ticket o el tráfico antes de gastar un dólar en implementación."*  

**No ejecutamos hasta que los números cierren.** La ejecución de un plan con matemática rota solo quema recursos y credibilidad. ¿Quieres que te ayude a rediseñar el embudo con números realistas?