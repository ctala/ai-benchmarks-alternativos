# GPT-5.6 Terra Pro — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 30.255s | tokens_per_second: 182.8
- input_tokens: 7262 | output_tokens: 5532

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

No entres en pánico por el 31%: **esa cifra mezcla usuarios gratuitos y de pago**. Es correcta para “usuarios totales”, pero probablemente no responde a la pregunta de negocio que te preocupa: *¿estoy perdiendo clientes que pagan?*

## Qué está midiendo cada tasa

| Segmento | Usuarios al inicio | Bajas | Churn mensual |
|---|---:|---:|---:|
| Total | 200 | 62 | **31,0%** |
| Gratuito | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |

Cálculos:

- Churn total: `62 / 200 = 31%`
- Churn gratuito: `60 / 178 = 33,7%`
- Churn de pago: `2 / 22 = 9,1%`

## Qué tan grave es

### 1. El 31% no significa que hayas perdido el 31% de tu negocio de pago
El 31% está dominado por las bajas gratuitas: **60 de las 62 bajas (97%)** eran de free users.

Si tu prioridad es ingresos, el número relevante es inicialmente **9,1% de churn de clientes de pago**, no 31%.

### 2. El 9,1% merece atención, pero la muestra es muy pequeña
Con solo 22 clientes de pago:

- 1 baja equivale a **4,5 puntos porcentuales** de churn.
- 2 bajas = **9,1%**.
- Si hubieras tenido 1 baja, verías 4,5%, muy cerca de tu expectativa de 5%.

Es decir: pasar de “normal” a “alarmante” puede depender de **una sola cuenta**. No conviene concluir todavía que hay una crisis estructural basándote en un mes y dos cancelaciones.

Aun así, si tu referencia era 5%, este mes está por encima de ella y debes investigarlo.

## Primero: verifica que comparas la misma métrica

Tu “5% esperado” podría no ser comparable con el 31% del panel. Confirma estas definiciones:

1. **¿El 5% era churn de clientes de pago o de todos los usuarios?**
2. **¿Las “bajas” son cancelaciones voluntarias, cuentas eliminadas, o expiraciones por pago fallido?**
3. **¿El denominador son clientes activos al inicio del mes?**  
   Para churn mensual de clientes, normalmente sí.
4. **¿Mides cuentas, usuarios, seats o suscripciones?**
5. **¿Incluyes clientes anuales que cancelaron pero aún conservan acceso?**
6. **¿Hay usuarios gratuitos que se registran para probar y luego eliminan la cuenta?**  
   Eso es importante para producto/adquisición, pero no equivale automáticamente a churn de ingresos.

## Plan de acción

### Hoy: corrige la lectura del dashboard

Crea o pide estas métricas separadas:

1. **Churn de clientes de pago (logo churn)**  
   `Clientes de pago perdidos / clientes de pago al inicio`

2. **Churn de ingresos (gross revenue churn)**  
   `MRR perdido por bajas y downgrades / MRR inicial`

3. **Churn gratuito**  
   `Usuarios free que abandonan / usuarios free iniciales`

4. **Churn involuntario**  
   Pago fallido, tarjeta vencida, error de cobro, fraude, etc.

No uses una sola tasa de churn global para tomar decisiones de retención o salud de ingresos.

### Próximas 48 horas: investiga las 2 bajas de pago

Revisa individualmente las dos cuentas de pago:

- Plan y precio.
- MRR perdido.
- Antigüedad como cliente.
- Fuente de adquisición.
- Uso del producto antes de cancelar: frecuencia, usuarios activos, funcionalidades usadas.
- Evento previo a la baja: error, soporte, aumento de precio, renovación, pago fallido, falta de adopción.
- Motivo declarado de cancelación.
- Si eran clientes mensuales o anuales.

Clasifícalas en categorías simples:

- No obtuvo valor / baja activación.
- Falta de funcionalidad.
- Precio o presupuesto.
- Cambio a competidor.
- Problema técnico o soporte.
- Pago fallido.
- Cliente temporal / caso de uso terminado.

Esto te dirá si son dos casos aislados o una señal repetible.

### Esta semana: trata el churn free como un problema distinto

Un churn free de 33,7% puede ser normal o preocupante según tu modelo. No es necesariamente malo si la mayoría de esos usuarios:

- Nunca se activaron,
- Eran registros de baja intención,
- Usaron el producto una vez,
- O eliminaron una cuenta de prueba.

Pero sí es preocupante si los usuarios que **sí alcanzan activación** también se van.

Segmenta free users por comportamiento:

- Se registraron pero nunca completaron onboarding.
- Alcanzaron el “momento de valor”.
- Usaron el producto 1 vez vs. varias veces.
- Volvieron en semana 1, semana 2 y semana 4.
- Fuente de adquisición.
- Caso de uso o país/dispositivo, si aplica.

La pregunta útil no es solo “¿cuántos free se van?”, sino:  
**“¿Qué porcentaje de los usuarios activados se va, y por qué?”**

### Durante el próximo mes: construye una serie temporal

No tomes una decisión estructural con un solo mes y dos bajas pagas. Mira al menos 3–6 meses de:

- Clientes de pago al inicio.
- Nuevos clientes de pago.
- Clientes perdidos.
- Churn de clientes de pago.
- MRR inicial y MRR perdido.
- Expansión/downgrade, si existe.
- Churn por cohorte de alta.
- Churn por plan, canal de adquisición y antigüedad.

## Lectura ejecutiva

- **No tienes evidencia de un churn del 31% entre clientes de pago.**
- Tu churn de pago este mes es **9,1%: 2 de 22 clientes**.
- Está por encima de tu referencia de 5%, pero con una base tan pequeña una sola baja mueve mucho la métrica.
- El problema visible en los datos es sobre todo **abandono de usuarios gratuitos (33,7%)**, que debe analizarse como activación, calidad de adquisición u onboarding.
- Prioridad inmediata: entender las dos bajas pagas y separar en el panel churn de pago, churn de ingresos y abandono free.