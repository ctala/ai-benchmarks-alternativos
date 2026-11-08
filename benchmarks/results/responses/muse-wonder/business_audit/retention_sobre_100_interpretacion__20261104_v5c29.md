# Muse Wonder — business_audit/retention_sobre_100_interpretacion

- model_id: `meta/muse-wonder`
- success: True  | final: 8.17 | quality: 10.0
- latency_total: 19.374s | tokens_per_second: 92.8
- input_tokens: 144 | output_tokens: 1797

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Y en tu caso, ese 114% está escondiendo un problema de churn importante.

Estás mezclando dos métricas distintas:

### 1. Retención de clientes (logo retention)
Es qué porcentaje de clientes se queda.

Esta **nunca puede superar el 100%**, porque no puedes retener a más clientes de los que tenías.

En tu caso:

- Mes pasado: 40 clientes
- Este mes: 36 clientes

Si no entró ningún cliente nuevo, tu retención de clientes es como máximo:

**36 / 40 = 90%**

Es decir, **10% de churn mensual de clientes**.

Y si entre esos 36 hay clientes nuevos, tu retención real es todavía menor. Por ejemplo, si entraron 3 nuevos, solo conservaste a 33 de los 40 originales: 82,5% de retención.

Un 10% mensual no es "prácticamente no se me va nadie". Compuesto en el tiempo, 0,90^12 = 28,2%. Manteniendo ese ritmo, en un año te quedaría menos de un tercio de la base inicial.

### 2. Retención de ingresos (Net Revenue Retention, NRR)
Es qué pasa con los **ingresos de los clientes que ya tenías**, incluyendo subidas de plan, más usuarios, add-ons, etc.

Esta sí puede superar el 100%, porque un mismo cliente puede pagar más que antes.

Fórmula simplificada:

**NRR = (MRR inicial - ingresos perdidos por bajas - rebajas + expansión) / MRR inicial**

Ejemplo compatible con tu 114%:

- 40 clientes pagando 100 € = 4.000 € MRR
- Pierdes 4 clientes: -400 €
- Varios de los que quedan suben de plan: +960 € de expansión
- Resultado: 4.560 € de esa cohorte

4.560 / 4.000 = **114% NRR**

Lectura correcta: "Los clientes que se quedaron gastaron lo suficiente para compensar a los que se fueron, y un 14% más".

Lectura incorrecta: "No se va nadie".

### Por qué no debes dejar de preocuparte por el churn

Porque la expansión tiene límites y concentra el riesgo:

1. **Los que quedan no pueden subir de plan infinitamente.**
2. **Cada vez dependes de menos clientes.** Ahora tus ingresos dependen de 36 cuentas, no de 40. Si mañana se va uno de los que expandió, el golpe es mayor.
3. **Captar sobre una base que se vacía es carísimo.** Con un 10% de churn mensual, necesitas captar más del 10% de tu base cada mes solo para no decrecer en número de clientes.

Además, revisa cómo calcula tu panel ese 114%. La NRR verdadera **excluye a los clientes nuevos** del periodo. Si los incluye, no es retención, es simplemente crecimiento de ingresos, y es aún menos informativa sobre el churn.

### Lo que deberías mirar a partir de ahora

Separa estas tres métricas:

- **Logo Retention / Logo Churn:** ¿cuántos clientes se van?
- **Gross Revenue Retention (GRR):** ingresos retenidos sin contar expansión. Esta nunca supera el 100% y te muestra el daño real de bajas y rebajas.
- **Net Revenue Retention (NRR):** tu 114%. Útil para ver expansión, pero nunca sola.

Conclusión menos halagadora pero precisa: tienes una señal positiva de expansión en los supervivientes, y simultáneamente una señal de alarma en retención de clientes. No metas todo en captación. Primero averigua por qué se fueron esos 4 —o más, si hubo altas nuevas— porque son la fuga que el 114% está tapando.