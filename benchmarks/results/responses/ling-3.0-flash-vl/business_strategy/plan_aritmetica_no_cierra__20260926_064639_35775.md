# Ling 3.0 Flash VL — business_strategy/plan_aritmetica_no_cierra

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 13.078s | tokens_per_second: 144.7
- input_tokens: 253 | output_tokens: 1893

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

## 🚫 No. No le damos. El plan no cuadra.

Tu instinto de "la mayoría de los planes mueren en la multiplicación" se cumple aquí, pero no por la incertidumbre — sino porque **la matemática directa no llega al objetivo**. Veamos:

---

### La cadena multiplicativa real

| Paso | Dato | Resultado acumulado |
|------|------|---------------------|
| Visitas mensuales | 200,000 | 200,000 |
| × Conversión a suscriptor (1,5%) | × 0,015 | **3,000 suscriptores** |
| × Tasa de compra (2%) | × 0,02 | **60 compradores** |
| × Precio del curso ($30) | × $30 | **$1,800/mes** |

### $1,800 ≠ $6,000

**Falta un factor de 3,33x.** El plan dice "cómodamente a $6,000" pero la operación básica da exactamente un tercio de eso.

---

### Donde puede morir el plan (además del cálculo)

1. **La multiplicación encadenada amplifica cualquier error.** Si el 1,5% baja al 1% y el 2% baja al 1,5%, terminas con:
   - 200,000 × 0,01 × 0,015 × $30 = **$900/mes**. Un desastre de 7 veces menor al objetivo.

2. **Los porcentajes "conservadores" no lo son tanto.** Un 1,5% de conversión de visita a suscriptor en un sitio sin contexto de urgencia o valor demostrado es **agresivo** para la mayoría de sectores. Un 2% de compra en una lista fría (sin calentamiento previo) también. Estás asumiendo que todo funciona bien en el mejor escenario conservador, pero en la práctica los dos bajan juntos.

3. **"$6.000 recurrentes" es un error conceptual.** Vender un curso de $30 una vez no genera ingresos recurrentes. ¿Hay upsell? ¿Suscripción? ¿Recompra? Si no hay un mecanismo de retención, eso es $1.800 **no recurrentes** que se evaporan al mes siguiente.

---

### Lo que sí funciona (el plan corregido)

Para llegar a $6.000/mes con las 200,000 visitas, necesitas cambiar **al menos una variable significativa**:

| Opción | Qué cambiar | Nuevo valor |
|--------|------------|-------------|
| **A** | Subir precio del curso | De $30 a **$100** (60 × $100 = $6.000) |
| **B** | Subir tasa de compra | De 2% a **6,7%** (3.000 × 6,7% × $30 = $6.000) |
| **C** | Subir conversión a suscriptor | De 1,5% a **4,5%** (9.000 × 2% × $30 = $5.400... cerca pero no basta) |
| **D** | Combinar ajustes | Precio $50 + tasa de compra 4% = $6.000 |
| **E** | Agregar modelo recurrente | Curso + suscripción/membresía |

---

### Mi recomendación

**No ejecutes el plan tal como está.** Pero no lo rechaces: está a un ajuste de distancia. Haz esto antes de aprobar:

1. **Valida la conversión real con datos**, no con estimaciones. Lanza el formulario esta semana y mide.
2. **Valida la tasa de compra real.** Un 2% en lista fría es una hipótesis, no un hecho.
3. **Define el modelo de recurrencia** o cambia el objetivo a $1.800/mes (que sigue siendo un negocio interesante, pero honesto).

> **La regla de oro:** Si al multiplicar tres o más números estimados no llegas al objetivo, el plan no es conservador — es incorrecto. Corregí la matemática antes de comprometer recursos.