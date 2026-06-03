# Claude Sonnet 4.6 (suscripción) — deep_reasoning/fermi_estimation

- model_id: `claude-sonnet-4-6`
- success: True  | final: 6.45 | quality: 8.2
- latency_total: 50.629s | tokens_per_second: 54.5
- input_tokens: 3 | output_tokens: 2761
- judge_score: 5.0 | justificación: 

## Respuesta completa

# ☕ Estimación Fermi: Litros de café en oficinas de Santiago / día

---

## SUPUESTOS NUMERADOS

### Bloque 1 — Personas en oficinas

| # | Supuesto | Valor central | Rango |
|---|---|---|---|
| 1 | Población Gran Santiago | 7.0 M hab | 6.8–7.2 M |
| 2 | Población en edad laboral (15–64) | 66 % → **4.62 M** | 64–68 % |
| 3 | Tasa de ocupación en Santiago | 61 % → **2.82 M** trabajadores | 58–64 % |
| 4 | Fracción que trabaja en oficina/escritorio (admin, finanzas, tech, gobierno, educación administrativa) | 40 % → **1.13 M** | 35–45 % |
| 5 | Asistencia presencial ese día (descuenta teletrabajo, licencias, vacaciones) | 75 % → **845 000** en oficina | 65–82 % |

> **Chile post-COVID**: ~20–25 % work-from-home full time; otro 15 % híbrido → la asistencia física diaria está en torno al 75 %.

---

### Bloque 2 — Consumo por persona

| # | Supuesto | Valor central | Rango |
|---|---|---|---|
| 6 | Fracción de los presentes que toma café en la oficina | 70 % → **591 500** | 60–80 % |
| 7 | Tazas de café por bebedor por día en oficina | **2.5 tazas** | 1.5–3.5 |
| 8 | Volumen por taza (mezcla nescafé/americano/espresso) | **180 ml** | 150–220 ml |

> Nota cultural: Chile consume ~1.5 kg café/cápita/año (vs. ~10 kg en Finlandia). Pero el consumo *de oficina* es más alto que el promedio total porque concentra el momento social de la pausa.

---

## CÁLCULO CENTRAL

```
845 000 presentes
  × 0.70 (beben café)         =  591 500 bebedores
  × 2.5 tazas                 = 1 478 750 tazas
  × 0.180 L                   =   266 175 L
```

### ➤ Mejor estimación: **~265 000 litros / día**

---

## RANGO MÍNIMO–MÁXIMO

| Escenario | Presentes | % toman café | Tazas/día | ml/taza | **Litros/día** |
|---|---|---|---|---|---|
| **Mínimo** | 700 000 | 60 % | 1.5 | 150 | **~95 000 L** |
| **Central** | 845 000 | 70 % | 2.5 | 180 | **~265 000 L** |
| **Máximo** | 1 050 000 | 80 % | 3.5 | 220 | **~648 000 L** |

### ➤ Rango razonable: **100 000 – 650 000 L/día**

---

## ¿QUÉ SUPUESTO TIENE MÁS IMPACTO?

**El supuesto #7 (tazas por bebedor por día) domina el resultado**, por dos razones:

1. **Rango relativo mayor**: varía de 1.5 a 3.5 tazas → es una variación de **×2.3** entre extremos, mientras que el volumen por taza solo varía ×1.5 y la fracción de bebedores ×1.3.

2. **Se multiplica sobre toda la base**: afecta al resultado en proporción directa.

```
Sensibilidad (cambio de ±1 taza):
  1 taza menos → 265 000 − 106 000 = 159 000 L  (−40 %)
  1 taza más   → 265 000 + 106 000 = 371 000 L  (+40 %)
```

El número de trabajadores en oficina (#4) también es relevante, pero su rango de incertidumbre es más estrecho (±5 puntos porcentuales).

---

## SANITY CHECK

265 000 L/día ÷ 845 000 presentes ≈ **0.31 L por persona** = 1.7 tazas promedio poblacional (incluyendo los que no beben). Eso es razonable para un país con cultura cafetera moderada.