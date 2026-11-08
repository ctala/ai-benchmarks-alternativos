# Mercury 2.5 — sales_outreach/campaign_optimization

- model_id: `inception/mercury-2.5`
- success: True  | final: 6.75 | quality: 6.0
- latency_total: 2.882s | tokens_per_second: 331.8
- input_tokens: 297 | output_tokens: 956

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

Aquí tienes el análisis detallado y las recomendaciones estratégicas para tu campaña de Google Ads.

### 1. Métricas por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** | 3.0% | 4.0% | 6.0% |
| **CPC** | $1.40 | $0.38 | $3.56 |
| **CPA** | $46.67 | $75.00 | $88.89 |
| **Tasa de Conv. (CR)** | 3.0% | 0.5% | 4.0% |

*(Cálculos: CTR = Clicks/Impresiones; CPC = Costo/Clicks; CPA = Costo/Signups; CR = Signups/Clicks)*

### 2. ¿Escalar o Pausar?

**Escalar: Campaña C (Competidor)**
*   **Justificación:** Aunque tiene el CPA más alto ($88.89), presenta la **tasa de conversión más alta (4%)** y el CTR más alto (6%). Esto indica que el tráfico es extremadamente cualificado y la intención de compra es alta (están buscando activamente cambiarse de un rival). En etapas tempranas, este tráfico es más valioso por su calidad que por su costo inmediato.

**Pausar: Campaña B (Blog Content)**
*   **Justificación:** Es la peor campaña en eficiencia. El CPA es el más alto ($75) y la tasa de conversión es la más baja (0.5%). Obtienes mucho tráfico barato (CPC de $0.38), pero no convierte. La página del blog probablemente no está alineada con el objetivo de "sign up" directo.

### 3. Redistribución del Presupuesto ($5,000)

El objetivo es maximizar el volumen de signups optimizando el CPA y aumentando la calidad del tráfico.

**Asignación sugerida:**
*   **Campaña C (Competidor):** $3,500 (70%)
*   **Campaña A (Landing):** $1,500 (30%)
*   **Campaña B (Blog):** $0 (0%)

**Proyección de Resultados (Mensual):**
*   **Campaña C:** Al duplicar el presupuesto, esperamos mantener el CPA y el volumen de conversiones.
    *   Signups estimados: ~40
*   **Campaña A:** Al mantener el presupuesto, esperamos un desempeño similar.
    *   Signups estimados: ~30
*   **Total Estimado:** **~70 Signups** (Comparado con los 105 actuales).

*Nota:* Aunque el volumen absoluto disminuye, la **calidad y rentabilidad general** mejoran al eliminar el tráfico de bajo rendimiento de la Campaña B y redirigir esos fondos a la Campaña C, que cierra ventas más rápido.

### 4. A/B Tests para el Próximo Mes

Para mejorar la eficiencia y la tasa de conversión:

1.  **Campaña C (Competidor): Test de Extensión de Anuncio.**
    *   *Hipótesis:* Agregar extensiones de "Características clave" o "Casos de uso" podría reducir el CPA sin sacrificar el CTR.
    *   *Medición:* CPA y CTR.

2.  **Campaña A (Landing): Test de Copy del Títlo.**
    *   *Hipótesis:* Cambiar un enfoque funcional a uno orientado al ahorro de tiempo o dinero (ej. "Automatiza tu inventario en 5 min" vs. "Software de gestión").
    *   *Medición:* Tasa de Conversión (CR).

3.  **Campaña B (Reactivación): Test de Llamada a la Acción (CTA).**
    *   *Hipótesis:* Si decides reactivar la campaña del blog, prueba cambiar el objetivo de "Sign up" a "Lead Magnet" (ej. descarga de una guía) para mejorar el CTR inicial.
    *   *Medición:* CTR y CPA por Lead.