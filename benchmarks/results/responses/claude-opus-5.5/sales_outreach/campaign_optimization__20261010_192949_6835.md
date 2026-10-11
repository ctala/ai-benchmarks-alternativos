# Claude Opus 5.5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 36.963s | tokens_per_second: 97.4
- input_tokens: 395 | output_tokens: 3599

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estos resultados de mi campana de Google Ads del ultimo mes:

Campana A (Landing principal):
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100
- Keywords: "software gestion inventario", "inventario pymes"

Campana B (Blog content):
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800
- Keywords: "como gestionar inventario", "problemas inventario restaurante"

Campana C (Competidor):
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200
- Keywords: "alternativa a [competidor]", "[competidor] vs"

Mi presupuesto total es $5,000/mes.

1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?


## Respuesta completa

# Análisis de campañas de Google Ads

## 1. Métricas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** (clicks/impresiones) | 3.0% | 4.0% | **6.0%** |
| **CPC** (costo/clicks) | $1.40 | **$0.38** | $3.56 |
| **Conversion rate** (signups/clicks) | 3.0% | 0.5% | **4.0%** |
| **CPA** (costo/signups) | **$46.67** | $75.00 | $88.89 |

**Totales:** $7,100 gastados, 105 signups, CPA promedio de $67.62.

⚠️ **Observación importante:** gastaste $7,100, un 42% más que tu presupuesto de $5,000. Revisa los límites diarios de tus campañas. Google puede gastar hasta el doble del presupuesto diario en días puntuales, aunque en teoría compensa en el mes.

## 2. ¿Cuál escalar y cuál pausar?

### Escalar: Campaña A
- Tiene el CPA más bajo ($46.67), un 38% más barato que B y un 47% más barato que C.
- Genera el 43% de los signups con el 30% del gasto.
- Sus keywords ("software gestion inventario") muestran intención de compra directa.

### Optimizar (no pausar del todo): Campaña C
Por CPA es la peor ($88.89). Aun así tiene la mejor intención: CTR de 6% y conversion rate de 4%. El problema no es la calidad del tráfico sino el CPC alto ($3.56). Además, quien busca "alternativa a [competidor]" ya está pagando por una solución similar, así que suele convertir mejor a cliente pagado.

### Reducir fuertemente: Campaña B
- Los clicks son baratos ($0.38), pero solo convierte el 0.5%. Es 6 veces peor que A.
- "Cómo gestionar inventario" es tráfico informativo: la gente busca aprender, no comprar.
- Excepción: "problemas inventario restaurante" puede ser un nicho valioso (ver tests).

### La pregunta crítica: ¿qué pasa después del signup?
Un signup no es un cliente. Antes de decidir, revisa la tasa de signup → cliente pagado de cada campaña:

- Para que **C** sea igual de rentable que A, sus signups deben convertir a pago **1.9 veces mejor** ($88.89 / $46.67).
- Para **B**, necesitaría convertir **1.6 veces mejor** ($75 / $46.67).

Si los usuarios de C convierten a pago, por ejemplo, al 30% y los de A al 12%, C sería tu mejor campaña. Sin ese dato, el análisis está incompleto.

## 3. Redistribución de $5,000

Recomendación, asumiendo que no tienes aún datos de conversión a pago:

| Campaña | Presupuesto | % | CPA estimado | Signups estimados |
|---|---|---|---|---|
| A (Landing) | $3,000 | 60% | ~$52* | ~58 |
| C (Competidor) | $1,400 | 28% | ~$80** | ~17 |
| B (Blog) | $600 | 12% | ~$65*** | ~9 |
| **Total** | **$5,000** | | **~$60** | **~84** |

\* Asumo que el CPA de A sube un ~10% al escalar, por rendimientos decrecientes. Antes de escalar, revisa el "porcentaje de impresiones perdidas por presupuesto". Si es bajo, no hay mucho volumen extra disponible y tendrás que añadir keywords relacionadas ("sistema de inventario", "control de stock pymes").

\** C mejora al recortar los peores competidores o keywords y quedarte con los de mejor CPA.

\*** B solo con la keyword de restaurantes y/o remarketing a visitantes del blog.

**Resultado:** unos 84 signups con $5,000, frente a 105 con $7,100. El volumen baja un 20%, pero el CPA mejora un ~11% y te ajustas al presupuesto.

**Plan alternativo:** si descubres que C convierte a pago mucho mejor, invierte la proporción entre A y C (por ejemplo, A $2,200 / C $2,200 / B $600).

## 4. A/B tests para el próximo mes

**Aviso sobre el tamaño de muestra:** con un conversion rate de 3%, detectar una mejora relativa de 30% requiere unos 5,700 clicks por variante. La campaña A tiene unos 2,000 clicks al mes, así que los tests deben buscar cambios grandes, no ajustes de color de botón. Haz un test por campaña como máximo.

### Test 1: Campaña C, landing de comparación (prioridad alta)
- **Control:** landing actual.
- **Variante:** página específica "[Tu producto] vs [Competidor]" con tabla comparativa, oferta de migración gratuita y testimonios de clientes que se cambiaron.
- **Objetivo:** subir el conversion rate de 4% a más de 5.5%, lo que bajaría el CPA a unos $65.
- **En paralelo:** mejora la relevancia del anuncio para subir el Quality Score y reducir el CPC de $3.56.

### Test 2: Campaña A, oferta principal
- **Control:** CTA actual.
- **Variante:** cambio de fricción, por ejemplo "Prueba gratis 14 días sin tarjeta" frente a "Agenda demo", o un formulario de 2 campos frente al actual.
- **Objetivo:** subir el conversion rate de 3% a 4%.

### Test 3: Campaña B, landing vertical para restaurantes
- **Control:** tráfico al artículo del blog.
- **Variante:** landing dedicada "Software de inventario para restaurantes" (mermas, recetas, proveedores).
- **Objetivo:** demostrar si este nicho puede tener un CPA similar al de A. Si funciona, conviértelo en una campaña independiente.

### Test 4: Estrategia de puja en A
Usa la función de **Experimentos** de Google Ads: CPA objetivo ($50) frente a tu estrategia actual, con un reparto 50/50 del tráfico.

### Configura esto antes de empezar
1. **Tracking de conversión a pago por campaña** (UTMs + CRM). Es lo más importante.
2. Importar las conversiones offline a Google Ads para optimizar por clientes, no por signups.
3. Microconversiones (scroll, clic en CTA) para tener señales más rápidas en los tests de bajo volumen.

**Resumen:** escala A, optimiza C sin matarla hasta conocer su conversión a pago, y reduce B a su nicho de restaurantes. Lo más valioso que puedes hacer este mes es medir qué campaña trae clientes que pagan, no solo signups.