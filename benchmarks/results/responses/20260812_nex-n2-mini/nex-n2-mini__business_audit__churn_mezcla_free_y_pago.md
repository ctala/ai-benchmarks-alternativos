# Nex-N2-Mini — business_audit/churn_mezcla_free_y_pago

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.14 | quality: 10.0
- latency_total: 28.674s | tokens_per_second: 195.9
- input_tokens: 188 | output_tokens: 5617

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

No estás en pánico por nada: **el 31% es correcto para “usuarios totales”, pero no es el churn de tus usuarios de pago**.

## 1. Qué está pasando realmente

| Segmento | Bajas del mes | Usuarios inicio mes | Churn |
|---|---:|---:|---:|
| Total | 62 | 200 | **31%** |
| Gratuito | 60 | 178 | **33.7%** |
| Pago | 2 | 22 | **9.1%** |

Conclusión rápida:

- **Churn total de usuarios:** 31%. Sí, el panel está calculando bien esa métrica.
- **Churn de usuarios de pago:** 2 / 22 = **9.1%**, no 5%.
- **Churn de usuarios gratuitos:** 60 / 178 = **33.7%**.
- El 97% de las bajas vienen del plan gratuito: 60 de 62.

Así que el problema no es que el dashboard esté “mintiendo”; es que **está mezclando poblaciones distintas** y eso es peligroso para interpretar retención.

## 2. Qué tan grave es

**Para usuarios de pago: grave, pero manejable.**

9.1% mensual de churn pagado está por encima de 5%, pero solo son 2 clientes pagados de 22. Con una base tan pequeña, una sola baja más subiría el churn a:

- 3 bajas / 22 = **13.6%**

Así que hay que actuar, pero no conviene tomar decisiones grandes basadas solo en 2 clientes.

**Para usuarios gratuitos: alto, pero no necesariamente catastrófico.**  
Si tu modelo es freemium, el churn gratuito puede ser naturalmente alto. Lo importante es ver si esos usuarios gratuitos se activan, convierten a pago o generan valor indirecto.

## 3. Plan inmediato

### Hoy: ordena la métrica

Reformula el dashboard con estas métricas separadas:

1. **Churn total de usuarios**  
   `bajas totales / usuarios inicio mes`

2. **Churn de usuarios de pago**  
   `bajas de pago / usuarios de pago inicio mes`

3. **Churn de usuarios gratuitos**  
   `bajas gratuitas / usuarios gratuitos inicio mes`

4. **Gross revenue churn**, si tienes MRR:  
   `MRR perdido por bajas pagadas / MRR inicio mes`

5. **Net revenue churn**, si tienes expansión/contracción:  
   `(MRR inicio - MRR fin + expansión) / MRR inicio`

No mezcles users gratuitos con users de pago si tu negocio se mide por ingresos.

## 4. Acciones de 24 a 72 horas

### A. Revisa a los 2 usuarios de pago que se dieron de baja

Para cada uno, mira:

- Último login
- Uso de funciones clave
- Facturación: pagos fallidos, tarjetas vencidas
- Tickets de soporte
- Plan comprado
- Tiempo desde que se registraron
- Canal de adquisición
- Motivo declarado de baja, si existe

Contacta a ambos con una pregunta simple:

> “Nos dimos cuenta de que cancelaste tu plan. ¿Qué ocurrió? Queremos entender si fue precio, falta de uso, un problema técnico o algo que podríamos haber hecho mejor.”

Objetivo: recuperar al menos 1, o al menos entender la causa.

### B. Revisa a los 20 usuarios de pago restantes

No esperes a que cancelen.

Busca señales de riesgo:

- No han entrado en los últimos 7-14 días
- Pagaron pero no han usado la herramienta
- Tienen tickets abiertos
- Usan solo una función limitada
- Están cerca del límite del plan
- Han intentado actualizar o cambiar plan

Puedes hacer outreach preventivo.

## 5. Diagnóstico de causa

Clasifica las 62 bajas por motivo probable:

| Causa | Qué revisar | Acción |
|---|---|---|
| Pago fallido | tarjetas, dunning, facturas | mejorar recordatorios, retries, dunning |
| Bajo uso | activación, onboarding | guías, emails, in-app prompts |
| Precio | plan, valor percibido | mejorar empaquetado, prueba de valor |
| Problema técnico | bugs, incidentes | priorizar fixes, comunicación |
| Mal canal | tráfico de baja calidad | ajustar adquisición |
| Expectativa no cumplida | onboarding inicial | mejorar mensajes y expectations |

La clave es saber si las bajas vienen de un mismo grupo: mismo canal, misma cohorte, mismo plan, misma funcionalidad rota o misma fecha de campaña.

## 6. Qué hacer con el churn gratuito

No intentes “resolver” el churn gratuito como si fuera igual al churn pagado.

Si tienes freemium, enfócate en:

- Tasa de activación
- Tiempo hasta primer valor
- Conversión gratuito → pago
- Uso de funciones clave
- Reactivación de usuarios inactivos
- Embudo desde registro hasta primera acción importante

El churn gratuito puede ser alto y no significar pérdida directa de ingresos. Pero sí puede indicar problemas de adquisición o onboarding.

## 7. Plan de 30 días

### Semana 1

- Separar KPIs: total, gratuito, pago, MRR.
- Contactar a los 2 usuarios pagados que cancelaron.
- Revisar los 20 usuarios pagados restantes.
- Detectar si hubo incidente, bug, cambio de precio o problema de facturación.

### Semana 2

- Lanzar acciones correctivas según causa:
  - Dunning para pagos fallidos.
  - Onboarding para bajo uso.
  - Outreach para cuentas de riesgo.
  - Comunicación si hubo bug o mala experiencia.

### Semana 3-4

- Medir:
  - Churn pagado semanal
  - MRR perdido
  - Usuarios pagados reactivados
  - Activación de nuevos usuarios
  - Conversión gratuito → pago

Objetivo razonable:

- Reducir churn pagado de **9.1%** hacia **5% o menos**
- Recuperar al menos 1 de los 2 clientes pagados que cancelaron
- Evitar que el churn total de usuarios siga dominando el dashboard con usuarios gratuitos

## Mensaje interno sugerido

Puedes comunicarlo así:

> “El churn reportado de 31% corresponde a usuarios totales. Al segmentar, vemos que el churn de usuarios de pago es 9.1%, no 5%. El churn gratuito es 33.7% y está empujando el número total. Vamos a separar los KPIs, priorizar la retención pagada y revisar las causas de baja por cohorte y plan.”

En resumen: **no estás en 5%, pero tampoco el 31% debe tratarse como churn pagado.** El número urgente es **9.1% de churn pagado**, y el dashboard necesita segmentación antes de que el equipo tome decisiones.