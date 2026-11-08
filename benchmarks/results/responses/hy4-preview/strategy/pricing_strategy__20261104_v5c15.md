# Tencent Hy4 preview — strategy/pricing_strategy

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.09 | quality: 10.0
- latency_total: 351.464s | tokens_per_second: 63.9
- input_tokens: 201 | output_tokens: 22450

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

Aquí tienes un análisis completo con supuestos explícitos. Usaré **LTV ajustado por margen bruto** (la métrica correcta para SaaS) y también mostraré el LTV de ingresos para que compares con tu número actual.

---

## 0) Foto actual (baseline)

| Métrica | Valor |
|---|---:|
| Precio / mes | **$60** |
| Costo variable / mes | **$8** |
| Margen bruto / mes | **$52** (86.7%) |
| Churn mensual | **7%** |
| Vida media del cliente | **1 / 0.07 = 14.3 meses** (casi tus 14 meses) |
| CAC | **$120** |
| Clientes actuales | **200** |
| MRR actual | **$12,000** |
| Margen bruto MRR actual | **$10,400** |

**Unit economics hoy (usando 14.3 meses):**

- **LTV (ingresos)** = $60 / 0.07 = **$857** → LTV/CAC = **7.1x**
- **LTV (margen)** = $52 / 0.07 = **$743** → LTV/CAC = **6.2x**
- **Payback** = $120 / $52 = **2.3 meses**

> Si usas exactamente 14 meses: LTV ingresos = $840 (ratio 7.0x) y LTV margen = $728 (ratio 6.1x). La conclusión no cambia.

**Conclusión base:** tu negocio ya es saludable (todo >3x, ideal >5x). El problema no es el LTV/CAC, sino que **estás dejando dinero sobre la mesa** y tu churn (7% mensual = ~58% anual) es alto para SaaS B2B.

---

## 1) ¿Cómo cambiaría el LTV/CAC si subes a $89 y el churn NO cambia?

Si el churn se mantuviera en 7% (escenario puramente matemático):

| Métrica | Hoy ($60) | Con $89 (mismo churn) |
|---|---:|---:|
| Ingresos / mes | $60 | **$89** |
| Margen / mes | $52 | **$81** (91%) |
| LTV ingresos | $857 | **$1,271** |
| LTV margen | $743 | **$1,157** |
| LTV/CAC ingresos | 7.1x | **10.6x** |
| LTV/CAC margen | 6.2x | **9.6x** |
| Payback | 2.3 meses | **1.5 meses** |

**Pero el churn sí reacciona al precio.** Por eso el análisis importante son los umbrales:

- **Umbral de LTV:** si el churn mensual se mantiene **por debajo de 10.9%**, el LTV por cliente (margen) sigue siendo **mayor** que hoy, aunque el churn suba.
- **Umbral de ratio LTV/CAC si el CAC también sube:**
  - Si CAC sube a **$150**, el churn debe mantenerse **<8.7%** para superar el ratio actual de 6.2x.
  - Si CAC sube a **$190**, el churn **no puede subir nada** (debe quedarse ~6.9% o menos) para mantener el ratio actual.

---

## 2) Impacto esperado en churn (benchmarks SaaS)

Tu aumento es **+$29 (+48.3%)**. Puntos clave con benchmarks de la industria (ProfitWell / Price Intelligently / OpenView / SaaS Capital):

1. **$89 está dentro del rango competitivo** ($29–$149). De hecho, **$89 es exactamente el punto medio** del rango de tus competidores, así que no es un precio “fuera de mercado”.
2. **Aumentos pequeños (5–15%)** bien comunicados suelen aumentar el churn solo **0–1 punto porcentual**.
3. **Aumentos grandes (>30%) en SMB** tienen una elasticidad de retención típica de **0.5 a 1.0**. Un aumento del **48%** puede traducirse en un aumento *relativo* del churn de **25% a 70%**.
   - Eso significa pasar de **7% → 8.5% a 12% mensual** si no se gestiona bien.
4. **Choque de transición:** si subes el precio de golpe a clientes actuales sin “grandfathering”, es normal perder entre **10% y 30% de la base** en el momento del cambio.
5. **Adquisición (CAC):** un precio 48% más alto suele reducir la conversión de nuevos leads entre **20% y 40%**, lo que encarece el CAC. Por eso modelo CAC de **$120 → $150 (realista) o $190 (pesimista)**.

Con esto, los escenarios son:

---

## 3) Escenarios (precio $89, costo $8, margen $81)

> Proyección de **solo la base actual de 200 clientes**, sin contar nuevos clientes, para aislar el efecto del precio.

| Escenario | Aceptan $89 (retención inicial) | Churn mensual post | CAC | Vida media | LTV margen | LTV/CAC margen | Payback | MRR tras migración | Margen bruto mensual | Margen bruto acumulado 12 meses |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Hoy (base)** | 200 clientes a $60 | 7.0% | $120 | 14.3 m | $743 | **6.2x** | 2.3 m | $12,000 | $10,400 | **$86,300** |
| **Optimista** | **90%** (180) | **7.5%** | $120 | 13.3 m | $1,080 | **9.0x** | 1.5 m | **$16,020** (+34%) | **$14,580** (+40%) | **$118,100** (+37%) |
| **Realista** | **75%** (150) | **9.0%** | $150 | 11.1 m | $900 | **6.0x** | 1.9 m | **$13,350** (+11%) | **$12,150** (+17%) | **$91,500** (+6%) |
| **Pesimista** | **60%** (120) | **12.0%** | $190 | 8.3 m | $675 | **3.6x** | 2.3 m | **$10,680** (-11%) | **$9,720** (-6.5%) | **$63,500** (-26%) |
| **Pesimista extremo** (sensibilidad) | 55% (110) | 14% | $200 | 7.1 m | $579 | **2.9x** | 2.5 m | $9,790 | $8,910 | ~$55k |

**Lectura clave:**

- En **optimista y realista**, el margen bruto anual sube (+37% y +6%) aunque pierdas 10% o 25% de clientes.
- En **realista**, el ratio LTV/CAC (6.0x) es casi igual al de hoy (6.2x), **pero el beneficio por cliente (LTV – CAC) sube de $623 a $750 (+20%)** porque el margen mensual es mucho mayor.
- En **pesimista**, el ratio sigue >3x, pero el LTV por cliente cae a $675 (vs $743 hoy) y el margen anual cae 26%. Ahí sí duele.
- **Punto de equilibrio para no perder margen bruto anual:**
  - Con churn 7.5% → necesitas retener **~66%** de la base.
  - Con churn 9% → necesitas retener **~71%**.
  - Con churn 12% → necesitas retener **~82%** (muy difícil si haces un salto brusco).

---

## 4) Recomendación (con números concretos)

### ✅ Sí, deberías subir a $89 — pero NO de golpe a toda la base

El precio de $89 está justificado (es el punto medio del mercado, tu costo es solo $8 y tu margen actual ya es alto). Sin embargo, un salto del **48% de una sola vez a clientes actuales** tiene un riesgo real de churn y de pérdida de MRR si no se gestiona.

**Números que debes tener claros:**

- Hoy ganas **$10,400 de margen bruto mensual** con 200 clientes.
- Si subes a $89 y **solo se queda el 64%** de la base (128 clientes), igualas tu margen bruto mensual actual.
- Si se queda el **67%**, igualas tu MRR actual.
- Pero para no perder margen **anual** con un churn de 9%, necesitas retener al **~71%**. Por eso el escenario de “subida universal inmediata” es una apuesta.

### Recomendación concreta

1. **Sube el precio a $89 inmediatamente SOLO para nuevos clientes** (o crea un tier “Pro” a $89).  
   - Mantén a los 200 actuales en **$60 como plan “legacy / grandfathered”** por 6–12 meses.  
   - Esto captura el upside sin arriesgar tus $10,400 de margen mensual actual.

2. **Mide la cohorte nueva durante 60–90 días.**  
   - Guardarraíl: si la cohorte $89 tiene **churn >10.9%** o **CAC >$190**, no la uses como modelo para migrar a la base actual.

3. **Si la cohorte nueva se comporta en escenario realista u optimista (churn ≤9%, CAC ≤$150), entonces migra a los actuales de forma gradual:**
   - Mes 6: **$60 → $75** (+25%). Un aumento <30% está dentro del rango “seguro” según benchmarks.
   - Mes 12: **$75 → $89** (+18.7%).  
   Esto evita el choque de 48% de una sola vez.

4. **Alternativa recomendada (aún mejor): “price fencing” / packaging**  
   En lugar de subir el precio plano, lanza:
   - **Basic: $60** (o $59) con límites o menos features.
   - **Pro: $89** con multi-almacén, reportes avanzados, integraciones, etc.  
   Así los clientes sensibles al precio se quedan en $60 y los que valoran el producto pagan $89. Subes el ARPU mezclado sin forzar churn.

5. **Ataca el churn en paralelo.**  
   7% mensual es alto (~58% anual). Si logras bajarlo a 5% y cobras $89:
   - LTV margen = $81 / 0.05 = **$1,620**
   - LTV/CAC = **13.5x** (vs 6.2x hoy).  
   Reducir churn potencia muchísimo más el valor de la subida de precio.

---

## 5) Estrategia de implementación sugerida

| Paso | Acción | Timing |
|---|---|---|
| 1 | **Documenta y comunica valor/ROI** (ahorro de horas, reducción de quiebres de stock). Un cliente que ahorra $300–$500/mes no se va por $29 más. | Antes del aumento |
| 2 | **A/B test en nuevos leads**: cotiza $89 a todos los prospectos nuevos. Mide conversión y CAC. | Día 0–30 |
| 3 | **Grandfathering a actuales**: comunica que los 200 clientes actuales mantienen $60 como “precio de por vida” o por 12 meses. | Día 0 |
| 4 | **Lanza plan Pro $89** para nuevos clientes y para quien quiera nuevas features. Ofrece **prepago anual**: $890/año (~$74/mes) para mejorar caja y bajar churn. | Día 0–30 |
| 5 | **Migración gradual de legacy**: avisa con 30–60 días. Sube a $75 y luego a $89, o dales opción de quedarse en Basic $60. Usa contratos anuales para fijar precio. | Mes 6–12 |
| 6 | **Monitorea cohortes separadas** ($60 legacy vs $89 nuevo). Vigila: churn mensual, downgrade rate, CAC por cohorte, LTV/CAC por cohorte. Si la cohorte $89 baja de 3x LTV/CAC o churn >10.9%, pausa y ajusta packaging. | Continuo |

### En resumen
- **Sube a $89 para nuevos clientes ya.**
- **No hagas un salto de $60 → $89 a la base actual sin grandfathering o migración gradual.**
- Con una migración bien hecha, el escenario más probable es el **realista/optimista**: más margen, mejor LTV por cliente y payback más rápido, sin destruir tu base instalada.