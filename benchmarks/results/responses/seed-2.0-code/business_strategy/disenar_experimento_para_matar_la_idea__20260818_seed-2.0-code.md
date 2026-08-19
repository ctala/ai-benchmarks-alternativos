# Seed 2.0 Code — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.12 | quality: 8.0
- latency_total: 35.57s | tokens_per_second: 57.6
- input_tokens: 222 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa


El usuario quiere un experimento para MATAR su hipótesis, no validarla. Primero, recordar que la hipótesis tiene dos pilares OCULTOS que la mayoría olvida: 1) "agencias de marketing PEQUEÑAS" (definir exactamente, no vago) y 2) "PAGARÍAN $200/MES AHORA" (no "están interesadas", sino pago real).

Primero, el usuario iba a invertir 2 meses, así que el experimento tiene que ser MENOS de 1 semana, menos de $100, y con un CRITERIO DE FALLO CLARO (no "pocos interesados", sino un umbral irrefutable).

Primero, DEFINIR EXACTAMENTE la muestra, no "agencias pequeñas": hay que evitar ambigüedad. Vamos a definir "agencias pequeñas de marketing" como:
- Menos de 10 empleados (para que no tengan equipo de datos interno)
- Tienen entre 5 y 20 clientes (para que los reportes sean un dolor, no 1 cliente ni 50 que ya usan herramientas caras)
- Facturan entre $5k y $50k/mes (para que $200 no sea insignificante ni imposible)
- No usan herramientas de reporte automatizado (ej: no usan Tableau, Looker Studio Pro, AgencyAnalytics) → Eso es clave, porque si ya usan, no necesitan la tuya.

Ahora, el experimento NO PUEDE SER "hacer una landing page y ver clicks" → Eso es interés, no pago. El usuario quiere MATAR la hipótesis, así que necesitamos PAGO REAL (o compromiso irrevocable de pago en 72h) porque el dolor real se mide con la billetera.

¿Cómo hacerlo sin tener la herramienta? Porque el usuario no quiere construir nada aún. La clave es el "MVP de venta", no el MVP de producto.

Pasos exactos:

1. PRIMERO, FILTRAR LA MUESTRA SIN GASTAR:
   - Usa LinkedIn Sales Navigator Free (o incluso solo LinkedIn) + Google Maps:
     - Buscar "agencia de marketing [ciudad cercana, ej: Madrid, Ciudad de México, Buenos Aires]" → Filtrar por "menos de 10 empleados" en LinkedIn.
     - O usar Directorio de Empresas (en muchos países es gratuito) para buscar agencias de marketing con <10 empleados.
     - Luego, contactar a 30 personas (dueños o gerentes de cuentas) → PERO NO HABLES DE LA HERRAMIENTA AÚN. Primero, un filtro de dolor en 1 pregunta para no perder tiempo:
       "Hola [Nombre], soy [Tu Nombre], estoy investigando dolores de agencias pequeñas de marketing. ¿Podrías responder 1 pregunta en 2 segundos? ¿Te gastas más de 2 horas a la semana haciendo reportes para clientes, y no tienes herramienta automatizada para ello?"
       - Si dice NO → Descartar. Si dice SÍ → Pasar a la venta (porque el dolor existe, ahora medir disposición a pagar).

2. SEGUNDO, LA VENTA SIN PRODUCTO (EL EXPERIMENTO CLAVE):
   - Para los que pasaron el filtro de dolor, les dices EXACTAMENTE ESTO (sin adornos, sin promesas falsas):
     "Perfecto, estoy construyendo una herramienta que automatiza esos reportes: conecta Facebook Ads, Google Ads, Instagram, Google Analytics, envía reportes personalizados por correo a clientes cada semana/mes, sin que tengas que tocar Excel.
     Aún no la tengo lista, pero estoy buscando 10 PRIMEROS CLIENTES que paguen $200/mes (precio definitivo, no descuento) a partir de HOY, y en 2 semanas les entrego la herramienta. Si no la entrego en 2 semanas, les devuelvo TODO el dinero sin preguntas.
     ¿Quieres reservar tu plaza pagando HOY $200 por PayPal/Stripe?"
   - ¿Por qué $200 HOY, no después? Porque el "me interesa" es gratis, el pago es la única prueba real.
   - ¿Por qué devolución garantizada? Para eliminar el riesgo del cliente, así que su único "inconveniente" es hacer clic en pagar → si no lo hace, es que la hipótesis es falsa.

3. TERCERO, CRITERIO DE FALLO IRREFUTABLE (NO AMBIGUO):
   - Tú necesitas MATAR la hipótesis, así que el umbral de fallo es BAJO (porque si ni siquiera con este trato (garantía de devolución, precio exacto) consigues suficientes pagos, la hipótesis es muerta).
   - Umbral: De 30 contactos filtrados por dolor (es decir, 30 personas que dijeron que gastan >2h/semana en reportes y no tienen herramienta), SI CONSIGUES MENOS DE 2 PAGOS → ABANDONA LA IDEA.
   - ¿Por qué 30 contactos filtrados? Porque es un tamaño muestral suficiente para un test rápido (ley de los grandes números no aplica, pero para MATAR la hipótesis, si ni 2 de 30 con DOLOR REAL paguen $200 con garantía, no hay mercado).
   - ¿Por qué menos de 2? Porque 1 pago podría ser un conocido que te quiere ayudar. 2 pagos son al menos 2 personas con dolor real que están dispuestas a arriesgar (aunque con devolución) $200.

4. COSTOS Y TIEMPOS EXACTOS:
   - TIEMPO TOTAL: 4 DÍAS (no más):
     Día 1: Buscar 40 agencias pequeñas (filtradas por <10 empleados, 5-20 clientes) → 2 horas.
     Día 1-2: Enviar mensajes LinkedIn/correo (usar correos encontrados en su web, o LinkedIn InMail Free) a las 40 → 1 hora.
     Día 2-3: Recibir respuestas, filtrar las que dicen SÍ al dolor (aprox 30 de 40, si la muestra es buena), enviar la propuesta de venta.
     Día 4: Cerrar pagos (si los hay), contar resultados.
   - COSTOS TOTALES: $0 (si usas LinkedIn Free, correos gratuitos, PayPal/Stripe sin tarifas iniciales → las tarifas de PayPal/Stripe se cobran solo si hay pagos, y si devuelves, las recuperas o son mínimas). Opcional: $10 para un dominio temporal si quieres poner un link de pago en una página muy básica (pero no es necesario: puedes enviar el link de PayPal/Stripe directamente).

5. ¿POR QUÉ ESTO MATA LA HIPÓTESIS SI FALLA?
   - Porque eliminaste TODAS las excusas que los clientes suelen tener para no pagar:
     1. "No tengo dolor": Filtraste a personas que dijeron que gastan >2h/semana en reportes.
     2. "No tengo dinero": La muestra es de agencias que facturan >$5k/mes → $200 es 4% de sus ingresos mensuales, lo que es razonable para una herramienta que les ahorra 8h/mes (2h/semana).
     3. "No quiero arriesgar": Garantía de devolución total en 2 semanas.
     4. "No sé si funciona": Les explicaste exactamente lo que hace, y es un problema que tienen todos los días.
   - Si ni siquiera con esto consigues 2 pagos de 30 personas con dolor real, es que:
     - O el precio es demasiado alto (pero la hipótesis es $200/mes, no $100).
     - O el dolor no es lo suficientemente fuerte como para pagar (lo que significa que la hipótesis es falsa).
     - O ya tienen una solución que no te dijeron (pero filtraste a los que no tienen herramienta, así que es poco probable).

6. ¿Y SI CONSIGUES 2 O MÁS PAGOS?
   - Entonces NO has validado la hipótesis, pero NO la has matado → puedes seguir adelante (porque al menos 2 personas están dispuestas a pagar $200/mes por ella, y con la garantía, no te arriesgas a nada: si no la construyes, devuelves el dinero).

¿Qué hay de las trampas