# Kimi K2.6 — business_audit/retention_sobre_100_interpretacion

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 32.25s | tokens_per_second: 71.9
- input_tokens: 161 | output_tokens: 2319

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

 **No. Esa lectura es incorrecta y, si actúas sobre ella, te expones a un problema serio.**

El 114 % que ves es **Retención Neta de Ingresos** (Net Revenue Retention, NRR), no retención de clientes. Son métricas distintas y una puede ocultar a la otra. Veamos los números con precisión:

### Lo que realmente está pasando
- **Retención de clientes (Logo Retention):** 36 / 40 = **90 %**.  
  Te fuiste **1 de cada 10 clientes** en un solo mes. Eso es un churn mensual del 10 %, que anualizado te dejaría una retención de clientes cercana al 28 % (es decir, perderías casi tres cuartas partes de tu base en un año). Eso es una hemorragia, no una fuga menor.
- **Retención de ingresos (NRR): 114 %.**  
  Los 36 clientes que se quedaron gastan, en conjunto, un 14 % más que lo que gastaban los 40 originales. Los upgrades (upsell) de algunos compensaron con creces la pérdida de los 4 que cancelaron.

### Por qué no puedes "dejar de preocuparte por el churn"

1. **La expansión tiene techo.** Puedes subir de plan a un cliente solo hasta cierto punto. Si sigues perdiendo 1 de cada 10 logos mensualmente, tarde o temprano no habrá suficientes upgrades que tapen el agujero.
2. **Dependencia creciente.** Cada vez tienes menos clientes sobre los que aplicar expansión. Pasaste de 40 a 36. Si el ciclo se repite, dependerás de una base cada vez más pequeña y, probablemente, más concentrada en pocos cuentas grandes.
3. **Señal de fondo.** Un churn del 10 % mensual de logos sugiere un problema de ajuste producto-mercado, onboarding o soporte. Los upgrades de los que se quedaron no eliminan esa señal; solo la maquillan financieramente.
4. **Coste de reposición.** Captar 4 clientes nuevos para reemplazar a los que te fuiste cuesta significativamente más (CAC) que haber retenido a los que ya habías conquistado.

### Lo que deberías hacer ahora

No desvíes "todo el esfuerzo" a captación. Divide tu atención:

1. **Calcula tu Gross Revenue Retention (GRR):** cuántos ingresos de los 40 originales conservaste *sin contar* upgrades. Si los 4 clientes perdidos eran de planes medianos, tu GRR probablemente esté entre 85 % y 95 %. Si baja de 85 %, tienes un problema estructural grave.
2. **Analiza el *quién*:** ¿Se fueron 4 clientes pequeños y los 36 restantes son enterprise que subieron de plan? O ¿se fueron 4 cuentas clave y los upgrades vinieron de un par de clientes grandes? La concentración importa.
3. **Investiga el *porqué*:** Entrevista o encuesta a los 4 que se fueron (y a los 36 que se quedaron). Un NRR del 114 % con un churn del 10 % mensual suele indicar que tu producto funciona muy bien para un segmento y muy mal para otro.
4. **Equilibra el pipeline:** Sí, captar clientes nuevos es necesario para reponer los 4 logos, pero tu prioridad inmediata debería ser **detener la sangría** antes de escalar adquisición. De lo contrario, estarás llenando un balde con un agujero creciente.

**Conclusión:** Un NRR del 114 % es financieramente positivo y muestra que tu mecanismo de expansión funciona, pero **no significa que "no se te va nadie"**. Se te va mucha gente. La métrica te dice que, por ahora, los que se quedan pagan más; no que tu negocio sea sano a largo plazo. Corrige el churn antes de apostar todo al crecimiento.