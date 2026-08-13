# Muse Spark 1.2 — business_audit/retention_sobre_100_interpretacion

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 15.41s | tokens_per_second: 146.3
- input_tokens: 129 | output_tokens: 2255

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Esa lectura es incorrecta y es peligrosa si tomas decisiones con ella.

`Retención de Ingresos: 114%` no significa que no se te va nadie, y `Retención de Clientes` nunca puede estar por encima del 100%.

Te explico lo que realmente te está diciendo tu panel:

### 1. Estás confundiendo dos métricas distintas

**a) Retención de Clientes [Logo Retention]:** ¿Cuántos clientes se quedan?
> `Clientes retenidos / Clientes al inicio del periodo`

Tú mismo das el dato: Empezaste con 40 y terminaste con 36.
Incluso en el mejor caso, si no captaste ningún cliente nuevo este mes, retuviste a 36 de 40.

`Retención de Clientes = 36 / 40 = 90%`
`Churn de Clientes = 10%`

Te fuiste un 10% de tu base. Y si dentro de esos 36 hay algún cliente *nuevo* que captaste este mes, tu retención real es aún peor. Ejemplo: si de los 36, 2 son nuevos, solo retuviste 34 de los 40 originales = 85% de retención.

**b) Retención de Ingresos [Net Revenue Retention - NRR]:** ¿Cuánto dinero se queda + cuánto crece?

Es la que tu panel marca como 114% y se calcula así:

`NRR = (MRR Inicial - MRR perdido por churn - MRR perdido por bajadas de plan + MRR ganado por subidas de plan) / MRR Inicial * 100`

Que te dé 114% solo significa que **el dinero extra que te dejaron los que subieron de plan fue mayor que el dinero que perdiste por los 4 que se fueron.**

Ejemplo con números para que se vea:

* MRR Inicial: 40 clientes x 100€ = 4.000€
* Churn: 4 clientes se van = -400€
* Expansión: 6 clientes suben de 100€ a 180€ = +480€
* NRR = (4.000 - 400 + 480) / 4.000 = 4.560 / 4.000 = 114%

Sí, facturas más, pero perdiste clientes.

Para ver la salud real necesitas la otra cara: la **Retención Bruta de Ingresos [Gross Revenue Retention - GRR]**, que NO cuenta las subidas:

`GRR = (MRR Inicial - MRR perdido por churn y bajadas) / MRR Inicial * 100`

En el ejemplo anterior tu GRR sería del 90%. Nunca puede ser >100% y es la que te dice si tienes un agujero en el cubo.

### 2. ¿Puedes dejar de preocuparte por el churn y solo captar?

No. Al contrario. Un NRR de 114% con un churn de clientes del 10% mensual es una señal de alerta, no de tranquilidad.

Por tres razones:

1.  **Estás tapando un cubo con fugas.** La expansión tiene un límite. Un cliente solo puede subir de plan una o dos veces. El churn es infinito si no lo arreglas. Cuando se acabe el margen para hacer upsell, tu NRR caerá por debajo del 100% de golpe.

2.  **El churn de logo es carísimo.** Captar un cliente nuevo cuesta 5 a 7 veces más que retener uno [CAC]. Si pierdes 10% cada mes, necesitas captar 4 clientes solo para quedarte igual, antes de poder crecer. Estás pagando por rellenar lo que pierdes.

3.  **Es un sesgo de supervivencia.** Los que se quedan y pagan más te hacen ver un promedio bonito, pero no ves a los 4 que se fueron y por qué se fueron. Si ese 10% mensual se mantiene, en un año has perdido más del 70% de tu base original.

Un SaaS sano suele tener:
* GRR > 85-90%
* NRR > 100-110% 
Tú tienes lo segundo, pero lo primero lo tienes tocado.

### Qué hacer ahora en lugar de solo captar:

1.  Calcula tu GRR y tu Churn de Logo real del mes.
2.  Habla con esos 4 que se fueron. ¿Por qué se fueron? ¿Precio, falta de valor, competencia?
3.  Segmenta: ¿El churn viene de un plan pequeño? ¿De un tipo de cliente concreto? ¿Los que hacen upsell son del mismo perfil que los que se van?

Un NRR de 114% es excelente y significa que tu estrategia de expansión funciona. Pero no significa que retengas bien. Significa que, *por ahora*, los que se quedan te pagan lo suficiente para compensar a los que pierdes.