# Gemma 4 26B MoE (3.8B activos) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 8.91 | quality: 10.0
- latency_total: 21.197s | tokens_per_second: 42.3
- input_tokens: 222 | output_tokens: 896

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

**Ni se te ocurra. Detente ahí mismo.**

Como analista, mi trabajo es evitar que quemes esos $10,000 en un agujero negro financiero. Tu entusiasmo es peligroso porque estás cometiendo el error clásico de los fundadores: **estás calculando un LTV teórico basado en una suposición de retención que tu Churn actual no respalda.**

Aquí está el desglose de por qué tu aritmética es errónea y por qué este plan te puede quebrar:

### 1. El error del "LTV de dos años"
Dices que un cliente se queda 24 meses. Pero tu **Churn mensual es del 8%**.
En el mundo de los modelos de suscripción, la vida media de un cliente se calcula como:
$$\text{Vida Media} = \frac{1}{\text{Churn Rate}}$$

En tu caso: $1 / 0.08 = \mathbf{12.5 \text{ meses}}$.

No se quedan 24 meses. La estadística dice que, con un 8% de churn, la mitad de tus clientes habrán desaparecido mucho antes de llegar al segundo año. Tu cálculo de LTV está inflado un 90%.

### 2. Recalculando tus Unit Economics reales
Vamos a usar tus números reales (Margen Bruto $\times$ Vida Media):

*   **LTV Real:** $\$35 (\text{Precio}) \times 0.70 (\text{Margen}) \times 12.5 (\text{Meses}) = \mathbf{\$306.25}$
*   **CAC:** $\mathbf{\$290}$
*   **Ratio LTV/CAC Real:** $306.25 / 290 = \mathbf{1.05}$

**Tu ratio no es 2.9, es 1.05.**

### 3. El diagnóstico: Estás en la zona de muerte
Un ratio de **1.05 es una sentencia de muerte para el escalado**. 

¿Por qué? Porque ese 1.05 es tu margen *bruto* después de infraestructura. No has restado:
*   Salarios de soporte/operaciones.
*   Impuestos.
*   Costos de software de gestión.
*   El costo de oportunidad de tu tiempo.

Si metes $10,000 en publicidad, vas a adquirir aproximadamente 34 clientes ($10,000 / $290). Esos clientes te van a dejar un margen bruto total de $10,412 a lo largo de su vida. **Vas a gastar $10,000 para ganar $412 de margen bruto.** En términos de flujo de caja, vas a asfixiar tu empresa.

### Mi veredicto y plan de acción:

**NO le des al botón de "Aumentar Presupuesto".** Si escalas con estos números, solo vas a morir más rápido.

Antes de tocar la publicidad, tienes que trabajar en dos palancas, en este orden de prioridad:

1.  **Bajar el Churn (Prioridad Máxima):** Un churn del 8% es altísimo para un modelo de $35/mes. Si logras bajar el churn al **4%**, tu vida media sube a 25 meses y tu LTV real salta a **$612**. Ahí es donde el juego se pone divertido.
2.  **Optimizar el CAC:** Si no puedes bajar el churn de inmediato, necesitas que ese CAC de $290 baje a menos de $100 para tener un margen de maniobra saludable.

**Tu objetivo antes de escalar:** Necesitas un LTV/CAC de al menos 3.0 con tus números actuales. Con un CAC de $290, tu LTV debería ser de ~$870. Para lograr eso con un margen del 70%, necesitas que tus clientes se queden **35 meses** (un churn del 2.8%).

**Vuelve cuando el churn sea menor al 4%. Hasta entonces, no escalas.**