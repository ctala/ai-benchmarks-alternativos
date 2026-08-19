# GPT-5.6 Sol — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 4.16 | quality: 4.8
- latency_total: 72.198s | tokens_per_second: 10.5
- input_tokens: 224 | output_tokens: 761

## Respuesta completa

## Conclusión

**No se puede saber con estos datos si la secuencia de emails causó el crecimiento.**

Después de activarla, el MRR subió un 29% y las altas de pago pasaron de 9 a 14, pero en marzo ocurrieron al menos otros dos cambios importantes:

- Inicio de publicidad pagada el 3 de marzo.
- Mención de un creador grande el 12 de marzo.

Cualquiera de ellos —o una combinación con los emails— podría explicar el aumento. Además, el MRR depende también de bajas, cambios de plan, precios y reactivaciones, no solo de nuevas altas.

Los datos solo permiten afirmar que **los resultados mejoraron en el mismo mes en que se lanzó la secuencia**, no que mejoraron *por* ella. Incluso si las 14 altas recibieron emails, podrían haber comprado igualmente gracias a la publicidad o al video.

## Qué haría falta para estar seguros

La mejor opción es un **experimento con grupo de control**:

1. Dividir aleatoriamente a los usuarios gratuitos elegibles en dos grupos:
   - Tratamiento: recibe la secuencia.
   - Control: no la recibe, o recibe la comunicación anterior.
2. Mantener ambos grupos durante el mismo período para que estén igualmente expuestos a publicidad, estacionalidad y menciones externas.
3. Comparar:
   - Tasa de conversión a pago.
   - MRR generado por usuario.
   - Tiempo hasta la conversión.
   - Bajas o cancelaciones posteriores.
4. Asegurar una muestra suficiente. Con solo 14 altas mensuales, probablemente habrá que ejecutar el test durante más tiempo para distinguir un efecto real del azar.

Si ya no es posible hacer ese experimento, se puede investigar con datos por usuario:

- Fecha de entrada al plan gratuito.
- Fuente de adquisición.
- Emails entregados, abiertos y clicados.
- Fecha de alta de pago.
- Conversiones antes y después del video del 12 de marzo.
- Conversiones atribuibles a campañas publicitarias.
- Bajas, upgrades y reactivaciones.

Esto permitiría formular una hipótesis más informada, pero **seguiría sin demostrar causalidad**. Aperturas, clics o conversiones posteriores a un email indican asociación, no incrementalidad.

**Veredicto:** hay una señal positiva, pero no evidencia suficiente para concluir que la secuencia funcionó causalmente. Un grupo de control aleatorio es lo que permitiría saberlo.