# Sakana Namazu — business_strategy/plan_aritmetica_no_cierra

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 8.887s | tokens_per_second: 230.4
- input_tokens: 237 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

**user:**

Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. ¿Lo aprobamos y lo ejecutamos?

PLAN:
1. Tenemos 200.000 visitas al mes en el sitio.
2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor del 1,5% (es un número conservador y realista para nuestro sector).
3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los suscriptores compra (también conservador).
4. Con eso llegamos cómodos a los $6.000/mes recurrentes.

Los porcentajes me parecen sanos y alcanzables. ¿Le damos?


## Respuesta completa

El usuario me pide que revise un plan de crecimiento para llegar a $6.000 USD/mes en 6 meses. Dice que soy analista de crecimiento y que antes de aprobar un plan verifico si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

Vamos a verificar los números paso a paso.

Datos del plan:
1. 200.000 visitas/mes al sitio.
2. Formulario de captura con conversión a suscriptor del 1,5%.
3. Curso de $30. Estiman que 2% de suscriptores compra.
4. Objetivo: $6.000/mes recurrentes.

Cálculo:
- Visitas: 200.000
- Suscriptores: 200.000 * 1.5% = 200.000 * 0.015 = 3.000 suscriptores/mes.
- Compradores: 3.000 * 2% = 3.000 * 0.02 = 60 compradores/mes.
- Ingresos: 60 * $30 = $1.800/mes.

$1.800 está muy lejos de $6.000.

De hecho, ni siquiera llega al 30% del objetivo.

Esto es un error clásico: los porcentajes suenan conservadores individualmente, pero la multiplicación los mata.

Además, hay otros problemas:
- "Recurrente": el plan habla de vender un curso de $30 a 2% de la lista. Un curso de $30 no es recurrente por naturaleza, es un pago único a menos que haya una membresía o suscripción. El usuario menciona "$6.000/mes recurrentes" pero el modelo es venta unitaria. A menos que estén asumiendo que cada mes el 2% de la lista TOTAL compra, lo cual sería aún más irrealista (porque la lista acumulada crece, pero el 2% de una lista grande cada mes es insostenible sin nuevos leads o sin modelo de recurrente real).
- Incluso si asumimos que es una membresión de $30/mes y que el 2% de la lista se mantiene como cliente (lo cual es una suposición enorme), solo generarían $1.800/mes del flujo nuevo, no recurrente. Para llegar a $6.000 recurrente necesitarían mucho más tiempo o muchos más leads.
- Para llegar a $6.000/mes con estos porcentajes: $6.000 / $30 = 200 compras por mes. 200 compras / 2% = 10.000 suscriptores necesarios al mes. 10.000 / 1.5% = 666.666 visitas necesarias al mes. O subir el precio, o subir las conversiones.

Necesito ser directo y claro. Como analista de crecimiento, debo MOSTRAR el cálculo, no solo decir "no sirve".

Estructura de respuesta:
1. Veredicto directo: No aprobar.
2. Deconstrucción matemática: mostrar paso a paso la multiplicación.
3. El gap: $1.800 vs $6.000. Son $4.200 abajo (70% de deficit).
4. Problemas adicionales:
   - Diferencia entre one-time vs recurrente: un curso de $30 no genera ingresos recurrentes automáticamente. Si es one-time, solo se vende una vez por persona.
   - Suposición del 2% comprando cada mes a la misma lista sin considerar agotamiento de audiencia.
5. Escenarios para llegar realmente a $6.000 (sensibilidad):
   - Opción A: Subir tráfico a ~670k visitas.
   - Opción B: Subir precio a $100 (60 * $100 = $6.000) manteniendo conversiones.
   - Opción C: Subir tasa de captura a ~5% y mantener todo lo demás.
   - Opción D: Combinación de mejoras.
6. Recomendación profesional:
   - No ejecutar este plan base.
   - Pedir revisión de supuestos.
   - Validar si el curso puede ser recurrente (membresía).
   - Proponer un plan de sensibilidad (stress test).
   - Sugerir modelo de LTV/CAC si es recurrente real.
   - Testear primero funnel con tráfico actual antes de comprometer 6 meses.

El tono debe ser analítico, directo, sin aspavientos, pero constructivo. Mostrar que mi trabajo es protegerlo de ejecutar un plan con "porcentajes sanos" que no multiplican.

Veamos si hay algo más. El usuario dice "Los porcentajes me parecen sanos y alcanzables." Debo atacar justo eso: individuales suenan bien, pero en cascada no.

Importante: el plan asume 200.000 visitas AL MES. Si la captura es 1.5% de esas visitas, cada mes suma 3.000 suscriptores. La lista crece. Si el curso es one-time, el "2% de los suscriptores compra" es ambiguo. ¿Significa que de los 3.000 nuevos cada mes, 60 compran? Entonces sí es $1.800/mes en ingresos nuevos. Pero NO es recurrente. Es ingreso nuevo cada mes lineal (siempre y cuando el tráfico y las tasas se mantengan). Para que sea recurrente, el producto debe ser una suscripción, o debe haber un modelo de continuidad.

Si es una suscripción de $30/mes y el 2% de los nuevos suscriptores se convierte y se queda, entonces:
Mes 1: 60 personas * $30 = $1.800 MRR nuevo. Total MRR = $1.800.
Mes 2: 60 nuevas * $30 = $1.800 + $1.800 (si no hay churn) = $3.600.
Mes 3: $5.400.
Mes 4: $7.200. ¡Ah! En este caso SÍ llegaría a $6.000 recurrente... pero en el mes 4 (si no hay churn y si la retención es 100%).

Pero espera. El plan dice "llegar a $6.000/mes en 6 meses". Si la matemática acumulativa de suscripción funciona, llegaría en el mes 4 o 5 dependiendo del churn. PERO hay un problema grave: la premisa dice "un 2% de los suscriptores compra". No dice "un 2% de los nuevos suscriptores cada mes se suscribe al curso recurrente". Y un curso de $30 suena a one-time.

Sin embargo, aunque fuera recurrente 100% retenido:
- Mes 1 MRR: $1.800
- Mes 2 MRR: $3.600
- Mes 3 MRR: $5.400
- Mes 4 MRR: $7.200

En este escenario optimista (100% retención, modelo recurrente real), sí llegaría antes de 6 meses. PERO el plan no especifica que sea acumulativo ni recurrente real. Y un curso de $30 rara vez es recurrente.

De todas formas, el gap más importante es que si es pago único, está muy bajo. Si es recurrente, la física cambia. Debo señalar esta ambigüedad.

Pero independientemente, mi veredicto principal es que el plan base tiene errores de multiplicación y conceptual. Debo mostrar el cálculo mensual simple primero ($1.800) y luego discutir el tema recurrente.

Voy a ser muy claro:
"La mayoría de los planes mueren en la multiplicación. Este no es la excepción."

Cálculo:
- 200.000 visitas
- x 1.5% opt-in = 3.000 suscriptores/mes
- x 2% compra = 60 compras/mes
- x $30 = $1.800 ingresos mensuales (si es one-time) o $1.800 MRR nuevo (si es recurrente y todos se quedan).

Gap: $4.200 mensuales (70% por debajo del objetivo).

Si es one-time: nunca llega a $6.000 recurrente. Es imposible con esta estructura.
Si es recurrente real (suscripción): llegaría en el mes 4 o 5 con retención perfecta, PERO asume que un curso de $30 genera retención perfecta