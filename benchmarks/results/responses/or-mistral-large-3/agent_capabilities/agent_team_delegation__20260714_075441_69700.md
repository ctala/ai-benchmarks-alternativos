# Mistral Large 3 675B — agent_capabilities/agent_team_delegation

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.48 | quality: 9.72
- latency_total: 24.316s | tokens_per_second: 63.0
- input_tokens: 970 | output_tokens: 1531
- judge_score: 4.8 | justificación: 

## Respuesta completa

Vamos a estructurar este proyecto en **5 fases** con dependencias claras entre las tareas. Aquí está el plan de ejecución:

---

### **Fase 1: Investigación (Prioridad: Urgent)**
**Objetivo**: Obtener datos clave sobre la competencia para guiar el diseño y copy.
**Agente asignado**: `researcher`
**Tareas**:
1. Identificar **3 competidores directos** de *AutoFlow AI* (ej: Zapier, Make, Tray.io).
2. Analizar:
   - Estructura de sus landing pages (secciones, jerarquía).
   - Mensajes clave (hero, features, pricing, CTA).
   - Assets visuales (imágenes, iconos, colores).
   - Precios y modelos de suscripción.
3. Entregar un **resumen ejecutivo** con:
   - Fortalezas/debilidades de cada competidor.
   - Oportunidades para diferenciar *AutoFlow AI*.

**Dependencias**: Ninguna (es la primera fase).

---

### **Fase 2: Copywriting (Prioridad: High)**
**Objetivo**: Redactar el contenido de la landing basado en los insights de la investigación.
**Agente asignado**: `writer`
**Tareas**:
1. Escribir el **hero section** (título + subtítulo + CTA principal).
2. Redactar las **features** (3-4 beneficios clave con ejemplos).
3. Crear la sección de **pricing** (planes, precios, beneficios por nivel).
4. Diseñar **CTAs** (llamados a acción para cada sección).
5. Entregar un **documento estructurado** con el copy listo para implementación.

**Dependencias**:
- **Fase 1 completada** (el `writer` necesita los datos del `researcher`).

---

### **Fase 3: Diseño Visual (Prioridad: High)**
**Objetivo**: Crear los assets visuales para la landing.
**Agente asignado**: `designer`
**Tareas**:
1. Diseñar la **imagen hero** (background + producto + estilo visual).
2. Crear **iconos/ilustraciones** para las features.
3. Generar **mockups** de la herramienta (si aplica).
4. Entregar archivos en formatos:
   - `.png`/`.svg` (para web).
   - `.psd`/`.figma` (editable si hay cambios).

**Dependencias**:
- **Fase 2 avanzada** (el `designer` necesita los textos para alinear el estilo visual con el mensaje).

---

### **Fase 4: Desarrollo (Prioridad: High)**
**Objetivo**: Codificar la landing page en HTML/CSS.
**Agente asignado**: `coder`
**Tareas**:
1. Estructurar el **HTML** (secciones: hero, features, pricing, footer).
2. Aplicar **CSS**:
   - Estilos responsivos (mobile/desktop).
   - Animaciones sutiles (ej: hover en botones).
   - Integración con los assets del `designer`.
3. Añadir **JavaScript básico** (si hay interacciones como tabs o modales).
4. Entregar:
   - Archivos `.html`, `.css`, `.js`.
   - Vista previa en un **servidor temporal** (ej: Netlify, Vercel).

**Dependencias**:
- **Fase 2 completada** (copy finalizado).
- **Fase 3 avanzada** (assets visuales listos).

---

### **Fase 5: Revisión y QA (Prioridad: Urgent)**
**Objetivo**: Garantizar calidad antes del lanzamiento.
**Agente asignado**: `reviewer`
**Tareas**:
1. **Revisión de copy**:
   - Ortografía, claridad y tono de marca.
   - Coherencia entre secciones.
2. **Revisión técnica**:
   - Validar HTML/CSS (W3C).
   - Pruebas en dispositivos (mobile, tablet, desktop).
   - Velocidad de carga (optimización de imágenes).
3. **Revisión visual**:
   - Alineación con la identidad de *AutoFlow AI*.
   - Calidad de assets (resolución, formato).
4. **Feedback**:
   - Generar un **reporte de errores** (si los hay).
   - Sugerir mejoras (ej: ajustes de UX).

**Dependencias**:
- **Fase 4 completada** (código y assets integrados).

---

### **Plan de Acción Detallado**
1. **Iniciar Fase 1** (investigación) → `researcher`.
2. **Al terminar Fase 1**, iniciar **Fase 2** (copy) → `writer`.
3. **Cuando el copy esté al 50%**, iniciar **Fase 3** (diseño) → `designer`.
4. **Cuando el copy y diseño estén al 80%**, iniciar **Fase 4** (código) → `coder`.
5. **Al terminar Fase 4**, iniciar **Fase 5** (revisión) → `reviewer`.
6. **Aprobación final**: Si el `reviewer` da luz verde, se publica. Si no, se iteran los cambios.

---

### **Posibles Riesgos y Mitigación**
- **Retraso en investigación**: Si el `researcher` tarda, el `writer` no puede empezar. *Solución*: Asignar prioridad `urgent` y monitorear progreso.
- **Cambios en el copy**: Si el `writer` modifica textos después del diseño, el `designer` debe ajustar assets. *Solución*: Congelar el copy al 90% antes de diseñar.
- **Errores en el código**: Si el `reviewer` encuentra bugs, el `coder` debe corregir. *Solución*: Asignar tiempo extra para QA.

---
### **Próximos Pasos**
Voy a delegar la **Fase 1** al `researcher` para empezar inmediatamente. ¿Confirmas que quieres proceder con este plan?