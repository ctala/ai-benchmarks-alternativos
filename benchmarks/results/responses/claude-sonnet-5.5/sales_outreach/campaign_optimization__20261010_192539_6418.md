# Claude Sonnet 5.5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 33.413s | tokens_per_second: 117.9
- input_tokens: 395 | output_tokens: 3941

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

## ⚠️ Primero: los números no cuadran con tu presupuesto
La suma de costos es **$7,100**, no $5,000 (un 42% por encima). Revisa si el presupuesto es otro, si hubo gasto extra o si el dato del costo está mal. Mi análisis usa los datos tal como los diste.

## 1. Métricas por campaña

| Métrica | **A** (Landing) | **B** (Blog) | **C** (Competidor) | **Total** |
|---|---|---|---|---|
| CTR | 3.0% | 4.0% | 6.0% | 3.9% |
| CPC | $1.40 | $0.38 | $3.56 | $0.99 |
| Conv. rate (signup/click) | 3.0% | 0.5% | 4.0% | 1.46% |
| **CPA** | **$46.67** | $75.00 | $88.89 | $67.62 |
| % del gasto | 30% | 25% | 45% | |
| % de signups | 43% | 23% | 34% | |

**Lectura:**
- **A** es la más eficiente: 30% del gasto trae 43% de los signups.
- **B** tiene buen CTR y CPC bajo, pero casi nadie convierte (0.5%). Es tráfico informativo, no de compra.
- **C** tiene el mejor CTR y conversion rate (la intención es alta), pero el CPC de $3.56 la hace la más cara por signup. Se lleva el 45% del gasto.

## 2. Qué escalar y qué pausar

**Escalar: Campaña A.** Su CPA es 38% menor que el promedio ($46.67 vs $67.62). Escalar no será lineal: al subir presupuesto el CPC suele subir, así que incrementa de forma gradual (+20-30% por semana).

**Pausar o recortar: depende del valor de un signup.** Solo con el CPA, C es la peor ($88.89). Pero no la pausaría sin ver un dato clave:

> **C solo vale la pena si sus signups pagan al menos 1.9x más que los de A** ($88.89 / $46.67). Para B, el umbral es 1.6x.

Mi recomendación:
- **B: pausar en su forma actual.** El problema es estructural (0.5% de conversión), no de ajustes. Reconviértela a retargeting o a lead magnet (ver abajo).
- **C: recortar y optimizar, no pausar.** Tiene 4% de conversion rate, así que el problema es el CPC. Deja solo la keyword que mejor convierta en exact/phrase, crea una landing de comparación y revisa el Quality Score. Si en 30 días el CPA no baja de ~$70, páusala.

Antes de decidir, cruza los signups con **activación o pago por campaña**. Eso puede cambiar todo el ranking.

## 3. Redistribución de $5,000

| Campaña | Actual | Propuesto | Cambio | Signups est.* |
|---|---|---|---|---|
| A | $2,100 | **$2,900** | +38% | ~55 (CPA ~$52) |
| B | $1,800 | **$600** | -67% | ~8 |
| C | $3,200 | **$1,500** | -53% | ~19 (CPA ~$80) |
| **Total** | $7,100 | **$5,000** | | **~82** |

*Estimación conservadora: asumo que A empeora ~10% su CPA al escalar y que C mejora algo al optimizar.

**Comparación justa:** si recortaras todo proporcionalmente a $5,000, obtendrías ~74 signups. Con esta redistribución, ~82 (**~11% más**), con CPA blended de ~$61 vs $67.6.

- **B ($600):** solo retargeting y las 1-2 keywords con mejor conversión, más negativas ("gratis", "plantilla excel", "pdf").
- **Reserva:** si quieres, deja $200-300 de A como colchón y libéralo solo si el CPA se mantiene bajo $55.

## 4. A/B tests para el próximo mes

**Aviso sobre volumen:** con ~3% de conversión, detectar una mejora del 50% (3% → 4.5%) requiere ~2,500 clics por variante. A tiene 1,500 clics al mes en total, así que prueba cambios grandes (no matices de color) y deja correr los tests 3-4 semanas. Si puedes, mide también micro-conversiones (clic en CTA, inicio del formulario).

**Campaña A (prioridad alta)**
1. **Headline de la landing:** beneficio ("Controla tu inventario sin hojas de cálculo") vs. dolor ("Deja de perder dinero por stock mal controlado").
2. **Formulario:** solo email vs. email + nombre + empresa.
3. **Anuncios (RSA):** enfoque en prueba gratis/sin tarjeta vs. enfoque en ahorro de tiempo.

**Campaña C**
4. **Landing:** página genérica vs. página de comparación dedicada ("Tú vs. [competidor]" con tabla de funciones y precios).
5. **Oferta:** "Migración gratis de tus datos" vs. "Prueba gratis".
6. **Estrategia de puja:** Target CPA vs. Maximizar conversiones, para frenar el CPC alto.

**Campaña B (rediseño)**
7. **CTA en el blog:** descarga de lead magnet (checklist o plantilla de inventario) vs. signup directo. Captura el lead y nutre por email.
8. **Retargeting:** visitantes del blog que ven un anuncio del producto vs. sin retargeting.

**Reglas:** una variable por test, 50/50 de tráfico, y define de antemano la métrica ganadora (CPA y calidad del signup, no solo volumen).

Si me compartes el valor de un cliente (LTV) y el % de signups que se vuelven clientes de pago, puedo afinar la redistribución con CPA objetivo real.