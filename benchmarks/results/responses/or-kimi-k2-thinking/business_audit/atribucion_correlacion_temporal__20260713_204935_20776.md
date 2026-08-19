# Kimi K2 Thinking — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2-thinking`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 8.8s | tokens_per_second: 199.0
- input_tokens: 269 | output_tokens: 1751
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis exhaustivo y recomendaciones prácticas para futuras pruebas.

## Respuesta completa

**Conclusión: No se puede saber si la secuencia de emails funcionó.**

Con los datos que tienes, es imposible atribuir el aumento de MRR o altas específicamente a los emails. El crecimiento de marzo es **explicado por al menos tres variables que ocurrieron simultáneamente**, y no tienes forma de separar su impacto.

---

### **Problemas críticos en tu análisis:**

1. **Tres intervenciones, un resultado**: Publicidad, mención del creador y emails se activaron dentro de 11 días. Es como echar sal, pimienta y limón a un plato y preguntar cuál ingrediente lo hizo sabroso.

2. **Falta de grupo control**: No sabes qué conversiones habrías tenido *sin* emails. ¿Las 14 altas de marzo fueron 5 extra, o habrías tenido 20 con la publicidad y la mención solas?

3. **Muestra demasiado pequeña**: La diferencia es de solo 5 altas más. Con números así, el ruido aleatorio es más grande que la señal. Podría ser variación natural.

4. **No hay rastro de atribución**: No sabes si los 14 nuevos pagos llegaron desde el email, la publicidad, la mención, o boca a boca orgánico.

---

### **Qué haría falta para estar seguros:**

- **Test A/B**: Dividir usuarios gratuitos en dos grupos (uno recibe emails, otro no) y medir tasa de conversión diferencial *en el mismo período*.

- **Tracking granular por fuente:**
  - UTMs únicos en cada email
  - Código de referencia en el checkout ("¿Cómo te enteraste?")
  - Píxeles de conversión separados para anuncios vs emails

- **Datos del funnel de emails:**
  - ¿Cuántos usuarios gratuitos recibieron los emails?
  - ¿Tasa de apertura? ¿de clics? ¿de conversión desde clic?

- **Desglose temporal:**
  - ¿Qué día se produjeron cada una de las 14 altas?
  - ¿Hubo picos el 12 de marzo (mención) vs el 1-5 (emails)?

- **Encuesta a nuevos usuarios:** En el onboarding, pregunta directamente: "¿Qué te motivó principalmente a unirte?" con opciones que incluyan "Email que recibí".

---

### **Próximo paso recomendado:**

**No vuelvas a lanzar una secuencia sin un experimento controlado.** Para la próxima, selecciona una cohorte de usuarios gratuitos, divídelos aleatoriamente en dos grupos idénticos, y envía emails solo a uno. Mide la conversión diferencial durante 30 días. Esa es la única forma de saberlo con certeza.

Con los datos actuales, lo único seguro es que **marzo fue un buen mes**, pero el email es sospechoso sin coartada.