# Claude Opus 4.8 (suscripción) — business_strategy/plan_aritmetica_no_cierra

- model_id: `claude-opus-4-8`
- success: True  | final: 6.78 | quality: 8.4
- latency_total: 95.303s | tokens_per_second: 60.3
- input_tokens: 4 | output_tokens: 5743

## Respuesta completa

## No. El plan no llega. Se queda en el 30% del objetivo.

Antes de discutir si los porcentajes son "sanos", hay que multiplicarlos. Con los números del propio plan:

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas | — | 200.000/mes |
| Captura 1,5% | 200.000 × 0,015 | **3.000 suscriptores/mes** |
| Compra 2% | 3.000 × 0,02 | **60 compradores/mes** |
| Ticket $30 | 60 × 30 | **$1.800/mes** |

**$1.800, no $6.000.** Faltan $4.200. El plan está 3,3x corto usando *sus propios supuestos*, sin que yo cuestione ni un número.

Y eso es bruto. Descontando comisiones de pago (3,5-5% en LATAM) y reembolsos (~5-8%), quedan ~$1.600 netos.

---

## Los tres errores, en orden de gravedad

### 1. El "recurrente" no existe

Un curso de $30 se compra **una vez**. Quien compró no vuelve a comprar el mismo curso el mes siguiente. Tu motor no es la lista acumulada, es el **flujo de suscriptores nuevos**: ~3.000/mes. Ese flujo produce ~60 ventas/mes y se acabó. No hay recurrencia, hay repetición del mismo esfuerzo.

**Sospecho de dónde salió el $6.000:** alguien aplicó el 2% sobre la lista *acumulada*. Mes 6 = 18.000 suscriptores × 2% × $30 = $10.800. Suena hermoso y es falso: estás cobrándole el mismo curso, seis veces, a la misma gente. La lista se quema. Cada cohorte compra una vez y pasa a ser inventario muerto para ese producto.

Pregúntale a tu socio si el cálculo fue sobre lista acumulada. Si dice que sí, ahí está la fuga.

### 2. Los porcentajes no son conservadores. Son el techo.

- **1,5% visita→suscriptor** con un formulario a secas: el rango real es 0,5%–1,5%. Estás usando el borde superior. Conservador sería 0,8%.
- **2% suscriptor→venta** de un producto pagado a tráfico frío evergreen: lo típico es 0,5%–1%. El 2% se ve en lanzamientos a listas calientes, no en un embudo automático alimentado por SEO.

Y el problema no es cada número: es que **se multiplican**. Dos supuestos "un poco optimistas" se convierten en uno muy optimista.

| Escenario | Captura | Venta | Compradores | Ingreso |
|---|---|---|---|---|
| Pesimista | 0,8% | 1% | 16 | **$480** |
| Base (el tuyo) | 1,5% | 2% | 60 | **$1.800** |
| Optimista | 3% | 3% | 180 | **$5.400** |

Lee esa última fila. **Tu escenario optimista tampoco llega a $6.000.** Un plan donde el mejor caso posible no alcanza la meta no es un plan conservador: es un plan sin margen.

### 3. Falta el reverso

Para $6.000/mes con ticket de $30 necesitas **200 ventas/mes**. Eso exige una de estas:

- Conversión suscriptor→venta de **6,7%** (no 2%), o
- **10.000 suscriptores nuevos/mes**, o sea **667.000 visitas** (3,3x tu tráfico).

Ninguna de las dos aparece en el plan. Nadie corrió la división.

---

## Qué sí llega (con la misma gente y el mismo tráfico)

El cuello no es el tráfico ni la conversión. Es **el ticket de $30 y el modelo de una sola venta**.

**Palanca A — Subir el valor por comprador.** Con 60 compradores/mes, necesitas un **AOV de $100** para hacer $6.000. Ruta: curso $30 como puerta de entrada + order bump ($50) + producto de fondo ($250). Si 30% de los 60 toman el backend: 60 × ($30 + 0,30 × $250) = **$6.300**. Es la vía con menos supuestos nuevos — no requiere más tráfico ni mejor conversión, solo algo más que vender.

**Palanca B — Recurrencia de verdad.** Membresía de $30/mes en vez de curso de $30. **200 miembros activos = $6.000 MRR.** Con 60 altas/mes y churn 8%, cruzas los 200 alrededor del mes 4 y el techo queda en ~750. Esta es la única versión donde la frase "$6.000/mes recurrentes" es literalmente cierta.

**Palanca C — Arreglar el embudo.** Lead magnet real (captura 3%) + secuencia de email decente (venta 4%): 6.000 subs × 4% = 240 × $30 = $7.200. Funciona, pero exige que **dos** apuestas salgan bien al mismo tiempo. Es la de mayor riesgo de ejecución.

Mi recomendación: **A + B**. Front-end de $30 que empuja a membresía de $30/mes. Los $6.000 dejan de depender de vender 200 cursos cada mes, para siempre.

---

## Antes de comprometer 6 meses, gasta 3 semanas

Tienes cero datos propios. El 1,5% y el 2% son benchmarks de internet, no mediciones tuyas.

1. **Semana 1-2:** pon el formulario. Mide la captura real sobre tus 200.000 visitas.
2. **Semana 3:** véndele el curso a los primeros ~500 suscriptores. Mide la conversión real.

Con esos dos números, el modelo se recalcula solo y deja de ser una discusión de opiniones.

Tres preguntas para tu socio mientras tanto:
1. **¿200.000 son sesiones o usuarios únicos?** Y de esos, ¿qué fracción tiene intención de compra vs. tráfico informativo que rebota? Si es SEO de artículos genéricos, la captura real va a estar más cerca del 0,5%.
2. **¿De dónde salió el 2%?** ¿Le vendiste algo antes a esta audiencia, o es un número que leíste?
3. **¿El $6.000 lo calculaste sobre lista acumulada?**

**Veredicto: no lo apruebo tal como está.** No porque los porcentajes sean absurdos —son discutibles pero defendibles—, sino porque **con sus propios números el plan hace $1.800 y la meta es $6.000**. El plan no murió en los supuestos. Murió en la multiplicación.