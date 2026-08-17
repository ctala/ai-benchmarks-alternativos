# GLM 5 (NIM) — sales_outreach/campaign_optimization

- model_id: `z-ai/glm5`
- success: True  | final: 6.98 | quality: 9.36
- latency_total: 242.635s | tokens_per_second: 6.7
- input_tokens: 270 | output_tokens: 1634
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes un análisis detallado de tus resultados y un plan de acción para optimizar tu presupuesto.

### 1. Cálculo de Métricas (CTR, CPC, Tasa de Conversión y CPA)

*Nota: Tasa de conversión (Conv. Rate) = (Signups / Clicks) * 100*

**Campaña A (Landing principal)**
*   **CTR:** 3.00% *(1,500 / 50,000)*
*   **CPC:** $1.40 *(2,100 / 1,500)*
*   **Tasa de Conversión:** 3.00% *(45 / 1,500)*
*   **CPA (Costo por Adquisición/Signup):** $46.67 *(2,100 / 45)*

**Campaña B (Blog content)**
*   **CTR:** 4.00% *(4,800 / 120,000)*
*   **CPC:** $0.38 *(1,800 / 4,800)*
*   **Tasa de Conversión:** 0.50% *(24 / 4,800)*
*   **CPA:** $75.00 *(1,800 / 24)*

**Campaña C (Competidor)**
*   **CTR:** 6.00% *(900 / 15,000)*
*   **CPC:** $3.56 *(3,200 / 900)*
*   **Tasa de Conversión:** 4.00% *(36 / 900)*
*   **CPA:** $88.89 *(3,200 / 36)*

---

### 2. ¿Cuál campaña escalar y cuál pausar?

*   **Escalar: Campaña A.** Es tu campaña "estrella". Tiene el CPA más bajo ($46.67) y la mejor relación entre volumen de conversiones (45) y costo. Aunque su CTR es menor que la B, la calidad del tráfico es muy superior (3% de conversión vs 0.5% de la B). Es tu motor de crecimiento rentable.
*   **Pausar (o reestructurar fuertemente): Campaña B.** Aunque es la campaña más barata por clic ($0.38) y genera mucho tráfico, su CPA es alto ($75) y su tasa de conversión es bajísima (0.5%). El problema aquí es de **intención de búsqueda**: las personas que buscan "cómo gestionar inventario" quieren información, no necesariamente comprar un software hoy. Pagar por ese tráfico en Ads es caro para los resultados que da.
*   **Mantener pero optimizar (No pausar aún): Campaña C.** Tiene el CPA más alto ($88.89), pero tiene la tasa de conversión más alta (4%) y el mejor CTR (6%). El problema es el CPC altísimo ($3.56). Al ser términos de competencia, la subasta es cara, pero quien busca "alternativa a [competidor]" tiene altísima intención de compra. No debes pausarla, pero debes trabajar en bajar su CPC.

---

### 3. Redistribución del presupuesto ($5,000/mes)

El gasto actual total es de $7,100, por lo que recortar a $5,000 requiere ser agresivos con lo que no funciona.

*   **Campaña A: $3,000 (60% del presupuesto)**
    *   *Justificación:* A CPA de $46.67, este presupuesto debería darte unos **64 signups**. Es tu apuesta segura y rentable. Al escalar, el CPA podría subir ligeramente por la ley de rendimientos decrecientes, pero seguirá siendo tu fuente principal.
*   **Campaña C: $1,500 (30% del presupuesto)**
    *   *Justificación:* Reducimos su presupuesto actual ($3,200) para controlarlo, pero le damos suficiente margen para seguir captando usuarios de alta intención. A un CPA de $88.89, esperarías unos **16-17 signups**. El objetivo aquí será bajar el CPC para que este presupuesto rinda más.
*   **Campaña B: $500 (10% del presupuesto)**
    *   *Justificación:* Reducción drástica. En lugar de pausarla de golpe, la dejamos con el mínimo necesario para recoger datos y probar correcciones. A un CPA de $75, esperarías unos **6 signups**.

*Total estimado con esta distribución:* ~87 signups por $5,000 (CPA promedio mezclado: ~$57.47). Antes estabas pagando un promedio de ~$63.64 por signup. Mejoras tu eficiencia global mientras ahorras $2,100.

---

### 4. A/B Tests sugeridos para el próximo mes

**Para la Campaña A (Escalar):**
*   **Test de Landing Page (Formulario vs. Demo):** Probar una versión de la landing con un formulario de contacto más corto (solo Email + Nombre) vs uno largo (Email + Nombre + Empresa + Empleados). Quiero ver si al reducir la fricción sube el volumen de signups, aunque baje un poco la calidad.
*   **Test de Mensaje en Anuncios:** Probar añadir una promoción temporal (ej. "15% de descuento en el primer mes" o "Prueba gratis de 30 días") en los títulos para ver si el CTR sube del 3% y acelera la captación.

**Para la Campaña B (Corregir la desconexión):**
*   **Test de Flujo (Lead Magnet):** El problema es que el blog no convierte en signups de software. Cambia el objetivo del tráfico: en lugar de mandarlos a un artículo de blog genérico, mándalos a un artículo de blog que contenga un *Lead Magnet* descargable (ej. "Plantilla de Excel para gestionar inventario" o "Guía para reducir mermas"). Pide el email para descargar la plantilla y luego nutre ese email con automatizaciones hacia el software.
*   **Test de Palabras Clave (Long Tail Comercial):** Dejar de pujar por "cómo gestionar inventario" (muy genérico) y probar "software para gestionar inventario gratis" o "mejor programa de inventario para pymes" (añadiendo palabras de transacción como "software", "programa", "herramienta", "app").

**Para la Campaña C (Bajar el CPA):**
*   **Test de Pujas y Concursos:** El CPC de $3.56 es abusivo. Prueba una estrategia de puja de **ROAS objetivo** o **CPA objetivo** en lugar de maximizar clics/conversiones, dándole a Google un tope. Además, añade como palabra clave negativa el nombre de tu propia marca dentro de esta campaña para evitar pujar contra ti mismo.
*   **Test de Copy de Contraste:** En los anuncios de esta campaña, prueba dos ángulos: Ángulo A (Precios: "La alternativa a [Competidor] que no destruye tu presupuesto") vs Ángulo B (Funcionalidad: "[Competidor] vs Nosotros: Descubre por qué pymes cambian su gestión de inventario"). Esto buscará mejorar la tasa de conversión que ya es buena (4%) para compensar el alto CPC.