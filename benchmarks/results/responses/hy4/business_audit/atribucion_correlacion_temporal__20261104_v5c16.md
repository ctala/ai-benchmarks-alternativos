# Tencent Hy4 — business_audit/atribucion_correlacion_temporal

- model_id: `tencent/hy4`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 44.055s | tokens_per_second: 93.8
- input_tokens: 256 | output_tokens: 4133

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

**Conclusión: no se puede saber.**

Y te diría algo más incómodo: con estos números no podemos ni siquiera afirmar que la secuencia *contribuyera* algo. Tampoco podemos decir que falló. Hoy está en **"efecto no medido"**. Si la damos por ganada, el mes que viene estaremos decidiendo presupuesto de emails (o quitándole mérito a los ads) con un argumento que los datos no sostienen.

**Por qué no da para concluir**

1. **Cambiaste tres cosas en el mismo mes.** Email (1/3), publicidad (3/3) y mención del creador (12/3). El +29% de MRR y el paso de 9 a 14 altas tienen tres candidatos a explicarlos y cero reparto entre ellos. Atribuirlo al email es elegir el primero de la lista, no medir.

2. **El email ni pudo impactar a parte de esas 14 altas.** La secuencia fue para *usuarios free ya existentes el 1 de marzo*. Los ads y el video traen visitantes nuevos, que nunca recibieron los 5 correos. Sin saber cuántas de las 14 venían de esa base free y cuántas son gente nueva, el denominador del email es desconocido. Podría ser cero.

3. **Falta el eje temporal.** Solo tengo totales de mes. Si 10 de las 14 altas son posteriores al 12, el creador explica casi todo; si se concentran antes del 3, cambia el cuento. Sin fecha por alta, el 3 y el 12 no se pueden separar.

4. **14 eventos es ruido.** De 9 a 14 (+5) entra cómodamente en la variación normal mes a mes de una comunidad pequeña, sin ninguna campaña de por medio. No hay baseline de conversión free→pago ni grupo contra el que comparar.

5. **El MRR no es un contador de altas.** +$1.200 es una cifra *neta*: altas + upgrades − bajas − downgrades. Sin desglose y sin precio por plan, ni siquiera puedo confirmar que ese +$1.200 corresponda a las 14 altas. Usarlo como prueba del email sería un doble salto.

**Qué haría falta para estar seguros** (en orden de coste/beneficio, para empresa pequeña)

- **Separar las 14 altas por origen, ya.** Enlace propio con UTM en cada email, UTMs en los ads, link/código del creador y un "¿cómo llegaste?" en el checkout. Con una tabla `alta | fecha | era_free_el_1_3 | origen` resolvemos el 80% de la duda sin gastar un peso más.
- **Serie diaria de altas y MRR** cruzada con el 3 y el 12. Es un CSV, no un proyecto.
- **Desglose del MRR** en new / expansion / churn / contraction, para que el +$1.200 cuadre con las altas.
- **Holdout en la próxima.** Dejar un 10–20% de los free sin secuencia y comparar conversión. Es la única forma de medir el email *incluso con ads y creadores activos*. Atajo: si hubo usuarios free del 1/3 que no recibieron los correos por un error de segmentación, ese es tu grupo control gratis — míralo antes de relanzar nada.
- **Métricas de la propia secuencia**: entregados, clics al enlace de upgrade, altas con ese UTM. Ojo: clics no demuestran ingresos, pero sí que el email se entregó y se usó.
- **Acumular antes de declarar victoria.** Con n=14, aunque el origen estuviera limpio, un mes no da potencia. Repetir en un mes sin ruidos (o con holdout) y mirar varios lotes.

**Lo que pondría en el informe de hoy, literal:**

> Marzo cerró +$1.200 MRR y +5 altas vs. febrero. Coincidieron secuencia de emails, publicidad y mención externa. El efecto de la secuencia es **no medido**. No se recomienda escalarla ni cortarla con este resultado.

Pásame las 14 altas con fecha y origen y te digo hasta dónde se puede afinar sin inventar nada.