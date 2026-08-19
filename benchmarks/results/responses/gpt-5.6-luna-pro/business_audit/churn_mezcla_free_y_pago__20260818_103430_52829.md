# GPT-5.6 Luna Pro — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 21.352s | tokens_per_second: 248.8
- input_tokens: 6963 | output_tokens: 5312

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

Primero: **no entres en pánico**. El 31% no necesariamente significa que hayas perdido el 31% de tus clientes de pago.

## Qué está midiendo realmente el 31%

El panel está calculando:

\[
62 \text{ bajas} / 200 \text{ usuarios iniciales} = 31\%
\]

Pero mezcla usuarios gratuitos y de pago:

| Segmento | Usuarios iniciales | Bajas | Churn |
|---|---:|---:|---:|
| Gratuito | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |
| Total | 200 | 62 | **31,0%** |

La cifra total está dominada por el plan gratuito: representa el 89% de tu base y el 97% de las bajas.

### Lectura preliminar

- **Churn de usuarios totales:** 31%.
- **Churn gratuito:** 33,7%. Es alto, pero puede incluir cuentas poco activas, registros de prueba o usuarios sin valor económico.
- **Churn de pago:** 9,1%. Es la métrica más relevante para ingresos, aunque solo tienes 22 usuarios, por lo que dos bajas producen una variación grande.
- **Churn de ingresos:** todavía no se puede calcular. Necesitas saber cuánto MRR representaban esos dos clientes.

Si tu expectativa del 5% se refería al **churn de clientes de pago**, la situación es peor que lo esperado, pero no es comparable directamente con el 31% del panel. Si el 5% era una cifra de usuarios totales, entonces hay un problema claro de retención o de definición de métricas.

## Qué haría ahora

### 1. Validar la definición antes de tomar decisiones

Confirma estas preguntas:

1. ¿“Baja” significa cancelación, eliminación de cuenta, inactividad o vencimiento?
2. ¿Los 200 eran usuarios activos al inicio del mes o todas las cuentas existentes?
3. ¿Se cuentan pruebas gratuitas que terminan naturalmente?
4. ¿Un usuario que pasa de pago a gratuito aparece como baja?
5. ¿La métrica se basa en usuarios, cuentas, suscripciones o ingresos?
6. ¿Se están mezclando eventos ocurridos este mes con cohortes de altas de meses anteriores?

Crea un pequeño diccionario de métricas. Por ejemplo:

- **Logo churn de pago:** clientes de pago al inicio que cancelaron durante el mes / clientes de pago al inicio.
- **Revenue churn:** MRR perdido por cancelaciones y downgrades / MRR al inicio.
- **Free churn:** cuentas gratuitas que se desactivaron o dejaron de estar activas / cuentas gratuitas activas al inicio.

### 2. Separar el panel inmediatamente

Como mínimo, muestra por separado:

- Usuarios gratuitos.
- Usuarios de pago.
- Churn de clientes de pago.
- Churn de ingresos.
- Nuevos clientes, expansiones y reactivaciones.
- Cancelaciones voluntarias frente a fallos de cobro.
- Churn por cohorte de alta.

No uses el 31% como indicador principal de salud del negocio si los usuarios gratuitos no generan ingresos.

### 3. Investigar las dos bajas de pago

Con solo dos casos, haz entrevistas o revisiones individuales. Para cada cliente, averigua:

- Fecha de alta y tiempo hasta la baja.
- Plan y MRR.
- Uso durante los últimos 30 días.
- Funciones utilizadas.
- Tickets o problemas recientes.
- Motivo declarado de cancelación.
- Si se fue a un competidor o simplemente dejó de necesitar el producto.
- Si hubo un fallo de cobro.

Dos clientes pueden esconder causas completamente distintas. No generalices a partir de una muestra tan pequeña.

### 4. Analizar las 60 bajas gratuitas

Aquí el objetivo no es necesariamente “evitar todas las bajas”. Primero segmenta:

- Usuarios de prueba frente a usuarios gratuitos permanentes.
- Usuarios activados frente a usuarios que nunca completaron el onboarding.
- Usuarios con uso reciente frente a cuentas inactivas.
- Fuente de adquisición.
- Fecha de registro.
- Funcionalidad alcanzada o no alcanzada.

Si la mayoría nunca llegó al momento de valor, el problema puede ser de **activación y adquisición**, no de retención.

### 5. Revisar el tamaño de la base de pago

Dos bajas sobre 22 clientes equivalen a 9,1%, pero la incertidumbre es alta. No declares todavía que el churn “real” es exactamente 9,1%. Con una base tan pequeña, un solo cliente cambia la tasa de forma importante:

- 1 baja: 4,5%.
- 2 bajas: 9,1%.
- 3 bajas: 13,6%.

Por eso conviene observar una media móvil de tres a seis meses y reportar también el número absoluto de bajas.

## Plan práctico

### Hoy

- Congelar cualquier conclusión basada en el 31%.
- Verificar las definiciones y los denominadores.
- Identificar a los dos clientes de pago perdidos.
- Calcular el MRR perdido.
- Separar cancelaciones, downgrades, fallos de pago y cuentas gratuitas.

### Esta semana

- Contactar a los dos clientes de pago.
- Revisar sus sesiones, uso, tickets y eventos previos.
- Clasificar las 60 bajas gratuitas por tipo y cohorte.
- Construir un panel segmentado.
- Comparar la métrica actual con el 5% usando exactamente la misma definición y ventana temporal.

### Próximos 30 días

- Mejorar el onboarding hacia el primer momento de valor.
- Configurar alertas de riesgo para clientes de pago con caída de uso.
- Añadir una encuesta de cancelación, sin usarla como única fuente de verdad.
- Implementar recuperación de pagos fallidos.
- Contactar proactivamente a clientes de pago con baja adopción.
- Medir mensualmente logo churn, revenue churn, activación y retención por cohorte.

## Conclusión

La cifra de **31% es real como churn agregado de usuarios**, pero está siendo impulsada casi completamente por el plan gratuito. La cifra más importante para el negocio es actualmente **2 bajas de 22 clientes de pago**, equivalente a **9,1%**, junto con el MRR que esas bajas representan.

La prioridad no es reaccionar a ciegas, sino responder estas dos preguntas:

1. **¿Las 60 bajas gratuitas son pérdida real o limpieza de cuentas de bajo valor?**
2. **¿Por qué se fueron esos dos clientes de pago y cuánto ingreso representan?**

Hasta responderlas, el diagnóstico correcto es: **hay una alerta de retención, pero el 31% probablemente está sobredimensionando la gravedad económica del problema**.