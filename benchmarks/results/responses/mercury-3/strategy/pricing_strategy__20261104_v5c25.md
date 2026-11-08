# Mercury 3 — strategy/pricing_strategy

- model_id: `inception/mercury-3`
- success: True  | final: 5.36 | quality: 5.0
- latency_total: 19.732s | tokens_per_second: 338.4
- input_tokens: 170 | output_tokens: 6678

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

# Análisis: subir de $60 a $89/mes

## 1. LTV/CAC actual y proyectado

Primero, lo más correcto es calcular el LTV sobre el **margen bruto**, no sobre el precio bruto, porque el costo por usuario ($8/mes) reduce tu ganancia real.

| Métrica | Actual ($60) | Con $89 (sin cambio de churn) |
|---|---|---|
| Margen mensual por cliente | $60 – $8 = **$52** | $89 – $8 = **$81** |
| Churn mensual | 7% | 7% |
| Vida media del cliente | 1 / 0.07 = 14.3 meses | 14.3 meses |
| LTV (sobre margen) | $52 × 14.3 = **$743** | $81 × 14.3 = **$1,157** |
| CAC | $120 | $120 |
| **LTV/CAC** | **6.2** | **9.6** |

Si prefieres usar el LTV sin descontar costos (como lo planteaste): actual = $840 / $120 = **7.0**. Con $89 sin cambio de churn = $1,246 / $120 = **10.4**.

O sea, el ratio ya es bueno, y con el aumento mejoraría mucho **si el churn no subiera**. Pero el churn sí subirá, y eso es lo que hay que modelar.

---

## 2. Impacto estimado en churn

Benchmarks de la industria SaaS (especialmente SMB/B2B) indican que un aumento de precio de 10% genera típicamente un aumento **relativo** del churn de entre 2% y 5%. Tu aumento es de 48% ($60 → $89), así que el churn podría subir entre:

- 48% × 2% = **+9.6% relativo** → churn de 7% a **7.7%**
- 48% × 5% = **+24% relativo** → churn de 7% a **8.7%**

Además, tu churn base de 7% mensual ya es alto (58% anual). Eso sugiere que el producto ya tiene problemas de retención independientes del precio. Un aumento puede acelerar la salida de clientes poco satisfechos o sensibles al precio.

Dato importante: tus competidores cobran hasta $149/mes, así que $89 sigue dentro de un rango defendible. Eso reduce el riesgo de que los clientes se vayan a un competidor más barato.

---

## 3. Modelo de 3 escenarios

Supongamos que aplicas el aumento a los 200 clientes actuales. Uso el margen bruto ($81) y el churn nuevo según escenario.

| Escenario | Churn mensual nuevo | Vida media | LTV (margen) | LTV/CAC | Clientes que quedan a los 12 meses (de 200) | Margen total acumulado a 12 meses |
|---|---|---|---|---|---|---|
| Actual (sin subir) | 7% | 14.3 meses | $743 | 6.2 | ~84 | **$86,000** |
| Optimista | 7% (no cambia) | 14.3 meses | $1,157 | 9.6 | ~84 | **$134,500** |
| Realista | 8.5% | 11.8 meses | $953 | 7.9 | ~69 | **$124,900** |
| Pesimista | 10% | 10 meses | $810 | 6.8 | ~56 | **$116,300** |

### Lectura de los resultados

- Incluso en el escenario **pesimista** (churn sube a 10%), el LTV/CAC sigue siendo **6.8**, muy por encima del 3 recomendado.
- El margen total a 12 meses **sube en todos los escenarios**, incluso perdiendo más clientes. En el pesimista, ganas $116,000 vs $86,000 actuales: **+35%**.
- El payback del CAC también mejora: pasas de recuperar el CAC en 2.3 meses a recuperarlo en 1.5 meses ($120 / $81).

Conclusión cuantitativa: **subir a $89 es rentable incluso en el peor escenario razonable**, siempre que el churn no suba por encima de ~10% mensual.

---

## 4. Recomendación

**Sí, te recomiendo subir el precio a $89/mes.** Los números lo justifican:

- Tu LTV/CAC realista pasaría de **6.2 a 7.9**.
- Tu margen total a 12 meses para los 200 clientes actuales subiría de **$86,000 a ~$125,000** en el escenario realista.
- Aunque pierdas ~15 clientes adicionales por el aumento, los que se quedan pagan 48% más, y el margen extra compensa con creces.

Pero con dos condiciones:

1. **Antes de subir, ataca el churn base de 7%.** Es tu problema más grave. Si el churn sigue alto, cualquier aumento de precio amplifica la fuga. Trabaja en onboarding, soporte y hábito de uso.
2. **No apliques el aumento de golpe a todos sin estrategia.** El riesgo principal no es el LTV, sino el impacto en la relación con clientes existentes y en la adquisición de nuevos clientes (la conversión puede bajar, subiendo tu CAC efectivo).

---

## 5. Estrategia de implementación

Te recomiendo un enfoque **híbrido**, no un grandfathering total ni un aumento brusco universal.

### Opción recomendada: aumento escalonado + descuento anual

1. **Clientes nuevos: cobrar $89 desde ya.** Esto es lo más fácil y no genera conflicto con la base actual.
2. **Clientes existentes: anunciar el aumento con 60 días de anticipación**, ofreciendo dos alternativas:
   - Mantener $60/mes si firman un **contrato anual por adelantado** (bloqueo de precio por 12 meses).
   - Si no, pasan a $89/mes al final del aviso.
3. **Ofrecer un plan anual con descuento**: $79/mes pagado anualmente (en lugar de $89). Esto reduce el churn, mejora el flujo de caja y hace que el aumento se sienta menos agresivo.
4. **Comunicar valor añadido**: antes del aumento, lanza o destaca mejoras (reportes, integraciones, soporte prioritario). Justifica el precio con producto, no solo con inflación.
5. **Monitorear semanalmente**: si en los primeros 60 días el churn supera el 9% mensual, activa un plan de retención:
   - Llamadas de éxito del cliente a los que amenacen con irse.
   - Ofrecer un descuento temporal de 20% por 6 meses.
   - Migrar a los más sensibles a un plan básico más barato (por ejemplo $49) con menos features.

### Por qué no hacer grandfathering total

El grandfathering total (dejar a todos los existentes en $60 para siempre) protege el churn, pero:

- Dejas de capturar valor de tu base actual durante años.
- Creas una estructura de precios injusta entre clientes nuevos y antiguos.
- El aumento solo impactaría en nuevos clientes, y el efecto en ingresos sería mucho más lento.

### Por qué no subir de golpe sin aviso

Un aumento de 48% sin preparación puede generar una ola de cancelaciones emocionales. El aviso de 60 días, la opción anual y el plan de retención reducen ese riesgo.

---

## Resumen ejecutivo

- **Sube a $89/mes.** Es rentable incluso en el escenario pesimista.
- Tu LTV/CAC realista pasará de **6.2 a 7.9**.
- Tu margen total a 12 meses subirá de **$86k a ~$125k**.
- Implementa con aviso de 60 días, opción de plan anual a $79, y monitoreo semanal del churn.
- Si el churn supera 9% tras el aumento, activa descuentos temporales y llamadas de retención.

El precio no es tu problema principal: el churn de 7% mensual sí lo es. Usa el aumento de precio como una oportunidad para también mejorar la retención y el valor percibido del producto.