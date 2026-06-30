# Grok 4.3 — strategy/pricing_strategy

- model_id: `x-ai/grok-4.3`
- success: True  | final: 8.74 | quality: 10.0
- latency_total: 13.093s | tokens_per_second: 117.3
- input_tokens: 300 | output_tokens: 1536

## Respuesta completa

**Análisis de subida de precio: $60 → $89/mes**

### 1. LTV/CAC actual y proyectado

**Actual:**
- LTV = $840
- CAC = $120
- **LTV/CAC = 7.0x** (muy bueno)

**Si subes a $89 manteniendo el mismo churn (7%):**
- Nuevo LTV = 14.28 meses × $89 = **$1,271**
- Nuevo LTV/CAC = **10.6x**

Este cálculo es teórico. El churn casi seguro va a subir.

### 2. Impacto estimado en churn

Un aumento del **48%** ($60 → $89) es agresivo. Según benchmarks de SaaS (Price Intelligently, Paddle, ChartMogul):

- Aumentos >30-40% suelen generar un **aumento de churn de 2-5 puntos porcentuales** en los primeros 3-6 meses.
- Clientes existentes son más sensibles que los nuevos.

**Estimaciones realistas de churn post-subida:**
- Optimista: **8.5%** (+1.5pp)
- Realista: **10-11%** (+3-4pp)
- Pesimista: **13-14%** (+6-7pp)

### 3. Modelado de escenarios (200 clientes actuales)

Asumo:
- No pierdes clientes inmediatamente (solo churn mensual).
- CAC se mantiene en $120.
- Costo por usuario = $8.

| Escenario     | Churn mensual | LTV   | LTV/CAC | Ingresos mensuales (mes 12) | MRR neto a 12 meses | Comentario |
|---------------|---------------|-------|---------|-----------------------------|---------------------|----------|
| **Optimista** | 8.5%         | $1,047 | 8.7x   | $14,240                    | +$2,240            | Churn sube poco |
| **Realista**  | 10.5%        | $848  | 7.1x   | $12,950                    | +$950              | Escenario más probable |
| **Pesimista** | 13.5%        | $659  | 5.5x   | $11,200                    | -$800              | Fuerte resistencia |

**Notas sobre el modelado:**
- En el escenario realista, a los 12 meses estarías facturando ~$950/mes más que ahora, pero con mayor riesgo de erosión de base de clientes.
- El LTV/CAC se mantiene saludable (>5x) incluso en el caso pesimista.

### 4. Recomendación

**Recomendación principal: Subir, pero no a $89 para todos.**

**Opción recomendada:**
- **Precio nuevo para nuevos clientes: $89/mes**
- **Clientes existentes: mantener $60** (ver estrategia abajo)

**Razones:**
- Tu LTV/CAC actual es excelente (7x), tienes margen para absorber algo de churn.
- $89 está dentro del rango de competidores ($29-$149).
- Un aumento del 48% a todos los clientes actuales es muy riesgoso con solo 200 clientes.

**Alternativa más conservadora:**
- Subir a **$79** (en vez de $89) → menor riesgo de churn (~9-10%).

### 5. Estrategia de implementación

**Recomendación: Modelo híbrido**

| Segmento              | Precio     | Momento          | Justificación |
|-----------------------|------------|------------------|-------------|
| **Nuevos clientes**   | $89       | Inmediato        | Maximizar LTV desde día 1 |
| **Clientes existentes** | $60     | Mantener       | Grandfathering total |
| **Clientes existentes (opcional)** | $79 | A los 6-9 meses | Si quieres capturar algo de revenue |

**Otras tácticas recomendadas:**

1. **Grandfathering agresivo** (recomendado)
   - Mantén $60 a los 200 actuales de por vida.
   - Justifícalo como "precio legacy".

2. **Aumento gradual para existentes** (si decides subirles)
   - Opción A: +$10 cada 4 meses hasta llegar a $79.
   - Opción B: Avisar con 60 días de antelación + ofrecer 3 meses a precio actual.

3. **Añadir valor perceptible** antes de subir
   - Idealmente lanza 1-2 features nuevas antes del aumento de precio (aunque sea para nuevos clientes).

4. **Test de precio**
   - Antes de subir a $89, prueba $79-$85 con nuevos leads durante 30-45 días.

**Resumen final:**
Sube a **$89 para nuevos clientes** y mantén $60 a los actuales. Esto te da la mejor relación riesgo/recompensa dado tu tamaño actual (200 clientes). El escenario realista te dejaría ~$950 MRR adicional en 12 meses con riesgo controlado.