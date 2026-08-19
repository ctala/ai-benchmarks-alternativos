# Seed 2.1 Turbo — business_audit/churn_mezcla_free_y_pago

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 150.817s | tokens_per_second: 54.3
- input_tokens: 220 | output_tokens: 8192

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

Respira, no tienes un churn de 31% de ingresos. El pánico viene de que la métrica que estás viendo mezcla dos poblaciones completamente distintas, y está dominada por el segmento que no genera ingresos. Vamos a desglosarlo paso a paso.

---

## 1. Diagnóstico rápido: ¿de dónde sale el 31%?
La plataforma está calculando el **churn de base de usuarios total** (todos los usuarios registrados, gratuitos + de pago) sobre el total de usuarios al inicio del mes:
> 62 bajas / 200 usuarios iniciales = 31%

Matemáticamente es correcto, pero es una métrica casi inútil para medir la salud de tu negocio, porque mezcla:
- Usuarios que pagan (tu fuente de ingresos)
- Usuarios gratuitos (que no generan ingresos directos y tienen comportamientos muy distintos)

Al separar por segmento (lo que sí importa):
| Segmento       | Usuarios inicio mes | Bajas | Churn mensual |
|----------------|---------------------|-------|----------------|
| Plan gratuito  | 178                 | 60    | 33,7%          |
| Plan de pago  | 22                  | 2     | 9,1%           |

Tu expectativa de 5% casi seguro corresponde al **churn de pago** (la métrica estándar para medir retención de ingresos), así que no estás en 31%, estás en 9,1%: es un desvío respecto a tu objetivo, pero no una catástrofe.

---

## 2. ¿Qué tan grave es realmente?
Depende de tu modelo de negocio, pero en orden de impacto:
### ✅ Impacto en ingresos: BAJO-MEDIO (nada de crisis)
- El 97% de las bajas (60 de 62) son de usuarios que no pagan, así que no afectan directamente tus ingresos.
- Con una base de pago tan pequeña (22 usuarios), el churn de usuarios es muy volátil: una sola baja más o menos cambia la métrica mucho. Por ejemplo, si el mes pasado tuviste 1 baja, el churn era de 4,5% (casi tu objetivo de 5%). Este mes con 2 bajas sube a 9,1%: puede ser un caso puntual, no un problema estructural.
- Si calculas el **churn de ingresos** (MRR perdido / MRR inicial), que es la métrica más fiable para negocios de suscripción, probablemente sea aún menor: si los 2 usuarios que se fueron tenían planes baratos, podría estar incluso por debajo de tu 5% objetivo.

### ⚠️ Impacto en funnel de adquisición: MEDIO (depende del propósito del plan gratuito)
El churn de 33,7% en gratuitos solo es preocupante si:
- El plan gratuito es un **trial** (prueba para convertir a pago): en ese caso, es una tasa de abandono de trial alta para muchos sectores, y afecta la cantidad de leads que pasan a pagar.
- El plan gratuito es permanente y lo usas para monetizar por publicidad/referidos: en ese caso, sí es un problema de retención de usuarios.

Si las bajas son de usuarios que nunca activaron la cuenta o la usaron una sola vez: no es grave, es limpieza natural de cuentas inactivas.

---

## 3. Plan paso a paso (ordenado por prioridad)

### Fase 1: Sal del pánico y valida el diagnóstico (primeros 30 minutos)
1. **Confirma la configuración del panel**: Revisa qué población usa la plataforma para calcular el churn. Seguro que tiene marcado "todos los usuarios registrados" e incluye gratuitos. Eso confirma que el 31% es un churn de base total, no de clientes de pago.
2. **Calcula la métrica que realmente importa**:
   - Si tu negocio es de suscripciones: calcula el **churn de ingresos** (si tienes datos de MRR):
     `MRR perdido por bajas este mes / MRR al inicio del mes`
     Esta métrica pondera por el valor de cada cliente, así que te dice realmente cuánto ingreso pierdes.
   - Si el plan gratuito es un trial: renombra esa métrica a "tasa de abandono de trial" y calcula la tasa de conversión a pago de los que se quedan.
3. **Alinea tu expectativa de 5%**: ¿De dónde salía ese número? ¿Medías antes solo usuarios de pago activos? ¿Era churn anual? Alinear la definición te quitará sustos futuros.

### Fase 2: Arregla tu panel para no volver a pasar esto (1-2 días)
1. **Elimina el "churn total" de tu panel principal**: Ponlo en una sección secundaria de métricas de base de usuarios, no de salud del negocio.
2. **Configura segmentación obligatoria**:
   - Métrica principal: Churn de pago (de ingresos, preferiblemente)
   - Segmentos secundarios: Churn por plan, por antigü