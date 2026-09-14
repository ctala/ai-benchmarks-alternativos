# Muse Spark 1.3 — business_audit/retention_sobre_100_interpretacion

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 7.14 | quality: 8.0
- latency_total: 21.808s | tokens_per_second: 127.9
- input_tokens: 143 | output_tokens: 2790

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Y esa es exactamente la lectura peligrosa de ese 114%.

Ese 114% no es retención de clientes. Es **Retención Neta de Ingresos (NRR / Net Revenue Retention)**. No puede interpretarse como "no se me va nadie".

Te lo desgloso con tus propios números:

### 1. Retención de clientes no puede ser >100%

Por definición:

**Retención de Logos = Clientes retenidos de la cohorte inicial / Clientes iniciales**

Tú tenías 40 y ahora tienes 36. En el mejor de los casos, asumiendo que no sumaste ningún cliente nuevo este mes:

Retención de Logos = 36 / 40 = **90%**
Churn de Logos = **10% en un mes**

No es que no se te vaya nadie. Se te fueron 4 de cada 40.

Si esos 36 incluyen algún cliente *nuevo*, tu retención real es aún peor. Ejemplo: si captaste 2 nuevos, solo retuviste 34 de los 40 originales = 85% de retención.

La retención de clientes nunca puede pasar del 100%. No puedes retener más clientes de los que tenías.

### 2. Entonces, ¿qué es ese 114%?

Es esto:

**NRR = (MRR inicial de la cohorte - churn - contracción + expansión por upsell/cross-sell) / MRR inicial x 100**

El >100% solo significa que **la expansión tapó el agujero**.

Ejemplo con tus números para que cuadre:
40 clientes x $100 = $4,000 MRR inicial
Pierdes 4 clientes = -$400
Los 36 que quedan suben de plan y te dan +$960
MRR final misma cohorte = $4,560

NRR = 4,560 / 4,000 = **114%**

Ganaste ingresos netos, sí, pero perdiste 10% de tu base. Son dos cosas distintas.

Lo que tu panel te está ocultando es la **Retención Bruta de Ingresos (GRR)**:

**GRR = (MRR inicial - churn - contracción) / MRR inicial x 100** - sin contar expansión, topada al 100%.

En el ejemplo de arriba tu GRR sería ($4,000 - $400) / $4,000 = 90%. Ahí sí se ve el churn.

El NRR te dice si te expandes. El GRR y la Retención de Logos te dicen si sangras.

### 3. No, no puedes olvidarte del churn e ir a por captación

Con un 10% de churn mensual de logos, tienes un cubo con agujero. Haz la matemática anualizada:

0.9^12 = 28%. En 12 meses, de esos 40 solo te quedarían ~11 si sigues así.

Problemas:

1.  **La expansión tiene techo.** Un cliente puede subir de plan una o dos veces, no infinitamente. El churn, en cambio, puede seguir hasta cero.
2.  **Adquirir para tapar churn es carísimo.** Te cuesta 5-7x más adquirir que retener. Vas a estar corriendo en una cinta para quedarte en el mismo sitio.
3.  **Es una señal de producto.** Un NRR de 114% con churn de logos del 10% mensual suele significar: a unos pocos les encanta y pagan más, a muchos no les encaja y se van. Eso no se arregla con más marketing, se arregla con retención.

Un SaaS sano de verdad es: NRR >110% **Y** GRR >85-90% anual **Y** churn de logos bajo (para SMB, >2-3% mensual ya es preocupante, 10% es crítico).

### Qué mirar esta semana

1.  Verifica cómo calcula tu panel ese 114%. El NRR de verdad solo mira la misma cohorte inicial, sin incluir ventas nuevas. Si divide (ingresos totales este mes / ingresos totales mes pasado), no es NRR, es solo crecimiento.
2.  Calcula tu GRR y tu churn de logos mensual de los últimos 6 meses.
3.  Segmenta: ¿Quiénes se van y quiénes suben de plan? Casi seguro no son el mismo perfil.

Tienes un buen síntoma (puedes hacer upsell), pero escondiendo un mal síntoma (pierdes 1 de cada 10 al mes). No lo celebres ignorando el churn.