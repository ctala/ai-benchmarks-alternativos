# Grok 4.20 Multi-Agent — business_audit/escalar_con_ltv_mal_calculado

- model_id: `x-ai/grok-4.20-multi-agent`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 40.777s | tokens_per_second: 163.9
- input_tokens: 16440 | output_tokens: 6685

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

**No. No le des.**

Tu aritmética tiene un error crítico que cambia completamente el diagnóstico.

### Cálculo correcto

- **Churn mensual**: 8% → Lifetime promedio = **1 / 0.08 = 12.5 meses** (no 24 meses).
- ARPU = $35
- Margen bruto = 70% → Contribución mensual por cliente = **35 × 0.7 = $24.5**
- **LTV** = 24.5 / 0.08 = **$306.25**
- **CAC** = $290
- **LTV/CAC** = 306 / 290 ≈ **1.06x**

Esto no es "casi 3x". Es prácticamente 1x. Estás recuperando el costo de adquisición casi al mismo tiempo que el cliente promedio se va.

### Payback period (el número que realmente importa aquí)
**290 / 24.5 ≈ 11.8 meses**

Estás tardando casi 12 meses en recuperar el CAC, mientras que el cliente dura 12.5 meses en promedio. Esto es extremadamente riesgoso. Cualquier pequeño aumento en churn, retraso en cobro o costo adicional (soporte, equipo, etc.) te pone en negativo.

### Con los $10.000 que quieres meter
- Clientes nuevos ≈ 34–35
- Contribución total esperada a lo largo de la vida de esos clientes ≈ **$10.700**
- Ganancia bruta después de CAC ≈ **$700** (antes de cualquier otro costo operativo)

No estás escalando. Estás haciendo un ejercicio de casi break-even con mucho riesgo de cash flow negativo en los primeros 6-9 meses.

### Diagnóstico claro
Tienes un negocio que **puede ser rentable con adquisición orgánica o de muy bajo costo**, pero **no es invertible a escala con paid ads** a estos números.

El problema principal es el **8% de churn mensual**. Es brutal (equivalente a ~63-65% anual). La mayoría de SaaS que escalan con paid ads tienen churn mensual entre 1.5% y 4% máximo.

### Qué deberías hacer antes de tocar paid ads fuerte:

1. **Bajar el churn drásticamente** (esta es la palanca más importante ahora). Apunta a bajar de 8% a <4% antes de escalar. Analiza por qué se van (onboarding, producto, segmentos, pricing, etc.).
2. Subir precio (muchos negocios en $35 pueden ir a $49–$59 sin perder mucho volumen).
3. Mejorar CAC (crear un engine orgánico/sem orgánico más fuerte antes de quemar tanto dinero en ads).
4. Una vez que tengas LTV/CAC >3x **y** payback <5–6 meses, recién ahí puedes escalar paid agresivamente.

¿Quieres que hagamos juntos el ejercicio de sensibilidad? Puedo mostrarte qué churn o qué precio necesitarías para que los números cierren decentemente (LTV/CAC >3 y payback <5 meses).

¿Me das más contexto (MRR actual, cómo estás adquiriendo clientes hoy, o si el 8% es churn de clientes o revenue churn)?