# Claude Opus 5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 52.156s | tokens_per_second: 54.8
- input_tokens: 216 | output_tokens: 2860

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## Respuesta corta: no. Estás leyendo una métrica de dinero como si fuera una métrica de clientes.

"Retención de ingresos" al 114% casi con seguridad es **NRR (Net Revenue Retention)**: ingresos de la cohorte inicial al final del periodo ÷ ingresos de esa cohorte al inicio, incluyendo expansión (upgrades, más asientos, uso) y restando contracción y churn.

La clave: **la expansión y el churn se suman en el mismo número y se cancelan entre sí**. Un 114% no significa "no se va nadie"; significa "lo que subieron algunos superó lo que perdí por los que se fueron". Son dos fuerzas independientes escondidas en un solo dato.

## Tus propios números lo delatan

- 40 → 36 clientes = **90% de retención de logos en un mes**, es decir ~10% de churn mensual.
- Compuesto: 0,90^12 ≈ **28%**. De cada 100 clientes, en un año te quedan ~28. Churn anual de logos ~72%.
- ARPA: pasó de R/40 a 1,14R/36, o sea **+27% de ingreso medio por cuenta**.

Referencia gruesa: SaaS SMB sano ronda 3-5% de churn mensual de logos; mid-market/enterprise, por debajo de 1-2%. Estás claramente por encima.

⚠️ **Y probablemente sea peor de lo que parece.** El "36" puede ser neto de nuevas altas. Si este mes captaste 3 clientes, no perdiste 4 de 40: perdiste 7 (17,5% de churn). Necesitas separar bajas de altas antes de sacar conclusiones.

## Qué te está pasando realmente

Tienes un producto que **encanta a un subconjunto de cuentas** (suben de plan) y **no retiene al resto**. Eso no es un problema resuelto, son dos problemas: uno bueno y uno grave.

Los riesgos concretos de tratar el 114% como luz verde:

1. **Concentración.** Con solo 36 cuentas, ese +14% probablemente viene de 2-4 upgrades. Si una de esas cuentas se va el mes que viene, tu NRR se hunde por debajo de 100% de golpe. Estás apoyado en muy pocos pilares.
2. **La expansión es un escalón, el churn es una corriente.** Un cliente puede pasar de plan básico a pro una vez, o dos. Hay techo. El churn no tiene techo: se repite cada mes sobre una base cada vez mayor.
3. **El cubo agujereado.** Si aceleras captación con 10% de fuga mensual, el churn escala contigo. Con 100 clientes perderás ~10 al mes: necesitarás captar 10 solo para no moverte. El CAC se convierte en un coste de reposición, no de crecimiento.
4. **Puede que estés captando justo lo que se te cae.** Si los que se van son los pequeños y tu marketing sigue apuntando a pequeños, estás pagando por llenar el agujero.

## Las métricas que sí te faltan

- **GRR (Gross Revenue Retention)**: igual que NRR pero **sin contar expansión**. Tope 100%. Este es tu número de fugas real. Con 114% de NRR y este churn de logos, tu GRR podría estar en 80-88%; a nivel mensual eso es alarmante. **Pide o calcula este dato antes que nada.**
- **Churn de logos vs. churn de ingresos**, separados y sin netear con altas nuevas.
- **Retención por cohorte** (clientes que entraron en enero, febrero...): te dice si el problema mejora con las últimas cohortes o es estructural.
- **Retención por segmento/plan**: para saber si la fuga está concentrada en un tipo de cliente.
- **Ventana temporal del 114%**: ¿es mensual o anual? Un 114% mensual implicaría 1,14^12 ≈ 4,8x anual, poco creíble de forma sostenida. Confirma qué está midiendo el panel exactamente.

## Qué haría yo

**No** ponerlo todo en captación. Un orden razonable:

1. Averiguar por qué se fueron esos 4-7. Con esos volúmenes son llamadas o emails, no un estudio: en una tarde tienes las razones.
2. Mirar si hay patrón: mismo plan, mismo canal de adquisición, mismo tiempo de vida (¿se van en el mes 1? Entonces es onboarding u expectativas de venta, no producto).
3. Decidir explícitamente si ese segmento es tu cliente. Si concluyes que no lo es, perderlos es sano —pero entonces cambia el targeting de captación en consecuencia y mídelo como tal, no como churn accidental.
4. Solo entonces pisar el acelerador de adquisición, sabiendo qué perfil retiene.

**Resumen:** el 114% dice que tu monetización de los clientes que se quedan es buena. No dice nada bueno sobre tu capacidad de quedártelos. Con 90% de retención de logos mensual, el churn es tu problema número uno, y el 114% lo está tapando.