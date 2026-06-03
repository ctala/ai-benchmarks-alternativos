# Claude Opus 4.8 (suscripción) — reasoning/business_analysis

- model_id: `claude-opus-4-8`
- success: True  | final: 7.14 | quality: 10.0
- latency_total: 48.865s | tokens_per_second: 70.3
- input_tokens: 2026 | output_tokens: 3436
- judge_score: 5.0 | justificación: 

## Respuesta completa

## 1. Métricas clave

| Métrica | Enero | Febrero | Marzo | Tendencia |
|---|---|---|---|---|
| **Churn rate** (churns/usuarios inicio mes) | 3.75%¹ | 4.33% | 5.04% | 🔴 subiendo |
| **Growth MRR** (MoM) | — | +12.5% | +9.6% | 🔴 desacelera |
| **Growth usuarios** (MoM) | — | +12.5% | +9.6% | 🔴 desacelera |
| **LTV/CAC** | 4.94x | 4.51x | 5.23x | 🟢 sano (>3x) |
| **ARPU** (MRR/usuarios) | $15.00 | $15.00 | $15.00 | ⚠️ plano |
| **NRR**² (estimado) | — | ~95.7% | ~95.0% | 🔴 <100% |

¹ Enero usa su propia base por falta de mes previo.
² NRR estimada asumiendo ARPU constante y sin datos de expansión: `(MRR inicio − MRR churneado) / MRR inicio`. MRR churneado = churns × $15.

**Dato clave que se esconde detrás de los números:** descompuse el crecimiento neto de usuarios.

| | Febrero | Marzo |
|---|---|---|
| Nuevos brutos (neto + churn) | 202 | 198 |
| Churns | 52 | 68 |
| **Neto agregado** | **+150** | **+130** |

La adquisición está **plana (~200/mes)**. El crecimiento se está frenando **no porque entren menos, sino porque se van más**.

## 2. Tendencias preocupantes

1. **Churn acelerando, no creciendo lineal.** Incrementos de +7 y luego +16 churns. No es ruido: es una fuga que se agranda y ya te come el 34% de tus altas brutas en marzo (68 de 198).
2. **ARPU congelado en $15 → cero expansión.** Todo tu crecimiento de MRR viene de cabezas nuevas, ninguno de tu base existente. Con NRR ~95% (<100%), tu base **se contrae sola**: sin adquirir, perderías plata cada mes. Los SaaS sanos viven en NRR >100%.
3. **LTV cayendo ($420→$415→$408)** — consecuencia directa del churn. Y empeorará: el LTV de marzo aún refleja el churn viejo; con churn al 5% el LTV real ya es más bajo de lo reportado.
4. **Desaceleración del MRR** (12.5%→9.6%). Si churn sube y adquisición no, esto sigue bajando.

## 3. Tres acciones concretas

**A. Atacar el churn YA (prioridad #1).** Es tu fuga estructural. Segmentá los 68 churns de marzo: ¿son del último mes (onboarding roto) o cohortes viejas (falta de valor sostenido)? Implementá un health score + intervención proactiva. Bajar el churn de 5% a 3.75% (tu nivel de enero) en abril te recuperaría ~18 usuarios/mes y subiría el LTV ~30%.

**B. Construir expansión para romper el ARPU plano.** NRR <100% es el síntoma más grave. Lanzá upsells: tier superior, add-ons por uso, o anual con descuento. Meta: NRR >100%, donde tu base crece sin adquirir. Mover ARPU de $15 a $17 = +13% MRR sin un solo usuario nuevo.

**C. Pisar el acelerador de adquisición — tenés margen.** LTV/CAC de 5.2x en marzo (con CAC bajando a $78) significa que estás **sub-invirtiendo**. La regla sana es ~3x; estás holgado. Reasigná presupuesto al canal que bajó tu CAC. **Pero**: solo después de tapar el churn (A), o estarás llenando un balde agujereado.

## 4. Proyección abril (si las tendencias continúan)

Asumiendo adquisición plana (~195 brutos), churn acelerando (+~18 → ~86 churns) y ARPU en $15:

| Métrica | Marzo (real) | **Abril (proyectado)** |
|---|---|---|
| Usuarios | 1,480 | **~1,590** (+110 neto) |
| MRR | $22,200 | **~$23,850** (+7.4%) |
| Churns | 68 | **~86** |
| Churn rate | 5.04% | **~5.8%** |
| Net adds | +130 | **~+109** |
| LTV/CAC | 5.23x | ~5.0x (LTV sigue cayendo) |

**Lectura:** seguís creciendo en términos absolutos, pero el motor pierde fuerza cada mes — growth de 12.5%→9.6%→~7.4%. El número que decide tu trayectoria de 6 meses es el churn: si lo estabilizás en abril, el resto se corrige solo. Si no, en ~3-4 meses el churn alcanza a la adquisición y el crecimiento neto se aplana.

---

¿Querés que arme un mini-modelo (Excel/Sheets o script) con estas fórmulas para que metas los datos de abril y proyecte automáticamente distintos escenarios de churn?