# MiniMax M3.1 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 73.635s | tokens_per_second: 177.2
- input_tokens: 368 | output_tokens: 13048

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

## Veredicto

**No, con esos números no aprobaría una inversión de $10.000 para “escalar fuerte”.** El cálculo tiene dos errores importantes y deja un margen muy pequeño.

### 1. Con 8% de churn mensual, la vida esperada no es de 24 meses

Vida esperada:

\[
\frac{1}{0,08}=12,5\text{ meses}
\]

De hecho, la probabilidad de que un cliente siga activo al mes 24 es:

\[
(1-0,08)^{24}=13,5\%
\]

Además, aunque现实中 se quedara 24 meses:

\[
\frac{840}{290}=2,90
\]

Eso **no está por encima de 3**; está por debajo.

### 2. Para comparar con CAC hay que usar LTV de margen bruto

El beneficio bruto mensual por cliente es:

\[
\$35 \times 70\%=\$24,50
\]

Por tanto:

| Métrica | Resultado |
|---|---:|
| Vida esperada | 12,5 meses |
| LTV de ingresos | $437,50 |
| **LTV de margen bruto** | **$306,25** |
| **LTV/CAC de margen bruto** | **1,06×** |
| Payback simple | 11,8 meses |

El LTV/CAC de **1,06×** está muy lejos de un objetivo prudente de 3×. El payback de 11,8 meses tampoco es muyistenido: contar con churn, el beneficio bruto acumulado esperado durante los primeros 12 meses es solo unos **$194 por cliente**, todavía inferior al CAC de $290.

Incluso aceptando tus 24 meses, el LTV de margen bruto sería:

\[
\$35 \times 70\% \times 24=\$588
\]

Y el ratio sería:

\[
588/290=2,03\times
\]

## ¿Qué producen los $10.000?

A un CAC de $290:

\[
10.000/290=34,48\text{ clientes}
\]

Beneficio bruto esperado de esos clientes durante su vida:

\[
34,48 \times \$306,25=\$10.560
\]

Después de publicidad:

\[
\$10.560-\$10.000=\boxed{\$560}
\]

Eso es un margen esperado de apenas **5,6%**, antes de descontar tiempo, impuestos, costos incrementales y cualquier deterioro del CAC. Además:

- Si el CAC sube seulement a **$306** —un 5,6%— el resultado cae a break-even.
- Si el churn sube de 8,0% a **8,45%**, también cae a break-even.

Es extremadamente frágil para una campaña de “escala fuerte”.

## Qué necesitas para decir que sí

Con los números actuales, para lograr un LTV/CAC de 3×你需要 uno de estos:

- **CAC máximo de aproximadamente $102**, manteniendo churn y margen.
- **Churn mensual de aproximadamente 2,8% o menos**, manteniendo CAC de $290.
- O una combinación: mejor CAC, mayor ARPU, mejor margen y mejor retención.

Para un mínimo más flexible de 1,5×, el CAC tendría que estar cerca de **$204**, todavía bastante por debajo de $290.

## Recomendación

No meta los $10.000 como inversión de escala. Puedes hacer una **prueba pequeña y capada por canal** para aprender, pero mide:

- CAC marginal, no CAC promedio.
- Retención real de los cohorts(Applicationes pagando, no el promedio de clientes antiguos.
- ARPU realmente cobrado.
- Churn de los primeros 30, 90 y 180 días.
- Margen después de todos los costos variables.

Escála en incrementos únicamente cuando los datos reales permitan sostener un LTV/CAC de margen bruto de al menos 3× y un payback que no te deje financiando clientes durante meses.

**Resumen: con 8% de churn, margen 70% y CAC $290, cada cliente deja solo unos $16 de contribución esperada. No hay margen suficiente para escalar fuerte.**