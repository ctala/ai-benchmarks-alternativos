# DeepSeek V4 Pro (0813) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 44.275s | tokens_per_second: 63.2
- input_tokens: 281 | output_tokens: 2796

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

**No le doy.** Su cálculo tiene un error de aritmética y otro de concepto: **usted no tiene LTV/CAC de 2,9. Tiene ~1,1.**

Aquí está el recálculo como analista de unit economics.

### 1. El lifetime no es 24 meses
Con un churn mensual del 8%, la vida media de un cliente se calcula como:

**Vida media = 1 / churn mensual = 1 / 0,08 = 12,5 meses**

No 24 meses. Eso ya reduce su LTV a la mitad.

### 2. El LTV debe usar margen bruto, no ingreso bruto
Usted cobra $35/mes, pero solo retiene 70% de margen bruto:

**Contribución bruta mensual = $35 × 70% = $24,50**

Entonces el LTV bruto real es:

**LTV = $24,50 × 12,5 meses = $306,25**

### 3. Su LTV/CAC real
Con CAC de $290:

**LTV / CAC = $306,25 / $290 = 1,06**

Incluso si ignoráramos el margen bruto y usáramos los $35 completos:

**LTV (ingreso) = $35 × 12,5 = $437,50 → LTV/CAC = 1,51**

Nada cercano a 2,9. Y mucho menos a 3.

### 4. Qué significa meter $10.000
Con CAC de $290, adquiriría:

**$10.000 ÷ $290 = 34,5 clientes**

El LTV bruto total de esa cohorte sería:

**34,5 × $306,25 = $10.560**

Es decir, **recuperaría apenas la inversión publicitaria con un excedente bruto de ≈ $560**, antes de soporte, desarrollo, costos fijos, impuestos, etc. Eso probablemente es pérdida neta.

### 5. Payback period
**Payback = $290 / $24,50 = 11,8 meses**

Tarda casi un año en recuperar solo el costo de adquisición. Para escalar con capital propio, eso es demasiado lento y frágil: cualquier empeoramiento del churn o aumento del CAC lo deja en negativo.

### 6. Qué necesitaría para escalar con seguridad
Para tener LTV/CAC ≥ 3 con su contribución bruta actual ($306,25), el CAC debería ser:

**CAC objetivo = $306,25 / 3 ≈ $102**

Es decir, un tercio del CAC actual.

O, manteniendo CAC de $290, el LTV bruto debería ser:

**LTV objetivo = 3 × $290 = $870**

Eso implicaría una vida media de:

**$870 / $24,50 = 35,5 meses** → **churn mensual ≈ 2,8%**

O subir precio/margen bruto, o añadir upsells que aumenten drásticamente el LTV.

### Conclusión
No meta $10.000 todavía. Primero trabaje en:
- **Reducir CAC** (mejorar ads, landing, conversión, retargeting, orgánico).
- **Mejorar retención** (bajar churn de 8% a 5% ya duplica la vida media a 20 meses).
- **Aumentar margen bruto o ticket** (upsell, planes anuales, add-ons).

Con métricas actuales, escalar con publicidad pagada es quemar caja con un retorno marginal nulo. Pruebe con presupuestos chicos ($1.000–$2.000) y itere hasta lograr LTV/CAC ≥ 3 y payback < 6 meses. Después, escale.