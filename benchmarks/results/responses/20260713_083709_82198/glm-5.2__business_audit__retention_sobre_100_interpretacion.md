# GLM 5.2 — business_audit/retention_sobre_100_interpretacion

- model_id: `z-ai/glm-5.2`
- success: True  | final: 7.26 | quality: 8.14
- latency_total: 28.557s | tokens_per_second: 56.8
- input_tokens: 138 | output_tokens: 1622

## Respuesta completa

No. Tu interpretación es incorrecta y, aunque ese 114% es un indicador excelente, no significa que puedas dejar de preocuparte por el *churn*. Te explico por qué la lectura intuitiva es engañosa en este caso:

**1. Retención de ingresos (NDR) vs. Retención de clientes**
El 114% se refiere a la **Retención Neta de Ingresos (Net Dollar Retention o NDR)**. Significa que el dinero extra que pagaron los clientes que subieron de plan (expansión) fue tan grande que no solo compensó el ingreso que perdiste por los que se dieron de baja, sino que dejó tu facturación un 14% por encima del mes anterior. Es una métrica de monetización fantástica.

Sin embargo, tu **retención de clientes** no está por encima del 100%; está en el **90%**. Pasaste de 40 a 36 clientes. Estás perdiendo un **10% de tu base de usuarios mensual**, lo cual es una tasa de *churn* de clientes bastante alta para un SaaS.

**2. El peligro de la expansión enmascarada**
El NDR del 114% te está dando una falsa sensación de seguridad. Lo que realmente está ocurriendo es que tienes un motor de *upsell* muy potente que está tapando una "cubeta con fugas". Los clientes que se quedan pagan más, pero te estás quedando sin clientes. 

Si decides ignorar el *churn* y meter todo el esfuerzo en captación nueva, enfrentarás dos problemas:
*   **Dilución del NDR:** Tu NDR se calcula sobre la cohorte existente. Si sigues perdiendo un 10% de clientes al mes, la base sobre la que puedes hacer *upsell* se reducirá hasta el punto en que las subidas de plan ya no podrán compensar a los que se van. Ese 114% caerá drásticamente.
*   **Ineficiencia de capital:** Adquirir un cliente nuevo (CAC) es mucho más caro que retener uno existente o hacerle un *upsell*. Si el 10% de tus recién llegados se va al mes siguiente, estarás quemando dinero en captación sin construir valor a largo plazo.

**3. Lo que debes hacer ahora**
No puedes dejar de preocuparte por el *churn*, pero tampoco debes frenar la captación. Tu prioridad inmediata debe ser el análisis de cohortes:
*   **¿Quiénes son los 4 clientes que se fueron?** ¿Eran clientes de plan básico? ¿Eran usuarios nuevos (churn temprano) o llevaban tiempo contigo?
*   **¿Quiénes subieron de plan?** ¿Son los clientes grandes/maduros?

El escenario ideal es aquel donde mantienes a tus clientes (retención >95%) y además logras que un porcentaje de ellos suba de plan. Tienes la segunda parte resuelta, pero necesitas arreglar la primera antes de que la base de clientes se agote.