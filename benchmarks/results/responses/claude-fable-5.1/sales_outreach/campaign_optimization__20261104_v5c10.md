# Claude Fable 5.1 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.86 | quality: 10.0
- latency_total: 51.592s | tokens_per_second: 68.9
- input_tokens: 395 | output_tokens: 3554

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

| Métrica | A (Landing) | B (Blog) | C (Competidor) |
|---|---|---|---|
| CTR | 3.0% | 4.0% | **6.0%** |
| CPC | $1.40 | **$0.38** | $3.56 |
| Conv. rate (click→signup) | 3.0% | 0.5% | **4.0%** |
| CPA | **$46.67** | $75.00 | $88.89 |
| Signups | 45 | 24 | 36 |

**Totales:** $7,100 gastados → 105 signups → CPA blended **$67.62**.

⚠️ Primer dato importante: gastaste $7,100 con un presupuesto de $5,000. Estás un 42% por encima. Cualquier redistribución implica recortar, no solo mover dinero.

---

## 2. Qué escalar y qué pausar

**Escalar: Campaña A.** Es la más eficiente por lejos: CPA de $46.67, un 30% mejor que el blended y casi la mitad del de C. Tiene buen balance entre intención (keywords transaccionales) y costo de click. Antes de escalar, revisa en Google Ads el *Search Impression Share lost to budget*: si está por encima del 20-30%, hay demanda que no estás capturando y escalar debería mantener el CPA razonablemente estable.

**Pausar (o reducir drásticamente): Campaña B.** Aunque tiene el CPC más barato y el mayor volumen, su conversion rate de 0.5% revela el problema de fondo: las keywords son informacionales ("cómo gestionar inventario"). La gente que busca eso quiere leer, no registrarse. Un CPA de $75 no es catastrófico, pero es 60% peor que A, y su problema es estructural (intención equivocada para un objetivo de signup), no de optimización.

**Campaña C: no pausar, sí optimizar.** Tiene el peor CPA ($88.89) pero el mejor conversion rate (4%) y CTR (6%). El problema no es la landing ni la intención —es el CPC de $3.56. Eso se puede atacar: separar "alternativa a [competidor]" de "[competidor] vs" (probablemente convierten muy distinto), bajar pujas, revisar términos de búsqueda y agregar negativas. Además, un usuario que busca alternativas a un competidor suele tener mayor probabilidad de pagar y mayor LTV que uno que lee un blog. Si puedes conectar signups con conversión a pago, es muy posible que C sea más rentable de lo que sugiere el CPA.

**Dato que te falta:** signup → cliente pagando por campaña. Sin eso, estás optimizando por un proxy. Si el 15% de signups de C pagan y solo el 3% de B lo hacen, la foto cambia completamente.

---

## 3. Redistribución de $5,000

| Campaña | Antes | Propuesto | Cambio | Signups est. |
|---|---|---|---|---|
| A | $2,100 | **$2,800** | +33% | ~57 (CPA sube a ~$49 al escalar) |
| C | $3,200 | **$1,700** | −47% | ~21 (CPA baja a ~$80 con optimización) |
| B | $1,800 | **$0** (search) | pausar | — |
| Remarketing (nuevo) | $0 | **$500** | nuevo | ~8-10 |
| **Total** | $7,100 | **$5,000** | | **~86-88** |

**Resultado esperado:** ~87 signups por $5,000 → CPA blended ~$57, vs. $67.62 actual. Menos signups absolutos (porque hay $2,100 menos), pero un 15% más eficientes.

**Por qué remarketing:** B te generó 4,800 visitantes en un mes que ya conocen el problema. En vez de seguir pagando por tráfico frío que no convierte, usa ese pool (y el de A y C que no convirtió) para impactar con anuncios de display/search remarketing. Suele dar CPAs mejores que cualquier campaña de prospección.

**Regla de salida para C:** si después de un mes de optimización el CPA no baja de ~$70, reduce otros $700 y pásalos a A.

---

## 4. A/B tests para el próximo mes

**Campaña A (prioridad alta, es donde más volumen hay):**
- Headline de landing: enfocado en feature ("Software de gestión de inventario") vs. enfocado en resultado ("Deja de perder ventas por quiebres de stock")
- CTA: "Prueba gratis" vs. "Agenda demo" — cambia el tipo de lead que atraes
- Formulario de signup: 3 campos vs. 5+ campos

**Campaña C:**
- Landing genérica vs. landing comparativa dedicada ("[Tu producto] vs [Competidor]" con tabla de features y precios). Esto suele subir mucho el CVR en keywords de competidor
- Ad copy: diferenciador de precio vs. diferenciador de feature/soporte
- Separar en dos ad groups: "alternativa a" vs. "vs" y comparar CPA de cada uno

**Estructura/pujas:**
- Estrategia de puja en A: Manual CPC vs. Maximizar conversiones (con 45+ conversiones/mes ya tienes datos suficientes para que el algoritmo funcione)
- Match types: revisar si phrase vs. broad con audiencia de señal cambia el CPC en C

**Si decides mantener algo de B:**
- Cambiar el objetivo: en vez de pedir signup, ofrecer lead magnet (plantilla de inventario, checklist) y nutrir por email. Mide costo por lead, no por signup

Una regla práctica: no corras más de 2-3 tests simultáneos, y asegúrate de que cada variante tenga al menos ~30 conversiones antes de declarar un ganador. Con tu volumen, los tests en A pueden cerrarse en 3-4 semanas; en C probablemente necesitarás 6-8.