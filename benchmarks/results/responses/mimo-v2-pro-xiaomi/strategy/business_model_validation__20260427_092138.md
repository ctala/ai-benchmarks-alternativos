# MiMo V2-Pro (Xiaomi direct) — strategy/business_model_validation

- model_id: `mimo-v2-pro`
- success: True  | final: 7.67 | quality: 9.06
- latency_total: 44.755s | tokens_per_second: 43.3
- input_tokens: 430 | output_tokens: 1937
- judge_score: 4.4 | justificación: 

## Respuesta completa

# 🔥 La versión sin filtro

## 1. Los 5 riesgos principales

**Riesgo 1: El infierno del chicken-and-egg**
Nadie viene si no hay nadie. Necesitas proveedores para atraer restaurantes y restaurantes para atraer proveedores. ¿Cuál resuelves primero? Y no me digas "los dos al mismo tiempo" porque con $10K eso es fantasía.

**Riesgo 2: Te van a sacar del medio (disintermediation)**
El restaurante descubre al proveedor por tu app, le gusta, y la próxima vez le llama directo. Tu plataforma se convierte en un directorio gratuito. ¿Por qué pagarían 15% recurrentemente si ya tienen el número?

**Riesgo 3: El 15% es suicidio en un negocio de márgenes brutales**
Un restaurante pequeño tiene márgenes netos del 5-10%. Les estás pidiendo que te paguen más de lo que ellos ganan. Un proveedor que vende tomates con margen del 20% no te va a ceder el 15%. Te van a odiar a los dos lados.

**Riesgo 4: Relaciones informales y cash**
En LATAM, el 70%+ de estos negocios opera en efectivo, con proveedores que son "el primo del vecino" que truye cosas de la central de abastos. No tienen ni factura. Tu modelo asume transacciones digitalizables que quizás no existen.

**Riesgo 5: Ticket promedio bajísimo = unit economics imposibles**
Si un restaurante pequeño compra $200 USD en ingredientes por pedido, tu comisión es $30. ¿Con cuántos pedidos pagas adquisición de usuario, operaciones, soporte, y todavía dejas margen? Spoiler: muchos.

---

## 2. ¿Por qué NO funciona en LATAM específicamente?

- **Desconfianza digital**: El dueño de taquería no confía en una app para lo que le llega mañana a las 6am. Si falla, no abre. No es Uber Eats donde es "nice to have".
- **Infraestructura de logística fragmentada**: No hay un FedEx de ingredientes frescos. Cada proveedor entrega en su camioneta con su ruta. ¿Quién resuelve el last-mile de producto perecedero? Tú no, con $10K.
- **Regulación inconsistente**: Facturación, impuestos, permisos sanitarios varían por país, por ciudad, por barrio. Tu app tiene que ser compliant en 15 jurisdicciones si escalas.
- **Cultura de relación personal**: "Mi proveedor me fía cuando estoy mal", "me deja cambiar pedido a las 10pm", "me truye extras sin cobrar". Tu app no reemplaza eso.
- **Internet y smartphones no son universales**: El cocinero que recibe el pedido a las 5am no tiene smartphone, o no tiene datos, o no sabe usar la app.

---

## 3. ¿Qué tendría que ser VERDAD para que funcione?

| Assumption | Qué tan probable es |
|---|---|
| Los restaurantes SÍ tienen dolor real (no solo inconveniencia menor) | **Media** — muchos ya tienen sistemas que "funcionan suficiente" |
| Están dispuestos a pagar 15% por la conveniencia | **Baja** — especialmente si el margen del restaurante es del 8% |
| Los proveedores quieren más clientes y aceptan la comisión | **Media-alta** — si no les cuesta nada operacionalmente |
| Una vez en la plataforma, se quedan (retención) | **Baja** — alta probabilidad de disintermediation |
| Puedes logísticamente entregar ingredientes frescos sin ser tú el proveedor | **Muy baja** — esto es el problema de verdad |
| El mercado es suficientemente denso geográficamente para que funcione el marketplace | **Depende de la ciudad** |

**La assumption #1 que si falla, todo se cae**: *Los restaurantes tienen suficiente dolor como para cambiar su comportamiento actual Y pagar por ello.*

---

## 4. Escenario de fracaso rápido

> Lanzas en Ciudad de México. Gastas 3 meses convenciendo 40 proveedores de listarse. Nadie ordena porque no hay restaurantes.
>
> Convences 20 restaurantes de probar. Hacen 1 pedido. El proveedor llega tarde, trae aguacates duros, y el restaurante vuelve a llamar a su proveedor de siempre.
>
> Los proveedores se quejan de que "solo llegan pedidos de $500 pesos y no vale la pena".
>
> Tú sigues pagando AWS, tu dev, tu tiempo. En 4 meses estás en cero.
>
> **Causa de muerte**: No resolviste el dolor real. Resolviste un dolor que TÚ imaginaste, pero que el taquero no siente con suficiente intensidad como para cambiar 15 años de hábito.

---

## 5. Con $10K: qué haría yo

**No construyas la app. Todavía no.**

1. **$0 — Habla con 50 dueños de restaurantes pequeños** (no encuestas, conversaciones de 30 min). Pregunta: "¿Cuánto tiempo pierdes a la semana en compras? ¿Qué es lo peor del proceso? ¿Cuánto pagas hoy por resolverlo?" Si no te dicen que es un dolor del 8/10, para.

2. **$0 — Haz shadowing**: Pasa 3 días con 3 restaurantes viendo cómo compran. Observa el proceso real, no el que te imaginaste.

3. **$2K — Concierge MVP**: Tú eres la app. Tomas pedidos por WhatsApp, llamas a proveedores, coordinas entregas. Cobra 10-15%. Hazlo para 10 restaurantes durante 4 semanas. Mide: ¿repiten? ¿se quejan del precio? ¿te saltan?

4. **$3K — Mide retención y willingness to pay**: Si después de 4 semanas el 70%+ repite Y acepta pagar la comisión, tienes señal. Si no, pivot o muere rápido.

5. **$5K — Solo entonces** construye un MVP simple (WhatsApp bot o web app básica) para automatizar lo que ya hiciste manualmente.

---

## La pregunta que no te estás haciendo

> **¿Por qué DoorDash, Rappi, o algún unicornio de food-tech no ha hecho esto ya?**

Si fuera tan obvio, alguien con $500M lo habría intentado. El hecho de que no exista una solución dominante puede significar que el problema no es tan grande como crees, o que es más difícil de resolver de lo que parece.

¿Quieres que te ayude a diseñar las 50 entrevistas de validación?