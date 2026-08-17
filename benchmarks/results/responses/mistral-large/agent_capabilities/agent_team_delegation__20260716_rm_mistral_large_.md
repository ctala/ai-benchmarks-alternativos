# Mistral Large — agent_capabilities/agent_team_delegation

- model_id: `mistralai/mistral-large`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 24.612s | tokens_per_second: 63.1
- input_tokens: 970 | output_tokens: 1553
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y estructurado que un emprendedor podría implementar directamente.

## Respuesta completa

Vamos a estructurar este proyecto en **5 fases** con tareas específicas para cada agente, respetando dependencias y prioridades. Aquí está el plan de ejecución:

---

### **Fase 1: Investigación (Agente: Researcher)**
**Objetivo**: Analizar a 3 competidores directos de *AutoFlow AI* para identificar:
- Estructura de sus landings (secciones clave).
- Mensajes principales (hero, features, CTA).
- Modelos de pricing (si lo muestran).
- Assets visuales recurrentes (iconos, imágenes, colores).
- Fortalezas y debilidades de su propuesta.

**Tarea para Researcher**:
- Buscar 3 competidores (ej: *Zapier*, *Make.com*, *n8n*).
- Extraer datos clave y patrones comunes.
- Entregar un informe estructurado con:
  - Secciones de landing más efectivas.
  - Copy destacado (ej: headlines, CTAs).
  - Paleta de colores y estilo visual.
  - Gaps o oportunidades para *AutoFlow AI*.

**Prioridad**: **Urgent** (Base para las demás fases).

---

### **Fase 2: Copywriting (Agente: Writer)**
**Dependencia**: Investigación completada.
**Objetivo**: Redactar el copy de la landing con:
1. **Hero Section**:
   - Headline principal + subheadline.
   - CTA primario (ej: "Empieza gratis" / "Agenda una demo").
2. **Features**:
   - 3-4 beneficios clave con bullets o párrafos cortos.
   - Posible sección "How it works" (opcional).
3. **Pricing**:
   - Tabla comparativa (ej: Plan Básico/Pro/Enterprise).
   - FAQ breve (2-3 preguntas comunes).
4. **CTA Final**:
   - Mensaje de cierre + botón destacado.

**Tarea para Writer**:
- Usar el informe del *Researcher* para alinear el tono (ej: si la competencia es técnica, ajustar el lenguaje).
- Entregar el copy en un documento organizado por secciones.
- Incluir notas para el *Designer* (ej: "Hero image debe mostrar dashboard de la herramienta").

**Prioridad**: **High**.

---

### **Fase 3: Diseño Visual (Agente: Designer)**
**Dependencias**:
- Investigación completada (para alinear estilo visual).
- Copy del *Writer* (para crear assets coherentes).

**Objetivo**: Crear:
1. **Hero Image**:
   - Ilustración o mockup del producto (ej: interfaz de *AutoFlow AI* con efectos de flujo de trabajo).
   - Alternativa: Imagen abstracta con colores de la marca.
2. **Feature Images**:
   - Iconos o ilustraciones para cada beneficio (ej: "Automatiza en 5 minutos" → icono de reloj).
3. **Assets Adicionales**:
   - Fondos, patrones o elementos decorativos.
   - Posible video explicativo (guion gráfico si aplica).

**Tarea para Designer**:
- Usar herramientas como *Figma* o *Adobe Illustrator*.
- Entregar archivos en formatos: PNG (alta resolución) + SVG (para escalabilidad).
- Incluir paleta de colores y tipografías sugeridas para el *Coder*.

**Prioridad**: **High**.

---

### **Fase 4: Desarrollo Frontend (Agente: Coder)**
**Dependencias**:
- Copy del *Writer* (para integrar texto).
- Assets del *Designer* (para maquetar).

**Objetivo**: Codificar la landing en **HTML/CSS** (y JavaScript si hay interactividad) con:
1. **Estructura**:
   - Header (logo + menú).
   - Hero section (con CTA).
   - Sección de features.
   - Pricing table.
   - Footer (enlaces legales, redes sociales).
2. **Estilo**:
   - Mobile-first y responsive.
   - Animaciones sutiles (ej: hover en botones).
3. **Optimización**:
   - Carga rápida (comprimir imágenes).
   - SEO básico (meta tags, alt text en imágenes).

**Tarea para Coder**:
- Entregar:
  - Archivo `index.html`.
  - Carpeta `assets/` (CSS, JS, imágenes).
  - Documentación breve (ej: cómo editar textos o colores).
- Opcional: Integración con herramientas como *Google Analytics* o *HubSpot*.

**Prioridad**: **Medium** (puede solaparse con diseño si hay assets listos).

---

### **Fase 5: Revisión Final (Agente: Reviewer)**
**Dependencias**: Todas las fases anteriores completadas.
**Objetivo**: Verificar:
1. **Copy**:
   - Ortografía/gramática.
   - Coherencia de mensajes (ej: CTA alineado con el hero).
2. **Diseño**:
   - Consistencia visual (colores, tipografías).
   - Calidad de imágenes (resolución, alineación).
3. **Código**:
   - Validación HTML/CSS (sin errores en consola).
   - Compatibilidad cross-browser (Chrome, Firefox, Safari).
   - Pruebas en móvil/tablet.
4. **Funcionalidad**:
   - Enlaces y botones funcionan.
   - Formularios (si los hay) envían datos correctamente.

**Tarea para Reviewer**:
- Entregar un informe con:
  - Errores críticos (requieren corrección inmediata).
  - Sugerencias de mejora (opcionales).
- Aprobar o rechazar para publicación.

**Prioridad**: **High**.

---

### **Plan de Ejecución Detallado**
| Fase       | Agente      | Tiempo Estimado | Prioridad | Dependencias          |
|------------|-------------|-----------------|-----------|-----------------------|
| Investigación | Researcher  | 4-6 horas       | Urgent    | Ninguna               |
| Copywriting   | Writer      | 6-8 horas       | High      | Investigación          |
| Diseño        | Designer    | 8-12 horas      | High      | Investigación + Copy   |
| Desarrollo    | Coder       | 10-14 horas     | Medium    | Copy + Diseño         |
| Revisión      | Reviewer    | 4-6 horas       | High      | Todas las anteriores   |

---

### **Próximos Pasos**
1. **Iniciar Fase 1**: Delegar la investigación al *Researcher*.
2. **Paralelizar**: Una vez que el *Writer* tenga datos, empezar con el copy. El *Designer* puede preparar bocetos preliminares.
3. **Sincronizar**: El *Coder* comenzará cuando el copy y los assets estén al 80% listos.
4. **Revisión**: El *Reviewer* tendrá todo el material 1 día antes de la fecha de lanzamiento.

¿Quieres que **inicie la Fase 1** (investigación de competidores) ahora? O prefieres ajustar algún detalle del plan.