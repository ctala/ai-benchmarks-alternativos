# KAT Coder Pro v2.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 7.14 | quality: 8.0
- latency_total: 28.874s | tokens_per_second: 64.8
- input_tokens: 179 | output_tokens: 1871

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa



## Experimento de Falsificación: "El Test del Dolor Real"

**Duración:** 5 días  
**Costo:** $0 - $50  
**Objetivo:** Descubrir si el problema es lo suficientemente doloroso como para que alguien saque la tarjeta ANTES de que el producto exista.

---

### Qué vas a hacer (paso a paso)

**Día 1-2: Identifica y contacta 40 dueños de agencias de marketing pequeñas (1-10 empleados)**

- No uses tu red. Busca en LinkedIn, Google Maps, directorios de agencias locales.
- Filtra: que tengan sitio web activo, que mencionen "reportes" o "reporting" en su contenido, que parezcan operar con varios clientes.
- Mensaje directo (email o LinkedIn):

> *"Hola [Nombre], estoy investigando un problema que tienen las agencias con los reportes a clientes. ¿Te molestaría si te hago 3 preguntas por teléfono? Toma 10 minutos. No te voy a vender nada."*

**Día 2-3: Las 3 preguntas (en llamada, no por email)**

1. *"¿Cuánto tiempo te toma preparar los reportes para tus clientes cada mes?"* (Cuantifica el dolor)
2. *"¿Has probado alguna herramienta para automatizarlo? ¿Qué pasó?"* (Valida que ya han intentado resolverlo)
3. *"Si existiera una herramienta que te ahorrara la mitad de ese tiempo por $200/mes, ¿la comprarías hoy?"*

**La pregunta trampa (Día 3-4):**

Si responden SÍ a la pregunta 3, dices:

> *"Justo estoy construyendo eso. Voy a lanzar una versión beta en 3 semanas a $200/mes. ¿Te interesa reservar tu lugar? Solo necesito que me des tu email y me confirmes que sí te interesa cuando esté lista."*

**Día 4-5: El test de fuego**

A los que dijeron que sí, les envías un email con un enlace a una landing page simple (Carrd, $19/año) que dice:

- Nombre del producto
- "Automatiza tus reportes. $200/mes."
- Botón: *"Reservar acceso anticipado — $1 hoy (reembolsable)"*

**El $1 es clave.** No es sobre el dinero. Es sobre el compromiso. Alguien que dice "sí, lo compraría" pero no pone $1, no lo comprará cuando esté listo.

---

### Costo total

- Dominio: $10 (opcional)
- Carrd: $19/año (o usa una landing gratuita de Notion/Carrd free tier)
- Stripe para cobrar $1: gratis
- **Total: $0 - $30**

---

### Criterio de ABANDONO (falsificación concluyente)

**Abandona la idea si:**

| Métrica | Resultado que mata la hipótesis |
|---------|--------------------------------|
| De 40 contactos, menos de 5 aceptan la llamada | El problema no es lo suficientemente visible/urgente |
| De las llamadas, menos de 3 dicen "sí, lo compraría" | El dolor no justifica $200/mes |
| De los que dicen "sí", NINGUNO pone $1 | Están siendo amables, no son compradores reales |

**Regla de oro:** Si después de 40 contactos cualificados y 10+ llamadas, **cero personas ponen $1**, la hipótesis está muerta. No construyas nada.

---

### Por qué este experimento funciona para FALSIFICAR

1. **No construyes software.** Si la hipótesis es falsa, solo perdiste 5 días y $30.
2. **Mides compromiso, no interés.** "Me interesa" es gratis. Poner $1 es compromiso.
3. **Hablas con extraños, no con amigos.** Los amigos te dicen lo que quieres oír. Los extraños te dicen la verdad.
4. **El criterio de abandono es binario.** O hay al menos 3 personas dispuestas a poner $1, o no. No hay "quizás", no hay "necesito más datos".

---

### Lo que NO debes hacer

- ❌ No construyas la landing page antes de hacer las llamadas (te enamoras del diseño)
- ❌ No hables con menos de 30 personas (muestra estadísticamente irrelevante)
- ❌ No aceptes un "me interesa" como validación (es la moneda más devaluada del mundo startup)
- ❌ No bajes el precio para "ver si así compran" (si no compran a $200, tu modelo de negocio no funciona)

---

**Si pasas el test** (3+ personas ponen $1): tienes señal suficiente para construir un MVP en 2 semanas y venderlo a esos 3 como beta testers.

**Si fallas el test:** acabas de ahorrarte 2 meses de construcción y miles de dólares. Busca otro problema.