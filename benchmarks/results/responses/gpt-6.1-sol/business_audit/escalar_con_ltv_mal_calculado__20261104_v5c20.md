# GPT-6.1 Sol — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 16.903s | tokens_per_second: 50.8
- input_tokens: 186 | output_tokens: 858

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

**No le daría a escalar fuerte todavía.** Con tus datos, estás prácticamente en el punto de equilibrio **antes de cubrir gastos operativos**. Ser rentable hoy no significa que comprar más clientes a ese CAC sea rentable.

### Recalculando tus números

Suponiendo que el churn del 8% se mantiene constante y que no hay expansión de ingresos:

| Métrica | Cálculo | Resultado |
|---|---|---:|
| Vida media esperada | 1 ÷ 8% | **12,5 meses** |
| Ingresos por cliente durante su vida | $35 × 12,5 | **$437,50** |
| LTV de margen bruto | $35 × 70% ÷ 8% | **$306,25** |
| LTV/CAC | $306,25 ÷ $290 | **1,06×** |
| Margen de vida restante tras adquisición | $306,25 − $290 | **$16,25 por cliente** |

Tu cálculo tiene tres problemas:
- **El churn no respalda una vida media de 24 meses**, sino de 12,5.
- Para comparar con CAC, necesitas el **LTV de margen bruto**, no solo los ingresos.
- Incluso tu ratio original de 2,9 está **por debajo de 3**, no por encima.

### ¿Qué implican los $10.000?

Si el CAC se mantiene en $290, comprarías aproximadamente **34–35 clientes**. Esos clientes generarían, durante toda su vida:

- **Margen bruto esperado:** unos **$10.560**.
- **Publicidad:** $10.000.
- **Remanente:** apenas **$560**, antes de sueldos, soporte que no esté incluido en tu margen, administración y otros gastos.

Y ese margen se cobra durante meses o años; la publicidad se paga ahora. Además, **el CAC podría subir al aumentar el gasto**.

### El payback también preocupa

La cuenta simple es:

**$290 ÷ ($35 × 70%) = 11,8 meses.**

Pero eso supone que el cliente sigue pagando. **Al incorporar el churn de la cohorte, recuperarías el gasto en aproximadamente tres años**, sin descontar el valor del dinero. Hay muy poco margen para errores.

### Mi decisión

**No aprobaría los $10.000 como presupuesto de escalado con estos datos.** Sí consideraría un presupuesto limitado de experimentación, con criterios de corte.

Como referencia, para alcanzar un LTV/CAC de **3×**, manteniendo lo demás constante, necesitarías aproximadamente:

- **CAC ≤ $102**, o
- **Churn mensual ≤ 2,8%**.

Antes de escalar, validaría retención y margen por cohorte de publicidad, y mediría el CAC de los clientes adicionales, no solo el promedio histórico.

**Hoy no tienes una máquina de crecimiento demostrada: tienes una adquisición que casi consume todo el margen futuro del cliente.**