# Claude Opus 4.7 (suscripción) — deep_reasoning/fermi_estimation

- model_id: `claude-opus-4-7`
- success: True  | final: 6.18 | quality: 7.58
- latency_total: 27.063s | tokens_per_second: 53.2
- input_tokens: 6 | output_tokens: 1440
- judge_score: 4.4 | justificación: 

## Respuesta completa

# Estimación: Litros de café consumidos al día en oficinas de Santiago

## Razonamiento paso a paso

### Supuesto 1: Población total de Santiago
Santiago Metropolitano tiene aproximadamente **7,1 millones de habitantes** (2026, proyección INE).

### Supuesto 2: Población económicamente activa (PEA) ocupada
Tasa de ocupación ~57% sobre población 15+ años. Considerando que ~78% de la población tiene 15+ años:
- 7,1M × 0,78 × 0,57 ≈ **3,15 millones de ocupados**

### Supuesto 3: Proporción que trabaja en oficinas
No todos los ocupados están en oficinas (comercio, construcción, manufactura, servicios personales, transporte, agricultura quedan fuera). Estimación: **~35% trabaja en oficina** (servicios financieros, públicos, profesionales, tech, administración).
- 3,15M × 0,35 ≈ **1,1 millones de trabajadores de oficina**

### Supuesto 4: Asistencia presencial efectiva
Post-pandemia, el trabajo híbrido redujo la presencialidad. Estimación: **~70% asiste presencialmente** un día promedio (mezcla full-presencial + híbridos).
- 1,1M × 0,70 ≈ **770.000 personas en oficina por día**

### Supuesto 5: Proporción que toma café
En Chile el café es popular pero el té también compite fuerte. Estimación: **~65% toma al menos un café al día** en la oficina.
- 770.000 × 0,65 ≈ **500.000 cafeteros diarios**

### Supuesto 6: Tazas promedio por persona por día
Mezcla entre quien toma 1 (desayuno) y quien toma 3-4 (heavy users). Promedio: **2 tazas/día**.

### Supuesto 7: Volumen por taza
Tazas de oficina típicas (incluye espresso de máquina, americano, instantáneo en jarro): promedio ponderado **~180 ml/taza**.

### Cálculo central
500.000 personas × 2 tazas × 0,18 L = **180.000 litros/día**

---

## Rango de incertidumbre

| Escenario | Trabajadores oficina | % cafeteros | Tazas/día | ml/taza | **Total** |
|---|---|---|---|---|---|
| **Mínimo** | 600.000 | 50% | 1,5 | 150 ml | **~67.500 L** |
| **Central** | 770.000 | 65% | 2,0 | 180 ml | **~180.000 L** |
| **Máximo** | 900.000 | 75% | 2,8 | 220 ml | **~415.000 L** |

**Mejor estimación: ~180.000 litros/día**
**Rango plausible: 70.000 – 415.000 litros/día**

---

## Supuesto con mayor impacto

El supuesto más sensible es el **#3 (proporción que trabaja en oficina)**, seguido del **#6 (tazas por persona)**.

- **Por qué #3 domina**: la diferencia entre "25% de los ocupados es oficinista" vs "45%" mueve el resultado en ±50%. No existe estadística oficial limpia que separe "trabajo de oficina" de otros sectores en la EOD/ENE del INE — hay que estimarlo desde la composición sectorial.
- **Por qué #6 es segundo**: pasar de 1,5 a 3 tazas/día duplica el resultado, y la variabilidad real entre personas es enorme (hay quien toma 0 y quien toma 5).

Los supuestos #1 y #2 son los más robustos (datos INE públicos, error <5%). El #4 (presencialidad híbrida) es relevante pero acotado (±15%).

**Sanity check**: 180.000 L/día equivale a ~7,2 g de café molido por persona-oficina por día (asumiendo ~10 g por taza × 2 tazas × 65% cafeteros / población total oficinas), consistente con consumo per cápita Chile (~1 kg/año/persona, mayoritariamente instantáneo).