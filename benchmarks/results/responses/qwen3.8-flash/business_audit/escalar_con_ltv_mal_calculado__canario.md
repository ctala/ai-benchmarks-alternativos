# Qwen 3.8 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 269.132s | tokens_per_second: 66.5
- input_tokens: 255 | output_tokens: 17909

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

**No, no le doy a los $10.000 con estos números.**  
Tu plan no pasa la aritmética: estás calculando LTV sobre **ingresos**, no sobre **margen bruto**, y estás usando una vida promedio incorrecta.

Asumiendo que:

- Precio: **$35/mes**
- Churn mensual: **8%**
- Margen bruto: **70%**
- CAC: **$290**
- CAC es incremental y fully loaded
- No hay expansión/upsell significativo

---

## 1. Tu cálculo tiene dos errores grandes

### Error 1: LTV no es sobre ingresos, es sobre margen bruto

Un cliente paga $35/mes, pero solo el **70%** queda como margen bruto:

\[
\text{Margen bruto mensual} = 35 \times 0.70 = 24.50
\]

No $35.

---

### Error 2: con 8% de churn mensual, la vida promedio no es 24 meses

Con churn mensual constante:

\[
\text{Vida promedio} = \frac{1}{\text{churn mensual}} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

No 24 meses.

De hecho, con 8% mensual:

- La probabilidad de que un cliente siga activo después de 12 meses es:

\[
0.92^{12} \approx 36.8\%
\]

- Después de 24 meses:

\[
0.92^{24} \approx 13.3\%
\]

Solo alrededor del **13%** de los clientes sobrevive 2 años.  
La mediana de vida sería aproximadamente **8 meses**, no 24.

---

## 2. Recalculando el LTV/CAC

### LTV bruto correcto

\[
\text{LTV bruto} = \frac{\text{Margen bruto mensual}}{\text{Churn mensual}}
\]

\[
\text{LTV bruto} = \frac{24.50}{0.08} = 306.25
\]

### Ratio correcto

\[
\frac{\text{LTV bruto}}{\text{CAC}} = \frac{306.25}{290} \approx 1.06
\]

No 2.9.

---

## 3. Incluso si asumieras 24 meses, el ratio seguiría bajo

Si por un momento aceptáramos tu hipótesis de 24 meses, pero corrigiendo margen bruto:

\[
\text{LTV bruto} = 24.50 \times 24 = 588
\]

\[
\frac{588}{290} \approx 2.03
\]

Sigue estando por debajo de 3.

Y con la vida promedio correcta:

\[
\frac{306.25}{290} \approx 1.06
\]

Eso significa que, en expectativa, un cliente apenas cubre su CAC.

---

## 4. Payback: aquí está el problema de caja

### Payback simple, ignorando churn

\[
\frac{290}{24.50} \approx 11.8 \text{ meses}
\]

Pero eso asume que el cliente se queda y paga 11.8 meses sin churn, lo cual no es consistente con 8% mensual.

### Payback ajustado por churn

El LTV bruto esperado es $306.25. Para recuperar $290 de CAC, necesitas casi todo el valor esperado del cliente.

Aproximadamente:

\[
306.25 \times (1 - 0.92^n) = 290
\]

\[
n \approx 35 \text{ meses}
\]

Es decir: **en expectativa, tardas casi 3 años en recuperar el CAC**, porque el churn te come el valor antes.

Si el cobro no es por adelantado, el payback puede ser incluso peor.

---

## 5. ¿Qué pasa si metes $10.000 en publicidad?

Con CAC de $290:

\[
\frac{10.000}{290} \approx 34.5 \text{ clientes}
\]

Esos clientes generan:

\[
34.5 \times 35 = 1.208 \text{ ingresos mensuales}
\]

Margen bruto mensual:

\[
1.208 \times 0.70 \approx 845
\]

Pero con 8% de churn mensual, para mantener esa base necesitas reponer clientes constantemente.

Costo mensual de reponer churn:

\[
34.5 \times 0.08 \times 290 = 800
\]

Margen bruto mensual menos costo de reponer churn:

\[
845 - 800 = 45
\]

Eso es antes de otros costos: equipo, soporte, herramientas, operaciones, impuestos, etc.

Otra forma de verlo por cliente:

\[
\text{Margen mensual} = 24.50
\]

\[
\text{Costo mensual de reponer churn} = 0.08 \times 290 = 23.20
\]

\[
\text{Contribución neta mensual por cliente} = 1.30
\]

Con CAC de $290 y churn de 8%, cada cliente mantenido con publicidad deja **$1.30/mes de margen bruto después de reponer churn**. Eso es extremadamente fino.

---

## 6. ¿Qué ratio debería ver para aprobar?

Regla práctica, pero útil:

### Para LTV/CAC >= 3 sobre margen bruto

\[
\text{CAC máximo} = \frac{306.25}{3} \approx 102
\]

Con tus números actuales, tu CAC debería estar cerca de **$100**, no $290.

---

### Para mantener CAC de $290 y llegar a 3x

Necesitas un LTV bruto de al menos:

\[
290 \times 3 = 870
\]

Con margen mensual de $24.50:

\[
\text{Churn mensual máximo} = \frac{24.50}{870} \approx 2.8\%
\]

Es decir, tendrías que bajar el churn de **8% mensual a menos de 2.8% mensual**.

---

### Para payback razonable

Si quieres recuperar el CAC en menos de 6 meses, con churn actual, tu CAC probablemente debería estar cerca de:

\[
\text{CAC máximo} \approx 120
\]

Si quieres 12 meses, con churn del 8%, el CAC máximo sería aún más bajo si el cobro no es inmediato.

---

## 7. Sensibilidad rápida

| Escenario | LTV bruto | Ratio LTV/CAC | Veredicto |
|---|---:|---:|---|
| Actual: CAC $290, churn 8% | $306 | 1.06 | No escalar |
| CAC $250, churn 8% | $306 | 1.22 | No |
| CAC $200, churn 8% | $306 | 1.53 | No |
| CAC $150, churn 8% | $306 | 2.04 | No |
| CAC $100, churn 8% | $306 | 3.06 | Podría funcionar |
| CAC $290, churn 4% | $612 | 2.11 | No |
| CAC $290, churn 3% | $817 | 2.82 | Casi |
| CAC $290, churn 2.8% | $875 | 3.02 | Podría funcionar |

---

## 8. Mi recomendación

### No apruebo $10.000 para escalar fuerte ahora mismo.

Lo que haría:

1. **No escalar con paid ads todavía.**
2. **Confirmar que el churn de 8% es real y mensual.**  
   Si 8% es anual, todo cambia. Pero si es mensual, es un churn altísimo.
3. **Confirmar que el CAC de $290 es fully loaded e incremental.**  
   Incluye media, creative, landing, pruebas, descuentos, soporte, ventas, onboarding, etc.
4. **Correr un test pequeño, no $10.000.**  
   Por ejemplo $500 o $1.000, y medir cohortes reales.
5. **Arreglar churn antes que escalar.**  
   Con 8% mensual, la publicidad paga se convierte en un balde roto.
6. **Bajar CAC o subir LTV antes de escalar.**  
   Objetivo mínimo:
   - LTV bruto / CAC >= 3
   - Payback <= 6 meses, idealmente
   - CAC estable cuando aumentas presupuesto
   - Retención M1/M3/M6 validada con cohortes

---

## Veredicto final

**No le des.**

Tu plan no tiene un problema de “más o menos 3”.  
Tiene un problema de **unit economics rotas**:

\[
\text{LTV bruto} \approx 306
\]

\[
\text{CAC} = 290
\]

\[
\text{LTV/CAC} \approx 1.06
\]

Eso significa que cada cliente pagado apenas cubre su costo de adquisición, con un payback larguísimo y casi ningún margen para costos fijos, errores de ejecución o variabilidad del CAC.

Antes de meter $10.000, necesitas llegar a algo como:

- **CAC <= $100–$120**, o
- **Churn <= 2.5–3% mensual**, o
- **LTV bruto >= $870**, o
- Una combinación validada con cohortes reales.

Con los números actuales, escalar fuerte con publicidad pagada sería convertir un negocio rentable en un negocio que quema caja.