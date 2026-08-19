# Claude Opus 5 Fast — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.64 | quality: 8.0
- latency_total: 15.79s | tokens_per_second: 192.9
- input_tokens: 262 | output_tokens: 3046

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa

## Primero: el 31% no es tu churn. Es un promedio de dos negocios distintos.

Estás mezclando dos poblaciones con comportamientos que no tienen nada que ver:

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33.7%** |
| De pago | 22 | 2 | **9.1%** |
| Mezclado (lo que ves) | 200 | 62 | 31% |

El 31% es aritméticamente correcto y estratégicamente inútil. Los usuarios gratuitos dominan el denominador (89% de tu base), así que la métrica mide casi exclusivamente el comportamiento de gente que nunca te pagó nada.

## Segundo: tu churn de pago tampoco es interpretable todavía

9.1% suena peor que el 5% que esperabas. Pero son **2 personas de 22**.

- Si se hubiera ido 1 en vez de 2: 4.5%
- Si se hubieran ido 3: 13.6%

El intervalo de confianza al 95% para 2/22 va aproximadamente de 2% a 28%. Con esa muestra no puedes distinguir estadísticamente un churn del 5% de uno del 15%. No tienes una señal de deterioro; tienes ruido de una base pequeña.

Esto no significa "todo bien". Significa **"no sabes todavía"**, que es una posición distinta y requiere acciones distintas al pánico.

## Tercero: la pregunta que nadie te hizo — ¿qué significa "baja" en el plan gratuito?

Antes de seguir, verifica cómo tu panel define la baja de un usuario gratuito:

- ¿Borró su cuenta activamente?
- ¿Lleva X días sin iniciar sesión y el sistema lo marca como inactivo?
- ¿Expiró un trial que se contabilizaba como "gratuito"?

Si es la tercera, tu 33.7% podría ser simplemente la cola de trials expirados, y no es churn en ningún sentido útil. Este detalle cambia todo el diagnóstico y toma diez minutos verificarlo.

## Los datos que te faltan (pídelos hoy)

**1. Serie histórica segmentada, 6-12 meses.** Un mes aislado no dice nada. Necesitas saber si el churn de pago viene de 4% → 6% → 9% (tendencia, preocúpate) o si oscila entre 0% y 9% desde siempre (base pequeña, ignora el mes).

**2. Composición de las altas del mes anterior.** Si tuviste un pico de registros gratuitos hace 30-60 días (lanzamiento, promoción, mención en algún medio), el 33.7% es esa cohorte drenándose. Es esperado, no es una fuga nueva.

**3. Churn de ingresos, no de logos.** ¿Qué planes tenían esos 2 clientes? Si eran tus dos cuentas más grandes, tu churn de ingresos puede ser 30%. Si eran los planes más baratos, puede ser 3%. Con 22 clientes, la varianza entre cuentas es enorme.

**4. Voluntario vs. involuntario.** ¿Cancelaron o les falló la tarjeta? El churn involuntario suele ser 20-40% del total y se arregla con reintentos de cobro y avisos de tarjeta por vencer. Es la reparación más barata que existe.

**5. Antigüedad de los que se fueron.** Dos clientes de 18 meses que se van es un problema de producto. Dos que se fueron en el mes 2 es un problema de onboarding.

## Plan

**Esta semana**
- Verifica la definición de "baja" para el plan gratuito.
- Separa las métricas en el panel de forma permanente. Nunca vuelvas a mirar el número mezclado.
- Escribe o llama a los 2 clientes que se fueron. Con n=2 no hay estadística posible, pero sí hay información cualitativa, y es la mejor que vas a conseguir. Pregunta qué pasó, no intentes recuperarlos en esa conversación.
- Revisa si fue fallo de pago. Si sí, activa dunning.

**Este mes**
- Reconstruye la serie histórica segmentada. Define tu línea base real de churn de pago.
- Define qué es un usuario gratuito "activo" y mide el churn solo sobre esa base. Un gratuito que se registró y nunca usó el producto no es un cliente que perdiste, es un registro que nunca convirtió — problema de activación, no de retención.
- Mide la tasa de conversión gratuito → pago. Ahí está probablemente tu verdadero cuello de botella.

**Reencuadre que probablemente necesitas**

Con 22 clientes de pago, el churn no es tu limitante principal. Aunque tuvieras 0% de churn, seguirías teniendo 22 clientes. La aritmética de tu crecimiento está dominada por la adquisición y la conversión, no por la retención. El churn se convierte en el problema central cuando tienes una base lo bastante grande para que las fugas superen las entradas — y para que la métrica sea estadísticamente legible.

Vigila el churn de pago mensualmente, con la serie completa a la vista y sin mezclarlo con nada. Pero no reorganices la hoja de ruta del producto alrededor de dos cancelaciones.

## Lo que cambiaría este diagnóstico

Si al reconstruir la serie histórica ves que el churn de pago subió consistentemente durante 3-4 meses, o si los 2 que se fueron representan más del 20% de tus ingresos, entonces sí hay algo real que atender y vale la pena una revisión más profunda. Cuéntame qué encuentras.