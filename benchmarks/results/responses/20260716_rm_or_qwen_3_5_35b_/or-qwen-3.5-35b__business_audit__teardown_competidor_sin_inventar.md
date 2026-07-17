# Qwen 3.5 35B — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 3.28 | quality: 2.0
- latency_total: 10.429s | tokens_per_second: 196.4
- input_tokens: 193 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

## Respuesta completa

Aquí tienes el teardown competitivo. He separado estrictamente los datos observables de mis deducciones, marcando el nivel de certeza de cada afirmación.

### 1. Resumen Ejecutivo: Datos vs. Inferencias

| Variable | Lo que sabemos (Hecho) | Lo que infiero (Análisis) | Certeza |
| :--- | :--- | :--- | :--- |
| **Tamaño Comunidad** | 2.400 miembros (visible en portada). | Es probable el número total de pagadores activos o totales acumulados. | Medio |
| **Precio** | $39 USD / mes. | No hay plan anual, lo que sugiere estrategia de volumen o falta de optimización de LTV. | Alto |
| **Contenido** | 3 posts/semana en feed público. | Es una cadencia estándar para mantener engagement sin saturar recursos. | Medio |
| **Autoridad** | Fundador con 60.000 seguidores. | Es su principal canal de adquisición (CAC bajo) y validador de confianza. | Alto |
| **Activos** | 12 cursos listados. | Probablemente contenido "evergreen" para onboarding, no necesariamente contenido nuevo diario. | Medio |

---

### 2. Estimación de Ingresos (Revenue)

**Cálculo Bruto:**
*   `[HECHO]` Precio: $39/mes.
*   `[HECHO]` Miembros: 2.400.
*   `[INFERENCIA - Certeza: Media]` Asumiendo que el número de miembros es real y no incluye pruebas gratuitas, el ingreso mensual bruto es:
    $$ 2.400 \times \$39 = \$93.600 / \text{mes} $$
    $$ \$93.600 \times 12 = \$1.123.200 / \text{año} $$

**Ajustes a Ingresos Netos:**
*   `[INFERENCIA - Certeza: Baja]` **Churn (Tasa de cancelación):** En comunidades de bajo ticket ($39), el churn mensual suele oscilar entre 5% y 10%. Si asumen un 7% de churn, el número de 2.400 es *estable*, no *creciente*.
*   `[INFERENCIA - Certeza: Alta]` **Costos de Plataforma:** Plataformas como Skool, Circle o Kajabi cobran entre $500 y $3.000/mes fijos + % de transacción.
*   `[INFERENCIA - Certeza: Alta]` **Procesamiento de Pagos:** Stripe/PayPal cobran ~2.9% + $0.30.
    *   Costo estimado de pasarela: $93.600 * 0.03 ≈ **$2.800/m