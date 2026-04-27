---
titulo: Cómo decidir qué modelo poner en producción
dificultad: Intermedio
tiempo_estimado: 30 min de lectura + 1-2 horas de validación
costo_estimado: Menos de $2 USD para validación final
requisitos_previos:
  - Idealmente tutoriales 01 a 04 completados
  - Tener identificado tu caso de uso real
  - Saber tu volumen estimado mensual de calls
---

# Cómo decidir qué modelo poner en producción

## Para qué sirve este tutorial

Este es el tutorial que **importa más que todos los demás juntos**. Los anteriores te enseñan a generar datos. Este te enseña a **decidir con esos datos**.

La trampa: hay 80+ modelos en el config. Si elegís por "el más popular" o "el que dijo Twitter", probablemente vas a pagar 10× lo que necesitás, o vas a poner un modelo que falla en tu caso pero brilla en benchmarks académicos.

## Lo que vas a tener al final

- Un framework de 7 dimensiones para decidir.
- Una lista corta (2-3 finalistas) para tu caso específico.
- Resultados de validación final contra esos finalistas.
- La decisión tomada, con criterio justificable a futuro.

## Filosofía: NO hay modelo mejor universal

Cualquier persona o blog que te diga "el mejor modelo es X" o **te está vendiendo algo** o **no entendió la pregunta**.

El "mejor" depende de:

```
mejor_para_vos = f(
    tarea_específica,
    volumen_calls,
    latencia_tolerada,
    privacidad_data,
    licencia,
    hardware,
    idioma
)
```

Cambiá uno solo de esos parámetros y el ganador puede ser otro completamente distinto.

## El framework de las 7 dimensiones

Antes de mirar ningún ranking, respondete estas 7 preguntas. Sé específico. "Coding" o "contenido" no alcanza.

### 1. Tarea específica

**Mal**: "necesito un modelo de coding".
**Bien**: "necesito generar templates de N8N en JSON para automatizar emails de marketing, max 200 líneas por workflow".

**Mal**: "para hacer contenido".
**Bien**: "blog posts en español neutro de 800-1200 palabras sobre startups LATAM, voz casual pero informada, con datos concretos".

Cuanto más específico, más fácil filtrar.

### 2. Volumen calls/mes

| Volumen | Implicación |
|---------|-------------|
| <100 calls/mes | Cualquier modelo, hasta los premium. |
| 1.000 - 5.000 | Tier cheap es lo razonable, premium solo si la tarea lo justifica. |
| 10.000+ | Tier ultra_cheap o cheap obligatorio. Premium = $$$ insostenible. |
| 100.000+ | Considerá local + DGX/Mac Studio para amortizar hardware. |

Calculá tu volumen real. Si tenés N8N corriendo workflows automáticos, multiplicá por usuarios.

### 3. Latencia tolerada

| Caso | Latencia tolerable |
|------|---------------------|
| Chat sincrónico al usuario final | <2 seg first token, <8 seg total |
| Workflow N8N que el usuario espera | <15 seg |
| Batch nocturno (newsletter, reports) | Puede tardar minutos |
| Generación de embeddings masivos | Cualquiera, es batch |

Cuanto más sincrónico, más importa **tokens/segundo**, no solo el score.

### 4. Privacidad de datos

| Tipo de data | Recomendación |
|--------------|---------------|
| Públicos / marketing | Cualquier provider. |
| PII de clientes (emails, nombres) | Provider con DPA firmado, idealmente en LATAM o EU. |
| Datos de salud, legal sensible | Local obligatorio. Ollama + DGX o Mac Studio. |
| IP de tu empresa | Mínimamente provider con no-training clause. OpenAI Enterprise o Claude. |

Si algo de esto aplica, **NO uses modelos free de OpenRouter** — esos tienen training-on-input habilitado.

### 5. Restricción de licencia

| Necesidad | Filtro |
|-----------|--------|
| Open source obligatorio (regulación, gobierno) | Apache 2.0 / MIT / Llama license. Ver flag `open_source: True` en config. |
| Open weights deseable, no obligatorio | Mismo filtro pero con propietarios como backup. |
| Sin restricción | Todo el universo. |

⚠️ Trampa común: "Qwen 3.6 Plus" suena open source porque la familia Qwen base lo es, pero **el Plus es propietario API-only**. Verificá siempre.

### 6. Hardware disponible

Solo importa si querés correr local.

| Hardware | Modelos viables |
|----------|-----------------|
| MacBook M1 16 GB | Modelos hasta 8B (Llama 3.1 8B, Phi-4, Gemma 2 9B). |
| MacBook M2/M3 32 GB | Hasta 32B con cuantización. Devstral Small Q4 va bien. |
| Mac Studio / PC con 64 GB | Modelos 70B con cuantización. |
| DGX Spark 128 GB / RTX 4090 + RAM | Modelos hasta 200B cuantizados. |
| Sin hardware potente | Cloud APIs only, o Ollama Cloud. |

### 7. Idioma principal

| Idioma | Filtro |
|--------|--------|
| Español neutro / LATAM | Qwen 3.5+, DeepSeek V3+, Gemini Flash, Mistral Small 4. Evitar modelos solo entrenados en inglés (Llama 2, Phi-3 chico). |
| Español rioplatense | Probar específicamente con tus tests — varía mucho. |
| Multilingüe (es + en) | Gemini, Claude, GPT-4.1 son fuertes en switching. |
| Solo inglés | Universo completo. |

## Caso ejemplo concreto

**Perfil**: emprendedora chilena, tiene un SaaS de gestión de clientes para coaches. Usa N8N para automatizar:
- Email de bienvenida cuando alguien se registra.
- Resumen semanal de actividad del coach.
- Resúmenes de sesiones a partir de transcripciones (~500 palabras → 150).

**Las 7 dimensiones**:

1. **Tarea**: 3 sub-tareas distintas (email marketing, summarization, structured content). Probablemente necesita 1-2 modelos, no uno solo.
2. **Volumen**: ~3.000 emails/mes + 300 resúmenes semanales + 800 sesiones/mes = ~5.500 calls/mes.
3. **Latencia**: emails y reports → batch, OK 30+ seg. Resúmenes de sesión → mejor <10 seg porque el coach lo espera.
4. **Privacidad**: PII de clientes (nombres, emails). Necesita provider con DPA. Idealmente no-training.
5. **Licencia**: no hay regulación, propietario aceptable.
6. **Hardware**: MacBook normal, no tiene servidor.
7. **Idioma**: español neutro 100%.

**Conclusión**: dos modelos en producción.

- Para emails y reports (asincrónico): **DeepSeek V3.2** ($0.14/$0.28, score contenido 7.0+, español sólido). Costo estimado: ~$3/mes.
- Para resúmenes con baja latencia: **Gemini 2.5 Flash Lite** (165 tok/s, $0.075/$0.30, multilingüe robusto). Costo estimado: ~$2/mes.

Total: $5-8/mes. Premium hubiera sido $80+/mes para igual calidad funcional.

## Paso 1 — Definí tus 7 dimensiones

Tomate 15 minutos y escribí tu caso real, dimensión por dimensión, en un .md o un papel. Sin esto el resto del tutorial no funciona.

## Paso 2 — Usá la calculadora web

Andá a **<https://benchmarks.cristiantala.com/>** y filtrá:

- Por tarea (selector de pillar: razonamiento / coding / contenido / agentes)
- Por presupuesto mensual estimado (con tu volumen calculado)
- Por open source sí/no
- Por idioma

La calculadora consume `docs/data/models.json` (el que regeneraste en el tutorial 02). Te devuelve un ranking ordenado para **tu** combinación.

## Paso 3 — Quedate con 2-3 finalistas

No 1, no 5. **2 o 3 finalistas**. Razones:

- Con 1 te casás con un proveedor sin contraste.
- Con 5+ no tenés tiempo de validar bien.
- Con 2-3 podés correr validación seria + tener un backup.

## Paso 4 — Validación final con tus prompts reales

Acá es donde la mayoría se traba. **No confíes en el ranking del benchmark para la decisión final**. El benchmark mide bien, pero nunca capturó EXACTAMENTE tu caso.

Hacé esto:

a) Junta **5-10 prompts reales** de tu caso, con outputs ideales que vos ya escribiste o que sabés cómo querés que sean.

b) Crealo como un test custom (tutorial 03) o simplemente probalos a mano:

```bash
# Para probar a mano contra OpenRouter:
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek/deepseek-chat",
    "messages": [{"role":"user","content":"TU PROMPT REAL ACA"}]
  }'
```

c) Corré los 5-10 prompts × 2-3 finalistas = 10-30 ejecuciones. Costo: <$2 USD.

d) **Leé las respuestas con ojo crítico**. Para cada una preguntate:
- ¿Refleja la voz que querés?
- ¿Tiene la longitud correcta?
- ¿Necesita post-procesamiento? (cuanto más, peor)
- ¿Cometé errores factuales graves?

## Paso 5 — Decidí

Después de la validación vas a tener **un ganador claro**, o un empate técnico entre dos.

### Si hay ganador claro

Implementalo en producción. Anotá la decisión con su justificación en un `decisions.md` interno. Vas a agradecer ese log dentro de 6 meses cuando aparezca un modelo nuevo y no te acuerdes por qué elegiste el actual.

### Si hay empate técnico

Desempatá por:

1. **Costo** (a igual calidad, el barato gana).
2. **Velocidad** (a igual costo, el rápido gana).
3. **Estabilidad del provider** (Groq, OpenAI, Anthropic > providers nuevos).
4. **Open source** (si te importa la portabilidad a futuro).

## Paso 6 — Configurá el monitoring

En producción:

- Loggeá latencia y costo de cada call (N8N permite esto fácil).
- Cada 30 días corré los 5-10 prompts canónicos contra el modelo elegido + 2 alternativos (con tu config y `runner.py`).
- Si algún alternativo te supera consistentemente, considerá el switch.
- Si tu modelo elegido empieza a fallar (silent retraining, cambio de pricing), tenés el backup ya validado.

## Anti-patterns (lo que NO hacer)

### "Voy a usar el modelo más nuevo porque salió esta semana"

Mal. Los modelos nuevos pueden tener bugs, providers inestables, o ser variantes que cambian rápido. Esperá 2-4 semanas y mirá los runs del benchmark antes de moverte.

### "Confío en el marketing del proveedor"

Anthropic dice que Claude Opus es el mejor en razonamiento. Es verdad — para algunos tipos de razonamiento. Para tu caso específico (emails LATAM, copy de marketing) es overkill caro. **Siempre validá**.

### "Voy con el más popular en Twitter / Reddit"

La popularidad mide hype, no fit con tu caso. Llama 3.3 70B es popular y es excelente para tool calling, pero terrible para coding complejo. Cada modelo brilla en algo y falla en otra cosa.

### "Voy a usar Claude Opus para todo"

Es excelente, pero a $15/$75 por M tokens, 5.000 calls/mes te puede costar $50-150/mes. Si Devstral Small ($0.10/$0.30) hace tu tarea con 80% de la calidad, **estás pagando 50× para ganar 20%**. La mayoría de las veces no lo justifica.

### "Probé 1 prompt y me convenció"

Cuidado. Los modelos varían bastante por prompt. Validá con **mínimo 5 prompts diversos** antes de decidir.

### "Cambio cada vez que sale algo nuevo"

Ineficiente. Cambiar de modelo en producción tiene costo de switching: re-ajustar prompts, monitorear regresiones, retrainear a tu equipo. Cambiá solo si el delta es claro y >15% mejor en tu validación.

## Recursos del repo para profundizar

- `MODELOS.md` — tabla de todos los modelos con scores actuales.
- `RECOMENDACIONES.md` — guía por plataforma (N8N, OpenClaw), tarea y presupuesto.
- `AGENTS.md` — el archivo que tu propio agente IA puede leer para auto-recomendar.
- `CASOS_DE_USO.md` — ejemplos resueltos similares al tuyo.
- `SUSCRIPCIONES.md` — análisis costo-eficiencia de planes (Pro $20, Enterprise, etc).
- `cheatsheet/` — referencias rápidas por categoría.

## Próximos pasos

Cerraste el ciclo. De acá podés:

- **Iterar tu suite custom** (tutorial 03) cada vez que cambia tu caso de uso.
- **Re-correr el benchmark mensualmente** con los 3-4 candidatos top, para detectar drift.
- **Compartir tus resultados**: si descubriste algo interesante (un modelo poco conocido que es bueno para X), abrí un PR al repo con tu suite y resultados — beneficiás a otros emprendedores LATAM.

Y la regla cardinal: **medí antes de elegir**. Siempre.
