# Qwen 3-Next 80B Instruct — agent_capabilities/agent_team_delegation

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 3.91s | tokens_per_second: 218.2
- input_tokens: 1055 | output_tokens: 853
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y estructurado que un emprendedor podría implementar directamente.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el agente coordinador de un Agent Team. Tienes 5 sub-agentes:
- researcher: busca informacion y datos
- writer: redacta contenido
- coder: genera codigo y automatizaciones
- reviewer: revisa calidad y errores
- designer: crea assets visuales

Reglas:
- Descompone tareas complejas en sub-tareas para cada agente
- Respeta dependencias (el writer necesita los datos del researcher primero)
- Asigna prioridades correctamente
- Explica el plan de ejecucion antes de delegar

**user:**

Necesito crear una landing page para el lanzamiento de nuestro nuevo producto "AutoFlow AI" (herramienta de automatizacion para startups). Incluye:
1. Investigar que hace la competencia (3 competidores)
2. Escribir el copy de la landing (hero, features, pricing, CTA)
3. Generar el codigo HTML/CSS de la pagina
4. Crear las imagenes hero y de features
5. Revisar todo antes de publicar

Coordinalo todo.


## Respuesta completa

Entendido. Vamos a descomponer este proyecto complejo en sub-tareas ordenadas, respetando las dependencias lógicas y asignando prioridades adecuadas. El objetivo es crear una landing page profesional y efectiva para "AutoFlow AI".

---

### 📋 **Plan de Ejecución**

1. **Investigación (Researcher)**  
   → Primero, necesitamos entender el mercado: qué hacen los 3 competidores clave, sus estructuras, copy, diseño y propuestas de valor.  
   → Esto es *esencial* para que el writer pueda redactar un copy diferenciado.

2. **Redacción de Copy (Writer)**  
   → Una vez con los datos de competencia, el writer creará el copy estructurado: Hero, Features, Pricing, CTA.  
   → El copy debe ser persuasivo, claro y alineado con el posicionamiento de AutoFlow AI.

3. **Diseño Visual (Designer)**  
   → Con el copy finalizado, el designer creará dos assets visuales clave:  
   - Imagen Hero (para la sección principal)  
   - Imágenes de Features (iconos o ilustraciones para cada punto clave)  
   → Estas imágenes deben reflejar la identidad visual y complementar el mensaje del copy.

4. **Desarrollo Frontend (Coder)**  
   → El coder generará el HTML/CSS de la landing page, usando el copy y las imágenes como base.  
   → La estructura será responsive, accesible y optimizada para conversión.

5. **Revisión Final (Reviewer)**  
   → Revisará todo: coherencia del mensaje, errores de texto, funcionalidad del código, calidad visual, y cumplimiento de objetivos.  
   → Si hay errores, devolverá a los agentes correspondientes para corrección.

---

### ✅ **Delegación de Tareas**

