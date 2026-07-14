# Devstral 2 (Dic 2025) — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.29 | quality: 8.0
- latency_total: 17.451s | tokens_per_second: 71.8
- input_tokens: 177 | output_tokens: 1253
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y práctico para evaluar la hipótesis con un enfoque en la eficiencia de costos y tiempo.

## Respuesta completa

**Experimento para matar la hipótesis:**
*"Agencias pequeñas pagarían $200/mes por automatización de reportes"*

---

### **1. Diseño del experimento (Método: "Fake Door" + Entrevistas)**
**Objetivo:** Medir el interés *real* de pago (no solo curiosidad) con el menor esfuerzo.

#### **Pasos concretos:**
**A. Crear una landing page falsa (1 día, $0-$50)**
- **Herramienta:** Carrd.co (gratis) o Unbounce (prueba gratuita).
- **Contenido mínimo:**
  - Título: *"Automatiza los reportes de tus clientes en 5 minutos. $200/mes."*
  - Descripción: *"Conecta Google Ads, Meta, GA4 y genera reportes personalizados con tu branding. Sin Excel, sin perder horas."*
  - Botón grande: *"Quiero probarlo GRATIS 7 días"* (link a un formulario).
  - **Importante:** Incluir un campo *"¿Cuántos clientes gestionas?"* (para segmentar agencias pequeñas).

**B. Conseguir tráfico CALIFICADO (3 días, $100-$200)**
- **Fuente 1:** Grupos de Facebook/LinkedIn de agencias de marketing (ej: *"Agencias de Marketing Digital Latinoamérica"*).
  - Publica: *"¿Cuánto tiempo pierdes al mes haciendo reportes para clientes? Estamos probando una herramienta que lo automatiza. Si te interesa, déjame un mensaje o regístrate aquí [link]."*
  - **Costo:** $0 (pero invierte 2 horas/día respondiendo comentarios).
- **Fuente 2:** Anuncios en LinkedIn/Instagram dirigidos a:
  - Dueños de agencias con 2-10 empleados.
  - **Presupuesto:** $50-$100 (para obtener ~200 clics).
  - **Texto del anuncio:** *"¿Odias hacer reportes manuales? Prueba [Nombre] 7 días gratis. Solo para agencias pequeñas."* (Usa una imagen de un reporte feo en Excel vs. uno bonito automático).

**C. Filtrar y entrevistar (2 días, $0)**
- **Criterio de filtrado:** Solo habla con quienes:
  1. Tengan una agencia con ≤10 empleados.
  2. Hayan hecho clic en el botón *"Quiero probarlo"* (aunque sea gratis).
- **Script de entrevista (10 mins por llamada):**
  1. *"Cuéntame cómo haces los reportes hoy. ¿Qué herramientas usas?"*
  2. *"¿Qué es lo más doloroso de ese proceso?"* (Si no mencionan tiempo/costo, la hipótesis es débil).
  3. *"Si existiera una herramienta que te ahorrara 8 horas/mes en reportes, ¿qué pagarías?"*
     - Si dicen *"$50"* o *"nada, ya uso [herramienta X]"*, **abandona**.
  4. *"Si te doy acceso hoy mismo por $200/mes, ¿la comprarías?"* (Si vacilan, pregunta: *"¿Qué te faltaría para decidirte?"*).

---

### **2. Métricas de fracaso (cuándo abandonar)**
- **Señal roja 1:** Menos del **5%** de los visitantes hacen clic en *"Quiero probarlo"* (ej: 200 visitas → ≤10 clics).
  - *Significado:* No hay suficiente dolor como para siquiera probar una solución.
- **Señal roja 2:** En las entrevistas, **ninguna agencia** dice que pagaría ≥$150/mes.
  - *Significado:* El precio está lejos de su disposición a pagar.
- **Señal roja 3:** Más del 50% de los entrevistados mencionan que ya usan una herramienta similar (ej: DashThis, AgencyAnalytics).
  - *Significado:* El mercado está saturado.

---

### **3. Costos y tiempo total**
- **Tiempo:** 1 semana (5 días hábiles).
- **Costo:** $100-$250 (anuncios + dominio si no usas Carrd).
- **Esfuerzo:** 10-15 horas (crear landing, publicar en grupos, entrevistar).

---

### **4. Alternativa aún más barata (si no tienes $100)**
- **Método:** Envíale un mensaje directo a 50 dueños de agencias pequeñas por LinkedIn/Instagram con este texto:
  *"Hola [Nombre], soy [Tu nombre]. Estoy validando una idea: una herramienta que automatiza reportes para agencias por $200/mes. ¿Te interesa probarla cuando lance el beta? (Responde SÍ/NO)."*
  - **Costo:** $0.
  - **Tiempo:** 2 horas.
  - **Señal de fracaso:** Si ≤5 responden *"SÍ"*, abandona.

---

### **Por qué esto mata la hipótesis:**
- Si las agencias no hacen clic en un botón de *"prueba gratis"*, **no pagarán $200**.
- Si en entrevistas no validan el precio, **el modelo de negocio no funciona**.
- Si ya usan alternativas, **no hay espacio para ti**.

**Regla de oro:** Si no encuentras al menos **10 agencias dispuestas a pagar $200/mes en 1 semana**, la hipótesis es falsa. **No construyas nada.**