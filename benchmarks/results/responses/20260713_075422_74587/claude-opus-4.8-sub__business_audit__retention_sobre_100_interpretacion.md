# Claude Opus 4.8 (suscripción) — business_audit/retention_sobre_100_interpretacion

- model_id: `claude-opus-4-8`
- success: True  | final: 5.17 | quality: 6.0
- latency_total: 71.735s | tokens_per_second: 56.8
- input_tokens: 4 | output_tokens: 4072

## Respuesta completa

## No. Estás leyendo una métrica de *ingresos* como si fuera una métrica de *clientes*.

Son dos cosas distintas, y en tu caso apuntan en direcciones opuestas.

**Ese 114% es Net Revenue Retention (NRR).** Mide dinero, no personas, y es una métrica *neta*: suma la expansión (upgrades) y le resta churn y downgrades, todo dentro de la cohorte de clientes que ya tenías. La expansión puede tapar el churn. En tu caso lo está tapando.

**Tu retención de clientes (logo retention) es 36/40 = 90%.** Eso es 10% de churn mensual. No es "prácticamente no se me va nadie": es que se te va 1 de cada 10 clientes al mes.

Y 10% mensual compuesto es brutal:
- `0.90^12 = 0.28` → de una cohorte de 100 clientes, en 12 meses te quedan ~28.
- Vida media del cliente = `1 / 0.10` = **10 meses**.

---

## Por qué ese 114% es más frágil de lo que parece

**1. La expansión tiene techo. El churn no.**
Un cliente puede subir de plan una o dos veces. Después se acabó — no hay tier al que escalar. El churn, en cambio, puede repetirse todos los meses indefinidamente. Estás financiando una fuga permanente con un ingreso que se agota.

**2. Mientras más alto el NRR por expansión, más concentrado el riesgo.**
Con 36 clientes, ese +14% neto lo están cargando unos pocos que subieron de plan. Si uno de esos se va el mes que viene, tu NRR no baja a 100%: se desploma. Estás construyendo el número sobre las cuentas más grandes, que son también las que más duelen cuando se van.

**3. La base que expande se está achicando.**
Los upgrades salen de clientes existentes. Si el stock de clientes cae mes a mes, el combustible de la expansión se acaba solo. Es una espiral que se ve bien en el dashboard hasta que deja de verse.

**4. n = 36. Estadísticamente, esto es una anécdota.**
Con esa muestra, un solo cliente mueve el NRR varios puntos. No tomes una decisión estratégica ("dejo de preocuparme por el churn") sobre un número que un accidente puede mover 10 puntos.

---

## Tres cosas que verificaría antes de mover nada

**a) ¿Ese 114% es NRR o es simplemente MRR de este mes / MRR del mes pasado?**
Muchos paneles etiquetan "retención de ingresos" a lo que en realidad es crecimiento de MRR — y ahí meten a los clientes *nuevos*. Si es eso, no es retención de nada: es un número que no dice absolutamente nada sobre tu fuga. Pista de diagnóstico: la **Gross Revenue Retention (GRR)** no puede pasar de 100% por definición (no incluye expansión). Si el panel muestra 114%, o es NRR o está mal calculado. Calcula tu **GRR**: te va a dar el tamaño real de la fuga, sin el maquillaje de los upgrades.

**b) ¿Hubo altas nuevas este mes?**
Dijiste 40 → 36. Si además entraron 3 clientes nuevos, entonces **se te fueron 7, no 4**. Tu churn real sería 17.5%, no 10%. El neto oculta el bruto. Necesitas el número de bajas, no la diferencia entre saldos.

**c) ¿Alguien pasó de mensual a anual?**
Si tienes plan anual, cómo se contabiliza en MRR distorsiona todo. Reconocer el pago anual completo en el mes del cobro infla el NRR de forma artificial. Debe normalizarse a mensual (anual / 12).

---

## Sobre "meter todo el esfuerzo en captar gente nueva"

Es exactamente la decisión que la lectura correcta desaconseja.

Con 10% de churn mensual, cada cliente nuevo que traes se te va en ~10 meses. Haz el cálculo de payback: si tu CAC tarda más de esos 10 meses en recuperarse, **la adquisición te está destruyendo dinero**, y escalarla solo acelera la pérdida. Antes de pisar el acelerador de captación, necesitas saber ese número.

Además, hay una asimetría de costo que suele ignorarse: retener y expandir es más barato que adquirir. Y expandir *requiere* que el cliente siga ahí. La retención no es una alternativa a la expansión — es su precondición.

**Lo que haría en tu lugar:**

1. Cuenta **bajas brutas**, no el delta de saldos. Es tu número real.
2. Calcula **GRR** y compárala con el 114%. La brecha entre ambas = cuánto te está maquillando la expansión.
3. Habla con los 4 (¿o 7?) que se fueron. Con esta muestra, la señal está en las entrevistas, no en el dashboard.
4. Mira **retención por cohorte**, no mes contra mes. ¿En qué mes de vida se caen? Si es en el 1-2, tienes un problema de onboarding/activación, no de producto.
5. Recién después: acelerar adquisición.

**La lectura honesta:** tienes una fuga de clientes seria, temporalmente compensada por un ingreso que no puede sostenerse. El 114% no te dice que estés bien; te dice que unos pocos clientes están pagando por los que se van.