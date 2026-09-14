# Fugu Max — business_audit/retention_sobre_100_interpretacion

- model_id: `sakana/fugu-max`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 16.906s | tokens_per_second: 67.0
- input_tokens: 201 | output_tokens: 1132

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **114% de retención de ingresos no significa 114% de retención de clientes**.

Probablemente ese dato sea la **retención neta de ingresos (NRR)**:

\[
\text{NRR}=\frac{\text{ingresos iniciales} - \text{churn} - \text{downgrades} + \text{expansiones}}{\text{ingresos iniciales}}
\]

Un 114% significa que, tomando **la misma cohorte de clientes que ya tenías al inicio**, ahora generas un 14% más de ingresos netos. Las subidas de plan pueden haber compensado —o más que compensado— las bajas.

Con tus clientes:

- Inicio: 40 clientes.
- Final: 36 clientes.
- Si no incorporaste ninguno nuevo, la retención de clientes sería **36/40 = 90%**, es decir, perdiste 4.
- Si incorporaste clientes nuevos, entonces perdiste más de 4. Por ejemplo, con 2 altas nuevas, habrías tenido 6 bajas y conservarías 34 de los 40 originales: **85% de retención de logos**.

Por tanto, el panel podría estar reflejando algo como esto:

- Se fueron varios clientes.
- Los que permanecieron ampliaron sus planes.
- La expansión superó los ingresos perdidos.
- Resultado: **NRR de 114%**, pero una retención de clientes inferior al 100%.

No dejaría de preocuparme por el churn. Deberías separar al menos estas métricas:

1. **Logo retention / retención de clientes**: qué porcentaje de clientes permanece.
2. **Logo churn**: qué porcentaje de clientes se va.
3. **GRR — Gross Revenue Retention**: ingresos retenidos sin contar ampliaciones.
4. **NRR**: incluye ampliaciones y reducciones.
5. **Expansion revenue**: cuánto crece el ingreso de los clientes existentes.
6. **Adquisición neta**: altas nuevas frente a bajas.

La lectura correcta sería: **tu base está expandiendo ingresos con éxito, pero está perdiendo clientes**. Eso puede ser sostenible si las ampliaciones son repetibles y los clientes que se van son pequeños, pero también puede ocultar una concentración peligrosa: unos pocos clientes grandes suben de plan mientras muchos clientes abandonan.

Así que no pondría todo el esfuerzo en captar nuevos clientes. Mantendría la captación, pero investigaría especialmente:

- quién se va y por qué;
- si el churn se concentra en un segmento o plan;
- la **GRR**, que mostrará mejor la pérdida real sin el efecto de las subidas;
- si el 114% procede de muchos clientes expandiéndose o de muy pocos.

En resumen: **114% de retención de ingresos es una buena señal de expansión, no una prueba de que el churn esté bajo**.