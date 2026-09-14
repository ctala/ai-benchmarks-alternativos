# GLM 5.3 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 47.337s | tokens_per_second: 73.2
- input_tokens: 235 | output_tokens: 3467

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

**Conclusión corta: no se puede saber si la secuencia funcionó.** Los datos muestran que *algo* empujó las conversiones en marzo, pero tienes tres cambios simultáneos y ninguna forma de repartir el crédito entre ellos. La historia "los emails funcionaron" y la historia "los emails no aportaron nada y fue todo ads + creador" explican estos números igual de bien.

**Por qué no alcanza con esto:**

1. **Solapamiento total de causas.** La secuencia arrancó el 1/3, la publicidad el 3/3 y la mención del creador el 12/3. La única ventana "limpia" de emails son el 1 y 2 de marzo, pero una secuencia de 5 emails actúa durante días o semanas: casi todo su efecto cae dentro del periodo con ads y la mención activas.
2. **Muestra demasiado chica.** 9 → 14 altas parece un salto del 56%, pero con esos volúmenes una variación de ±4-5 entre meses puede ser puro azar. No es interpretable.
3. **Falta línea base.** ¿Cuántas altas hubo en diciembre y enero? Si la comunidad ya venía creciendo, parte del aumento es tendencia, no intervención.
4. **El MRR no se descompone.** Los +$1.200 pueden incluir altas nuevas, upgrades, menos churn o cambios de plan. De hecho, salvo que tu ARPU ronde los $85, las 14 altas no explican solas el aumento — hay algo más moviéndose ahí que no estamos viendo. Y sin saber cuántos usuarios gratuitos tienes, tampoco puedo calcular tasa de conversión.

**Qué haría falta:**

*Forense rápido (con datos que probablemente ya existen):*
- Fuente de cada una de las 14 altas de marzo: link del creador, campaña de ads, UTM de email, u orgánico. Con eso ya tenés una primera partición.
- Fechas de las altas: ¿se concentran después del 12/3? ¿Goteo parejo desde el 1/3? Un clúster tras el video apuntaría a esa vía (sin probar que los emails no ayudaron).
- Precaución: las plataformas de ads se auto-atribuyen de más, y una mención del creador puede generar búsquedas de marca que los ads terminan "capturando".

*Para una respuesta real (próximos 30-60 días):*
- **Test con grupo de control:** dividí los usuarios gratuitos al azar; secuencia solo para la mitad. Comparar tasas de conversión es el único diseño que aísla el efecto de los emails. Si tu base gratuita es chica, puede que no haya potencia estadística — y eso también es información útil.
- **Línea base de 4-6 meses previos** para conocer la variación natural mes a mes.
- **Etiquetado permanente:** UTM en cada email, link o cupón único para el creador, y una pregunta opcional "¿cómo nos encontraste?" en el alta.

**Lo único sostenible hoy:** en marzo hubo más altas y más MRR que en febrero. Nada más. Antes de asumir que la secuencia funcionó (y de escalarla o replicarla en otra cohorte), valdría la pena hacer la mirada forense de las 14 altas: toma una tarde y cambia mucho la decisión.