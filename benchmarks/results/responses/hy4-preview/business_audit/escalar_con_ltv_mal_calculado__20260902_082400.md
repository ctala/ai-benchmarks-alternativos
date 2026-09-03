# Tencent Hy4 preview — business_audit/escalar_con_ltv_mal_calculado

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 82.953s | tokens_per_second: 56.5
- input_tokens: 228 | output_tokens: 4687

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

Frena las máquinas. **No le des.** 

Como analista de Unit Economics, mi trabajo es evitar que destruyas tu caja (cash flow). Y este es el clásico ejemplo de un plan que muere en la aritmética. Tienes dos errores fatales en tu modelo mental, y de paso, hiciste un "redondeo" psicológico para convencerte a ti mismo (2.9 es *menor* que 3, no mayor).

Vamos a rehacer los números. 

### Los 2 Errores Fatales en tu Cálculo

**1. Usaste Ingresos (Revenue) en lugar de Margen Bruto (Gross Profit)**
El LTV (Lifetime Value) siempre debe calcularse sobre el dinero que realmente te queda después de los costos variables (infraestructura, pasarelas de pago, soporte). 
* Tu ingreso es $35, pero tu ganancia bruta real es: **$24.50/mes** ($35 × 70%).

**2. Inventaste el "Lifetime" (Tiempo de vida) ignorando tu propio Churn**
Asumiste que el cliente se queda 24 meses (2 años). La aritmética del churn dice otra cosa. Si pierdes el 8% de tus clientes cada mes, la vida promedio de un cliente es:
* Vida promedio = 1 / Churn = 1 / 0.08 = **12.5 meses** (¡No 24!).

---

### La Aritmética Real (La verdad duele)

Vamos a calcular tu LTV real con *tus* datos:
* **Margen Bruto Mensual:** $24.50
* **Vida Promedio del Cliente:** 12.5 meses
* **LTV Real:** $24.50 × 12.5 = **$306.25**

Ahora comparemos eso con lo que te cuesta adquirirlo (CAC):
* **LTV / CAC:** $306.25 / $290 = **1.05x**

No tienes un ratio de 3, tienes un ratio de **1.05**. La regla de oro para escalar de forma saludable es un LTV/CAC mayor a 3. Con un 1.05, estás básicamente pagando $290 para ganar $16 dólares en todo el ciclo de vida del cliente.

---

### La Sentencia de Muerte: El Tiempo de Recuperación (Payback Period)

Incluso si ignoramos el bajo margen de ganancia, el mayor asesino aquí es el flujo de caja. ¿Cuánto tardas en recuperar los $290 que gastaste en publicidad?
* **Payback Period:** CAC ($290) / Margen Mensual ($24.50) = **11.8 meses.**

Esto significa que **tardas casi un año (11.8 meses) en recuperar la inversión** de un cliente. Pero como el cliente se va a los 12.5 meses, solo tienes unas 3 semanas de "ganancia real" antes de que cancele. 

Si tu churn sube tan solo un 1% (al 9%), la vida del cliente baja a 11.1 meses. ¿Ves el problema? Empezarías a **perder dinero** con cada cliente que entra.

---

### ¿Qué pasa si metes los $10.000?

Si ejecutas tu plan este mes:
1. Quemarás $10.000 de tu banco hoy.
2. Adquirirás unos 34 clientes nuevos.
3. Estarás en números rojos con ese grupo de clientes durante **11 meses y medio**.
4. Cuando ese grupo de 34 clientes finalmente cancele (en poco más de un año), habrás generado una ganancia total de **$552 dólares**. 

Inmovilizar $10.000 de tu capital de trabajo durante un año para ganar $500 es una pésima decisión financiera, asumiendo un riesgo enorme.

### ¿Qué deberías hacer antes de prender la manguera de la publicidad?

Antes de escalar, tienes que arreglar la "cubeta" (tu retención), porque está agujereada.

1. **Ataca el Churn (Tu prioridad #1):** Un 8% mensual es altísimo. Si logras bajarlo a la mitad (4%), la vida de tu cliente sube a 25 meses, tu LTV sube a $612 y tu LTV/CAC a 2.1. 
2. **Sube el precio o el margen:** ¿Puedes cobrar $49 o $59 al mes? ¿Puedes negociar con tu procesador de pagos o bajar el costo de tu infraestructura?
3. **Baja el CAC:** Necesitas un CAC por debajo de los $100 para que esto tenga sentido a este precio. 

**Veredicto:** No gastes los $10.000 en ads. Gasta ese dinero en mejorar el onboarding, hablar con tus usuarios actuales y reducir ese churn del 8%. Cuando tu LTV/CAC sea 3 y recuperes tu CAC en menos de 6 meses, ahí sí, pon el pie en el acelerador a fondo.