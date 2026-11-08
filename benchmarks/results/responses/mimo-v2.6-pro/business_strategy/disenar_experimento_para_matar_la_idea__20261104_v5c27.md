# MiMo V2.6 Pro — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 7.12 | quality: 8.0
- latency_total: 90.175s | tokens_per_second: 34.5
- input_tokens: 199 | output_tokens: 3109

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El experimento que puede matar tu idea en 10 días y $0

## El principio

Tu hipótesis tiene 3 partes. Cada una puede morir:

1. **Existe dolor real** (pierden tiempo haciendo reportes)
2. **Valorizan ese dolor en ≥$200/mes**
3. **Lo comprarían AHORA**, no "algún día"

Los tests que preguntan "¿lo usarías?" solo atacan la #1 (y mal). La #2 y #3 solo se pueden probar con **dinero real**.

Por lo tanto: **el test es vender algo que no existe.**

---

## El test: "El hombre detrás de la cortina"

Vendes el resultado (reportes automáticos a clientes), pero lo entregas **a mano** durante 2 semanas. Cero código.

### Día 1 — El artefacto ($0, 2 horas)

Necesitas una sola cosa tangible que enseñar: **un reporte de cliente terminado**.

- Elige un tipo: "reporte mensual de ads (Meta + Google) con marca del cliente".
- Conéctate a las cuentas de 1-2 agencias amigas (o usa datos de un caso público), y genera **uno real** con Google Slides + Google Sheets + la API de Meta/Google (o copia-pega, da igual). Hazlo bonito. Que se vea lo que recibiría su cliente el día 1.
- Ese PDF/Slides ES tu producto. No hay más.

### Día 2 — La página ($0, 45 min)

Una sola página en Carrd/Notion/Framer gratis:

> **"Reportes de clientes que se solos solucionan"**
> Recibe cada mes el reporte de tus campañas, con tu marca y la de tu cliente, listo para enviar. Sin abrir Sheets.
> **$200/mes por agencia. Hasta 10 clientes.**
> [Reservar un piloto — cupos limitados a 10 agencias]

Sin pricing tiers. Sin demo. Sin "agenda una llamada". **Un solo botón que cobra.**

### Día 2-3 — La lista ($0, 4 horas)

Busca **50 agencias pequeñas** (2-10 personas). Fuentes: Clutch.co, LinkedIn ("digital marketing agency" + "founder/owner"), Instagram, directorios locales.

Criterio de calificación (aplica antes de escribirles):
- Tienen ≥3 clientes activos en gestión
- Muestran trabajo en redes/paid ads (no SEO puro)
- Son lo suficientemente chicas que el dueño hace los reportes

### Día 3-7 — El outreach (el corazón)

**50 mensajes personalizados.** Este es tu embudo:

```
Hola [nombre], vi que manejas las campañas de [cliente visible].
Pregunta rápida y sin rodeo: ¿cuántas horas al mes
te quema armar los reportes que le mandas a tus clientes?

Te pregunto porque estoy lanzando [nombre]: el reporte
mensual de Meta + Google Ads con tu marca y la del cliente,
listo para enviar el día 1. $200/mes por agencia.

Si te interesa, te dejo uno de muestra armado con los
canales que manejas: [link al reporte de ejemplo].

— [tu nombre]
```

**Nada de "¿te gustaría una demo?"** El ask es dinero.

### Día 5-15 — La entrega (Wizard of Oz)

Cuando alguien diga que sí:
1. Le pasas un link de pago (Stripe Payment Link, 10 min de setup).
2. Cobras $200 el mes 1 **por adelantado**.
3. Le pides acceso a sus cuentas de Ads (o exportaciones).
4. Cada lunes tú mismo armas el reporte en **20 minutos** con tu template de Sheets/Slides.
5. Le dices: "esto es el piloto, la plataforma sale en X semanas".

Eso es todo.

---

## Coste y tiempo

| | |
|---|---|
| **Dinero** | $0 (Stripe es gratis hasta cobrar; Carrd free tier; Sheets free) |
| **Tiempo** | ~25-30 horas repartidas en 10-14 días |
| **Riesgo** | Cero. Si no paga nadie, borras la página. |

---

## Los criterios de muerte — PRE-REGISTRADOS

Escríbelos en un papel **antes de enviar el primer mensaje**. Si no los cumples, abandonas. Sin "pero es que el mercado necesita educación".

| Umbral | Si ocurre | Decisión |
|---|---|---|
| De 50 outreach, **<10 respuestas** | El mensaje/dolor no resuena | **Muerte del segmento** (o del framing). Cambia segmento, no construyas. |
| De 10 conversaciones, **<3 dicen "sí, cóbrame"** | El dolor no vale $200 | **Muerte del precio o del producto.** No hay negocio a $200/mes. |
| De 3 compromisos, **0 pagos reales** | "Sí" educado, no demanda | **Muerte de la idea.** Abandona. |
| **<2 clientes pagan y renuevan el mes 2** | No hay retención ni dolor recurrente | **Muerte.** El producto es un nice-to-have. |
| **≥3 pagan $200 sin pelear el precio** | Señal fuerte | Construye el MVP. Ya sabes quién lo compra y qué reporte quiere. |

Nota: si alguien negocia a $100, eso **no** mata la hipótesis a $200 — pero te dice que el precio está en $100-150 y tu modelo cambia.

---

## Por qué este test y no otros

**❌ Landing + Facebook Ads + "join the waitlist"**
Cuesta $300 y te da 50 emails de gente curiosa. Un email no es dinero. Nunca sabrías si habrían pagado $200 o $20.

**❌ 30 entrevistas de discovery**
Te van a decir "sí, suena genial" porque son amables y porque no les cuesta nada decir que sí. Las entrevistas sirven para **aprender el flujo de trabajo**, no para validar demanda. Úsalas SOLO para afinar el mensaje.

**❌ Construir un MVP de 2 semanas y regalarlo**
"¿Lo usarías gratis?" responde la pregunta equivocada. Lo gratis no prueba precio.

**✅ Vender antes de construir**
Un solo pago de $200 de un desconocido vale más que 100 encuestas. Y un solo silencio tras enviar 50 mensajes bien hechos es evidencia suficiente para matar todo.

---

## Lo que haces si sobrevive

No construyas el software todavía. Repite el mismo test 4 semanas más, hasta **10 clientes pagando** a mano. Ahí:
- Sabes el reporte exacto que quieren (no lo adivinas)
- Tienes $2.000 MRR para justificar las 2 meses de código
- Tienes 10 clientes listos para migrar el día del launch

Y si muere: perdiste 10 días y $0. Eso es exactamente lo que querías.