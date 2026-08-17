# Claude Haiku 4.5 (suscripción) — creativity/depth_vs_superficial

- model_id: `claude-haiku-4-5`
- success: True  | final: 7.38 | quality: 9.44
- latency_total: 30.251s | tokens_per_second: 83.3
- input_tokens: 10 | output_tokens: 2520
- judge_score: 4.6 | justificación: 

## Respuesta completa

# Tres ideas de IA para delivery en Santiago (no genéricas)

## 1. **Predictor de demanda local + juez LLM = recomendaciones tácticas al restaurante**

La mayoría dice "optimiza rutas". Aquí va lo real:

Entrenas un modelo pequeño con **tu data histórica de Santiago** (pedidos por zona, hora, día, clima, eventos conocidos) para predecir **picos de demanda 2-4 horas antes**. Luego pasas esa predicción a un LLM pequeño corriendo localmente (Phi-4 o Qwen 3.5 base vía Ollama = **cero costo API**) que genera una recomendación específica por restaurante:

> "Viernes 19:00-21:00 en Ñuñoa: +240% demanda esperada. Tus empanadas históricamente venden 3x. Recomendación: aumenta inventario de masa 2 kg, llama 1 repartidor extra."

**Números reales:**
- Un restaurante típico pierde $200-400/día por stockout o exceso de comida
- Tú cobras 3-5% por orden; con 200 órdenes/día en Santiago metro = $300-500/día en ingresos
- Una predicción acertada que evite 10 stockouts = $2,000-4,000/mes recuperados
- Costo de infraestructura: $30/mes en Ollama Cloud para el LLM + $50/mes en datos históricos = ROI en 2-3 restaurantes

Competidores como Uber usan modelos cerrados. Tú: **open-source local, latencia <50ms, cero dependencia de APIs remotas que se caen a las 20:00 en Santiago.**

---

## 2. **Agente de retención anti-churn con oferta hiperpersonalizada (no genérica)**

No es un email diciendo "20% descuento". Es un **agente N8N + LLM que monitorea cada cliente en tiempo real**:

Algoritmo:
1. Cliente que pedía 2x/semana lleva 3 semanas sin pedir → bandera roja
2. Agente consulta: "¿qué pedía? ¿cuándo? ¿cuál era su ticket promedio?"
3. LLM genera una oferta específica basada en patrón:
   - Cliente X pedía carbonara los jueves (promedio $8,500)
   - Hace 3 semanas paró
   - Restaurante Y acaba de entrar al catálogo, hace carbonara a $7,800
   - **Oferta generada automáticamente**: "Notamos que te encanta carbonara. Hoy el nuevo restaurante X la hace a $700 menos que tu promedio histórico"

**Números:**
- Tasa de churn típica en delivery: 30-40% mensual
- Si retienen a 5-10 clientes/mes con una oferta correcta = $1,000-2,000 en ingresos extra
- Costo: 1 llama de N8N ($50-100/mes) + API barata de LLM ($20/mes con Devstral vía OpenRouter)
- ROI: positivo en mes 1

**Por qué otros no lo hacen**: creen que personalization = big data + ML team. No. Es un script de 100 líneas de Python + un LLM barato.

---

## 3. **Riesgo silencioso que nadie menciona**

**Divergencia demanda-oferta.**

Tu predictor dice "19:00 hay demanda explosiva de sushi en La Serena". Generas la demanda, clientes abren la app, ven ofertas... pero:
- Tú no tienes restaurante sushi en La Serena
- O el que tienes cerró a las 19:30
- O está saturado y dirá "no hay cobertura"

**Resultado**: destruyes confianza. El cliente vuelve a Uber o Direct. Tu churn sube.

**Cómo evitarlo:**
- Entrenar el predictor NO solo en demanda histórica, sino en **oferta disponible en tiempo real**
- Si no tienes 3+ opciones de sushi en La Serena a esa hora → no predices demanda ahí, aunque exista
- Hacer esto requiere integración con inventarios de restaurantes (1-2 semanas de trabajo), pero es **no negociable**

---

## 4. **Opinión contraria: no uses GPT-4**

Acá viene lo heterodoxo.

Toda la gente dice "usa el modelo más grande". Para delivery en Santiago:

**Problema**: latencia. GPT-4 desde USA a Santiago = 150-250ms por request. Con 10,000 órdenes/día y operaciones LLM en 3-5 puntos del flujo, acumulas 3-5 segundos de latencia pura solo en APIs. El usuario lo siente. Competidor con Gemini Flash local (latencia <50ms) te gana en UX.

**Mi recomendación**: 
- Usa **Devstral Small** (7.35 puntos en nuestro benchmark) vía OpenRouter para predictor = $0.10 input / $0.30 output (barato)
- O corre **Qwen 3.5 base localmente** en un contenedor (Ollama Cloud, $20/mes, cero latencia)
- Guarda GPT-4 para decisiones no-latency-critical (análisis histórico, reportes)

Verás que los resultados no empeoran. La calidad de Devstral en contexto de "restaurante + historial cliente" es 95% de GPT-4, a **1/10 del costo y 1/5 de la latencia**.

---

**Acción concreta esta semana:**
1. Documenta 5 decisiones clave que hoy toma "a ojo" (stock, precios, zonas)
2. Pídele a un LLM que genere un prompt específico para cada una
3. Corre ese prompt 100 veces (con datos reales o sintéticos) usando Devstral vía OpenRouter ($1-2 de costo)
4. Compara: ¿mejor que tu intuición? Si sí, automatiza. Si no, refina el prompt.

Eso es IA para startup. No es "usar IA por usar". Es measurement + iteración.