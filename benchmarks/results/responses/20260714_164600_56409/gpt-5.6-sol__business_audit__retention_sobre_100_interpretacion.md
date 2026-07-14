# GPT-5.6 Sol — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 6.74 | quality: 8.0
- latency_total: 20.96s | tokens_per_second: 30.5
- input_tokens: 128 | output_tokens: 640
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una interpretación completa y matizada de la retención de ingresos por encima del 100%.

## Respuesta completa

No. **“Retención de ingresos: 114%” probablemente se refiere a retención neta de ingresos (NRR)**, no a retención de clientes.

\[
NRR=\frac{\text{Ingresos iniciales} - \text{churn} - \text{contracciones} + \text{expansiones}}{\text{Ingresos iniciales}}
\]

Un 114% significa que, dentro de la cohorte existente, las subidas de plan compensaron las bajas y reducciones, y además añadieron un 14% neto. **No significa que casi ningún cliente se haya ido.**

En tu caso:

- Clientes el mes pasado: 40  
- Clientes este mes: 36  
- Si no captaste clientes nuevos, la retención de clientes fue:

\[
36/40=90\%
\]

Es decir, **10% de churn de clientes mensual**, una cifra importante aunque la NRR sea excelente. Si los 36 actuales incluyen clientes nuevos, la retención de la cohorte anterior sería incluso inferior al 90%.

Además, la **retención de clientes no puede superar el 100%**: los clientes nuevos cuentan como crecimiento/adquisición, no como retención.

### Qué deberías mirar por separado

- **NRR:** 114%; refleja churn, contracciones y expansión de ingresos.
- **Retención de clientes o logos:** porcentaje de clientes iniciales que siguen.
- **Churn de clientes:** porcentaje de clientes iniciales que se fueron.
- **Retención bruta de ingresos (GRR):** excluye las subidas de plan y muestra cuánto ingreso conservas antes de expansión.
- **Concentración:** si unos pocos clientes grandes están compensando muchas bajas pequeñas.

Por tanto, **no conviene dejar de preocuparte por el churn**. Tu expansión es buena, pero podría estar ocultando pérdida de clientes. La decisión adecuada no es dedicar “todo” a adquisición, sino determinar:

1. qué clientes se van y por qué;
2. cuánto ingreso representan;
3. si las subidas de plan son repetibles;
4. si retener clientes cuesta menos que reemplazarlos.

La lectura correcta sería: **“Tengo una expansión de ingresos fuerte, pero posiblemente un problema de retención de clientes.”**