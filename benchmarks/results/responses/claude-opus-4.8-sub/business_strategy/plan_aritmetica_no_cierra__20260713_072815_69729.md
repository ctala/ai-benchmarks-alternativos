# Claude Opus 4.8 (suscripción) — business_strategy/plan_aritmetica_no_cierra

- model_id: `claude-opus-4-8`
- success: True  | final: 4.05 | quality: 4.4
- latency_total: 71.915s | tokens_per_second: 56.0
- input_tokens: 4 | output_tokens: 4029

## Respuesta completa

## No. El plan, con sus propios números, llega a $1.800/mes. No a $6.000.

Hagamos la multiplicación que el plan no hizo:

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas | — | 200.000 |
| → Suscriptores (1,5%) | 200.000 × 0,015 | **3.000** |
| → Compradores (2%) | 3.000 × 0,02 | **60** |
| → Ingreso (× $30) | 60 × 30 | **$1.800** |

**Gap: $4.200/mes. El plan cumple el 30% del objetivo.** Y eso es bruto: descontando comisión de pasarela (~5%) y reembolsos (~5-10%), quedan ~$1.550 netos. Cumple el 26%.

Tu socio tiene razón en que los porcentajes son sanos. Ese no es el problema. El problema es que porcentajes sanos multiplicados entre sí dan un número chico, y nadie hizo la multiplicación.

---

## Tres errores más, aparte de la aritmética

**1. "$6.000 recurrentes" es falso por definición.** Un curso de $30 de pago único no genera MRR. Genera $1.800 el mes 1, $1.800 el mes 2… ingreso *repetido*, no *recurrente*. La diferencia importa: si mañana cae el tráfico, cae el ingreso completo el mismo mes. No hay base instalada.

**2. La lista crece, los compradores no.** Es el error que hace que este plan "se sienta" escalable. Mes 6 tienes 18.000 suscriptores acumulados — pero no puedes venderles el mismo curso dos veces. El 2% aplica sobre *suscriptores nuevos*, no sobre la lista total. Tu ingreso es plano en $1.800, no creciente.

**3. 200.000 visitas ≠ 200.000 personas.** El 1,5% se aplica sobre visitantes únicos nuevos, no sobre sesiones. Si tienes 60.000 únicos con 3+ sesiones cada uno, tu pool real es 3x más chico y el plan baja de $1.800 a ~$540. **Este dato lo tienes en Analytics hoy. Míralo antes de seguir leyendo.**

---

## Qué tendría que ser verdad para llegar a $6.000

Necesitas un 3,3x. Una sola palanca, aislada:

| Palanca | De → A | ¿Creíble? |
|---|---|---|
| Precio | $30 → **$100** | Posible, pero es otro producto |
| Visita→sub | 1,5% → **5%** | No. 5% site-wide casi no existe |
| Sub→compra | 2% → **6,7%** | No en evergreen frío |
| Tráfico | 200k → **667k** | Es otro plan, de 18 meses |

Ninguna palanca sola aguanta. Un combo sí:

**1,5% → 2,5%** (lead magnet específico en vez de "suscríbete") × **2% → 3%** (secuencia de venta, no un solo email) × **$30 → $79** (curso + plantillas + sesión grupal) = 5.000 subs × 3% × $79 = **$11.850/mes**.

Eso sobrecumple. Pero son tres apuestas encadenadas, y si las tres fallan a la mitad, vuelves a $1.800.

---

## Y si de verdad quieres *recurrente*

Membresía a $30/mes en vez de curso único. Para $6.000 MRR necesitas **200 miembros pagando simultáneamente**.

- Optimista: 60 altas/mes, churn 8% → cruzas 200 miembros ~mes 4. Funciona.
- Realista: la conversión a suscripción suele ser la mitad que a un único. 30 altas/mes, churn 10% → techo en 300 miembros, cruzas 200 alrededor del **mes 8-9**. Fuera de tu ventana.

Es el camino correcto, pero no en 6 meses con este tráfico. Sé honesto con esa fecha antes de comprometerla.

---

## Qué haría yo esta semana, en vez de aprobar

No discutan más los supuestos. Son baratos de medir:

1. **Hoy:** Analytics → visitantes únicos nuevos/mes. Si no son ~200k, todo el plan se recalcula.
2. **Semana 1-2:** pon el formulario. Mide el 1,5% real. Costo: ~cero.
3. **Días 15-45:** vende a los primeros suscriptores. Mide el 2% real.

En 45 días tienes los dos números reales y el precio deja de ser una discusión de opiniones. **Si el resultado es $1.800, ya lo sabes ahora — la pregunta no es si aprobar el plan, sino si aprobar $1.800/mes como piso mientras construyes la palanca que falta.**

Eso sí lo aprobaría. Lo que no apruebo es ejecutar 6 meses creyendo que vas a $6.000.