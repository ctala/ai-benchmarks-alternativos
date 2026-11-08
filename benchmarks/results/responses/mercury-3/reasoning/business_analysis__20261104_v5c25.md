# Mercury 3 — reasoning/business_analysis

- model_id: `inception/mercury-3`
- success: True  | final: 8.37 | quality: 9.44
- latency_total: 22.478s | tokens_per_second: 482.9
- input_tokens: 157 | output_tokens: 10854
- judge_score: 4.6 | justificación: 

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

¡Hola! He analizado los datos de tu SaaS. Aquí tienes el desglose completo con las métricas, las señales de alerta, acciones recomendadas y la proyección para abril.

---

## 1. Métricas clave

| Métrica | Fórmula | Enero | Febrero | Marzo |
|---|---|---|---|---|
| **Churn rate mensual** | Churns ÷ clientes al inicio del mes | ~3,7%* | 4,3% | 5,0% |
| **Growth rate (usuarios/MRR)** | (Fin − Inicio) ÷ Inicio | — | 12,5% | 9,6% |
| **LTV/CAC** | LTV ÷ CAC | 4,94 | 4,51 | 5,23 |
| **Net Revenue Retention (NRR)** | 1 − churn de ingresos** | ~96,3% | 95,7% | 95,0% |
| **ARPU** | MRR ÷ usuarios | $15 | $15 | $15 |

*Enero: al no tener el número de clientes iniciales, usé el total del mes como proxy. Para febrero y marzo usé el saldo inicial del mes anterior.  
**Sin datos de expansión/contracción, asumo que el único cambio en el MRR existente es el churn. Como el ARPU es constante, el NRR = 1 − churn rate.

---

## 2. Tendencias preocupantes

1. **El churn está acelerándose**  
   - Churns absolutos: 45 → 52 → 68 (+51% en 3 meses).  
   - Churn rate: ~3,7% → 4,3% → 5,0%. Es un aumento del ~35% relativo. Si esto continúa, cada mes pierdes una porción mayor de tu base.

2. **El crecimiento se está desacelerando**  
   - Crecimiento mensual de usuarios/MRR: 12,5% → 9,6%. Sigue siendo positivo, pero la tendencia es claramente descendente.

3. **El LTV está cayendo**  
   - LTV: $420 → $415 → $408. Con un ARPU fijo de $15, esto significa que la vida útil promedio del cliente se está acortando (de ~28 a ~27 meses). Es consistente con el churn creciente.

4. **El NRR está bajando**  
   - Pasa de ~96,3% a ~95,0%. Cada mes retienes menos ingresos de tu base existente. A este ritmo, necesitas cada vez más clientes nuevos solo para mantener el MRR.

5. **⚠️ Inconsistencia entre LTV y churn**  
   - Con un churn del 5% y ARPU de $15, el LTV “real” debería ser ~$300 (15 ÷ 0,05). Pero reportas un LTV de $408. Esto sugiere que **el LTV está sobreestimado, el churn está subestimado, o hay ingresos por expansión que no estás capturando en los datos**. Es crítico revisar cómo estás calculando el LTV.

6. **La mejora del LTV/CAC en marzo es engañosa**  
   - El ratio sube a 5,23 porque el CAC bajó a $78, no porque el LTV haya mejorado. De hecho, el LTV sigue cayendo. Un CAC bajo puede atraer clientes de menor calidad y aumentar el churn futuro.

---

## 3. Tres acciones concretas

### 1. Diagnostica el churn a fondo
- **Segmenta los churns por cohorte, canal de adquisición, plan y antigüedad.**  
- Haz encuestas de salida a los clientes que cancelan.  
- Pregunta: ¿el churn viene de clientes nuevos (primeros 30-60 días) o antiguos? Si es de nuevos, el problema es el onboarding o la selección de clientes. Si es de antiguos, el problema puede ser el producto o el soporte.

### 2. Implementa un programa de retención temprana
- Define una métrica de **activación** (ej. completar una acción clave dentro de los primeros 14 días).  
- Automatiza alertas para clientes que no se activan o que reducen su uso.  
- Contacta proactivamente a los clientes en riesgo antes de que lleguen a cancelar.  
- Reducir el churn de 5% a 4% aumentaría tu LTV real de ~$300 a ~$375 y mejoraría el NRR.

### 3. Revisa la estrategia de adquisición y precios
- Calcula el **LTV/CAC por canal** para identificar qué canales traen clientes de mayor calidad, no solo los más baratos.  
- El CAC de $78 en marzo puede ser bueno, pero si esos clientes tienen un churn más alto, el costo real es mayor.  
- Evalúa si un plan de $15/mes es suficiente. Prueba precios más altos o planes anuales (con descuento) para mejorar la retención y el LTV.

---

## 4. Proyección para abril (si las tendencias continúan)

Asumo que las tendencias lineales observadas se mantienen.

| Métrica | Proyección abril |
|---|---|
| **Usuarios finales** | ~1.580 (crecimiento de ~6,7%) |
| **MRR** | ~$23.700 (1.580 × $15) |
| **Churn rate** | ~5,7% |
| **Churns** | ~84 (sobre 1.480 clientes iniciales) |
| **Nuevos clientes** | ~184 (1.580 − 1.480 + 84) |
| **NRR** | ~94,3% |
| **LTV reportado** | ~$402 (si sigue la tendencia lineal) |
| **LTV recalculado** | ~$264 (15 ÷ 0,057) |
| **LTV/CAC** (si CAC ≈ $80) | ~5,0 (con LTV reportado) o ~3,3 (con LTV recalculado) |

⚠️ **Nota importante:** Si la aceleración en el número de churns continúa (45 → 52 → 68), abril podría superar los 90 churns, elevando el churn rate a ~6,1%. Eso haría que el LTV real bajara aún más, a ~$246.

---

## Resumen ejecutivo

Tu negocio sigue creciendo, pero **el churn creciente y la caída del LTV están erosionando la rentabilidad futura**. El ratio LTV/CAC sigue siendo saludable (>3), pero la inconsistencia entre el LTV reportado y el churn real es una bandera roja. Te recomiendo priorizar la retención sobre la adquisición en los próximos meses.

Si quieres, puedo ayudarte a profundizar en el análisis por cohortes o a construir un modelo de proyección más detallado.