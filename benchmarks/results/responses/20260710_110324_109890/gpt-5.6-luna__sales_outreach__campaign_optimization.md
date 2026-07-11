# GPT-5.6 Luna — sales_outreach/campaign_optimization

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 17.205s | tokens_per_second: 167.6
- input_tokens: 261 | output_tokens: 2883
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y recomendaciones prácticas para la optimización de la campaña.

## Respuesta completa

## 1. Métricas por campaña

| Campaña | CTR | CPC | Conversion rate* | CPA |
|---|---:|---:|---:|---:|
| **A: Landing principal** | 1,500 / 50,000 = **3.0%** | $2,100 / 1,500 = **$1.40** | 45 / 1,500 = **3.0%** | $2,100 / 45 = **$46.67** |
| **B: Blog content** | 4,800 / 120,000 = **4.0%** | $1,800 / 4,800 = **$0.38** | 24 / 4,800 = **0.5%** | $1,800 / 24 = **$75.00** |
| **C: Competidor** | 900 / 15,000 = **6.0%** | $3,200 / 900 = **$3.56** | 36 / 900 = **4.0%** | $3,200 / 36 = **$88.89** |

\*Conversion rate calculado como signups / clicks.

### Lectura rápida

- **Campaña A:** mejor equilibrio entre volumen, conversión y costo. Es la más eficiente.
- **Campaña B:** genera tráfico barato y buen CTR, pero convierte muy poco: solo **0.5%**.
- **Campaña C:** tiene el mejor CTR y la mejor conversión, pero los clicks son muy caros y termina con el **CPA más alto**.

Además, el gasto reportado suma **$7,100**, que supera el presupuesto mensual de $5,000. Habría que revisar si los datos corresponden exactamente al mismo periodo y si hay sobreentrega o presupuesto adicional.

---

## 2. ¿Cuál escalar y cuál pausar?

### Escalar: Campaña A

Es la clara candidata a recibir más presupuesto:

- CPA de **$46.67**
- 3.0% de conversión
- CPC razonable de **$1.40**
- 45 signups con solo $2,100

Cada $1,000 adicionales, manteniendo el rendimiento actual, produciría aproximadamente:

\[
\$1,000 / \$46.67 \approx 21.4 \text{ signups}
\]

### Pausar o reducir fuertemente: Campaña C

Si el objetivo principal es maximizar signups al menor costo:

- CPA de **$88.89**, casi el doble que A.
- CPC de **$3.56**, muy superior a A y B.
- Aunque convierte al 4%, el alto costo del tráfico destruye la eficiencia.

La pausaría temporalmente o la dejaría con un presupuesto de prueba muy pequeño. Antes de eliminarla definitivamente, comprobaría si los usuarios de esta campaña tienen:

- Mayor activación del producto.
- Mayor conversión a clientes pagos.
- Mayor lifetime value.
- Mejor tasa de retención.

Si los signups de C valen considerablemente más que los de A, podría justificarse mantenerla.

### Campaña B: reducir y optimizar, no escalar todavía

B tiene buen CTR y CPC muy bajo, pero su conversión es débil:

- 4,800 clicks
- Solo 24 signups
- Conversion rate de **0.5%**
- CPA de **$75**

No la escalaría en su estado actual. La mantendría con presupuesto limitado para probar una mejor transición entre el contenido y el signup.

---

## 3. Redistribución propuesta del presupuesto de $5,000

### Opción recomendada

| Campaña | Presupuesto | Porcentaje |
|---|---:|---:|
| **A: Landing principal** | **$3,500** | **70%** |
| **B: Blog content** | **$1,000** | **20%** |
| **C: Competidor** | **$500** | **10%** |
| **Total** | **$5,000** | **100%** |

### Signups esperados, usando los CPA actuales

- Campaña A: $3,500 / $46.67 ≈ **75 signups**
- Campaña B: $1,000 / $75 ≈ **13 signups**
- Campaña C: $500 / $88.89 ≈ **6 signups**

Total estimado: aproximadamente **94 signups**, si el rendimiento se mantiene y no existe saturación.

La inversión en C sería principalmente para no perder presencia frente a competidores y validar si su calidad de usuario compensa el CPA alto. Si no mejora, esos $500 deberían trasladarse a A.

### Opción más agresiva basada exclusivamente en CPA

Si solo importa maximizar signups y no hay diferencias de calidad:

- **A: $4,000**
- **B: $1,000**
- **C: $0**

Esto produciría aproximadamente:

- A: 86 signups
- B: 13 signups
- Total: **99 signups estimados**

---

## 4. A/B tests recomendados

### Campaña A: Landing principal

1. **Titular alineado con cada keyword**
   - Variante A: “Software de gestión de inventario para pymes”
   - Variante B: “Reduce quiebres de stock y controla tu inventario”

2. **CTA**
   - “Crear cuenta gratis”
   - “Probar gratis”
   - “Solicitar demo”

3. **Longitud del formulario**
   - Formulario corto: email y contraseña.
   - Formulario largo: empresa, número de usuarios y sector.

4. **Prueba social**
   - Logos de clientes.
   - Testimonios.
   - Métricas como “reduce el tiempo de control de inventario”.

5. **Landing específica por segmento**
   - Una para pymes generales.
   - Otra para restaurantes.
   - Otra para ecommerce o retail.

---

### Campaña B: Blog content

El problema principal parece ser la desconexión entre el contenido informativo y el signup.

1. **CTA dentro del artículo**
   - CTA al inicio.
   - CTA después de la sección de solución.
   - CTA al final.

2. **Oferta**
   - “Probar el software gratis”.
   - “Descargar plantilla de inventario”.
   - “Ver una demo de 15 minutos”.
   - “Calcular el costo de tus pérdidas de inventario”.

3. **Landing posterior al contenido**
   - Enviar al usuario directamente al signup.
   - Enviar a una landing específica con el recurso prometido.

4. **Segmentación por intención**
   - Separar keywords educativas de keywords con intención comercial.
   - Reducir presupuesto en búsquedas puramente informativas.
   - Agregar keywords negativas como “definición”, “curso”, “pdf”, si no convierten.

5. **Remarketing**
   - Crear una audiencia de usuarios que leyeron el artículo pero no se registraron.
   - Mostrarles anuncios con prueba gratis o demo.

---

### Campaña C: Competidor

1. **Mensaje de comparación**
   - “Una alternativa más simple a [competidor]”.
   - “Compara funcionalidades y precios”.
   - “Migra desde [competidor]”.

2. **Landing específica**
   - Tabla comparativa.
   - Ventajas y limitaciones de cada plataforma.
   - Testimonios de usuarios que migraron.

3. **Oferta de migración**
   - Migración gratuita de datos.
   - Soporte de implementación.
   - Descuento durante los primeros meses.

4. **Segmentación por intención**
   - Separar “alternativa a competidor” de “[competidor] vs”.
   - Medir cuál grupo tiene mejor CPA y calidad.

5. **Control de costos**
   - Probar pujas más conservadoras.
   - Separar dispositivos y ubicaciones.
   - Excluir términos de baja intención.
   - Revisar si el CPC de $3.56 puede reducirse sin perder demasiado volumen.

---

## Recomendación final

- **Escalar A**, porque tiene el mejor CPA: **$46.67**.
- **No escalar B todavía**; optimizar el paso de contenido a signup.
- **Reducir o pausar C** bajo un criterio de CPA, ya que cuesta **$88.89 por signup**.
- Distribuir inicialmente **$3,500 en A, $1,000 en B y $500 en C**.
- Evaluar no solo signups, sino también activación, conversión a pago y retención. Si C produce clientes de mayor valor, su CPA alto podría ser aceptable.