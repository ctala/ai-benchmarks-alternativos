# Claude Opus 4.8 (suscripción) — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `claude-opus-4-8`
- success: True  | final: 6.8 | quality: 8.4
- latency_total: 98.346s | tokens_per_second: 53.5
- input_tokens: 4 | output_tokens: 5266

## Respuesta completa

## Primero: tu hipótesis no es una, son cuatro

"Las agencias pequeñas pagarían $200/mes por automatizar reportes" esconde 4 supuestos, y solo uno te va a matar:

1. Hacer reportes les duele (tiempo real, no imaginario)
2. Ese dolor NO está ya resuelto (AgencyAnalytics, Whatagraph, DashThis, Swydo, Looker Studio gratis)
3. Vale $200/mes para ellos (no $29)
4. Te lo pagan **a ti, hoy, sin producto**

El supuesto 2 es el que probablemente te mata, y lo puedes matar en 3 horas. El supuesto 4 es el único que da evidencia real. Los demás son ruido.

---

## Test 0 — El kill de 3 horas, costo $0

Antes de hablar con nadie: **auditar competencia**.

Lista los tools que ya hacen exactamente esto y su precio real. Si encuentras ≥4 players establecidos cobrando entre $60 y $180/mes, con miles de agencias pagando, entonces tu hipótesis ya no es "¿pagarían $200?" sino **"¿por qué cambiarían de algo que ya funciona a $60, para pagarte $200 a ti?"**.

**Criterio de muerte parcial:** si no puedes escribir en UNA frase por qué alguien deja AgencyAnalytics por lo tuyo, y esa frase no es "porque es más lindo" → paraste 2 meses de trabajo con una tarde de Google. Ya ganaste.

Si sobrevives, sigues.

---

## Test 1 — Concierge pre-sale (el que sí mata)

**La idea:** no construyes nada. Vendes el resultado y lo entregas **a mano** durante 30 días. Si no puedes vender la versión manual a $200, ningún software lo va a arreglar. El software solo abarata TU costo, no aumenta el valor de ellos.

### La oferta exacta

> *"Estoy armando una herramienta que automatiza los reportes mensuales a clientes de agencia. Mientras la construyo, tomo 3 agencias founding: yo hago tus reportes este mes, a mano, con tu branding, en tu formato. $200. Si en 30 días no te ahorra al menos 4 horas, te devuelvo el 100%. ¿Te sirve?"*

Link de pago Stripe. **La tarjeta se pasa hoy.** La garantía de devolución baja el riesgo de ellos y no contamina tu señal: igual tuvieron que sacar la tarjeta.

### Por qué esto y no una landing con waitlist

Un email en una waitlist vale ~$0 y miente. Un "sí, lo pagaría" en una encuesta vale menos que $0: te da falsa confianza y te compra 2 meses de trabajo. **Solo la tarjeta dice la verdad.**

### El segmento (aquí se juega el test)

No cualquier agencia. Filtro duro:
- 3–15 personas (el freelancer no paga $200; la agencia de 50 tiene equipo interno)
- 5–30 clientes activos
- Reportan mensualmente a clientes (paid media, SEO, social)

60 agencias en la lista. Sácalas con Apify/LinkedIn/Clutch/directorios de partners de Meta y Google. 2 horas.

---

## El plan día por día

| Día | Qué haces | Horas |
|---|---|---|
| 1 | Auditoría competitiva (Test 0). Decides seguir o parar. | 3 |
| 1–2 | Lista de 60 agencias del segmento exacto | 3 |
| 2 | Landing de 1 página + link de pago Stripe (Carrd/Framer). Sin demo, sin video, sin producto. | 3 |
| 3–7 | Outreach: 60 mensajes, 20 personalizados de verdad (LinkedIn DM + email). Meta: 20 conversaciones. | 8 |
| 5–12 | Conversaciones. En cada una: la pregunta de las horas (abajo) + la oferta + el link | 8 |
| 12 | Cierre y veredicto | 1 |

**Total: ~26 horas de trabajo, 12 días calendario.**
**Costo cash: $50–150** (dominio + landing + créditos de scraping). Stripe no cobra si no vendes.

Compáralo con 2 meses = ~320 horas y costo de oportunidad de todo lo demás.

---

## La pregunta que mata dentro de la conversación

No preguntes "¿pagarías?". Pregunta por el pasado, que no se puede inventar:

1. **"Muéstrame el último reporte que le enviaste a un cliente."** (Si no te lo muestra, no hay dolor.)
2. **"¿Cuántas horas te tomó armar todos los del mes pasado?"**
3. **"¿Qué usas hoy y cuánto pagas?"**
4. **"La última vez que buscaste una solución a esto, ¿qué probaste y por qué lo dejaste?"**

**Kill matemático:** $200/mes contra un costo/hora de agencia de $50–80 exige ahorrar mínimo 3h/mes solo para empatar, y en la vida real la gente compra con 3–5x de ROI → necesitas que hoy pierdan **8–10 horas al mes** en esto. Si la respuesta modal es "2 horas, lo hace mi junior con una plantilla" → **la hipótesis está muerta por aritmética**, sin importar cuán simpáticos sean en la llamada.

---

## Criterios de abandono (escríbelos ANTES de empezar, sin renegociar después)

| Señal | Umbral | Veredicto |
|---|---|---|
| Competidores establecidos ≤$180 y sin cuña defendible en 1 frase | sí | **Muerta** (o pivota la cuña, no construyas) |
| Horas/mes reportadas en reportes | mediana <5h en 20 conversaciones | **Muerta por aritmética** |
| Ya tienen tool y no se quejan sin que preguntes | >70% | **Muerta** (dolor resuelto) |
| **Pagos reales a los 12 días** | **0 de 20 conversaciones** | **Muerta. Abandonas.** |
| Pagos reales | 1 de 20 | Zona gris → 1 semana más, probablemente precio/segmento mal |
| Pagos reales | **≥3 de 20** | Sobrevive. Y aun así entregas manual 30 días antes de escribir código |

---

## Falso negativo: el error que te va a costar caro

Si mandas 60 mensajes y recibes 2 respuestas, **no mataste la hipótesis: mataste tu canal de outreach.** Son cosas distintas y confundirlas te hace tirar ideas buenas.

Regla: **el veredicto de muerte solo es válido con ≥20 conversaciones reales.** Si no llegas a 20 con cold outreach, consigue el acceso por otro lado (comunidades de agencias, tu red, un partner que ya les venda) antes de declarar nada. Sin conversaciones no hay dato, hay silencio.

---

## Lo que NO haces en estos 12 días

- Ni una línea de código
- Ni encuesta ("¿pagarías por…?" = basura)
- Ni waitlist de emails
- Ni demo, ni mockup, ni video de producto
- Ni "validación" con amigos que tienen agencia

---

## El punto incómodo

Este experimento tiene una trampa deliciosa: si vendes los 3 pilotos a $200 y haces los reportes a mano un mes, vas a descubrir **exactamente qué reporte quieren** — y probablemente no es el que ibas a construir. Ese es el verdadero premio, no el "sí".

Y si nadie paga: perdiste 26 horas y $100 en vez de 2 meses. Eso también es ganar.