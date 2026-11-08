# Tencent Hy3 — business_audit/retention_sobre_100_interpretacion

- model_id: `tencent/hy3`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 43.602s | tokens_per_second: 62.1
- input_tokens: 162 | output_tokens: 2707

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

Como analista, mi trabajo es darte la lectura exacta de los datos, y en este caso la interpretación intuitiva es **incorrecta** y, de actuar en consecuencia, bastante peligrosa para tu negocio.

Vamos a desglosar con precisión lo que realmente está pasando en tu panel:

### 1. Has confundido dos métricas distintas
El panel dice **"Retención de ingresos: 114%"**. En SaaS, esto se conoce como *Net Revenue Retention* (NRR). Esta métrica mide **el dinero**, no las personas. Mide cuánto ingreso conservas de la base de clientes que ya tenías al inicio del periodo, sumando las subidas de plan (expansión) y restando las bajas.

Tu "retención de clientes" (también llamada *Logo Retention*) es una métrica completamente diferente que mira el número de cuentas.

### 2. Tu retención de clientes NO está por encima del 100%
Según tu contexto: el mes pasado tenías 40 clientes y este mes tienes 36. Eso significa matemáticamente que **perdiste 4 clientes**.
Tu retención de clientes real es del **90%** (36 / 40). Tu *churn* (fuga) de logos es del **10% mensual**. Lejos de "no irse nadie", estás perdiendo una de cada diez cuentas cada mes.

### 3. ¿Qué significa entonces ese 114% de retención de ingresos?
Significa que los "varios" clientes que subieron de plan pagaron lo suficiente para cubrir el agujero financiero que dejaron los 4 clientes que se fueron, e **incluso aportaron un 14% extra de ingresos** respecto al mes anterior. 

Es una señal positiva de que tu capacidad de *upsell* (venta adicional) es fuerte, pero en este momento está actuando como un vendaje que tapa una herida abierta.

### 4. ¿Puedes dejar de preocuparte por el churn y enfocarte solo en captar? (Spoiler: NO)
**Rotundamente no.**
Un *churn* de logos del 10% mensual es una cifra altísima. Si mantienes esa tasa, en un año habrás perdido más del **70% de tu base de clientes actual** (0.9 elevado a 12 meses = 0.28, es decir, solo retienes el 28% anual).

Tienes lo que llamamos un **"cubo con fugas" (*leaky bucket*)**. Hoy el nivel del agua (tus ingresos) sube porque unos pocos clientes abren el grifo más fuerte (hacen upsell). Pero si el mercado se enfría, si esos clientes dejan de necesitar planes mayores, o si la competencia les quita esos upsells, tus ingresos caerán en picado porque la base de clientes se está encogiendo mes a mes.

### Recomendación analítica
No desmanteles tu estrategia de retención. Necesitas urgentemente entender **por qué se fueron esos 4 clientes** (¿precio, falta de *onboarding*, falta de features?). Tu NRR de 114% es bonito en el corto plazo, pero un negocio SaaS no es sostenible si tienes que correr más rápido captando nuevos clientes solo para reemplazar a los que se escapan por la puerta trasera.