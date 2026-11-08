# Qwen 3.6 35B base (OpenRouter FP8) — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 4.54 | quality: 4.0
- latency_total: 45.709s | tokens_per_second: 103.0
- input_tokens: 193 | output_tokens: 4707

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa



Aquí tienes el teardown estructurado bajo tu requisito: **cada afirmación está etiquetada como `[CONOCIDO]` o `[INFERIDO]`, y se marca su nivel de certeza (`ALTA / MEDIA / BAJA`).** No se presenta ningún dato interno como hecho.

---
### 📌 Nota metodológica
Los cálculos de facturación y salud son **modelos basados en benchmarks de la industria** (comunidades de membresía + cursos digitales). La certeza baja/media indica que los resultados cambian drásticamente según churn real, tasa de conversión, políticas de reembolso y estructura de costos interna.

---
## 💰 Estimación de facturación

| Afirmación | Origen | Certeza |
|------------|--------|---------|
| Precio visible: $39/mes | `[CONOCIDO]` | ALTA |
| Miembros declarados en portada: 2.400 | `[CONOCIDO]` | ALTA |
| No se observa plan anual ni descuentos | `[CONOCIDO]` | ALTA |
| Tasa de churn mensual típica en este modelo: 5-10% | `[INFERIDO]` (benchmark de comunidades + cursos) | MEDIA |
| Miembros activos/pagando reales: 60-80% de los declarados | `[INFERIDO]` (trial, inactivos, inflados por marketing, retención histórica) | BAJA |
| MRR estimado: ~$70.000-$85.000 → ARR: ~$840.000-$1.020.000 | `[INFERIDO]` (1.800-2.175 activos × $39 × 12) | BAJA |
| Ingresos por cursos (12 listados): $10k-$30k/mes promedio | `[INFERIDO]` (asume precio $297-$497, conversión 15-25%, ventas escalonadas) | BAJA |
| Ingreso total mensual estimado: ~$80k-$115k | `[INFERIDO]` (MRR + curso promedio) | BAJA |

**Lectura:** Si el modelo es correcto, facturan en el rango de **$850k-$1.1M ARR**. Sin embargo, la incertidumbre en miembros activos y churn hace que la cifra real pueda estar un 30-40% por debajo o por encima.

---

## 🏥 Salud del negocio

| Indicador | Origen | Certeza |
|-----------|--------|---------|
| Cadencia de contenido: 3 posts/semana en feed público | `[CONOCIDO]` | ALTA |
| Autoridad del fundador: 60k seguidores en 1 red | `[CONOCIDO]` | ALTA |
| Biblioteca de cursos: 12 listados, estado de finalización desconocido | `[CONOCIDO]` | ALTA |
| Ausencia de plan anual visible | `[CONOCIDO]` | ALTA |
| Riesgo de churn elevado por precio mensual puro | `[INFERIDO]` (la fricción de renovación mensual suele disparar churn en >8%) | MEDIA |
| Calidad/actualización de cursos no validable públicamente | `[INFERIDO]` (sin fechas de actualización, completados o reseñas visibles) | MEDIA |
| Engagement real de la comunidad no medible desde fuera | `[INFERIDO]` (posts públicos ≠ interacción interna, uso de herramientas, o actividad en chat) | BAJA |
| Concentración de tráfico en 1 red social | `[INFERIDO]` (60k seguidores en un solo canal sugiere dependencia de un algoritmo) | MEDIA |
| Escala vs. sostenibilidad operativa | `[INFERIDO]` (12 cursos + comunidad activa requiere soporte, moderación y actualizaciones constantes) | MEDIA |

**Diagnóstico de salud:** 
- **Puntos fuertes:** Modelo escalable, presencia de contenido consistente, autoridad de fundador, precio accesible.
- **Vulnerabilidades:** Retención frágil (sin plan anual), posible estancamiento de cursos, tráfico concentrado, y falta de señales públicas de outcomes o engagement real.
- **Certeza general del diagnóstico:** MEDIA (la salud real depende de métricas internas no visibles).

---

## 🎯 Cómo competir (palancas accionables)

| Palanca | Base lógica | Certeza |
|---------|-------------|---------|
| **1. Pricing con plan anual** | Ofrecer $349-$399/año reduce churn, mejora LTV y alinea incentivos. | MEDIA |
| **2. Comunidad activa vs. feed pasivo** | Diferenciarse con workflows, accountability, office hours, plantillas descargables y espacios por stack/herramienta. | MEDIA |
| **3. Nicho o stack específico** | "Automatización" es genérico. Especializarse en Make/n8n/Zapier + IA, o en industrias concretas (ecom, SaaS, agencias). | MEDIA |
| **4. Transparencia de resultados** | Mostrar tasas de completado de cursos, casos con métricas (horas ahorradas, ROI), y política de reembolso clara. | MEDIA |
| **5. Diversificar fuentes de tráfico** | Reducir dependencia del fundador: SEO técnico, partnerships con creadores de herramientas, webinars, newsletter con lead magnet funcional. | MEDIA |
| **6. Modelo de producto híbrido** | Mantener comunidad como core, pero estructurar cursos como "actualización continua" o "certificaciones por módulo", no como productos estáticos. | MEDIA |

**Estrategia de entrada recomendada:** 
Atacar donde tienen mayor incertidumbre pública: **retención, calidad validable y enfoque de nicho**. Si tu propuesta muestra flujos automatizados listos para copiar, comunidad con accountability real, y un plan anual que reduzca fricción de pago, capturarás churn natural y buscadores de resultados medibles.

---

## 🔍 Qué verificar para subir certeza (de BAJA/MEDIA a ALTA)

| Dato a verificar | Método | Impacto en certeza |
|------------------|--------|-------------------|
| Miembros activos reales y churn | Prueba de compra (funnel, onboarding, política de cancelación), análisis de reseñas, o contactar a miembros actuales | ALTA → BAJA |
| Precios y completados de los 12 cursos | Buscar en marketplaces, afiliados, o comprar 1-2 para evaluar estructura, actualizaciones y soporte | MEDIA → ALTA |
| Fuentes de tráfico y conversión | SimilarWeb, Social Blade, análisis de links en bio, campañas de ads (Facebook Ad Library) | MEDIA → ALTA |
| Tasa de engagement interna | Participar como miembro trial, medir respuestas en chat, uso de herramientas, asistencia a eventos | BAJA → MEDIA |
| Costos operativos y márgenes | No accesible públicamente. Requiere benchmark de plataformas (Circle, Skool, Kajabi) + volumen de soporte | BAJA (limitado) |

---
### ✅ Resumen ejecutivo
- **Facturación estimada:** $850k-$1.1M ARR (certeza: BAJA, depende de miembros activos y churn).
- **Salud:** Escala media-alta con vulnerabilidades en retención, diversificación de tráfico y validación de outcomes (certeza: MEDIA).
- **Cómo competir:** Pricing anual, comunidad orientada a resultados medibles, nicho/stack específico, transparencia de completados/casos, y tráfico diversificado fuera del fundador.
- **Próximo paso:** Verificar 3-4 métricas internas clave para ajustar el modelo de facturación y priorizar palancas con mayor probabilidad de impacto.

Si me compartes datos adicionales (fuente de tráfico visible, tipo de plataforma de membresía, o si los cursos tienen precios públicos), puedo refinar los cálculos y elevar la certeza de las inferencias.