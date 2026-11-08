# GPT-OSS 120B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 92.749s | tokens_per_second: 34.1
- input_tokens: 237 | output_tokens: 3163

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

## Resumen rápido

| Métrica | Valor que calculas | Valor real (con churn y margen) |
|---|---|---|
| **ARPU** | $35/mes | $35/mes |
| **Margen bruto** | 70 % | 70 % |
| **Contribución mensual** | $35 × 0.70 = **$24,5** | $24,5 |
| **Churn mensual** | 8 % | 8 % |
| **Vida media del cliente** | 24 meses (2 años) | **1 / 0.08 = 12,5 meses** |
| **LTV (bruto)** | $35 × 24 = $840 | **$24,5 × 12,5 = $306,25** |
| **CAC** | $290 | $290 |
| **LTV / CAC** | 2,9 | **1,06** |
| **Pay‑back (meses)** | 8,4 meses (≈ $290/$35) | **≈ 12 meses (≈ $290/$24,5)** |

> **Conclusión rápida:** Con los números actuales tu LTV es apenas un 6 % superior al CAC y el período de recuperación (pay‑back) está en torno a los 12 meses, prácticamente la vida útil del cliente. No hay “margen de seguridad” suficiente para escalar $10 000 de gasto publicitario sin arriesgar la liquidez.

---

## 1. ¿Por qué el cálculo de 2 años está equivocado?

El churn mensual del 8 % implica que, en promedio, **un cliente se queda 1 / 0,08 = 12,5 meses**, no 24.  
El cálculo “LTV = ARPU × meses esperados” solo funciona cuando la retención es **casi perfecta** (churn ≈ 0). Cuando el churn es significativo, la fórmula correcta es:

\[
\text{LTV} = \frac{\text{Contribución mensual}}{\text{Churn mensual}} = 
\frac{ARPU \times \text{Margen}}{\text{Churn}}
\]

\[
\text{LTV} = \frac{35 \times 0.70}{0.08}= \frac{24.5}{0.08}= \$306.25
\]

Este es el **valor de por vida neto** (sin contar otros costos operativos como soporte, atención al cliente, etc.). Si esos costos existen (y normalmente lo hacen), el LTV real será aún menor.

---

## 2. Métricas clave que deberías observar antes de escalar

| Métrica | Por qué importa | Umbral “sano” típico |
|---|---|---|
| **LTV / CAC** | Indica si el cliente paga más de lo que cuesta adquirirlo. | ≥ 3 (pero en SaaS B2C suele ser 3‑5). |
| **Pay‑back (meses)** | Cuántos meses tardas en recuperar el CAC con la contribución mensual. | ≤ 12 meses (ideal < 6). |
| **Margen de contribución** | Diferencia entre ingreso y costos variables (infra, pagos, comisiones). | ≥ 30‑40 % del ARPU (tú tienes 70 % de margen bruto, pero el margen de contribución es 24,5 USD). |
| **CAC real** | Costo efectivo de cada cliente (incluye creatividades, pruebas A/B, comisiones de plataformas). | Debería ser estable o decreciente con escala. |
| **Churn mensual** | Directamente afecta la vida media y el LTV. | < 5 % (B2C) o < 2 % (B2B). |
| **Cash‑flow de adquisición** | Necesitas capital para cubrir el “gap” entre CAC y la contribución que llega en los primeros meses. | No debe agotar tu cash‑flow. |

Con tus números actuales:

- **LTV / CAC = 1,06** → muy por debajo del umbral “seguro”.
- **Pay‑back = 290 / 24,5 ≈ 12 meses** → casi la vida del cliente.
- **Cash‑flow**: Cada $10 000 generan ~34,5 nuevos clientes → **contribución mensual total ≈ $845**; en 12 meses recuperas $10 000, pero en el inter‑medio necesitas cubrir ese gasto con capital propio.

---

## 3. ¿Qué pasa si inviertes $10 000 ahora?

1. **Número de clientes adquiridos:** 10 000 / 290 ≈ **34,5 clientes** (redondeemos a 34).  
2. **Ingresos mensuales adicionales:** 34 × $35 ≈ **$1.190**.  
3. **Contribución mensual (después del margen bruto):** 34 × $24,5 ≈ **$833**.  
4. **Recuperación del CAC:** $10 000 / $833 ≈ **12 meses**.  
5. **Riesgo de churn:** Con 8 % de churn mensual, al cabo de 12 meses tendrás aproximadamente 34 × (0,92)^12 ≈ **13 clientes activos**. El resto habrá “desaparecido” y no aportará nada para cubrir el CAC.

En otras palabras, estarías “quemando” el capital de 10 000 USD durante casi todo el año, con muy poco margen de error (cualquier aumento de churn, caída del ARPU o incremento del CAC destruye la rentabilidad).

---

## 4. Opciones para mejorar la ecuación

| Acción | Impacto esperado | Comentario |
|---|---|---|
| **Reducir churn** (p.ej. mejor soporte, onboarding, programa de retención) | Si bajas a 5 % → vida = 20 meses → LTV = $24,5 × 20 = $490 → LTV / CAC ≈ 1,69 | Aún insuficiente, pero mejora el pay‑back a ≈ 6 meses. |
| **Incrementar ARPU** (precio, upsells, cross‑sell) | Subir a $45 → contribución = $31,5 → LTV (8 % churn) = $31,5 × 12,5 = $394 → LTV / CAC ≈ 1,36 | Necesita validar que el mercado acepte el nuevo precio. |
| **Optimizar CAC** (segmentación, creatividades de bajo costo, referral) | Reducir a $150 → LTV / CAC ≈ 2,04 (con LTV $306) | Un CAC más bajo mejora el pay‑back a ≈ 6 meses. |
| **Mejorar margen bruto** (negociar procesador, usar infraestructura más barata) | Subir margen a 80 % → contribución = $35 × 0,8 = $28 → LTV = $28 / 0,08 = $350 → LTV / CAC ≈ 1,21 | Cada punto porcentual de margen ayuda, pero no basta solo. |
| **Combinación de las anteriores** | Por ejemplo: churn 5 %, ARPU $45, CAC $150 → LTV ≈ $490, LTV / CAC ≈ 3,3, pay‑back ≈ 4,7 meses | Esta combinación ya cumple los umbrales típicos. |

### Prioriza primero

1. **Churn** – es la variable que más afecta la vida media.  
2. **CAC** – prueba diferentes canales y creatividades antes de escalar.  
3. **ARPU** – evalúa si puedes ofrecer planes premium o servicios adicionales.  
4. **Margen** – revisa los costos de infraestructura y de procesamiento de pagos.

---

## 5. Estrategia de prueba antes de lanzar $10 000

| Paso | Qué medir | Cómo hacerlo |
|---|---|---|
| **1. Test de 1 000 USD** | CAC real, churn de la cohorte, LTV preliminar | Ejecuta una campaña pequeña (≈30‑35 clientes). Sigue la cohorte durante al menos 3‑4 meses. |
| **2. Analiza cohortes** | Retención mes a mes, costo por lead, coste de soporte | Usa herramientas de análisis (Mixpanel, Amplitude, o tu propio CRM). |
| **3. Optimiza** | Reduce CAC (p.ej. A/B test de creatividades), mejora onboarding | Itera rápidamente; cada 2‑3 semanas revisa los resultados. |
| **4. Escala gradualmente** | Aumenta gasto en 2 000‑3 000 USD si el LTV / CAC supera 1,5 y el pay‑back ≤ 8 meses | Solo después de validar que la cohorte mantiene churn ≤ 5 % y CAC ≤ $200. |
| **5. Monitorea cash‑flow** | Necesidad de capital de trabajo para cubrir el “gap” | Mantén al menos 3‑6 meses de cash‑flow libre antes de escalar a $10 000. |

---

## 6. Respuesta directa a tu pregunta

**¿Le doy $10.000 en publicidad este mes?**  
No, **no** con los parámetros actuales. El LTV real es ~ $306, lo que apenas cubre el CAC de $290 y el pay‑back se extiende casi todo el año. Gastar $10 000 ahora implicaría:

- **Alto riesgo de liquidez:** el dinero invertido tardará ~12 meses en recuperarse, mientras tu flujo de caja se verá comprometido.
- **Márgenes de seguridad muy estrechos:** cualquier aumento del churn o del CAC destruirá la rentabilidad.
- **Poca capacidad de iteración:** con una gran inversión sin validar, no tendrás margen para probar y corregir.

**Recomendación:**  
1. **Ejecuta un piloto de $1‑2 k** para validar CAC, churn y LTV.  
2. **Trabaja en reducir churn** (mejora onboarding, programa de retención).  
3. **Optimiza CAC** (segmentación, canales más baratos, referral).  
4. **Sólo cuando LTV / CAC esté ≥ 1,5‑2 y el pay‑back ≤ 8 meses**, considera escalar a $10 k o más.

---

## 7. Checklist rápido antes del próximo gasto

- [ ] **LTV calculado con churn y margen** (≈ $306).  
- [ ] **CAC real** (incluye creatividades, comisiones, pruebas).  
- [ ] **LTV / CAC ≥ 1,5** (ideal ≥ 3).  
- [ ] **Pay‑back ≤ 8 meses**.  
- [ ] **Cash‑flow suficiente** para cubrir el “gap” de 6‑12 meses.  
- [ ] **Plan de mejora** para churn y CAC antes de escalar.

Si marcas todas estas casillas, entonces sí podrás destinar $10 000 a publicidad con mayor confianza. Hasta entonces, la mejor inversión es **optimizar lo que ya tienes** antes de disparar el presupuesto. ¡Éxitos!