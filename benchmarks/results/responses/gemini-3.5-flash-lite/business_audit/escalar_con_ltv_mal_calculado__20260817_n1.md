# Gemini 3.5 Flash Lite — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.07 | quality: 10.0
- latency_total: 4.599s | tokens_per_second: 210.3
- input_tokens: 194 | output_tokens: 967

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

Respira hondo y **para la pauta de inmediato**. No metas ni un dólar. 

Tu entusiasmo es admirable, pero tu aritmética financiera acaba de condenar tu flujo de caja a una muerte lenta y dolorosa. Estás cometiendo el error clásico del fundador optimista: confundir *ingresos brutos* con *contribución real*, y promediar el tiempo de vida del cliente ignorando la cruel realidad del interés compuesto del churn.

Vamos a destripar tus números como analista. Pon atención:

### 1. El LTV real (La ilusión de los 2 años)
Dices que un cliente se queda 2 años (24 meses) y multiplicas $35 por 24. 
**Error 1:** No consideras el margen bruto. El LTV se calcula sobre el *margen*, no sobre la venta. 
* Margen bruto: 70%. 
* Aporte real mensual por cliente: $35 × 0.70 = **$24.50**.

**Error 2:** El Churn no es lineal, es exponencial. Con un churn mensual del 8%, la realidad matemática es que la vida media real de un cliente no es de 24 meses, es de **12.5 meses** (1 / 0.08 = 12.5).

*   **Tu LTV real:** $24.50 × 12.5 meses = **$306.25**.

### 2. La dura verdad del LTV / CAC
Pones tu LTV real ($306.25) frente a tu CAC ($290):
*   $306.25 / $290 = **1.05**.

Un ratio LTV/CAC de 1.05 significa que **prácticamente estás cambiando dólares por dólares**, sin contar costos fijos, sueldos, impuestos ni herramientas. Para escalar con publicidad pagada sanamente, se busca un ratio mínimo de 3x *después* de todos los costos de adquisición. Con 1.05, cualquier mínimo aumento en tu CAC o en tu churn te vuelve netamente negativo.

### 3. El verdadero problema: El Periodo de Recuperación (Payback Period)
Aquí es donde tu plan de meter $10,000 este mes se estrella contra la pared. 

¿Cuánto tiempo tardas en recuperar los $290 que te costó adquirir ese cliente?
*   Aporte mensual por cliente (después de margen): $24.50.
*   CAC: $290.
*   Payback: $290 / $24.50 = **11.8 meses**.

**¡Tardas casi un año en recuperar el dinero que pusiste hoy en pauta!** 

Si metes $10,000 este mes en publicidad (asumiendo el mismo CAC, que empeorará al escalar), habrás adquirido unos 34 clientes. Esos clientes te dejarán $833 al mes en margen bruto. Tendrás que esperar casi un año solo para *recuperar* tu capital inicial, y para el mes 12, una buena parte de esos 34 clientes ya se habrán ido por culpa de tu 8% de churn mensual.

### Conclusión del analista:
Si ejecutas este plan, tu caja se va a evaporar en los próximos 60 días financiando clientes que se van antes de pagarse a sí mismos. Tu negocio actual es rentable *orgánicamente*, pero tu unidad económica para pauta pagada **no cierra**.

**¿Qué tienes que hacer antes de gastar un centavo?**
1.  **Bajar el Churn:** Un 8% mensual es altísimo (significa que pierdes casi el 65% de tus clientes al año). Si lo bajas al 3%, tu LTV salta dramáticamente.
2.  **Bajar el CAC:** Optimizar canales, mejorar la conversión, o encontrar canales más baratos.
3.  **Subir precios:** A $35 estás regalando el valor si tu CAC es de $290. Necesitas subir el ticket promedio para absorber ese costo de adquisición.

Guarda esos $10,000 en el banco. Con estos números hoy, escalar con pauta es un suicidio financiero. Arreglemos la máquina antes de pisar el acelerador.