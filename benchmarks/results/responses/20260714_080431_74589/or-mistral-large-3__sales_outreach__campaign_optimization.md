# Mistral Large 3 675B — sales_outreach/campaign_optimization

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 27.16s | tokens_per_second: 64.7
- input_tokens: 303 | output_tokens: 1757
- judge_score: 5.0 | justificación: 

## Respuesta completa

Vamos a analizar cada punto con detalle:

---

### **1. Métricas por campaña**
*(Fórmulas: CTR = Clicks/Impresiones; CPC = Costo/Clicks; CPA = Costo/Signups; CR = Signups/Clicks)*

| **Campaña**       | **CTR**  | **CPC**  | **CPA**  | **Conversion Rate (CR)** |
|-------------------|----------|----------|----------|--------------------------|
| **Campaña A**     | 3.0%     | $1.40    | $46.67   | 3.0%                     |
| **Campaña B**     | 4.0%     | $0.38    | $75.00   | 0.5%                     |
| **Campaña C**     | 6.0%     | $3.56    | $88.89   | 4.0%                     |

**Detalles:**
- **Campaña A**: Buen equilibrio entre CTR, CR y CPA. Es la más eficiente en costo por adquisición.
- **Campaña B**: Alto CTR y bajo CPC, pero **CR muy bajo** (0.5%). Atrae tráfico informativo, no conversiones.
- **Campaña C**: Alto CTR y CR, pero **CPA elevado** ($88.89). Es cara, pero genera leads de alta intención (usuarios comparando con competidores).

---

### **2. ¿Qué campaña escalar y cuál pausar?**
#### **Escalar: Campaña A**
**Razones:**
- **CPA más bajo** ($46.67 vs $75-$89 de las otras).
- **CR sólido** (3.0%), lo que indica que el mensaje y la landing son efectivos.
- **Keywords transaccionales** ("software gestión inventario"), con usuarios listos para comprar.
- **ROI positivo**: Por cada $46.67 gastados, obtienes un signup. Si el **LTV (Lifetime Value)** de un cliente es mayor a $46.67, es rentable.

#### **Pausar: Campaña B**
**Razones:**
- **CR extremadamente bajo** (0.5%). Aunque el CPC es barato, **solo 24 signups en 4,800 clics** indican que el tráfico no es cualificado.
- **Keywords informativas** ("cómo gestionar inventario"): Los usuarios buscan información, no una solución de pago.
- **CPA alto** ($75) para el tipo de tráfico que genera.

#### **Mantener (pero optimizar): Campaña C**
- **CR alto** (4.0%), pero **CPA elevado** ($88.89).
- **Oportunidad**: Los usuarios que buscan alternativas a competidores tienen **alta intención de compra**, pero el costo es prohibitivo.
- **Acciones**:
  - Reducir presupuesto temporalmente y optimizar pujas para bajar el CPA.
  - Mejorar la landing para aumentar CR (ej: destacar diferenciadores vs competidor).

---

### **3. Redistribución del presupuesto ($5,000)**
**Objetivo**: Maximizar signups con un CPA sostenible.

| **Campaña**       | **Presupuesto actual** | **Presupuesto propuesto** | **Justificación**                                                                 |
|-------------------|------------------------|---------------------------|-----------------------------------------------------------------------------------|
| **Campaña A**     | $2,100                 | **$3,500**                | Es la más eficiente. Aumentar presupuesto para captar más tráfico transaccional. |
| **Campaña B**     | $1,800                 | **$0**                    | Pausar por bajo CR.                                                              |
| **Campaña C**     | $3,200                 | **$1,500**                | Mantener, pero reducir presupuesto hasta optimizar el CPA.                       |

**Distribución final**:
- **Campaña A**: $3,500 (70%)
- **Campaña C**: $1,500 (30%)

**Resultado esperado**:
- **Signups totales**: ~100-120 (vs 105 actuales).
- **CPA promedio**: ~$45-$50 (vs $50 actual).

---

### **4. A/B Tests para el próximo mes**
#### **Para Campaña A (Landing principal)**:
1. **Variantes de landing page**:
   - **Test A**: Landing actual (formulario largo + CTA "Prueba gratis").
   - **Test B**: Landing con **formulario corto** (solo email) + CTA "Descarga guía gratuita" (lead magnet) para luego nurturear con email marketing.
   - **Métrica**: CR y CPA.

2. **CTA en anuncios**:
   - **Test A**: "Prueba gratis 14 días" (actual).
   - **Test B**: "Descubre cómo [beneficio clave] en 2 minutos" (ej: "Descubre cómo reducir errores de inventario en 2 minutos").
   - **Métrica**: CTR y CR.

3. **Keywords**:
   - **Test A**: "software gestión inventario" (actual).
   - **Test B**: "mejor software para inventario de pymes" (long-tail con mayor intención).
   - **Métrica**: CTR, CR y CPA.

#### **Para Campaña C (Competidor)**:
1. **Mensaje en anuncios**:
   - **Test A**: "[Competidor] vs [Tu marca]: Comparativa honesta" (actual).
   - **Test B**: "¿Cansado de [dolor del competidor]? Prueba [Tu marca]" (enfoque en problema).
   - **Métrica**: CTR y CR.

2. **Landing page**:
   - **Test A**: Comparativa lado a lado (actual).
   - **Test B**: Landing con **testimonios de clientes** que migraron desde el competidor.
   - **Métrica**: CR y CPA.

3. **Pujas**:
   - **Test A**: Pujas manuales (actual).
   - **Test B**: Pujas automáticas con **estrategia de "Maximizar conversiones"** (para reducir CPA).
   - **Métrica**: CPA y volumen de signups.

#### **Para Campaña B (si se reactiva)**:
- **Solo si se optimiza**:
  - **Test A**: Enviar tráfico a un **lead magnet** (ej: "Guía gratuita: 5 errores de inventario que arruinan tu restaurante") en lugar de la landing de signup.
  - **Test B**: Usar **retargeting** para nutrir a los usuarios que descargaron la guía y luego ofrecerles una demo.
  - **Métrica**: Tasa de descarga del lead magnet y CR posterior.

---

### **Resumen de acciones clave**:
1. **Escalar Campaña A** (presupuesto a $3,500) y pausar Campaña B.
2. **Optimizar Campaña C** (reducir presupuesto a $1,500 y probar A/B tests para bajar CPA).
3. **Priorizar tests** que mejoren CR (landing pages, CTAs) y reduzcan CPA (pujas, keywords).
4. **Monitorear LTV**: Si el CPA de $46-$50 es sostenible con el valor de vida del cliente, sigue escalando.

**Nota**: Si el **LTV de un cliente es bajo** (ej: $40), la Campaña A no es rentable. En ese caso, enfócate en **reducir CPA** (ej: mejorar CR con tests) o **aumentar LTV** (upselling, cross-selling).