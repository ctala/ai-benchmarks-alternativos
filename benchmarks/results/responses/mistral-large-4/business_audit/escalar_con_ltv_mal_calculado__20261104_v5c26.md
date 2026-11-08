# Mistral Large 4.0 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 46.633s | tokens_per_second: 60.3
- input_tokens: 194 | output_tokens: 2814

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

No. **No metas los $10.000 todavía.** Tu aritmética tiene dos errores graves que convierten un ratio de 2,9 en uno de **~1,06**, y a esa escala te vas a quemar el capital.

Vamos a recalcular como se debe:

## 1. El error del "2 años de vida"
Con un churn del **8% mensual**, la vida promedio del cliente no es 24 meses. Es:

**Vida promedio = 1 / churn = 1 / 0,08 = 12,5 meses**

¿Por qué? Porque el churn es exponencial, no lineal. Después de 12 meses, no se ha ido el 96% de tus clientes, sino que quedan activos el 36,8% (0,92¹²). Después de 24 meses, aún queda el 13,5%.

La mediana (el cliente "típico") se va a los **~8,7 meses** (ln(2)/0,08).

## 2. El error de usar ingresos brutos en vez de margen
El LTV se calcula con el **margen bruto**, no con el precio:

**LTV = Precio × Margen × Vida promedio**
**LTV = $35 × 0,70 × 12,5 = $306,25**

(O en una sola fórmula: LTV = ($35 × 0,70) / 0,08 = $24,50 / 0,08 = **$306,25**)

## 3. Tu ratio real
**LTV / CAC = $306,25 / $290 = 1,06**

No 2,9. Estás pagando $290 para ganar $306 en toda la vida del cliente. Tu margen de seguridad es de **$16 por cliente**, antes de pagar equipo, herramientas o cualquier costo fijo.

## 4. El payback period te mata
Cuánto tardas en recuperar el CAC:
**Payback = CAC / (Precio × Margen) = $290 / $24,50 = 11,8 meses**

Necesitas que el cliente viva casi un año solo para empatar. Y la vida promedio es 12,5 meses. **Estás en el filo de la navaja**: cualquier deterioro en churn o aumento de CAC te hace perder dinero en cada cliente adquirido.

## 5. ¿Qué pasa con tus $10.000?
- Clientes adquiridos: ~34 ($10.000 / $290)
- Margen bruto total generado por ellos en toda su vida: 34 × $306 = **$10.404**
- **Retorno sobre el gasto en ads: $404 (4%)**, antes de costos fijos.

Y eso asumiendo que:
- El CAC se mantiene en $290 (al escalar 10x, suele subir por saturación de audiencia; si sube a $350, pierdes dinero en cada cliente: LTV/CAC = 0,87)
- El churn de los clientes de ads es igual al de los orgánicos (suele ser peor, porque vienen por impulso, no por necesidad)
- No hay costos de onboarding adicionales

## Qué hacer antes de quemar los $10k

1. **Baja el churn primero.** Un 8% mensual es muy alto para escalar. Si lo bajas a 4%, la vida promedio sube a 25 meses y el LTV salta a $612 (LTV/CAC = 2,1). Si lo bajas a 3%, LTV = $816 (ratio 2,8). Ahí sí tiene sentido escalar.

2. **Sube el precio o el margen.** Si subes a $45/mes, LTV = $393 (ratio 1,35). Todavía ajustado, pero mejor.

3. **Baja el CAC o mejora la conversión del funnel.** $290 es caro para un producto de $35/mes a menos que tengas una retención brutal.

4. **Test pequeño primero.** Mete $1.000-$2.000, mide el churn real de esa cohorte específica (a veces los de ads se van al mes 3), y valida que el CAC no suba cuando aumentes el presupuesto.

**Regla de oro:** para escalar agresivo con ads pagados, necesitas LTV/CAC ≥ 3 y un payback < 6 meses (idealmente < 3). Ahora tienes 1,06 y 11,8 meses.

Arregla la retención o el precio primero. La publicidad pagada solo amplifica lo que ya tienes: si tu unidad económica es débil, quemarás $10.000 en 3 meses.

¿Tienes datos de si el churn es diferente entre clientes orgánicos vs. los que vienen de ads? Eso suele ser la trampa oculta.