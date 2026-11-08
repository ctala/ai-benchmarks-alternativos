# Muse Wonder — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta/muse-wonder`
- success: True  | final: 8.31 | quality: 10.0
- latency_total: 17.367s | tokens_per_second: 111.7
- input_tokens: 203 | output_tokens: 1940

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

No. No le des. Tu plan muere en 3 errores de aritmética:

### 1. Un cliente NO se queda 2 años

Con un churn mensual del 8%, la vida media es:

**Vida media = 1 / Churn = 1 / 0,08 = 12,5 meses**

No 24 meses.

De hecho, después de 24 meses solo te queda el 13,5% de una cohorte: `0,92^24 = 0,135`. Estás contando casi el doble de vida de la que tienes.

### 2. Tu LTV no es $840, es $306

Calculaste LTV en ingresos, no en margen. Para compararlo con el CAC tienes que usar el margen bruto.

```
LTV ingresos = $35 x 12,5 meses = $437,50
LTV margen bruto = $437,50 x 70% = $306,25
```

Ese es el dinero real que un cliente te deja para pagar publicidad, sueldos, y todo lo demás.

### 3. Tu LTV/CAC no es 2,9. Es 1,06

```
LTV / CAC = $306,25 / $290 = 1,06
```

No estás "más o menos en 3". Estás apenas por encima de 1.

Eso significa que por cada $290 que gastas hoy, esperas recuperar $306... repartidos en los próximos 12,5 meses, antes de sueldos, impuestos, soporte y costos fijos. En la práctica, pierdes dinero.

Peor aún, el payback:

```
Payback = CAC / Margen mensual por cliente
Payback = $290 / ($35 x 70%) = $290 / $24,50 = 11,8 meses
```

Necesitas que un cliente se quede 11,8 meses solo para recuperar su adquisición, pero la vida media es 12,5 meses. Solo el ~37% de tus clientes llegará a ser rentable individualmente. La mitad se irá antes de los 8,3 meses.

### Qué pasa si metes los $10.000

```
$10.000 / $290 = 34 clientes aprox.
Retorno bruto esperado = 34 x $306,25 = $10.562
```

Ganancia esperada: **$562 en más de un año**, antes de cualquier otro costo, y asumiendo que el CAC no sube al escalar — que casi siempre sube. Si el churn pasa de 8% a 9%, ya pierdes.

Ser rentable con clientes orgánicos no significa que puedas comprar clientes rentablemente.

### Qué tendrías que arreglar antes de escalar

Para tener un LTV/CAC = 3 con tus números actuales, necesitarías una de estas:

1. **Bajar el CAC a ~$102** ($306 / 3), un 65% menos.
2. **Bajar el churn a 2,8% mensual** (de 8%), para llegar a 35 meses de vida media.
3. Una combinación de ambas.

**Veredicto: No aprobado para escalar.**

Primero retención y CAC. Prueba canales con $500-$1.000 para validar, pero no metas $10.000 a un canal que devuelve 1,06x.