# Seed 2.1 Turbo — sales_outreach/campaign_optimization

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 7.15 | quality: 8.0
- latency_total: 33.602s | tokens_per_second: 61.5
- input_tokens: 347 | output_tokens: 2065

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

Vamos a analizar tus campañas paso a paso con datos concretos y recomendaciones accionables:

---

## 1. Cálculo de métricas por campaña
Primero definimos las fórmulas usadas:
- **CTR (Click-Through Rate)**: (Clicks / Impresiones) * 100 → % de usuarios que hacen clic después de ver el anuncio
- **CPC (Costo Por Clic)**: Costo total / Clicks → costo de cada clic
- **Tasa de conversión (CVR)**: (Signups / Clicks) * 100 → % de clics que se convierten en registro
- **CPA (Costo Por Adquisición)**: Costo total / Signups → costo de cada registro

| Métrica               | Campaña A (Landing principal) | Campaña B (Blog content) | Campaña C (Competidor) |
|-----------------------|--------------------------------|---------------------------|-------------------------|
| CTR                   | 3% (1.500 / 50.000 *100)       | 4% (4.800 / 120.000 *100) | 6% (900 / 15.000 *100)  |
| CPC                   | $1,40 ($2.100 / 1.500)         | $0,375 ($1.800 / 4.800)   | $3,55 ($3.200 / 900)    |
| Tasa de conversión (CVR) | 3% (45 / 1.500 *100)        | 0,5% (24 / 4.800 *100)    | 4% (36 / 900 *100)      |
| CPA                   | $46,67 ($2.100 / 45)           | $75 ($1.800 / 24)         | $88,89 ($3.200 / 36)    |

---

## 2. ¿Qué campaña escalar y cuál pausar?
### 🚀 Campaña para ESCALAR: **Campaña A (Landing principal)**
Justificación numérica:
- Tiene el **CPA más bajo de todas ($46,67)**, un 38% más barato que la Campaña B y un 48% más barato que la Campaña C.
- Su tasa de conversión (3%) es sólida para keywords transaccionales de producto, y a diferencia de la Campaña C, su CPC es bajo ($1,40) por lo que hay margen para aumentar alcance sin disparar costos.
- Las keywords ("software gestion inventario", "inventario pymes") son de intención transaccional alta: usuarios buscan directamente una solución como la tuya, por lo que la calidad de los registros es probablemente mayor (más probabilidad de convertirse en clientes pagos, no solo registros).

### ⏸️ Campaña para PAUSAR: **Campaña C (Competidor)**
Justificación numérica:
- Tiene el **CPA más alto de todas ($88,89)**, casi el doble que la Campaña A.
- Aunque su CTR y CVR son altos, su CPC es muy elevado ($3,55, 2,5x más caro que la Campaña A) porque las keywords de competidor son muy competitivas y tienen poca intención de compra en muchos casos (usuarios solo comparan sin intención de cambiar de herramienta).
- Con el presupuesto que invertiste en C ($3.200) obtuviste 36 registros; si ese mismo presupuesto lo hubieras puesto en A, habrías obtenido ~68 registros (un 89% más).

### 📝 Campaña B: NO pausar, optimizar
Aunque su CPA es alto ($75), sus clics son muy baratos ($0,375) y su volumen de impresiones es alto. El problema no es el tráfico, sino la conversión: su CVR es de solo 0,5% (6 veces menor que la Campaña A). Tiene potencial si mejoras el flujo de conversión del blog.

---

## 3. Redistribución del presupuesto de $5.000/mes
La regla es asignar más presupuesto a las campañas con menor CPA y mayor retorno, manteniendo una parte para prueba y optimización de campañas con potencial:

| Campaña               | Presupuesto asignado | % del total | Justificación                                                                 |
|-----------------------|----------------------|-------------|--------------------------------------------------------------------------------|
| Campaña A (Landing principal) | $3.000          | 60%         | Es la de mayor rendimiento: con $3.000 obtendrías ~64 registros (vs 45 actuales). Aumenta el presupuesto gradualmente (20-30% semanal) para no perder eficiencia en subastas. |
| Campaña B (Blog)      | $1.250               | 25%         | Reducimos su presupuesto un 30% para quitar el gasto en clics de baja calidad, pero mantenemos inversión para testear mejoras en conversión. Con optimizaciones en el blog puedes subir su CVR a 1,5% y bajar su CPA a $25. |
| Campaña C (Competidor)| $0 (pausada)         | 0%          | Eliminamos su gasto por su alto CPA. Puedes reactivarla en el futuro si tienes una oferta diferenciadora clara (ej: "migra desde [competidor] y obtén 2 meses gratis"). |
| Pruebas nuevas        | $750                 | 15%         | Destinamos una parte pequeña a probar nuevas oportunidades: keywords long-tail transaccionales para A, nuevos formatos de anuncio o audiencias similares. |

*Nota: Si mediste la calidad de los registros (no solo cantidad, sino cuántos se convierten en clientes pagos) y los registros de la Campaña C tienen una tasa de pago muy alta, puedes asignarle un presupuesto pequeño de prueba ($250) para validar. Por defecto, con los datos de registros que tienes, es mejor pausarla.*

---

## 4. A/B tests sugeridos para el próximo mes
Ordenados por impacto potencial:

### 🔹 Para Campaña A (mayor presupuesto, mayor impacto)
1. **Test de anuncios: Oferta diferenciadora vs beneficio general**
   - Variante A (actual): "Software de gestión de inventario para pymes"
   - Variante B: "Gestiona tu inventario en 10 minutos al día | Prueba gratis 14 días"
   - Objetivo: Subir el CTR y la CVR al enfatizar una propuesta de valor concreta.

2. **Test de landing page: Formulario corto vs formulario largo**
   - Variante A (actual): Formulario de 4 campos (nombre, email, empresa, teléfono)
   - Variante B: Formulario de solo 2 campos (nombre, email)
   - Objetivo: Subir la CVR reduciendo fricción en el registro (puedes pedir datos adicionales después del registro).

### 🔹 Para Campaña B (mayor margen de mejora)
1. **Test de flujo de conversión: CTA en blog vs redirección directa a landing**
   - Variante A (actual): Usuario llega al artículo del blog, tiene que buscar el CTA para registrarse
   - Variante B: Usuario llega al artículo, y después de 30 segundos o al llegar al final del texto, se le muestra un popup o banner sticky con oferta de prueba gratis
   - Objetivo: Subir la CVR de 0,5% a al menos 1,5% (lo que bajaría el CPA a $25).

2. **Test de keywords: Filtrar intención informativa vs transaccional**
   - Agrega palabras clave negativas como "gratis", "ejercicios", "trabajo", "ejemplo" para excluir búsquedas sin intención de compra.
   - Prueba agregar keywords long-tail como "software para gestionar inventario de restaurante" que combinan intención informativa y transaccional.

### 🔹 Test transversal
- **Test de audiencia: Usuarios nuevos vs remarketing**
  - Crea una campaña de remarketing para usuarios que visitaron tu sitio pero no se registraron, con una oferta especial (ej: "¿Olvidaste terminar tu registro? Obtén 1 mes gratis al inscribirte hoy").
  - El CPA de remarketing suele ser un 50-70% más bajo que el de campañas de captación fría.