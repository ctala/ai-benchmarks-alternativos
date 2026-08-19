# Nemotron 3.5 Lightning — business_audit/atribucion_correlacion_temporal

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.41 | quality: 10.0
- latency_total: 4.404s | tokens_per_second: 383.3
- input_tokens: 243 | output_tokens: 1688
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un análisis detallado y práctico para evaluar la causalidad en el crecimiento del MRR.

## Respuesta completa

**Conclusión:** No se puede saber si la secuencia de emails fue la causante del crecimiento con los datos que compartes. Lo que ves es una correlación temporal, no una evidencia de causalidad.

**Por qué los datos no sostienen esa conclusión:**

1. **Múltiples intervenciones coinciden en el tiempo**  
   - Empezaste a pagar publicidad el 3 de marzo ($400 en el mes).  
   - Un creador grande mencionó la comunidad el 12 de marzo.  
   Ambos eventos ocurren dentro de la ventana en la que la secuencia de 5 emails también estaría activa (generalmente 1–2 semanas para una secuencia corta). No hay forma de aislar cuál de los tres impulsó los resultados.

2. **El aumento de conversiones es pequeño y sin contexto**  
   - Pasaste de 9 a 14 altas al plan pago (+5 usuarios).  
   - Eso representa apenas ~0,12% de crecimiento en MRR (aprox. $60–$75 de los $1.200 nuevos), si cada nuevo usuario paga el mismo monto promedio. El crecimiento total de MRR (+$1.200) suque que hay otras fuentes de ingresos además de esas 5 conversiones.

3. **Falta la base de usuarios y la atribución**  
   - No sabemos cuántos usuarios free había al 1 de marzo, por lo que no podemos calcular la tasa de conversión real ni ver si +5 es dentro de lo esperado, alto o bajo.  
   - No hay rastreo de fuente: ¿sabemos cuántos de esos 14 nuevos pagantes llegaron por email, por el video del creador, por el anuncio, o por búsqueda/orgánico?

4. **No hay grupo de control ni período base aislado**  
   - Para afirmar que los emails "funcionaron", deberíamos ver qué pasaba con el mismo segmento de usuarios que no recibía los emails (o un grupo holdout), o tener un período anterior comparable sin intervención.

**Qué haría falta para estar seguros:**

- **Atribución granular:** Cada nuevo pagante debe etiquetarse con su fuente de adquisición (email, anuncio, referido, orgánico, etc.).
- **Tamaño de la audiencia free:** Número de usuarios en el plan gratuito al 1 de marzo, para calcular la tasa de conversión real.
- **Test holdout o A/B:** Un grupo de usuarios free que no reciba la secuencia de emails, comparado con el que sí lo hace, manteniendo ads y menciones de creadores constantes (o medidos por separado).
- **Medición del impacto de ads y el video:** Rastrear cuánto tráfico y MRR trae cada uno durante marzo, para restarlos y ver qué queda atribuible a la secuencia.
- **Evolución temporal:** Graficar las conversiones día por día para ver si hay un pico inmediato después del envío de cada email, o si el crecimiento se alinea mejor con el 12 de marzo (video) o con el inicio de los ads (3 de marzo).

Si quieres, puedo ayudarte a diseñar un modelo de atribución básica o un test holdout con los datos que ya tengas. Lo importante es no atribuir crecimiento a un solo canal cuando tres cosas cambiaron a la vez.