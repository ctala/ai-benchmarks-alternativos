# Step 3.5 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.42 | quality: 8.0
- latency_total: 55.312s | tokens_per_second: 79.5
- input_tokens: 205 | output_tokens: 4398

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

**Experimento para falsar la hipótesis: "Pre-venta con compromiso financiero real"**

---

### **Qué haces (pasos concretos)**
1. **Define el target preciso**: Agencias de marketing con ≤5 empleados, facturación anual <$300k, que trabajen con clientes locales (ej. restaurantes, clínicas, retail). Evita agencias digitales grandes o especializadas en grandes marcas.
2. **Consigue 50 leads válidos**:
   - Busca en LinkedIn, directorios locales (Google My Business), y listas de cámaras de comercio.
   - Filtra por tamaño (usa datos públicos como número de empleados en LinkedIn).
   - Extrae email de contacto general o del gerente.
3. **Crea una landing page de una página** (usando Carrd, Gumroad o Shopify "buy now" button):
   - Título: "Automatiza tus reportes de marketing en 1 clic. Acceso anticipado para agencias pequeñas".
   - Texto breve: "Herramienta que genera reportes profesionales para clientes automáticamente (Google Data Studio/PPT). Lanzamiento en 60 días. Precio de lanzamiento: $200/mes. **Pago por adelantado del primer mes con reembolso completo si no se entrega en 60 días**".
   - Botón: "Reservar acceso - $200 reembolsables".
   - Incluye un formulario mínimo: nombre, agencia, email.
   - Integra Stripe/PayPal para cobrar (aunque sea simbólico, luego reembolsas).
4. **Contacto directo**:
   - Envía un email personalizado (1-2 líneas) a cada una de las 50 agencias:
     *"Hola [Nombre], vi que trabajan con [tipo de cliente]. ¿Les cuesta horas crear reportes mensuales para clientes? Estoy creando una herramienta que lo automatiza. Ofrezco acceso anticipado a $200/mes (primer mes reembolsable si no lanzo en 60 días). ¿Interesan en probarla? Aquí más info: [link landing]"*.
   - Haz seguimiento a los que no abran en 3 días (llamada o segundo email).
5. **Registra todo**:
   - Número de emails enviados, abiertos, clicks.
   - Cuántos llegan a la landing page.
   - Cuántos intentan pagar (abandonan en checkout).
   - Cuántos completan el pago.
   - En las llamadas/emails de seguimiento, anota objeciones clave (ej: "ya usamos hojas de cálculo", "no tenemos presupuesto", "no es prioridad").

---

### **Cuánto te cuesta**
- **Tiempo**: 2 días para lista + 1 día para landing page + 3 días de contacto/seguimiento = **6 días hábiles** (≈ 48 horas de trabajo).
- **Dinero**: 
  - Landing page: $0-20 (Carrd gratis o dominio barato).
  - Stripe/PayPal: comisión por transacción (2.9% + $0.30) por cada pago recibido, pero como reembolsarás, asumes ese costo solo si alguien paga (ej: $6 por cada $200). Si nadie paga, $0.
  - Herramientas de email (Mailtrack, etc.): $0-10.
  - **Total monetario: <$50** (incluso $0 si usas herramientas gratuitas y nadie paga).
- **Oportunidad**: 48 horas que no dedicas a construir. Es la inversión más barata posible.

---

### **Cuánto tarda**
- **Semana 1**: Lista de 50 agencias + landing page.
- **Semana 2**: Contacto y seguimiento (máximo 5 días laborables).
- **Resultado en 10 días** (si aceleras, en 1 semana).

---

### **Resultado que te hace abandonar la idea (falsación concluyente)**
**Criterio de abandono:**
- **0 pagos completados** de 50 agencias contactadas, **y** al menos 30% de las agencias (15+) mencionan en conversaciones que:
  - "No es un problema doloroso" (ej: "nos toma 1-2 horas al mes, no es gran cosa").
  - "Ya tenemos solución (hojas de cálculo, freelancer barato)".
  - "No hay presupuesto para herramientas >$50/mes".
- **O**: Menos de 3 pagos (≤6% conversión) **y** objeciones claras de precio ("$200 es demasiado para nuestro tamaño").

**Por qué esto mata la hipótesis:**
- El pago por adelantado con reembolso es una **señal fuerte de intención real**. Si no pagan, no es por desconfianza en ti (el reembolso elimina el riesgo), sino porque:
  1. El problema no es lo suficientemente doloroso.
  2. El precio supera su presupuesto.
  3. Ya tienen solución (gratuita o barata).
- Si consigues 3+ pagos, la hipótesis **no se falsa** (pero aún no se valida: necesitarías construir y retener). Si tienes 0-2 pagos y objeciones consistentes, es evidencia sólida de que estás equivocado.

---

### **Variante más extrema (si quieres aún menos tiempo)**
- **Solo llamadas**: En lugar de landing page, llama a 30 agencias en 2 días y ofrece: "Si me das $200 vía PayPal ahora, te entrego la herramienta en 60 días o te devuelvo el dinero". 
  - **Costo**: $0.
  - **Tiempo**: 2-3 días.
  - **Falsación**: 0 pagos de 30 llamadas → abandona.
  - **Riesgo**: Sesgo por rechazo directo, pero si ni siquiera consideran pagar, la hipótesis es débil.

---

### **Conclusión**
Este experimento **no construye nada**, solo prueba **disposición a pagar real** con riesgo cero para el cliente. Si fallas (menos de 3 pagos de 50), la hipótesis está probablemente equivocada. Si pasas, tienes tracción inicial para construir. **Inversión: <1 semana, <$50.**