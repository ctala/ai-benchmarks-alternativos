# DeepSeek V4 Pro — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.88 | quality: 9.36
- latency_total: 108.773s | tokens_per_second: 34.6
- input_tokens: 272 | output_tokens: 3759
- judge_score: 4.6 | justificación: 

## Respuesta completa

**1. Métricas por campaña**

| Métrica | Campaña A (Landing principal) | Campaña B (Blog content) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** (Clics / Impresiones) | 1,500 / 50,000 = **3.00 %** | 4,800 / 120,000 = **4.00 %** | 900 / 15,000 = **6.00 %** |
| **CPC** (Costo / Clics) | $2,100 / 1,500 = **$1.40** | $1,800 / 4,800 = **$0.38** | $3,200 / 900 = **$3.56** |
| **CPA** (Costo / Signups) | $2,100 / 45 = **$46.67** | $1,800 / 24 = **$75.00** | $3,200 / 36 = **$88.89** |
| **Conversion Rate** (Signups / Clics) | 45 / 1,500 = **3.00 %** | 24 / 4,800 = **0.50 %** | 36 / 900 = **4.00 %** |

**2. ¿Cuál campaña escalar y cuál pausar?**

**Escalar: Campaña A (Landing principal)**  
- Es la más eficiente en costo por adquisición con un **CPA de $46.67**, casi la mitad que las otras.  
- Tiene un buen balance entre CTR (3%) y tasa de conversión (3%), lo que indica que atrae tráfico relevante y su landing convierte.  
- Con keywords transaccionales (“software gestion inventario”, “inventario pymes”) apunta a usuarios con alta intención de compra.

**Pausar: Campaña C (Competidor)**  
- Presenta el **CPA más alto ($88.89)**, un 90% más caro que el de la Campaña A.  
- Aunque su CTR (6%) y CVR (4%) son los mejores, el costo por clic es excesivo ($3.56) y el volumen de conversiones es bajo en relación a la inversión (36 signups por $3,200).  
- Las keywords de competidor suelen tener menor volumen y alta competencia; en este caso no justifican el gasto frente a opciones más rentables.

*Nota sobre Campaña B*: No se pausa aún porque genera mucho tráfico barato (CPC $0.38, 120k impresiones). Su punto débil es la conversión (CVR 0.5%), lo que la convierte en candidata a optimización y no a eliminación inmediata (ver punto 4).

**3. Redistribución del presupuesto de $5,000/mes**

El mes pasado se invirtieron $7,100. Para ajustarse a $5,000 y maximizar los signups, propongo:

| Campaña | Presupuesto anterior | Nuevo presupuesto | Justificación |
|---|---|---|---|
| **A** | $2,100 | **$4,000** | Escalar el 90% adicional sobre lo ya ejecutado. Al menor CPA, maximiza las altas. Se monitoreará que el CPA no se dispare al aumentar el volumen. |
| **B** | $1,800 | **$1,000** | Mantener con menor inversión mientras se ejecutan A/B tests para mejorar su CVR (ver punto 4). Si el CPA no baja de $50, reevaluar el mes siguiente. |
| **C** | $3,200 | **$0** | Pausar completamente; su CPA no es sostenible. |
| **Total** | $7,100 | **$5,000** | Ahorro y reenfoque en la campaña más rentable. |

Con esta redistribución se estiman ≈(4000/46.67) + (1000/75) = **85 + 13 = 98 signups**, frente a los 45+24+36=105 actuales, pero con un 30% menos de gasto y un CPA ponderado mucho más sano (~$51).

**4. A/B Tests sugeridos para el próximo mes**

1. **Campaña B – Landing page específica vs. blog genérico**  
   *Problema:* CVR de solo 0.5%. El tráfico aterriza en artículos del blog sin una llamada a la acción clara.  
   *Test:* Desviar el 50% del tráfico a una landing page dedicada con un lead magnet (guía descargable, plantilla de inventario) y formulario de registro, manteniendo el otro 50% en el artículo con un banner de suscripción.  
   *Medir:* CVR y CPA por variante. Buscar llevar el CVR al menos al 1.5‑2%.

2. **Campaña A – Copys de anuncio enfocados en “Prueba gratuita” vs. “Demo”**  
   *Objetivo:* Mejorar el CTR y la calificación del clic.  
   *Versión A:* “Software de Gestión de Inventario – Prueba Gratis 14 Días”.  
   *Versión B:* “Solicita una Demo Personalizada de Inventario”.  
   *Medir:* CTR, CVR por ad y CPA final.

3. **Campaña A – Extensiones de anuncio**  
   *Test:* Incluir sitelinks (“Planes y precios”, “Caso de éxito pyme”, “Integraciones”) y callouts (“Soporte 24/7”, “Sin tarjeta de crédito”).  
   *Hipótesis:* Aumentan el CTR y dan más información para pre‑calificar al usuario, manteniendo o mejorando el CPA.

4. **Campaña B – Palabras clave**  
   *Test:* Dentro del presupuesto reducido, probar nuevas variaciones con intención más alta como “plantilla inventario restaurante” o “software inventario restaurante” (hibridando lo informativo con lo transaccional) y medir si el CVR mejora respecto a las keywords puramente informativas.