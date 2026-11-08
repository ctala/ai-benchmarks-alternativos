# MiMo V2.6 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 33.883s | tokens_per_second: 52.7
- input_tokens: 227 | output_tokens: 1785

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

# ❌ No. Tu aritmética tiene dos errores graves.

---

## Error 1: Vida del cliente mal calculada

Con un churn mensual del 8%:

$$\text{Vida promedio} = \frac{1}{0.08} = 12{,}5 \text{ meses}$$

**No 24 meses.** Un cliente se queda ~1 año y 1 mes, no 2 años.

## Error 2: No aplicaste el margen bruto

El LTV no es lo que el cliente *paga*, es lo que te *deja*. Con 70% de margen:

$$\text{LTV real} = 35 \times 0{,}70 \times 12{,}5 = \boxed{\$306}$$

---

## Tu número real vs. tu número

| | Tu cálculo | Real |
|---|---|---|
| Vida del cliente | 24 meses | **12,5 meses** |
| LTV | $840 | **$306** |
| **LTV/CAC** | **2,9** | **1,06** |

---

## Lo que realmente pasa si gastas $10.000

- **Clientes adquiridos:** $10.000 / $290 = **~35 clientes**
- **Margen bruto que generan en vida:** 35 × $306 = **$10.706**
- **Beneficio neto de la inversión:** $706 sobre 12,5 meses

**Prácticamente 0%.** Vas a inmoviliar $10.000 durante más de un año para recuperar $10.706.

---

## El periodo de recuperación (payback) lo confirma

$$\text{Payback} = \frac{CAC}{\text{Margen bruto/mes}} = \frac{290}{35 \times 0{,}70} = \frac{290}{24{,}50} = \textbf{11,8 meses}$$

Recuperas cada cliente **al final de su vida útil**. Si churn sube un punto al 9%:

$$\text{LTV} = 35 \times 0{,}70 \times 11{,}1 = \$272$$
$$\text{LTV/CAC} = \textbf{0{,}94} \quad ← \text{estás regalando clientes}$$

---

## Lo que necesitas antes de gastar un solo dólar en ads

| Variable | Actual | Necesario para LTV/CAC ≥ 3 |
|---|---|---|
| CAC | $290 | **≤ $102** |
| Churn mensual | 8% | **≤ 3,5%** |
| Precio | $35 | **$88+** |
| Margen bruto | 70% | ~el mismo |

**Al menos dos de estas cuatro.** Puedes combinar (churn del 5% + precio $55 da LTV = $770, con CAC $250 → ratio 3,08 ✅).

---

## Veredicto

> **No apruebo $10.000 en publicidad.** Estás a un punto de churn de distancia de perder dinero con cada campaña. Primero reduce churn a <5% y ajusta el precio. Recién después escala.

Tu plan "escalaba fuerte" directo al abismo con aritmética optimista.