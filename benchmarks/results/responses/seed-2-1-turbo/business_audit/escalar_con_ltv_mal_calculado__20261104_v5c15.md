# Seed 2.1 Turbo — business_audit/escalar_con_ltv_mal_calculado

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 85.842s | tokens_per_second: 68.1
- input_tokens: 249 | output_tokens: 5843

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

### Respuesta directa: No le das ni de cerca. Tu cálculo tiene dos errores gravísimos que hacen que tu LTV/CAC real sea 6 veces menor de lo que crees, y prácticamente no ganas nada (o pierdes) con cada cliente que adquieres por publicidad.

Vamos a desglosarlo paso a paso, para que veas de dónde viene la diferencia:

---

## Tus dos errores centrales
### Error 1: Usas ingresos brutos para calcular el LTV, no el margen bruto
El LTV que importa para comparar con el CAC es el valor neto que te deja cada cliente a lo largo de su vida, no lo que cobras. Los $35/mes no son tuyos: el 30% se va en infraestructura y procesador de pagos, así que solo **$24,5/mes** aportan para cubrir el costo de adquisición, gastos fijos y ganancias.

Tu cálculo usa los ingresos totales, lo que infla el LTV en un 43% de más.

### Error 2: Tu cálculo de la vida útil del cliente es completamente erróneo
Dices que un cliente se queda 2 años, pero con un churn mensual del 8%, la vida media de un cliente es de **1 / 0,08 = 12,5 meses** (poco más de un año, no dos).

Para que la vida media fuera de 24 meses, tu churn mensual tendría que ser de ~4,17%, la mitad de lo que reportas. Probablemente confundiste churn mensual con anual, o calculaste la vida útil sin usar la fórmula estándar de suscripciones (distribución geométrica de la permanencia).

De hecho, el 63% de tus clientes se van antes de cumplir el primer año.

---

## Cálculo real de LTV/CAC
La fórmula correcta de LTV de contribución (el que se usa para comparar con CAC) es:
> LTV = (ARPU mensual * Margen bruto) / Churn mensual

Sustituyendo tus números:
LTV = ($35 * 0,7) / 0,08 = $24,5 / 0,08 = **$306,25**

Tu LTV/CAC real es:
$306,25 / $290 = **1,06x**

### Aún peor si contamos el valor del dinero en el tiempo
Los $24,5 que cobras dentro de 12 meses valen menos que los $290 que pagas hoy por adquirir el cliente. Con una tasa de descuento estándar para startups del 1% mensual (~13% anual), el LTV descontado es:
LTV descontado = $24,5 / (0,08 + 0,01) = **$272,2**
Así que tu LTV/CAC descontado es de 0,94x: **pierdes dinero con cada cliente que adquieres por publicidad**.

---

## Más datos que confirman que no es momento de escalar
1. **Payback de CAC de casi 12 meses**: Tardas 290 / 24,5 = ~11,8 meses en recuperar lo que te costó adquirir el cliente. Es un plazo extremadamente largo para publicidad pagada: tienes que financiar $10.000 hoy y no lo recuperas hasta dentro de un año, asumiendo que el churn y el CAC se mantengan (lo que casi nunca pasa al escalar).
2. **No te queda nada para gastos fijos**: Ese LTV de $306 solo cubre el costo de adquisición. No aporta nada para pagar salarios, herramientas, alquiler o ganancias. Tu rentabilidad actual seguro viene de clientes orgánicos (con CAC $0 o muy bajo), pero los clientes pagos casi no generan valor.
3. **Tu propio cálculo erróneo ni siquiera llega al umbral que mencionas**: Dices que 2,9 está por encima de 3, cuando es menor. Y ese umbral de 3x siempre se refiere a LTV de margen, no de ingresos brutos.
4. **Riesgo altísimo**: Si el CAC sube un 5% al escalar (lo normal al agotar las audiencias más eficientes) o el churn de clientes pagos es un punto mayor que el de tus clientes actuales (también muy común), pasas de ganar poco a perder dinero por cada cliente.

Si metes $10.000 hoy, adquirirás ~34 clientes que en total te dejarán solo $412 de margen bruto a lo largo de toda su vida, y tendrás que esperar más de un año para recuperar la inversión. No tiene sentido.

---

## ¿Cuándo sí le darías a la publicidad?
Necesitas cumplir dos requisitos mínimos para escalar con seguridad:
- LTV/CAC de margen de al menos 2,5-3x
- Payback de CAC menor de 6 meses (idealmente 3-4)

Para llegar ahí, mueve estas palancas primero:
1. **Baja el churn**: Si reduces el churn mensual de 8% a 3%, la vida media pasa a 33 meses, el LTV sube a $816 y el ratio llega a 2,8x (casi al umbral). Es la palanca más potente para suscripciones.
2. **Baja el CAC**: Prueba creatividades nuevas, audiencias más segmentadas o canales más baratos. Si logras bajar el CAC de $290 a $100, ya tienes un ratio de 3x con tus números actuales.
3. **Agrega ingresos adicionales**: Upsells, planes anuales (que reducen el churn y mejoran el flujo de caja al cobrar por adelantado) o funcionalidades premium aumentan el LTV sin necesidad de adquirir más clientes.
4. **Prueba primero con presupuesto chico**: Antes de meter $10.000, invierte $1.000 para confirmar que el CAC de la campaña se mantiene y que el churn de los clientes adquiridos por publicidad es igual al de tus clientes actuales (muchas veces los clientes pagos tienen mayor rotación que los orgánicos).

Con tus números actuales, escalar en publicidad es quemar caja por muy poco retorno. Mejor invierte ese dinero en arreglar el churn o mejorar la eficiencia de tus campañas primero.