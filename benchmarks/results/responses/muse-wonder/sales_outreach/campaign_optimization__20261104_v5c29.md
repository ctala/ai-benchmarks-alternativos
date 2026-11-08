# Muse Wonder — sales_outreach/campaign_optimization

- model_id: `meta/muse-wonder`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 41.113s | tokens_per_second: 93.6
- input_tokens: 261 | output_tokens: 3849

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

Con tus datos, la campaña que más clicks trae no es la más rentable. La clave está en cruzar CPC con Conversion Rate.

### 1. Métricas por campaña

Formulas: `CTR = Clicks/Impresiones` | `CPC = Costo/Clicks` | `CVR = Signups/Clicks` | `CPA = Costo/Signups`

| Campaña | CTR | CPC | Conversion Rate | CPA | Signups |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A - Landing principal** | 3.0% (1.500/50.000) | **$1.40** | 3.0% | **$46.67** | 45 |
| **B - Blog content** | 4.0% (4.800/120.000) | **$0.38** | 0.5% | **$75.00** | 24 |
| **C - Competidor** | 6.0% (900/15.000) | **$3.56** | 4.0% | **$88.89** | 36 |

**Promedio total:** Gastaste $7.100 para 105 signups = **CPA blended de $67.62**

### 2. ¿Cuál escalar y cuál pausar?

**ESCALAR: Campaña A**
Es la ganadora indiscutible para adquisición directa. Tiene el CPA más bajo ($46.67), es decir, un signup de C te cuesta casi el doble (1.9x). Sus keywords "software gestion inventario" tienen intención transaccional clara: el usuario ya busca una solución para comprar.

**PAUSAR: Campaña B (como campaña de Signups)**
Es la trampa clásica. Tiene el CPC más barato ($0.38) y buen CTR (4%), pero su Conversion Rate es pésimo: 0.5%, 6 veces peor que A y 8 veces peor que C.

¿Por qué? Intención informacional ("como gestionar...") vs. transaccional. Llegan a un blog a leer, no a registrarse. Gastaste $1.800 para solo 24 signups.

No significa que el contenido sea inútil, pero no debe medirse ni optimizarse por Signups directos. Pausala en frío.

**MANTENER CON TECHO, NO ESCALAR TODAVÍA: Campaña C**
Es la más interesante: CTR 6% y CVR 4%, los mejores de la cuenta. Quien busca "alternativa a [competidor]" está insatisfecho y listo para cambiar.

El problema es el costo: CPC de $3.56 (estás pujando en la marca de otro). Eso dispara el CPA a $88.89. Hay demanda de alta calidad, pero cara. Hay que optimizarla antes de meterle más dinero.

> **Advertencia:** Esta decisión es solo por CPA. Antes de pausar definitivamente, revisa el LTV por campaña. Si los clientes que vienen de C pagan más o churnean menos que los de A, C podría justificarse.

### 3. Redistribución del presupuesto de $5.000

Hoy gastas $7.100. Si mantuvieras la misma proporción con $5.000, obtendrías ~74 signups.

Con esta redistribución:

| Campaña | Presupuesto | % | Signups proyectados* |
| :--- | :--- | :--- | :--- |
| **A - Landing principal** | **$3.750** | 75% | ~80 |
| **C - Competidor** | **$1.250** | 25% | ~14 |
| **B - Blog** | **$0** | 0% | 0 |
| **TOTAL** | **$5.000** | 100% | **~94** |

*\*Proyección lineal con CPA actual.*

Son **~20 signups más (+27%) con el mismo presupuesto.**

No pongas el 100% en A porque sus keywords tienen un volumen limitado (50k impresiones). Al escalar, vigila semanalmente que el CPC no se dispare por saturación. Sube el presupuesto de a 20% por semana, no de golpe.

El presupuesto de los tests A/B sale de dentro de A y C, no es extra.

### 4. A/B Tests prioritarios para el próximo mes

Con tu volumen (24-45 signups/mes por campaña) no puedes correr 5 tests a la vez, no tendrás significancia estadística. Prioriza estos 2, en este orden:

**Test 1 - Campaña C: Landing dedicada vs. Landing genérica [Mayor impacto]**
*   **Hipótesis:** Una landing específica de comparación reducirá el CPA de $88.89.
*   **Control:** Tu landing principal actual.
*   **Variante:** Landing "[Tu Producto] vs [Competidor]" con tabla comparativa, foco en migración en 1 click y oferta de onboarding gratuito.
*   **Meta:** Subir el CVR de 4.0% a 5.5%. Solo con eso, el CPA bajaría a ~$64 sin tocar el CPC.

**Test 2 - Campaña A: Message Match en la Landing**
*   **Hipótesis:** Alinear el titular con la keyword de PyMEs subirá el CVR de 3%.
*   **Control:** Titular genérico actual.
*   **Variante:** Titular: "Software de gestión de inventario para PyMEs" + prueba social de PyMEs + CTA "Prueba gratis 14 días" (vs. "Crear cuenta").
*   **Meta:** CVR 3.0% -> 3.8%. CPA bajaría de $46.67 a ~$36.8.

**Test 3 - Rescate de B (solo si quieres mantener contenido): Lead Magnet**
No mandes tráfico frío del blog a un signup. Testea en una campaña separada de remarketing a los 4.800 visitantes de B:
*   **Variante:** Ofrece una "Plantilla gratuita de control de inventario" a cambio del email.
*   Mídelo por **Costo por Lead (email)**, no por Signup. Luego nutre esos emails.

Regla para los tests: 50/50 de tráfico, una sola variable por test, y no decidas un ganador con menos de 30 conversiones por variante o menos de 2 semanas.

**Resumen:** Escala A, pausa B en frío, y arregla la landing de C. Ahí está tu crecimiento eficiente el próximo mes.