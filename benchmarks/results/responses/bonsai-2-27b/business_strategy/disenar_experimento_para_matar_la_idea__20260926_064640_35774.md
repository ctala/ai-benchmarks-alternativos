# Bonsai 2 27B — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 6.85 | quality: 8.0
- latency_total: 360.05s | tokens_per_second: 29.9
- input_tokens: 217 | output_tokens: 10775

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa



No construyas todavía. Haz el experimento del **cheque**: 30 agencias, 72 horas, 3 pagos reales.

## Experimento: “Piloto de reportes con pago anticipado”

**Hipótesis que matas:**  
“Las agencias de marketing pequeñas pagarían $200/mes por una herramienta que automatice reportes a clientes.”

**Versión testable:**  
“Al menos 3 agencias pequeñas pagarían $200 hoy por un piloto de reportes a clientes, entregados en 7 días.”

Si no pasa, la idea no tiene base suficiente para 2 meses de construcción.

---

# Qué vendes exactamente

No vendas “software”. Vende resultado:

> **$200/mes**  
> Te entrego **3 reportes listos a tus clientes** en **7 días**.  
> Si no te ahorra tiempo, no renuevas.  
> Primer mes se paga antes.

Importante:  
No prometas “automatización mágica en 7 días”. Promete **reportes listos y un proceso repetible**. Si pagan, tú lo haces a mano o semi-manualmente con plantillas. Eso sirve para validar.

No hagas:
- Trial gratis
- Descuentos
- “Te aviso si me interesa”
- Demos
- Formulario de registro
- “Agenda una llamada”

Solo aceptas **pago real**.

---

# Pasos exactos

## 1. Lista 30 agencias objetivo

Necesitas **30 agencias de marketing pequeñas** que ya hagan reportes a clientes.

Perfil:
- 2 a 15 empleados
- Tienen clientes activos
- Hacen reportes mensuales, semanales o por campaña
- No son grandes agencias corporativas
- No son freelancers sin clientes recurrentes

Fuentes:
- LinkedIn
- Instagram
- Directorios locales
- Portafolios
- Agencias que publican casos de éxito
- Communities de marketing
- Clientes pasados de agencias

Si en 2 horas no encuentras 30 agencias claras, resegmenta:
- Agencias de SEO
- Agencias de performance
- Agencias de e-commerce
- Agencias locales
- Agencias de branding + reporting

Si no puedes definir bien el segmento, no empieces.

---

## 2. Crea un pago simple

Usa Stripe, PayPal invoice, o lo equivalente en tu país.

Crear un payment link de:

> **$200 — Piloto de reportes a clientes, 1 mes**

El título del pago puede ser:

> “Piloto de reportes a clientes — primer mes”

No hagas landing page complicada. El pago directo es suficiente.

Costo:
- $0 hasta que alguien pague
- Comisión de Stripe/PayPal por cada pago, aproximadamente 2.9% + $0.30 o equivalente

---

## 3. Manda 30 mensajes directos

Envía 10 por día durante 3 días.

No escribas un email genérico. Personaliza la primera línea.

---

# Plantilla de mensaje

**Asunto:** Reportes de clientes

> Hola [nombre],  
>  
> Vi que [agencia] trabaja con clientes de [sector] y publican reportes.  
>  
> Te propongo un piloto: por **$200/mes** te entrego **3 reportes listos a tus clientes** en **7 días**.  
>  
> El primer mes se paga antes. Si no te sirve, no renuevas.  
>  
> Si te interesa, puedes pagar aquí: [link de pago]  
>  
> ¿Te lo hago hoy?

---

# Follow-up a las 24 horas

> Hola [nombre],  
>  
> Solo por si se te perdió el mensaje: el piloto es de **$200/mes**, con **3 reportes listos en 7 días**.  
>  
> Si quieres, pago aquí: [link]  
>  
> Si no te interesa, no pasa nada.

---

# Follow-up a las 48 horas

> Hola [nombre],  
>  
> Cierro los cupos del piloto.  
>  
> Si quieres, aquí está el pago: [link]  
>  
> Si no, no te molesto más.

No hagas más de 2 follow-ups.

---

# Reglas que no rompas

Si te dicen:

> “Me interesa, pero déjame pensarlo.”

Respuesta:

> Perfecto. Si quieres el piloto, el pago es aquí: [link].

Si te dicen:

> “¿Me puedes hacer una demo?”

Respuesta:

> No hago demos. El piloto es $200/mes y el pago es aquí: [link].

Si te dicen:

> “¿Puedo pagar al final del mes?”

Respuesta:

> Para el piloto, sí.

Si te dicen:

> “¿Me haces un descuento?”

Respuesta:

> El precio del piloto es $200/mes.

Si te dicen:

> “Necesito hablar con mi socio.”

Respuesta:

> Perfecto, si deciden hacer el piloto, el pago es aquí: [link].

Si no pagan, no cuentan.

---

# Cuánto cuesta

## Costo total

| Concepto | Costo |
|---|---:|
| Stripe/PayPal | $0 hasta el pago |
| Commission fees | ~$0.30 + 2.9% por pago |
| Landing page | $0, usas payment link |
| Outreach | $0 si usas LinkedIn/email |
| Cold email tool opcional | $20-$30 máximo |
| **Total realista** | **$0 a $50** |

Si el experimento te cuesta más de $50, ya está mal diseñado. Para este test, no vale la pena gastar más.

---

# Cuánto tarda

## Tiempo total: 72 horas

Distribución:

| Hora | Actividad |
|---:|---|
| 2h | Armar lista de 30 agencias |
| 1h | Crear payment link y oferta |
| 3h | Enviar 30 mensajes |
| 1.5h | Follow-ups |
| 0.5h | Decisión final |

**Tiempo total:** aproximadamente **5 a 8 horas** en 72 horas.

No extiendas el experimento.  
Si a las 72 horas no hay 3 pagos, paras.

---

# Resultado que te hace abandonar la idea

## Abandonas si:

> **Menos de 3 pagos reales en 72 horas.**

Es decir:

- 0 pagos → abandonas
- 1 pago → abandonas
- 2 pagos → abandonas

No importa si hay:
- Interés
- “Me parece bien”
- “Te aviso”
- “Quiero una demo”
- “Me gustaría más info”
- “Puedo pagar si me haces factura”

Solo importa dinero real de agencias objetivo.

---

# ¿Y si logras 3 pagos?

Si logras **3 pagos reales en 72 horas**, la hipótesis no está muerta.

Pero **no construyes aún**.

Siguiente paso:

1. Entrega el piloto a mano.
2. Pide acceso a los datos mínimos.
3. Entrega 3 reportes en 7 días.
4. Mide si realmente les ahorra tiempo.
5. Pide renovación para el mes siguiente.

Si los 3 renuevan, tienes base para seguir.  
Si no renuevan, matas la idea de nuevo.

---

# Por qué este experimento mata bien

Porque no mide curiosidad. Mide dinero.

Una agencia puede decir:
- “Me gusta”
- “Necesito algo así”
- “Sería bueno”
- “Me gustaría automatizar”

Pero si no paga $200 hoy, no está validando la hipótesis. Está validando que le suena bien.

Con 30 agencias y 72 horas, si no hay 3 pagos, no tienes demanda suficiente para justificar 2 meses de construcción.

---

# Tu regla final

Haz esto:

> **30 agencias pequeñas, 72 horas, $200 por piloto, 3 pagos reales.**

Si no alcanzas 3 pagos:

> **Abandona la idea tal como está.**

No la construyas.  
No la “ajustes un poco”.  
No hagas MVP.  
No hagas 2 meses.

La hipótesis está muerta.