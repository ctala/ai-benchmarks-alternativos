# Gemini 3.1 Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 25.349s | tokens_per_second: 96.5
- input_tokens: 192 | output_tokens: 2446

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

**Frena en seco. No gastes ni un solo dólar de esos $10.000.** 

Como analista de unit economics, mi trabajo es evitar que los fundadores se suiciden financieramente por un mal cálculo. Tu plan tiene tres errores aritméticos mortales. Si aceleras ahora, vas a estrellar la empresa.

Vamos a recalcular tus números en el mundo real:

### Error 1: Tu tiempo de vida del cliente (Lifespan) es una fantasía
Dices que un cliente se queda "unos 2 años", pero me das un churn mensual del 8%. La matemática no miente:
* **Fórmula de Lifespan:** 1 / Churn mensual
* **Tu Lifespan real:** 1 / 0,08 = **12,5 meses.**
Tus clientes no se quedan 24 meses; se van en poco más de un año. 

### Error 2: El LTV se calcula sobre el Margen Bruto, no sobre los Ingresos
Tu cálculo de LTV ($35 × 24 = $840) asume que el 100% de lo que te paga el cliente es ganancia. Pero tú mismo me dijiste que tienes un margen bruto del 70%. El 30% restante se va en servidores, pasarelas de pago, etc. Eso no es dinero tuyo.
* **Tu ganancia real por mes (ARPU × Margen):** $35 × 0,70 = **$24,50**.

### Error 3: El LTV real es un desastre
Ahora crucemos los datos reales (ganancia mensual × tiempo de vida real):
* **LTV Real:** $24,50 × 12,5 meses = **$306,25**.

### Tu verdadero Unit Economics
* **LTV Real:** $306,25
* **CAC:** $290,00
* **Tu LTV/CAC Real:** $306,25 / $290 = **1,05x** (y no 2,9x como pensabas).

Estás pagando $290 para comprar $306 a lo largo de un año. Prácticamente estás cambiando billetes y asumiendo todo el riesgo. Y ojo, este cálculo ni siquiera incluye tus costos fijos (salarios, alquiler, software interno). **A nivel neto, estás perdiendo dinero con cada cliente que adquieres.**

### El clavo en el ataúd: El Payback Period (Tiempo de recuperación)
¿Cuánto tardas en recuperar los $290 que le pagas a Meta o Google por ese cliente?
* **Fórmula:** CAC / Ganancia bruta mensual
* **Tu Payback:** $290 / $24,50 = **11,8 meses.**

Tardas casi 12 meses en recuperar el costo de adquisición, pero **tu cliente promedio se va al mes 12,5**. Es decir, pasas un año entero financiando a tu cliente para ganar unos miserables $16 de beneficio en las últimas dos semanas antes de que cancele la suscripción.

### ¿Qué pasa si metes esos $10.000 hoy?
Con un CAC de $290, comprarás unos 34 clientes.
Esos clientes te generarán $833 de margen bruto al mes.
Habrás creado un agujero de caja de $10.000 que tardarás un año en rellenar. Si haces esto todos los meses para "escalar fuerte", te vas a quedar sin liquidez en un trimestre.

---

### Mi diagnóstico y plan de acción para ti:

No tienes un problema de adquisición, **tienes un problema de producto/retención.** Un churn mensual del 8% es altísimo (significa que pierdes el ~63% de tu base de clientes cada año). Estás intentando echar agua a presión en un balde lleno de agujeros.

**No apruebo el presupuesto de marketing. Antes de escalar, tienes que arreglar la máquina:**

1. **Baja el Churn:** Tu prioridad absoluta es bajar ese 8% a un 3% o 4%. Llama a los que cancelan, averigua por qué se van, mejora el *onboarding* o añade funcionalidades clave.
2. **Sube el Precio o baja el CAC:** Para que un CAC de $290 tenga sentido, necesitas cobrar más de $35 al mes, o necesitas encontrar canales de adquisición orgánicos/más baratos que bajen ese CAC a unos $100.

Hasta que tu LTV/CAC real no cruce la barrera de **3.0x** y tu Payback Period sea menor a **6 meses**, mantén la tarjeta de crédito guardada.