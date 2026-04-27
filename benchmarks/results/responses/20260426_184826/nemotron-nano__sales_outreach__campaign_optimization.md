# Nemotron 3 Nano 30B — sales_outreach/campaign_optimization

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.85 | quality: 9.0
- latency_total: 38.581s | tokens_per_second: 104.9
- input_tokens: 316 | output_tokens: 4046
- judge_score: 4.8 | justificación: 

## Respuesta completa

## 1️⃣ Métricas clave (cálculos)

| Campaña | Impresiones | Clicks | Sign‑ups | Coste | **CTR** | **CPC** | **CPA** | **Conversion Rate (CVR)** |
|---------|-------------|--------|----------|-------|--------|----------|----------|---------------------------|
| **A – Landing principal** | 50 000 | 1 500 | 45 | $2 100 | **3 %** (1 500 ÷ 50 000) | **$1,40** (2 100 ÷ 1 500) | **$46,67** (2 100 ÷ 45) | **3 %** (45 ÷ 1 500) |
| **B – Blog content** | 120 000 | 4 800 | 24 | $1 800 | **4 %** (4 800 ÷ 120 000) | **$0,38** (1 800 ÷ 4 800) | **$75,00** (1 800 ÷ 24) | **0,5 %** (24 ÷ 4 800) |
| **C – Competidor** | 15 000 | 900 | 36 | $3 200 | **6 %** (900 ÷ 15 000) | **$3,56** (3 200 ÷ 900) | **$88,89** (3 200 ÷ 36) | **4 %** (36 ÷ 900) |

> **Notas de cálculo**  
> - **CTR** = Clicks ÷ Impresiones.  
> - **CPC** = Coste total ÷ Clicks.  
> - **CPA** = Coste total ÷ Sign‑ups (costo por adquisición).  
> - **Conversion Rate (CVR)** = Sign‑ups ÷ Clicks (tasa de conversión “click → signup”).  

---

## 2️⃣ ¿Qué campana escalar y cuál pausar?

| Métrica | Campaña A | Campaña B | Campaña C |
|---------|-----------|-----------|-----------|
| **CTR** | 3 % | 4 % | **6 %** (más alto) |
| **CPC** | $1,40 | **$0,38** (más bajo) | $3,56 (más alto) |
| **CPA** | **$46,67** (más bajo) | $75,00 | $88,89 (más alto) |
| **CVR** | **3 %** (más alta) | 0,5 % | 4 % (más alta, pero menos fiable por volumen) |

### Interpretación rápida
| Campaña | Puntos fuertes | Puntos débiles |
|---------|----------------|----------------|
| **A** | - CPA más bajo → mejor rentabilidad por signup. <br>- CVR del 3 % (muy superior a B). <br>- CPC razonable ($1,40). | - CTR algo bajo (3 %). |
| **B** | - CPC más bajo ($0,38) → barato generar tráfico. | - CPA alto ($75) → cada signup cuesta mucho más. <br>- CVR mínima (0,5 %). |
| **C** | - CTR más alto (6 %). | - CPA y CPC muy altos → menos eficiente en coste por signup. <br>- Inversión desproporcionada respecto a resultados. |

### Recomendación
- **Escalar: Campaña A**  
  - Tiene el **CPA más bajo** y una **CVR del 3 %**, lo que indica que el tráfico que genera está convirtiendo mejor que el de B y C.  
  - El CPC ($1,40) sigue siendo aceptable dentro del presupuesto y permite mantener un flujo de leads sin que el coste se dispare.  
  - Además, la audiencia está muy alineada con “software gestión inventario” y “inventario pymes”, palabras clave de alta intención comercial.

- **Pausar (o reducir drásticamente): Campaña C**  
  - Aunque su CTR es el más alto, el **CPA de $88,89** y el **CPC de $3,56** son los peores de los tres.  
  - Cada signup le cuesta casi el doble que la campaña A y el presupuesto actual se está “quemando” sin rendimientos proporcionales.  
  - Mantenerla con el presupuesto actual (≈$3 200) supera ampliamente el límite de $5 000 y no aporta retornos sostenibles.

> **Conclusión:** Mantén/expande la campaña A, reduce o pausa la campaña C. La campaña B puede seguir activa como canal de “awareness”, pero con una asignación de presupuesto más conservadora.

---

## 3️⃣ Redistribución del presupuesto de **$5 000/mes**

### Paso 1 – Ajustar los gastos actuales
- Gasto total actual = $2 100 + $1 800 + $3 200 = **$7 100** (excede el presupuesto en $2 100).  
- Necesitamos recortar $2 100 y redistribuirlos de forma estratégica.

### Paso 2 – Propuesta de nuevo reparto

| Campaña | Gasto propuesto | % del presupuesto total | Comentario |
|---------|----------------|--------------------------|------------|
| **A – Landing principal** | **$2 800** | **56 %** | Incrementar +$700 respecto al gasto original para aprovechar su mejor CPA y CVR. |
| **B – Blog content** | **$1 500** | **30 %** | Mantener una presencia de contenido, pero con un presupuesto reducido (≈‑$300) ya que su CPA es alto y su CVR baja. |
| **C – Competidor** | **$500** | **10 %** | Mantener solo una **prueba mínima** (p.ej., 1‑2 anuncios) para seguir monitorizando la métricas, pero sin inversión significativa. |
| **Reserva / testing** | **$200** | **4 %** | Fondo para pruebas A/B, ajustes de puja y optimización de landing pages. |

> **Total = $5 000** (ajustado al presupuesto máximo).  

### ¿Por qué esta distribución?
- **Mayor inversión en la campaña con mejor retorno (A)**: el CPA es 38 % menor que el de B y 48 % menor que el de C. Incrementar su gasto maximiza el número de sign‑ups por dólar invertido.  
- **Preservar la presencia de B** como canal de contenido y SEO, pero con un gasto limitado al nivel que nos permite observar tendencias sin comprometer la rentabilidad.  
- **Testeo controlado de C**: con $500 podemos seguir recogiendo datos de impresiones/CTR sin que el coste se vuelva crítico. Si en los próximos 2‑3 semanas el CPA mejora > $70, podríamos reconsiderar. De lo contrario, se pausa definitivamente.  

---

## 4️⃣ Tests A/B sugeridos para el próximo mes

### 4.1. Campaña A – Landing principal
| Variable a testear | Idea de variante | Métrica objetivo |
|--------------------|------------------|------------------|
| **Copy del anuncio** | - Enfocar en “Gestiona tu inventario en 5 min”. <br>- Enfocar en “Software de inventario 100 % gratuito en la primera mes”. | Mejora el CTR y la tasa de clics cualificados. |
| **Titular de la landing** | - “Control total de tu inventario”. <br>- “Optimiza tus recursos y reduce costes”. | Incrementar CVR (más clics → sign‑ups). |
| **Imagen / Video** | - Imagen estática de dashboard vs. video corto de 15 s mostrando flujo de trabajo. | Aumento de CTR y tiempo de permanencia. |
| **Formulario** | - Formulario de 1 campo (email) vs. formulario de 2 campos (email + empresa). | Reducir fricción → mayor CVR. |
| **CTA** | - “Empieza ahora gratis” vs. “Solicita una demo”. | Mejorar tasa de conversión. |
| **Extensiones** | - Añadir extensión de llamada y extensión de “Precio”. | Incrementar CTR y calidad del tráfico. |
| **Palabras clave** | - Utilizar coincidencia “exacta” vs. “de frase”. <br>- Incluir variantes “software de gestión de inventario para pymes”. | Ajustar volumen y calidad del tráfico. |

### 4.2. Campaña B – Blog content
| Variable a testear | Idea de variante | Métrica objetivo |
|--------------------|------------------|------------------|
| **Titular del anuncio** | - “Aprende a gestionar inventario en tu restaurante”. <br>- “Soluciones rápidas para problemas de inventario”. | Elevar CTR. |
| **Formato de anuncio** | - Texto tradicional vs. anuncio de imagen con captura de pantalla del blog. | Mejorar CTR y CVR. |
| **Landing de captura** | - Página de “Descarga guía gratuita”. <br>- Página con webinar en vivo. | Mejorar calidad de leads (CVR). |
| **Segmentación de audiencia** | - Targeting por “propietarios de restaurantes” vs. “gerentes de operaciones”. | Aumentar relevancia y CTR. |
| **Oferta** | - “Acceso inmediato al artículo”. <br>- “Acceso a video tutorial + checklist”. | Incrementar conversiones. |

### 4.3. Campaña C – Competidor (solo testeo)
| Variable a testear | Idea de variante | Métrica objetivo |
|--------------------|------------------|------------------|
| **Palabra clave** | - Cambiar “alternativa a [competidor]” por “software de inventario rival a [competidor]”. | Mejorar relevancia y CTR. |
| **Copy de anuncio** | - Enfatizar “Sin contratos a largo plazo”. <br>- Enfatizar “Precio bajo + soporte 24/7”. | Reducir CPA. |
| **Landing de destino** | - Landing con testimonios de clientes actuales vs. landing con demo en video. | Mejorar CVR. |
| **Oferta de prueba** | - Prueba gratuita de 7 días vs. “Demo guiada en 15 min”. | Atraer usuarios con mayor intención de compra. |

---

### Cómo medir el éxito de los tests
1. **Duración:** al menos **7‑10 días** por variante para capturar variación de día‑a‑día.  
2. **Muestreo mínimo:** al menos **100‑150 clics** por variante antes de declarar ganador.  
3. **KPIs a monitorizar:** CTR, CPC, CPA y CVR. Priorizar la mejora del **CPA** (costo por signup) y la **CVR** (eficiencia de la landing).  
4. **Herramientas:** Google Ads Experiments, Google Optimize (o GA4) para pruebas de landing, y BigQuery / Data Studio para análisis de resultados.

---

### Resumen rápido
- **Escalar** la **Campaña A** (landing principal) – mayor rentabilidad.  
- **Pausar / reducir** la **Campaña C** – alto CPA y CPC.  
- **Mantener** la **Campaña B** con un presupuesto reducido y usarla como canal de contenido/awareness.  
- **Reasignar** el presupuesto total de $5 000 según la tabla propuesta.  
- **Implementar** pruebas A/B en copy, landing page, extensiones y segmentación para seguir afinando la eficiencia de cada campaña.

¡Con estos ajustes deberías maximizar el número de sign‑ups dentro del límite de $5 000 y mejorar la rentabilidad de tus campañas! 🚀