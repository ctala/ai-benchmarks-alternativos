# DeepSeek V4.1 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 27.044s | tokens_per_second: 176.7
- input_tokens: 206 | output_tokens: 4779

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

Respira: el 31% es probablemente una **métrica mezclada** y no el churn que te importa si tu negocio monetiza sobre todo el plan de pago.

## Diagnóstico rápido

| Segmento | Usuarios inicio | Bajas | Churn |
|---|---:|---:|---:|
| Total | 200 | 62 | **31,0%** |
| Gratuito | 178 | 60 | **33,7%** |
| Pago | 22 | 2 | **9,09%** |

El churn total es real: `62 / 200 = 31%`.  
Pero está dominado por el plan gratuito: **60 de 62 bajas (96,8%) son gratis**.

## ¿Qué tan grave es?

Depende de qué sea tu KPI real:

1. **Si tu KPI era churn de usuarios de pago:**  
   El churn de pago es `2 / 22 = 9,09%`.  
   Está por encima del 5% que esperabas, pero con solo 22 cuentas de pago es muy ruidoso.  
   Una sola baja mueve el churn ~4,5 puntos. Si el churn real fuera 5%, ver 2 o más bajas en 22 cuentas ocurre cerca del 30% de las veces. No es un colapso; es una señal para investigar.

2. **Si tu KPI era churn total:**  
   El 31% es alto, pero está arrastrado por el plan gratuito. Si los gratuitos son usuarios activos de tu producto, el `33,7%` de churn free puede ser un problema de producto o adquisición. Si son registros inactivos o limpieza de cuentas, no es churn de negocio.

3. **Impacto en ingresos:**  
   No lo sabemos. Hay que calcular **MRR perdido** de esas 2 cuentas de pago dividido por el MRR total al inicio. Dos cuentas pueden ser el 2% o el 20% de tus ingresos. Ese es el número que dirección debería mirar.

**Conclusión:** no es una catástrofe con los datos que das, pero tampoco lo ignores. El 31% no es churn de pago; el churn de pago es 9,1% con muestra pequeña. El free churn es 33,7% y puede ser el verdadero foco si esos usuarios te importan para crecimiento.

## Plan de acción

### Hoy / 0-2 horas
- Corrige la lectura del panel: no comuniques “31% de churn” como si fuera churn de pago.
- Calcula y separa:
  - Churn total de usuarios.
  - Churn de pago o *logo churn*.
  - Churn de ingresos: `MRR perdido / MRR inicio`.
  - Churn neto de ingresos: `(MRR perdido - expansión) / MRR inicio`.

### 24 horas
- Audita la definición de “baja”:
  - ¿Es cancelación voluntaria, borrado de cuenta, inactividad, expiración?
  - ¿El denominador son usuarios al inicio del mes o al cierre?
  - ¿Incluye altas nuevas del mismo mes?
  - ¿Hay cuentas internas, test o duplicadas?
- Revisa las 2 bajas de pago una por una:
  - Motivo declarado.
  - Antigüedad.
  - Plan y MRR.
  - Uso reciente.
  - Tickets de soporte.
  - ¿Fue churn voluntario o fallo de pago/dunning?

### 72 horas
- Segmenta el churn por:
  - Plan free vs pago.
  - Cohorte de alta.
  - Canal de adquisición.
  - País, dispositivo, uso.
  - Motivo de baja.
- Compara contra una ventana móvil de 3 meses, no solo contra un mes.
- Entrevista o intenta recuperar las 2 cuentas de pago. Con N=22, cada recuperación cambia mucho la métrica.

### 7 días
- Crea alertas separadas:
  - Churn de pago mensual.
  - Churn de ingresos neto.
  - Retención/activación de free.
  - Conversión free → pago.
- Implementa o revisa dunning para pagos fallidos.

### 30 días
- Si el problema es retención de pago:
  - Onboarding, health score, avisos de renovación, encuestas de salida, planes anuales, soporte proactivo.
- Si el problema es free:
  - Define si el free churn importa para adquisición/conversión.
  - Mejora activación temprana y hábitos de uso.
  - Limpia inactivos para que no contaminen el panel.

## Qué decir a dirección

> “El 31% es churn total de usuarios y está dominado por el plan gratuito: 60 de 62 bajas son free. El churn de pago es 2/22 = 9,1%, por encima del 5%, pero con solo 22 cuentas una baja mueve 4,5 puntos. Estamos calculando el impacto en MRR e investigando las 2 bajas de pago. No hay evidencia de colapso, pero sí de que el panel estaba mezclando poblaciones distintas.”

La frase clave: **no compares 31% total contra 5% de pago**. Separa free, pago e ingresos, y el problema se vuelve mucho más manejable.