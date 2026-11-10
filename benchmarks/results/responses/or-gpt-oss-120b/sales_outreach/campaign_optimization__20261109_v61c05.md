# GPT-OSS 120B — sales_outreach/campaign_optimization

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.73 | quality: 8.0
- latency_total: 31.358s | tokens_per_second: 102.0
- input_tokens: 322 | output_tokens: 3200

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

## 1️⃣ Métricas de cada campaña (mes)

| Campaña | Impresiones | Clicks | Sign‑ups | Costo | **CTR** | **CPC** | **CPA** | **Conversion Rate** |
|---------|-------------|--------|----------|-------|---------|--------|--------|----------------------|
| **A – Landing principal** | 50 000 | 1 500 | 45 | $2 100 | **3.00 %** (1 500 ÷ 50 000) | **$1.40** (2 100 ÷ 1 500) | **$46.67** (2 100 ÷ 45) | **3.00 %** (45 ÷ 1 500) |
| **B – Blog content** | 120 000 | 4 800 | 24 | $1 800 | **4.00 %** (4 800 ÷ 120 000) | **$0.38** (1 800 ÷ 4 800) | **$75.00** (1 800 ÷ 24) | **0.50 %** (24 ÷ 4 800) |
| **C – Competidor** | 15 000 | 900 | 36 | $3 200 | **6.00 %** (900 ÷ 15 000) | **$3.56** (3 200 ÷ 900) | **$88.89** (3 200 ÷ 36) | **4.00 %** (36 ÷ 900) |

> **Definiciones**  
> - **CTR** = Clicks ÷ Impresiones × 100  
> - **CPC** = Coste ÷ Clicks  
> - **CPA** = Coste ÷ Sign‑ups (costo por adquisición)  
> - **Conversion Rate** = Sign‑ups ÷ Clicks × 100  

---

## 2️⃣ ¿Qué campaña escalar y cuál pausar?  

| Métrica | Campaña A | Campaña B | Campaña C |
|---------|-----------|-----------|-----------|
| **CPA (costo por adquisición)** | $46.7 **← más bajo** | $75 | $88.9 |
| **Conversion Rate** | 3 % | 0.5 % **← muy bajo** | 4 % |
| **CPC** | $1.40 | $0.38 **← barato** | $3.56 **← muy caro** |
| **CTR** | 3 % | 4 % | 6 % |
| **Volumen de sign‑ups** | 45 (45 % del total) | 24 (24 % del total) | 36 (36 % del total) |

### 🟢 **Escalar: Campaña A (Landing principal)**
- **CPA más bajo** ($46.7) → mayor rentabilidad.
- **Conversion Rate razonable** (3 %) y volumen de sign‑ups mayor que B.
- CPC aceptable y CTR sólido.  
- El objetivo principal (generar leads) se está cumpliendo de forma eficiente.

### 🟡 **Mantener y optimizar: Campaña B (Blog content)**
- **CPC muy bajo** ($0.38) y **CTR alto** (4 %) → está atrayendo mucho tráfico barato.
- **Conversion Rate muy bajo** (0.5 %) → la calidad del tráfico o la página de destino no está convirtiendo.
- Acción: invertir en pruebas de landing‑page / formularios y en segmentación de audiencia para elevar el CR.

### 🔴 **Pausar / replantear: Campaña C (Competidor)**
- **CPA más alto** ($88.9) y **CPC elevado** ($3.56) → gasto ineficiente.
- Aunque el CTR y la tasa de conversión son buenos, el costo por adquisición supera ampliamente al de la campaña A.
- Mejor destinar esos fondos a A (escala) y a B (optimización) o a nuevas pruebas.

---

## 3️⃣ Redistribución del presupuesto de $5 000/mes  

**Situación actual** (gasto total = $7 100)  
- A: $2 100 (30 %)  
- B: $1 800 (25 %)  
- C: $3 200 (45 %)

**Objetivo:** eliminar el gasto poco rentable (C) y reforzar A, manteniendo una partida para probar mejoras en B.

### Propuesta de asignación

| Campaña / Acción | % del presupuesto | Monto ($) | Comentario |
|------------------|-------------------|-----------|------------|
| **A – Escalado** | **55 %** | **$2 750** | +$650 respecto a lo actual → más impresiones y pujas más agresivas. |
| **B – Optimización** | **35 %** | **$1 750** | Mantener el nivel actual + $‑50; usar el extra para pruebas de landing‑page y audiencias. |
| **Test / Experimentos (A/B, remarketing, nuevas creatividades)** | **10 %** | **$500** | Fondos reservados para los experimentos listados en el punto 4. |

**Resultado:** $2 750 + $1 750 + $500 = $5 000 → presupuesto bajo control, sin desperdicio en la campaña C.

*Si después de 2‑3 semanas B sigue con CR < 1 %, se puede recortar ese 35 % y reasignar el resto a A o a nuevas pruebas.*

---

## 4️⃣ A/B tests recomendados para el próximo mes  

### 4.1. Landing‑page (Campaña A y B)
| Variante | Elemento a probar | Hipótesis |
|----------|-------------------|-----------|
| **Headline** | “Software de gestión de inventario para PYMES” vs “Control total de tu inventario en minutos” | Un mensaje más orientado a beneficio aumentará el CR. |
| **Formulario** | 1 campo (email) vs 3 campos (nombre, email, teléfono) | Menos fricción → más sign‑ups. |
| **CTA botón** | “Regístrate gratis” (verde) vs “Empieza ahora” (rojo) | Un CTA más directo y color contrastante mejorará la tasa de conversión. |
| **Prueba social** | Sin testimonios vs 2 testimonios de clientes + logo de partners | Añadir prueba social aumentará la confianza y el CR. |
| **Video vs Imagen** | Hero video de 10 s vs imagen estática de la interfaz | Un video explicativo incrementará la intención de registro. |

### 4.2. Copys y extensiones de anuncio (todas)
| Test | Variable | Rango esperado |
|------|----------|----------------|
| **Valor añadido** | “Ahorra 20 % en tiempo de inventario” vs “Gestión 100 % en la nube” | Incremento del CTR en 0.5‑1 pp. |
| **Llamada a la acción** | “Solicita demo” vs “Prueba gratis” | Mejora del CPC y del CR. |
| **Match type** | Broad match modificados vs Exact match | Reducción del CPC sin perder impresiones. |
| **Extensiones** | Añadir extensiones de sitio y de llamada vs solo extensiones de enlace | Mejora del CTR y del Quality Score. |

### 4.3. Segmentación de audiencia
| Audiencia | Test | Métrica clave |
|-----------|------|---------------|
| **Tamaño de empresa** (1‑10 vs 11‑50 empleados) | Crear grupos de anuncios separados | CPA y CR por segmento. |
| **Industria** (retail vs restaurantes vs manufactura) | Palabras clave específicas por sector | CPA y volumen de leads. |
| **Remarketing** | Audiencia que hizo click pero no se registró → display ads con oferta “Descuento 10 % 7‑días” | Coste por lead de remarketing vs nuevo tráfico. |

### 4.4. Estrategia de puja
| Estrategia | Test | Expectativa |
|------------|------|-------------|
| **Maximizar conversiones** (actual) vs **CPA objetivo** = $45 | Ver si el CPA objetivo permite bajar el CPA sin sacrificar volumen. | Reducción del CPA en ≤ 10 % manteniendo ≥ 80 % del tráfico. |
| **Smart Bidding (ROAS)** (si se dispone de datos de valor de cliente) | Comparar con CPA objetivo. | Mejora del retorno económico. |

### 4.5. Competidor (Campaña C) – “Mini‑test”
- **Palabras clave de cola larga**: “alternativa a [competidor] para pymes” vs “alternativa a [competidor] gratis”.  
- **Landing específica**: página comparativa con tabla de ventajas → medir si el CPA baja.  
- Si después de 2 semanas el CPA sigue > $80, se recomienda pausar definitivamente.

---

## Resumen rápido

| Acción | Por qué |
|-------|----------|
| **Escalar Campaña A** | CPA más bajo ($46.7) y buen CR (3 %). |
| **Mantener y optimizar Campaña B** | CPC barato ($0.38) pero CR muy bajo (0.5 %). Necesita mejoras en landing‑page y segmentación. |
| **Pausar Campaña C** | CPA más alto ($88.9) y CPC elevado ($3.56). No rentable con el presupuesto actual. |
| **Redistribuir presupuesto** | $2 750 a A, $1 750 a B, $500 a tests (total $5 000). |
| **A/B tests** | Landing‑page, copys, audiencias, pujas y mini‑test de competidor para bajar CPA y subir CR. |

Con esta redistribución y los experimentos propuestos, deberías:

1. **Mejorar el costo por adquisición** (meta: < $50).  
2. **Aumentar el número total de leads** (objetivo: +30 % respecto al mes anterior).  
3. **Obtener datos claros** para decidir si la estrategia “competidor” vale la pena volver a activar en el futuro.  

¡Éxitos en el próximo mes de campañas! 🚀