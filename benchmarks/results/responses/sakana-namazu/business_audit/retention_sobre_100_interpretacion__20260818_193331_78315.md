# Sakana Namazu — business_audit/retention_sobre_100_interpretacion

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 17.584s | tokens_per_second: 194.8
- input_tokens: 161 | output_tokens: 3426

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No. Esa lectura es incorrecta y, si actúas sobre ella, probablemente dañarás el negocio.**

Una retención de ingresos del 114 % no significa que “no se te va nadie”. Significa exactamente lo contrario en tu caso: **se te están yendo clientes, pero los que se quedan están pagando lo suficiente como para cubrir esas bajas y dejar un margen positivo del 14 %**.

Veamos tu situación con precisión.

---

### 1. Lo que dice realmente tu métrica

Una “retención de ingresos” superior al 100 % es, técnicamente, **Retención Neta de Ingresos** (Net Revenue Retention, NRR). Se calcula sobre una cohorte de ingresos existentes y refleja tres fuerzas:

\[
\text{NRR} = \text{Ingresos iniciales} - \text{Churn (bajas)} - \text{Contracción} + \text{Expansión (upsells/cross-sells)}
\]

Tú partías de **40 clientes** y ahora tienes **36**. Es decir, perdiste a **4 clientes**, lo que equivale a un **churn de clientes (logo churn) del 10 %** en el período. Si estamos hablando de un ciclo mensual, eso es una cifra muy grave; implicaría que anualmente retendrías solo alrededor del **28 % de tus clientes** (0,9^12).

El panel muestra 114 % porque los upgrades (clientes que subieron de plan) sumaron más dinero del que se fugó con esas 4 bajas. Eso es bueno para el flujo de caja a corto plazo, pero **no elimina el problema estructural: tu cubo tiene un agujero grande**.

---

### 2. La trampa de confundir “dinero retenido” con “clientes retenidos”

Son métricas ortogonales:

| Métrica | Tu valor aproximado | Qué mide |
| :--- | :--- | :--- |
| **Retención Neta de Ingresos (NRR)** | 114 % | Si los ingresos de tus clientes existentes crecen o se contraen. |
| **Retención de Clientes (Logo Retention)** | ~90 % (perdiste 4 de 40) | Qué porcentaje de tus cuentas sigue activo. |

**El error de interpretación:** Creer que el dinero creció un 14 % porque “nadie se va”. La realidad es que **el dinero creció a pesar de que se van clientes**, gracias a una expansión fuerte entre los que permanecen.

---

### 3. ¿Puedes dejar de preocuparte por el churn?

**No.** De hecho, deberías preocuparte más. Esto es por qué:

* **La expansión tiene límites.** No puedes confiar en que una base de clientes que se reduce 10 % mensual siga pagando más y más indefinidamente. Tarde o temprano te quedas sin usuarios a quienes hacer upsell.
* **Estás destruyendo rentabilidad unitaria.** Si gastas dinero en adquirir clientes (CAC) y se van al mes siguiente o muy pronto, estás quemando capital. Llenar un cubo con un agujero del 10 % es matemáticamente agotador.
* **El churn es una señal de producto.** Un 10 % de logos que se van en un mes indica fricción real: onboarding fallido, expectativas no cumplidas, precio desajustado para ciertos segmentos o competencia ganando terreno. Ocultarlo con upsells no lo resuelve.

---

### 4. Lectura correcta de tu negocio (la menos halagüeña)

Tu SaaS tiene **dos realidades simultáneas**:

1. **Un motor de expansión sano:** Los clientes que se quedan ven suficiente valor como para pagar más. Eso es un punto a favor claro.
2. **Un problema grave de retención de cuentas:** Pierdes a 1 de cada 10 clientes en cada ciclo. Eso es una alerta roja.

La interpretación optimista (“puedo olvidarme del churn y sólo vender”) es numéricamente autodestructiva. Si mantienes ese churn de logos, necesitarías una máquina de adquisición perfecta e infinita solo para mantenerte estático en usuarios, mientras rezas para que los que quedan sigan expandiendo.

---

### 5. Qué hacer en lugar de “meter todo el esfuerzo en captación”

Tu estrategia debe ser bifurcada:

* **Investiga el churn inmediatamente:**
  * ¿Quiénes se fueron? ¿Tenían un plan específico, tamaño o canal de adquisición común?
  * ¿Cuánto tiempo duraron? Si se van antes del segundo pago, es un problema de onboarding. Si duran meses y luego se van, es un problema de valor percibido a largo plazo.
  * Habla con esos 4 clientes (o los que puedas). Una encuesta de cancelación es mínima aquí.

* **Segmenta tu base:**
  * Es probable que los 36 que se quedan sean de un segmento que sí encaja con el producto (y por eso expanden), mientras que los 4 que se fueron correspondan a un segmento para el cual tu SaaS no es el adecuado. Si es así, deja de adquirir ese perfil; enfoca marketing en los que se parecen a tus upgraders.

* **Adquisición sí, pero con el churn contenido:**
  * No muevas “todo” el esfuerzo. Asegúrate de que el CAC payback period sea sostenible considerando la vida útil real de tus clientes. Con 10 % de churn mensual, la vida media de un cliente es muy corta y el LTV se desploma.

---

### Conclusión

**114 % de retención neta de ingresos es un resultado financiero positivo, pero no es sinónimo de salud del negocio.** En tu caso, está enmascarando una pérdida de clientes del 10 % en el período. Ignorar el churn porque el indicador de ingresos luce verde es como ignorar una hemorragia porque tu presión arterial todavía parece normal.

Prioriza encontrar por qué se van esos clientes y cómo sellar esa fuga. La captación masiva debería ser tu segundo impulso, no tu primera excusa.