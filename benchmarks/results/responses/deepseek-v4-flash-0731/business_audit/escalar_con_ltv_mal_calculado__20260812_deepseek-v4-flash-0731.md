# DeepSeek V4 Flash 0731 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 107.05s | tokens_per_second: 22.3
- input_tokens: 202 | output_tokens: 2390

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

Voy a detenerte aquí, porque tu instinto de escalar es correcto, pero tu aritmética tiene un error fatal que te va a hacer quemar $10,000 sin retorno. Como analista, no puedo aprobar ese desembolso con estos números.

Aquí está el desglose de por qué tu cálculo está mal y qué significa realmente tu negocio.

### 1. El Error Crítico: La Vida del Cliente (Lifetime)
Tú asumiste que el cliente se queda **24 meses** (2 años). Pero tu churn mensual es del **8%**.

La fórmula para la vida promedio del cliente es:
**Vida (meses) = 1 / Churn Mensual**

- 1 / 0.08 = **12.5 meses** (no 24).

Tu cliente promedio se va en poco más de un año, no en dos. Ese es el error que infla tu LTV.

### 2. El Segundo Error: El Margen Bruto
Incluso si usaras 12.5 meses, estás calculando LTV sobre el ingreso bruto ($35). Pero tú mencionas que tu margen bruto es del **70%** (después de infraestructura y pagos). El LTV debe calcularse sobre el **beneficio bruto mensual**, no sobre el ingreso.

**Beneficio bruto mensual por cliente:** $35 × 0.70 = **$24.50**

### 3. El Cálculo Correcto (La Realidad)
Aquí están los números reales de tu unidad económica:

- **LTV (Beneficio Bruto):** $24.50 × 12.5 meses = **$306.25**
- **CAC:** $290
- **Ratio LTV/CAC:** $306.25 / $290 = **1.06**

**Tu ratio real es 1.06, no 2.9.**

### 4. El Veredicto: NO le des a $10,000
Con un ratio de **1.06**, estás en el punto de **equilibrio absoluto** (y probablemente perdiendo dinero si consideras gastos generales no incluidos en tu margen del 70%).

- Si inviertes $10,000, adquieres ~34 clientes ($10,000 / $290).
- Esos 34 clientes generarán un beneficio bruto total de ~$10,412 ($306 × 34).
- Estás ganando ~$400 en beneficio bruto sobre $10,000 de gasto, **antes** de pagar tu salario, software, soporte, etc. Básicamente, estás regalando tu tiempo y asumiendo todo el riesgo para no ganar nada.

**Regla general:** La mayoría de los inversores y operadores buscan un LTV/CAC de **3:1** para escalar agresivamente. Tú estás en 1.06. Escalar ahora es apostar a que tus números mejoren solos, lo cual no es una estrategia.

### 5. ¿Qué hago en lugar de gastar $10,000?

Necesitas arreglar la máquina antes de pisar el acelerador. Tienes tres palancas claras:

1.  **Reducir el Churn (La palanca más poderosa):**
    - Si bajas el churn del 8% al **5%** mensual, la vida del cliente sube a 20 meses.
    - Nuevo LTV: $24.50 × 20 = $490.
    - Nuevo Ratio: $490 / $290 = **1.69**. (Mejor, pero aún no es 3).
    - Si lo bajas al **3.5%** mensual (vida de 28.5 meses), el LTV sube a ~$700, y el ratio llega a **2.4**. Ahí ya puedes empezar a hablar de escalar.

2.  **Reducir el CAC:**
    - Tu CAC de $290 es muy alto para un producto de $35/mes. Necesitas que el CAC esté por debajo de **$100** para que el ratio sea saludable (LTV $306 / CAC $100 = 3.06).
    - ¿Puedes cambiar a canales orgánicos, referidos, o mejorar tu página de aterrizaje para convertir mejor con el mismo tráfico pagado?

3.  **Aumentar el Precio o el Margen:**
    - Si subes el precio a $49/mes (manteniendo el margen del 70%), el beneficio bruto mensual es $34.30.
    - LTV: $34.30 × 12.5 = $428.
    - Ratio: $428 / $290 = **1.47**. Sigue siendo bajo.

### Mi recomendación profesional:
**No gastes los $10,000.** En su lugar, destina **$500 - $1,000** para una prueba controlada.

- Usa ese dinero para probar 2 o 3 creatividades/audiencias nuevas.
- Mide el CAC real y el churn de esos 3-4 clientes nuevos.
- Mientras tanto, enfócate el 100% de tu energía en mejorar la retención (onboarding, soporte, características de valor). Un pequeño cambio en el churn tiene un impacto exponencialmente mayor que cualquier optimización de anuncios.

Cuando tu ratio LTV/CAC esté por encima de **2.5** (idealmente 3) de forma consistente, entonces podrás hablar conmigo de nuevo para escalar. Hoy, esos $10,000 son una apuesta perdedora.