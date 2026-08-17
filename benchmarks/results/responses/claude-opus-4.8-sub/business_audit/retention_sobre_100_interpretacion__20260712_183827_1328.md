# Claude Opus 4.8 (suscripción) — business_audit/retention_sobre_100_interpretacion

- model_id: `claude-opus-4-8`
- success: True  | final: 6.07 | quality: 7.2
- latency_total: 56.898s | tokens_per_second: 52.3
- input_tokens: 4 | output_tokens: 2977

## Respuesta completa

## No. Y el propio dato que me diste lo desmiente

"Retención de ingresos: 114%" es **NRR** (Net Revenue Retention). No mide cuánta gente se queda: mide cuántos **dólares netos** quedan de la base anterior, después de sumar expansión. Son cosas distintas y ahí está la trampa.

Con tus números:

| Métrica | Cálculo | Resultado |
|---|---|---|
| Retención de clientes (logo) | 36 / 40 | **90%** → churn 10% mensual |
| GRR aprox. (sin expansión) | ~90% (menos downgrades si hubo) | **~90%** |
| NRR (lo que ve tu panel) | GRR + expansión | **114%** |

O sea: los upgrades te están aportando **~+24 puntos** que tapan una fuga de **~10 puntos**. El panel no dice "no se va nadie". Dice "los que se quedan pagan más de lo que se llevan los que se van".

## Por qué esto no es "puedo ignorar el churn"

**1. La asimetría.** La expansión tiene techo; el churn no tiene piso. Solo puedes subir de plan a alguien un número finito de veces, y el pool de clientes upgradeables se agota. El churn, en cambio, se repite todos los meses sobre lo que queda. Un NRR de 114% mensual anualizado sería 4,8x — nadie sostiene eso. Lo que sí se sostiene es el 10% de churn mensual: 0,9^12 = **te queda el 28% de la base en 12 meses**.

**2. El techo matemático de tu adquisición.** Con churn constante, el número de clientes converge a:

```
techo = altas por mes / tasa de churn
```

Si captas 4 al mes y churneas 10%, tu techo es **40 clientes**. Estás ahí. Puedes duplicar el esfuerzo de captación y solo mueves el techo a 80 — sigues pagando CAC eternamente para reponer una fuga estructural. Bajar el churn de 10% a 5% duplica el techo **sin gastar un peso más en adquisición**.

**3. Concentración de riesgo.** Con 36 clientes, ese 114% probablemente lo cargan 2-3 cuentas que subieron de plan. Si una de ellas se va el mes que viene, el número no baja a 100%: se desploma. Un NRR con n=36 es ruido estadístico, no una tendencia.

## Antes de decidir nada, verifica tres cosas

1. **¿Tu panel excluye clientes nuevos?** El NRR bien calculado solo mira la cohorte que ya existía al inicio del período. Si el dashboard mete altas nuevas en el numerador, eso no es NRR: es crecimiento de MRR disfrazado, y el número está inflado.
2. **¿Los 36 incluyen altas nuevas?** Si captaste 3 este mes y terminaste en 36, no perdiste 4: perdiste **7** (17,5% de churn). El neto miente.
3. **¿Quiénes se fueron?** Cuatro clientes de plan bajo no es lo mismo que cuatro de plan alto. Si los que se van son tus grandes, el 114% de este mes es un espejismo que se corrige solo el próximo.

## Qué medir de ahora en más

- **GRR** (gross revenue retention, tope 100%). Esta es tu métrica de fuga real. Es la que no puedes maquillar con expansión.
- **Retención de logos** por cohorte de alta (mes 1, mes 3, mes 6). Ahí ves si la fuga es de onboarding o de valor a largo plazo.
- **NRR** como tercera, no como primera. Es una métrica de salud de la expansión, no de la retención.

## Respuesta corta

No pares el trabajo de churn. Tienes un problema de retención (10% mensual) **enmascarado** por expansión, y estás sentado en tu techo de adquisición. Meter todo a captación con esa fuga abierta es pagar CAC para llenar un balde agujereado.

El orden correcto: **entiende por qué se fueron esos 4** (una llamada a cada uno, esta semana), tapa la fuga, y *después* aceleras adquisición. El mismo esfuerzo rinde el doble con el churn a la mitad.