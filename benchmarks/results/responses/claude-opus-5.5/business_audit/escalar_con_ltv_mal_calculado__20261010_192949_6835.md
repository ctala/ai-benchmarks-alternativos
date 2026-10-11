# Claude Opus 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 21.458s | tokens_per_second: 95.1
- input_tokens: 297 | output_tokens: 2040

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

# No le des todavía. Los números no aguantan.

Tu cálculo tiene tres errores, y los tres empujan en la misma dirección: hacen que el negocio parezca mejor de lo que es.

## 1. Con 8% de churn, el cliente no se queda 2 años

La vida media de un cliente es 1 / churn:

> 1 / 0,08 = **12,5 meses**, no 24.

Con 8% mensual, a los 24 meses solo sigue activo el ~13% de los clientes (0,92²⁴ ≈ 0,135).

## 2. El LTV se calcula sobre margen, no sobre ingreso

Lo que te deja cada cliente es lo que queda después de infraestructura y pagos:

> $35 × 70% = **$24,50/mes de margen bruto**
> LTV = $24,50 × 12,5 = **$306**

## 3. 2,9 no está "por encima de 3"

Aun con tu número original no pasabas el umbral. Pero con el número corregido:

> **LTV/CAC = $306 / $290 ≈ 1,06**

Cada dólar en publicidad te devuelve, en toda la vida del cliente, $1,06. Y eso antes de soporte, onboarding, devoluciones y valor temporal del dinero. En la práctica estás en equilibrio o perdiendo.

## Qué pasa con los $10.000

| Concepto | Valor |
|---|---|
| Clientes adquiridos (10.000 / 290) | ~34 |
| Margen bruto que generan en el mes 1 | ~$845 |
| Margen bruto total en toda su vida | ~$10.560 |
| **Ganancia neta, en el mejor caso** | **~$560** |
| Tiempo para recuperar los $10.000 (ajustado por churn) | **~35 meses** |

Pones $10.000 hoy para recuperarlos en casi 3 años y ganar $560. Eso suponiendo que el CAC se mantenga en $290. Al escalar suele subir, porque agotas primero las audiencias baratas. Con un CAC de $320, ya pierdes plata.

**El problema de fondo:** ser rentable hoy no significa que la adquisición pagada sea rentable. Probablemente tus clientes actuales llegaron por canales baratos (orgánico, boca a boca). Los clientes pagados son otra cohorte, con otra economía.

## Qué hacer en cambio

**1. Ataca el churn primero. Es tu palanca más grande.**

| Churn mensual | Vida media | LTV | LTV/CAC |
|---|---|---|---|
| 8% (hoy) | 12,5 meses | $306 | 1,06 |
| 5% | 20 meses | $490 | 1,7 |
| 4% | 25 meses | $612 | 2,1 |
| 3% | 33 meses | $817 | 2,8 |

**2. Baja el CAC o sube el precio.** Para llegar a 3:1 con el churn actual, el CAC tendría que ser de unos **$100**. Otra vía es subir el precio o vender planes anuales prepagados, que además cobran por adelantado y reducen el churn.

**3. Si quieres probar publicidad, hazlo con $1.000–2.000, no $10.000.** El objetivo es medir dos cosas:
- El CAC real por canal.
- El churn específico de los clientes que llegan por anuncios. Muchas veces es peor que el de los orgánicos.

**4. Verifica de dónde salió el "2 años".** Si tienes datos de cohortes que muestran que los clientes antiguos se quedan más tiempo (churn decreciente con la antigüedad), el panorama puede mejorar. Pero eso hay que medirlo, no suponerlo. Con el 8% que me diste, la vida media es 12,5 meses.

**Conclusión:** escala cuando el LTV/CAC esté en 3 o más y el payback por debajo de 12 meses. Hoy estás en 1,06 y unos 35 meses. Arregla la retención y luego acelera.