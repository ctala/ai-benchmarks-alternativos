# Claude Opus 5 (suscripción) — sales_outreach/campaign_optimization

- model_id: `claude-opus-5`
- success: True  | final: 7.82 | quality: 10.0
- latency_total: 141.742s | tokens_per_second: 63.1
- input_tokens: 2 | output_tokens: 8951

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

## 1. Los números

| Campaña | Impresiones | Clicks | CTR | CPC | Signups | CVR | Costo | CPA |
|---|---|---|---|---|---|---|---|---|
| **A** Landing | 50,000 | 1,500 | 3.00% | $1.40 | 45 | 3.00% | $2,100 | **$46.67** |
| **B** Blog | 120,000 | 4,800 | 4.00% | $0.38 | 24 | 0.50% | $1,800 | **$75.00** |
| **C** Competidor | 15,000 | 900 | 6.00% | $3.56 | 36 | 4.00% | $3,200 | **$88.89** |
| **Total** | 185,000 | 6,900 | 3.73% | $1.03 | 105 | 1.52% | **$7,100** | **$67.62** |

**Primer hallazgo, antes del análisis:** gastaste $7,100 con un presupuesto de $5,000. Estás 42% arriba. Aunque no cambies nada más, vas a recortar $2,100.

**Lo que dicen los números:**
- A gana por **costo**, no por intención. Su CVR (3.0%) es *menor* que la de C (4.0%). Todo su ventaja está en pagar $1.40 por click en vez de $3.56.
- C gana por **intención**. CTR 6% y CVR 4% son los mejores del account. Pierde en la subasta.
- B compra tráfico barato que no convierte. 4,800 clicks y solo 24 signups.

**Advertencia estadística:** la diferencia de CVR entre A (3.0%) y C (4.0%) **no es significativa** con este volumen (z ≈ 1.27, p ≈ 0.20). No concluyas que C convierte mejor. Lo que sí es sólido es la diferencia de CPC (900+ clicks es muestra suficiente) y el desastre de B (0.5% vs 3.0% es 6× de diferencia, eso no es ruido).

---

## 2. Qué escalar y qué pausar

**Escalar: A.** CPA $46.67, 47% mejor que el blended. Es el único que sostiene volumen adicional a costo razonable.

**Pero ojo con el techo:** con 50,000 impresiones no sabés cuánto espacio queda. **El dato que falta es impression share.** Si A está al 40%, tenés 2.5× de headroom. Si está al 85%, subir presupuesto solo te sube el CPC. Míralo antes de mover un peso.

**Recortar (no pausar): C.** CPA $88.89, el peor. Pero acá hay un detalle que cambia la decisión: **C no es escalable aunque quisieras.** 15,000 impresiones mensuales es el techo natural de "alternativa a [competidor]". Está limitada por volumen de búsqueda, no por presupuesto. Los $3,200 que le metiste ya compraron casi todo el inventario disponible. Recortá a lo que compre los términos de mayor intención ("[competidor] vs") y soltá los genéricos.

**Recortar y rediseñar: B.** Acá está el punto que importa más que toda la redistribución:

> B no es una mala campaña. Es una **buena fuente de tráfico sin ruta de conversión.** 4,800 clicks a $0.38 es tráfico que ya estás pagando y se está fugando entero.

"Cómo gestionar inventario" es intención de **investigación**, no de compra. Pedirle signup a esa gente es pedirle matrimonio en la primera cita. Si llevaras esa CVR de 0.5% a apenas 1.2% (nada heroico para top-funnel), serían 58 signups con los mismos $1,800 → **CPA $31, la mejor del account.** Ese es el mayor upside que tenés y no requiere un peso más de presupuesto.

**Nada se pausa a cero**, salvo esta excepción: si no tenés capacidad de construir la oferta intermedia para B este mes, pausala completa y mové todo a A. Mantenerla como está es quemar $1,800.

---

## 3. Redistribución de los $5,000

| Campaña | Actual | Propuesto | Δ | Signups proyectados | CPA esperado |
|---|---|---|---|---|---|
| A | $2,100 | **$2,800** | +33% | ~50 | $56 |
| C | $3,200 | **$1,600** | −50% | ~21 | $76 |
| B | $1,800 | **$600** | −67% | 8 (o ~24 si el test funciona) | $75 → $25 |
| **Total** | $7,100 | **$5,000** | −30% | **~79 (hasta 95)** | **~$63** |

**Supuestos explícitos** (si no se cumplen, el plan cambia):
- El CPA de A **sube al escalar**, no se mantiene. Asumí $46.67 → $56 (+20%) por deterioro marginal de la subasta. Si tu impression share ya es alto, va a subir más.
- C mejora su CPA al cortar términos genéricos ($88.89 → ~$76).
- B queda con presupuesto de test, no de producción: $600 compra ~1,600 clicks, suficiente para leer si la oferta intermedia mueve la aguja.

**Sé honesto con la magnitud:** esta redistribución te compra ~8% de mejora en CPA. Es el movimiento correcto, pero no es donde está el dinero. El dinero está en el punto siguiente.

**El agujero real: no sabés cuánto vale un signup, ni si vale lo mismo en cada campaña.**

Un signup de C viene de alguien que está evaluando activamente reemplazar su software. Un signup de B viene de alguien googleando cómo ordenar su bodega. Es perfectamente plausible que el de C convierta a pago 3× más. **Si eso es cierto, el CPA efectivo de C es el mejor de las tres y esta redistribución está al revés.**

Antes de comprometer el recorte de C, medí signup→pago por campaña. Mientras no lo tengas, hacé el shift en dos tiempos: este mes movés la mitad de lo propuesto, y con los datos de conversión a pago decidís el resto.

---

## 4. A/B tests para el próximo mes

Primero, la restricción que casi nadie calcula antes de testear:

> **Tu volumen no soporta tests de mejoras pequeñas.** Para detectar un lift de 3.0% → 3.9% en la campaña A con poder estadístico decente necesitás ~6,600 clicks por variante (~13,000 en total). A 1,500 clicks/mes son **8-9 meses**. Para detectar 3.0% → 6.0% necesitás ~1,500 clicks: **un mes**.

Conclusión práctica: **solo testeá cambios radicales.** Nada de colores de botón ni variantes de headline. Si el cambio no tiene chance de duplicar, no lo testees con este tráfico.

**Test 1 — B: ruta de conversión (máxima prioridad)**
- Control: blog → CTA de signup a la app
- Variante: blog → herramienta gratuita (calculadora de merma / plantilla de inventario) → email → secuencia de nurture
- Métrica primaria: leads capturados. Secundaria: leads → signup a 30 días
- Por qué primero: es el único con lift esperado de 3× y ya tenés el tráfico pagado. Baseline 0.5% hace que un salto a 1.5% sea legible con el presupuesto de test.

**Test 2 — C: mensaje de switching**
- Control: mensaje de features/precio vs competidor
- Variante: "Migramos tu data de [competidor] gratis, en 48 horas"
- Por qué: el que busca "alternativa a X" ya decidió que quiere irse. Su objeción no es el precio, es el costo de mudarse. Nadie testea esto y es donde vive la fricción real.
- Nota: con 900 clicks/mes solo vas a leer diferencias grandes. Corré 6 semanas, no 4.

**Test 3 — A: formato de oferta**
- Control: trial self-serve
- Variante: demo agendada (o al revés, según lo que tengas hoy)
- Por qué: es un cambio lo bastante grande como para producir un delta detectable en un mes. Impacta CVR y también calidad del signup.

**Test 4 — estructural, no es A/B: control de match types y negativos**
- Revisá el search terms report de B. Con 120,000 impresiones en keywords informacionales, apostaría a que hay una fracción alta de queries irrelevantes que ni siquiera son de tu ICP.
- En C, exact match sobre los términos con marca para bajar ese CPC de $3.56.
- Esto no necesita test: es limpieza y se paga sola.

**Y lo que no es un test pero va antes que todos:** instrumentá **signup → cliente pago, atribuido por campaña**. Todo lo anterior optimiza una métrica intermedia. Sin el tramo final, podés estar escalando muy eficientemente la campaña que trae la peor gente.

---

**Datos que te pediría antes de ejecutar esto:**
1. Impression share por campaña (define el techo real de A)
2. Signup → pago por campaña, últimos 90 días
3. LTV o ticket promedio (para saber si un CPA de $88 es caro o regalado)
4. Search terms report de B
5. Ventana de conversión y modelo de atribución (con signups de blog, un modelo last-click subestima a B sistemáticamente)