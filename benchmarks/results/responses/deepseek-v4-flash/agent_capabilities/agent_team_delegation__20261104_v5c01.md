# DeepSeek V4 Flash (OpenRouter) — agent_capabilities/agent_team_delegation

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.83 | quality: 9.52
- latency_total: 12.888s | tokens_per_second: 52.1
- input_tokens: 1188 | output_tokens: 672
- judge_score: 4.8 | justificación: 

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

## 🚀 Plan de Ejecución para la Landing Page de **AutoFlow AI**

Voy a coordinar a los agentes en el siguiente orden, respetando las dependencias:

```
FASE 1 (Paralelo)
   ┌─ 🔍 Researcher → Investiga 3 competidores
   └─ 🎨 Designer   → Crea brief visual para imágenes

FASE 2 (Depende de Researcher)
   └─ ✍️ Writer → Redacta copy con datos de competencia

FASE 3 (Depende de Writer)
   └─ 💻 Coder → Genera HTML/CSS con el copy listo

FASE 4 (Depende de todo)
   └─ ✅ Reviewer → Revisa calidad final
```

¡Empecemos! Delegando las primeras tareas en paralelo:

---

### 🔍 FASE 1A: Researcher - Investigar competidores