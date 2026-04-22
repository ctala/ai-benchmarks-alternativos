# Roadmap del Benchmark

> Ultima actualizacion: 22 de Abril de 2026

## En Progreso (Abril 2026)

- [x] Run completo de Kimi K2.6 vs Claude Opus 4.7/4.6 con juez Phi-4
- [ ] Run completo de 8 modelos principales con juez Phi-4 (643/728, ~40 min restantes)
- [ ] Run de lote 2: modelos restantes (GPT-4.1, GPT-5.4, Mistral Large, Kimi K2, Qwen, Nemotron, GLM-5.1) con juez
- [ ] Regenerar CheatSheet PDF con resultados scoring v2 + juez
- [ ] Actualizar ranking global en README con resultados definitivos

## Proxima Version (Mayo 2026)

### Tests Nuevos
- [ ] **n8n_workflow_generation**: Generar workflows de N8N funcionales (simple y complejo) usando nodos correctos, validar contra documentacion de N8N via MCP
- [ ] **n8n_debugging**: Dar un workflow roto y que el modelo lo debugee y corrija
- [ ] **contract_review**: Revisar contratos y detectar clausulas problematicas
- [ ] **cv_screening**: Evaluar CVs para un puesto con ranking y justificacion
- [ ] **video_script**: Guion para video corto de producto (60-90 segundos)

### Modelos Nuevos por Evaluar
- [ ] Modelos que salgan en Mayo 2026
- [ ] Re-evaluar Gemma 4 cuando Ollama arregle el bug de output vacio
- [ ] Probar modelos locales en NVIDIA DGX Spark (llega la otra semana)

### Mejoras al Scoring
- [ ] Guardar respuesta COMPLETA en JSON (no solo preview de 300 chars) para poder re-calcular scores sin re-llamar APIs
- [ ] Multi-judge: correr con 2-3 jueces y promediar para reducir sesgo
- [ ] Validacion especifica de JSON en news_seo_writing (parsear y verificar claves)
- [ ] Validacion de caracteres chinos como categoria separada (no solo penalizacion)

### Infraestructura
- [ ] Script para re-calcular scores desde respuestas guardadas (evitar re-llamar APIs)
- [ ] Dashboard web simple para visualizar resultados (HTML estatico)
- [ ] Automatizar run mensual con GitHub Actions o cron
- [ ] Comparar resultados entre meses (delta tracking)

## Mejoras Futuras (Q3 2026)

### Tests Avanzados
- [ ] **agent_long_session**: Sesiones de agente de 30+ minutos con contexto acumulado
- [ ] **multi_agent_collaboration**: Dos modelos colaborando en una tarea
- [ ] **real_api_integration**: Llamadas reales a APIs (no simuladas) con validacion de resultado
- [ ] **image_understanding**: Dar una imagen y que el modelo la describa/analice (modelos con vision)
- [ ] **cost_optimization_routing**: Dado un budget, elegir el mix optimo de modelos

### Plataformas
- [ ] Tests especificos de compatibilidad con OpenClaw
- [ ] Tests especificos de compatibilidad con Hermes
- [ ] Tests de Agent Teams (multiples agentes coordinados)
- [ ] Validar que workflows generados funcionen en N8N real (no solo formato)

### Hardware Local (DGX Spark)
- [ ] Benchmark de modelos locales: latencia, tok/s, calidad sin internet
- [ ] Comparar mismo modelo local vs API (calidad, velocidad, costo total)
- [ ] Fine-tuning de modelo local para tareas especificas del negocio
- [ ] Juez local con modelo mas grande (Qwen 3.5 72B como juez en DGX Spark)

## Pendiente: Recomendaciones por Caso de Uso Real

Generar una seccion (o documento separado) con recomendaciones especificas basadas en los resultados del benchmark. No solo "mejor modelo global" sino "mejor modelo para TU caso":

### Por Plataforma de Agentes
- [ ] **OpenClaw**: Que modelo usar como cerebro, que modelo para sub-tareas, configuracion recomendada
- [ ] **Hermes**: Modelos compatibles, cual da mejor tool calling, setup optimo
- [ ] **N8N**: Que modelo para el nodo AI Agent, que modelo para AI Text, workflows recomendados
- [ ] **Claude Code (alternativas)**: Setup con Roo Code + MiniMax/Devstral/DeepSeek por ~$50/mes

### Por Tarea de Negocio
- [ ] **Soporte al cliente**: Modelo + configuracion + ejemplo de workflow N8N
- [ ] **Generacion de contenido SEO**: Pipeline completo (research -> escribir -> publicar)
- [ ] **Campanas de marketing**: Modelo para copy, modelo para analisis de datos, modelo para A/B tests
- [ ] **Calificacion de leads**: Workflow N8N con modelo + CRM + scoring
- [ ] **Generacion de workflows N8N**: Que modelo genera mejores flujos funcionales
- [ ] **Debugging de codigo**: Modelo + IDE (Cursor/Roo Code) + configuracion

### Por Presupuesto
- [ ] **$0/mes**: Solo modelos locales (Ollama + DGX Spark) - que instalar
- [ ] **$20/mes**: Una sola suscripcion, cual elegir
- [ ] **$50/mes**: Combo optimo de 2-3 servicios
- [ ] **$100+/mes**: Setup enterprise con fallbacks

## SEO y Comunidad

El repo es publico y debe servir como funnel para la comunidad de emprendedores en Skool.

### Pendiente
- [ ] Descripcion del repo en GitHub optimizada para SEO (keywords: AI benchmark, emprendedores, N8N, agentes)
- [ ] Topics/tags en GitHub: ai-benchmark, llm-comparison, n8n, openclaw, startup-tools, ai-agents
- [ ] README con badges (modelos testeados, ultima actualizacion, license)
- [ ] Link a la comunidad Skool en footer de README y CheatSheet
- [ ] Blog post en cristiantala.com con resultados y link al repo
- [ ] Social cards (Open Graph image) para cuando se comparta en redes
- [ ] CheatSheet PDF descargable desde el README (link directo)
- [ ] Seccion "Contributing" para que otros emprendedores agreguen tests/modelos
- [ ] Issue templates: "Agregar modelo", "Reportar resultado", "Sugerir test"
- [ ] Hacer el CheatSheet visualmente atractivo para compartir en LinkedIn

### Seguridad (repo publico)
- [x] config.py en .gitignore (API keys nunca commiteadas)
- [x] config.example.py solo tiene placeholders
- [ ] Revisar historial de git por si alguna key fue commiteada antes
- [ ] Agregar .env.example como alternativa a config.py

## Decisiones Tomadas (documentacion)

### Por que Phi-4 como juez
- Microsoft no tiene modelos en nuestro benchmark = cero conflicto de interes
- Investigacion (NeurIPS 2024): self-enhancement bias de 5-7% cuando juez y evaluado son del mismo proveedor
- MIT license = cualquiera puede replicar exactamente nuestros resultados
- 14B parametros, 3-9s por evaluacion, cabe en 24GB RAM

### Por que 4 pilares
- Razonamiento, Coding, Contenido/Marketing, Agentes/Operaciones
- Basado en las necesidades reales de un emprendedor solo (one-man army)
- Cada pilar agrupa suites relacionadas para dar un score por area
- Un emprendedor puede elegir modelo segun SU pilar mas importante

### Por que no re-usar benchmarks publicos
- LMSYS Arena mide preferencia humana en chat, no utilidad para agentes
- SWE-Bench mide coding puro, no generacion de contenido ni estrategia
- Nuestros tests simulan tareas reales: escribir blog, calificar leads, crear workflows N8N
- Medimos desde Chile (latencia real para LATAM)
- Incluimos costo por llamada en el score (critico para startups con presupuesto limitado)
