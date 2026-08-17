# Muse Spark 1.2 — sales_outreach/campaign_optimization

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 7.13 | quality: 8.0
- latency_total: 16.034s | tokens_per_second: 176.3
- input_tokens: 260 | output_tokens: 2827

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

Esta campaña está gastando $7,100 para un presupuesto de $5,000 y está optimizando para la métrica equivocada. Aquí está el análisis:

### 1. CÁLCULO DE MÉTRICAS

| Métrica | Fórmula | Campaña A | Campaña B | Campaña C |
| :--- | :--- | :--- | :--- | :--- |
| **CTR** | `Clicks / Impresiones` | **3.0%** | **4.0%** | **6.0%** |
| **CPC** | `Costo / Clicks` | **$1.40** | **$0.37** | **$3.56** |
| **Tasa de Conversión** | `Signups / Clicks` | **3.0%** | **0.5%** | **4.0%** |
| **CPA** | `Costo / Signups` | **$46.67** | **$75.00** | **$88.89** |

**Resumen actual:** Gastas $7,100 para 105 signups. CPA Blended: **$67.62**

> Conclusión rápida: CTR alto no es igual a rentable. La Campaña B y C te engañan con CTR alto pero te están matando el CPA.

### 2. ¿QUÉ ESCALAR Y QUÉ PAUSAR?

**ESCALAR: CAMPAÑA A - La Ganadora Clara**
Es tu campaña más eficiente y rentable. Tiene el **CPA más bajo de todos: $46.67**, un 38% más barato que B y 47% más barato que C. Su intención es transaccional `software gestion inventario` = gente lista para comprar. Su tasa de conversión del 3% es 6 veces mejor que B. Cada dólar aquí te trae más clientes.

**PAUSAR: CAMPAÑA B - Tráfico Barato que No Convierte**
Tiene el CPC más barato `$0.37` y CTR bueno `4%`, pero es una trampa. Su tasa de conversión es **miserable: 0.5%**. Necesitas 200 clicks para 1 signup. Su intención es informacional `como gestionar...` = gente que quiere aprender, no comprar. Su CPA de $75 es 60% más caro que A. Estás pagando por curiosos, no por compradores.

**OPTIMIZAR Y REDUCIR, NO ESCALAR: CAMPAÑA C - Convierte Bien Pero Es Insostenible**
Es tu mejor convertidora `4.0%` y con mejor CTR `6.0%`, lo que indica que tu oferta resuena contra el competidor. El problema es el costo: **CPC de $3.56 es 2.5x más caro que A**. Eso dispara tu CPA a $88.89, el más caro de todos. Es 90% más cara que A por cada cliente. Escalarla así te quiebra. Hay que optimizarla antes de escalar.

### 3. REDISTRIBUCIÓN DE PRESUPUESTO DE $5,000

No puedes mantener las 3. Tienes que recortar $2,100. Mi recomendación es una estrategia 70/30 enfocada en eficiencia.

**Propuesta Recomendada:**

| Campaña | Presupuesto Nuevo | % | Justificación | Signups Estimados |
| :--- | :--- | :--- | :--- | :--- |
| **A - Principal** | **$3,500** | 70% | Escalar lo que ya es rentable. Bajar CPA blended. | ~75 |
| **C - Competidor** | **$1,500** | 30% | Mantenerla pero obligarla a ser rentable. Con $1,500 la fuerzas a optimizar CPC y Quality Score. | ~17 |
| **B - Blog** | **$0** | 0% | **PAUSADA en Google Ads.** | 0 |
| **TOTAL** | **$5,000** | 100% | | **~92 signups** |

**¿Por qué es mejor?**
*   **Antes:** 105 signups por $7,100 = CPA $67.62
*   **Ahora:** 92 signups por $5,000 = **CPA $54.34**
*   Consigues solo 13 signups menos pero **ahorras $2,100 al mes**. Tu eficiencia mejora un 20%.

> **¿Qué hacer con la Campaña B?** No la borres. Muévela a otro objetivo: Cámbiala de `Signups` a `Lead Magnet` como descargar un ebook o suscribirse al newsletter. Y deja de pagar clicks en Search, pásala a SEO orgánico y a una audiencia de Remarketing en Display/YouTube por $200-300/mes. Es para nutrir, no para vender directo.

**Alternativa si no quieres pausar B:** A: $3,000 `60%` / C: $1,200 `24%` / B: $800 `16%` pero cambiando su conversión a micro-conversión y con CPC máximo de $0.40.

### 4. A/B TESTS PARA EL PRÓXIMO MES

No testees todo a la vez. Un test por campaña.

**Test 1: Campaña A - Landing Principal [Prioridad #1]**
*   **Hipótesis:** El formulario actual genera fricción. Reducir campos aumentará la conversión.
*   **Variable A:** Landing actual con formulario de 5 campos `Nombre, Email, Empresa, Teléfono, Empleados`
*   **Variable B:** Landing con formulario de 2 campos `Email + Empresa` + prueba social arriba `Logos de clientes + "Usado por 1,200+ pymes"`
*   **Métrica de éxito:** Tasa de Conversión. Objetivo: pasar de 3.0% a >4.5%
*   **Duración:** Hasta 100 conversiones por variante.

**Test 2: Campaña C - Competidor [Para bajar el CPC de $3.56]**
*   **Hipótesis:** Una landing de comparativa directa convertirá mejor y mejorará el Quality Score que una landing genérica.
*   **Variable A:** Anuncio y landing genérica actual.
*   **Variable B:** Anuncio `¿Buscas alternativa a [Competidor]? Más barato y sin permanencia` -> Landing de comparativa `Tabla [Competidor] vs Tú: Precio, Funciones, Soporte`
*   **Métrica de éxito:** CPA y Quality Score. Objetivo: Bajar CPA de $88.89 a <$60
*   **Extra:** Añade keywords negativas exactas de `[competidor] login`, `[competidor] soporte` para no pagar por usuarios actuales.

**Test 3: Campaña B - Cambio de Oferta [Para no desperdiciar el tráfico barato]**
*   **Hipótesis:** El usuario informacional no quiere un "Signup", quiere una solución gratis.
*   **Variable A:** CTA actual `Prueba Gratis / Solicita Demo`
*   **Variable B:** CTA `Descarga Gratis: Plantilla Excel para Control de Inventario Restaurante` -> Luego nutres por email y lo llevas a signup.
*   **Métrica de éxito:** Costo por Lead Magnet `< $5` y Tasa de conversión de Lead a Signup >8%

**Test 4: Global - Estructura de Puja**
*   **Hipótesis:** Estás pagando de más por click en manual.
*   **Variable A:** Puja Manual CPC actual.
*   **Variable B:** Cambiar Campaña A a `Maximizar Conversiones con tCPA de $50`. Deja que Google busque usuarios con perfil convertidor.
*   **Métrica de éxito:** Mantener o bajar CPA con mismo presupuesto.

**Próximo paso inmediato:** Pausa B hoy mismo, sube el presupuesto de A a $3,500 y revisa el informe de términos de búsqueda de C para añadir negativas. En 14 días revisamos si el CPA de C baja.