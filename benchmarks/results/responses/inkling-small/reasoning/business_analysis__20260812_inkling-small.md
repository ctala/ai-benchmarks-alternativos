# Inkling Small — reasoning/business_analysis

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 7.76 | quality: 9.44
- latency_total: 243.45s | tokens_per_second: 28.9
- input_tokens: 176 | output_tokens: 7028
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes el análisis completo de tu SaaS. Primero los datos clave que emergen: tu **ARPU es exactamente $15/usuario/mes** en los 3 meses, lo que simplifica mucho el análisis (todo el crecimiento es por volumen, no por expansión de ingresos).

---

### 1. Métricas Clave Calculadas

| Métrica | Enero | Febrero | Marzo | Cálculo / Nota |
|---|---|---|---|---|
| **Usuarios (fin mes)** | 1,200 | 1,350 | 1,480 | — |
| **MRR** | $18,000 | $20,250 | $22,200 | — |
| **ARPU** | $15.00 | $15.00 | $15.00 | MRR / Usuarios |
| **Growth MRR** | — | **+12.5%** | **+9.6%** | (Mes actual - Mes ant.) / Mes ant. |
| **Growth Usuarios** | — | **+12.5%** | **+9.6%** | Idem |
| **Churns (absolutos)** | 45 | 52 | 68 | — |
| **Churn Rate**¹ | ~3.8% | **4.33%** | **5.04%** | Churns / Usuarios inicial mes |
| **Churn MRR** | $675 | $780 | $1,020 | Churns × $15 |
| **LTV** | $420 | $415 | $408 | — |
| **CAC** | $85 | $92 | $78 | — |
| **LTV/CAC** | **4.94x** | **4.51x** | **5.23x** | LTV / CAC |
| **CAC Payback**² | 5.7 mes | 6.1 mes | 5.2 mes | CAC / $15 |
| **NRR (mensual)**³ | — | **95.7%** | **95.0%** | (MRR inicial - Churn MRR) / MRR inicial |

¹ *Para enero uso la base aproximada de cierre (1,200); para febrero y marzo uso la base inicial real (1,200 y 1,350 respectivamente).*  
² *Asumiendo margen bruto ~100% dado que no hay datos de COGS.*  
³ *Net Revenue Retention: como tu ARPU no cambia, no hay expansión ni contracción; es 100% - churn rate de ingresos.*

**Insight rápido:** Tu negocio crece **solo por nuevos usuarios**, no por upsell. El NRR está por debajo del 100% y cayendo, lo que significa que tu base existente se está erosionando.

---

### 2. Tendencias Preocupantes (lo que grita la data)

1. **Churn acelerado (+51% en 2 meses)**  
   De 45 a 68 churns. La tasa subió de ~3.8% → 4.3% → 5.0%. Si esta curva continúa, en abril podrías perder ~90 usuarios.

2. **Crecimiento desacelerando**  
   De +12.5% a +9.6% en MRR y usuarios. La "fuerza" de adquisición se debilita mientras la fuga aumenta.

3. **LTV en caída libre (-2.9% en 2 meses)**  
   $420 → $415 → $408. Esto suele indicar que los clientes que se quedan duran menos o que tu cálculo de LTV está siendo arrastrado por el churn creciente.

4. **NRR < 100% y decreciente (95.7% → 95.0%)**  
   Esto es crítico: **no retienes ingresos de tu base existente**. Todo tu crecimiento es "sangre nueva". Si un día se te encarece la adquisición, el crecimiento se colapsa.

5. **ARPU estancado ($15)**  
   No hay expansión de ingresos por usuario. No estás monetizando más a la base existente.

6. **CAC volátil y riesgo de eficiencia**  
   Subió 8% en febrero ($92) y cayó 15% en marzo ($78). No hay estabilidad; si el canal barato de marzo se agota, tu LTV/CAC podría caer por debajo de 4x.

---

### 3. 3 Acciones Concretas Basadas en Datos

#### Acción A: Frenar el churn antes de que sea estructural (prioridad alta)
**Dato que la respalda:** Churn subió 51% (45→68) y la tasa pasó de ~3.8% a 5.0%. Tu NRR es 95%.
- **Qué hacer:** Lanza una encuesta de cancelación (exit survey) obligatoria y un "save offer" (descuento de 2 meses o downgrade a plan básico) para los próximos 30 días. Además, implementa un "onboarding de 7 días" con check-in automático, porque con ARPU fijo y MRR creciendo por volumen, probablemente pierdes usuarios nuevos muy temprano.
- **Meta:** Bajar churn rate a <3.5% en abril y recuperar NRR a >98%.

#### Acción B: Romper el techo de $15 de ARPU (expansión)
**Dato que la respalda:** ARPU es idéntico los 3 meses; NRR es <100%. No hay crecimiento orgánico de ingresos.
- **Qué hacer:** Introduce un add-on o plan "Pro" de $5-$10/mes (o límite de uso) para un 20-30% de tu base. Si lograses subir el ARPU a $17, tu churn de ingresos bajaría proporcionalmente y tu NRR podría superar 100% sin depender solo de nuevos usuarios.
- **Meta:** Subir ARPU a $16.50+ y llevar NRR a >100% en 60 días.

#### Acción C: Replicar y escalar el canal de CAC $78, eliminar el de $92
**Dato que la respalda:** CAC varió entre $78 y $92 (±18%). El mes con menor CAC es marzo, que además coincide con el mayor volumen de usuarios.
- **Qué hacer:** Audita qué canal/campaña generó los usuarios de marzo (probablemente un canal de bajo costo o referencia). Reasigna el 70% del presupuesto de febrero (el caro, $92) a ese canal. Si mantienes CAC en $78 y LTV en $408, tu ratio es 5.2x; si LTV sigue cayendo, necesitas este colchón.
- **Meta:** Estabilizar CAC < $80 y proteger LTV/CAC > 5x.

---

### 4. Proyección para Abril (si las tendencias continúan)

Usando la **tendencia lineal** observada (desaceleración de crecimiento + aceleración de churn):

| Métrica | Proyección Abril | Razonamiento |
|---|---|---|
| **Churns** | **~85 - 95** | Tendencia: +7, +16 → +20-25. Tasa ~5.7-6.3%. |
| **Churn Rate** | **~5.7% - 6.0%** | Subió ~0.7 pts/mes; base ~1,480. |
| **Crecimiento Neto Usuarios** | **~+100 a +120** | De +150 → +130 → ~+110 (desaceleración constante). |
| **Usuarios (fin abril)** | **~1,590 - 1,600** | 1,480 + 110. |
| **MRR** | **~$23,850 - $24,000** | 1,590 × $15. Crecimiento ~7.4%. |
| **Growth MRR** | **~6.5% - 7.5%** | De 12.5% → 9.6% → ~7%. |
| **LTV** | **~$400 - $405** | Tendencia: -5, -7 → ~-9. |
| **CAC** | **~$75 - $82** | Volátil; asumimos rango cercano a marzo. |
| **NRR** | **~94% - 95%** | Sigue por debajo de 100% si no hay expansión. |
| **LTV/CAC** | **~5.0x - 5.3x** | Depende de si LTV no colapsa más. |

**Escenario de riesgo:** Si el churn llega a 95 y solo sumas 100 usuarios netos, tu MRR sería ~$23,700 (crecimiento +6.8%). **No es una catástrofe**, pero es una señal de que tu motor de crecimiento se está quedando sin gasolina: necesitas que el crecimiento neto sea >150 usuarios para compensar la fuga creciente.

---

### Resumen Ejecutivo para tu toma de decisiones

- **No todo es malo:** Tienes LTV/CAC > 4x (saludable) y crecimiento positivo.
- **El problema es estructural:** Creces por adquisición, no por retención ni expansión. El churn está acelerando y tu base existente se erosiona.
- **Lo más urgente:** Actuar sobre el churn (acción A) y romper el techo de $15 (acción B) antes de que la desaceleración de marzo se convierta en estancamiento.

¿Quieres que calcule escenarios más específicos (ej. "¿Qué pasa si subo ARPU a $18?" o "¿Cuántos usuarios nuevos necesito para compensar un churn del 6%?")?