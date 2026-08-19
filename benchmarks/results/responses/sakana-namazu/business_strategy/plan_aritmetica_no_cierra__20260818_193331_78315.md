# Sakana Namazu — business_strategy/plan_aritmetica_no_cierra

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.38 | quality: 10.0
- latency_total: 32.932s | tokens_per_second: 95.7
- input_tokens: 237 | output_tokens: 3153

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

**No. No se aprueba.** 

No porque los porcentajes sean descabellados, sino porque **la multiplicación del plan no llega al objetivo**. La mayoría de los planes mueren exactamente aquí: en la aritmética.

---

### 🧮 Tu matemática vs. tu meta

Vamos línea por línea:

| Paso | Cálculo | Resultado |
|------|---------|-----------|
| Tráfico actual | 200.000 visitas/mes | 200.000 |
| Conversión a email (1,5 %) | 200.000 × 0,015 | **3.000 suscriptores/mes** |
| Conversión a compra (2 %) | 3.000 × 0,02 | **60 compras/mes** |
| Ingreso mensual (curso $30) | 60 × $30 | **$1.800/mes** |

**Estás $4.200 abajo de tu meta.** El plan genera menos del 30 % de lo que promete.

Ni siquiera es cerca. Es un déficit del **70 %**.

---

### 🚨 Dos problemas conceptuales graves

**1. Esto no es "recurrente"**
Un curso de $30 de pago único no te da $6.000/mes recurrentes. Te da $1.800 **una sola vez** por esa oleada de nuevos suscriptores. El mes siguiente necesitas *otras* 60 ventas nuevas para volver a facturar $1.800. Si no hay tráfico nuevo o no hay más productos que vender a la lista existente, tus ingresos tienden a cero, no se repiten solos.

**2. Estás asumiendo independencia lineal**
Una conversión de compra del 2 % sobre una lista fresca de captación no se sostiene mes a mes sobre los mismos nombres. Esa tasa aplica a *nuevos* suscriptores calientes, no a toda tu base acumulada.

---

### ¿Qué necesitarías REALMENTE para llegar a $6.000?

Si mantienes todo "conservador y realista", necesitas **3,3 veces más volumen** en alguna parte de la tubería. Algunas combinaciones:

- **Opción A (tráfico):** 666.667 visitas/mes con tus mismos 1,5 % y 2 %.
- **Opción B (opt-in):** 5 % de conversión a email (subiría a 10.000 suscriptores/mes) manteniendo el resto.
- **Opción C (precio):** Subir el curso a **$100** y mantener el 2 % de conversión (que a $100 es mucho más difícil que a $30).
- **Opción D (ventas):** Mantener todo igual pero convertir a **6,7 %** de tu lista (más de 3x tu estimación "conservadora").
- **Opción E (modelo):** Convertir esto en una membresía/suscripción de ~$30/mes y lograr 200 miembros (pero eso es otro producto y otra conversión).

Ninguna de esas opciones se describe en el plan. Por tanto, **el plan no es un plan, es un deseo con porcentajes**.

---

### 🎯 Antes de aprobar cualquier versión 2, responde con datos duros:

1. ¿El tráfico de 200.000 es *actual y sostenido* o es una proyección a 6 meses?
2. ¿Ya has medido el 1,5 % de opt-in con ese formulario específico en ese sitio específico, o es un benchmark de Google?
3. ¿Ya has vendido el curso a $30? ¿A cuántas personas? ¿Cuál fue la tasa de conversión real sobre leads calientes?
4. Si es un curso one-time, ¿cuál es el siguiente producto para monetizar la lista mes a mes y buscar recurrencia real (LTV)?
5. ¿Cuál es el **LTV (Lifetime Value)** actual de un cliente? Si es $30, necesitas 200 clientes/mes. Si logras que cada cliente pague $90 en promedio (upsells, más cursos), necesitas 67 clientes/mes.

---

**Veredicto como analista:** Rechazado por trayectoria insuficiente. No ejecutes hasta que la hoja de cálculo cierre **$6.000 reales** a partir de datos actuales, no de estimaciones "conservadoras" sin benchmark propio.

Si quieres, trae esos números verdaderos y armamos un plan que sí cierre.