# Inkling Small — business_audit/churn_mezcla_free_y_pago

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 98.451s | tokens_per_second: 28.9
- input_tokens: 172 | output_tokens: 2842
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una descomposición detallada de las métricas de churn y un plan de acción claro.

## Respuesta completa

Antes de interpretar nada, verifico qué población mide realmente tu panel: **mide todos los usuarios registrados (free + pago), no solo los que generan ingresos ni los activos.** Eso explica el pánico.

Tu 31% es matemáticamente correcto (62/200), pero es un **churn blended que no sirve para decisiones de negocio** si eres freemium.

Aquí está la verdad de los datos:

| Segmento | Inicio mes | Bajas | Churn real |
|---|---|---|---|
| **Gratuito** | 178 | 60 | **33,7%** |
| **Pago** | 22 | 2 | **9,1%** |
| **Total (lo que reporta tu panel)** | 200 | 62 | **31%** |

**¿Qué tan grave es?**
- **No es 31% de crisis.** Es una historia de dos métricas distintas.
- El 33,7% de gratuitos es típico en freemium (baja barrera, sin compromiso financiero). No es tu "churn de negocio".
- El **9,1% de pago es tu número real**. Es casi el doble del 5% que esperabas, pero con una muestra de **solo 22 usuarios**, 2 bajas te mueven el porcentaje enormemente (si hubiera sido 1 baja, estarías en 4,5%). No es una catástrofe, pero sí una señal amarilla.

Probablemente tu "5%" histórico era **churn de pago** o un promedio de 3 meses. El panel te está mezclando la basura con el oro.

---

### Plan de acción (en orden)

**1. Separar inmediatamente las métricas (hoy)**
No uses "churn total" para reportar al equipo o a inversionistas. Define:
- **Paid Logo Churn:** 2/22 = 9,1%.
- **Free Churn / Activation Drop:** 60/178 = 33,7%.
- **Revenue Churn / Net Revenue Retention:** Calcula si esos 2 de pago eran de alto valor.

**2. Tratar la muestra de pago como volátil (esta semana)**
Con 22 usuarios, un solo cambio de mes te da 4,5% o 13,6%. No tomes decisiones estructurales (cambiar precios, despedir al CS) con n=22. Usa un **promedio móvil de 3 meses** para el churn pagado.

**3. Investigar las 2 bajas de pago (esta semana)**
No el panel. Llama/escribe a esos 2 usuarios.
- ¿Se fueron por precio, falta de feature, o por un problema técnico?
- ¿Eran de un mismo canal de adquisición o de una misma cohorte (ej. una promoción)?
- ¿Bajaron a free o cancelaron totalmente? (Si bajaron, es downgrades, no churn puro).

**4. Revisar la definición del denominador**
Asegúrate de que los 200 sean usuarios que **estaban activos al inicio** y que no incluyas:
- Usuarios que se registraron y se fueron el mismo mes (deberían ir al numerador pero a veces se excluyen del denominador).
- Usuarios que pasaron de pago a free (si tu panel los cuenta como "baja").

**5. Definir tu KPI de retención real**
Para una plataforma freemium:
- **Churn de pago mensual:** Meta <5% (o lo que corresponda a tu CAC).
- **Free-to-Paid conversion:** Si el gratuito se va, importa si antes convirtió.
- **Revenue Retention:** Si los 2 de pago eran los únicos que pagaban mucho, el impacto en ingresos es mayor que en usuarios.

**6. No toques la estrategia de "free" por este número**
El 33,7% de gratuitos podría ser normal si son usuarios de prueba o de baja intención. Si empiezas a retener gratuitos a la fuerza sin convertirlos, solo aumentas tu coste operativo. Mejor analiza si esos 60 se fueron antes de activar (día 0-7) o después de meses.

---

**Resumen para que respiras:** El panel te está mintiendo por agregación. Tu negocio no está en 31%; tu negocio está en **9,1% de pago con una base muy pequeña**. Eso requiere atención, no pánico. Corrige la segmentación hoy, investiga esas 2 bajas esta semana, y deja de mirar el número global. ¿Quieres que calculemos el impacto en ingresos si esos 2 de pago eran, por ejemplo, tu 80% de MRR?