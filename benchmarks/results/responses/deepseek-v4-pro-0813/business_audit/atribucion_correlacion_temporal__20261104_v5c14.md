# DeepSeek V4 Pro (0813) — business_audit/atribucion_correlacion_temporal

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 162.548s | tokens_per_second: 58.1
- input_tokens: 314 | output_tokens: 9444

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

Mi conclusión honesta: **no se puede saber si la secuencia de emails funcionó** con los datos que tienes. Marzo fue un buen mes en MRR y en altas, pero no puedes atribuirlo a la secuencia de correos.

### Lo que muestran los números

- MRR al 28 de febrero: **$4.100**
- MRR al 31 de marzo: **$5.300**
- Cambio: **+$1.200 / +29%**
- Altas al plan pago en febrero: **9**
- Altas al plan pago en marzo: **14**

Es una mejora descriptiva real. Pero **no es evidencia de que la secuencia de emails la haya causado**.

### Por qué no se puede atribuir a la secuencia

1. **Hay tres cambios simultáneos**  
   - 1 de marzo: secuencia de 5 emails.  
   - 3 de marzo: publicidad paga.  
   - 12 de marzo: mención de un creador con audiencia grande.  

   Los tres pudieron generar altas. No hay forma limpia de separar cuánto aportó cada uno.

2. **No hay grupo de control**  
   Todos los usuarios gratuitos recibieron la secuencia. No sabes cuántos se habrían pasado al plan pago igual sin recibir esos emails.

3. **MRR no es una métrica de email**  
   El MRR sube o baja por altas nuevas, churn, upgrades, downgrades, cambios de plan. No sabes cuánto del aumento de $1.200 viene de nuevas conversiones y cuánto de otros movimientos.

4. **El volumen de datos es chico**  
   Pasar de 9 a 14 altas son solo 5 altas más. Con números tan bajos, esa diferencia podría ser ruido normal del negocio, sobre todo si se compara un solo mes contra otro.

### Qué haría falta para estar seguros

Para poder decir “la secuencia de emails funcionó”, necesitarías algo así:

- **Un grupo de control o un test A/B**  
  Por ejemplo, dividir a los usuarios gratuitos elegibles: un grupo recibe la secuencia, otro no. Luego comparas conversión a pago entre ambos grupos. Eso se acerca mucho más a medir causalidad.

- **Atribución por fuente**  
  Links con UTM en los emails, seguimiento de clics y conversiones, y una forma de registrar si cada alta paga vino de: email, ads, video del creador u orgánico.

- **Datos diarios de altas y conversiones**  
  Si la mayoría de altas ocurrió después del 12 de marzo, el influencer probablemente explica una parte grande. Si ocurrieron antes, aún queda la mezcla email-publicidad, pero ayudaría a descartar hipótesis.

- **Desglose de MRR**  
  Nuevo MRR por nuevas suscripciones, MRR perdido por cancelaciones, expansión/upgrades, etc. Sin eso, solo ves el saldo final.

- **Historial previo**  
  Varios meses de MRR y altas antes de marzo para saber si febrero fue un mes atípico o si ya venía una tendencia de crecimiento.

### En resumen

No puedes decir que la secuencia de emails funcionó. Tampoco puedes decir que no funcionó. Lo correcto con estos datos es: **marzo mejoró, pero no sabemos cuánto fue por el email, por los ads, por el creador o por variación normal.**