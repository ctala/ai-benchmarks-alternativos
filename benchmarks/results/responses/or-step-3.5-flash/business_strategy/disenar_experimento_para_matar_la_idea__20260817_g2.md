# Step 3.5 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.61 | quality: 8.0
- latency_total: 23.891s | tokens_per_second: 67.6
- input_tokens: 205 | output_tokens: 1616

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

**Experimento: "La Prueba del Depósito Reembolsable"**

---

### **Objetivo**
Determinar si agencias de marketing pequeñas (1-10 empleados) están dispuestas a **pagar $200/mes** por automatizar reportes, midiendo **intención de pago real** (no solo interés).

---

### **Diseño del experimento (sin escribir código)**

1. **Crea un "prototipo de fantasía" (Fake Door Test)**
   - Usa **Google Sheets + Zapier/Make** para simular la automatización:
     - Conecta 2-3 fuentes de datos comunes (Google Analytics, Meta Ads, Google Ads) a una plantilla de reporte pre-diseñada.
     - Configura actualizaciones automáticas cada 24h.
   - **No construyas nada**: Solo muestres el resultado final como si fuera un producto real.
   - Tiempo: 4-8 horas.

2. **Página de aterrizaje minimalista**
   - Usa Carrd o Webflow (gratis/barato).
   - Copy claro: "*Automatiza reportes de marketing en 1 clic. $200/mes. Sin contrato. Pruébalo gratis 7 días con tus datos reales*".
   - Incluye un formulario para solicitar acceso al "beta".
   - Tiempo: 2 horas.

3. **Identifica y contacta a 50 agencias pequeñas**
   - Busca en directorios locales, Clutch.co, o LinkedIn (filtro: 1-10 empleados).
   - Contacto **personalizado** (email/LinkedIn):
     - "*Vi que trabajan con [cliente similar]. Tenemos una herramienta que reduce 10h/semana de trabajo manual en reportes. ¿Les interesa probarla con sus datos esta semana?*"
   - **No hables de características**: Solo habla de **ahorro de tiempo**.
   - Tiempo: 4-6 horas.

4. **El "experimento" en la llamada de prueba**
   - Si responden (espera 20-30 respuestas de 50), programa una **llamada de 15 min**.
   - En la llamada:
     1. Muestra el prototipo **con sus datos** (previamente cargados de forma anónima o con su permiso).
     2. Di: "*El costo es $200/mes. Para acceder a la beta, necesitamos un depósito reembolsable de $50 que se descuenta del primer mes. Si no les funciona después de 7 días, lo devolvemos.*"
     3. Pregunta: "*¿Lo probarían con este modelo?*"

---

### **Costo total**
- Herramientas: $0-$30 (Zapier gratis, Carrd gratis).
- Tiempo: **16-20 horas** (2.5 días de trabajo focused).
- **Total monetario: menos de $50** (solo si usas plan pagado de Zapier).

---

### **Resultado que **MATA** la hipótesis**
**Condición de abandono (fallo concluyente):**

- **Menos del 10% de las agencias contactadas** (es decir, <5 de 50) aceptan pagar el depósito de $50 **después de ver el prototipo funcionando con sus datos**.
- **O**, si encuentras que **más del 70% ya usan una herramienta existente** (DashThis, Whatagraph, ReportGarden) y están satisfechos con ella.
- **O**, si en las llamadas dicen: "*$200 es demasiado para el valor que veo*" o "*ya lo hacemos en 2h con Excel*".

---

### **Por qué esto funciona**
- **Mide行为, no opiniones**: El depósito reembolsable filtra a los que solo "quieren ayudar" vs. los que tienen dolor real.
- **Barato y rápido**: No desarrollas, solo automatizas lo existente.
- **Conclusión clara**:
  - Si **≥10% aceptan** → Hipótesis viable (validación temprana).
  - Si **<10% aceptan** → Hipótesis muerta. El precio no se justifica o el dolor no existe.

---

### **Siguientes pasos si sobrevive**
Si pasa el test, el próximo experimento es construir un **MVP con 3 clientes de pago real** (no depósito) en 2 semanas, usando el mismo flujo manual "detrás del telón". Pero si fallas aquí, **abandonas hoy** y ahorras 2 meses de desarrollo.

**Ejecuta esto en 1 semana. Si no hay fila para pagar $50, no hay fila para pagar $200.**