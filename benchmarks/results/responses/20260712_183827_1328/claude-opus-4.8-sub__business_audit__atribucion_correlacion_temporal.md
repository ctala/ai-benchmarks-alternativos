# Claude Opus 4.8 (suscripción) — business_audit/atribucion_correlacion_temporal

- model_id: `claude-opus-4-8`
- success: True  | final: 4.37 | quality: 4.8
- latency_total: 66.18s | tokens_per_second: 50.6
- input_tokens: 4 | output_tokens: 3348

## Respuesta completa

## Veredicto

**No se puede saber.** Y no es que falte un dato: el experimento, tal como se corrió, es irrecuperable. Tres causas plausibles se activaron en la misma ventana de 30 días y ninguna se puede separar de las otras con los números que tienes.

Cualquiera que te diga "sí, funcionó, +29% MRR" te está vendiendo una historia, no un análisis.

---

## Lo que los números sí dicen (y lo que no)

**1. El +29% de MRR no mide altas.**
$5.300 − $4.100 = $1.200 de MRR neto. Divídelo entre 14 altas y te da ~$86 por alta. Salvo que tu plan cueste eso, la cuenta no cuadra. El MRR neto es:

```
nuevas + expansión − contracción − churn
```

No me diste churn, ni upgrades, ni si hubo anuales, ni si tocaste precios. Es perfectamente posible que las 14 altas hayan aportado, digamos, $500 y el resto venga de que en marzo se te cayó menos gente que en febrero. Ese +29% podría no tener nada que ver con los emails, incluso si los emails hubieran funcionado.

**2. Las 14 altas vs 9 no son una señal, son ruido.**
Con una tasa base de ~9 al mes, observar 14 por puro azar tiene una probabilidad de aproximadamente **1 en 8**. Nadie toma decisiones con eso. Y ojo: marzo tiene 31 días y febrero 28. Solo por calendario, esperarías ~10, no 9. La diferencia real que estás celebrando es 14 contra ~10.

Peor: no tengo una serie histórica. Si tus meses anteriores fueron 6, 12, 8, 15, 9 — entonces 14 es un martes cualquiera.

**3. Tres tratamientos, una sola observación.**
- Emails: 1 de marzo
- Ads ($400): 3 de marzo
- Mención de un creador grande: 12 de marzo

Están solapados. Y el tercero es el más peligroso: una mención de alguien con audiencia grande puede generar un pico de altas por sí sola, en cuestión de días. Si tus 5 altas extra cayeron entre el 12 y el 20 de marzo, la explicación más simple no son tus emails.

---

## Qué necesitas para tener una respuesta (en orden de costo)

**Hoy mismo, gratis, con lo que ya tienes:**

1. **Corta marzo por fecha.** Altas del 1–11 (emails + ads, sin creador) vs 12–31 (los tres). Si el 80% del salto está después del 12, tienes tu sospechoso. No es prueba, pero descarta rápido.
2. **Cruza cada alta contra la lista de la secuencia.** ¿Cada una de las 14 personas estaba en el plan gratuito y recibió los emails? ¿O varias entraron directo desde el anuncio o el video, sin pasar nunca por la secuencia? Si 6 de 14 nunca vieron un email, ya sabes algo.
3. **Métricas del embudo, no del resultado.** Enviados → abiertos → clicks → visitas a la página de pago → altas. Si el email 3 tuvo 200 clicks y 0 conversiones, la secuencia no está funcionando aunque el MRR haya subido.
4. **Trae churn y expansión de febrero y marzo.** Sin eso, el +29% es un número que no significa nada.
5. **12 meses de altas mensuales.** Para saber cuánta variación es "normal" en tu negocio. Sin baseline, no hay anomalía.

**Para el próximo mes, esto sí te da causalidad:**

6. **Holdout.** Deja al 20-30% de los usuarios gratuitos **fuera** de la secuencia, elegidos al azar. Comparas la tasa de conversión free→paid del grupo tratado contra el de control, en la misma ventana. Es la única forma de que el creador de turno, la estacionalidad y los ads afecten a ambos grupos por igual y se cancelen.

   Con tus volúmenes (9-14 altas/mes) esto va a tardar. Para detectar una diferencia razonable vas a necesitar **2-3 meses acumulados** de datos. Es lento, pero es la diferencia entre saber y creer.

7. **Una cosa a la vez.** Emails en marzo, ads en abril. Si tienes que lanzar dos, al menos que el holdout te proteja.

---

## Lo que sí puedes decir en voz alta

> "En marzo lanzamos la secuencia, empezamos ads y nos mencionó un creador. Subimos de 9 a 14 altas y el MRR neto creció $1.200. No sabemos cuánto aportó cada cosa, y el salto de altas está dentro del rango de variación normal. Estamos montando un holdout para medir la secuencia de verdad."

Eso es honesto y te deja bien parado. Lo otro —"la secuencia funcionó, +29%"— es una conclusión que la data no sostiene, y el costo de creértela es que el mes que viene vas a invertir tiempo en optimizar emails cuando quizás lo que te movió la aguja fue un video de YouTube que no controlas.

**Riesgo específico que quiero dejarte marcado:** si la secuencia se envió de golpe a *todos* los usuarios gratuitos acumulados (no como drip a los nuevos), lo que viste es un efecto de una sola vez sobre el backlog. Ese número no se repite en abril, y si construiste tu proyección asumiendo que sí, te vas a llevar un susto.