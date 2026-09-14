# GLM 5.3 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 177.89s | tokens_per_second: 43.8
- input_tokens: 206 | output_tokens: 7785

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

# Veredicto: No. El plan muere en la segunda línea de aritmética.

Tus dos números clave se contradicen entre sí, y el error arrastra todo lo demás.

## Error 1: la vida promedio no es 24 meses, es 12,5

Con churn mensual de 8%, la vida esperada de un cliente es **1 / 0,08 = 12,5 meses**. No es opinión, es la fórmula. Con 8% mensual, solo el 13,5% de tus clientes (0,92²⁴) sigue vivo a los 2 años, y la mediana se va a los ~8 meses. O tu churn real es mucho menor que 8%, o tus clientes duran la mitad de lo que crees. **Averigua cuál de las dos es cierta antes de gastar un dólar**, porque cambia todo.

## Error 2: el LTV se calcula sobre margen, no sobre ingresos

El CAC lo pagas con plata real; lo que lo recupera es el margen de contribución, no el revenue.

- LTV en ingresos: $35 × 12,5 = $437,50
- **LTV en margen: $437,50 × 0,70 = $306**

(Nota al margen: ni con tu propia aritmética llegabas a 3 — $840 / $290 = 2,9.)

## Los números corregidos

| Métrica | Tu cálculo | Real |
|---|---|---|
| Vida promedio | 24 meses | 12,5 meses |
| LTV (margen) | $840 | **$306** |
| LTV/CAC | 2,9 | **1,06** |
| Payback | — | $290 / $24,50 ≈ **12 meses** |

Un ratio de 1,06 significa que cada cliente te deja ~$16 de margen bruto neto en toda su vida. Y el payback (12 meses) consume casi toda su vida útil (12,5).

## Qué compra tu $10.000

- ~34 clientes (10.000 / 290)
- ~$10.500 de margen bruto que vuelven a goteo de ~$845/mes durante un año
- Ganancia neta esperada: **~$560**, repartida en 12 meses — antes de que el CAC suba al escalar (y sube: subastas, saturación), antes de descontar el valor del dinero, antes de tu tiempo gestionando campañas

Le estás prestando $10.000 a Google/Meta por un año para recuperar ~$10.500. Peor que dejarla en el banco, con riesgo de churn incluido.

## El problema de fondo: balde roto

8% de churn mensual = **~63% de churn anual**. Se te va dos tercios de la base cada año. Escalar adquisición sobre eso es comprar agua para un balde agujereado.

## Qué tendría que ser cierto para aprobarlo

| Churn mensual | Vida | LTV margen | LTV/CAC |
|---|---|---|---|
| 8% (hoy) | 12,5 m | $306 | 1,1 |
| 6% | 16,7 m | $408 | 1,4 |
| 5% | 20 m | $490 | 1,7 |
| 4% | 25 m | $613 | 2,1 |
| ~2,8% | 36 m | $875 | **3,0** |

Para LTV/CAC ≥ 3 con CAC de $290 necesitas churn ≤ ~2,8% mensual. Alternativas: CAC ≤ ~$100 con el churn actual, o subir precio ~3x (optimista sin arreglar el churn antes).

## Mi dictamen

1. **Primero mide cohortes reales** y resuelve la contradicción entre churn y vida útil.
2. **Ataca el churn hasta ≤4% antes de meter un dólar en paid.** Es la palanca con más torque: bajar de 8% a 4% casi duplica tu LTV sin tocar nada más.
3. Si igual quieres probar paid: máximo **$1.500–2.000** como test, con CAC completamente cargado (creativos, herramientas, reembolsos, tu tiempo). No escales hasta que una cohorte recupere su CAC en ≤4 meses.
4. La rentabilidad que ya tienes seguro viene de canales baratos. No la diluyas con un canal que hoy destruye valor.

**Aprobado:** que necesitas crecer. **Rechazado:** este plan, tal como está. Vuelve cuando el churn esté en 4% o el CAC en $100, y lo hablamos con gusto.