# Claude Opus 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.13 | quality: 10.0
- latency_total: 22.294s | tokens_per_second: 96.7
- input_tokens: 297 | output_tokens: 2155

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

Hay tres errores en el cálculo, y juntos cambian la conclusión.

## Error 1: con 8% de churn, el cliente no se queda 2 años

La vida media de un cliente es **1 / churn = 1 / 0,08 = 12,5 meses**, no 24.

Para dimensionarlo:
- La mitad de tus clientes se va antes de **~8 meses**.
- A los 24 meses solo queda el **13%** de una cohorte (0,92²⁴).

## Error 2: el LTV debe calcularse sobre margen, no sobre ingreso

Con ingreso calculas cuánto factura el cliente. Con margen calculas cuánto te deja para pagar el CAC.

- Margen mensual por cliente: $35 × 70% = **$24,50**
- LTV = $24,50 × 12,5 meses = **$306**

## Error 3: 2,9 está por debajo de 3

Es un detalle, pero el umbral se usa para decidir y lo estabas redondeando a tu favor.

## El ratio real

| | Tu cálculo | Recalculado |
|---|---|---|
| Vida del cliente | 24 meses | 12,5 meses |
| LTV | $840 (ingreso) | $306 (margen) |
| LTV/CAC | 2,9 | **1,06** |

Con un ratio de 1,06 cada cliente pagado apenas devuelve lo que costó, y no cubre gastos fijos, sueldos, soporte ni el costo del dinero en el tiempo.

## Qué pasaría con los $10.000

- Adquieres ~34 clientes ($10.000 / $290).
- El primer mes te dejan ~$845 de margen.
- Recuperas los $10.000 recién a los **~35 meses** (considerando el churn de la cohorte).
- Ganancia total en toda su vida: unos **$560**, antes de gastos operativos y sin descontar.

En la práctica, el riesgo es perder dinero:
- **El CAC sube al escalar.** Los primeros $290 suelen venir de la audiencia más barata, y al multiplicar el gasto por 10 casi siempre empeora.
- **Los clientes de publicidad pagada suelen tener más churn** que los orgánicos. Si tu 8% viene mayormente de clientes orgánicos, el churn de los pagados probablemente sea peor.
- Inmovilizas $10.000 de caja durante casi 3 años para ganar unos cientos.

## Qué tendría que cambiar para llegar a LTV/CAC ≥ 3

Necesitas un LTV de ~$870. Cada palanca por separado:

| Palanca | Valor actual | Valor necesario |
|---|---|---|
| Churn mensual | 8% | **≤ 2,8%** |
| CAC | $290 | **≤ $100** |
| Precio | $35 | **~$99** |

Lo realista es combinar varias. Por ejemplo, churn al 5% + precio a $45 + CAC a $200 da un LTV de ~$630 y un ratio de ~3,1.

## Lo que haría en tu lugar

1. **Atacar el churn primero.** Es la palanca que más mueve el número. Averigua por qué se van los clientes en los primeros meses (onboarding, valor percibido, cobros fallidos).
2. **Ofrecer plan anual prepago** (por ejemplo, 2 meses gratis). Mejora la retención y te da la caja por adelantado, lo que cambia mucho el payback.
3. **Probar subir el precio.** Con margen del 70% y churn alto, puede que estés cobrando poco por lo que entregas.
4. **Hacer una prueba chica de $1.000–2.000**, no $10.000. Mide el CAC real por canal y, sobre todo, el churn de esa cohorte pagada durante 2–3 meses.
5. **Escalar solo cuando la cohorte pagada muestre LTV/CAC ≥ 3** con datos propios, no estimados.

Ser rentable hoy es una buena base. Pero la rentabilidad actual no garantiza que la publicidad lo sea. Hoy cada dólar en ads te devuelve aproximadamente un dólar, y en tres años.