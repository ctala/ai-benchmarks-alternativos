# Claude Haiku 4.5 (suscripción) — reasoning/business_analysis

- model_id: `claude-haiku-4-5`
- success: True  | final: 7.58 | quality: 9.8
- latency_total: 37.848s | tokens_per_second: 110.9
- input_tokens: 10 | output_tokens: 4197
- judge_score: 5.0 | justificación: 

## Respuesta completa

Te haré un análisis cuantitativo completo de tu SaaS. Voy a calcular las métricas, identificar las banderas rojas y proyectar.

## 1. MÉTRICAS CLAVE CALCULADAS

| Métrica | Enero | Febrero | Marzo | Cambio |
|---------|-------|---------|-------|--------|
| **Churn Rate** | 3.75% | 3.85% | 4.59% | ⚠️ +22.4% |
| **Growth Rate (Usuarios)** | — | +12.5% | +9.63% | ⬇️ Decelerando |
| **ARPU** | $15.00 | $15.00 | $15.00 | ✅ Estable |
| **LTV/CAC Ratio** | 4.94 | 4.51 | 5.23 | 🔄 Volátil |
| **Net Revenue Retention** | — | 95.7% | 94.9% | ⚠️ Bajando |
| **MRR Growth** | — | +12.5% | +9.63% | ⬇️ Sincronizado con usuarios |

**Detalle de cálculos:**

```
Churn Rate = Churns / Usuarios inicio período
Enero: 45/1,200 = 3.75%
Febrero: 52/1,350 = 3.85%
Marzo: 68/1,480 = 4.59%

NRR = (Revenue retenida) / (MRR inicio)
Febrero: ($18,000 - $780 churn) / $18,000 = 95.7%
Marzo: ($20,250 - $1,020 churn) / $20,250 = 94.9%

ARPU = MRR / Usuarios = Constante $15/mes
```

---

## 2. TENDENCIAS PREOCUPANTES 🚨

### 🔴 **CRÍTICA: Churn acelerador**
- **Progresión**: 3.75% → 3.85% → 4.59%
- **Velocidad**: +22% en 2 meses
- **Impacto**: A este ritmo, perderás **~6% del base en abril**
- **Síntomas**: Podría ser producto (feature gap, bugs), precio (competencia), o onboarding (churn temprano)

### 🟠 **ALTA: LTV cayendo mientras CAC está volátil**
- **LTV**: $420 → $415 → $408 (-2.9%)
- **CAC**: $85 → $92 → $78 (±8.5%)
- **Ratio LTV/CAC**: Aunque suena bien (5.23), está siendo sostenido por CAC bajo en marzo, NO por LTV fuerte
- **Riesgo**: Si vuelves a gastar $92 en CAC pero los clientes siguen churning a 4.59%, el ratio se derrumba a 4.43

### 🟡 **MODERADA: Desaceleración de crecimiento**
- **Usuarios**: 12.5% → 9.63% (decayendo)
- **Patrón**: Growth es lineal con churn, así que a menos que bajes churn **no recuperarás velocidad de crecimiento**

### 🔵 **CONTEXTUAL: NRR sub-95%**
- Estándares SaaS: >110% es excelente, >100% es healthy, <90% es crítico
- **Tu posición**: 94.9% = borderline. El churn está comiéndose la expansión

---

## 3. TRES ACCIONES CONCRETAS (PRIORIDAD)

### **Acción 1: Auditoría de Churn (Semana 1) — URGENTE**
Responde estas preguntas con data:
- **¿Qué cohorte está churnando?** Nuevos clientes (0-3 meses) o base histórica?
  - Si es onboarding → fix product docs, trial UX, o early touch points
  - Si es base → problema de producto o competencia
- **¿Cuál es la razón #1 según exit surveys?** (Si no los tienes, implementa hoy)
- **¿A qué día del ciclo churnan?** (Ej. siempre en día 60 → problema de feature específica o renovación de contrato)

**Owner**: Product/CS | **Métrica de éxito**: Reducir a 3.5% en abril

---

### **Acción 2: Alineación Precio ↔ Producto (Semana 2)**
El ARPU plano ($15) + CAC volátil sugieren:
- **Analiza**: ¿Qué % de clientes nuevos (marzo) son menor tier que enero?
  - Si CAC bajó a $78 pero ARPU es igual, podría ser estrategia de volumen (bien) o degradación de mix (mal)
- **Test**: En abril, prueba +5-10% en precios para nuevos clientes (A/B con cohorte pequeña)
  - Si elasticidad es baja, ganas 5% más MRR inmediato
  - Si conversión cae, aborta en 2 semanas

**Owner**: Growth/Pricing | **Métrica de éxito**: Aumentar ARPU a $15.50+ o LTV a $420+

---

### **Acción 3: Reactivación de Churn (Inmediato)**
Implementa esto en 48h:
- **Winback email**: A los 68 clientes que churnaron en marzo, ofrece 50% descuento X 3 meses si regresan
- **Cost**: ~$700 (si 10% rebota = $350 MRR recuperado, ROI 2:1)
- **Tracking**: Mide tasa de reactivación por cohorte de exit

**Owner**: Customer Success | **Métrica de éxito**: Recuperar 5-10% de los churn recientes

---

## 4. PROYECCIÓN ABRIL (Si tendencias continúan) 📈

**Supuestos**:
- Churn rate sigue acelerando: +0.74% cada mes → 5.35% en abril
- Crecimiento de usuarios sigue decelerando: -2.87% cada mes → 8.2% en abril
- ARPU y CAC siguen su tendencia (ARPU plano, CAC hacia $76)

| Métrica | Marzo (Real) | Abril (Proyectado) | Cambio |
|---------|-------------|------------------|--------|
| Usuarios | 1,480 | **1,601** | +8.2% |
| Churn | 68 | **85** | +25% |
| MRR | $22,200 | **$24,015** | +8.2% |
| CAC | $78 | ~$76 | -2% |
| LTV | $408 | ~$401 | -1.7% |
| LTV/CAC | 5.23 | **5.28** | Plano |
| Churn Rate | 4.59% | **5.35%** | 🚨 +0.76pp |

**Interpretación**: En abril ganarás ~$1.8k MRR más, **pero perderás esa ganancia en churn adicional** si no actúas. El sistema está en equilibrio inestable.

---

## 🎯 RESUMEN EJECUTIVO

| Señal | Estado | Riesgo |
|-------|--------|--------|
| **Crecimiento** | Decelerando pero positivo (8.2% proyectado) | MEDIA — puede revertirse con product wins |
| **Churn** | **ACELERADOR** (3.75% → 4.59% → 5.35%) | 🔴 CRÍTICA — urgente diagnóstico |
| **Unit Economics** | LTV cayendo, CAC volátil | 🟡 RIESGO — ratio está inflado por CAC bajo |
| **Health General** | NRR < 95%, no hay margen de error | 🟠 MODERADA — tienes 4-6 semanas antes de que se desmorona |

**La buena noticia**: Aún creces y tus ratios base son saludables (5.23 LTV/CAC es bueno). **La mala**: El churn acelerador es canario en la mina. Si lo controlas en abril, vuelves a 12%+ growth. Si no, caerás en mayo.

¿Quieres que profundice en alguna métrica específica o haga un análisis de sensibilidad (ej: "si reduzco churn 1%, cuál es el impacto en MRR")?