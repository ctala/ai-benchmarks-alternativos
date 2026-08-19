# Claude Opus 5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.07 | quality: 10.0
- latency_total: 38.363s | tokens_per_second: 61.0
- input_tokens: 364 | output_tokens: 2341

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

# Conclusión corta

**No se puede saber con estos datos.** El crecimiento es real, pero tienes tres causas candidatas activas en el mismo mes y ninguna forma de separarlas. Cualquier respuesta que te diga "sí, funcionó" te estaría vendiendo una historia, no un hallazgo.

---

## Por qué no se puede concluir

**1. Tres intervenciones solapadas, un solo resultado.**
Emails (1 de marzo), publicidad ($400 desde el 3) y la mención del creador (12 de marzo). Las tres pueden generar altas al plan pago. No hay manera aritmética de repartir 14 altas entre ellas sin datos de atribución.

**2. La publicidad y la mención contaminan la propia audiencia de los emails.**
Esto es lo más incómodo: la secuencia va dirigida a usuarios del plan gratuito. La publicidad y el creador probablemente **metieron gente nueva al plan gratuito**, que luego entró en la secuencia. Así que ni siquiera puedes decir "los emails convirtieron a mi base existente": la base cambió de tamaño y de composición en el mismo periodo. Tráfico nuevo suele convertir distinto que un usuario que llevaba meses inactivo.

**3. n=9 vs n=14 es demasiado pequeño para ser señal.**
5 altas de diferencia sobre 9. Con estos volúmenes, la variación mes a mes por puro azar es enorme. No sé cuánto variaron enero, diciembre, noviembre — pero si tus meses históricos oscilan entre 7 y 13 altas, marzo con 14 es apenas el borde de lo normal. Sin esa serie histórica, +5 no es un resultado, es ruido plausible.

**4. Febrero tiene 28 días, marzo 31.**
Un 10,7% más de días. Sobre 9 altas, eso ya "explica" cerca de 1 alta sin que pase nada. No cambia el cuadro, pero el +29% de MRR y el +56% de altas están ambos algo inflados por el calendario.

**5. El MRR y las altas no cuadran de forma obvia — y eso importa.**
+$1.200 de MRR con 14 altas serían ~$86 por alta. Si tu plan cuesta bastante menos, hay algo más moviéndose ahí (upgrades a plan anual, cambios de precio, menos cancelaciones) y ese algo no tiene por qué venir de los emails. Si cuesta bastante más, entonces hubo churn que el crecimiento está tapando. En cualquier caso, el +29% no es un indicador limpio del efecto de la secuencia.

**6. Falta el denominador.**
14 altas sobre 200 usuarios gratuitos y 14 sobre 600 son cosas opuestas. Si la publicidad y el creador triplicaron tu base gratuita, tu **tasa** de conversión pudo haber empeorado mientras el número absoluto subía.

---

## Qué haría falta para estar seguros

**Ahora mismo, sin gastar nada — mira si los datos que ya tienes descartan algo:**

| Dato a extraer | Qué te dice |
|---|---|
| Altas mensuales de los últimos 6-12 meses | Si 14 cae dentro del rango histórico, no hay nada que explicar |
| Usuarios gratuitos activos a fin de feb y fin de marzo | El denominador; te da tasa de conversión, no solo volumen |
| Curva diaria de altas en marzo | ¿Hay un pico el 12-14 (creador) o están repartidas? Esto es lo más revelador que puedes sacar hoy |
| Cohorte de cada alta de marzo: fecha de registro al plan gratuito | Separa "base antigua" (candidata a mérito de los emails) de "usuarios nuevos de marzo" (llegaron por ads/creador) |
| Métricas de la secuencia: apertura, clics, y clics que terminaron en pago | Si casi nadie hizo clic en un enlace de upgrade, los emails no fueron el motor |
| Churn y upgrades de plan en marzo | Explica el desajuste entre MRR y altas |

**El análisis de cohortes es tu mejor herramienta disponible.** Si de las 14 altas, 11 son usuarios que se registraron en marzo (o sea, llegaron por ads o por el creador), la secuencia tuvo poco que ver. Si 12 son usuarios que llevaban meses en el plan gratuito y se activaron tras recibir los emails, tienes una señal decente — aún no una prueba, pero algo defendible.

**Para tener una respuesta de verdad, hacia adelante:**

1. **Test A/B con holdout.** Deja el 30-50% de los nuevos usuarios gratuitos fuera de la secuencia. Compara tasa de conversión a 30 días entre grupos. Es la única forma de aislar el efecto.
2. **No cambies varias cosas a la vez.** El problema real de marzo no son los datos, es el diseño. Si vas a probar algo, aíslalo o al menos escalona los cambios con semanas de separación.
3. **Ten paciencia con el tamaño.** Con ~10-15 altas al mes, un A/B honesto necesita varios meses para distinguir un efecto moderado del ruido. Si la secuencia duplicara la conversión, lo verías rápido; si la mejora un 20%, tardarás mucho en poder afirmarlo.
4. **Métricas intermedias como señal temprana.** Clics en el CTA de upgrade por email enviado se acumulan mucho más rápido que las altas. No prueban ingresos, pero te dicen si el mensaje mueve a alguien.

---

## Lo que sí puedes decir sin mentir

- El MRR creció y las altas subieron. Eso es un hecho.
- Marzo tuvo tres iniciativas nuevas y el resultado global fue positivo.
- **No sabes cuál de las tres lo produjo, ni si alguna lo hizo.** La hipótesis "el crecimiento vino del creador, y los emails y la publicidad no aportaron nada medible" encaja igual de bien con estos números.

Mi recomendación práctica: no apagues la secuencia (cuesta poco, riesgo bajo) pero **no la declares ganadora ni construyas planes sobre ella**. El error caro aquí no es mantener unos emails que quizá no sirven; es concluir que funcionan, escalar esa apuesta, y descubrir en tres meses que tu crecimiento de marzo fue un video de YouTube que no vas a poder repetir.

Si me pasas las altas históricas, el desglose diario de marzo y la fecha de registro de cada alta, puedo decirte bastante más.