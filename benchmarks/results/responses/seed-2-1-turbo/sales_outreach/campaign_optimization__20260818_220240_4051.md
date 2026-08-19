# Seed 2.1 Turbo — sales_outreach/campaign_optimization

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 202.641s | tokens_per_second: 60.7
- input_tokens: 348 | output_tokens: 12292

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

---
### 1. Cálculo de métricas por campaña
Usamos como conversión objetivo los **signups (registros)**, y las fórmulas estándar de Google Ads:
- **CTR (Tasa de clic):** `(Clicks / Impresiones) * 100` → Porcentaje de usuarios que hacen clic en el anuncio al verlo.
- **CPC (Costo por clic):** `Costo total / Clicks totales` → Costo de cada visita al sitio.
- **CR (Tasa de conversión):** `(Signups / Clicks) * 100` → Porcentaje de clicks que terminan en registro.
- **CPA (Costo por registro):** `Costo total / Signups totales` → Costo de cada nuevo registro.

---
#### Resultados por campaña
| Campaña                | CTR   | CPC   | CR    | CPA    |
|------------------------|-------|-------|-------|--------|
| A (Landing principal)  | 3,0%  | $1,40 | 3,0%  | $46,67 |
| B (Blog content)       | 4,0%  | $0,38 | 0,5%  | $75,00 |
| C (Competidor)         | 6,0%  | $3,56 | 4,0%  | $88,89 |

---
##### Cálculos detallados para verificación:
- **Campaña A:**  
  CTR = (1.500 / 50.000) * 100 = 3% | CPC = 2.100 / 1.500 = $1,40 | CR = (45 / 1.500) * 100 = 3% | CPA = 2.100 / 45 = $46,67
- **Campaña B:**  
  CTR = (4.800 / 120.000) * 100 = 4% | CPC = 1.800 / 4.800 = $0,38 | CR = (24 / 4.800) * 100 = 0,5% | CPA = 1.800 / 24 = $75,00
- **Campaña C:**  
  CTR = (900 / 15.000) * 100 = 6% | CPC = 3.200 / 900 = $3,56 | CR = (36 / 900) * 100 = 4% | CPA = 3.200 / 36 = $88,89

---
### 2. Campaña a escalar y a pausar (justificación numérica)
Supuesto base: el objetivo principal es maximizar el número de signups al menor costo, asumiendo que todos los registros tienen el mismo valor (no contamos con datos de tasa de pago o LTV por origen).

---
#### 📈 Campaña a ESCALAR: Campaña A (Landing principal)
Justificación con números:
1. Tiene el **CPA más bajo del grupo ($46,67)**: cada registro cuesta un 38% menos que en la Campaña B y un 48% menos que en la Campaña C.
2. Su tasa de conversión (3%) es muy sólida para términos genéricos de producto, lo que confirma que tanto la intención de los usuarios como el rendimiento del landing page son buenos.
3. Con el mismo presupuesto que se invierte en la Campaña C para obtener 36 registros ($3.200), en la Campaña A se obtendrían ~69 registros, casi el doble.

---
#### ⏸️ Campaña a PAUSAR (o reducir drásticamente): Campaña C (Competidor)
Justificación con números:
1. Tiene el **CPA más alto de las tres ($88,89)**, casi el doble que la Campaña A. Aunque su tasa de conversión es la mayor (4%) por la intención muy alta de los usuarios (que ya conocen un competidor y buscan alternativas), el CPC es excesivamente caro ($3,56, 2,5 veces más que la Campaña A), lo que hace que la inversión sea muy poco eficiente.
2. Su volumen de impresiones es muy bajo (15.000/mes), por lo que tiene poco margen de escalado para mejorar su rendimiento.

⚠️ Matización clave: Si tienes datos de que los registros de términos de competidor tienen una tasa de pago o LTV mucho mayor que los de otras campañas (lo que es habitual, por ser usuarios más avanzados en el proceso de compra), no la pares completamente: reduce su presupuesto para mantener solo los clicks de mayor calidad.

---
### 3. Redistribución del presupuesto de $5.000/mes
Primero, aclaramos los supuestos de la distribución:
1. Las campañas no están al 100% de su cuota de impresiones, por lo que pueden escalar hasta un 30% más sin que su CPA aumente significativamente (valor estándar en campañas de búsqueda con cuota media).
2. Buscamos un equilibrio entre eficiencia a corto plazo (maximizar signups inmediatos) y crecimiento a largo plazo (generar demanda nueva con contenido de tope de embudo).
3. El gasto anterior sumaba $7.100, por lo que debemos recortar $2.100 en total, priorizando los recortes en las campañas menos eficientes.

---
#### Distribución propuesta (equilibrada):
| Campaña                | Presupuesto | % del total | Cambio vs gasto anterior | Signups estimados |
|------------------------|-------------|-------------|---------------------------|-------------------|
| A (Landing principal)  | $2.700      | 54%         | +$600 (+29%)              | ~58               |
| B (Blog content)       | $1.500      | 30%         | -$300 (-17%)              | ~20               |
| C (Competidor)         | $800        | 16%         | -$2.400 (-75%)            | ~9                |
| **Total**              | **$5.000**  | **100%**    | **-$2.100 (-30%)**        | **~87 signups**   |

---
#### Justificación:
1. **Campaña A:** Aumentamos su presupuesto casi un 30% (hasta el límite de escalado sin pérdida de eficiencia) porque es la más rentable. Con este aumento, pasamos de 45 a ~58 registros al mes.
2. **Campaña B:** Reducimos su presupuesto solo un 17%, ya que aunque su CPA es mayor que la A, tiene un CPC muy bajo y genera conciencia de marca entre usuarios que aún no conocen tu producto (tope de embudo). Estos usuarios luego pueden convertir en campañas de fondo de embudo en meses siguientes.
3. **Campaña C:** Reducimos su presupuesto drásticamente un 75%, ya que es la menos eficiente para generar registros. Mantenemos un presupuesto mínimo para no perder la captura de usuarios de muy alta intención, que suelen tener mayor probabilidad de convertirse en clientes pagos.

---
📌 Escenario alternativo de máxima eficiencia a corto plazo (si solo te importan los signups inmediatos):
Si la Campaña A tiene suficiente volumen de búsquedas para escalar más de un 30%, puedes asignarle más presupuesto y reducir aún más B y C:
- Campaña A: $3.200 → ~69 signups
- Campaña B: $1.000 → ~13 signups
- Campaña C: $800 → ~9 signups
- Total: ~91 signups

---
### 4. A/B tests sugeridos para el próximo mes
Los tests se adaptan a los puntos débiles de cada campaña:

---
#### 🎯 Para Campaña A (mejorar aún más la eficiencia para justificar el aumento de presupuesto)
1. **Test de landing page:** Compara el landing actual con una variante con formulario más corto (solo nombre y email) y prueba social destacada (ej: "Usado por más de 2.000 pymes").  
   *Objetivo: Aumentar el CR en al menos un 15%, reduciendo el CPA por debajo de los $40.*
2. **Test de copia de anuncios:** Prueba una variante que destaque el precio/ahorro vs una que destaque la facilidad de uso.  
   *Objetivo: Aumentar el CTR para capturar más clicks sin aumentar el CPC.*
3. **Test de keywords long tail:** Agrega términos más específicos como "software de inventario para tiendas de ropa" o "gestión de inventario pymes sin instalación", y compara su rendimiento con las keywords genéricas actuales.  
   *Objetivo: Capturar clicks de mayor calidad con menor CPC, aumentando el volumen de registros sin subir el CPA.*

---
#### 📝 Para Campaña B (solucionar el bajo CR, su principal problema)
1. **Test de oferta de conversión:** Compara el objetivo actual (signup para prueba gratuita) con una oferta de contenido gratuito adaptada a la búsqueda:
   - Para "como gestionar inventario": Plantilla Excel de gestión de inventario
   - Para "problemas inventario restaurante": Guía PDF "5 pasos para reducir pérdidas de inventario en restaurantes"  
   *Objetivo: Aumentar el CR de 0,5% a al menos 2%, reduciendo el CPA por debajo de los $20. Luego puedes nutrir a estos registros por email para que se conviertan en clientes.*
2. **Test de destino del anuncio:** Compara llevar a los usuarios directamente al artículo del blog vs a una página de destino dedicada al recurso gratuito.  
   *Objetivo: Medir cuál ruta genera más registros de calidad.*
3. **Test de palabras clave negativas:** Excluye búsquedas sin intención de usar un software (ej: "ejercicios de gestion de inventario", "inventario ejercicio resuelto").  
   *Objetivo: Mejorar la calidad de los clicks, aumentando el CR sin aumentar el CPC.*

---
#### 🏁 Para Campaña C (reducir el alto CPC y mejorar el CPA)
1. **Test de keywords long tail de competidor:** Compara las keywords amplias actuales ("alternativa a [competidor]", "[competidor] vs") con términos más específicos como "alternativa a [competidor] para pymes pequeñas" o "[competidor] vs [tu marca] precio".  
   *Objetivo: Reducir el CPC al capturar búsquedas con menos competencia, manteniendo el CR alto.*
2. **Test de copia de anuncio centrada en ventajas diferenciales:** Prueba anuncios que destaquen explícitamente las ventajas frente al competidor (ej: "50% más barato que [competidor]", "Sin contrato de permanencia") vs anuncios genéricos de tu producto.  
   *Objetivo: Aumentar aún más el CTR y el CR, reduciendo el CPA.*
3. **Test de estrategia de pujas:** Compara la estrategia de puja actual con una estrategia de CPA objetivo, configurando un valor ligeramente menor al CPA actual.  
   *Objetivo: Reducir el CPA automáticamente al optimizar las pujas por los clicks con mayor probabilidad de convertir.*

---
#### 📊 Test transversal para todas las campañas
- **Test de modelo de atribución:** Compara los resultados con atribución de último clic (el modelo actual) con atribución de primer clic o lineal.  
  *Objetivo: Medir si las campañas de tope de embudo (B) contribuyen a las conversiones de las campañas de fondo (A y C), para ajustar el presupuesto en función del valor real de cada campaña en el recorrido de compra.*