# GPT-6 Luna — sales_outreach/campaign_optimization

- model_id: `openai/gpt-6-luna`
- success: True  | final: 7.84 | quality: 8.0
- latency_total: 8.709s | tokens_per_second: 103.5
- input_tokens: 261 | output_tokens: 901

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

## 1. Métricas por campaña

Fórmulas: CTR = clics ÷ impresiones; CPC = costo ÷ clics; CPA = costo ÷ signups; tasa de conversión = signups ÷ clics.

| Campaña | CTR | CPC | CPA | Tasa de conversión |
|---|---:|---:|---:|---:|
| **A — Landing principal** | 3,0% | $1,40 | **$46,67** | 3,0% |
| **B — Blog content** | 4,0% | **$0,38** | $75,00 | 0,5% |
| **C — Competidor** | **6,0%** | $3,56 | **$88,89** | **4,0%** |

## 2. ¿Qué escalar y qué pausar?

- **Escalar A con cautela:** tiene el CPA más bajo ($46,67), así que obtiene signups al menor costo. Es la mejor candidata para recibir más presupuesto, aunque conviene aumentar gradualmente y vigilar si el CPA sube.
- **Reducir o pausar B, según el valor de esos signups:** atrae muchos clics baratos, pero convierte solo el 0,5% y su CPA ($75) es bastante peor que el de A. Si el objetivo es generar signups inmediatos, reduciría su inversión. Si el blog contribuye a conversiones posteriores, evaluaría su impacto asistido antes de pausarla por completo.
- **No escalar C todavía:** tiene la mejor tasa de conversión (4%), pero su CPC alto produce el CPA más caro ($88,89). Mantendría una prueba limitada y optimizaría anuncios y landing antes de aumentar presupuesto. Si su CPA supera el máximo rentable para el negocio, la pausaría.

La decisión final depende del **CPA máximo aceptable** y del valor de cada signup; esos datos no están incluidos.

## 3. Redistribución sugerida de los $5.000

Como punto de partida, propondría:

| Campaña | Presupuesto mensual | Cambio de enfoque |
|---|---:|---|
| **A** | **$3.000** | Escalar keywords de intención alta y monitorear el CPA. |
| **B** | **$500** | Mantener solo si hay evidencia de conversiones asistidas; si no, pausar. |
| **C** | **$1.000** | Limitar y usar como presupuesto de prueba con mejoras de eficiencia. |
| **Total** | **$4.500** | |

Quedan **$500 sin asignar** deliberadamente: los liberaría tras una o dos semanas de datos, priorizando A si mantiene un CPA cercano al actual. No forzaría el gasto de todo el presupuesto si las campañas no generan conversiones rentables. La distribución inicial supone que A puede absorber más inversión sin que su CPA se deteriore.

## 4. A/B tests para el próximo mes

1. **Landing de A:** comparar la página actual con una versión más específica para “software de gestión de inventario”, con beneficios, prueba social y un CTA más visible.
2. **Oferta o CTA:** probar “Solicitar demo” frente a “Probar gratis” o “Ver precios”. Medir signups y, si es posible, calidad de los leads.
3. **Mensajes de C:** comparar anuncios centrados en funcionalidades frente a anuncios de comparación (“alternativa a…”). Mantener el cumplimiento de las políticas de Google sobre marcas de terceros.
4. **Destino de B:** probar el artículo actual frente a una landing de conversión relacionada, o añadir al artículo un CTA contextual. Medir conversiones posteriores y asistidas, no solo conversiones inmediatas.
5. **Keywords y concordancias:** probar concordancia exacta/frase frente a la configuración actual y revisar términos de búsqueda para excluir consultas informativas poco relevantes.
6. **Segmentación y horarios:** experimentar con audiencias, dispositivos u horarios, cambiando una variable por prueba para poder atribuir el resultado.

Usa **CPA y calidad de signup** como criterios principales; CTR y CPC son indicadores útiles, pero por sí solos no muestran si la inversión es rentable.