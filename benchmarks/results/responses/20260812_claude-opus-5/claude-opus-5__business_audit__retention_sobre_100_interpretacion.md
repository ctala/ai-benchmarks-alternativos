# Claude Opus 5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 33.273s | tokens_per_second: 61.6
- input_tokens: 216 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## No, son dos cosas distintas

"Retención de ingresos" (normalmente **NRR**, *Net Revenue Retention*) mide euros, no clientes. Y es **neta**: suma las ampliaciones de plan y resta las bajas y bajadas de plan en el mismo número. Por eso puede superar el 100% mientras pierdes clientes — de hecho es exactamente lo que te está pasando.

**Tu retención de clientes (logo retention) es 36/40 = 90% mensual.** Es decir, un churn del 10% al mes.

Y ojo con un detalle importante: si esos 36 incluyen clientes nuevos captados este mes, tu churn real es peor. Si captaste 3 nuevos, perdiste 7 de los 40 originales → 82,5% de retención, 17,5% de churn mensual.

## Lo que significa un 10% mensual

- Anualizado: 0,9¹² ≈ **28%**. De cada 100 clientes, en un año te quedan 28.
- Vida media del cliente: ~10 meses.

Eso pone un techo duro al LTV y hace que casi cualquier CAC salga mal.

## Por qué el 114% está tapando el problema

Haz la cuenta con números redondos. 40 clientes a 100 €/mes = 4.000 € MRR. Pierdes 4 clientes medios: −400 €. Para llegar a 114% (4.560 €) necesitas:

`4.000 − 400 + expansión = 4.560` → **expansión = 960 €, un +24% sobre la base**

Es decir: unas pocas cuentas crecieron muchísimo y compensaron la fuga. Dos métricas que necesitas separar:

- **GRR** (retención bruta, sin contar ampliaciones): en este ejemplo, 90%. Nunca puede pasar de 100%. Es tu medida real de fuga.
- **NRR**: 114%. Mezcla dos dinámicas opuestas.

Tres razones para no relajarte:

1. **Concentración de riesgo.** Si ese +24% viene de una o dos cuentas, el día que una se vaya pasas de 114% a bastante por debajo de 100% de golpe. Y cuanto más se concentra el ingreso, más frágil es.
2. **La expansión tiene techo, el churn no.** Un cliente puede subir de plan un número finito de veces. Puede irse una vez, y ya está.
3. **Base bimodal.** Un 24% de expansión junto a un 10% de churn sugiere que tu producto encaja excelentemente con un perfil y mal con otro. Eso es información valiosísima sobre a quién deberías captar — y ahora mismo la estás promediando hasta hacerla invisible.

## Antes de decidir nada, comprueba

1. **¿Cómo define tu panel esa métrica?** Algunos incluyen clientes nuevos en el numerador, lo que la infla y la vuelve inútil como medida de retención. Búscalo.
2. **Calcula tu GRR real** con tus cifras, no con mi ejemplo. Los 4 que se fueron, ¿eran cuentas grandes o pequeñas?
3. **Concentración de la expansión:** ¿qué % del crecimiento viene de tu mayor cuenta? ¿Y de las tres mayores?
4. **Segmenta el churn.** ¿Qué tienen en común los 4 que se fueron (canal de captación, tamaño, caso de uso, tiempo de vida)? ¿Y los que ampliaron?
5. **NRR por cohorte de alta**, no agregado. El agregado esconde si las cohortes recientes retienen peor que las antiguas — que es la señal que de verdad import