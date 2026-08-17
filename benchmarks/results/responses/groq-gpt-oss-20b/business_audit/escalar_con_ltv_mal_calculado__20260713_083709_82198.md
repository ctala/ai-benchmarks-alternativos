# GPT-OSS 20B (Groq) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.23 | quality: 8.4
- latency_total: 2.858s | tokens_per_second: 693.0
- input_tokens: 250 | output_tokens: 1981

## Respuesta completa

## 1️⃣ Re‑calcula el LTV con los datos reales

| Variable | Valor | Cálculo |
|----------|-------|---------|
| Precio mensual | $35 | – |
| Retención mensual | 92 % (8 % churn) | – |
| Margen bruto | 70 % | – |
| **Lifetime (meses)** | \(1 / 0.08 = 12.5\) | Cada mes pierdes el 8 % de los clientes. El promedio de vida de un cliente es 12.5 meses. |
| **LTV bruto** | \(35 \times 12.5 = \$437.50\) | 12.5 meses × $35 |
| **LTV neto (con margen)** | \(437.50 \times 0.70 = \$306.25\) | 70 % del LTV bruto |

> **El LTV que usaste ($840) está sobrestimado por un factor de ~2.7** (24 meses en lugar de 12.5 meses).

## 2️⃣ LTV/CAC con los datos correctos

| Variable | Valor | Cálculo |
|----------|-------|---------|
| LTV neto | $306.25 | – |
| CAC | $290 | – |
| **LTV/CAC** | \(306.25 / 290 = 1.06\) | Sólo un poco por encima de 1 |

- **Interpretación**: Cada dólar que gastas en adquisición te devuelve ~1.06 $ en margen bruto.  
- **Conclusión**: No hay margen suficiente para crecer de forma sostenible.

## 3️⃣ Pay‑back period (tiempo de recuperación del CAC)

- Margen bruto mensual por cliente: \(35 \times 0.70 = \$24.50\)
- Pay‑back period: \(290 / 24.50 \approx 11.8\) meses

> **El CAC se recupera casi al final de la vida media del cliente**. Cualquier variación en churn, CAC o margen empuja la empresa hacia la pérdida.

## 4️⃣ ¿Qué pasa con $10 000 de publicidad?

| Variable | Cálculo | Resultado |
|----------|---------|-----------|
| Clientes adquiridos | \(10\,000 / 290 \approx 34\) | 34 nuevos clientes |
| Margen bruto total | \(34 \times 24.50 = \$833\) | 34 × $24.50 |
| Costo CAC total | \(34 \times 290 = \$9\,860\) | 34 × $290 |
| **Resultado neto** | \(833 - 9\,860 = -\$9\,027\) | **Pérdida** |

> **Con los números correctos, la inversión de $10 000 generaría una pérdida de ~\$9 k**. El beneficio que calculaste ($552) fue un error de cálculo del LTV.

## 5️⃣ ¿Cuáles son las opciones?

| Estrategia | Qué cambia | Impacto esperado |
|------------|------------|------------------|
| **Reducir churn** | Si logras bajar el churn a 4 % mensual, el LTV pasa a ~\$550 | LTV/CAC ≈ 1.9 |
| **Aumentar precio** | Subir a $45/mes (manteniendo margen) | LTV ≈ \$374 (más alto) |
| **Bajar CAC** | Reducir a $200 con mejor targeting | LTV/CAC ≈ 1.5 |
| **Mejorar margen** | Optimizar costos de infra y pagos a 60 % | LTV ≈ \$350 |
| **Combinación** | Reducir churn a 5 % + subir precio a $40 | LTV ≈ \$420 (LTV/CAC ≈ 1.45) |

> **La única forma de tener un LTV/CAC > 3** es combinar al menos dos de las mejoras anteriores (p.ej., bajar churn a 5 % y subir precio a $40/mes, o reducir CAC a $200 y bajar churn a 5 %).  

## 6️⃣ Checklist antes de escalar

1. **Confirma el churn real**: ¿Es 8 % mensual o 8 % anual?  
2. **Revisa los costos de infraestructura y pagos**: ¿El margen bruto realmente es 70 %?  
3. **Controla el CAC**: ¿El costo de adquisición se mantiene constante a escala o aumenta?  
4. **Evalúa los costos operativos**: OPEX, soporte, desarrollo, etc.  
5. **Define el pay‑back period objetivo**: 6 – 12 meses son típicos; 12 meses es marginal.  
6. **Prueba A/B**: Experimenta con precios y mensajes de venta antes de gastar $10 k.

## 7️⃣ Respuesta directa

> **No, no deberías invertir $10 000 en publicidad con los números que presentas.**  
> El LTV real es solo ~$306, el CAC es $290, y el pay‑back period está casi al final del tiempo de vida de un cliente. La inversión produciría pérdidas y no habría margen para crecer.

### Próximos pasos

1. **Re‑calcula el churn** (si es mensual, ajusta a 12.5 meses; si es anual, ajusta a 12 meses).  
2. **Optimiza**: reduce churn, mejora el margen o reduce CAC.  
3. **Re‑evalúa** la campaña de publicidad con los nuevos números.  
4. **Mide** los resultados y ajusta iterativamente.

---

> **El unit economics es la brújula del crecimiento**. Si la brújula apunta a pérdidas, la mejor decisión es detenerse, corregir y volver a intentarlo. 🚀