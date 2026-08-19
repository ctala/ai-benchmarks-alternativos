# Sakana Namazu — business_audit/atribucion_correlacion_temporal

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 9.228s | tokens_per_second: 221.9
- input_tokens: 270 | output_tokens: 2048

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

**Conclusión: No se puede saber si la secuencia de emails funcionó.** 

Con los datos que tienes hoy, atribuir el crecimiento de marzo a los emails sería una conjetura, no una conclusión de datos. Sí creciste: +$1.200 de MRR y +5 altas. Pero tenías tres motores encendidos al mismo tiempo (emails + publicidad + mención grande), y todavía no sabemos qué tan caliente estaba cada uno.

---

### Por qué los números actuales no responden la pregunta

1. **Las "altas" son un agregado que mezcla orígenes.**  
   Los emails iban dirigidos a usuarios **gratuitos existentes**, pero las 14 altas de marzo pueden ser:
   - Usuarios gratuitos previos que convirtieron (lo que buscabas con los mails).
   - Gente completamente nueva que llegó por los anuncios o el video del creador.  
   Sin segmentar esas 14 altas por procedencia, no sabemos si los emails convirtieron a alguien o si apenas captaron usuarios nuevos.

2. **Faltan datos de una cohorte o grupo de control.**  
   Lo ideal hubiera sido dejar un 15-20 % de tus usuarios gratuitos **fuera** de la secuencia de emails. Si la tasa de conversión de quienes recibieron los mails fuera, digamos, 3 % y la de quienes no recibieron 0.5 %, tendríamos evidencia. Sin ese contrafactual, cualquier interpretación es débil.

3. **El timing juega en contra de los emails.**  
   El 12 de marzo una mención grande puede generar un pico de tráfico y conversiones. Tus 14 altas pueden haberse concentrado en la segunda quincena, lo que minaría la hipótesis de que fueron los emails los principales responsables.

4. **La base de usuarios gratuitos es desconocida.**  
   Si tenías 50 usuarios gratuitos, 5 conversiones es una brutalidad. Si tenías 2.000, es ruido. Sin saber el tamaño de la base, el número de altas no dice nada sobre la efectividad de la secuencia.

---

### Qué haría falta para estar seguros

Para poderte responder con rigor, necesitaríamos esto (ordenado por prioridad):

| Información | Para qué sirve |
|-------------|----------------|
| **Segmentar esas 14 altas** en: "nuevos usuarios" vs. "gratuitos previos que convirtieron". | Para aislar el objetivo de los emails. |
| **Saber cuántos usuarios gratuitos tenías al 1 de marzo** y qué porcentaje convirtió. | Para calcular una tasa de conversión real. |
| **Comparar con un grupo de control** de febrero o de marzo que no recibió emails. | Para separar el efecto de los emails del comportamiento natural. |
| **Ver las fechas exactas de las 14 altas.** | Si la mayoría ocurrió antes del 12, el video no explica todo; si ocurrió después, el video es un candidato fuerte. |
| **Tasa de apertura, clics y conversiones directas de los emails.** | Muestra engagement, pero recuerda que el clic no garantiza que el email causó la conversión (atribución asistida). |

---

### Mi recomendación práctica

Si tu plataforma de emails o tu CRM lo permite, haz