# DeepSeek V4 Flash 0731 — business_audit/atribucion_correlacion_temporal

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 58.439s | tokens_per_second: 24.5
- input_tokens: 235 | output_tokens: 1430

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

**Conclusión: No podemos saber si la secuencia de emails funcionó. Es más, con los datos que me das, sería irresponsable afirmar que lo hizo.**

El crecimiento es real (+29% MRR, +55% altas), pero tienes **tres variables independientes** ocurriendo casi al mismo tiempo. Es imposible aislar el efecto de los emails con esta información. Te explico por qué:

**1. El problema del solapamiento temporal (Confusores)**
- **1 de marzo**: Activas la secuencia de emails.
- **3 de marzo**: Empiezas a pagar publicidad ($400).
- **12 de marzo**: Un creador con audiencia grande te menciona.

Las altas de marzo (14) pudieron venir de cualquiera de las tres fuentes, o de una combinación. Si el creador generó 10 altas y los anuncios 3, los emails solo habrían generado 1. O al revés. **No tienes forma de saberlo** mirando solo el total mensual.

**2. El problema de la métrica (MRR)**
El MRR subió de $4.100 a $5.300. Pero el MRR no mide solo altas nuevas; mide *churn* (bajas), *upgrades* y *downgrades*. Si en marzo se dieron de baja 5 clientes que pagaban $100, y ganaste 14 nuevos que pagan $50, el MRR sube igual. La secuencia de emails va dirigida a usuarios *gratuitos* (para convertirlos), pero no sé si esos 14 nuevos vienen del plan gratuito o de tráfico directo.

**3. El problema de la atribución**
No me dices si esos 14 nuevos en marzo **hicieron clic en un email** o si llegaron por un enlace de afiliado, un anuncio o el video. Sin parámetros UTM o códigos de seguimiento por fuente, es imposible atribuir la conversión.

---

**¿Qué haría falta para estar seguros?**

Para darte una respuesta sólida, necesitaría al menos una de estas tres cosas:

1. **Datos diarios o semanales**: Si las altas se concentraron el 13-14 de marzo (después del video) y no después de cada email, eso ya te da una pista visual. Si las altas vinieron en picos justo después de los emails (días 1, 4, 8, 12, 15 de marzo), el caso gana fuerza.
2. **Atribución por fuente**: ¿Cuántas de esas 14 altas vinieron de un clic en el email? (Necesitas tracking UTM en los links de los emails).
3. **Un grupo de control**: No lo tienes, pero podrías haber dividido a los usuarios gratuitos en dos grupos (A: recibe emails, B: no recibe) para comparar tasas de conversión. Eso es lo único que te daría causalidad real.

---

**Mi recomendación práctica (sin datos adicionales):**

No tires la secuencia de emails todavía, pero **no la des por buena**. Lo que sí puedes decir es que marzo fue un mes bueno. Para saber si los emails funcionan:

- **Mira el embudo**: ¿Cuántos abrieron, hicieron clic y convirtieron? Si la tasa de apertura es baja (<20%) o la de clics es baja (<2%), probablemente los emails no están funcionando aunque el MRR suba.
- **Aísla la próxima vez**: Pausa los anuncios durante una semana o espera a que pase el pico del video, y lanza una secuencia similar a un segmento pequeño para medir su efecto sin ruido.

En resumen: **Los números no sostienen la conclusión de que los emails funcionaron**. Solo sostienen que "hubo crecimiento en marzo". Si me apuras, te diría que el 80% de ese crecimiento probablemente vino del video viral, pero eso también sería una especulación sin datos. Prefiero no inventarlo.