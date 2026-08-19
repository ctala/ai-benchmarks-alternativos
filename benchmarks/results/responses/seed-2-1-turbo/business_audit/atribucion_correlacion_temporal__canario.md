# Seed 2.1 Turbo — business_audit/atribucion_correlacion_temporal

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 109.877s | tokens_per_second: 61.0
- input_tokens: 275 | output_tokens: 6702

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

### Conclusión principal: No se puede saber si la secuencia de emails funcionó.
Los datos que compartes no permiten atribuirle el aumento de MRR o de altas, porque hubo otros cambios importantes en el mismo periodo y no hay forma de separar su impacto del de la secuencia. No podemos afirmar ni que sirvió de nada ni que perjudicó: simplemente no hay evidencia suficiente para llegar a una conclusión fiable.

---

### Motivos por los que no se puede atribuir el resultado a la secuencia:
1. **Hay dos factores externos que pueden explicar todo el aumento (variables confundidoras)**  
   Empezaste a pagar publicidad solo 2 días después de lanzar la secuencia, y un creador grande te mencionó a mitad de mes. Ambas acciones suelen generar altas (tanto directas al plan pago como de usuarios que pasan por el gratuito) que no tienen nada que ver con la secuencia enviada a la base antigua. No hay forma de saber cuánto del aumento viene de los emails, cuánto de la publicidad y cuánto de la mención. Incluso podría pasar que la secuencia no sirvió de nada (o incluso que molestó a los usuarios) y el aumento se debe enteramente a las otras dos acciones.

2. **No sabes si las altas vienen del público al que iba dirigida la secuencia**  
   La secuencia se envió a los usuarios del plan gratuito que había al 1 de marzo. Pero no tienes desglosado cuántas de las 14 altas de marzo son de esos usuarios (que sí recibieron los emails) y cuántas son de:
   - Usuarios que se registraron en el plan gratuito *después* del 1 de marzo (por publicidad o la mención del creador)
   - Personas que se apuntaron directamente al plan pago, sin pasar nunca por el gratuito (que nunca recibieron la secuencia)
   Si la mayoría de las altas nuevas no vienen de la base gratuita del 1 de marzo, el aumento no tiene relación con la secuencia.

3. **No tienes contexto de tendencia para comparar**  
   Solo nos das datos de febrero. Si las altas venían creciendo mes a mes (por ejemplo, 6 en enero, 9 en febrero, 14 en marzo sigue la misma tendencia), el aumento de marzo sería parte de ese crecimiento natural, no por la secuencia. Tampoco sabes si marzo tiene estacionalidad (por ejemplo, es un mes donde la gente se apunta más a comunidades por propósitos de año nuevo) que explique el aumento.

4. **El MRR depende de más factores que las altas nuevas**  
   El aumento de MRR no se debe solo a más altas: también influyen las bajas (si hubo menos bajas en marzo que en febrero, el MRR sube sin que las altas aumenten por la secuencia), los upgrades de plan (si usuarios pasaron de un plan más barato a uno más caro) o cambios de precios. No tienes datos de eso para descartarlo.

---

### ¿Qué puedes hacer para tener más claridad?
#### Pasos que te darán indicios (no certeza absoluta) con datos que probablemente ya tengas:
1. **Desglosa las altas por origen**: Separa cuántas fueron directas al plan pago, cuántas de usuarios gratuitos que ya estaban el 1 de marzo y cuántas de usuarios gratuitos que entraron después. Si la mayoría de las altas nuevas no vienen de la base del 1 de marzo, es muy probable que el aumento venga de la publicidad o el creador.
2. **Mira la temporalidad de las altas de la base inicial**: Si las altas de los usuarios que ya estaban en gratuito el 1 de marzo se concentran en los días siguientes al envío de cada email, y especialmente si hubo un aumento antes del 3 de marzo (antes de la publicidad) o antes del 12 de marzo (antes de la mención), sería un indicio a favor de la secuencia. Si la mayoría son después del 12, es mucho más probable que vengan de la mención del creador.
3. **Compara con la tendencia de meses anteriores**: Trae datos de 3-6 meses antes de marzo para ver cuánto crecían las altas y el MRR cada mes. Si el aumento de marzo es muy superior a la tendencia normal, habría más probabilidades de que alguna de las acciones que lanzaste lo causara, pero igual no sabrás cuál.
4. **Rastrea el origen de los usuarios**: Si usas parámetros UTM en los enlaces de la publicidad y del vídeo del creador, sabrás cuántas altas vienen de esas fuentes. Si esa cantidad explica todo el aumento de febrero a marzo, la secuencia probablemente no tuvo impacto.

#### La única forma de tener certeza absoluta:
Haz un **test A/B (experimento controlado)**:
- Divide aleatoriamente a los usuarios del plan gratuito (tanto los que ya están como los que van entrando) en dos grupos:
  • Grupo tratamiento: recibe la secuencia de 5 emails.
  • Grupo control: no recibe la secuencia (o recibe los emails que enviabas antes de lanzar esta).
- Como la asignación es aleatoria, ambos grupos estarán expuestos a los mismos factores externos (publicidad, menciones, estacionalidad, etc.), así que cualquier diferencia en la tasa de conversión a plan pago entre los dos grupos se deberá exclusivamente a la secuencia.
- Deja correr el experimento durante el tiempo que tarda la secuencia en completarse y generar conversiones (por ejemplo, 4 semanas) y luego compara las tasas. Si la del grupo tratamiento es claramente mayor, la secuencia funciona.

Para comunidades pequeñas puede tardar más en tener resultados fiables (porque necesitas suficientes usuarios para que la diferencia no sea por azar), pero es la única forma de evitar equivocarte de conclusión.