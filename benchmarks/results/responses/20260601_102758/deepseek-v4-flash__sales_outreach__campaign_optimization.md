# DeepSeek V4 Flash (OpenRouter) — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.15 | quality: 9.56
- latency_total: 46.155s | tokens_per_second: 90.1
- input_tokens: 272 | output_tokens: 4157
- judge_score: 5.0 | justificación: 

## Respuesta completa

## 1. Métricas calculadas

| Campaña     | CTR      | CPC        | CPA        | Tasa de conversión (CVR) |
|-------------|----------|------------|------------|--------------------------|
| **A**       | 3%       | $1.40      | $46.67     | 3%                       |
| **B**       | 4%       | $0.375     | $75.00     | 0.5%                     |
| **C**       | 6%       | $3.56      | $88.89     | 4%                       |

**Fórmulas:**
- CTR = Clics / Impresiones
- CPC = Costo / Clics
- CPA = Costo / Signups
- CVR = Signups / Clics

---

## 2. ¿Qué campaña escalar y cuál pausar?

**Escalar Campaña A** – Tiene el CPA más bajo ($46.67) y la mayor eficiencia por dólar (0.0214 signups/$).  
**Pausar Campaña C** – Presenta el CPA más alto ($88.89) y la menor eficiencia (0.01125 signups/$). Aunque su CVR es del 4%, el alto CPC ($3.56) encarece cada conversión.

**Justificación numérica:**
- Por cada $1,000 invertidos:
  - Campaña A → 21.4 signups
  - Campaña B → 13.3 signups
  - Campaña C → 11.3 signups
- Campaña A duplica casi la rentabilidad de C. Además, con el mismo presupuesto ($5,000), asignarlo todo a A generaría ~107 signups, mientras que mantener C solo aportaría ~56 signups combinando A y C.

---

## 3. Redistribución del presupuesto de $5,000

Lo óptimo es **destinar el 100% a la Campaña A** (por su mejor CPA y ROI).  
- **Presupuesto propuesto:** $5,000 para Campaña A.  
- **Estimación de resultados:**  
  - Clics: (5,000 / 1.40) ≈ 3,571 clics  
  - Signups: 3,571 × 3% ≈ 107 signups  

Si existieran limitaciones de volumen (por ejemplo, la campaña A no puede absorber todo el presupuesto sin degradar el CPA), se podría dejar un pequeño porcentaje (ej. 20%) en la Campaña B para mantener flujo de awareness, pero con los datos actuales A es claramente superior.

---

## 4. A/B tests sugeridos para el próximo mes

### Campaña A (Landing principal – prioridad)
- **Test de landing page:** Comparar una versión con formulario de registro directo vs. una con solicitud de demo gratuita.  
- **Test de copy de anuncios:** Probar variaciones que destaquen “Prueba gratis 14 días” vs. “Solución para pymes” para mejorar CTR y potencialmente CPA.  
- **Test de llamado a la acción (CTA):** “Regístrate ahora” vs. “Empieza hoy” en el botón principal.

### Campaña B (Blog content – baja conversión)
- **Test de lead magnet:** Incluir un pop-up ofreciendo un ebook o checklist descargable a cambio del email (en lugar de solo el blog).  
- **Test de formato de contenido:** Comparar el blog actual con un video corto incrustado que termine en un CTA de registro.  
- **Test de segmentación:** Evaluar si los usuarios de “problemas inventario restaurante” responden mejor a un case study de clientes similares.

### Campaña C (Competidor – si se reactiva)
- **Test de copy de anuncios:** Enfocar en ventajas concretas (precio, funcionalidades) vs. “alternativa a [competidor]”.  
- **Test de landing page:** Mostrar una tabla comparativa vs. un testimonio de un cliente que migró.  
- **Test de puja:** Reducir la puja máxima para bajar el CPC y ver si el CPA mejora (aunque baje el volumen).

Estos tests permitirían optimizar cada campaña en función de su objetivo, ya sea escalar eficiencia (A), mejorar conversión (B) o reducir costo (C).