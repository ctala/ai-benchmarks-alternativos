# Seed 2.1 Turbo — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 6.84 | quality: 8.0
- latency_total: 160.522s | tokens_per_second: 62.7
- input_tokens: 222 | output_tokens: 10063

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento: Smoke Test de Pago Directo en Outreach Frío
### Objetivo: MATAR tu hipótesis de forma concluyente, no validarla.
Este test está diseñado para fallar rápidamente si tu idea es mala, sin invertir en desarrollo. Mide la única métrica que no miente: disposición a pagar dinero real por el producto que quieres construir.

---

## Datos básicos
| Duración total | Coste total | Tiempo de trabajo efectivo |
|----------------|-------------|-----------------------------|
| 4 días         | $0 (versión gratuita) / $20 máximo (versión acelerada) | 7-8 horas |

---

## Paso 0 (OBLIGATORIO, antes de empezar): Define el umbral de fracaso
Para no caer en sesgos de confirmación después, escribe esta regla y cúmplela sin excepciones:
> Si de **20 leads CALIFICADOS** que cumplen el perfil objetivo, MENOS DE 2 PAGAN $200 de forma inmediata, mi hipótesis es falsa. Abandono la idea.

### ¿Qué es un lead calificado?
Debe cumplir LOS 3 CRITERIOS (si no los cumple, no cuenta para la muestra):
1. Es dueño/responsable de una agencia de marketing de 1 a 5 empleados.
2. Gestiona entre 3 y 20 clientes activos.
3. Actualmente hace reportes a clientes de forma manual (Google Sheets, Canva, corta y pega capturas, etc.)

Cualquier respuesta que no sea un pago inmediato de $200 cuenta como NO PAGO (no valen "me apunto la semana que viene", "me gustaría pero necesito X funcionalidad", "me parece caro, ¿tienes descuento?").

---

## Pasos exactos, día por día

### Día 1 (2 horas de trabajo)
1. **Consigue 40 contactos de dueños de agencias pequeñas** (para asegurar que llegas a los 20 calificados):
   - **Opción gratuita ($0):** Entra en 3-5 grupos de Facebook/LinkedIn de dueños de agencias de marketing pequeñas (ej: "Dueños de Agencias de Marketing España", "Pequeñas Agencias SEO LATAM", "Agencias de Redes Sociales Independientes"). Busca miembros que indiquen en su perfil que son dueños de agencias de 1-5 personas. Copia su nombre y perfil.
   - **Opción acelerada ($20):** Crea un anuncio de Facebook/Instagram dirigido a personas con puesto "Dueño de agencia de marketing" / "Director de agencia", tamaño de empresa 1-5 empleados. El anuncio lleva a un formulario de 2 preguntas: "¿Cuántos empleados tiene tu agencia?" y "¿Haces reportes manuales a tus clientes?". Con $20 te llegarán entre 10 y 30 respuestas en 24 horas.

2. **Escribe el mensaje de outreach** (personalizado, sin trucos):
   > Hola [Nombre], soy [Tu nombre], estoy desarrollando una herramienta para agencias de marketing pequeñas que automatiza los reportes a clientes. Antes de invertir meses en construirla, quería confirmar algo contigo:
   > 1. ¿Tu agencia es de 1 a 5 personas?
   > 2. ¿Gestionas entre 3 y 20 clientes?
   > 3. ¿Actualmente haces los reportes a clientes de forma manual (Sheets, Canva, capturas, etc.)?
   > Si es así, te quería hacer una oferta muy rápida.
   > Saludos!

3. Envía el mensaje a los 40 contactos (o publícalo en los grupos, si permiten publicaciones de herramientas).

---

### Días 2 y 3 (4 horas de trabajo totales)
1. Responde a todas las respuestas. Si la persona cumple los 3 criterios de calificación, le haces la oferta de forma directa:
   > Genial, gracias por responder. La herramienta hace exactamente esto:
   > - Se conecta a Meta Ads, Google Ads, Google Analytics, Instagram y TikTok.
   > - Genera reportes personalizados con el logo y colores de tu agencia.
   > - Se los envía automáticamente a tus clientes por correo cada semana o mes, sin que tengas que hacer nada.
   > Cuesta $200/mes.
   > Estamos terminando de desarrollarla, y si te apuntas HOY como cliente fundador, pagas $200 ahora, y tienes 30 días de prueba desde que te demos acceso: si no te ahorra al menos 5 horas a la semana, te devuelvo el dinero completo sin preguntas.
   > ¿Te apuntas?

2. Si la persona dice que sí, envíale un enlace de pago de Stripe o Mercado Pago (cuentas gratuitas, solo cobran comisión si hay ventas, y si devuelves el dinero, te devuelven la comisión).

3. **Inmediatamente después de que se complete el pago**, le envías este mensaje (para ser 100% ético y no dañar tu reputación):
   > Muchas gracias por tu confianza. Para ser completamente transparente, actualmente estamos en etapa de validación de demanda, y la herramienta no está terminada todavía. Acabo de devolverte el $200 íntegramente (deberías verlo en tu cuenta en 2-3 días hábiles). El objetivo de esta prueba era confirmar que hay agencias dispuestas a pagar por esta solución, y tu pago nos ayuda a validarlo. Como agradecimiento, te daremos acceso gratuito a la herramienta durante los primeros 3 meses cuando la lancemos, y te mantendremos informado de todo el proceso. Disculpa las molestias, y gracias de nuevo por tu ayuda.

---

### Día 4 (1 hora de trabajo)
1. Cuenta cuántos leads calificados tuviste y cuántos pagaron $200.
2. Compara con el umbral de fracaso que definiste antes de empezar.

---

## Resultado que te hace ABANDONAR la idea (concluyentemente)
Si de **al menos 20 leads calificados**, tienes **MENOS DE 2 PAGOS** (tasa de conversión <10%), tu hipótesis es falsa. Abandonas.

No vale excusas:
- Si no pagan ahora con una garantía de reembolso total, no pagarán después cuando no te conozcan de nada.
- Si necesitan funcionalidades extra que no habías planeado, tu producto original no es lo que quieren pagar, así que tu hipótesis inicial es errónea.
- Si prefieren esperar, es que el problema no es lo suficientemente doloroso como para pagar por una solución ahora.

---

## ¿Por qué este experimento es concluyente para matar la hipótesis?
Porque mide la única cosa que importa: disposición a pagar dinero real. Las encuestas, los "me gustaría" o los registros en landing pages de "próximamente" no valen nada: la gente miente por amabilidad o por no querer ser mala. Pero nadie paga $200 por algo que no necesita de verdad.

Además, el outreach personalizado es el canal con MAYOR tasa de conversión que existe para SaaS de nicho. Si en el mejor escenario posible (te diriges directamente a la persona que tiene el problema, le explicas el producto de forma personalizada) no consigues ni un 10% de conversión, entonces cuando hagas marketing masivo, landing pages, etc, la tasa será de 1-2% como máximo, lo que hace que el costo de adquisición sea prohibitivo para un producto de $200/mes.

---

## ¿Qué pasa si no matas la hipótesis (consigues 2 o más pagos)?
No significa que tengas razón. Solo significa que no has podido demostrar que estás equivocado, así que puedes seguir invirtiendo tiempo (por ejemplo, construir un MVP mínimo en 2 semanas en lugar de 2 meses) para seguir probando. Pero este experimento ya te ha ahorrado 2 meses de trabajo si la idea era mala.