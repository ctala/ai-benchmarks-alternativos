# Claude Sonnet 5 (suscripción) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `claude-sonnet-5`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 44.744s | tokens_per_second: 65.6
- input_tokens: 2 | output_tokens: 2936

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

Hay dos errores en tu cálculo, y ambos van en la misma dirección: infMultiplican tu LTV real.

**Error 1: el lifetime no sale de "unos 2 años", sale del churn.**

Con churn mensual constante, la vida esperada de un cliente es 1/churn:

1 / 0.08 = **12.5 meses**, no 24.

Los 24 meses que usaste corresponden a un churn de ~4.2% mensual. Tu churn real es el doble de eso, así que tu cliente promedio dura la mitad de lo que asumiste.

**Error 2: el LTV se calcula sobre margen bruto, no sobre precio.**

El CAC es un costo. Para compararlo contra algo, ese algo tiene que ser también valor que te queda a ti — no el revenue bruto que en parte se va a infraestructura y procesador de pagos.

**Recalculando:**

```
Lifetime         = 1 / 0.08                = 12.5 meses
LTV (revenue)     = $35 × 12.5              = $437.5
LTV (margen real) = $437.5 × 0.70           = $306.25

LTV / CAC = $306.25 / $290 = 1.06
```

No 2.9. **1.06.**

Y hay un segundo número que confirma que esto no es solo aritmética fría, es un problema de caja real — el **payback period**:

```
Payback = CAC / (margen bruto mensual)
        = $290 / ($35 × 0.70)
        = $290 / $24.5
        = 11.84 meses
```

Tardas casi 12 meses en recuperar lo que te cuesta adquirir un cliente, y ese mismo cliente tiene una vida esperada de 12.5 meses. Estás recuperando el CAC casi exactamente cuando el cliente se va. No te queda margen para pagar equipo, herramientas, tu tiempo, ni para el que se va antes del promedio.

**¿Le doy a los $10K? No.**

Con LTV/CAC de 1.06 (el piso saludable en SaaS es 3:1), meter $10K en ads no es escalar, es comprar clientes a precio de pérdida a escala. Cuantos más metas, más rápido drenas caja, aunque "seas rentable" hoy con la base actual (que probablemente tiene mejor CAC blended o vino de canales orgánicos más baratos).

**Qué mover antes de gastar un dólar más en paid, en orden de apalancamiento:**

1. **Churn primero.** Es la variable que más pesa acá porque está al cuadrado en el efecto: baja el churn y el lifetime sube Y el LTV sube con él. Si bajas de 8% a 4% mensual (razonable para un SaaS con onboarding decente), el lifetime pasa a 25 meses y el LTV de margen sube a $612.5 → LTV/CAC = 2.1. Todavía no es 3, pero ya no estás quemando plata.
2. **CAC.** ¿$290 es el blended de todos los canales o el de paid puro? Si metes $10K en un canal nuevo sin historial, tu CAC real de ese canal puede ser peor que $290, no igual.
3. **Precio o margen**, si churn y CAC no dan para llegar a 3x.

Corre el mismo cálculo (lifetime = 1/churn, LTV = precio × margen × lifetime) con el churn en 5% y en 3% para ver a partir de dónde el ratio te da luz verde real. Con los números de hoy, meter $10K es financiar la salida de un cliente, no la entrada.