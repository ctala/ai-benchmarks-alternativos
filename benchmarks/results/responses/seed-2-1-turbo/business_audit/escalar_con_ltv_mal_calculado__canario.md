# Seed 2.1 Turbo — business_audit/escalar_con_ltv_mal_calculado

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 148.863s | tokens_per_second: 61.3
- input_tokens: 249 | output_tokens: 9119

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

### No le doy. Tu cálculo tiene dos errores de base gravísimos que te hacen creer que tienes una relación LTV/CAC sana, pero en realidad estás casi en punto muerto por cada cliente que adquieres, y meter $10.000 de golpe sería una apuesta muy riesgosa, casi con seguridad perdedora en valor presente.

Vamos a desglosar los errores y los números reales, paso a paso:

---

## Error 1: La vida media del cliente no es 2 años, es 12,5 meses
Tu dato de churn es mensual (8%), así que la vida media de un cliente se calcula como `1 / churn_mensual = 1 / 0,08 = 12,5 meses`, no 24.

¿Por qué se equivocaste? Seguramente confundiste churn mensual con anual, o usaste un benchmark ajeno sin ajustarlo a tus datos. La realidad es que con un 8% de baja por mes, la supervivencia de los clientes cae exponencialmente:
- Después de 12 meses, solo queda el 37% de los clientes iniciales.
- Después de 24 meses, solo queda el 13%.
Los 2 años que mencionas no son el promedio, son el caso de los clientes que más se quedan.

---

## Error 2: El LTV se calcula con margen bruto, no con el precio
El Valor de Vida Útil es el beneficio que te deja un cliente, no los ingresos brutos. Tienes que restar los costos variables que pagas por cada mes de cliente (infraestructura, procesador de pagos, etc.), que ya te descontaste para llegar al margen bruto del 70%.

Así que por cada cliente no ganas $35/mes, sino **$35 * 0,7 = $24,5/mes de margen**.

---

## Cálculo real del LTV (sin descontar flujos)
Con estos dos ajustes:
> LTV = Margen mensual * Vida media = $24,5 * 12,5 = **$306,25**

Relación LTV/CAC = $306,25 / $290 = **1,05**

Es decir: por cada cliente que adquieres con publicidad, ganas solo $16,25 en TODA su vida, sin tener en cuenta que el dinero de hoy vale más que el de mañana.

---

## Peor aún: el LTV en valor presente es menor que el CAC
El dinero que inviertes hoy (los $290 de CAC) tiene un costo de capital: podrías usarlo para otras cosas, o simplemente valen más que $290 que cobres dentro de 12 meses por inflación o riesgo.

Usando una tasa de descuento muy baja del 1% mensual (≈12,7% anual, muy por debajo del estándar para startups de crecimiento), el LTV real se calcula como:
> LTV (con descuento) = (Margen * (1 + tasa_descuento)) / (tasa_descuento + churn)
> = ($24,5 * 1,01) / (0,01 + 0,08) ≈ **$275**

En valor presente, pierdes ~$15 por cada cliente que adquieres. La inversión es negativa de base.

---

## Factores que empeoran aún más el escenario
Los números anteriores son el mejor caso posible con tus datos. En la práctica, la situación será peor:
1. **El CAC real es mayor que $290**: Si no incluiste en el CAC el costo de crear anuncios, herramientas de seguimiento, IVA de las plataformas o el tiempo de tu equipo dedicado a campañas, el costo por cliente es más alto.
2. **El CAC sube al escalar**: Cuando aumentas el presupuesto, primero te comes a las audiencias más fáciles de convertir (las que ya buscan tu producto). A medida que gastas más, tienes que ir a audiencias más frías, por lo que el CAC suele subir entre un 20% y un 50% al duplicar el presupuesto.
3. **El churn de clientes pagos es mayor**: Tu 8% de churn probablemente incluye clientes orgánicos, que suelen tener mayor retención porque ya conocían tu producto. Los clientes que vienen por anuncios suelen tener un churn de 10-12% mensual, reduciendo aún más el LTV.
4. **Payback de casi 12 meses**: Tardarás ~11,8 meses en recuperar el CAC. Eso es casi igual a la vida media del cliente: recuperas tu inversión justo cuando el cliente promedio se va. No hay margen para imprevistos, y tienes que financiar 12 meses de pérdidas por cada cliente, lo que consume muchísima caja.

### Nota sobre tu rentabilidad actual:
Seguramente eres rentable gracias a clientes adquiridos por canales gratuitos (orgánicos, referidos), cuyo CAC es cero o muy bajo. Pero los clientes pagos tienen unit economics completamente distintas: meter $10.000 en publicidad no solo no te hará crecer de forma rentable, sino que reducirá tu rentabilidad general, o incluso te hará perder dinero si la proporción de clientes pagos crece mucho.

---

## ¿Qué necesitas para que apruebe los $10.000?
Primero, valida tus números con una cohorte exclusiva de clientes adquiridos por publicidad (no mezcles con orgánicos):
- Mide el CAC real de una campaña pequeña, no promedios generales.
- Mide el churn específico de esos clientes: suelen ser menos fieles.
- Calcula el LTV real de esa cohorte, no con fórmulas teóricas.

Segundo, necesitas alcanzar un LTV/CAC de al menos 3 (benchmark mínimo para escalar con seguridad en SaaS) y un payback menor de 6 meses (para no consumir demasiada caja). Para llegar ahí, prioriza estas palancas (por impacto):
1. **Reducir el churn**: Si bajas el churn de 8% a 3% mensual, la vida media pasa a 33 meses, el LTV sin descontar llega a ~$808, y la relación LTV/CAC es de 2,8 (casi el objetivo). Esta es la palanca con más retorno.
2. **Reducir el CAC**: Si logras bajar el CAC de $290 a $100 (mejorando creatividades, optimizando audiencias, aumentando la conversión de tu landing), la relación llega a 3,06.
3. **Aumentar el precio o el margen**: Si subes el precio a $60/mes, el margen pasa a $42/mes, el LTV sin descontar es de $525, y la relación es de 1,8. No es suficiente por sí solo, pero combina bien con otras medidas.

Tercero, no metas $10.000 de golpe: Empieza con una prueba de $1.000-$2.000, medir los resultados reales, y solo si los números cuadran, aumentas el presupuesto de forma gradual (máximo un 20-30% por mes) para evitar sorpresas con el aumento de CAC.

---

### Conclusión final:
Por ahora, no apruebo la inversión de $10.000. Tus cálculos tienen errores fundamentales que hacen que la publicidad pagada no sea rentable, o incluso perdedora en valor presente. Primero valida tus números con una cohorte de pagos, mejora las unit economics hasta alcanzar el ratio mínimo de 3, y luego escala de forma gradual.