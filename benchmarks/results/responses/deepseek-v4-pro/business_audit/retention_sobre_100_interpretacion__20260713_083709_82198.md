# DeepSeek V4 Pro — business_audit/retention_sobre_100_interpretacion

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.8 | quality: 7.2
- latency_total: 36.688s | tokens_per_second: 54.8
- input_tokens: 139 | output_tokens: 2011

## Respuesta completa

No, rotundamente no. Has interpretado "retención de ingresos 114 %" como sinónimo de retención de clientes perfecta y eso es un error clásico. Vamos a separar los dos conceptos con los datos que tú mismo das.

### Lo que realmente mide (y esconde) ese 114 %
Ese número es **Net Revenue Retention (NRR)** mensual sobre la base de clientes que tenías el mes pasado. Significa que los ingresos recurrentes generados *este mes* por los mismos 40 clientes que tenías *el mes pasado* equivalen al 114 % de lo que pagaban entonces. En euros: si antes pagaban 100, ahora pagan 114.  
Eso solo es posible porque las expansiones (upgrades de plan) de algunos clientes compensaron con creces la pérdida de ingresos de los que se fueron o redujeron su gasto. Es una señal muy positiva de que los que se quedan te valoran, pero **no dice nada sobre cuántos clientes perdiste**.

### La realidad que oculta el NRR de 114 %
Tú mismo lo cuentas: **pasaste de 40 clientes de pago a 36**. Es decir, perdiste 4 clientes netos (o más, si hubo bajas compensadas por altas nuevas; asumiremos que fueron 4 bajas puras sobre la base antigua).

- **Customer churn rate mensual:** 4/40 = 10 %. Eso es muy alto.  
- **Revenue churn rate (sin upgrades):** seguramente negativo (perdiste X € de los que se fueron, pero sin contar los upgrades tus ingresos recurrentes habrían bajado). El NRR de 114 % te dice que *a pesar de esa pérdida de clientes*, el ingreso total de esa cohorte subió.

En resumen: tienes una máquina de expandir ingresos en los clientes fieles, pero también una puerta giratoria de abandono que estás disfrazando con upgrades.

### ¿Puedes centrarte solo en captar nuevos?
**No, y te explico por qué es peligroso:**

1. **El NRR alto es temporal si la base se erosiona:**  
   Si cada mes pierdes el 10 % de los clientes, al cabo de un año te habrás quedado con una fracción pequeña de ellos, por mucho que los supervivientes dupliquen su gasto. Llegará un momento en que la base sea tan pequeña que las expansiones no podrán compensar la pérdida de volumen total. Un NRR > 100 % con alto churn de logos es una señal de alerta, no de tranquilidad.

2. **Dependencia de unos pocos:**  
   Si solo 5 o 6 de los 36 que quedan son los que subieron de plan para darte ese 114 %, tu negocio descansa sobre un grupo muy reducido. El día que uno de ellos se vaya, el NRR se desplomará y perderás ingresos de golpe sin suficientes clientes para reponerlo con adquisición.

3. **El coste de captar vs. retener:**  
   Conseguir un cliente nuevo cuesta de 5 a 7 veces más que conservar uno existente (según estudios de referencia como Bain & Company). Si estás perdiendo el 10 % de tus clientes al mes, tendrías que traer un 11,1 % de clientes nuevos solo para mantener la misma base de 40 (necesitas 4,4 clientes nuevos cada mes). Eso es una rueda de hámster carísima.

4. **Señal de problemas de producto o satisfacción:**  
   Diez de cada cien clientes que se van cada mes es un síntoma de que algo no funciona: onboarding, soporte, relación precio/valor, competencia. Ignorar ese churn mientras solo sumas clientes nuevos es emparchar el agujero del cubo con más agua en lugar de arreglar la fuga.

### El diagnóstico completo que deberías dar
- **NRR = 114 %** → Excelente palanca de expansión. Producto sticky para los que se quedan.
- **Logo churn = 10 % mensual** → Grave hemorragia de clientes. Probablemente un segmento poco adecuado o una desconexión en etapas tempranas.
- **Estrategia:** No elijas entre uno y otro. Necesitas un plan en dos velocidades:  
  – **Retención de clientes:** analiza por qué se van esos 4 cada mes, reduce el churn a un nivel saludable (en SaaS B2B de ticket medio, un churn mensual > 3 % ya es preocupante; > 5 % es crítico).  
  – **Expansión y adquisición:** sigue haciendo upgrades a los fieles y adquiriendo nuevos, pero solo cuando hayas taponado la fuga. De lo contrario, escalarás un negocio que se cae por detrás.

Así que no, no puedes dejar de preocuparte por el churn. El 114 % es una buena noticia a medias: te dice que vendes bien a los que se quedan, pero también que no sabes mantener a los que entran. Arregla eso antes de pisar el acelerador de captación.