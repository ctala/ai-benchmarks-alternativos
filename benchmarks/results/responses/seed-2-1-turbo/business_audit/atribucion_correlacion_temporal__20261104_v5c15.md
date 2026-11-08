# Seed 2.1 Turbo — business_audit/atribucion_correlacion_temporal

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 91.767s | tokens_per_second: 64.2
- input_tokens: 275 | output_tokens: 5887

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

### Conclusión principal: No se puede saber si la secuencia de emails funcionó.
Los datos que compartes no permiten atribuirle el aumento de MRR o de altas, porque hay múltiples factores en juego y no hay forma de separar su impacto. Afirmar que funcionó (o que no) sería una conclusión que los datos no sostienen.

---

### Por qué no se puede saber, con tus datos específicos:
1. **Hay otras dos acciones que también generan altas en el mismo período**  
   Empezaste a pagar publicidad el 3 de marzo y un creador mencionó la comunidad el 12. Ambas pueden explicar todo o parte del aumento:
   - La publicidad puede haber traído usuarios nuevos al plan gratuito que luego se pasaron a pago.
   - La mención del creador puede haber generado altas directas al plan pago, o usuarios muy cálidos que se pasaron rápido del gratuito al pago.
   Con totales mensuales no hay forma de saber cuánto correspondió a cada acción.

2. **No tienes un grupo de comparación (control)**  
   La secuencia se la mandaste a todos los usuarios del plan gratuito, así que no tienes un grupo de usuarios iguales que no la hayan recibido para ver si su tasa de conversión fue menor. Sin eso, no puedes descartar que el aumento se deba a cualquier otro factor (ej: estacionalidad, noticias del rubro, etc.).

3. **No sabes de dónde vinieron las altas de marzo**  
   No tienes desagregación de si las 14 altas vinieron de:
   - Usuarios que ya eran gratuitos *antes del 1 de marzo* (que serían los únicos que podríamos ligar mínimamente a la secuencia, ya que no llegaron por las acciones de marzo).
   - Usuarios nuevos que entraron al gratuito en marzo por publicidad o la mención del creador.

4. **El MRR depende de más variables que solo las altas**  
   El aumento de $1.200 de MRR no se explica solo por las 5 altas extra (de 9 a 14). También influyen las bajas (churn) de clientes pagos, los cambios de plan (upgrades/downgrades) o aumentos de precio. No tienes datos de eso, así que ni siquiera podemos confirmar que el aumento de MRR se deba al aumento de altas.

5. **No hay contexto de tendencia anterior**  
   No sabemos si el aumento de altas es parte de una tendencia que ya venías teniendo (ej: si en enero hubo 7 altas, febrero 9, marzo 14: la tendencia ya era de crecimiento, y la secuencia no cambió nada) o si es estacional (incluso los 3 días extra de marzo respecto a febrero explican un aumento esperado de ~11% de altas, sin contar otras variables).

---

### Qué haría falta para estar seguros:
Separado en dos niveles:
#### 1. Análisis retrospectivo (da indicios, no certeza, con datos que probablemente ya tienes)
Para acercarte a una respuesta sin experimentos, revisa estos datos:
- **Desagrega las altas por fecha de registro en el gratuito**: Cuenta cuántas de las 14 altas de marzo corresponden a usuarios que se registraron *antes del 1 de marzo*. Si la mayoría son de estos usuarios, hay más indicios de que la secuencia pudo ayudar; si la mayoría son de usuarios nuevos de marzo, el aumento se explica más por publicidad o el creador.
- **Mira la evolución diaria/semanal de las altas**: ¿Hubo un pico justo después del 12 de marzo (cuando salió el video del creador)? Si es así, esa acción explica gran parte del aumento. ¿Las altas se distribuyeron de forma gradual desde el 1 de marzo, como lo esperarías de una secuencia de emails?
- **Usa datos de atribución**: ¿Tienes tracking de clicks en los emails de la secuencia? Cuenta cuántas altas vinieron de esos enlaces (no es perfecto, porque alguien puede ver el email y luego entrar por otro canal, pero te da una referencia). ¿Sabes cuántas altas vinieron de los enlaces de la publicidad o del video?
- **Compara con la tendencia anterior**: Revisa las altas de los 2-3 meses previos a marzo para ver si venías creciendo a un ritmo similar.
- **Controla por el churn**: Revisa cuántas bajas hubo en febrero y marzo. Si en marzo hubo muchas menos bajas, parte del aumento de MRR se debe a eso, no a las altas.

#### 2. Experimento controlado (única forma de tener certeza)
Para confirmar sin dudas si la secuencia funciona, haz un **test A/B con asignación aleatoria**:
1. Divide a los usuarios nuevos que se registran en el plan gratuito en dos grupos completamente aleatorios (así son iguales en origen, interés, etc.):
   - **Grupo control**: No recibe la secuencia de emails (o recibe la secuencia que usabas antes, si la había).
   - **Grupo tratamiento**: Recibe la nueva secuencia de 5 emails.
2. Medir la tasa de conversión a plan pago de ambos grupos durante un período suficiente (ej: 30 días, para dar tiempo a que termine la secuencia y los usuarios decidan contratar).
3. Si la diferencia de conversión entre ambos grupos es estadísticamente significativa (es decir, es muy improbable que sea por azar), entonces sí puedes afirmar que la secuencia funciona (o no, si no hay diferencia).