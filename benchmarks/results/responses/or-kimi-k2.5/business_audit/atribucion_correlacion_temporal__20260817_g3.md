# Kimi K2.5 — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 93.651s | tokens_per_second: 36.1
- input_tokens: 269 | output_tokens: 3377

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de datos de una empresa pequeña. Tu trabajo es proteger al equipo de conclusiones que los datos no sostienen. Prefieres decir 'no se puede saber' antes que dar una respuesta cómoda pero falsa.

**user:**

Tengo una comunidad de pago online. Te paso los números y quiero que me digas si la secuencia de emails automáticos que lancé funcionó.

- El 1 de marzo activé una secuencia de 5 emails para los usuarios del plan gratuito.
- MRR al 28 de febrero: $4.100
- MRR al 31 de marzo: $5.300 (+29%)
- Altas al plan pago en febrero: 9
- Altas al plan pago en marzo: 14

Contexto adicional: también el 3 de marzo empecé a pagar publicidad ($400 en el mes), y el 12 de marzo un creador con audiencia grande mencionó la comunidad en un video.

¿La secuencia de emails funcionó? Dame tu conclusión y qué haría falta para estar seguros.


## Respuesta completa

**Conclusión: No se puede saber.** 

Con los datos actuales, afirmar que funcionaron los emails sería una conjetura, no un análisis. Tienes un problema clásico de **confusión de variables**: lanzaste tres cambios importantes en menos de dos semanas (emails, publicidad, mención viral), y no tienes mecanismos para separar qué causó qué.

---

### Por qué los números no sostienen la conclusión

1. **Tres tratamientos simultáneos**: 
   - 1 marzo: Emails a gratuitos
   - 3 marzo: Publicidad pagada ($400)
   - 12 marzo: Mención de creador grande
   
   El crecimiento (de 9 a 14 altas) podría explicarse enteramente por el influencer, por la publicidad, por los emails, o por una combinación imposible de cuantificar sin datos de atribución.

2. **El tamaño de muestra es demasiado pequeño**:
   - Pasar de 9 a 14 usuarios es una diferencia de solo 5 personas.
   - Con números tan bajos, la variación aleatoria (ruido) es tan grande como la señal. Un solo usuario que se decidió "porque sí" cambia tus porcentajes dramáticamente.

3. **La matemática del MRR sugiere otras fuerzas**:
   - Las altas crecieron 55% (de 9 a 14), pero el MRR solo 29%.
   - Esto implica que o bien:
     - Hubo churn (usuarios antiguos se fueron), o
     - Los nuevos usuarios compraron planes más baratos que los anteriores, o
     - Hubo downgrades.
   - Sin saber el churn, ni siquiera puedes calcular el valor real de esas 14 altas, menos atribuirlas.

4. **No sabes quién vino de dónde**:
   - ¿Cuántos de esos 14 usuarios mencionaron el video del creador?
   - ¿Cuántos llegaron por el anuncio pagado?
   - ¿Cuántos dijeron "me convenció la secuencia de emails"?
   - Sin esta segmentación, estás asumiendo que porque A pasó y luego B pasó, A causó B (falacia *post hoc*).

---

### Qué haría falta para estar seguros

Para poder atribuir el crecimiento a los emails específicamente, necesitarías:

**1. Atribución directa (lo más urgente)**
- Preguntar a esos 14 usuarios en el proceso de onboarding: "¿Qué te hizo decidirte a pagar?" (encuesta obligatoria).
- Revisar los UTM o parámetros de tracking: ¿cuántos clickearon directamente desde los emails vs. desde el video vs. desde los anuncios?

**2. Un grupo de control (para la próxima vez)**
- No enviar los emails a una porción aleatoria de los usuarios gratuitos (ej. 50% recibe emails, 50% no) y comparar tasas de conversión entre ambos grupos. Con tus volúmenes actuales, esto requeriría esperar 2-3 meses para tener significancia estadística.

**3. Métricas del embudo de emails**
- Open rate de la secuencia.
- Click-through rate en los links de pago.
- Conversion rate específico de esa fuente (no solo "altas totales").

**4. Test secuencial, no simultáneo**
- La próxima vez, no lances todo en el mismo mes. 
- Mes 1: Solo emails (sin publicidad ni influencers).
- Mes 2: Solo publicidad.
- Así estableces una línea base comparativa.

**5. Análisis de cohortes**
- Ver si los usuarios que se registraron *antes* del 1 de marzo (y recibieron los emails) tienen mayor tasa de conversión que los usuarios de febrero (que no los recibieron).

---

### Mi recomendación práctica

**No tomes decisiones de inversión basadas en estos datos.** No dupliques la frecuencia de emails ni los suspendas todavía. 

Lo que sí puedes hacer ahora:
1. **Encuesta a esos 14 usuarios** (y a los 9 de febrero como grupo de control retrospectivo) preguntando qué los convenció.
2. **Revisar tus logs**: Si usas Stripe, Memberful o similar, revisa si los usuarios de marzo tienen códigos de cupón específicos de la mención del influencer o parámetros UTM de los anuncios.
3. **Esperar**: Con $400 en publicidad y una mención viral, marzo fue un mes anómalo. Necesitas ver los números de abril (sin la mención del influencer) para empezar a aislar efectos.

Si tras la encuesta descubres que 10 de los 14 mencionaron el video del creador, entonces sabrás que los emails probablemente no fueron el driver principal. Si 8 dicen "los emails me recordaron que existía la comunidad", entonces sí funcionaron. Pero ahora mismo, **estás ciego**.