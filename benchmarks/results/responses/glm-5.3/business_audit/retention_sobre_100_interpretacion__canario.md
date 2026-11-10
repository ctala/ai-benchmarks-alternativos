# GLM 5.3 — business_audit/retention_sobre_100_interpretacion

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 100.448s | tokens_per_second: 56.9
- input_tokens: 138 | output_tokens: 5718

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No — esa lectura tiene dos errores, y el segundo importa bastante.**

## Error 1: La retención de clientes no puede superar el 100%

De tus 40 clientes, hoy tienes 36: perdiste 4, un **10% en un solo mes**. "Prácticamente no se va nadie" no describe tus datos — se fue 1 de cada 10. Si ese ritmo se mantuviera, de una cohorte de hoy solo quedaría ~28% dentro de un año (0.9¹²).

## Error 2: El 114% es retención neta de *ingresos*, no de clientes

La fórmula del NRR:

> NRR = (MRR inicial + expansión − contracción − churn de ingresos) / MRR inicial

Ilustración con tus números (asumiendo ARPU de $100, base de $4.000):

- Churn: −4 clientes ≈ **−$400 (−10%)**
- Para terminar en 114% necesitas $4.560 → expansión ≈ **+$960 (+24%)**

Es decir: **+24% de expansión − 10% de churn ≈ 114%.** El indicador compuesto esconde ambos movimientos. El 114% no dice que no se vaya nadie; dice que *quienes se quedan pagan suficiente más para compensar a quienes se van*. (Los porcentajes exactos dependen del tamaño de los clientes que se fueron, pero la estructura es esta.)

Lo de los upgrades **sí es una buena señal real**: subida voluntaria de plan significa disposición a pagar y valor entregado. El problema es que la expansión está *enmascarando* la fuga, no cerrándola.

## Por qué "olvidarme del churn" es la conclusión peligrosa

- **El combustible de la expansión es finito.** Subir de plan suele ser un evento puntual por cliente. Cuando la ola de upgrades se complete, tu NRR convergerá hacia la retención bruta (~90%), y verás el agujero sin maquillaje. Un mes al 114% no es una tasa anualizable; probablemente es una ola.
- **10% de churn mensual ≈ vida media de 10 meses** (1/0.10). Si tu CAC payback supera eso, cada cliente nuevo destruye valor aunque el NRR sea 114%. Revisa esa cuenta antes de escalar adquisición.
- **Cuba agujereada:** necesitas ~4 clientes nuevos al mes solo para quedarte en 36, y los estás pagando con CAC.
- **Muestra pequeña:** con 40 clientes, dos upgrades grandes mueven el NRR varios puntos. Pide la serie de 3–6 meses antes de sacar conclusiones de tasa.

## Lo que haría antes de mover presupuesto

1. **Separa las tres métricas:** logo retention (90%), GRR (ingresos retenidos *sin* expansión, probablemente ~90%) y NRR (114%). Un panel que solo muestra NRR te cuenta media historia.
2. **Habla con los 4 que se fueron.** ¿Eran del plan de entrada? ¿Distinto perfil que los que subieron? Si el churn se concentra en mal fit y los upgraders son otro segmento, el diagnóstico no es "churn alto" sino "adquiero clientes equivocados" — y la solución es distinta.
3. **Compara el perfil de upgraders vs. churners.** Tu ICP real probablemente se parece más a los primeros.

## Veredicto

El NRR >100% es un activo genuino: significa que podrías crecer ingresos sin vender a nadie nuevo. Pero con 10% de churn de clientes mensual, "todo el esfuerzo a captación" es escalar el riego de una cuba con el fondo agujereado. La pregunta correcta no es *churn o adquisición*, sino **por qué se va el 10%** antes de multiplicar lo que pagas por traerlos.