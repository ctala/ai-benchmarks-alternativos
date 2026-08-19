# Seed 2.1 Turbo — business_audit/escalar_con_ltv_mal_calculado

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.31 | quality: 10.0
- latency_total: 115.976s | tokens_per_second: 63.0
- input_tokens: 249 | output_tokens: 7309

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

No, rotundamente. Tu cálculo tiene dos errores gravísimos que hacen que tu LTV/CAC real sea 3 veces menor al que crees, y que casi pierdas dinero por cada cliente que adquieras. Vamos a desglosarlo paso a paso:

---

### Error 1: Sobrestimas la duración de los clientes de forma brutal
Tu estimación de "2 años por cliente" no coincide con el churn mensual del 8% que declaras. La vida media de un cliente con churn constante se calcula como `1 / churn mensual`:
- Vida media real = 1 / 0,08 = **12,5 meses** (no 24).
- La mitad de tus clientes se van antes de los 8 meses y medio (mediana de duración).
- Solo el 13% de los clientes llega a los 2 años que mencionas (cálculo: 0,92²⁴ ≈ 0,135).

Es un sesgo muy común: recordamos a los clientes fieles que se quedan años, y olvidamos a la mayoría que se va a los pocos meses. Los números del churn no mienten.

---

### Error 2: Calculas el LTV con ingresos brutos, no con el margen que realmente te queda
El LTV (Valor de Vida Útil) que compara con el CAC es el dinero neto que te deja cada cliente para cubrir gastos fijos y generar beneficio. No los ingresos totales: el 30% de cada pago se va directamente en infraestructura y procesador de pagos, ese dinero nunca pasa por tu caja.
- Margen mensual real por cliente = $35 × 70% = **$24,5** (no $35).

---

### Los números reales (tu unidad económica verdadera)
| Indicador | Tu cálculo erróneo | Valor real (sin descontar flujos) | Valor real (descontado 2% mensual*) |
|-----------|---------------------|------------------------------------|--------------------------------------|
| Vida media del cliente | 24 meses | 12,5 meses | 10 meses |
| LTV | $840 | $306,25 | $245 |
| LTV/CAC | 2,9 | **1,06** | **0,84** |

*Tasa de descuento razonable para startups (costo de capital + inflación + riesgo): el dinero que pagas hoy por el CAC vale más que el dinero que recibes dentro de 12 meses.

---

### ¿Qué significa esto en la práctica?
Tu ratio LTV/CAC real es de ~1,06: prácticamente recuperas el costo de adquisición justo antes de que el cliente promedio se vaya.
- El periodo de recuperación del CAC (payback) es de `290 / 24,5 ≈ 11,8 meses`: casi toda la vida del cliente se va solo en devolverte el dinero de la publicidad.
- Solo te quedan 0,5 meses de margen (~$12 por cliente) para cubrir salarios, alquiler, impuestos y cualquier otro gasto fijo.
- Si el churn sube solo 1 punto porcentual (a 9% mensual, algo muy común cuando escalas publicidad y atraes clientes menos calificados), ya no recuperas ni el CAC: pierdes dinero con cada cliente.

Si metes $10.000 este mes:
- Adquirirás ~34 clientes.
- En toda su vida, esos clientes te generarán ~$10.400 de margen bruto total.
- O sea, por invertir $10k hoy, te quedan $400 de "beneficio" en más de un año, sin contar ningún gasto adicional. Si descontamos el valor del dinero en el tiempo, pierdes alrededor de $1.500.

Por cierto: el ratio LTV/CAC de 3 no es un número "más o menos", es el mínimo recomendado para un SaaS escalable y saludable. Ese margen sirve para cubrir gastos fijos, costos indirectos de marketing, riesgos operativos y dejar beneficio para reinvertir. Tu ratio está en la mitad de lo mínimo aceptable.

---

### ¿Qué haces antes de escalar?
Ya eres rentable, así que tienes margen para arreglar la unidad económica antes de tirar dinero en publicidad. Las palancas prioritarias son:
1. **Bajar el churn (la más impactante):** Si logras bajar el churn mensual al 4%, la vida media sube a 25 meses, el LTV pasa a $612,5 y el LTV/CAC llega a ~2,1. Si lo bajas al 3%, el ratio llega a ~2,8, casi en el mínimo recomendado. Empieza por analizar por qué se van los clientes en los primeros meses (que son la mayoría) y arregla esas fricciones.
2. **Validar el churn de clientes de pauta:** El churn que usaste probablemente sea de tu base total (incluyendo orgánicos o recomendados). Los clientes adquiridos por publicidad suelen tener un 20-50% más de churn, así que el LTV real de los clientes de pauta será aún menor. Prueba con un presupuesto chico ($1.000) antes de escalar para medir este dato.
3. **Bajar el CAC:** Si optimizas tus campañas y logras bajar el CAC a $100, con los números actuales ya tienes un LTV/CAC de ~3,1. Pero ojo: bajar el CAC es más difícil de controlar que el churn, porque depende de plataformas y competencia.
4. **Subir el precio o agregar monetización:** Si subes el precio a $50/mes (manteniendo el 70% de margen), el LTV pasa a $437,5 y el ratio a ~1,5. Mejora, pero no es suficiente por sí solo. Combínalo con reducción de churn o planes anuales (que reducen el churn y te dan el dinero por adelantado).

---

### Recomendación final
No metas $10.000 este mes. Trabaja primero en reducir el churn hasta que el LTV/CAC esté al menos en 2,5 y el payback sea menor de 8 meses. Mientras tanto, prueba con un presupuesto de prueba de $1.000 para medir el churn real de los clientes adquiridos por publicidad y validar que tu CAC se mantiene cuando escalas. Escalar con una unidad económica rota solo te hace perder dinero más rápido.