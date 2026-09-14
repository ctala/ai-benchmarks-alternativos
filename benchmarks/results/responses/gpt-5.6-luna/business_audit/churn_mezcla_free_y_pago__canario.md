# GPT-5.6 Luna — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 15.575s | tokens_per_second: 107.8
- input_tokens: 165 | output_tokens: 1679

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

Respira: **no necesariamente tienes un churn de pago del 31%**. El panel está mezclando usuarios gratuitos y de pago.

### Qué está midiendo realmente

| Segmento | Base al inicio | Bajas | Churn |
|---|---:|---:|---:|
| Total | 200 | 62 | **31,0%** |
| Gratuito | 178 | 60 | **33,7%** |
| Pago | 22 | 2 | **9,1%** |

El 31% es correcto como **churn de usuarios totales**, calculado como:

> 62 bajas / 200 usuarios iniciales = 31%

Pero esa métrica está dominada por los usuarios gratuitos: representan el 89% de la base y 60 de las 62 bajas.

## ¿Qué tan grave es?

### Para el negocio de ingresos

El dato relevante probablemente es:

> **2 de 22 clientes de pago se dieron de baja: 9,1% mensual**

Eso es bastante más importante que el 31%, pero no equivale a que hayas perdido el 31% de los ingresos.

La gravedad depende de:

- El MRR o ARR de esos dos clientes.
- Si son clientes grandes o pequeños.
- Si el 5% era una meta de churn de pago mensual.
- Si las bajas son definitivas o simplemente cancelaciones de prueba, usuarios inactivos o cuentas gratuitas que nunca se activaron.
- Si este mes es estadísticamente representativo: con solo 22 clientes de pago, perder 2 produce un salto muy grande.

Si esperabas un 5% de churn de pago, 9,1% está por encima del objetivo, pero la diferencia es de **una baja adicional aproximadamente**. No tomaría decisiones drásticas con un solo mes y una base de 22 clientes.

### Para el producto y el embudo

El 33,7% de churn gratuito puede ser relevante si:

- Los gratuitos son una fuente de conversión a pago.
- Generan costes de infraestructura o soporte.
- El modelo depende de retener usuarios gratuitos.
- En realidad muchas “bajas” son usuarios que nunca terminaron el registro o eran cuentas duplicadas.

Pero no deberías presentarlo como churn comercial junto con clientes de pago.

# Plan de acción

## Hoy: validar que los datos sean comparables

Antes de interpretar nada, confirma:

1. **Definición de baja**
   - ¿Cancelación explícita?
   - ¿Expiración de una prueba?
   - ¿Cuenta eliminada?
   - ¿Usuario inactivo?
   - ¿Falló un pago?

2. **Denominador**
   - ¿Los 200 estaban activos al inicio del mes?
   - ¿Incluye cuentas creadas ese mismo mes?
   - ¿Incluye usuarios de prueba, cuentas internas o duplicadas?

3. **Estado del plan**
   - ¿El plan se asigna según el estado al inicio del mes o al momento de la baja?
   - ¿Alguno pasó de gratuito a pago o viceversa?

4. **Métrica del 5%**
   - ¿Era churn de usuarios?
   - ¿Churn de clientes de pago?
   - ¿Churn de ingresos/MRR?
   - ¿Churn mensual, trimestral o de una cohorte?

No compares el 31% con el 5% hasta comprobar que ambos miden la misma población y el mismo periodo.

## En las próximas 24–48 horas: analizar las dos bajas de pago

Para cada cliente de pago, revisa:

- MRR perdido.
- Antigüedad.
- Producto o funcionalidades utilizadas.
- Tickets de soporte y problemas recientes.
- Uso durante los últimos 30 días.
- Motivo declarado de cancelación.
- Si hubo intento fallido de cobro.
- Si existían señales de riesgo antes de la baja.

Contacta personalmente a esos dos clientes si todavía es posible. El objetivo no es solo recuperarlos, sino identificar si hay un patrón.

## En la próxima semana: separar el panel en métricas útiles

Como mínimo, crea estas métricas:

1. **Logo churn de pago**

   \[
   \text{clientes de pago dados de baja} \div \text{clientes de pago al inicio}
   \]

   En tu caso: **2 / 22 = 9,1%**.

2. **Revenue churn bruto**

   \[
   \text{MRR perdido por bajas} \div \text{MRR al inicio}
   \]

3. **Churn gratuito**

   Reportarlo aparte: **60 / 178 = 33,7%**.

4. **Churn por cohorte**

   Separar clientes nuevos, antiguos, por canal de adquisición, plan y tamaño.

5. **Bajas por motivo**

   Precio, falta de uso, producto, soporte, cambio de negocio, fallo de pago, prueba no convertida, etc.

6. **Retención de activación**

   Medir qué porcentaje de usuarios realiza la acción clave del producto y cómo cambia su probabilidad de convertirse o permanecer.

## Durante los próximos 30 días: actuar según la causa

- Si las bajas de pago fueron por **fallos de cobro**: configurar reintentos, avisos y recuperación automática.
- Si fueron por **falta de uso**: crear alertas de riesgo y campañas de activación antes de la cancelación.
- Si fueron por **funcionalidades o calidad**: priorizar las causas repetidas, no solicitudes aisladas.
- Si fueron por **precio**: probar downgrade, pausa o planes más pequeños antes de perder al cliente.
- Si el problema está en usuarios gratuitos: mejorar onboarding y activación, pero sin asumir que el churn gratuito implica pérdida de ingresos inmediata.

## Recomendación ejecutiva

Por ahora comunicaría internamente:

> “El 31% corresponde al churn agregado de todos los usuarios y está fuertemente influido por la base gratuita. El churn de clientes de pago fue 9,1%: 2 de 22. Es superior a nuestra referencia del 5%, pero la muestra es pequeña. Vamos a validar definiciones, revisar las dos bajas y medir también churn de MRR antes de concluir que existe un deterioro estructural.”

La prioridad no es entrar en pánico por el 31%, sino **corregir la segmentación del panel y entender esas dos bajas de pago**.