# Grok 4.20 — business_audit/atribucion_correlacion_temporal

- model_id: `x-ai/grok-4.20`
- success: True  | final: 5.32 | quality: 4.8
- latency_total: 5.715s | tokens_per_second: 107.4
- input_tokens: 399 | output_tokens: 614

## Respuesta completa

**Conclusión: No se puede saber si la secuencia de emails funcionó.**

Los datos que me diste **no permiten atribuir** el aumento de 5 altas (+56%) ni los +$1.200 de MRR a la secuencia de emails. Hay demasiada contaminación en los números.

### Por qué no se puede atribuir el resultado a los emails:

1. **Confounding fuerte (variables que se solapan en el tiempo)**:
   - 1 de marzo → Empiezas la secuencia de emails
   - 3 de marzo → Empiezas a pagar publicidad ($400)
   - 12 de marzo → Un creador grande menciona tu comunidad en un video

   Estos tres eventos ocurren en un intervalo de 11 días. Es imposible separar su efecto con los datos agregados que tienes.

2. **El aumento de 5 altas es muy pequeño** para sacar conclusiones estadísticamente confiables. Con solo 9 y 14 conversiones, el ruido es enorme.

3. **No tienes grupo de control**. No sabemos cuántas altas hubieras tenido sin enviar la secuencia.

### Lo que haría falta para estar razonablemente seguros:

Para poder atribuir causalidad necesitarías al menos:

- **Datos a nivel de usuario**: fecha exacta de alta, si recibió la secuencia o no, si venía de ads, si vio el video del creador, etc.
- **Grupo de control** (la forma más limpia):
  - Ideal: haber hecho un test A/B dividiendo la base gratuita en dos grupos el 1 de marzo (50% secuencia, 50% sin secuencia).
  - Alternativa más débil: comparar marzo vs febrero/mismo mes del año anterior, pero ajustando por el efecto del video y los ads.
- **Atribución de fuente** de las nuevas altas (aunque sea declarativa).
- **Serie temporal más larga** (al menos 2-3 meses antes y después) para ver la tendencia orgánica.
- **Costo de adquisición** por canal para entender si el incremento de MRR realmente es rentable.

### Recomendación práctica (lo que yo haría ahora):

1. **Para este mes**: Asume que **no sabes** cuál de los tres movió la aguja. No celebres todavía la secuencia.
2. **Para el próximo experimento**: 
   - Para probar emails, haz un test A/B real (mitad de la base recibe la secuencia, mitad no).
   - O al menos segmenta claramente las altas entre: "vinieron del video", "vinieron de ads" y "orgánico/email".
3. Analiza las **14 altas de marzo** una por una (aunque sea manualmente) e intenta clasificarlas en buckets: Video del creador / Ads / Email / Orgánico puro.

¿Quieres que te arme una tabla sencilla para que clasifiques esas 14 altas y poder sacar algo de señal a pesar de todo?