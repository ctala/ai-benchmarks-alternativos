# Mercury 2.5 — sales_outreach/campaign_optimization

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.44 | quality: 10.0
- latency_total: 3.349s | tokens_per_second: 745.7
- input_tokens: 288 | output_tokens: 2497

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



Aquí tienes el análisis de tus campañas basado en los datos proporcionados:

### 1. Cálculo de Métricas

| Métrica | Campaña A | Campaña B | Campaña C |
| :--- | :--- | :--- | :--- |
| **CTR** | 3.0% | 4.0% | 6.0% |
| **CPC** | $1.40 | $0.38 | $3.56 |
| **CPA** | $46.67 | $75.00 | $88.89 |
| **Tasa de Conversión** | 3.0% | 0.5% | 4.0% |

### 2. Escalar o Pausar

*   **Escalar: Campaña A.**
    *   **Justificación:** Tiene el **CPA más bajo** ($46.67), lo que la hace la más eficiente para adquirir usuarios. Aunque su volumen es menor que B, mantiene una tasa de conversión saludable (3%) y genera casi el doble de signups que C con la mitad de costo por conversión.
*   **Pausar: Campaña B.**
    *   **Justificación:** A pesar de tener clics baratos, su tasa de conversión es mínima (0.5%), resultando en un **CPA alto** ($75.00). El tráfico atraído al blog no se convierte bien en signups directamente, desperdiciando presupuesto.

*Nota sobre Campaña C:* Tiene altoCP (4%) pero es muy costosa ($88.89 CPA). Úsala solo si el valor de vida del cliente (LTV) justifica pagar más por un usuario de alta intención.

### 3. Redistribución de Presupuesto ($5,000/mes)

Actualmente gastas $7,100, por encima de tu límite. Aquí una propuesta para optimizar el retorno:

*   **Campaña A:** $3,500 (Prioridad principal para volumen eficiente).
*   **Campaña C:** $1,500 (Mantener para capturar intención alta, pero limitada).
*   **Campaña B:** $0 (Redirigir presupuesto a A).

### 4. Sugerencias de A/B Tests

1.  **Landing Page (Campaña A):** Probar dos versiones del titular principal para ver si mejoras la tasa de conversión actual del 3%.
2.  **Copy de Anuncio (Campaña C):** Comparar mensajes que enfatizan "ahorro de dinero" versus "facilidad de uso" para reducir el CPC.
3.  **Llamada a la Acción (CTA):** Testear "Regístrate gratis" contra "Prueba demo" en la landing principal para ver cuál genera más signups cualificados.