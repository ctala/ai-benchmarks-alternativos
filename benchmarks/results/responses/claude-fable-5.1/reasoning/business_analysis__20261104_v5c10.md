# Claude Fable 5.1 — reasoning/business_analysis

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.81 | quality: 10.0
- latency_total: 62.02s | tokens_per_second: 74.1
- input_tokens: 256 | output_tokens: 4597
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y acciones concretas basadas en los datos.

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

# Análisis de métricas SaaS (Ene–Mar)

## 1. Métricas clave

**Datos derivados primero:**

| | Enero | Febrero | Marzo |
|---|---|---|---|
| ARPU (MRR / usuarios) | $15.00 | $15.00 | $15.00 |
| Altas brutas (netos + churns) | — | 202 | 198 |
| Altas netas | — | +150 | +130 |

**Métricas solicitadas:**

| Métrica | Enero | Febrero | Marzo |
|---|---|---|---|
| **Churn rate** (churns / usuarios al inicio del mes)* | 3.75% | 4.33% | 5.04% |
| **Growth rate** usuarios | — | 12.5% | 9.6% |
| **Growth rate** MRR | — | 12.5% | 9.6% |
| **LTV/CAC** | 4.9x | 4.5x | 5.2x |
| **NRR** (MRR inicial − MRR perdido) / MRR inicial** | ~96.3% | 95.7% | 95.0% |
| CAC payback (CAC / ARPU) | 5.7 meses | 6.1 meses | 5.2 meses |

\* Enero usa usuarios de cierre por falta de dato de diciembre.
\*\* No hay datos de expansión/upsell; como el ARPU es exactamente $15 los tres meses, asumo expansión = 0, por lo que NRR = GRR.

**⚠️ Nota sobre el LTV reportado:** con ARPU de $15, un LTV de $408 implica un churn mensual de ~3.7%. Tu churn real en marzo es 5.0%. Recalculando: **LTV real ≈ $15 / 0.0504 ≈ $298**, y el LTV/CAC real de marzo sería **~3.8x**, no 5.2x. Sigue siendo sano (>3x), pero tu LTV está sobreestimado ~35% y empeora cada mes.

---

## 2. Tendencias preocupantes

**🔴 Churn acelerándose (la más grave)**
Los churns crecieron 51% (45 → 68) mientras la base creció solo 23%. La tasa pasó de 3.75% a 5.04% en dos meses. Para un SaaS de ~$15/mes, 5% mensual = ~46% anual: pierdes casi la mitad de tus clientes cada año.

**🟠 Crecimiento desacelerando por el "balde agujereado"**
Las altas brutas están planas (~200/mes), pero el churn se come cada vez más: altas netas bajaron 150 → 130. Con 5% de churn necesitas ~74 nuevos usuarios/mes solo para no decrecer. Si la tendencia sigue, en menos de un año el churn absorbería toda tu adquisición.

**🟠 Cero expansión de ingresos**
ARPU clavado en $15. NRR < 100% y bajando. Todo tu crecimiento depende de nuevos logos, que es la forma más cara de crecer. Los SaaS saludables tienen NRR ≥ 100%.

**🟡 Señal sospechosa: CAC baja justo cuando el churn sube**
CAC de $92 → $78 en marzo mientras el churn salta. Hipótesis a validar: un canal más barato puede estar trayendo usuarios de menor calidad/fit. Correlación, no causalidad todavía, pero hay que mirarlo por cohorte.

---

## 3. Tres acciones concretas

**1. Diagnóstico de churn por cohorte y canal (esta semana)**
Segmenta los 68 churns de marzo por: mes de alta, canal de adquisición y uso del producto. Dos preguntas clave: ¿se van en los primeros 30 días (problema de onboarding) o después (problema de valor/competencia)? ¿Los churns se concentran en el canal "barato"? Agrega encuesta de salida obligatoria en el flujo de cancelación. Objetivo: volver a ≤4% en 60 días (eso solo ya recuperaría ~15 usuarios/mes y ~$2,700 de LTV mensual).

**2. Crear una palanca de expansión: planes anuales + tier superior**
- Plan anual con 15–20% de descuento: reduce churn mecánicamente (compromiso de 12 meses) y adelanta caja.
- Un tier de $25–30 con 1–2 features de alto valor para power users. Con que el 15% de la base suba de tier, el ARPU pasa de $15 a ~$17 y el NRR se acerca a 100% sin gastar un dólar en CAC.

**3. Corregir el LTV y poner guardarraíles al CAC por canal**
Recalcula el LTV con churn real (y con margen bruto si no lo estás incluyendo) y úsalo para decidir presupuesto. No escales el canal de CAC $78 hasta validar que su retención a 60–90 días es igual o mejor que la del resto. Establece como regla: LTV/CAC real ≥ 3x por canal, no solo en el agregado.

---

## 4. Proyección abril (si las tendencias continúan)

Supuestos: altas brutas ~198, churn rate sube ~0.7 pts → ~5.7%, ARPU $15, LTV sigue cayendo ~$8/mes, CAC vuelve al promedio (~$85).

| Métrica | Marzo | **Abril (proyectado)** |
|---|---|---|
| Churns | 68 | **~85** |
| Churn rate | 5.04% | **~5.7%** |
| Usuarios | 1,480 | **~1,590** (rango 1,575–1,600) |
| Altas netas | +130 | **~+113** |
| Growth rate | 9.6% | **~7.5%** |
| MRR | $22,200 | **~$23,850** (rango $23,600–$24,000) |
| NRR | 95.0% | **~94.3%** |
| LTV reportado / real | $408 / ~$298 | **~$400 / ~$263** |
| LTV/CAC real | 3.8x | **~3.1x** |

**Lectura:** abril todavía se vería "bien" en la superficie (+$1,650 de MRR), pero el LTV/CAC real tocaría el umbral de 3x y el crecimiento habrá caído a la mitad en tres meses. El churn es la métrica a atacar ahora; el resto se arregla solo si lo controlas.