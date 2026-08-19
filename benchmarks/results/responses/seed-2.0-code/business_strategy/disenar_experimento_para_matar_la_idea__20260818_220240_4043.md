# Seed 2.0 Code — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.88 | quality: 8.0
- latency_total: 121.767s | tokens_per_second: 57.2
- input_tokens: 222 | output_tokens: 6968

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

### Experimento para MATAR tu hipótesis (NO VALIDARLA)
**Diseñado para ser el más rápido (48h) y barato (<$5) posible, con una señal concluyente de FALLO**

---

## Primero: Definición sin ambigüedad de la hipótesis y target (sin esto, el experimento no vale)
Tu hipótesis original es vaga. La reescribimos para ser medible:
> **Hipótesis Medible**: Agencias de marketing DIGITAL de 1-4 empleados, que pierden >2h/semana armando reportes MANUALES a clientes, y facturan entre $5k-$30k/mes, **pagarán $200/mes por una herramienta que automatice esos reportes** (sin riesgo para ellas).

Si te desvías de este target (ej: agencias grandes, agencias que ya usan herramientas), el resultado no es concluyente.

---

## Qué haces exactamente (pasos por hora)
### Paso 1: Preparar herramientas sin costo (1h)
No construyas NADA de la herramienta. Usa:
1. **Landing Page GRATUITA**: Usa *Google Sites* o *Carrd (versión gratuita)*. No necesites diseño bonito, solo claridad.
2. **Pago REAL sin riesgo**: Crea una cuenta en *Stripe* (gratuita, sin costos fijos) y configura un producto:
   - Nombre: **Acceso Anticipado Automatizador de Reportes**
   - Precio: $200/mes (suscripción, PERO con una promesa EXPLÍCITA en el checkout de **reembolso TOTAL si no entregas la herramienta en 30 días**)
   - Coloca el enlace de Stripe Checkout en un botón de la landing.

#### Contenido OBLIGATORIO de la landing (sin vaguezas, sin jerga):
> **Título**: Agencias Pequeñas: Automatiza tus Reportes a Clientes en 5min (Sin Supermetros Caros)
> **Subtítulo**: Pierdes >2h/semana armando reportes en Excel/Canva? Esta herramienta lo hace por ti, con tu logo y colores.
> **Características CONCRETAS** (solo las que necesitan):
> 1. Conecta con Meta Ads, Google Ads, GA4, Instagram
> 2. Genera PDF/Canva editable con tu marca
> 3. Envía el reporte AUTOMÁTICAMENTE el día que quieras
> **Oferta EXCLUSIVA (sin riesgo)**:
> - Solo 10 cupos para agencias de 1-4 empleados
> - $200/mes → Reembolso TOTAL si no entrego en 30 días
> **Botón**: [Pagar Ahora y Reservar Mi Cupo]
> **Pie de página (transparente, no engaño)**: Esta herramienta está en desarrollo. Tu pago asegura tu lugar en la primera cohorte. Si no la entrego, te devuelvo TODO sin preguntas.

---

### Paso 2: Conseguir 20 agencias del TARGET EXACTO (2h)
No pagues publicidad. Usa **LinkedIn y grupos de Facebook de agencias de marketing de TU PAÍS** (sin barreras de idioma/pago).

#### Criterios de INCLUSIÓN OBLIGATORIOS (si no los cumple, NO la contactes):
1. Agencias de MARKETING DIGITAL (no tradicionales: manejan ads/SEO/redes)
2. 1-4 empleados (ver LinkedIn: número de personas en el perfil; o página web: equipo <5 nombres)
3. Pierden >2h/semana armando reportes MANUALES (lo confirmas con una pregunta antes de ofrecer el pago)
4. Facturan $5k-$30k/mes (ver: no tienen clientes grandes, no tienen puesto de "Data Analyst")

#### Mensaje PERSONALIZADO (sin plantillas, para que respondan):
> **Para LinkedIn (mensaje directo)**:
> Hola [Nombre], vi que eres fundador/a de [Nombre Agencia], una agencia de marketing digital con 3 empleados (vi tu perfil) y que trabajas con clientes como [Cliente de su página web].
> Yo tuve una agencia pequeña y perdía 8h/semana armando reportes a clientes. Ahora estoy desarrollando una herramienta para automatizar eso, y quiero probar SI HAY DEMANDA REAL (no encuestas, no promesas).
> Antes de seguir: **¿Actualmente pierdes más de 2h/semana armando reportes manuales para tus clientes?**
> Si la respuesta es SÍ: te ofrezco un cupo de acceso anticipado por $200/mes, con reembolso TOTAL si no entrego la herramienta en 30 días. Aquí el enlace: [Landing]
> Si no: no hay problema, solo quería validar si mi solución sirve para agencias como la tuya.

> **Para grupos de Facebook (publicación)**:
> Hola equipo, soy [Tu Nombre], tuve una agencia de marketing pequeña hace 2 años y el mayor dolor era ARMAR REPORTES A CLIENTES: perdía 8h/semana en Excel/Canva, y si un cliente pedía un cambio, perdía otras 2h.
> Ahora estoy desarrollando una herramienta para automatizar eso, y quiero PROBAR SI HAY DEMANDA REAL (no promesas).
> **Oferta sin riesgo**: 10 cupos de acceso anticipado por $200/mes → Reembolso TOTAL si no entrego en 30 días.
> **Solo para**: agencias de 1-4 empleados que PIERDAN >2h/semana en reportes MANUALES.
> Si eres uno de ellos: comenta "REPORTE" y te envío el enlace privado.

---

### Paso 3: Medir resultados (24h después de enviar el último mensaje)
Tu muestra final es **20 agencias que cumplen TODOS los criterios de inclusión** (incluyendo que respondieron "SÍ" a la pregunta de dolor de >2h/semana).

---

## Cuánto cuesta
**Total: <$5**
- Landing page: GRATIS
- Stripe: Sin costos fijos. La tarifa es 2.9% + $0.30 por pago, PERO SI DEVUELVES EL DINERO (porque el experimento falla), STRIPE DEVUELVE LA TARIFA en la mayoría de países. Si no hay pagos: $0.
- Publicidad: $0 (toda la obtención de leads es orgánica)

---

## Cuánto tarda
**Total: 48 HORAS**
- Día 1: Preparar landing + Stripe + buscar 20 agencias
- Día 2: Enviar mensajes personalizados
- Plazo de respuesta: 24h después del último mensaje (para dar tiempo a que decidan)

---

## Resultado que MATA TU HIPÓTESIS (conclusivo, sin dudas)
### Si de las 20 agencias del TARGET EXACTO, **MENOS DE 3 PAGAN EL $200/MES CON LA GARANTÍA DE REEMBOLSO** → ABANDONA LA IDEA.

### Por qué es concluyente?
1. **Sin riesgo para el cliente**: La garantía de reembolso elimina cualquier excusa (no pagan por miedo a perder dinero, pagan solo si valoran la solución).
2. **Target perfecto**: Son las agencias con MAYOR DOLOR y CAPACIDAD DE PAGO ($200/mes es el 4% de su facturación mínima de $5k, lo que es razonable).
3. **Muestra estadísticamente significativa**: 20 agencias no son un azar. Una tasa de conversión <15% (3/20) es el mínimo mínimo para un producto B2B de pago. Si es menor, la demanda no existe para ese precio y target.

---

## Qué pasa si 3 o más pagan?
La hipótesis **NO ESTÁ MUERTA** (pero no está validada). Ahora puedes construir la herramienta con la seguridad de que al menos un segmento de mercado valora tu solución lo suficiente para pagar sin riesgo.

### Importante:
Si pagaron agencias y no quieres construirla, devuélveles el dinero inmediatamente. No hay engaño: la garantía es explícita.

---

## Por qué este experimento es mejor que construir primero?
- Ahorras 2 meses de trabajo y $1k+ en herramientas/salarios.
- La señal es REAL (pago) no falsa (encuestas, "suscribete para ser notificado").
- Es imposible que te equivoques por targetear mal: los criterios de inclusión son estrictos.