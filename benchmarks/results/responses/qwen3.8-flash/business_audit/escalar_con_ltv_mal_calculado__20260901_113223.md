# Qwen 3.8 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 145.946s | tokens_per_second: 105.3
- input_tokens: 255 | output_tokens: 15375

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

**Respuesta corta: no, no le daría a $10.000 en publicidad este mes para “escalar fuerte” con estos números.**

Tu canal, tal como está, **no es rentable de forma sólida**: el nuevo cliente pagado apenas cubre su costo de adquisición. Y tu cálculo tiene tres problemas importantes:

1. **Estás usando ingresos, no margen bruto.**  
   El LTV relevante para decidir si escalar con paid ads debe ser **margen bruto acumulado**, no facturación.

2. **Con churn mensual de 8%, la vida promedio no es 24 meses.**  
   Si el churn es 8% mensual y constante, la vida promedio es aproximadamente **12,5 meses**, no 2 años.

3. **2,9 no está por encima de 3.**  
   Incluso con tu propio número, 2,9 está por debajo del benchmark clásico. Y cuando lo corriges por margen y churn, el ratio baja muchísimo.

---

## 1. Recalculo el LTV correctamente

### Margen bruto mensual por cliente

Precio: **$35/mes**  
Margen bruto: **70%**

\[
\text{Margen bruto mensual} = 35 \times 0,70 = \$24,50
\]

### Vida promedio con churn 8%

Si el churn mensual es 8%:

\[
\text{Vida promedio} = \frac{1}{0,08} = 12,5 \text{ meses}
\]

No 24 meses.

### LTV en ingresos

\[
\text{LTV ingresos} = \frac{35}{0,08} = \$437,50
\]

### LTV en margen bruto

\[
\text{LTV margen bruto} = \frac{24,50}{0,08} = \$306,25
\]

Ese es el número que importa para comparar contra CAC.

---

## 2. LTV/CAC corregido

CAC: **$290**

\[
\text{LTV/CAC} = \frac{306,25}{290} = 1,06
\]

No 2,9.

### Significado práctico

Por cada cliente adquirido, después de pagar publicidad y considerar margen bruto y churn, te quedan aproximadamente:

\[
306,25 - 290 = \$16,25
\]

de contribución neta durante toda la vida del cliente.

Eso es prácticamente **break-even**.

Y ojo: ese $16,25 es antes de muchos otros costos: soporte, refunds, chargebacks, descuentos, diseño de anuncios, agencia, equipo comercial, impuestos, herramientas, overhead, etc.

---

## 3. Incluso si aceptáramos que el cliente dura 24 meses

Tu fundador dice: “se queda unos 2 años”. Aceptemos eso por un momento, aunque sea inconsistente con churn 8%.

LTV en margen bruto:

\[
24,50 \times 24 = \$588
\]

LTV/CAC:

\[
\frac{588}{290} = 2,03
\]

Sigue estando por debajo de 3.

Además, si el churn mensual es 8%, la probabilidad de que un cliente siga activo después de 24 meses es:

\[
0,92^{24} \approx 13,5\%
\]

Es decir, con churn 8% mensual, solo un pequeño porcentaje sobrevive 2 años. El promedio real es mucho más corto.

---

## 4. Qué pasa si metes $10.000 en publicidad

### Clientes nuevos estimados

\[
\frac{10.000}{290} \approx 34,5 \text{ clientes}
\]

### MRR nuevo

\[
34,5 \times 35 \approx \$1.207
\]

### Margen bruto mensual nuevo

\[
34,5 \times 24,50 \approx \$845
\]

### Payback simple, sin considerar churn

\[
\frac{290}{24,50} \approx 11,8 \text{ meses}
\]

Eso ya es alto para un SaaS de $35/mes.

### Payback real considerando churn 8%

Como el cohorte se va perdiendo, no recuperas $845 cada mes para siempre. El cohorte decae.

Con churn 8%:

- Después de 12 meses, ese cohorte te habría generado aprox. **$6.700** de margen bruto acumulado.
- Después de 24 meses, aprox. **$9.100**.
- Necesitas unos **35 meses** para recuperar los $10.000 invertidos en publicidad.
- El margen bruto total de por vida de ese cohorte sería aprox. **$10.600**.

Es decir:

\[
\text{Margen bruto lifetime} \approx \$10.600
\]

\[
\text{Inversión} = \$10.000
\]

\[
\text{Contribución neta lifetime} \approx \$600
\]

Eso es antes de overhead, soporte, refunds, agencia, diseño, tracking, etc.

Y si consideras costo de dinero, por ejemplo un 10% anual, el LTV descontado baja. Con descuento, el LTV en margen bruto por cliente puede caer a alrededor de:

\[
\frac{24,50}{0,08 + 0,008} \approx \$286
\]

que es menor que el CAC de $290. Ahí el negocio de pagar anuncios puede volverse **NPV negativo**.

---

## 5. Por qué es frágil

Tu punto de equilibrio aproximado es:

\[
\text{Churn break-even} = \frac{\text{margen bruto mensual}}{\text{CAC}} = \frac{24,50}{290} \approx 8,45\%
\]

Es decir, con un churn de 8,45% mensual, el LTV en margen bruto iguala al CAC.

Tú estás en 8%. Solo tienes medio punto porcentual de margen de seguridad.

Cualquier desvío te puede hacer negativo:

- CAC sube a $305 y ya estás en break-even.
- Churn sube a 8,5% y ya estás en break-even.
- Pagas agencia, creativos, refunds o soporte adicional y probablemente estás negativo.
- Escalas publicidad y el CAC sube porque saturaste el público.
- Adquiere clientes que habrían entrado orgánicamente y el CAC incremental real es mayor.

---

## 6. Qué números necesitarías para escalar con más confianza

Con tus actuales:

- Precio: $35/mes
- Churn: 8%
- Margen bruto: 70%
- LTV margen bruto: $306,25

Para tener **LTV/CAC = 3**, necesitarías:

### Opción A: bajar CAC

\[
\text{CAC objetivo} = \frac{306,25}{3} \approx \$102
\]

Hoy estás en $290. Necesitarías bajar el CAC a aproximadamente un tercio.

### Opción B: bajar churn

Para que LTV/CAC sea 3 con CAC $290:

\[
\text{LTV necesario} = 290 \times 3 = \$870
\]

Con margen mensual $24,50:

\[
\text{Churn necesario} = \frac{24,50}{870} \approx 2,82\%
\]

Es decir, tendrías que bajar el churn mensual de 8% a alrededor de 2,8%.

### Opción C: subir precio o margen

Si mantienes churn 8% y margen 70%, para que LTV/CAC sea 3 necesitas un margen bruto mensual de:

\[
\frac{870}{12,5} = \$69,60
\]

Con 70% de margen, eso implica un precio de:

\[
\frac{69,60}{0,70} \approx \$99,40/mes
\]

No realista con tu oferta actual, a menos que subas mucho el valor percibido, hagas upsells o pases a planes anuales.

---

## 7. Mi recomendación práctica

### No escales fuerte con paid ads ahora.

Con estos números, meter $10.000 en publicidad no es un motor de crecimiento rentable. Es una apuesta al break-even con payback muy largo y alta fragilidad.

### Antes de escalar, arregla una o varias de estas palancas:

1. **Reducir churn**
   - Onboarding
   - Activación temprana
   - Email/retención
   - Win-back
   - Mejorar producto
   - Reducir customer effort
   - Mejorar soporte proactivo

2. **Reducir CAC**
   - Mejorar targeting
   - Mejorar landing pages
   - Mejorar creativos
   - Aumentar conversión
   - Probar canales más baratos
   - Referral
   - Partnerships
   - Contenido/SEO
   - Retargeting inteligente

3. **Aumentar ARPU**
   - Planes anuales
   - Prepay
   - Tiers más altos
   - Add-ons
   - Upsells
   - Precio mínimo más alto
   - Segmento B2B con mayor willingness to pay

4. **Aumentar margen bruto**
   - Negociar infraestructura
   - Cambiar procesador
   - Optimizar costos variables
   - Reducir refunds
   - Reducir soporte por cliente

5. **Mejorar flujo de caja**
   - Cobrar anual
   - Trial con tarjeta
   - Prepay discounts
   - Reducir tiempo de conversión

---

## 8. Si aun así quieres probar publicidad

Hazlo como experimento controlado, no como plan de escalar fuerte.

Por ejemplo:

- Invierte $1.000 o $2.000, no $10.000.
- Mide CAC incremental real.
- Mide churn por cohorte, no promedio global.
- Mide payback por cohorte.
- Mide LTV en margen bruto.
- Incluye costos de creativos, agencia, herramientas, soporte y refunds.
- Evalúa si el CAC sube cuando aumentas presupuesto.

### Criterios mínimos para escalar con paid ads

Yo buscaría algo como:

- **LTV/CAC en margen bruto ≥ 3**
- **CAC payback ≤ 6 a 12 meses**, idealmente ≤ 6 meses
- **Churn mensual bajo**, idealmente < 5% para un producto de $35/mes
- **CAC fully loaded**, no solo ad spend
- **CAC estable o decreciente** al escalar presupuesto
- **Margen bruto realista**, incluyendo soporte y refunds

Con tus números actuales:

\[
\text{LTV/CAC} = 1,06
\]

\[
\text{Payback real con churn} \approx 35 \text{ meses}
\]

Eso no es para escalar fuerte.

---

## Veredicto final

**No le des a los $10.000 este mes.**

Tu plan no muere en estrategia; muere en aritmética.

Con churn 8% mensual, margen bruto 70% y CAC $290, el nuevo cliente pagado genera apenas unos **$16 de contribución neta de por vida**, antes de otros costos. Eso no es un motor de crecimiento rentable. Es un canal en punto de equilibrio.

Primero arregla unit economics: baja CAC, baja churn, sube ARPU o mejora margen. Después escala.