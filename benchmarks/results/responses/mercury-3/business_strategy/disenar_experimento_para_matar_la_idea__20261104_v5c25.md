# Mercury 3 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `inception/mercury-3`
- success: True  | final: 7.32 | quality: 8.0
- latency_total: 33.236s | tokens_per_second: 405.9
- input_tokens: 207 | output_tokens: 13489

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Tu hipótesis, tal como está, **no es falsable**. “Pagarían” es demasiado vago. Hay que reformularla para poder matarla:

> **Versión falsable:** De 50 agencias pequeñas contactadas, al menos 5 pagarán $200/mes por recibir sus reportes de clientes ya hechos.

Si eso no ocurre, la idea no merece 2 meses de construcción.

---

## El experimento: Concierge de pago

No construyas nada. **Vende el resultado antes de tener la herramienta.** Tú eres la herramienta.

Si no puedes vender el servicio manualmente, la herramienta tampoco lo venderá. El riesgo no es la tecnología; es que nadie pague.

---

## Qué hacer exactamente

### 1. Define la oferta

- **Precio:** $200/mes por agencia.
- **Qué incluye:** Reportes mensuales para hasta 5 clientes de la agencia.
- **Formato:** PDF o link con métricas, gráficos y comentarios.
- **Pago:** Tarjeta de crédito, vía Stripe.

No bajes el precio. No ofrezcas prueba gratis. El experimento es para saber si pagan $200, no $50.

### 2. Monta el canal de pago

- Crea un producto recurrente en Stripe y genera un **Payment Link** de $200/mes.
- Opcional: una página simple en Carrd o Google Sites con el precio y un botón “Pagar $200/mes”.

No necesitas más. Cero código.

### 3. Haz una lista de 50 agencias pequeñas

- **Criterio:** Agencias de marketing con 2–20 empleados, que manejen varios clientes.
- **Fuentes:** LinkedIn, Clutch, Google Maps, directorios locales.
- **Datos:** Nombre de la agencia, nombre del fundador, email y LinkedIn.

Guarda todo en una hoja de cálculo.

### 4. Contacta a las agencias

Envía mensajes personalizados. Ejemplo:

> Hola [Nombre],  
> Sé que las agencias pequeñas pierden horas armando reportes para clientes.  
> Estoy lanzando un servicio que te los arma por $200/mes.  
> Estoy buscando 5 agencias para el primer mes, y yo mismo haré los reportes.  
> ¿Te interesa que te muestre un ejemplo?  
> [Link de pago]

- Envía a 20 agencias el primer día.
- A los 3 días, haz seguimiento.
- Luego envía a las otras 30.

### 5. Da seguimiento y cierra

- Si responden, ofrece una llamada de 15 minutos.
- En la llamada pregunta:
  - ¿Cuánto tiempo gastan en reportes al mes?
  - ¿Cuánto les cuesta ese tiempo?
  - ¿Qué herramientas usan?
- Luego di:

> Esto cuesta $200/mes. Si te lo hago yo este mes, ¿lo pagas hoy?

No aceptes “me interesa”, “quizás” ni “te aviso”. Solo acepta el pago.

### 6. Si alguien paga, entrégale el servicio manualmente

- Pídele acceso de solo lectura a Google Analytics, Meta Ads, etc., o que te pase los números.
- Usa una plantilla de Google Slides o Canva para hacer el reporte.
- Dedica 1–2 horas por cliente.

Esto es trabajo real, pero es el costo del experimento.

### 7. Mide todo

Registra:

- Agencias contactadas.
- Respuestas.
- Llamadas hechas.
- Pagos recibidos.
- Ingresos totales.
- Objeciones principales.

---

## Costo

| Concepto | Costo |
|---|---|
| Dominio (opcional) | $10/año |
| Carrd (opcional) | $19/año |
| Stripe | 2.9% + $0.30 por pago |
| **Total en efectivo** | **$0–$35** |
| Tu tiempo | 20–40 horas |

El costo real es tu tiempo. Pero es mucho más barato que 2 meses construyendo.

---

## Tiempo

| Fase | Duración |
|---|---|
| Preparación | 2 días |
| Outreach | 7 días |
| Seguimiento | 7 días |
| Cierre | 7 días |
| **Total** | **21 días** |

Puedes apretarlo a 14 días si envías los 50 mensajes el primer día.

---

## Resultado que te hace abandonar

**Abandona si, después de 30 días y 50 agencias contactadas, tienes menos de 5 pagos de $200.**

También aborta antes si, en los primeros 20 contactos, no consigues **ningún pago**.

No cuentan los “me interesa”. Solo cuentan los que pagan.

---

## Si obtienes 5+ pagos

No has validado la herramienta. Has validado que hay dolor.

No construyas todavía. Sigue vendiendo el servicio manual hasta tener 10–20 clientes, o hasta que el trabajo manual te ahogue. Ahí es cuando sabes que vale la pena automatizarlo.

---

## Errores que debes evitar

- No hagas encuestas. La gente miente.
- No preguntes “¿te gustaría?” Pregunta “¿lo pagas hoy?”
- No construyas un MVP.
- No ofrezcas gratis.
- No aceptes compromisos verbales.
- No bajes el precio.
- No cambies el umbral a mitad del experimento.

---

Este experimento puede fallar de forma concluyente. Si falla, te habrás ahorrado 2 meses. Si pasa, tendrás clientes que te pagan y un servicio manual que puedes convertir en software. Exactamente lo que necesitas.