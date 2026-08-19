# Gemini 3.1 Pro — business_audit/teardown_competidor_sin_inventar

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 6.25 | quality: 6.94
- latency_total: 19.838s | tokens_per_second: 103.0
- input_tokens: 177 | output_tokens: 2044

## Respuesta completa

Como analista competitivo, mi primera regla es no tomar las métricas de marketing como verdades absolutas. Las páginas de aterrizaje (*landing pages*) están diseñadas para vender, no para ser auditadas.

Aquí tienes el *teardown* (desglose) de tu competidor. He clasificado mis conclusiones separando estrictamente lo que **sabemos (hechos)** de lo que **deduzco (inferencias)**, indicando mi nivel de certeza.

---

### 1. ESTIMACIÓN DE FACTURACIÓN

**[HECHO]** Muestran 2.400 miembros y un precio de $39/mes.
**[INFERENCIA]** La facturación real NO es $93.600/mes ($1.12M/año). **[CERTEZA ALTA]**

*¿Por qué?* En la industria de las comunidades de pago, el número "público" de miembros casi siempre refleja el **histórico total** (todos los que alguna vez se registraron, incluyendo pruebas gratuitas, usuarios dados de baja, amigos/familiares y cuentas beta), no los suscriptores activos actuales.

**Escenarios de facturación realista (Inferencia basada en benchmarks de la industria):**

*   **Escenario Optimista [CERTEZA BAJA]:** Tienen una retención increíble. El 60% de esos 2.400 son activos pagando el precio completo (sin descuentos anuales).
    *   *1.440 miembros x $39 = ~$56.000 / mes.*
*   **Escenario Realista [CERTEZA MEDIA]:** Tasa de conversión estándar desde su audiencia (60k seguidores) y rotación (*churn*) normal de una comunidad. Aproximadamente el 30-40% del número público son miembros de pago activos. Asumiendo un Ticket Medio (ARPU) de $30/mes (descontando planes anuales o promociones pasadas).
    *   *800 - 1.000 miembros x $30 = **$24.000 - $30.000 / mes**.*
*   **Escenario Pesimista [CERTEZA MEDIA]:** La comunidad está estancada. El creador hizo un gran lanzamiento inicial, sumó mucha gente, pero el *churn* ha sido alto porque los cursos no están terminados.
    *   *300 - 500 miembros x $30 = $9.000 - $15.000 / mes.*

**Veredicto de Facturación:** Negocio