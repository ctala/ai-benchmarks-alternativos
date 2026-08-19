# Qwen 3.6 Max — business_audit/retention_sobre_100_interpretacion

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 5.34 | quality: 6.0
- latency_total: 96.161s | tokens_per_second: 32.7
- input_tokens: 143 | output_tokens: 3144

## Respuesta completa

**Respuesta directa:** No. Tu interpretación es incorrecta y, si actúas en consecuencia, pondrás en riesgo la sostenibilidad del negocio.

### Qué mide realmente ese 114%
Ese número es **Net Revenue Retention (NRR)** o Retención Neta de Ingresos. Mide cuánto ingreso conservas de tu base de clientes existente después de:
- Restar el ingreso perdido por bajas (churn) y bajadas de plan (downgrades)
- Sumar el ingreso adicional por subidas de plan, usos extra o cross-sell (expansión)

El NRR **puede superar el 100%** porque los clientes que se quedan gastan más. La **retención de clientes (logo retention)** nunca puede superar el 100%; cuenta logos, no euros. Son métricas distintas y responden a preguntas distintas.

### Tu contexto en números
- Mes anterior: 40 clientes
- Mes actual: 36 clientes
- **Churn de logos:** 4/40 = **10% mensual**

Eso no es “prácticamente nadie”. Un 10% mensual, si se mantiene, implica perder ~72% de tu base en 12 meses `(1 - 0.9^12)`. El 114% de NRR solo indica que el ingreso adicional de los que subieron de plan compensó con creces el ingreso perdido por los 4 que se fueron. Es expansión enmascarando rotación.

### Por qué no puedes ignorar el churn
1. **Matemática de adquisición:** Cada cliente que pierdes debe ser reemplazado solo para mantener el ritmo. Con 10% mensual, tu CAC efectivo se dispara porque estás pagando por adquirir clientes que rotan rápido. El payback se alarga y el LTV/CAC se deteriora.
2. **La expansión no es infinita:** Los upgrades tienen techo. Si la base se erosiona, el motor de expansión se queda sin combustible. Un NRR > 100% con churn alto suele depender de pocos clientes o de subidas puntuales; no es estructuralmente sostenible.
3. **Señal de fricción:** Perder 1 de cada 10 clientes cada mes indica problemas en onboarding, ajuste de precio, valor percibido, competencia o soporte. Si no lo investigas, el churn terminará superando la expansión y el NRR colapsará de forma abrupta.

### Qué deberías monitorizar y hacer
| Métrica | Qué mide | Qué esperar en SaaS sano |
|--------|----------|--------------------------|
| **NRR** | Ingreso neto de la base (churn + downgrades + expansión) | >100% es excelente, pero no aislado |
| **GRR** (Retención Bruta) | Ingreso retenido sin contar expansión | >90% mensual en SMB, >95% en enterprise |
| **Logo Retention / Churn** | % de clientes que se quedan o se van | <3-5% mensual en SMB, <1-2% en enterprise |

Acciones concretas:
1. **Separa las métricas.** No tomes decisiones de crecimiento mirando solo el NRR. Calcula GRR y logo churn mensuales.
2. **Audita las 4 bajas.** Clasifícalas por motivo, plan, tiempo en producto y uso previo. ¿Fue precio? ¿Falta de activación? ¿Competencia? ¿Mal fit?
3. **Verifica la concentración de la expansión.** Si el +14% neto viene de 2-3 clientes, tu NRR es frágil. Calcula el % de expansión por cliente y su distribución.
4. **Equilibra el esfuerzo.** No abandones la captación, pero asigna recursos a retención proporcionalmente al churn. En SaaS, el crecimiento eficiente se construye con **base estable + expansión**, no con expansión que tapa rotación.
5. **Establece umbrales de alerta.** Ejemplo: si logo churn >5% mensual o GRR <85%, congela campañas de adquisición agresivas y prioriza investigación de churn, onboarding y ajustes de pricing/empaquetado.

### Conclusión
El 114% es una buena señal: tus clientes existentes encuentran valor para pagar más. Pero **no es un permiso para ignorar que estás perdiendo el 10% de tu base cada mes**. En SaaS, el NRR > 100% acelera el crecimiento solo cuando el logo churn está controlado. Si lo dejas correr, la expansión se agotará, el CAC se comerá el margen y el panel pasará de 114% a <90% más rápido de lo que crees.

Si quieres, comparte el ingreso perdido por las 4 bajas, el ingreso ganado por upgrades y la antigüedad media de los clientes. Te calculo GRR, NRR desglosado y te digo si tu expansión es estructural o puntual.