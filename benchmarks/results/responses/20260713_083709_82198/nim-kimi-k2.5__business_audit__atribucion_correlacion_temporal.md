# Kimi K2.5 (NIM) — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 5.68 | quality: 6.0
- latency_total: 49.138s | tokens_per_second: 36.7
- input_tokens: 270 | output_tokens: 1801

## Respuesta completa

**Conclusión: No se puede saber.** Con los datos actuales, es imposible determinar si la secuencia de emails funcionó, falló, o tuvo efecto neutro.

## Por qué tus números no responden la pregunta

Tienes un **problema de variables confusas** (confounding variables). Observaste un aumento del 29% en MRR y 55% más altas, pero en marzo ocurrieron tres intervenciones simultáneas:

1. **Secuencia de emails** (1 marzo)
2. **Publicidad pagada** ($400, desde 3 marzo)  
3. **Mención de creador grande** (12 marzo)

Cualquiera de estas tres cosas (o la combinación, o factores externos) podría explicar el crecimiento. Los datos que me das no permiten desagregar el efecto de cada una.

## Lo específico que falta para saberlo

Para atribuir esas 14 altas de marzo a los emails específicamente, necesitarías:

**Datos de atribución:**
- ¿Cuántas de las 14 altas llegaron mediante UTM de los emails vs. UTM de la publicidad vs. búsqueda directa (posiblemente por la mención del creador)?
- ¿Cuándo exactamente ocurrieron las 14 altas? Si la mayoría fue después del 12 de marzo, sospecharía más del creador que de tus emails.

**Datos de funnel:**
- ¿Cuántos usuarios gratuitos recibieron la secuencia? (tamaño de la cohorte)
- ¿Cuál era la tasa de conversión baseline de usuarios gratuitos *antes* de marzo? (Si en febrero convertías al 2% y en marzo al 2.1%, los emails no hicieron mucho; si saltaste al 5%, hay señal)

**Datos de engagement:**
- Tasas de apertura y click de los 5 emails
- ¿Cuántos de los 14 nuevos pagados abrieron los emails antes de pagar?

**Grupo de control:**
- ¿Hubo usuarios gratuitos que *no* recibieron la secuencia en marzo? Comparar su tasa de conversión vs. los que sí la recibieron sería el único método semi-confiable sin herramientas complejas.

## Mi diagnóstico probabilístico

Si me obligaras a apostar:
- La mención del creador grande (12 marzo) probablemente explicó más del crecimiento que tus emails, simplemente por el volumen típico que generan ese tipo de shoutouts.
- Los $400 en publicidad, dependiendo del CPA, podrían explicar 2-5 altas si la conversión es decente.
- Tus emails podrían haber contribuido, pero no puedo estimar cuánto sin ver una curva de conversión diaria.

## Qué hacer para medirlo bien

Para la próxima campaña:

1. **Test A/B simple**: Divide tu lista de gratuitos en dos grupos aleatorios. Grupo A recibe los emails, Grupo B no. Compara tasas de conversión al cabo de 30 días.

2. **Seguimiento de cohortes**: Etiqueta en tu CRM/Stripe a los usuarios que entren al funnel de emails. Luego filtra: "¿Cuántos pagaron provenientes de la secuencia de marzo vs. otros canales?"

3. **Análisis temporal**: Grafica altas diarias. Si ves un pico específico alrededor del 12-15 de marzo, es el creador. Si es gradual durante todo marzo, podría ser la publicidad o los emails.

4. **Pregunta directa**: En el checkout o onboarding de pago, pregunta "¿Qué te hizo decidirte a pagar?" (opciones: emails, mención de [creador], publicidad, boca a boca, etc.).

**Veredicto provisional**: Mantén la secuencia si el costo de mantenerla es bajo, pero no atribuyas el crecimiento de marzo a ella sin más datos. Probablemente estés sobreestimando su impacto frente a la mención del creador.