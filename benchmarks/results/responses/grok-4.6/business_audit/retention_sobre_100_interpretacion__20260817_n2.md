# Grok 4.6 — business_audit/retention_sobre_100_interpretacion

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 38.385s | tokens_per_second: 48.6
- input_tokens: 328 | output_tokens: 1867

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No. La lectura correcta es menos halagadora: tienes churn de clientes real (al menos ~10 % mensual de logos) y la métrica del 114 % no lo niega.**

“Retención de ingresos: 114 %” es casi siempre **Net Revenue Retention (NRR)** de la base existente. Se calcula sobre el MRR/ARR de partida:

NRR = (MRR inicial + expansiones − contracciones − churn de ingresos) / MRR inicial

Puede superar el 100 % aunque se vayan clientes, siempre que los que se quedan (y suben de plan) generen más ingreso extra del que se pierde. Eso es exactamente lo que describes: 40 → 36 clientes de pago, pero varios upgrades. El ingreso neto de esa cohorte creció un 14 %. No significa que “prácticamente no se te va nadie”.

La **retención de clientes (logo retention)** no puede estar por encima del 100 % de forma sostenida. Aquí está en ~90 % (36/40). Perdiste al menos 4 clientes de pago. Si en el mes entraron clientes nuevos, el churn real de la base antigua es aún mayor.

### Por qué no puedes dejar de preocuparte por el churn
- Un cubo con fugas sigue siendo un cubo con fugas. El NRR alto es bueno (señala valor y capacidad de expansión en los que se quedan), pero 10 % de churn mensual de logos es muy alto. Anualizado (0,9¹²) deja una retención de cohortes de ~28 %. Eso destruye LTV, alarga el payback del CAC y limita el crecimiento compuesto.
- Los clientes que se van ya no pueden expandir más, no dan referencias y a menudo indican problemas de encaje, onboarding, valor percibido o segmentos que no deberías haber captado.
- El NRR >100 % puede enmascarar temporalmente el problema (sobre todo si unos pocos grandes suben mucho). Cuando se agoten las expansiones fáciles o cambie el mix, el crecimiento se frena.
- Distingue siempre NRR de GRR (Gross Revenue Retention). El GRR excluye expansiones y casi nunca supera el 100 %. Si tu panel solo muestra el 114 % y no el GRR ni la retención de logos, te está dando la versión más optimista.

No metas “todo el esfuerzo” solo en captación. Sigue adquiriendo, pero prioriza entender y reducir el churn de esos 4 (y de los que vengan): por qué se fueron, en qué segmento/plan/cohort, cuánto tiempo llevaban, si hubo downgrade previo, etc. Analiza cohortes, no solo el número agregado del mes. Un NRR alto con logo churn elevado es común en land-and-expand, pero no es una licencia para ignorar las fugas.

Si me das el GRR, el desglose de expansiones vs. churn de ingresos, o si esos 36 ya incluyen altas nuevas, se puede afinar más el diagnóstico.