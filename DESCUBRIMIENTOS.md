# Descubrimientos y Observaciones

> Hallazgos no obvios descubiertos durante los benchmarks. Actualizado cada edicion.

## Abril 2026

### Comportamiento de Modelos

- **MiniMax y Qwen a veces responden en chino**: Tanto MiniMax M2.7 como Qwen 3.6 Plus ocasionalmente incluyen caracteres chinos en sus respuestas en espanol. Esto ocurre mas frecuentemente en tareas de razonamiento y menos en content generation.

- **GPT-4.1 supera consistentemente a GPT-5.4**: En TODAS las categorias de nuestros tests, GPT-4.1 (varias generaciones atras) rinde mejor que GPT-5.4. Esto podria deberse a que GPT-5.4 esta optimizado para tareas de agente de larga duracion y no para respuestas puntuales como nuestros tests.

- **GPT-5.4 Mini gana a GPT-5.4**: El modelo "mini" supera al modelo completo en todas las categorias. OpenAI parece haber optimizado el mini para respuestas mas directas.

- **Claude Opus es #9 global y #3 en Agentes**: Con los tests de alucinaciones y creatividad, Opus sube de #13 a #9. Sonnet sube a #7 gracias a ser #1 en honestidad (7.62). Donde Claude realmente brilla es en tareas que requieren empatia, protocolos de seguridad y juicio situacional.

- **Devstral Small es la sorpresa del benchmark**: Un modelo de Mistral que cuesta $0.10/$0.30 per M tokens y es open-source (Apache 2.0) lidera en 5 de 6 categorias agrupadas. Su debilidad: customer support (#1 pero otros le pisan los talones).

### Problemas Tecnicos

- **Gemma 4 via OpenRouter es muy lento**: 11-19 tok/s con rate limits frecuentes (429). Mejor correrlo local en DGX Spark.

- **MiniMax Coding Plan no incluye TTS**: El Token Plan (Coding) no da acceso a Speech-02. Se necesita el plan Agent ($19/$69) para TTS.

- **GPT-5.4 usa max_completion_tokens**: No acepta el parametro standard max_tokens. Requiere max_completion_tokens.

- **Qwen 3.6 Plus :free fue deprecado**: La version gratuita en OpenRouter fue removida. Solo la version pagada funciona.

- **Ningun modelo copia strings perfectamente**: En el test de string_precision, ningun modelo logro 10/10 en ningun test. Devstral fue el mejor (8.58) y Claude Opus el peor (7.47). Claude falla especificamente en write_config_file (escribir credenciales en archivos .env).

- **Kimi K2 y Mistral Large no sirven para articulos largos**: 100% timeout en news_seo_writing. No pueden generar articulos de 1500+ palabras sin cortarse.

- **DeepSeek V3.2 es el mejor para noticias SEO**: #1 en news_seo_writing (7.67), ideal para el workflow de ecosistemastartup.com que actualmente usa Claude Sonnet.

### Sobre el Scoring

- **[CORREGIDO en v1.3.0] El scoring favorecia formato sobre sustancia**: Modelos que producen respuestas bien estructuradas (headers, listas, longitud adecuada) obtenian scores altos aunque el contenido sea generico. Formato valia 3/10 puntos (30% de calidad). Ahora vale 2/10 (20%) y se valida contenido real con score_expected_answer (60% del score de calidad cuando hay expected_answer). Ver CHANGELOG para detalles.

- **La latencia desde Chile penaliza a modelos lentos**: Qwen 3.6 Plus tiene 83s de latencia promedio, lo que baja su score significativamente vs Gemini Flash Lite con 4.7s.

- **El costo impacta el ranking**: Con 15% de peso, modelos caros como Claude Opus ($0.00417/call) bajan vs modelos baratos como DeepSeek ($0.00024/call).

### Recomendaciones Basadas en Descubrimientos

1. **Para espanol puro sin caracteres chinos**: Usa GPT-4.1, Claude, o Devstral. Evita MiniMax y Qwen para contenido editorial en espanol.

2. **Para agentes N8N que necesitan funcionar 24/7**: DeepSeek V3.2 o Devstral por costo y disponibilidad. MiniMax con suscripcion fija si prefieres predecibilidad.

3. **Para tareas que requieren juicio y empatia**: Claude Opus o Sonnet. Paga el premium por la calidad en customer support.

4. **Para volumen alto y velocidad**: Gemini 2.5 Flash Lite (212 tok/s) o Devstral (171 tok/s).
