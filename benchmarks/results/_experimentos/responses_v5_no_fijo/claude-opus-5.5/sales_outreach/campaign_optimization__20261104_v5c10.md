# Claude Opus 5.5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 49.251s | tokens_per_second: 101.8
- input_tokens: 395 | output_tokens: 5015

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

## Un dato importante antes de empezar

Sumando los costos, **el mes pasado gastaste $7,100**, no $5,000 ($2,100 + $1,800 + $3,200). Estás $2,100 (42%) por encima de tu presupuesto. Así que no solo hay que redistribuir, también hay que recortar.

---

## 1. Métricas por campaña

| Métrica | Fórmula | A (Landing) | B (Blog) | C (Competidor) |
|---|---|---|---|---|
| **CTR** | Clicks / Impresiones | **3.0%** | **4.0%** | **6.0%** ✅ |
| **CPC** | Costo / Clicks | **$1.40** | **$0.38** ✅ | **$3.56** |
| **Conv. Rate** | Signups / Clicks | **3.0%** | **0.5%** | **4.0%** ✅ |
| **CPA** | Costo / Signups | **$46.67** ✅ | **$75.00** | **$88.89** |

**Total actual:** 105 signups con $7,100, un **CPA combinado de $67.62**.

**Cómo leer cada campaña:**
- **A** es la más equilibrada: el CPC es razonable y convierte bien, así que tiene el CPA más bajo.
- **B** trae clicks baratos, pero la intención es informativa. La gente busca aprender, no comprar, y por eso convierte 6 veces menos que A.
- **C** tiene la audiencia de mayor intención (CTR 6%, conversión 4%), pero el CPC de $3.56 la hace la más cara por signup.

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ Escalar: Campaña A
- Su CPA es el más bajo: **$46.67**, un 31% mejor que el promedio combinado.
- Cada $1,000 adicionales generarían unos **21 signups**, contra 13 en B y 11 en C.
- **Ojo:** al escalar, el CPA suele subir porque entras a subastas más caras. Revisa el *Impression Share* en Google Ads. Si ya está por encima del 80%, hay poco margen para crecer sin que el CPA suba bastante.

### ⚠️ Reducir y optimizar, no pausar: Campaña C
- Es la peor en CPA ($88.89), pero **el problema es el costo, no la audiencia**. Tiene la mejor tasa de conversión (4%).
- Los usuarios que buscan alternativas a un competidor suelen tener mayor intención de pago, porque ya usan una solución y están insatisfechos.
- Conviene recortarle presupuesto, quedarte solo con las keywords que mejor funcionan y bajar las pujas.

### ⚠️ Reducir mucho y reestructurar: Campaña B
- Su CPA ($75) es mejor que el de C, pero su conversión del 0.5% muestra que el tráfico no está listo para registrarse.
- No la pausaría del todo. Esta audiencia sirve para **remarketing** y para ofrecerle algo más fácil de aceptar que un signup.

### 🔑 La decisión real depende de un dato que falta
Un signup no es un cliente. Necesitas saber **qué porcentaje de signups de cada campaña pasa a pago**. Ejemplo hipotético:

| | CPA signup | % a pago | CPA cliente real |
|---|---|---|---|
| A | $46.67 | 15% | $311 |
| C | $88.89 | 35% | **$254** ✅ |

Si los signups de C convierten más del doble que los de A, **C sería tu mejor campaña**. Antes de hacer cortes drásticos, conecta tu CRM o tu sistema de pagos con Google Ads, por ejemplo mediante *offline conversion import*.

---

## 3. Redistribución de los $5,000

Asumiendo que todavía no tienes los datos de conversión a pago:

| Campaña | Antes | Ahora | Cambio | CPA esperado | Signups est. |
|---|---|---|---|---|---|
| **A** (Landing) | $2,100 | **$2,600** | +24% | ~$52 (+10% por escala) | ~50 |
| **C** (Competidor) | $3,200 | **$1,400** | −56% | ~$75 (al quedarte con las mejores keywords) | ~18 |
| **B** (Blog) | $1,800 | **$600** | −67% | ~$75 | ~8 |
| **Remarketing** (nueva) | $0 | **$400** | nueva | ~$50 | ~8 |
| **Total** | $7,100 | **$5,000** | | **~$60** | **~84** |

**Resultado:** tendrás menos signups (84 contra 105) porque gastas 30% menos, pero cada uno costará unos $60 en vez de $67.62, es decir, **11% más eficiente**.

**Acciones concretas por campaña:**
- **A:** prueba la estrategia de puja *Target CPA* con un objetivo de alrededor de $50. Amplía con variantes como "sistema de inventario", "control de stock pymes" y "software inventario restaurante".
- **C:** revisa el informe de términos de búsqueda, quédate con concordancia exacta o de frase, y pausa las keywords con CPA mayor a $100. "[Competidor] vs" suele traer usuarios comparando, con mayor intención.
- **B:** mantén solo la keyword que mejor convierta. "Problemas inventario restaurante" probablemente sea la mejor, porque es más específica que "como gestionar inventario".
- **Remarketing:** dirígelo a quienes visitaron el blog (los 4,800 clicks de B) y no se registraron. Ya te conocen, así que deberían convertir mucho mejor.

---

## 4. A/B tests para el próximo mes

### Primero, una advertencia sobre el volumen
Con unos 1,900 clicks al mes en A, **no puedes detectar mejoras pequeñas en la landing**. Con una conversión base del 3%:
- Detectar una mejora del 20% (de 3% a 3.6%) requiere unos **14,000 clicks por variante**, es decir, varios meses.
- Detectar una mejora del 50% (de 3% a 4.5%) requiere unos **2,500 clicks por variante**, alrededor de 2 o 3 meses.

**Conclusión:** prueba **cambios grandes**, no colores de botón. Prioriza también los tests de anuncios, donde el volumen de impresiones sí alcanza para obtener resultados.

### Tests recomendados (por prioridad)

**🥇 Test 1: copy de anuncios en C (bajar el CPC)**
- **Variante A:** el anuncio actual.
- **Variante B:** incluir el precio o la comparación directa, por ejemplo "50% más barato que [Competidor]. Migración gratis."
- **Métrica:** CTR y CPA. Un anuncio más específico mejora el Quality Score, lo que baja el CPC, y además filtra clicks sin intención real.
- **Volumen:** viable con unas 7,500 impresiones por variante.

**🥈 Test 2: oferta de la landing en A (cambio grande)**
- **Variante A:** "Prueba gratis 14 días" o tu oferta actual.
- **Variante B:** una oferta de menor compromiso, como "Ver demo en 2 minutos" o un registro sin tarjeta de crédito.
- **Métrica:** conversión a signup y, sobre todo, **conversión a pago**.

**🥉 Test 3: conversión intermedia en B**
- **Variante A:** CTA de registro en el artículo (lo actual).
- **Variante B:** un recurso descargable, como "Descarga gratis: Plantilla Excel de inventario para restaurantes", seguido de una secuencia de emails que lleve al registro.
- **Métrica:** costo por lead y conversión del lead a signup en 30 días.
- **Hipótesis:** quien está aprendiendo no se registra a un software, pero sí descarga una plantilla útil.

**Test 4: landing dedicada para C**
- **Variante A:** la landing genérica.
- **Variante B:** una página de comparación "[Tu producto] vs [Competidor]" con tabla de funciones, testimonios de clientes que migraron y una guía de migración.
- **Métrica:** conversión a signup. Podría pasar del 4% a 6% o más, lo que bajaría el CPA a unos $60 aunque el CPC no cambie.

### Reglas para que los tests sean válidos
1. **Un solo cambio por test**, para saber qué causó la diferencia.
2. **Usa Google Ads Experiments**, que reparte el tráfico 50/50 de forma automática.
3. **Define antes de empezar** la métrica principal y la duración mínima del test.
4. **No detengas un test antes de tiempo**, aunque una variante vaya ganando la primera semana.

---

## Resumen

| Prioridad | Acción |
|---|---|
| 🔴 Urgente | Corregir el exceso de gasto: estás gastando $7,100 con un presupuesto de $5,000 |
| 🔴 Urgente | Medir la conversión de signup a pago por campaña |
| 🟡 Este mes | Redistribuir así: A $2,600 / C $1,400 / B $600 / Remarketing $400 |
| 🟢 Este mes | Lanzar los tests 1 (anuncios de C) y 3 (recurso descargable en B) |

Si me compartes la tasa de conversión a pago o el LTV por cliente, puedo calcular tu CPA máximo rentable y afinar la redistribución.