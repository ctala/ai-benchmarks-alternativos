# Grok 4.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `x-ai/grok-4.5`
- success: True  | final: 5.58 | quality: 6.0
- latency_total: 22.294s | tokens_per_second: 88.6
- input_tokens: 328 | output_tokens: 1975

## Respuesta completa

**No. Esa lectura es incorrecta y peligrosa.**

### Qué significa realmente “Retención de ingresos: 114%”
Eso es **Net Revenue Retention (NRR / Net Dollar Retention)**.  
Mide únicamente la evolución de los **ingresos de la cohorte de clientes que ya tenías el mes pasado**.  
Fórmula simplificada:

\[
NRR = \frac{\text{Ingresos de la cohorte anterior este mes (incluye expansiones, restando churn + downgrades)}}{\text{Ingresos de esa misma cohorte el mes pasado}}
\]

114 % significa que las **expansiones** (subidas de plan, upsells, cross-sells) de los clientes que se quedaron superaron en un 14 % neto las pérdidas por churn y downgrades.  
**No incluye clientes nuevos.**  
**No dice nada directo sobre cuántos clientes se quedan.**

### Lo que sí te dicen tus números
- Mes pasado: 40 clientes de pago  
- Este mes: 36 clientes de pago  

→ Has perdido **netos 4 clientes**. Tu **retención de logos (customer retention)** está claramente por debajo del 100 %.  
Aunque varios hayan subido de plan, eso solo explica por qué el NRR > 100 %; no borra el hecho de que se te están yendo clientes.

Por tanto:
- **No** “prácticamente no se te va nadie”.
- La retención de **clientes** no está por encima del 100 % (es imposible que lo esté de forma neta cuando el conteo baja).
- El churn de clientes **existe y es real**.

### ¿Puedes dejar de preocuparte por el churn y meter todo el esfuerzo en captación?
**No.**  
Un NRR del 114 % es una métrica excelente (muchas empresas top están en 110-130 %), pero esconde un problema:

- Cada logo que se va es un cliente que ya no puede expandirse en el futuro.
- Estás sustituyendo (o no) clientes que ya habías adquirido y onboardeado.
- Si la tasa de expansión se ralentiza o el churn de logos sigue, el NRR se derrumbará.
- El LTV se ve afectado negativamente por el logo churn aunque el NRR actual se vea bien.
- En la práctica, un NRR alto + logo churn elevado suele indicar que estás “exprimiendo” a los que se quedan mientras pierdes base.

### Qué deberías mirar además (y no confiar solo en el 114 %)
1. **Gross Revenue Retention (GRR)** → sin expansiones. Si está muy por debajo del 100 % (por ejemplo <90-95 %), el churn + downgrades son agresivos y las expansiones solo los están maquillando.
2. **Logo retention / Customer churn rate** mensual y de cohorte.
3. **Expansion rate** vs **churn + contraction rate** por separado.
4. Cuántos de los 36 son clientes netos nuevos vs cuántos de los 40 originales se quedaron.
5. Churn por cohorte y por segmento (los que más expanden suelen ser los más valiosos; si se te van los pequeños y se expanden los grandes, el riesgo de concentración crece).

### Resumen directo
- 114 % NRR = las expansiones están compensando (y superando) las pérdidas de revenue de la base existente. Buena noticia de corto plazo.
- 40 → 36 clientes = estás perdiendo clientes. Mala noticia.
- No puedes “dejar de preocuparte por el churn”. Tienes que atacar el logo churn **y** seguir impulsando expansiones. Meter todo el esfuerzo solo en captación mientras se te escapan clientes es la forma clásica de construir un cubo con agujeros.

Si quieres, dame los números de MRR del mes pasado de esos 40, el MRR actual de los que quedaron + expansiones, y cuántos clientes nuevos entraron realmente, y te desgloso GRR, NRR, logo retention y el impacto real del churn.