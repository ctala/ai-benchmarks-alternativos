# Claude Haiku 4.5 (suscripción) — deep_reasoning/fermi_estimation

- model_id: `claude-haiku-4-5`
- success: True  | final: 6.83 | quality: 8.18
- latency_total: 27.215s | tokens_per_second: 123.6
- input_tokens: 10 | output_tokens: 3363
- judge_score: 4.4 | justificación: 

## Respuesta completa

# Estimación: Consumo de Café Diario en Oficinas de Santiago

## Razonamiento paso a paso

**SUPUESTO 1: Población de Santiago Metropolitana**
- 5,400,000 habitantes (estimado 2026)

**SUPUESTO 2: Población Económicamente Activa (PEA)**
- 65% de población adulta (18-65 años) = 5.4M × 0.65 = 3.51M adultos
- 60% tasa de participación laboral = 3.51M × 0.60 = **2.1M en PEA**

**SUPUESTO 3: Proporción que trabaja en "oficinas"**
- Incluye: finanzas, seguros, IT, administración pública, educación, legal, consultoría, comercio administrativo
- Excluye: construcción, manufactura, retail presencial, transporte, servicios hogar, agrícola
- Estimado: **50% del PEA = 1.05M trabajadores de oficina**

**SUPUESTO 4: Qué porcentaje bebe café**
- Adultos que NO beben (lactancia, problemas digestivos, religión, preferencias) = ~30%
- Bebedores de café en oficina: **70% × 1.05M = 735,000 personas**

**SUPUESTO 5: Consumo por persona que bebe café**
- Rango típico: 1-2 tazas durante jornada laboral
- Promedio: 1.5 tazas/día
- Volumen estándar: 250 ml/taza
- **Consumo per cápita: 1.5 × 0.25L = 0.375 L/día**

**SUPUESTO 6: Café en máquinas y cafeterías corporativas**
- Máquinas expendedoras en edificios (café vendido separado del que trae gente)
- Cafés en cafeterías corporativas
- Factor adicional: **+20% al consumo casero**

---

## Cálculo Final

**Mejor estimación:**
```
735,000 personas × 0.375 L = 275,625 L
+ máquinas/cafeterías (×1.20) = 330,750 L

≈ 330,000 LITROS/DÍA
```

---

## Rango Min-Max

| Escenario | Supuestos | Cálculo | Total |
|---|---|---|---|
| **MÍNIMO** | 45% en oficinas, 60% beben, 1.2 tazas, sin máquinas | 945k × 0.60 × 0.3L | **170,000 L** |
| **MEJOR ESTIMACIÓN** | 50% en oficinas, 70% beben, 1.5 tazas, +20% máquinas | 735k × 0.375L × 1.20 | **330,000 L** |
| **MÁXIMO** | 55% en oficinas, 80% beben, 2 tazas, +30% máquinas | 924k × 0.5L × 1.30 | **600,000 L** |

**Rango: 170,000 - 600,000 litros/día** | **Mejor estimación: ~330,000 L/día**

---

## Análisis de Sensibilidad: ¿Cuál supuesto impacta más?

Variando cada parámetro ±1 desviación estándar desde la estimación base (330k L):

| Supuesto | Variación | Impacto |
|---|---|---|
| **Consumo per cápita (tazas × 250ml)** | 0.3L → 0.5L | **±165,000 L** ⭐ |
| **% que bebe café** | 60% → 80% | ±110,000 L |
| **% trabajadores en oficina** | 45% → 55% | ±110,000 L |
| **Factor máquinas (+20% → +30%)** | × 1.20 → × 1.30 | ±33,000 L |
| **Población total Santiago** | ±5% | ±82,000 L |

### 🎯 **Supuesto más impactante: CONSUMO PER CÁPITA**

La diferencia entre "1 taza promedio" vs "2 tazas promedio" prácticamente **dobla el resultado**. Esto es porque es el multiplicador directo del volumen por persona.

**Explicación:** Si 200,000 personas bebieran 2 tazas en vez de 1, son +50,000 L extra. El consumo está directamente atado al comportamiento diario observable, con más varianza que la demografía.

---

## Sanity Check

**330,000 L ÷ 1.05M trabajadores = 0.31 L/trabajador/día** ✓

*Esto equivale a ~1.2 tazas por trabajador completo (incluyendo abstinentes), razonable para Santiago.*