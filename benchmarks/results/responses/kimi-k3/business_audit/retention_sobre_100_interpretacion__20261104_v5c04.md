# Kimi K3 — business_audit/retention_sobre_100_interpretacion

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.56 | quality: 8.0
- latency_total: 95.891s | tokens_per_second: 39.8
- input_tokens: 245 | output_tokens: 3819

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. La lectura correcta es casi la contraria de la que haces, y los números que das lo demuestran.

**Qué mide cada cosa**

- La "retención de ingresos" (NRR) mide **dinero, no clientes**. Un 114% significa que la cohorte de clientes de inicio de periodo genera hoy un 14% más de ingresos: las subidas de plan superaron, en euros, al churn y a las bajadas de plan. El hecho de que supere el 100% confirma que incluye expansión.
- La retención de clientes (logo retention) **no puede superar el 100%** por definición: no puedes conservar más clientes de los que tenías.

**Tus números reales**

- 40 → 36 clientes = has perdido al menos 4 (más, si captaste alguno nuevo este mes).
- Logo churn mensual ≥ 10%. Anualizado: 0,9¹² ≈ 0,28, es decir, a ese ritmo perderías **~72% de tu base en un año**.
- Vida media esperada de un cliente: 1 / 0,10 ≈ 10 meses.

**Por qué el 114% es engañoso aquí**

NRR alto + churn de logos alto es el patrón clásico de la expansión tapando una fuga estructural:

1. **La expansión tiene techo.** Cuando los que subieron de plan lleguen al plan máximo, ese motor se apaga y el churn queda desnudo.
2. **Concentración.** Menos clientes sosteniendo más ingresos cada uno: cada baja duele más.
3. **Base menguante.** Cada mes hay menos cuentas sobre las que expandir.
4. **Muestra pequeña.** Con 36 clientes, 2-3 upgrades mueven el NRR enormemente. Es una métrica volátil a este tamaño.

El contraste honesto sería tu GRR (retención bruta de ingresos, sin expansión): asumiendo que los que se fueron eran de tamaño medio, rondaría el 90% mensual. El GRR nunca supera el 100%, precisamente para que la fuga no se pueda maquillar.

**Sobre la estrategia**

Meter todo el esfuerzo en captación con 10% de churn mensual es pagar CAC por clientes con vida media de ~10 meses: escalas el desperdicio, no el negocio. Además, retención y expansión no compiten: cada cliente retenido es expansión futura.

Lo que haría:

- Medir logo churn, GRR y NRR **por separado** y por cohortes.
- Investigar por qué se fueron esos 4+ (entrevistas de salida, motivo de cancelación).
- Comprobar si se van los pequeños y expanden los grandes — aun así, 10% mensual es insostenible.
- Pisar el acelerador de captación cuando el churn mensual baje a niveles sanos (en SaaS SMB, por debajo del 2-3%).

La lectura menos halagadora pero correcta: tu panel no dice "no se me va nadie". Dice "los que quedan pagan más, pero se va uno de cada diez cada mes".