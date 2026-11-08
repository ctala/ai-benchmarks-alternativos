# DeepSeek V4 Flash 0731 — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 7.92 | quality: 8.0
- latency_total: 11.388s | tokens_per_second: 141.5
- input_tokens: 273 | output_tokens: 1611

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

Aquí tienes el análisis completo y estratégico basado en tus datos:

---

### 1. Cálculo de métricas clave (CTR, CPC, CPA, CVR)

| Campaña | CTR (Clicks/Impresiones) | CPC (Costo/Clicks) | CVR (Signups/Clicks) | CPA (Costo/Signups) |
| :--- | :--- | :--- | :--- | :--- |
| **A (Landing)** | 3.0% (1,500/50,000) | $1.40 ($2,100/1,500) | 3.0% (45/1,500) | **$46.67** ($2,100/45) |
| **B (Blog)** | 4.0% (4,800/120,000) | $0.38 ($1,800/4,800) | 0.5% (24/4,800) | **$75.00** ($1,800/24) |
| **C (Competidor)** | 6.0% (900/15,000) | $3.56 ($3,200/900) | 4.0% (36/900) | **$88.89** ($3,200/36) |

---

### 2. ¿Cuál escalar y cuál pausar? (Justificación numérica)

**👉 Escalar: Campaña A (Landing principal)**
- **Mejor CPA ($46.67)**: Es la más rentable. Cuesta menos de la mitad que la campaña C y un 38% menos que la B.
- **Alta intención de compra**: Las keywords ("software gestion inventario") indican que el usuario busca una solución activamente.
- **CVR sólida (3%)**: Demuestra que el mensaje y la landing page convierten bien a un costo razonable.
- **Potencial de escala**: Con un CPC bajo ($1.40) y un CTR decente (3%), hay margen para subir pujas y presupuesto sin disparar el CPA.

**⏸️ Pausar o reestructurar: Campaña B (Blog content)**
- **Peor CVR (0.5%)**: Es 6 veces inferior a la campaña A. El tráfico es "frío" (informativo, no transaccional).
- **CPA alto ($75)**: A pesar de ser la más barata en CPC ($0.38), el costo por resultado es caro porque casi nadie se registra.
- **Volumen engañoso**: Genera muchos clics baratos, pero no aporta a tu objetivo de conversión (signups). **Recomendación**: *No pausar del todo*, sino cambiar el objetivo a *remarketing* (ver punto 4) o reducir drásticamente la inversión.

**⚠️ Reevaluar: Campaña C (Competidor)**
- **CPA más alto ($88.89)**: Es la más cara en adquisición.
- **CPC elevado ($3.56)**: Las keywords de competidor son caras y el tráfico es "caliente" pero con mucha competencia.
- **CVR alta (4%)**: Es la mejor convirtiendo, pero el costo inicial es tan alto que no compensa. **Recomendación**: *Reducir pujas* para bajar el CPC, o *pausar* si el presupuesto es limitado y la campaña A puede absorber más tráfico.

---

### 3. Redistribución del presupuesto ($5,000)

**Estrategia: Maximizar el CPA más bajo (A) y usar B/C de forma inteligente.**

| Campaña | Presupuesto Actual | **Nuevo Presupuesto** | Cambio | Razonamiento |
| :--- | :--- | :--- | :--- | :--- |
| **A (Landing)** | $2,100 | **$3,500** | +$1,400 | **Escalar agresivamente**. Es tu máquina de hacer dinero. Intenta capturar más volumen de las mismas keywords o añadir variantes (ej. "software inventario gratis"). |
| **B (Blog)** | $1,800 | **$500** | -$1,300 | **Reducir a mínimo**. No la pauses del todo, pero úsala solo para *remarketing* (ej. mostrar anuncios a quien leyó el blog pero no convirtió). |
| **C (Competidor)** | $3,200 | **$1,000** | -$2,200 | **Reducir y optimizar**. Baja las pujas un 20-30% para bajar el CPC. Si el CPA sigue >$70, pausa y traslada ese $1,000 a A. |

**Total: $5,000**

---

### 4. A/B Tests sugeridos para el próximo mes

**Prioridad: Optimizar la campaña A (la que escala).**

1.  **Test de Landing Page (Campaña A):**
    - **Hipótesis**: Reducir el número de campos en el formulario de registro (de 5 a 3) aumentará la CVR.
    - **Test**: Crea una variante de la landing page con un formulario más corto y un botón de CTA más visible ("Prueba gratis 14 días" vs "Comenzar ahora").
    - **Métrica**: Comparar la CVR (Signups/Clicks) entre la versión original y la variante.

2.  **Test de Pujas y Palabras Clave (Campaña C):**
    - **Hipótesis**: Bajar la puja un 25% reducirá el CPC lo suficiente como para que el CPA baje por debajo de $60.
    - **Test**: Crea un experimento dentro de la campaña C con una puja máxima más baja (ej. $2.50 vs $3.56 actual).
    - **Métrica**: Monitorizar el CPA y el volumen de clics. Si el CPA mejora, mantén la puja baja.

3.  **Test de Remarketing (Campaña B):**
    - **Hipótesis**: Las personas que leyeron el blog son más propensas a convertirse si ven un anuncio de "cómo empezar" en lugar del anuncio genérico.
    - **Test**: Crea una lista de remarketing para usuarios que visitaron el blog pero no se registraron. Muestra un anuncio específico con un descuento o un caso de éxito.
    - **Métrica**: Comparar el CPA de este grupo contra el CPA general de la campaña B.

---

### Resumen ejecutivo
- **Mata la campaña B como tráfico frío** y conviértela en remarketing.
- **Inyecta el dinero en la Campaña A** (tu ganador claro).
- **Controla la Campaña C**: Si no baja su CPA a <$70, pausa y traslada el dinero a A.
- **El test más importante** es el de la landing page de A, ya que un 1% de mejora en CVR se traduce en ahorro directo.