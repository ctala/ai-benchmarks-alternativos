# Nemotron 3 Super — business_audit/escalar_con_ltv_mal_calculado

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 55.378s | tokens_per_second: 44.9
- input_tokens: 223 | output_tokens: 2487

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

**No le doy.** Con esos números, meter $10.000 en publicidad es quemar efectivo, no invertirlo.

El fundador está calculando el LTV como si fuera un negocio de suscripción sin churn y sin costos. Eso es aritmética de cuento de hadas. Aquí está la recalculación real.

---

### 1. Los tres errores del cálculo del fundador

| Error | Lo que hizo el fundador | Lo correcto |
|-------|------------------------|-------------|
| **Ingreso vs. margen** | Usó los $35 de precio completo. | Debe usar el margen bruto: $35 × 70% = **$24,50** por mes. El resto se lo queda la infraestructura y el procesador. |
| **Ignoró el churn** | Asumió que todos los clientes pagan 24 meses. | Con un churn del 8% mensual, la vida esperada es **1 / 0,08 = 12,5 meses**, no 24. |
| **LTV bruto** | LTV = $840. | LTV de contribución = Margen mensual × Vida esperada. |

---

### 2. La aritmética real

**Margen mensual por cliente:**  
$35 × 70% = **$24,50**

**Vida esperada del cliente (con churn 8%):**  
1 ÷ 0,08 = **12,5 meses**

**LTV real (contribución):**  
$24,50 × 12,5 = **$306,25**

**LTV / CAC real:**  
$306,25 ÷ $290 = **1,06**

**Período de recuperación (payback):**  
$290 ÷ $24,50 = **~11,8 meses**

Para ser generoso, incluso si limitamos el cálculo a exactamente 24 meses (ignorando que la mayoría se irá antes), el LTV acumulado a 2 años es solo de unos **$265**, aún por debajo del CAC de $290.

**Resultado:** Cada cliente que adquiera con publicidad pierde dinero en unidad. No gana $550 por cliente (como sugiere su LTV/CAC de 2,9); pierde aproximadamente **$16,25** por cliente, y tarda casi un año en recuperar lo que gastó en adquirirlo.

---

### 3. Qué significa gastar $10.000 este mes

- Clientes adquiridos: $10.000 ÷ $290 ≈ **34 clientes**.
- Margen bruto mensual generado por esos 34 clientes: 34 × $24,50 ≈ **$833/mes**.
- Tiempo para recuperar los $10.000 solo con el margen de esos clientes: **~12 meses**.

Y eso asume que:
- El CAC no sube al escalar (lo cual suele subir por saturación de audiencia).
- El churn no empeora con clientes de menor calidad traídos por ads.
- No hay costos de atención, soporte o éxito del cliente.

---

### 4. Qué tendría que cambiar para que sí le dé

Para llegar a un LTV/CAC sano de 3 con un CAC de $290, necesitaría un LTV de contribución de al menos **$870**. Con un margen de $24,50/mes, eso implica una vida esperada de **35,5 meses**, es decir, un churn mensual de alrededor del **2,8%**.

Alternativamente, manteniendo el churn del 8%, necesitaría:
- Bajar el CAC a menos de **$100**, o
- Subir el precio/margen mensual a más de **$92**, o
- Reducir el churn a menos del **3% mensual**.

---

### Veredicto

**No apruebo el plan.** Con un LTV/CAC de ~1,06 y un payback de casi 12 meses, escalar con publicidad pagada acelera la quema de caja, no el crecimiento rentable.

Primero arregle el embalse: baje el churn, suba el precio o baje el CAC. Cuando el LTV de contribución sea al menos 3 veces el CAC y el payback sea inferior a 6-9 meses, entonces hablemos de meter los $10.000.