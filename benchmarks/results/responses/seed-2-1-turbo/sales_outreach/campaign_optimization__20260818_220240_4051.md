# Seed 2.1 Turbo — sales_outreach/campaign_optimization

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 194.388s | tokens_per_second: 57.5
- input_tokens: 348 | output_tokens: 11182

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

### Suposiciones iniciales para las recomendaciones
1. El KPI principal de medición es el costo por signup (CPA), ya que es la única métrica de conversión que compartes.
2. Los signups de todas las campañas tienen una calidad similar (no tenemos datos de tasa de conversión a pago ni valor de vida útil de los leads).
3. Las campañas tienen espacio para escalar (no están limitadas por el volumen de búsquedas de sus keywords actuales, o se pueden expandir con términos similares de la misma intención).
4. Tu presupuesto mensual de $5.000 es inferior al gasto total del mes anterior ($7.100), por lo que se prioriza la eficiencia.

---

## 1. Cálculo de métricas por campaña
Fórmulas utilizadas:
- CTR = (Clicks / Impresiones) * 100
- CPC = Costo total / Cantidad de clicks
- Tasa de conversión (CR) = (Signups / Clicks) * 100
- CPA = Costo total / Cantidad de signups

| Métrica                | Campaña A (Landing principal) | Campaña B (Blog content) | Campaña C (Competidor) |
|------------------------|--------------------------------|---------------------------|-------------------------|
| CTR                    | 3,0%                           | 4,0%                      | 6,0%                    |
| CPC                    | $1,40                          | $0,38                     | $3,56                   |
| Tasa de conversión (CR)| 3,0%                           | 0,5%                      | 4,0%                    |
| CPA (costo por signup) | $46,67                         | $75,00                     | $88,89                  |
| Rendimiento por $1 invertido (signups/$) | 0,021 | 0,013 | 0,011 |

---

## 2. ¿Qué campaña escalar y cuál pausar?
### ✅ Campaña a escalar: Campaña A (Landing principal)
Justificación numérica:
- Tiene el CPA más bajo del grupo: es 38% más barato que la Campaña B y 90% más barato que la Campaña C.
- Su rendimiento por dólar invertido es el más alto: por cada $1 que inviertes, generas 0,021 signups, un 62% más que la Campaña C y un 61% más que la Campaña B.
- Su tasa de conversión de 3% es muy alta para keywords transaccionales de fondo de embudo, lo que indica que la coincidencia entre la intención de búsqueda, el copy de los anuncios y la landing page es muy buena.

### ❌ Campaña a pausar (con matices): Campaña C (Competidor)
Justificación numérica:
- Tiene el CPA más alto del grupo ($88,89), casi el doble que la Campaña A. Esto se debe a que su CPC es 2,5 veces más caro que el de la Campaña A ($3,56 vs $1,40), a pesar de tener una tasa de conversión mayor.
- Su volumen de impresiones es muy bajo (15.000, solo el 30% de la Campaña A y el 12,5% de la Campaña B), lo que indica que el volumen de búsquedas de estas keywords de competidor es limitado, por lo que no tiene mucho espacio para escalar incluso si se mejora su rendimiento.

> ⚠️ Matización muy importante: Si tienes datos que demuestren que los signups de la Campaña C tienen una tasa de conversión a pago o un LTV 2 veces mayor que los de la Campaña A (porque son usuarios que ya están evaluando herramientas y están más cerca de comprar), no deberías pausarla, sino reducir su presupuesto y optimizarla. Con los datos que compartes (solo signups), es la menos eficiente.

> 💡 ¿Y la Campaña B? No hay que pausarla: a pesar de tener una tasa de conversión baja, su CPC es muy barato y genera tráfico de tope de embudo que se puede nutrir por email para convertir a largo plazo. Su problema no es la campaña en sí, sino la conversión del blog, que se puede mejorar con pruebas A/B.

---

## 3. Redistribución del presupuesto de $5.000
Te propongo dos escenarios según tu objetivo:

### Escenario 1: Maximizar signups de corto plazo
Priorizas completamente la eficiencia de costo por signup, manteniendo partidas mínimas para las otras campañas:
| Campaña | Presupuesto | % del total | Justificación | Signups estimados |
|---------|-------------|-------------|---------------|-------------------|
| A       | $3.500      | 70%         | Aumento de 67% respecto al gasto anterior. Asumiendo un aumento de 10% en el CPA por escalado (por mayor competencia en keywords de alta intención), se mantiene como la más eficiente. | ~68 |
| B       | $1.000      | 20%         | Reducción de 44% del gasto anterior, pero mantenés tráfico de tope de embudo para probar mejoras de conversión. | ~13 |
| C       | $500        | 10%         | Reducción de 84% del gasto anterior, partida mínima para capturar usuarios de alta intención y probar optimizaciones. | ~5-6 |
| **Total** | **$5.000** | **100%** | | **~86-87** |

> Resultado: Reducís el gasto en un 30% respecto al mes anterior, pero solo perdés un 17% de los signups (de 105 a ~86), por la mayor eficiencia de la asignación.

---

### Escenario 2: Equilibrar signups de corto plazo y crecimiento a largo plazo
Mantenés una presencia fuerte en todo el embudo de conversión, para generar leads que se convertirán en clientes en los próximos meses:
| Campaña | Presupuesto | % del total | Justificación | Signups estimados (métricas actuales) |
|---------|-------------|-------------|---------------|----------------------------------------|
| A       | $2.750      | 55%         | Aumento de 31% respecto al gasto anterior, escalado moderado para no subir demasiado el CPA. | ~56 |
| B       | $1.750      | 35%         | Mantenés casi todo su presupuesto anterior (solo 3% de reducción), ya que su tráfico barato de tope de embudo genera conciencia de marca y leads nutribles. Si lográs subir su CR a 1% con tests, el CPA bajaría a $37,5 y generaría ~46 signups. | ~23 |
| C       | $500        | 10%         | Igual que en el escenario anterior, partida mínima de prueba. | ~5-6 |
| **Total** | **$5.000** | **100%** | | **~84-85** |

> Resultado: Tenés casi la misma cantidad de signups que en el escenario 1, pero generás 3.500 clicks de tope de embudo (contra 2.631 del escenario 1) para nutrir y convertir a largo plazo.

---

## 4. Tests A/B sugeridos para el próximo mes
Los tests se enfocan en solucionar los puntos débiles de cada campaña:

### 🔹 Para Campaña A (objetivo: mantener el CPA bajo al escalar)
1. **Test de headline de landing: Beneficio vs funcionalidad**
   - Variante A (actual): "Software de gestión de inventario para pymes"
   - Variante B: "Reduce tus pérdidas por inventario descontrolado en un 30%"
   - Por qué: Los usuarios de fondo de embudo responden mejor a beneficios tangibles que a descripciones de producto. Se espera un aumento de 10-20% en el CR.
2. **Test de formulario de signup: 3 campos vs 1 campo**
   - Variante A: Nombre, email, teléfono
   - Variante B: Solo email
   - Por qué: Los formularios más cortos aumentan la tasa de conversión, aunque pueden reducir la calidad del lead. Ideal si tu objetivo es maximizar signups.
3. **Test de CTA: "Prueba gratis 14 días" vs "Solicita demostración personalizada"**
   - Por qué: Dependiendo de tu cliente ideal, una opción de prueba sin compromiso puede convertir más que una demostración, o viceversa.

---

### 🔹 Para Campaña B (objetivo: subir el CR de 0,5% para bajar el CPA)
1. **Test de imán de leads: Prueba de software vs recurso gratuito**
   - Variante A (actual, supuesta): CTA que invita a probar el software
   - Variante B: CTA que ofrece una plantilla de Excel/Sheets de gestión de inventario a cambio del email
   - Por qué: Los usuarios de tope de embudo que buscan "cómo gestionar inventario" no están listos para probar un software, pero sí dan su email por un recurso que solucione su problema inmediato. Se espera un aumento de 2-3x en el CR.
2. **Test de ubicación del CTA: Solo al final del artículo vs CTA sticky + pop-up de salida**
   - Por qué: Muchos usuarios no llegan al final del artículo, por lo que agregar CTAs en ubicaciones visibles aumenta la probabilidad de conversión.
3. **Test de coincidencia anuncio-contenido: Anuncio específico ("5 pasos para gestionar inventario") vs anuncio genérico**
   - Por qué: El CTR es alto, pero si el contenido no cumple lo que promete el anuncio, los usuarios se van sin convertir. Alinear el copy aumenta la relevancia y la conversión.

---

### 🔹 Para Campaña C (objetivo: bajar el CPC o subir el CR para reducir el CPA)
1. **Test de landing: Landing genérica vs página de comparación dedicada**
   - Variante A (actual, supuesta): Landing principal de la herramienta
   - Variante B: Página que compara lado a lado tu herramienta con el competidor (precio, funcionalidades, soporte)
   - Por qué: Los usuarios que buscan "alternativa a X" quieren una comparación directa, no una landing genérica. Se espera un aumento de 20-30% en el CR, lo que bajaría el CPA a ~$68.
2. **Test de copy de anuncio: Diferenciación clara vs copy genérico**
   - Variante A: "Alternativa a [Competidor] para pymes"
   - Variante B: "Alternativa a [Competidor]: 50% más barato y sin contratos de permanencia"
   - Por qué: Un copy con diferenciación clara atrae usuarios más calificados y aumenta la relevancia del anuncio, lo que Google premia con un CPC más bajo. Se espera una reducción de 15-25% en el CPC.
3. **Test de pujas por posición: Posición 1 vs posición 2-3**
   - Por qué: La posición 1 tiene más clicks, pero un CPC mucho más alto. Los usuarios de comparación suelen revisar varias opciones, por lo que la posición 2-3 mantiene una tasa de conversión similar con un CPC 20-30% más bajo.

---

### 🔹 Tests transversales para todas las campañas
1. Test de pujas por dispositivo (desktop vs móvil): Ajusta las pujas según la tasa de conversión de cada dispositivo.
2. Test de horarios: Aumenta las pujas en horario laboral (si tu público son dueños de pymes o gerentes) y reducelas en horarios no laborales para evitar clicks de baja calidad.
3. Amplía la lista de keywords negativas: Especialmente en la Campaña C (agrega términos como "[competidor] inicio de sesión", "[competidor] soporte") y la Campaña B (agrega términos que no se alineen con tu oferta, como "plantilla gratis" si no la ofreces).