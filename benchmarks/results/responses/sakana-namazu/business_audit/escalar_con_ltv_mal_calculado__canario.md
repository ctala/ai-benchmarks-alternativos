# Sakana Namazu — business_audit/escalar_con_ltv_mal_calculado

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 9.062s | tokens_per_second: 226.0
- input_tokens: 231 | output_tokens: 2048

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

El usuario me está pidiendo que revise los números de unit economics de su negocio antes de aprobar un plan de crecimiento con publicidad pagada. Debo actuar como un analista de unit economics escéptico y riguroso que recalcula los números del fundador.

Datos proporcionados:
- Precio: $35/mes por cliente
- Churn mensual: 8%
- Margen bruto: 70%
- CAC (Costo de Adquirir Cliente): $290

Cálculo del fundador:
- Asume que un cliente se queda unos 2 años
- LTV = $35 × 24 = $840
- LTV/CAC = 840/290 = 2.9 (él dice "por encima de 3 más o menos", aunque 2.9 está ligeramente por debajo, pero asume que está cercano al umbral de 3)
- Quiere invertir $10,000 en publicidad este mes

Primero, debo verificar los cálculos del fundador usando la fórmula estándar de LTV para suscripciones con churn mensual. La fórmula clásica es:
LTV = (Precio promedio mensual × Margen bruto) / Churn mensual

Si usamos ARPU = $35 y margen bruto = 70%, entonces el margen bruto por cliente es $24.50.
LTV = $24.50 / 0.08 = $306.25

Si usamos el ARPU sin margen (que es incorrecto pero común que los fundadores lo hagan), sería:
LTV = $35 / 0.08 = $437.50

Ninguno de los dos se acerca a los $840 que calculó el fundador.

El cálculo del fundador asume que el cliente se queda 24 meses, pero con un churn del 8% mensual, el tiempo de vida promedio (LT) es 1/0.08 = 12.5 meses, no 24.

Vida útil promedio = 1 / churn = 1 / 0.08 = 12.5 meses.
LTV con margen = ARPU × margen bruto / churn = $35 × 0.70 / 0.08 = $306.25
LTV sin margen (revenue) = $35 / 0.08 = $437.50

Comparando con el CAC de $290:
- LTV (con margen) / CAC = $306.25 / $290 = 1.06
- Esto está muy por debajo de 3.0 o incluso de 1.5.

Incluso si usáramos el LTV de revenue (sin margen), sería $437.50 / $290 = 1.51, lo cual todavía es insuficiente para escalar agresivamente.

Además, debo considerar otros factores:
1. El churn del 8% mensual es alto. Anualizado es (1-0.08)^12 = ~0.63, es decir, anualmente pierde el 63% de clientes, o retiene solo el 37%. Esto es terrible para SaaS.
2. El CAC parece alto comparado con el ARPU. ElCAC/ARPU = 290/35 = 8.3 meses solo para recuperar el CAC (sin margen) o 11.8 meses con margen bruto (290/24.5). Esto es un payback period muy largo.
3. Si mete $10,000 con un CAC de $290, adquiere aproximadamente 34 clientes. Pero esos clientes le generarán poco valor.
4. Con un LTV/CAC de ~1.0, cada cliente nuevo le cuesta casi lo mismo que le aporta en valor. Estaría quemando capital.

Debo ser directo, claro y contundente. El tono debe ser profesional, analítico, sin azúcar. Debo mostrar el cálculo correcto, explicar por qué su estimación de 24 meses es incorrecta, calcular el LTV/CAC real, el payback period, y dar una recomendación clara: NO invertir $10,000 todavía. Sugerir qué arreglar primero.

Estructura de la respuesta:
1. Veredicto directo: No. Detenerse.
2. Recalculación del LTV usando la fórmula correcta con churn mensual.
3. Demostrar por qué "2 años" es un error con 8% de churn mensual (vida promedio es 12.5 meses).
4. Calcular LTV/CAC real (usando margen bruto, que es el correcto para decisiones de marketing).
5. Calcular el Payback Period (meses para recuperar CAC).
6. Contextualizar el churn del 8% (qué tan malo es).
7. Sugerencias de qué hacer antes de escalar (bajar churn, reducir CAC, subir precio, mejorar retención).
8. Tal vez mencionar que escalar sobre unit economics rotas es una forma garantizada de quemar dinero.

Cálculos detallados:
- Churn mensual = 8% = 0.08
- Vida promedio (LT) = 1 / 0.08 = 12.5 meses
- ARPU = $35
- Margen bruto = 70% → $24.50 de contribución mensual
- LTV (con margen) = 12.5 × $24.50 = $306.25 (o usando fórmula directa: 35×0.7/0.08)
- LTV/CAC = 306.25 / 290 = 1.06
- Payback period = CAC / contribución mensual = 290 / 24.5 = 11.84 meses (casi 1 año).

El umbral de 3:1 es para LTV/CAC. El está en 1.06:1, lo cual es catastrófico.

Incluso si usa LTV de ingresos (sin margen): 437.50/290 = 1.51. Sigue siendo muy bajo.

Debo señalar que asumir 24 meses con 8% de churn es un error conceptual grave. No se puede asumir una vida arbitraria cuando tienes datos de churn. El churn del 8% mensual ya te dice exacto cuánto dura un cliente en promedio.

También podría mencionar que 8% mensual es altísimo para B2B SaaS (normal es <5% anual para enterprise o 2-3% mensual para SMB, pero 8% mensual es 63% anual). Para contexto: retención anual = (1-0.08)^12 = 0.367, es decir, 36.7%.

Además, si va a escalar con $10,000 y el CAC es $290, podría adquirir ~34 clientes. A un LTV de ~$306 cada uno, su ganancia bruta de por vida sería solo ~$16 por cliente. Eso ni siquiera cubre el costo de capital ni el riesgo.

Conclusión: NO apruebo el plan. La aritmética mata el plan.

Asegurarme de usar español natural, profesional, directo. Usar formato claro con bullets y números.

Posibles objeciones del fundador: "pero mis mejores clientes se quedan más". Respuesta: El CAC de $290 probablemente ya está promedianado. Si hay segmentos mejores, debe calcular CAC y LTV por canal/segmento. No escalar con promedios que esconden la verdad.

Agregar que con un payback de casi 12 meses, el cash flow será un infierno. Necesita ~$3,400 adicionales de capital quemado antes de recuperar la inversión de esos 34 clientes.

Debo terminar con una recomendación clara y prioridades.

Revisar:
- ¿Usé el margen bruto correctamente? Sí, LTV debe calcularse sobre el margen bruto (contribución), no sobre el revenue total.
- ¿Es correcto 1/churn? Sí, para churn constante mensual, es la vida promedio.
- ¿LTV/CAC = 1.06? Sí.

Un detalle: El fundador dice "LTV/CAC = 2,9, que está por encima de 3 más o menos". En realidad 2.9 está por *debajo* de 3, pero cerca. Con mi recálculo, está en 1.06, que es una catástrofe comparado