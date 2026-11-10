# GPT-OSS 20B — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 11.01s | tokens_per_second: 103.0
- input_tokens: 288 | output_tokens: 1134

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

**Conclusión preliminar**

Con la información que me has dado no se puede afirmar con certeza que la secuencia de 5 correos electrónicos haya sido la causa principal del aumento en el MRR ni del número de suscripciones pagas en marzo. Los datos que tenemos (MRR, número de nuevas suscripciones y los eventos externos de publicidad e influencer) son insuficientes para separar el efecto de cada uno de estos factores.

**Por qué no se puede concluir**

| Variable | Lo que sabemos | Lo que necesitamos |
|----------|----------------|--------------------|
| **MRR** | $4 100 (feb.) → $5 300 (mar.) | Desglose de MRR por fuente (influencer, ads, emails, orgánico) |
| **Nuevas suscripciones** | 9 en febrero, 14 en marzo | Identificar qué canal generó cada suscripción (email, anuncio, video) |
| **Emails** | Secuencia de 5 emails lanzada el 1 mar | Tasa de apertura, clics, conversiones de cada email; número de usuarios que recibieron la serie |
| **Publicidad** | $400 gastados el 3 mar | Métricas de rendimiento (CTR, CPA, MRR generado) |
| **Influencer** | Mención el 12 mar | Tráfico y suscripciones atribuibles al video (UTM, códigos de descuento) |

Sin segmentar los datos por fuente de adquisición y sin un control de variables, cualquier afirmación sobre la efectividad del email es especulativa.

---

## Qué se necesita para estar seguros

1. **Etiquetado y seguimiento de origen**  
   - Añadir parámetros UTM a los enlaces de los emails, a los anuncios y a los posts del influencer.  
   - Registrar en el CRM o en la herramienta de analytics a qué campaña pertenece cada nuevo usuario.

2. **Métricas de rendimiento del email**  
   - Tasa de apertura y clics por email.  
   - Conversión (suscripción pagada) desde el email.  
   - Tiempo hasta la conversión (para medir la velocidad de respuesta).

3. **A/B testing (o multivariate testing)**  
   - Lanzar la secuencia de correos a un 50 % de los usuarios del plan gratuito y a un 50 % a los que no reciben nada (o reciben una versión diferente).  
   - Comparar el número de conversiones, el MRR incremental y la tasa de churn entre los grupos.

4. **Modelo de atribución**  
   - Usar un modelo de atribución (por ejemplo, “último clic” o “modelo ponderado”) para distribuir el crédito entre los canales (email, ads, influencer).  
   - Revisar si la mayoría del crédito se asigna al email o a los otros canales.

5. **Cohort analysis**  
   - Analizar cohortes de usuarios que recibieron la serie de correos vs. los que no, a lo largo de varias semanas.  
   - Observa la retención y el valor de vida útil (LTV) de cada cohorte.

6. **Control de variables externas**  
   - Registrar cualquier cambio en la oferta, precios o en la competencia durante marzo.  
   - Ajustar el análisis para descontar estos efectos.

---

## Próximos pasos recomendados

| Acción | Herramienta / recurso | Tiempo estimado |
|--------|----------------------|-----------------|
| Implementar UTM y registrar en CRM | Google Analytics, Mixpanel, HubSpot | 1–2 días |
| Medir métricas de email (open/click/conv.) | Plataforma de email marketing (Mailchimp, SendGrid) | 1 día |
| Diseñar y lanzar A/B test | HubSpot, Optimizely, Google Optimize | 1–2 semanas (incluye tiempo de recopilación de datos) |
| Configurar modelo de atribución | GA4, Attribution.com, Data Studio | 2–3 días |
| Generar reportes de cohortes | Looker, Power BI, Excel | 1–2 días |

Una vez que tengas datos segmentados y un experimento controlado, podrás estimar con mayor precisión el impacto de la secuencia de emails. Hasta entonces, la afirmación de que “la secuencia funcionó” sería una conjetura no respaldada por evidencia.