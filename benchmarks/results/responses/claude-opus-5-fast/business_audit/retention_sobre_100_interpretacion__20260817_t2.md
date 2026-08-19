# Claude Opus 5 Fast — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 12.532s | tokens_per_second: 180.7
- input_tokens: 216 | output_tokens: 2264

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## Respuesta corta

No. Estás leyendo una métrica de **dinero** como si fuera una métrica de **personas**. Son cosas distintas y, en tu caso concreto, la de personas está mal.

Tus propios números lo dicen: pasaste de 40 a 36 clientes. Eso es **retención de logos del 90% mensual**, no del 114%. El 114% te dice que los que se quedaron gastan tanto más que compensaron con creces a los que se fueron. Es una buena noticia sobre tu producto, no una señal de que nadie se va.

## Qué está pasando por debajo

Con números redondos, si tenías 40 clientes a 100 €/mes = 4.000 € de MRR inicial:

| Concepto | Importe |
|---|---|
| MRR inicial | 4.000 € |
| Churn (4 clientes) | −400 € |
| **GRR (retención bruta)** | **3.600 € → 90%** |
| Expansión (upgrades) | +960 € |
| **NRR (retención neta)** | **4.560 € → 114%** |

Los 14 puntos por encima de 100 no significan "cero fuga". Significan "fuga del 10% tapada por una expansión del 24%". Son dos hechos separados y solo uno de ellos aparece en tu panel.

## Por qué esto importa más de lo que parece

**1. El 90% mensual compuesto es demoledor.** Si se mantiene, `0,9^12 ≈ 28%`. De cada 100 clientes que entren, en un año te quedan 28. Estás llenando un cubo agujereado, y la expansión de unos pocos te está ocultando el agujero.

**2. La expansión probablemente está concentrada.** Con 36 clientes, casi seguro que ese +960 € viene de dos o tres cuentas que subieron de plan. Si una de ellas se va el mes que viene, tu NRR se desploma por debajo de 100 de golpe. Un NRR de 114% sobre 36 clientes no es una tendencia, es una anécdota estadística.

**3. Es probable que estés perdiendo justo a quien te alimenta el futuro.** El patrón clásico: las cuentas pequeñas se van, las grandes crecen. El NRR sale precioso mientras se te seca la cantera de las cuentas grandes de dentro de dos años.

**4. Captar más gente empeora el problema, no lo arregla.** Si metes clientes nuevos en un producto del que se va el 10% al mes, estás pagando CAC para alimentar el churn. El coste de adquisición no se amortiza si la vida media del cliente es de diez meses.

## Dos cosas que verificar en el propio panel

- **¿El 114% incluye clientes nuevos?** Es el error de configuración más común. El NRR debe medir *solo* la cohorte que ya existía al inicio del periodo. Si tu herramienta está metiendo altas nuevas en el numerador, eso no es retención, es crecimiento de MRR disfrazado y el número no significa nada.
- **¿Los 36 de este mes incluyen altas?** Si captaste, digamos, 3 clientes nuevos, entonces no perdiste 4 sino 7 de los 40 originales. Tu churn real sería del 17,5% mensual, y el cuadro es bastante peor.

## Qué mirar a partir de ahora

Pon cuatro números juntos, nunca uno solo:

- **GRR** (nunca pasa de 100%) — mide la fuga real. Es tu número doloroso.
- **NRR** — mide fuga + expansión.
- **Churn de logos** — cuántos clientes, no cuántos euros.
- **Concentración de la expansión** — qué % del upside viene de tu mayor cuenta.

Y para las 4 bajas: llámalas. Con esos volúmenes, cuatro conversaciones te dan más señal que cualquier panel.

**En resumen:** el 114% dice que tu producto genera valor creciente en quien se queda. Eso es real y está bien. No dice absolutamente nada sobre si la gente se queda, y ahí tus datos apuntan a un problema serio. Arregla la retención antes de pisar el acelerador de captación.