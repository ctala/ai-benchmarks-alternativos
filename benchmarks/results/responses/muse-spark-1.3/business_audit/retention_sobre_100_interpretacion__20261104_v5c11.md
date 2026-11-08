# Muse Spark 1.3 — business_audit/retention_sobre_100_interpretacion

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 20.616s | tokens_per_second: 104.9
- input_tokens: 144 | output_tokens: 2163

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Y esa es justo la trampa de esa métrica.

Lo que tu panel llama **"Retención de ingresos: 114%" es Retención Neta de Ingresos (NRR / Net Dollar Retention)**, no retención de clientes.

Y con tus propios números lo puedes ver: **sí se te está yendo gente.**

### 1. Retención de clientes no puede estar por encima del 100%

Retención de clientes / logos es:

> Clientes retenidos de la cohorte inicial / Clientes iniciales

Tú pasaste de 40 a 36. Asumiendo que no sumaste clientes nuevos este mes:

36 / 40 = **90% de retención de logos, 10% de churn de logos en un mes.**

Si sí sumaste clientes nuevos, es peor. Ejemplo: si de esos 36, 2 son nuevos, entonces solo retuviste 34 de los 40 originales: 34 / 40 = **85% de retención.**

Por definición, la retención de logos tiene un techo de 100%. No puedes retener más clientes de los que tenías.

Perder 10% de tus clientes en un mes es muchísimo. Anualizado, eso sería quedarte solo con ~28% de tus clientes al cabo de un año si no captas a nadie más.

### 2. Por qué entonces ingresos da 114%?

Porque la fórmula Neta mezcla 4 cosas distintas:

**NRR = (Ingresos iniciales + Expansión - Contracción - Churn) / Ingresos iniciales x 100**

Tu 114% no significa "no hay churn". Significa:

**La expansión de los que se quedaron tapó el hueco de los que se fueron.**

Ejemplo simplificado con tus números:
40 clientes x $100 = $4,000 iniciales
- Pierdes 4 clientes: -$400 por churn
- 10 clientes suben de $100 a ~$196: +$960 por expansión
Final: $4,560 / $4,000 = **114%**

Ganas más dinero con menos clientes. Eso es bueno, pero esconde el problema.

Lo que no te está mostrando ese 114% es tu **Retención Bruta (GRR)**:

**GRR = (Ingresos iniciales - Contracción - Churn) / Ingresos iniciales x 100**

La GRR no suma la expansión, y nunca puede pasar de 100%. Esa es tu verdadera medida de fuga. Con un churn de logos del 10%, tu GRR casi seguro está por debajo del 90%, que para SaaS es una señal roja.

### 3. ¿Puedes dejar de preocuparte por el churn y solo captar?

No, es lo contrario. Un NRR >100% con caída de logos es insostenible:

1.  **Estás encogiendo la base que se puede expandir.** Los upsells de hoy son de un grupo cada vez más pequeño. No puedes subir de plan infinitamente a los mismos 36, 30, 25...
2.  **Estás llenando un cubo con fugas.** Captar para compensar un 10% de churn mensual te va a salir carísimo en CAC, y normalmente los clientes nuevos pagan menos y churnean más que los antiguos.
3.  **Es un sesgo de supervivencia.** "Varios subieron de plan" suena bien, pero ¿quiénes se fueron? Si se van los pequeños y solo se quedan los grandes, tu producto puede estar dejando de servir a un segmento entero.

Un 114% de NRR es de hecho excelente — el benchmark top es 110-130% — pero solo es sano si viene acompañado de una GRR alta (>90%) y una retención de logos alta.

Tú tienes la mitad buena (expansión) y la mitad mala (fuga).

No mires solo el neto. Pide a tu panel que te desglose para la misma cohorte:
- Ingreso perdido por churn
- Ingreso perdido por downgrades
- Ingreso ganado por upsell/cross-sell

Ahí verás la lectura menos halagadora, pero correcta.