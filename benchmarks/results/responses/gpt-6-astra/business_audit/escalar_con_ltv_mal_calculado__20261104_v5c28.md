# GPT-6 Astra — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-6-astra`
- success: True  | final: 8.03 | quality: 10.0
- latency_total: 17.574s | tokens_per_second: 36.9
- input_tokens: 186 | output_tokens: 648

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

**No le daría a los $10.000 todavía.** Con los números que das, la adquisición pagada apenas recupera su costo antes de gastos operativos. Tu cálculo sobreestima el LTV.

### Recalculando

Suponiendo churn constante, sin expansión de ingresos y CAC estable:

| Métrica | Cálculo | Resultado |
|---|---|---:|
| Vida media esperada | 1 ÷ 8% | **12,5 meses**, no 24 |
| Margen bruto mensual por cliente | $35 × 70% | **$24,50** |
| LTV sobre margen bruto | $24,50 ÷ 8% | **$306,25** |
| LTV/CAC | $306,25 ÷ $290 | **1,06×** |
| Recuperación simple del CAC | $290 ÷ $24,50 | **11,8 meses**, sin considerar churn |

Además, $840 ÷ $290 = **2,90×**, que está **por debajo** de 3, no por encima. Pero el problema principal es asumir 24 meses y comparar ingresos con el costo de adquisición sin descontar el costo de servir al cliente.

### ¿Qué implican los $10.000?

Si el CAC se mantiene en $290:

- Adquirirías unos **34,5 clientes**.
- Generarían aproximadamente **$10.560 de margen bruto durante toda su vida**.
- Después de publicidad, quedarían apenas **$560**, antes de sueldos, soporte no incluido en el margen, herramientas, administración y costo del capital.

**Eso no son $560 de beneficio neto ni de caja este mes.** Es el excedente esperado de toda la cohorte durante su vida.

Y los 11,8 meses de recuperación simple son engañosos para la cohorte: algunos clientes se irán antes. Incorporando el churn, el margen bruto acumulado esperado por cliente adquirido tras \(n\) meses es:

\[
306,25 \times (1 - 0,92^n)
\]

Para recuperar $290 necesitas aproximadamente **36 meses**, bajo estos supuestos. Es decir: adelantas caja hoy para recuperarla muy lentamente y con muy poco colchón.

### ¿Qué tendría que mejorar?

Si tomamos **3× como referencia orientativa**, no como garantía de viabilidad, necesitarías una de estas mejoras, manteniendo lo demás constante:

- **CAC ≤ $102**, frente a $290.
- **Churn mensual ≤ 2,8%**, frente a 8%.
- **Precio ≈ $99/mes**, si el margen porcentual, churn y CAC no cambian.

También puede servir una combinación de mejoras.

**Mi recomendación:** no escales fuerte todavía. Usa un presupuesto de prueba limitado por tu caja para validar CAC y retención de las cohortes pagadas, y trabaja en mejorar estas variables antes de aumentar inversión. Ser rentable hoy no demuestra que el próximo cliente comprado sea suficientemente rentable; con tus cifras actuales, prácticamente todo su margen de vida se lo lleva la publicidad.