# Kimi K2 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.16 | quality: 8.0
- latency_total: 26.753s | tokens_per_second: 34.9
- input_tokens: 224 | output_tokens: 934

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## Experimento: "La Landing que Miente"

**Duración:** 48-72 horas
**Costo:** $50-150 USD
**Trabajo real:** ~4 horas

---

## Qué haces (paso a paso)

### Día 1 (2 horas)
1. **Crea una landing en Carrd.co** ($19/año, o gratis con marca) o Notion + Super.so
2. **Copia específica que vende el dolor, no el producto:**
   - Headline: "Tus clientes dejan de molestarte por reportes. Automático."
   - 3 bullets del dolor: "Dejas de perder sábados", "Dejas de excusas con el cliente", "Un dashboard que ellos ven, tú no tocas"
   - Precio visible: **$200/mes** — no "$199", no "desde". El número exacto que testeas.
   - CTA: "Reserva tu acceso" (no "Compra", no "Prueba gratis")

3. **Formulario de "reserva":** Nombre, email, nombre de agencia, cuántos clientes manejan, tarjeta **no se carga**, solo se guarda (Stripe tiene "setup mode" o usa Typeform + aviso honesto: "te contactamos para activar")

### Día 2-3 (2 horas)
4. **LinkedIn outreach frío a 30 fundadores de agencias pequeñas** (2-10 empleados, servicios de marketing):
   - Busca "Founder at [Nombre] Agency" o "CEO at [Nombre] Marketing"
   - Mensaje de 2 líneas: *"Estoy armando algo para agencias que odian hacer reportes manuales. ¿Tienes 3 min para una pregunta rápida?"*
   - Si responden, mandas link. Si no, no insistas.

5. **Opcional acelerador:** $30-100 en LinkedIn ads micro-targeteadas (agencia owners, company size 1-10, marketing services) — solo si quieres velocidad.

---

## Métrica de muerte (abandonas si pasa esto)

> **Menos de 3 reservas con datos de tarjeta** de 50-100 visitantes cualificados.

No "registros de email". No "me interesa". **Reservas con intención de pago demostrada** (tarjeta guardada o mensaje de "¿cuándo cobran?").

---

## Por qué esto mata bien

| Trampa común | Tu defensa |
|-------------|-----------|
| "Me dijeron que les interesa" | Solo cuentan quienes dejan tarjeta |
| "Necesitan ver el producto" | El dolor es del reporte, no de la UI |
| "El precio asusta sin probar" | Si $200 asusta, tu modelo ya falló |
| "Hago MVP primero" | 2 meses de código vs 2 días de mentira |

---

## Resultados posibles y siguiente paso

| Escenario | Interpretación | Siguiente paso |
|-----------|---------------|--------------|
| 0-2 reservas | Precio, dolor o target mal | Pivota o mata. No sigas. |
| 3-5 reservas | Señal débil, no conclusiva | Testea con $150/mes y $300/mes para ver elasticidad |
| 6+ reservas | Señal fuerte | Ahora sí, construye lo mínimo para cobrar la primera |

---

## El principio que aplicas

> *"Si necesitas construirlo para saber si lo quieren, ya perdiste."*

Tu landing es **mentirosa intencional**: promete automación que no existe. No es ético cobrar. Pero es ético *ver* si hay manos levantadas antes de que exista el martillo.

**72 horas. $100. Una decisión real.**

¿Te atreves a que fracase?