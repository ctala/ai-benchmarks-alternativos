# Claude Opus 4.8 (suscripción) — business_audit/atribucion_correlacion_temporal

- model_id: `claude-opus-4-8`
- success: True  | final: 5.21 | quality: 6.0
- latency_total: 65.523s | tokens_per_second: 51.8
- input_tokens: 4 | output_tokens: 3396

## Respuesta completa

## Respuesta corta

No se puede saber. Con estos datos no hay forma de separar el efecto de la secuencia del efecto de los ads y del creador. Y ni siquiera está claro que haya un efecto que separar.

## Qué dicen los números realmente

**1. Tres intervenciones en la misma ventana.**
Emails (1-mar), ads (3-mar), creador (12-mar). Los tres apuntan al mismo mes. Cualquier atribución que hagas es una historia, no una medición. Esto es lo que mata el análisis, todo lo demás es secundario.

**2. La diferencia de altas está dentro del ruido.**
9 → 14 parece +56%. Pero marzo tiene 31 días y febrero 28: ajustando por calendario, la base esperada es ~10, no 9.
Y con números tan chicos, 10 vs 14 no distingue nada. Si tiras una moneda 23 veces (9+14), sacar 14 caras es perfectamente normal. La probabilidad de ver una diferencia así o mayor **solo por azar** es de ~40%. No es una señal, es una fluctuación mensual típica.

**3. El +29% de MRR no cuadra con las altas.**
+$1.200 de MRR con 14 altas implica ~$86 por alta nueva. A menos que ese sea tu precio real, hay otra cosa moviendo el MRR: planes anuales, upgrades de gente que ya pagaba, churn más bajo, cambio de precio. **El MRR no es un proxy de la secuencia de emails.** No lo uses como métrica de éxito de esto.

**4. Falta el denominador.**
Los ads y el creador probablemente inflaron la base de usuarios free. Si tu base gratuita creció 40% y las altas crecieron 40%, tu **tasa de conversión free→paid no mejoró en nada**, y la secuencia no aportó. Contar altas absolutas mientras cambias el tráfico de entrada es la forma más común de engañarse.

## Qué necesitaría para responder

En orden de valor:

**a) Cohorte limpia (esto lo puedes hacer hoy, con datos que ya tienes).**
Aísla a los usuarios free que **ya estaban en tu lista antes del 1 de marzo**. Ese grupo no llegó por ads ni por el creador. Compara su tasa de conversión en marzo contra su tasa en enero-febrero. Es la única lectura semi-limpia disponible retroactivamente. Ojo: sigue sin ser causal (el creador pudo darle notoriedad a la comunidad y empujar a los viejos también), pero elimina el confusor más grande.

**b) Timestamps a nivel individual.**
De las 14 altas: ¿cuántas recibieron la secuencia *antes* de pagar? ¿Cuántas ni la vieron (pagaron el mismo día que llegaron por el video)? Si 9 de las 14 vinieron del creador y nunca abrieron un email, ya tienes tu respuesta.

**c) Descomponer el MRR.**
Nuevas + expansión − churn − contracción. Hasta que no separes eso, el "+29%" no significa nada operativo.

**d) Un holdout, desde ahora.**
50/50 de los usuarios free nuevos: mitad recibe la secuencia, mitad no. Es la única forma de saberlo de verdad.

**Advertencia honesta sobre el holdout:** con ~10-14 conversiones al mes, detectar una mejora realista (digamos +30%) con confianza estadística te tomaría **varios meses por rama**. Tu volumen es el cuello de botella, no tu instrumentación. Opciones: (1) aceptar que la lectura será direccional y lenta, (2) medir métricas intermedias con más volumen (click en el email → visita a checkout), asumiendo que correlacionan con la conversión.

## Lo que yo haría esta semana

1. Sacar la lista de las 14 altas de marzo con: fecha de alta, fecha de registro free, fuente, y si recibieron/abrieron la secuencia. Es una tarde de trabajo y probablemente cambia toda tu lectura.
2. Dejar de reportar "MRR +29%" como resultado de los emails. No lo sostiene la data.
3. Montar el holdout ahora, y asumir que la respuesta real llega en 3-6 meses.

**Conclusión:** hoy la secuencia está en estado "funcionando técnicamente, ROI pendiente de medir". No es un fracaso. Tampoco es un éxito. Es una incógnita, y la diferencia entre las dos cosas importa cuando decidas cuánto invertir en el próximo embudo basándote en esto.