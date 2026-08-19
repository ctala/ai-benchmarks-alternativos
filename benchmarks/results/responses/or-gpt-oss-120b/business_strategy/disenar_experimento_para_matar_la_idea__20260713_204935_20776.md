# GPT-OSS 120B — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.54 | quality: 8.0
- latency_total: 39.508s | tokens_per_second: 44.8
- input_tokens: 228 | output_tokens: 1771
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan detallado y práctico para evaluar la hipótesis de manera económica y rápida.

## Respuesta completa

## Experimento “Mata la hipótesis”  
**Hipótesis que queremos *desmentir***  
> *“Pequeñas agencias de marketing pagarían $200 / mes por una herramienta que les automatice los reportes a clientes.”*  

### 1. Definir el criterio de “muerte”
| Criterio | ¿Qué indica que la hipótesis está **muerta**? |
|----------|----------------------------------------------|
| **Precio** | < 15 % de los prospectos entrevistados (o encuestados) dicen que **$200/mes es demasiado caro** para lo que describimos. |
| **Necesidad** | < 20 % de los prospectos dicen que **actualmente les cuesta > 2 h/semana** crear esos reportes **y que les molestaría automatizarlos**. |
| **Disposición a pagar** | En una encuesta de “pretensión de pago” (ver abajo) **ninguno** de los prospectos indica que pagaría **≥ $150/mes** (el 75 % del precio objetivo). |
| **Compromiso real** | No conseguimos **ni una** pre‑venta o “letter of intent” (LOI) de $200/mes (incluso si es solo una firma de intención sin pago). |

**Si cualquiera de los cuatro criterios se cumple, detén el proyecto.**  
(El criterio más barato y rápido de los cuatro suele ser el de “precio/ disposición a pagar”. Usa ese como disparador inicial; si falla, revisa los demás.)

---

## 2. El experimento de “validación de precio” (el más barato y rápido)

### Paso a paso

| Paso | Acción | Herramientas / Coste | Tiempo estimado |
|------|--------|----------------------|-----------------|
| 1️⃣ | **Crear una página de aterrizaje mínima (landing‑page)** que describa la solución en 3‑4 frases, muestre un mockup sencillo del reporte automatizado y destaque *“Solo $200 / mes”.* | Herramienta gratuita ( Carrd, Softr, Webflow free tier ) → **$0**. Usa una captura de pantalla generada con IA (Midjourney/DALL‑E) → **$0** (versión gratuita). | 2 h |
| 2️⃣ | **Añadir un botón de “Quiero probarlo”** que abra un formulario corto (Google Forms / Typeform free). Preguntas: <br> a) Nombre de la agencia <br> b) Número de empleados <br> c) Cuántas horas gastan en reportes cada semana <br> d) ¿Estarían dispuestos a pagar $200/mes? (Sí/No/¿Cuál sería un precio razonable?) <br> e) Correo para contacto. | Google Forms (gratis) + dominio opcional (si ya tienes, sino usa subdominio) → **$0**. | 1 h |
| 3️⃣ | **Traficar barato**: lanzar 2‑3 campañas de prueba en Facebook/Instagram o LinkedIn dirigidas a *“Propietarios de agencias de marketing”* y *“Consultores de marketing digital”* (presupuesto **$50** total). | $50 en ads + $0 en creatividades (usa el mockup + copy). | 1 día para lanzar, 3‑5 días de exposición. |
| 4️⃣ | **Medir la respuesta**: después de 5 días, revisa el formulario.<br> - Si **< 5 respuestas** → no hay suficiente mercado → **mata**.<br> - Si **≥ 5 respuestas** y **≤ 15 %** (0‑1) dicen “Sí, pagaría $200/mes” → **mata**.<br> - Si **≥ 30 %** dicen “Sí” o la respuesta de precio razonable está **≥ $150** → la hipótesis sigue viva → pasa al siguiente test (opcional). | Ningún coste adicional. | 1 h de análisis. |

#### Coste total del test
- **Landing page & formulario:** $0  
- **Publicidad:** **$50** (puedes bajar a $30 si usas sólo Facebook).  
- **Tiempo propio (≈ 8 h):** valor de oportunidad, pero sin gasto monetario directo.  

**Total monetario:** **≈ $50**  

**Duración total:** **7‑10 días** (incluye tiempo de publicación y espera de respuestas).

---

## 3. Qué hacer con los resultados

| Resultado | Acción inmediata |
|-----------|-------------------|
| **≤ 5 respuestas** o **≤ 15 % “Sí”** (0‑1 de 5‑10) | **Abortar**: la disposición a pagar es demasiado baja. |
| **≥ 30 % “Sí”** (≥ 2‑3 de 5‑10) y precio razonable ≥ $150 | **Hipótesis todavía viva** → puedes pasar a un test de “pre‑venta” (ver abajo) o a un MVP rápido. |
| **Entre 15‑30 %** (1‑2 de 5‑10) | **Re‑evaluar**: quizás el segmento está mal definido. Cambia targeting (ej. agencias de 5‑10 empleados) y repite con el mismo presupuesto antes de descartar. |

---

## 4. (Opcional) Test de compromiso real – “Letter of Intent” (LOI)

Si el test de precio pasa el umbral de 30 %, haz un segundo micro‑test antes de escribir código:

1. **En el mismo formulario**, añade una opción: “Si estuvieras interesado, firma una LOI de $200/mes (no se cobra ahora, solo compromiso)”.  
2. **Ofrece un incentivo simbólico** (ej. acceso a una hoja de trucos de reporting).  
3. **Si obtienes 1‑2 LOI firmadas**, ya tienes evidencia suficiente para invertir tiempo de desarrollo.  

**Coste:** $0 (solo tiempo).  
**Tiempo:** 2‑3 días adicionales.

Si no consigues ninguna LOI, **mata** la idea aunque el test de precio haya sido “pasable”.

---

## 5. Checklist rápido para ejecutar hoy

1. **Escribe el copy** (2‑3 frases + precio).  
2. **Crea el mockup** con IA (prompt: “Dashboard de reporte de marketing con gráficos de ROI, tráfico y leads, estilo SaaS minimalista”).  
3. **Construye la landing** en Carrd (usa plantilla “Simple”).  
4. **Configura el formulario** con las 5 preguntas clave.  
5. **Diseña el anuncio** (imagen del mockup + texto: “Reportes a clientes en 1 clic – $200/mes”).  
6. **Lanza la campaña** con $50 budget, segmentación: “Propietario de agencia de marketing”, “Gerente de cuentas”, “Consultor de marketing digital”, 0‑10 empleados, EE. UU./Canadá/Europa.  
7. **Monitorea** número de respuestas cada día.  
8. **Analiza** al día 5.  

---

### Resumen rápido

| Qué | Cuánto | Cuánto tiempo | Resultado que mata la hipótesis |
|-----|--------|---------------|---------------------------------|
| Landing + formulario | $0 | 3 h | < 5 respuestas o ≤ 15 % “Sí” |
| Ads (Facebook/IG/LinkedIn) | $50 | 5 días de exposición | < 5 respuestas o ≤ 15 % “Sí” |
| Análisis | $0 | 1 h | Ver tabla |
| (Opcional) LOI | $0 | 2 días | 0 LOI = muerte |

Con **menos de $60 y menos de 2 semanas** tendrás una respuesta clara: o la hipótesis está muerta o tienes suficiente señal para seguir invirtiendo. ¡Buena suerte y recuerda: el objetivo es *romper* la idea, no confirmarla!