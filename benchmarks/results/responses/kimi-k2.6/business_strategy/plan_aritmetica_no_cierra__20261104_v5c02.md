# Kimi K2.6 — business_strategy/plan_aritmetica_no_cierra

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 30.323s | tokens_per_second: 77.2
- input_tokens: 237 | output_tokens: 2342

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

 **No se aprueba.** 

El plan muere en la multiplicación. Con esos porcentajes y ese precio no llegan a $6.000; llegan a **$1.800 mensuales**. Están un 70% por debajo del objetivo.

Aquí la cuenta que su socio no hizo:

| Variable | Cálculo | Resultado |
|---|---|---|
| Tráfico | 200.000 visitas | 200.000 |
| Suscriptores | × 1,5 % | **3.000 leads/mes** |
| Compradores | × 2 % | **60 ventas/mes** |
| Ingreso | × $30 | **$1.800/mes** |

**Brecha:** $4.200 mensuales menos de lo prometido.

---

### Para llegar a $6.000/mes, alguna de estas variables debe cambiar drásticamente:

| Opción | Qué tendrían que mover | Nuevo valor |
|---|---|---|
| **A** | Precio del curso | **$100** (en vez de $30) |
| **B** | Conversión a suscriptor | **5,0 %** (en vez de 1,5 %) |
| **C** | Conversión a compra | **6,7 %** (en vez de 2 %) |
| **D** | Tráfico mensual | **~670.000 visitas** (en vez de 200.000) |
| **E** | Mix | Subir precio a $60 + conversión a compra al 5 % |

¿Son esos números “conservadores”? No. Son **incompatibles** con el objetivo si no se mueve nada más.

---

### Además: ¿de dónde sale lo “recurrente”?

Venden un **curso de $30**. Si es un producto de un solo pago, esos $1.800 no son recurrentes; son ingresos nuevos. Para que sea recurrente necesitan:
- Que el curso sea una **suscripción mensual** (y que pocos se den de baja), o
- Un **backend** de ventas sucesivas (upsell, membresía, etc.) que el plan no menciona.

---

**Dictamen:** Vuelvan a la hoja de cálculo. El plan actual no es conservador; es **insuficiente**. Ajusten las variables hasta que la multiplicación dé $6.000 (o más, para cubrir churn y devoluciones) y ahí lo conversamos.