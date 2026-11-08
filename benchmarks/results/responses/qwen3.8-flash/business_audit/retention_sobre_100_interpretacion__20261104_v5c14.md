# Qwen 3.8 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.77 | quality: 10.0
- latency_total: 67.175s | tokens_per_second: 115.2
- input_tokens: 181 | output_tokens: 7737

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. La lectura intuitiva es incorrecta.

Un **“Retención de ingresos: 114%”** casi nunca significa “no se me va nadie”. Normalmente es **Net Revenue Retention (NRR)**: mide el dinero recurrente que conservas **de los clientes que ya tenías al inicio**, incluyendo expansiones, downgrades y churn. Puede ser mayor que 100% aunque estés perdiendo clientes, siempre que los que se quedan suban de plan o gasten más.

## Qué te está diciendo realmente el 114%

La fórmula típica de NRR es:

\[
NRR = \frac{MRR_{inicio} - churn - downgrades + expansiones}{MRR_{inicio}}
\]

Si el resultado es **114%**, significa:

> Del MRR que tenías al inicio con esa cohorte de clientes, ahora tienes un 114% gracias a expansiones, compensando churn y/o downgrades.

No significa:

- que no hubo churn;
- que la retención de clientes sea 114%;
- que todos los clientes se quedaron;
- que el negocio sea estable solo por eso.

De hecho, **la retención de clientes por logos no puede ser “por encima del 100%” salvo que estés incluyendo nuevos clientes o reactivaciones**. Si incluyes nuevos, ya no es retención pura: es crecimiento.

---

## Tu contexto: 40 clientes el mes pasado, 36 este mes

Si estos 36 son el mismo grupo de clientes, sin nuevos, entonces:

\[
Logo\ retention = \frac{36}{40} = 90\%
\]

Es decir, **perdiste 4 clientes**, un **10% de churn mensual de logos**.

Eso es muy distinto de “prácticamente no se me va nadie”.

Y si además captaste nuevos clientes, el churn fue aún mayor. Por ejemplo:

- Empezaste con 40.
- Entraron 5 nuevos.
- Terminas con 36.

Entonces:

\[
Clientes\ perdidos = 40 + 5 - 36 = 9
\]

Churn de logos:

\[
\frac{9}{40} = 22.5\%
\]

En ese caso, el 114% de retención de ingresos podría estar escondiendo un problema serio de pérdida de clientes.

---

## Ejemplo simple para ver la trampa

Supongamos que el mes pasado tenías:

- 40 clientes.
- MRR inicial: 4.000 €.

Este mes:

- Se van 4 clientes pequeños: pierdes 400 € de MRR.
- Los 36 restantes siguen.
- Varios suben de plan: sumas 960 € de MRR por expansiones.

MRR final de esa cohorte:

\[
4.000 - 400 + 960 = 4.560
\]

NRR:

\[
\frac{4.560}{4.000} = 114\%
\]

Pero la retención de logos:

\[
\frac{36}{40} = 90\%
\]

Resultado:

- **NRR: 114%**
- **Logo retention: 90%**
- **Churn mensual: 10%**

Es decir: estás perdiendo clientes, pero los que se quedan están gastando más.

---

## Por qué esto puede ser una señal de alerta, no de tranquilidad

Un NRR superior al 100% puede ser excelente si:

- pierdes pocos logos;
- las expansiones son repetibles;
- los clientes que se quedan son cada vez más valiosos;
- no dependes de 1 o 2 subidas de plan enormes;
- el churn no está concentrado en clientes estratégicos.

Pero puede ser preocupante si:

- estás perdiendo clientes cada mes;
- el crecimiento de ingresos viene de pocos clientes que suben de plan;
- la base se concentra en menos cuentas;
- el churn es estructural;
- estás adquiriendo clientes nuevos para tapar fugas;
- las expansiones fueron puntuales, por subida de precios, pago anual o un upsell no recurrente.

En tu caso, si pasaste de 40 a 36 clientes en un mes, **no puedes dar por bueno el churn**. Con una base pequeña, 4 clientes son ruido, pero si es una tendencia, es una fuga importante.

Además, si el churn es del 10% mensual, anualizado sería brutal:

\[
0.90^{12} \approx 28.2\%
\]

Es decir, si ese ritmo se mantiene, solo conservarías aproximadamente un 28% de los logos iniciales tras un año.

---

## No confundas métricas

Estas son las que necesitas separar:

### 1. Retención de logos / clientes

\[
\frac{Clientes\ activos\ al\ final\ del\ periodo\ que\ ya\ eran\ clientes\ al\ inicio}{Clientes\ al\ inicio}
\]

Con 40 → 36 y sin nuevos: **90%**.

### 2. Gross Revenue Retention, GRR

Es el MRR conservado **sin contar expansiones**.

\[
GRR = \frac{MRR_{inicio} - churn - downgrades}{MRR_{inicio}}
\]

GRR nunca debería ser mayor que 100% si está bien calculado. Si tu panel dice “retención de ingresos 114%”, casi seguro no es GRR, es NRR.

### 3. Net Revenue Retention, NRR

Es GRR más expansiones.

\[
NRR = GRR + Expansiones
\]

Puede ser mayor que 100%.

### 4. New MRR / MRR de clientes nuevos

Esto no es retención. Es crecimiento por adquisición.

Si tu panel mete clientes nuevos dentro de la “retención de ingresos”, el número es engañoso. Debería llamarse crecimiento de MRR o revenue growth, no retención.

---

## ¿Puedes dejar de preocuparte por el churn y meter todo el esfuerzo en captar gente nueva?

No. Al contrario.

Con 40 → 36, el churn merece más atención, no menos.

Si metes todo el esfuerzo en captar nuevos clientes mientras pierdes logos, puedes estar haciendo esto:

- gastando CAC en clientes que no retienes;
- inflando el churn mensual;
- empeorando el LTV;
- aumentando la dependencia de expansiones no repetibles;
- creciendo con una base cada vez más concentrada;
- tapando un problema de producto, onboarding, soporte, pricing o fit.

Una regla razonable: **la adquisición amplifica la retención, no la sustituye**.

Si tu retención de logos es mala, más captación no arregla el problema. Solo acelera el consumo de caja.

---

## Qué deberías revisar en tu panel inmediatamente

Pide o calcula estas cifras para el mismo periodo:

1. **Clientes al inicio**: 40.
2. **Clientes retenidos del inicio**: ¿36? ¿incluye nuevos?
3. **Clientes nuevos**: ¿cuántos?
4. **Clientes perdidos**: ¿cuántos exactamente?
5. **MRR inicial de la cohorte**: no MRR total si entraron nuevos.
6. **Churn MRR**: cuánto dinero recurrente perdiste.
7. **Downgrade MRR**: cuánto bajó el MRR por clientes que redujeron plan.
8. **Expansion MRR**: cuánto subió por upgrades, cross-sells, add-ons o subida de precios.
9. **GRR**: retención bruta de ingresos.
10. **NRR**: retención neta de ingresos.
11. **Logo retention**: retención por número de clientes.
12. **Cuántos clientes expandieron**: no solo cuánto MRR.
13. **Si la expansión viene de 1 o 2 clientes grandes**: riesgo de concentración.
14. **Motivos de churn**: ¿competencia? ¿precio? ¿no uso? ¿onboarding? ¿soporte? ¿fit?

---

## Lectura correcta, menos halagadora

Tu panel probablemente te está diciendo:

> “De los ingresos recurrentes que ya tenías con los clientes actuales, hoy conservas un 114% gracias a que algunos subieron de plan, aunque puede haber clientes que se fueron o redujeron su gasto.”

No te está diciendo:

> “No se va nadie.”

Tampoco:

> “La retención de clientes está por encima del 100%.”

Si el número de clientes pasó de 40 a 36, la hipótesis más simple es que **sí se van clientes**.

---

## Recomendación práctica

No abandones la captación, pero no le metas “todo el esfuerzo” todavía.

Yo haría esto:

1. **Validar si el 40 → 36 incluye nuevos clientes**.  
   Si entraron nuevos, el churn real es mayor.

2. **Calcular logo retention mensual**.  
   Si es 90% mensual, es una señal de alarma.

3. **Calcular GRR**.  
   Si GRR está bajo y NRR está en 114% solo por expansiones, el modelo es frágil.

4. **Mirar la calidad de la expansión**.  
   ¿Subieron muchos clientes un poco, o solo dos clientes mucho?  
   ¿Es recurrente o fue pago anual / subida puntual?

5. **Entrevistar a los clientes que se fueron**.  
   Con 40 clientes, 4 entrevistas pueden enseñarte más que un dashboard.

6. **Mantener adquisición controlada**.  
   No frenes el crecimiento si tienes caja y PMF, pero no escales agresivamente sin entender por qué pierdes logos.

En resumen: **114% de retención de ingresos no significa que no tengas churn. Significa que, probablemente, las expansiones están compensando la pérdida de clientes o downgrades. Con 40 → 36, deberías preocuparte por el churn, no dejar de hacerlo.**