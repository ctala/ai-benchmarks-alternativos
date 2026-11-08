# Muse Wonder — business_audit/atribucion_correlacion_temporal

- model_id: `meta/muse-wonder`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 17.642s | tokens_per_second: 102.3
- input_tokens: 236 | output_tokens: 1804

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

## Conclusión: No se puede saber

Con esos datos no puedes atribuir la subida a la secuencia de emails. Y tampoco puedes decir que no funcionó.

Lo único que sabes es que en marzo pasaron 3 cosas a la vez y las altas subieron. Nada más.

### Por qué no es atribuible

**1. Lanzaste 3 palancas casi simultáneamente**
- 1 de marzo: secuencia de emails
- 3 de marzo: publicidad pagada ($400)
- 12 de marzo: mención de un creador grande

Si las altas suben, ¿fue por el email 3, por un anuncio, o porque 2.000 personas vieron ese video? Con los datos agregados del mes, es imposible separarlo.

**2. No hay grupo de control**
Activaste los emails para *todos* los usuarios gratuitos. No tienes un grupo comparable de usuarios gratuitos que NO los recibió para comparar su conversión.

Sin ese contrafactual, no sabes qué habría pasado sin emails.

**3. La muestra es demasiado pequeña**
Pasar de 9 a 14 altas son solo 5 altas de diferencia.

Con números tan bajos, esa variación puede ser ruido normal. Además, febrero tiene 28 días y marzo 31. Solo por duración, ya esperarías ~10 altas en marzo manteniendo el mismo ritmo de febrero.

9 vs 14 no es una señal estadísticamente sólida.

**4. MRR y altas absolutas no son la métrica correcta**
El MRR (+29%) también depende de bajas/churn, reactivaciones, cambios de plan y de *cuántos* usuarios gratuitos había.

Si la publicidad y la mención trajeron muchos más usuarios gratuitos en marzo, es normal que haya más altas aunque la secuencia no convierta mejor. Necesitas la tasa: `altas / usuarios gratuitos expuestos`.

### Qué puedes revisar ahora (ayuda, pero no prueba)

No te dará certeza, pero te puede dar pistas:

1.  **Fecha exacta de cada alta de marzo:** ¿Se concentran después del 12? ¿O entre el 1 y el 2, antes de ads y mención?
2.  **Origen de esos 14:** ¿Eran usuarios gratuitos antiguos (de antes del 1 de marzo) o llegaron en marzo por ads/video?
3.  **Comportamiento con el email:** De los que pagaron, ¿habían abierto/clicado la secuencia *antes* de pagar?

Si, por ejemplo, la mayoría son usuarios antiguos que abrieron el email 2 y pagaron antes del 12, es *sugerente*. Sigue sin ser prueba, porque igual habrían pagado sin email.

### Qué haría falta para estar seguros la próxima vez

Un test con holdout, aunque sea simple:

1.  Divide aleatoriamente a los nuevos usuarios gratuitos: **80% recibe la secuencia, 20% no recibe nada.**
2.  No cambies ads ni busques menciones durante el test si puedes evitarlo. Si no, ese test vale para ambos grupos por igual porque la división es aleatoria.
3.  Define antes de empezar la métrica principal: **% que pasa a pago en 14 días desde el registro**, no MRR del mes.
4.  Déjalo correr hasta tener un volumen decente. Con 9-14 altas al mes, necesitarás varios meses, no 2 semanas, para detectar un efecto real.
5.  Registra para cada alta: fecha, cohorte (con email / sin email), fuente de llegada (UTM / encuesta) y fecha de registro como gratuito.

Hasta que no tengas esa comparación, mi recomendación es que no presentes el +29% de MRR como "resultado de los emails" internamente. Es la conclusión cómoda, pero los datos no la sostienen.