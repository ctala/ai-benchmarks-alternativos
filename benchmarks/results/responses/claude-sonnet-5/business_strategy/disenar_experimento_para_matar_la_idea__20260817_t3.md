# Claude Sonnet 5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 6.79 | quality: 8.0
- latency_total: 43.804s | tokens_per_second: 76.2
- input_tokens: 289 | output_tokens: 3339

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El problema con tu hipótesis: mezcla 3 apuestas en una

"Agencias pequeñas pagarían $200/mes por reportes automatizados" en realidad son tres apuestas separadas:

1. El dolor de hacer reportes manuales es suficiente para pagar por resolverlo
2. $200/mes es el precio que aceptarían (no $20, no $500)
3. Pagarían **antes** de ver el producto, no solo dirían "sí me interesa"

La #3 es la que mata el 80% de las startups. Todo el mundo dice "sí, me gustaría" en una encuesta. Nadie dice eso cuando le pides la tarjeta.

---

## El experimento: Preventa con fricción real (no encuesta)

**No vas a preguntar si les gustaría. Vas a intentar cobrarles antes de construir nada.**

### Paso 1 — Define el ICP exacto (30 min, gratis)
No "agencias pequeñas de marketing" en general. Sé específico:
- Agencias de 3-15 empleados
- Que atienden a 5+ clientes activos simultáneos
- Que ya usan Google Data Studio/Looker Studio o Excel manual para reportar

Esto importa porque si fallas, necesitas saber en QUÉ segmento falló.

### Paso 2 — Crea una landing de preventa (1 día, $0-20)
Una sola página. No un producto, no un demo funcional. Solo:
- Headline: el dolor ("Dejar de armar reportes a mano cada mes")
- 3 bullets de lo que resuelve
- Precio visible: **$200/mes**
- Botón: "Reserva tu lugar — depósito de $50 reembolsable"
- El botón lleva a un Stripe Payment Link real que cobra $50 ahora

El depósito reembolsable es la clave. Es suficiente fricción para filtrar a los que solo "tienen curiosidad" de los que realmente lo necesitan. Si no te atreves a pedir dinero real, no vas a saber nada.

### Paso 3 — Outbound directo, no esperes tráfico (7-10 días, $0-100)
No hagas ads. Es lento y caro para esto. Ve directo:
- LinkedIn + email a 100 agencias que calzan tu ICP (Apollo.io o LinkedIn Sales Nav, plan free/trial sirve)
- Mensaje corto, sin pitch de venta, pidiendo una llamada de 15 min sobre cómo hacen reportes hoy

**No vendas en el mensaje. Vende en la llamada.**

### Paso 4 — La llamada (15 min, gratis, tu tiempo)
Estructura:
1. Preguntas de descubrimiento: "¿Cómo armas los reportes hoy? ¿Cuánto tiempo te toma? ¿Qué odias de eso?"
2. Si el dolor es real y coincide con tu hipótesis, ahí mismo: "Estoy armando algo para esto, cuesta $200/mes, ¿te interesa reservar tu lugar con un depósito de $50?"
3. Manda el link de Stripe en la llamada. Que paguen ahí, en vivo.

---

## Los números que definen la decisión

| Resultado | Contactos | Llamadas logradas | Depósitos pagados | Decisión |
|---|---|---|---|---|
| **Mata la idea** | 100 | <10 | 0-1 | Abandona o pivota el ángulo completamente |
| **Señal débil** | 100 | 10-15 | 2-3 | El dolor existe pero algo está mal (precio, segmento, mensaje) — no construyas aún, ajusta y repite |
| **Sigue** | 100 | 15+ | 4+ | Hay señal real de disposición a pagar — ahora sí vale la pena construir |

**El criterio de muerte concreto:** si contactas 100 agencias reales de tu ICP y consigues menos de 2 personas dispuestas a poner $50 de su bolsillo antes de ver nada, la hipótesis está muerta. No es "necesito mejor copy", es que el dolor no es suficientemente urgente o el precio está mal calibrado, y necesitas descubrir cuál antes de gastar 2 meses.

---

## Costo y tiempo total
- **Dinero:** $0-120 (landing + herramienta de prospección, opcional)
- **Tiempo:** 10-14 días calendario, no full-time
- **Tu inversión real:** ~15-20 horas de outbound y llamadas

---

## La trampa que debes evitar
Si consigues 3 llamadas donde te dicen "sí, me encantaría, cuando esté listo lo compro" pero nadie pone los $50 — **eso NO es señal positiva**. Es la mentira más común en customer discovery. La gente miente por educación cuando no hay dinero de por medio. Solo cuenta lo que pagan, no lo que dicen que pagarían.

Si en 10 días no logras que ni una sola persona ponga $50, no necesitas 2 meses de código para confirmarlo. Ya lo sabes.