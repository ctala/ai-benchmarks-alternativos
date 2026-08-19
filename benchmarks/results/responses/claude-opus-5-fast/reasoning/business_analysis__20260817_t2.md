# Claude Opus 5 Fast — reasoning/business_analysis

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.7 | quality: 9.76
- latency_total: 33.112s | tokens_per_second: 218.6
- input_tokens: 254 | output_tokens: 7237
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un análisis detallado y acciones concretas basadas en los datos.

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

# Análisis de métricas SaaS — Q1

**Supuestos que estoy aplicando** (corrígeme si difieren): los usuarios son cifras de *fin de mes*, el churn es de logos (cuentas) no de MRR, y no hay datos de diciembre ni de márgenes brutos.

---

## 1. Métricas clave

### Dato base: ARPU perfectamente plano
| Mes | MRR | Usuarios | ARPU |
|---|---|---|---|
| Ene | $18,000 | 1,200 | **$15.00** |
| Feb | $20,250 | 1,350 | **$15.00** |
| Mar | $22,200 | 1,480 | **$15.00** |

Un ARPU idéntico tres meses seguidos significa **cero expansión, cero upsell, cero contracción**. Todo tu crecimiento es 100% volumen de logos nuevos. Este es el hallazgo estructural más importante del set.

### Churn
| Mes | Churns | % sobre base inicial | % anualizado |
|---|---|---|---|
| Ene | 45 | n/d (falta base de dic) | — |
| Feb | 52 | **4.33%** | 41.2% |
| Mar | 68 | **5.04%** | 46.2% |

Sobre base de cierre (comparable entre los tres meses): 3.75% → 3.85% → **4.59%**. La aceleración de marzo es real, no un artefacto de la métrica.

### Crecimiento
| Métrica | Ene→Feb | Feb→Mar |
|---|---|---|
| Crecimiento MRR | **12.50%** | **9.63%** |
| Altas brutas (calculadas) | 202 | 198 |
| Altas netas | 150 | 130 |

Reconstrucción: Feb = 1,200 − 52 + **202**; Mar = 1,350 − 68 + **198**. **Las altas brutas están estancadas (–2%) mientras el churn creció +31%.** Todo el frenazo del crecimiento viene del churn, no de la adquisición.

### LTV/CAC
| Mes | LTV | CAC | Ratio | Payback (bruto) |
|---|---|---|---|---|
| Ene | $420 | $85 | 4.94x | 5.7 meses |
| Feb | $415 | $92 | 4.51x | 6.1 meses |
| Mar | $408 | $78 | **5.23x** | 5.2 meses |

⚠️ **Estos LTV no cuadran con tu churn real.** Un LTV de $408 con ARPU $15 implica una vida media de 27 meses = churn de 3.68%. Tu churn real de marzo es 5.04%.

**LTV recalculado (marzo):** $15 / 0.0504 = **$298** bruto. Aplicando un margen bruto típico de 80% → **$238**.
**LTV/CAC real:** 238 / 78 = **3.05x**, no 5.23x. Estás en el umbral mínimo aceptable, no en zona cómoda.

### Net Revenue Retention
| Mes | MRR perdido | NRR | GRR |
|---|---|---|---|
| Feb | 52 × $15 = $780 | **95.7%** | 95.7% |
| Mar | 68 × $15 = $1,020 | **95.0%** | 95.0% |

NRR = GRR porque no existe expansión. Un SaaS sano en SMB está en 100–110%; best-in-class >120%. Estás **25 puntos por debajo del benchmark**.

### Quick Ratio SaaS
(MRR nuevo + expansión) / (MRR perdido + contracción)
- Febrero: $3,030 / $780 = **3.88**
- Marzo: $2,970 / $1,020 = **2.91**

Cayó por debajo de 4 en un solo mes. Bajo 2 es zona de alarma.

---

## 2. Tendencias preocupantes

**🔴 Crítico — El churn se acelera más rápido que la adquisición**
+31% de churns en un mes con altas planas. Si extrapolas, el techo de tu negocio es: 198 altas ÷ 5.5% churn ≈ **3,600 usuarios (~$54K MRR)**, punto donde el crecimiento se detiene solo. Con churn en 6.5%, el techo baja a ~3,050 usuarios.

**🔴 Crítico — LTV reportado inflado ~37%**
Estás tomando decisiones de inversión en adquisición con un LTV/CAC de 5x cuando el real ronda 3x. Si el churn llega a 6%, el LTV cae a $250 bruto / $200 neto y el ratio baja a **2.5x**: por debajo del umbral de rentabilidad sana.

**🟠 Alto — Cero expansión revenue**
Tres meses con ARPU clavado en $15.00 sugiere pricing de tarifa única sin palancas de upgrade (asientos, uso, tiers). Sin expansión, cada punto de churn se paga íntegro con CAC nuevo. Es el motivo estructural de que el NRR esté en 95%.

**🟠 Alto — Correlación sospechosa CAC ↓ / churn ↑**
En marzo el CAC bajó 15% ($92→$78) y el churn subió 31%. El patrón clásico es un cambio de mix de canal hacia tráfico barato y de baja intención (descuentos, paid social amplio, afiliados) que convierte peor a largo plazo. **El CAC de marzo no es una mejora de eficiencia hasta que veas la cohorte a 90 días.**

**🟡 Medio — Adquisición estancada**
202 → 198 altas brutas. Aunque arreglaras el churn, la máquina de adquisición no está escalando. Dos problemas simultáneos, no uno.

---

## 3. Tres acciones concretas

### Acción 1 — Auditoría de cohortes y rescate de los primeros 60 días
**Qué hacer:** segmenta los 165 churns del trimestre por (a) antigüedad al cancelar, (b) canal de adquisición, (c) evento de activación completado o no. En SaaS con ARPU $15 típicamente el 50–60% del churn ocurre en los primeros 60 días → es problema de activación/onboarding, no de producto maduro.
Define **un** evento de activación medible, mide qué % lo alcanza en 7 días, y dispara intervención (email + in-app + llamada si el ticket lo justifica) a quien no lo alcance.

**Impacto cuantificado:** bajar el churn de 5.04% a 3.5% retiene ~23 usuarios/mes y sube el LTV de $298 a **$428** (+44%). El LTV/CAC real pasa de 3.05x a **4.4x**. En 12 meses eso son ~$41K de MRR adicional acumulado frente al escenario base.

### Acción 2 — Lanzar una palanca de expansión antes del 30 de abril
**Qué hacer:** rompe el ARPU plano. La vía más rápida con ARPU $15 no es un plan enterprise, es una **métrica de valor escalable**: asientos adicionales, límite de uso/registros, o un add-on de $8–10 (integraciones, reportes, API). Y activa un tier superior a $29 con paywall visible dentro del producto.

**Impacto cuantificado:** con solo un 3% de MRR de expansión mensual, el NRR pasa de 95% a **98%**, y con 6% superas el 100% (crecimiento sin adquirir a nadie). Sobre la base de marzo, 3% = **+$666/mes compuesto**, con CAC marginal ≈ $0.

**Meta:** NRR >100% en Q3.

### Acción 3 — Reauditar el mix de canales por calidad, no por coste
**Qué hacer:** desglosa los 198 usuarios nuevos de marzo por canal y calcula CAC *y* retención a 30/60 días de cada uno. Congela o recorta el 30% de gasto en el canal que trajo el CAC más barato si su churn a 60 días supera la media. Reasigna a los canales con mejor retención aunque su CAC sea $110–120: con LTV real de $298, un CAC de $110 sigue dando 2.7x si el usuario retiene bien, y es mejor negocio que $78 con churn del 8%.

**Impacto cuantificado:** si el 40% de los churns de marzo se concentra en un canal, eliminarlo baja el churn ~1.5 pp de inmediato, aunque cueste 20–30 altas brutas al mes. Matemáticamente sales ganando: pierdes 25 usuarios de baja calidad y retienes 20 de alta calidad con LTV 40% mayor.

---

## 4. Proyección de abril

**Metodología:** altas brutas siguiendo la tendencia (–2% m/m) → 194. Churn extrapolando la pendiente de +0.7 pp/mes → 5.7% sobre base de 1,480 → 84 bajas. ARPU constante $15.

| Métrica | Marzo (real) | **Abril (proyectado)** | Δ |
|---|---|---|---|
| Usuarios | 1,480 | **1,590** | +110 |
| Altas brutas | 198 | 194 | –4 |
| Churns | 68 | **84** | +16 |
| Churn rate | 5.04% | **5.68%** | +0.64 pp |
| MRR | $22,200 | **$23,850** | +$1,650 |
| Crecimiento MRR | 9.63% | **7.43%** | –2.2 pp |
| NRR | 95.0% | **94.3%** | –0.7 pp |
| LTV real (bruto) | $298 | **$264** | –$34 |
| CAC | $78 | ~$85 (media trim.) | — |
| LTV/CAC real (80% GM) | 3.05x | **2.48x** | ⚠️ bajo umbral |
| Quick Ratio | 2.91 | **2.31** | –0.60 |

### Lectura de la proyección
Abril todavía "se ve bien" en el reporte de arriba: MRR crece, usuarios crecen. **Pero es el mes en que la unit economics real cruza por debajo de 3x.** El deterioro está escondido bajo un MRR que sigue subiendo.

**Extendiendo la misma tendencia:**
- **Mayo:** ~1,690 usuarios, $25,350 MRR, crecimiento 6.3%, churn 6.4%
- **Junio:** ~1,780 usuarios, $26,700 MRR, crecimiento 5.3%, churn 7.1%
- **Punto de estancamiento (altas = bajas):** en torno a **2,900–3,100 usuarios (~$45K MRR)**, alcanzable hacia el Q4 si nada cambia.

Estás a **2–3 meses** de que el crecimiento se vuelva visiblemente plano en el propio dashboard de MRR. El momento de intervenir es ahora, mientras las métricas de superficie aún son positivas y tienes caja y tiempo.

---

## Datos que necesito para afinar el análisis

1. **Base de usuarios de diciembre** → cierra el churn rate de enero y confirma la pendiente.
2. **Churn de MRR vs. churn de logos** → si los que cancelan son cuentas de ticket alto, el daño es peor de lo calculado.
3. **Margen bruto real** → todos los LTV netos de arriba asumen 80%.
4. **Churns desglosados por antigüedad de cohorte** → determina si el problema es onboarding o producto. Es la variable que decide cuál de las 3 acciones va primero.
5. **Altas por canal con su retención** → valida o descarta la hipótesis del CAC barato de marzo.

Si me pasas el desglose de cohortes o el churn por canal, refino el modelo y priorizo las acciones por ROI esperado.