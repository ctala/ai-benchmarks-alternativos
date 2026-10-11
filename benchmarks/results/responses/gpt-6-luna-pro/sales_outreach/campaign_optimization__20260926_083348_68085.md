# GPT-6 Luna Pro — sales_outreach/campaign_optimization

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 30.452s | tokens_per_second: 152.3
- input_tokens: 6271 | output_tokens: 4638

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

Tomo la **tasa de conversión** como signups ÷ clics.

| Campaña | CTR | CPC | CPA por signup | Tasa de conversión |
|---|---:|---:|---:|---:|
| **A — Landing principal** | 3,0% | $1,40 | **$46,67** | 3,0% |
| **B — Blog content** | 4,0% | **$0,38** | $75,00 | 0,5% |
| **C — Competidor** | **6,0%** | $3,56 | $88,89 | **4,0%** |

Fórmulas: CTR = clics ÷ impresiones; CPC = costo ÷ clics; CPA = costo ÷ signups; tasa de conversión = signups ÷ clics.

## 2. Qué escalar y qué pausar

- **Escalaría A:** tiene el CPA más bajo ($46,67) y convierte el 3% de sus clics. Es la campaña más eficiente para generar signups según estos datos.
- **Pausaría C, al menos temporalmente:** aunque tiene el CTR y la tasa de conversión más altos, también tiene el CPC más caro ($3,56) y el CPA más alto ($88,89). Cada signup cuesta casi el doble que en A.
- **Mantendría B con presupuesto limitado:** su conversión es baja (0,5%), pero su CPA de $75 es mejor que el de C. Conviene conservarla si esos signups tienen calidad o si el blog ayuda a nutrirlos; si no avanzan en el embudo, sería candidata a recorte o pausa.

**Nota:** si el único objetivo es maximizar signups directos al menor costo, A es la ganadora. Para decidir si B merece presupuesto, conviene comparar también la calidad de los leads y las conversiones posteriores, no solo los signups iniciales.

## 3. Redistribución de los $5.000

Los costos reportados suman **$7.100**, es decir, $2.100 por encima del presupuesto indicado. Para el próximo mes propondría:

| Campaña | Presupuesto sugerido | Porcentaje |
|---|---:|---:|
| **A — Landing principal** | **$3.500** | 70% |
| **B — Blog content** | **$1.500** | 30% |
| **C — Competidor** | **$0** | 0% |
| **Total** | **$5.000** | 100% |

Aumentaría A de forma gradual y revisaría resultados semanalmente: al escalar, su CPA puede subir. Mantendría B como campaña secundaria mientras se verifica la calidad de sus leads. Si B no genera oportunidades calificadas, trasladaría parte de ese presupuesto a A.

Como referencia únicamente —no como garantía—, con los CPA históricos esa distribución daría aproximadamente **75 signups de A y 20 de B**. El rendimiento real puede cambiar al modificar presupuestos.

## 4. A/B tests para el próximo mes

1. **Landing de A:** probar dos titulares distintos, por ejemplo uno centrado en ahorrar tiempo frente a otro en reducir errores de inventario. Mantener el resto de la página igual.
2. **CTA y formulario de A:** comparar un CTA más específico frente al actual y, por separado, un formulario corto frente a uno más completo.
3. **Contenido de B:** probar CTA contextual dentro del artículo frente a CTA al final, ambos dirigidos a una landing relacionada con el tema del post.
4. **Página de comparación para C, si se reactiva:** comparar una landing de “alternativas” con una página de comparación directa. Antes, validar que el tráfico produzca leads de calidad y revisar las políticas aplicables a anuncios y uso de marcas.
5. **Calidad de conversión:** además de medir signups, registrar qué variante genera más leads calificados o clientes. Un test que sube signups pero baja su calidad podría no ser una mejora.

Para que los resultados sean interpretables, cambiar **una variable principal por test**, repartir el tráfico entre variantes de forma equilibrada y evitar decidir demasiado pronto.