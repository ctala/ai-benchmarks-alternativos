# GLM 5.3 — reasoning/business_analysis

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.01 | quality: 9.76
- latency_total: 106.733s | tokens_per_second: 75.0
- input_tokens: 183 | output_tokens: 8002
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Analiza estos datos de mi SaaS:

Enero: 1,200 usuarios, $18,000 MRR, 45 churns, CAC $85, LTV $420
Febrero: 1,350 usuarios, $20,250 MRR, 52 churns, CAC $92, LTV $415
Marzo: 1,480 usuarios, $22,200 MRR, 68 churns, CAC $78, LTV $408

Necesito:
1. Calcula las metricas clave (churn rate, growth rate, LTV/CAC ratio, net revenue retention)
2. Identifica tendencias preocupantes
3. Sugiere 3 acciones concretas basadas en los datos
4. Proyecta abril si las tendencias continuan


## Respuesta completa

# Análisis de tu SaaS (Enero–Marzo)

Resumen ejecutivo: tus unit economics son sanos, pero la retención se está deteriorando y es la causa de toda la desaceleración.

---

## 1. Métricas clave

| Métrica | Enero | Febrero | Marzo | Tendencia |
|---|---|---|---|---|
| Churn rate | 3.75% | 3.85% | 4.59% | ⚠️ Empeorando |
| Crecimiento usuarios | — | +12.5% | +9.6% | ⚠️ Desacelerando |
| Crecimiento MRR | — | +12.5% | +9.6% | ⚠️ Desacelerando |
| ARPU | $15.00 | $15.00 | $15.00 | Plano (cero expansión) |
| LTV/CAC | 4.9 | 4.5 | 5.2 | Volátil pero sano (>3) |
| NRR (estimado)* | n/d | ~95.7% | ~95.0% | ⚠️ Bajo 100% |

*Notas metodológicas: churn rate = churns/usuarios del mes. NRR estimado como (MRR inicial − MRR churneado)/MRR inicial, asumiendo cero expansión (el ARPU plano lo respalda) y churn al ARPU promedio. Si tienes datos de upgrades/downgrades, el NRR real puede variar.

**Hallazgo clave:** el ARPU es exactamente $15.00 los tres meses. Todo tu crecimiento depende 100% de adquisición; no hay ni un dólar de expansión.

---

## 2. Tendencias preocupantes (en orden de gravedad)

1. **Churn acelerando**: la tasa subió de 3.75% → 4.59% (+22% relativo en 2 meses). Los churns absolutos crecieron +51% (45→68) mientras los usuarios solo +23%. El lifetime esperado cayó de ~27 a ~22 meses.

2. **La desaceleración es 100% culpa del churn, no de adquisición.** Haz la resta: altas brutas = crecimiento neto + churns → Febrero: 150 + 52 = **202 altas**; Marzo: 130 + 68 = **198 altas**. Estás captando lo mismo (~200/mes), pero el churn se come cada vez más.

3. **NRR < 100%**: pierdes ~5% de revenue mensual de tu base existente. Eres un balde con fuga: sin adquisición constante, encoges.

4. **LTV en declive**: $420 → $408 (−2.9%). Y ojo: el churn implícito en tu LTV (~3.6%) es menor al churn observado (4.59%). Si recalcularas LTV con el churn real de marzo, sería ~$327, no $408. Probablemente tu LTV está desactualizado.

5. **Hipótesis a validar**: el CAC saltó a $92 en febrero y el churn saltó en marzo. ¿Capturaste usuarios de menor calidad ese mes? Vale la pena revisar la cohorte de febrero.

---

## 3. Tres acciones concretas

**① Diagnóstico de churn en 2 semanas (prioridad máxima)**
- Entrevista o encuesta a 15–20 de los 68 que cancelaron en marzo
- Segmenta churn por cohorte de adquisición, canal y antigüedad
- Implementa captura de "razón de cancelación" obligatoria en el flujo de baja
- Meta: identificar el motivo #1 y lanzar un fix en 30 días. Sospecha principal: la cohorte de febrero.

**② Crear ingreso de expansión para llevar NRR ≥ 100%**
- Con ARPU plano de $15, un plan superior o add-ons que suban el ARPU solo $1 (+6.7%) compensaría casi todo el churn de revenue (~5%)
- Lanza **planes anuales con descuento** (ej. 2 meses gratis): bloquean 12 meses de retención y adelantan caja
- Meta: NRR de 95% → 100%+ en un trimestre

**③ Blindar los primeros 90 días + recuperar pagos fallidos**
- La mayoría del churn SaaS ocurre en el primer trimestre: define tu métrica de activación ("aha moment") y rediseña el onboarding alrededor de ella
- Implementa dunning (recuperación de pagos fallidos) — en SaaS SMB suele representar 20–40% del churn total
- Meta: churn rate de vuelta a ≤3.75% en 60–90 días

---

## 4. Proyección de abril (si las tendencias continúan)

| Métrica | Marzo (real) | Abril (proyectado) |
|---|---|---|
| Usuarios | 1,480 | ~1,590 (+7.5%) |
| MRR | $22,200 | ~$23,850 |
| Churns | 68 | ~80–88 (rate ~5.2%) |
| CAC | $78 | ~$85 (es volátil) |
| LTV | $408 | ~$400 |
| NRR | ~95.0% | ~94.5% |

**⚠️ La proyección que debería preocuparte:** si las altas brutas siguen planas (~200/mes) y el churn sigue creciendo +15–20/mes, el crecimiento neto llega a **cero en ~6–7 meses** (septiembre–octubre), con el MRR estancándose alrededor de **$27–28K** y luego cayendo. Ese es el costo de no intervenir la retención ahora.

---

**Conclusión:** no tienes un problema de adquisición ni de unit economics (LTV/CAC > 4 es fuerte). Tienes un problema de retención que, sin acción, neutralizará todo tu crecimiento en medio año. Las acciones ① y ③ son urgentes; la ② es la palanca de mayor impacto a mediano plazo.

¿Quieres que te ayude a armar la encuesta de salida de churn o un template de análisis por cohortes?