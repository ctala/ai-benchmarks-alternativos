# Sakana Namazu — business_audit/escalar_con_ltv_mal_calculado

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 11.684s | tokens_per_second: 175.3
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

El usuario quiere escalar fuerte con publicidad pagada basándose en sus números. Dice ser rentable y quiere meter $10,000 en publicidad este mes. Debo analizar sus unit economics fríamente, como un analista que recalcula los números del fundador y mata planes en la aritmética.

Números del usuario:
- Precio: $35/mes
- Churn mensual: 8%
- Margen bruto: 70%
- CAC: $290
- Cálculo de LTV: 35 * 24 = $840
- LTV/CAC = 840/290 ≈ 2.9
- Dice que está "por encima de 3 más o menos" (en realidad es 2.9, cercano a 3)

Problemas evidentes:
1. Churn mensual de 8% es altísimo. Eso implica una vida útil promedio de 1/0.08 = 12.5 meses, NO 24 meses. El usuario asume 2 años ilegalmente sin justificación.
2. El LTV correcto usando el modelo simple: (Precio * Margen bruto) / Churn mensual, o al menos ARPU / churn. Pero debe usar margen bruto, no revenue bruto. El CAC se recupera con el margen, no con el revenue total.
3. Vamos a calcular:
   - LTV = ($35 * 70%) / 0.08 = $24.50 / 0.08 = $306.25
   - O si usamos revenue: $35 / 0.08 = $437.50
   - Comparado con CAC de $290.
   - Con margen: LTV/CAC = 306.25 / 290 ≈ 1.06. Es decir, apenas se paga el CAC, sin margen para gastos operativos, R&D, etc. Es inviable.
   - Con revenue (incorrecto): 437.5 / 290 ≈ 1.51. Aún así muy bajo.

4. Otra forma: Payback period. Con $35/mes y 70% margen = $24.50 contribución mensual. Para recuperar $290 de CAC: 290 / 24.50 ≈ 11.8 meses. Es decir, casi un año. Con un churn de 8% mensual, muchos clientes no llegarán a pagar el CAC.

5. Tiempo para recuperar CAC vs churn: A los 12 meses, la retención es (1-0.08)^12 ≈ 0.92^12 ≈ 0.367. Es decir, solo ~37% de los clientes quedan al año. La probabilidad de que un cliente randmom se quede lo suficiente para pagar el CAC es baja.

6. Si mete $10,000 con CAC $290, adquiere ~34 clientes. Esos clientes le generan flujo, pero dado el churn alto, no es claramente rentable.

7. El usuario dice "ya soy rentable". Pero si su churn es 8% mensual, eso es 63% anual (1 - (1-0.08)^12). Es difícil ser rentable a largo plazo con esos números a menos que la adquisición sea orgánica o muy barata. Quizá es rentable porque tiene otros canales oclientes antiguos con mejor retención.

8. Debo ser directo, frío, profesional. El tono debe ser el del personaje: "analista de unit economics que recalcula y mata planes". Debo corregir la matemática sin ser agresivo pero sí firme.

Estructura de respuesta:
- Veredicto inmediato: No le doy. O "stop". El plan muere en la aritmética.
- Error 1: La vida asumida de 24 meses es falsa. Con 8% churn mensual, la vida promedio es 12.5 meses.
- Error 2: LTV se calcula sobre margen, no revenue. Fórmula correcta: LTV = (ARPU × Margen Bruto) / Churn.
- Cálculo real:
  - ARPU = $35
  - Margen 70% = $24.50 contribución
  - Churn 8%
  - LTV = $24.50 / 0.08 = $306
  - LTV/CAC = 306 / 290 = 1.05 (casi 1.0, no 2.9)
- Qué significa LTV/CAC de 1.05: Por cada $290 que gastas, recuperas $306 en valor presente (y eso sin considerar costo de capital, ni el hecho de que el churn puede variar, ni que el CAC puede subir al escalar). No hay margen para operar. Es "buying revenue dollar at wholesale".
- Análisis de payback period: 11.8 meses. Con churn 8%, es un suicidio. A los 12 meses solo queda ~37% de la cohorte.
- Análisis del $10,000: Adquiere ~34 clientes. Esos aportan flujo futuro, pero el capital queda atrapado por casi un año, y pierdes ~8% de los clientes cada mes.
- Sugerencias: No escalar con paid ads todavía. Opciones:
  - Bajar CAC (mejorar creatives, canales).
  - Reducir churn (es la variable más crítica. De 8% a 4% cambia todo: LTV = 24.5/0.04 = 612; LTV/CAC = 2.1. Aún bajo pero mucho mejor. A 3%: LTV = 816; ratio 2.8).
  - Subir precio o monetización.
  - Si escalar, hacerlo solo si el churn que observa es en realidad mucho menor para el canal paid (p.ej. los que vienen de ads se quedan más). Pero hay que demostrarlo con cohortes, no asumir.
- Mencionar que "supporting" que es 8% mensual anualizado es ~63% anual. Muy alto para SaaS.

Tono: directo, frío, analítico. No usar introducciones largas. Ir al grano.

Posible formato:
- Veredicto: No.
- Cálculo correcto en una tabla o bullet points claros.
- Explicar por qué su LTV está sobrestimado por ~2.7x.
- Explicar por qué su CAC está bien pero no importa si el LTV está mal.
- Recomendación final.

Asegurarme de no ser insultante pero sí implacable con los números. El personaje dice "Muchos planes mueren en la aritmética". Debo encarnar eso.

Detalles adicionales:
- ¿Debería usar fórmula de LTV con discount rate? Quizá es overkill, pero puedo mencionar que sin tasa de descuento ya es malo. Si consideramos costo de capital, es peor.
- ¿Qué pasa con el $10,000 este mes? Si los adquiere, va a tener un hoyo de flujo de caja temporal grande. Con payback de ~12 meses, necesita capital para sobrevivir.
- Quizá sus clientes actuales se quedan 2 años, pero si el churn es 8%, eso es estadísticamente imposible a menos que sea muy no lineal (p.ej. muchos se van al inicio y luego se quedan). Si tiene datos de cohortes que demuestran que a los 12 meses el churn se frena (p.ej. churn de 8% solo en mes 1-3, luego 1%), entonces debe calcular LTV por cohorte, no con churn promedio simple. Pero no debe asumir.
- Puedo ofrecer una nota: Si su churn es "voluntario" vs "involuntario" (tarjetas que fallan), eso cambia la táctica. Pero el resultado es el mismo hasta que lo arregle.

Voy a escribir la respuesta. Voy a usar formato claro, cálculos explícitos.

Posible texto:

"No le doy. El plan muere en la aritmética."

Luego explicar los dos errores fatales:
1. **Confundir ingreso con contribución**. El CAC se recupera con el margen bruto, no con el precio total. Tu contribución mensual es $24.50, no $35.
2. **Confundir vida esperada con un número deseado**. Con churn mensual