# Seed 2.0 Code — sales_outreach/campaign_optimization

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 173.856s | tokens_per_second: 57.4
- input_tokens: 333 | output_tokens: 9982

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

### Respuesta estructurada según tus preguntas, con cálculos verificados y justificación numérica:

---

## 1. Cálculo de métricas por campaña
Primero, definimos las fórmulas estándar de Google Ads (usamos **Signups** como métrica de conversión, según tus datos):
- **CTR (Click-Through Rate)**: `(Clicks / Impresiones) * 100` → % de impresiones que generan clicks
- **CPC (Costo Por Click)**: `Costo Total / Clicks` → costo promedio de cada click
- **CPA (Costo Por Adquisición)**: `Costo Total / Signups` → costo promedio de cada registro
- **Tasa de Conversión (CR)**: `(Signups / Clicks) * 100` → % de clicks que generan registros

### Resultados por campaña (tabla comparativa):
| Métrica                | Campaña A (Landing Principal) | Campaña B (Blog Content) | Campaña C (Competidor) |
|------------------------|---------------------------------|---------------------------|-------------------------|
| CTR                    | 3%                              | 4%                        | 6%                      |
| CPC                    | $1.40                           | $0.38                     | $3.56                   |
| CPA                    | $46.67                          | $75.00                    | $88.89                  |
| Tasa de Conversión (CR)| 3%                              | 0.5%                      | 4%                      |

*Verificación de cálculos (ejemplo Campaña A):*
- CTR: `(1.500 / 50.000) * 100 = 3%`
- CPC: `$2.100 / 1.500 = $1.40`
- CPA: `$2.100 / 45 = $46.67`
- CR: `(45 / 1.500) * 100 = 3%`

---

## 2. ¿Cuál campaña escalar y cuál pausar?
Nos basamos en el objetivo de **maximizar signups con el presupuesto disponible**, por lo que la métrica clave es el **CPA (menor = más eficiente)**.

### ✅ Campaña a escalar: Campaña A (Landing Principal)
Justificación numérica:
1. **CPA más bajo del mercado ($46.67)**: Es un 38% más barato que la Campaña B y un 48% más barato que la Campaña C. Por cada $100 invertidos, A genera ~2.14 signups, contra ~1.33 de B y ~1.12 de C.
2. **Intención transaccional sólida**: Sus keywords (`"software gestion inventario"`, `"inventario pymes"`) son de usuarios que buscan activamente un producto como el tuyo. Su CTR (3%) y CR (3%) confirman que anuncios y landing page funcionan.
3. **Espacio para crecer**: Tuvo 50.000 impresiones (3x más que la Campaña C de competidores), lo que indica volumen de búsqueda sin explotar.

### ❌ Campaña a pausar: Campaña C (Competidor)
Justificación numérica:
1. **CPA más alto del mercado ($88.89)**: Casi el doble que la Campaña A. Por cada signup que genera, podrías generar casi 2 signups con la misma inversión en A.
2. **CPC excesivo ($3.56)**: Aunque tiene el CR más alto (4%) y CTR más alto (6%) (porque usuarios de keywords de competidor son de alta intención), su CPC es 2.5x más caro que A y 9x más caro que B, anulando su ventaja de conversión.
3. **Volumen limitado**: Solo tuvo 15.000 impresiones, lo que indica un techo de crecimiento muy bajo para estas keywords específicas de competidor.

*Nota sobre la Campaña B:* Aunque su CPA ($75) es más alto que A, es una campaña de **top of funnel (conciencia de marca)** que atrae usuarios en etapa de investigación. Su CPC muy bajo ($0.38) la hace útil para nutrir leads que se convertirán en signups más adelante, por lo que no se recomienda pausarla, sí reducir su presupuesto.

---

## 3. Redistribución del presupuesto de $5.000/mes
La regla es: **maximizar signups a corto plazo sin perder nutrición de leads a largo plazo**.

### Distribución óptima (suma $5.000):
| Campaña                | Presupuesto | % del total | Justificación                                                                 |
|------------------------|-------------|-------------|--------------------------------------------------------------------------------|
| Campaña A (Landing)    | $3.750      | 75%         | Maximiza signups a corto plazo: generará ~80 signups (`$3.750 / $46.67 ≈ 80`). Sus keywords generales tienen volumen suficiente para gastar este monto sin aumentar el CPA. |
| Campaña B (Blog)       | $1.250      | 25%         | Reserva para nutrición de leads: generará ~17 signups (`$1.250 / $75 ≈ 17`), además de conciencia de marca para usuarios en etapa de investigación. |
| Campaña C (Competidor) | $0          | 0%          | Pausada por su baja eficiencia: invertir $1.000 en C generaría ~11 signups, contra ~21 en A. |

*Total de signups estimados: ~97, vs ~70 si mantuvieras la proporción de gasto anterior.*

---

## 4. A/B Tests sugeridos para el próximo mes
Los tests se enfocan en solucionar los puntos débiles de cada campaña:

### Para Campaña A (mejorar aún más su eficiencia):
1. **Test de copy de anuncios**: Compara:
   - Control: Anuncio actual centrado en características
   - Variante: Anuncio centrado en beneficios y prueba social: *"Gestiona tu inventario en 5 minutos | Usado por 10.000 pymes | Prueba gratis 14 días"*
   - Métrica a medir: CTR y CR
2. **Test de landing page**: Compara el landing actual con una versión con formulario más corto (solo nombre y email, sin teléfono) y CTA fijo en la parte superior.
   - Métrica a medir: CR

### Para Campaña B (mejorar su CR muy baja de 0.5%):
1. **Test de oferta de conversión**: Compara:
   - Control: Ofrecer signup para el software directamente
   - Variante: Ofrecer un lead magnet alineado con el contenido: *"Descarga tu plantilla gratuita de gestión de inventario para restaurantes"* a cambio de signup
   - Métrica a medir: CR
2. **Test de ubicación de CTA**: Compara CTA solo al final del artículo vs un popup de salida o un CTA embebido en la mitad del contenido.
   - Métrica a medir: CR

### Para Campaña C (validar si se puede recuperar antes de pausar):
1. **Test de landing page de comparación**: Compara el landing actual con una versión específica para usuarios de competidores: *"[Tu Software] vs [Competidor]: 5 razones para cambiar | Descuento del 20% para usuarios de [Competidor]"*
   - Resultado esperado: Si el CR sube de 4% a 6%, el CPA baja a ~$59, volviéndose rentable.
2. **Test de keywords negativas**: Agrega términos como `"descargar [competidor]"`, `"precios [competidor]"` para evitar clicks de usuarios que no buscan cambiar de software.
   - Métrica a medir: CPC y CPA

### Test transversal (clave para medir el impacto de la Campaña B):
Cambia el modelo de atribución de **Último Clic (por defecto)** a **Atribución Basada en Datos** para medir si la Campaña B (top of funnel) contribuye a las conversiones de la Campaña A. Esto puede justificar aumentar o reducir su presupuesto a largo plazo.