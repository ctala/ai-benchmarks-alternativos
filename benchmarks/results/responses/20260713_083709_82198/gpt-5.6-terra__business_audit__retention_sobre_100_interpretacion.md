# GPT-5.6 Terra — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 7.03 | quality: 8.14
- latency_total: 11.205s | tokens_per_second: 90.4
- input_tokens: 128 | output_tokens: 1013

## Respuesta completa

No necesariamente. Ese **114% casi seguro es Retención Neta de Ingresos (NRR)**, no retención de clientes.

La NRR mide qué pasó con los ingresos de la base de clientes que ya tenías al inicio:

\[
\text{NRR} = \frac{\text{MRR inicial} - \text{churn} - \text{downgrades} + \text{expansiones}}{\text{MRR inicial}}
\]

Una NRR de 114% significa que, entre tus clientes iniciales, los upgrades y expansiones superaron las pérdidas por bajas y reducciones en un 14%.

Eso es bueno, pero **no significa que nadie se vaya**.

En tu caso:

- Pasaste de **40 a 36 clientes de pago**.
- Si no hubo clientes nuevos ni reactivados dentro de ese conteo, tu **retención de clientes/logos** fue:

\[
36 / 40 = 90\%
\]

Es decir: perdiste el 10% de tus cuentas, aunque el ingreso de las cuentas restantes haya crecido lo suficiente como para llevar la NRR a 114%.

Ejemplo simplificado:

- Empiezas con 40 clientes y €10.000 de MRR.
- Cuatro clientes cancelan y se llevan €1.500 de MRR.
- Los 36 restantes hacen upgrades por €2.900.
- Terminas con €11.400 de MRR de la cohorte inicial.

Resultado:

- **NRR:** 114%.
- **Retención de clientes:** 90%.
- Aun así, hubo cuatro cancelaciones.

Además, conviene mirar la **retención bruta de ingresos (GRR)**:

\[
\text{GRR} = \frac{\text{MRR inicial} - \text{churn} - \text{downgrades}}{\text{MRR inicial}}
\]

La GRR excluye expansiones y nunca debería superar el 100%. Es la métrica que revela cuánto ingreso se está perdiendo antes de que los upgrades lo compensen.

No conviene dejar de preocuparte por el churn solo porque la NRR sea alta. Una NRR de 114% puede esconder situaciones como:

- Los clientes grandes suben de plan mientras muchos pequeños cancelan.
- El crecimiento depende de pocos clientes con mucha capacidad de expansión.
- Estás perdiendo cuentas que podrían convertirse en clientes grandes más adelante.
- El coste de reemplazar clientes cancelados sigue siendo alto.

La lectura correcta es:

> Tienes una base con muy buena capacidad de expansión, pero también estás perdiendo clientes: ambas cosas son ciertas a la vez.

Priorizaría medir, como mínimo, en paralelo:

1. **NRR:** 114% — expansión neta de la base existente.
2. **GRR:** ingresos retenidos sin contar upgrades.
3. **Retención de logos:** clientes retenidos / clientes iniciales.
4. **Logo churn:** clientes perdidos / clientes iniciales.
5. **Churn por segmento y plan:** para saber si se van los clientes menos valiosos o si hay una señal de problema de producto, onboarding, precio o soporte.

Y revisaría la definición exacta del panel: si ese “114%” incluye ingresos de clientes nuevos, entonces no es NRR estándar y no sirve para evaluar retención de la misma forma.