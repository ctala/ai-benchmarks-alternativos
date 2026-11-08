# Kimi K3.1 Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 7.73 | quality: 10.0
- latency_total: 275.489s | tokens_per_second: 27.0
- input_tokens: 315 | output_tokens: 7434

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

**No aprobaría los $10.000 para escalar con estos números.** Como mucho, haría una prueba pequeña para validar el canal. Hay dos errores en el cálculo:

### 1. Ocho por ciento de churn no implica dos años de vida media

Con churn mensual constante:

\[
\text{Vida media}=\frac{1}{0.08}=12,5\text{ meses}
\]

Para una vida media de 24 meses, el churn tendría que ser aproximadamente **4,2% mensual**. Además, con 8% de churn, solo quedaría alrededor de **13,5% de la cohorte después de 24 meses**.

### 2. El LTV debe compararse con CAC usando margen, no solo facturación

| Métrica | Cálculo | Resultado |
|---|---:|---:|
| LTV de ingresos | $35 × 12,5 | **$437,50** |
| LTV de margen bruto | $437,50 × 70% | **$306,25** |
| LTV/CAC correcto | $306,25 / $290 | **1,06x** |

Es decir, después de recuperar el CAC, quedan aproximadamente **$16,25 por cliente durante toda su vida**, antes de gastos fijos, costos no incluidos en ese margen y cualquier descuento financiero.

El CAC máximo de equilibrio sería **$306,25**. Estás a solo **5,6%** de ese límite: cualquier empeoramiento moderado del CAC vuelve negativa la adquisición.

### Qué significa para los $10.000

- Clientes esperados: \(10.000/290 \approx 34,5\).
- Margen bruto de por vida esperado: aproximadamente **$10.560**.
- Excedente después de recuperar la pauta: apenas **$560**, repartido durante años y antes de otros costos.

El payback simple sería:

\[
\frac{290}{35 \times 70\%}=11,8\text{ meses}
\]

Pero ese cálculo supone que todos siguen pagando. Incorporando el churn, la cohorte recuperaría el CAC aproximadamente **cerca de tres años después**; a los 24 meses todavía habría generado solo unos **$265 de margen acumulado por cliente adquirido**, menos que los $290 de CAC.

### Qué tendría que cambiar

Si quieres usar **3x** como vara de referencia, manteniendo todo lo demás constante necesitarías, por ejemplo:

- **CAC ≤ $102**, o
- **Churn ≤ 2,8% mensual** con el CAC actual —vida media de unos 35,5 meses—, o
- Una combinación de mejoras en precio, retención, margen y CAC.

**Veredicto:** tu negocio actual puede ser rentable, pero esta adquisición pagada no tiene margen suficiente para escalar fuerte. No soltaría los $10.000 hasta mejorar la ecuación o validar con cohortes de pago que el CAC y el churn reales son sustancialmente mejores.