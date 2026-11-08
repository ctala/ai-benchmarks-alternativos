# Kimi K2.7 Code — business_audit/retention_sobre_100_interpretacion

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 55.355s | tokens_per_second: 47.9
- input_tokens: 160 | output_tokens: 2649

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No, no es correcto.** Un 114 % de retención de ingresos no significa que “no se te va nadie”, ni que puedas dejar de mirar el *churn*. Estás confundiendo dos métricas distintas:

| Métrica | Qué mide | Cálculo con tus datos | Techo |
|---|---|---|---|
| **Retención de logos/clientes** | Cuántos clientes conservas | 36 / 40 = **90 %** | 100 % |
| **Retención neta de ingresos (NRR)** | Cuánto ingreso conservas de la misma base, incluyendo upgrades | **114 %** | Puede superar 100 % |

### Por qué la NRR puede dar 114 % aunque hayas perdido clientes

La NRR incluye **ingresos de expansión**: clientes que subieron de plan y ahora pagan más. Si los que se quedan pagan lo suficiente de más, compensan —y superan— lo que dejaron de facturar los 4 clientes perdidos.

Con números sencillos: imagina que los 40 clientes pagaban $1 cada uno el mes pasado ($40 en total).

- Perdiste 4 clientes: -$4.
- Los 36 que quedan ahora pagan, en conjunto, $45,60 (114 % de $40).
- Eso significa que esos 36 expandieron su gasto en $9,60 sobre lo que ya pagaban.

Es decir, **perdiste el 10 % de tus clientes**, pero el 90 % restante aumentó su gasto lo suficiente como para que el ingreso total creciera un 14 %.

### ¿Por qué esto no es una señal de “todo bien”?

Una NRR > 100 % es buena noticia de expansión, pero combinada con una caída de 40 a 36 clientes indica lo siguiente:

1. **Tienes churn real.** El 10 % de tu base mensual se fue. Eso es una tasa que conviene entender, no ignorar.
2. **El crecimiento depende de que los que se quedan paguen más.** Si un día esos upgrades se frenan o se concentran en pocos clientes, la pérdida de clientes se hará visible de inmediato.
3. **Puede estar ocultando un problema de segmento.** Quizá estás reteniendo bien a los clientes grandes (que suben de plan) pero perdiendo a los pequeños, o viceversa. La NRR promedio no te dice eso.
4. **Captar clientes nuevos para rellenar una cubeta con agujero es caro.** Si no arreglas por qué se van 4 de cada 40, cada nuevo cliente cuesta más de lo necesario.

### Recomendación

No dejes de preocuparte por el *churn*. Haz esto:

- **Investiga quiénes se fueron y por qué.** Plan, tamaño, antigüedad, motivo de baja.
- **Separa NRR de GRR (retención bruta de ingresos).** La GRR solo mide ingreso retenido sin upgrades; en tu caso estaría en 90 % o menos. Si la brecha entre GRR y NRR es grande, tu negocio depende mucho de expansiones.
- **Sigue captando clientes**, pero también invierte en retener a los 36 que tienes y en entender por qué bajan 4 cada mes.
- **Mide ambas métricas mensualmente:** logos retenidos e ingreso neto retenido.

En resumen: **114 % de NRR es positivo, pero 90 % de retención de clientes es una señal de alerta que no deberías ignorar.**