# Nemotron 3 Ultra 550B — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 93.504s | tokens_per_second: 17.7
- input_tokens: 188 | output_tokens: 1654

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## Experimento: "La Carta de Venta de Una Página + Pre-venta Manual"

**Tiempo total:** 48 horas (2 días laborables)
**Coste total:** $0 - $50 (solo tu tiempo + quizás $20 en café para reuniones)
**Objetivo:** Conseguir **3 compromisos de pago firmes** (tarjeta en mano o transferencia acordada) de $200/mes *antes* de escribir una sola línea de código.

---

### Qué haces exactamente (Paso a paso)

#### Día 1 - Mañana (2 hrs): Construir la "Arma"
1.  **Crea un One-Pager (Notion, Carrd, Google Docs, da igual).** Título: *"Dejas de enviar reportes manuales esta semana"*.
2.  **Copy brutal, sin florituras:**
    *   **Dolor:** "Pierdes 6-10 hrs/mes/client copiando datos de GA4, Meta, Search Console, TikTok... y el cliente solo mira la primera hoja".
    *   **Solución:** "Conectas tus cuentas **una vez**. La herramienta genera el PDF/Slide/Email listo para enviar el día 1 de cada mes. Tú solo apruebas".
    *   **Precio visible y grande:** **$200/mes por agencia (clientes ilimitados).** *No "desde $XX", no "contacta para precio". $200 fijo.*
    *   **El "Gancho de Fundador":** "Estamos aceptando **solo 5 agencias fundadoras**. Pagan $200/mes *para siempre* (price lock), acceden a la beta en 4 semanas y definen las integraciones prioritarias. Después sube a $400/mes".
    *   **CTA único:** Botón/Enlace: **"Quiero ser agencia fundadora →"** (Lleva a un Calendly para llamada de 15 min *o* a un formulario Typeform corto: Nombre, Agencia, # Clientes, Email, "¿Pagas $200/mes hoy para reservar plaza?").

#### Día 1 - Tarde (3 hrs): Salir a cazar (Outbound puro)
**No publiques en LinkedIn. No hagas SEO. No esperes inbound.**
Haz una lista de **50 agencias pequeñas (2-15 empleados)**. Fuentes: Directorio de partners de HubSpot/SEMrush, "Agencia marketing [Tu Ciudad]", LinkedIn Sales Navigator (mes gratis), Apollo.io (gratis), directorios locales.
**Contacto DIRECTO (Email frío + LinkedIn DM):**
> *Asunto: Reportes automáticos para [Nombre Agencia] - 5 plazas fundadoras*
>
> Hola [Nombre Founder/CEO],
> 
> Veo que gestionáis ~X clientes. Supongo que el día 1-5 de mes es un infierno de copiar/pegar datos para reportes.
> 
> Estoy lanzando una herramienta que lo automatiza todo: conectas fuentes → generas reporte blanco → envías. **$200/mes fijo de por vida para 5 agencias fundadoras.** Beta en 4 semanas.
> 
> ¿Te interesa ver la demo cruda y reservar plaza? Si no, sin problema.
> 
> [Enlace Calendly / Typeform]
> 
> Saludos,
> [Tu Nombre]

**Meta:** Enviar **50 contactos personalizados** (mencionando algo real de su web/clientes) en 3 horas.

#### Día 2 (Todo el día): Las 15 min calls / Cierres
*   Si agendaron llamada: **No hagas demo bonita.** Enséñales un Figma feo / Loom de 2 min / Mockup en Excel. Pregunta: *"¿Esto resuelve tu dolor? ¿Me das los $200 del primer mes ahora por Stripe/Transferencia para reservar tu price-lock?"*.
*   Si rellenaron Typeform diciendo "Sí, pago": Envía link de pago Stripe **inmediatamente**. *"Gracias. El precio se fija al cobrar el primer mes. Aquí el link: [Stripe Link]. Tienes 24h."*

---

### Criterio de ABANDONO (Kill Signal) 🛑

**Si a las 48 horas NO tienes 3 pagos confirmados (dinero en cuenta o Stripe "succeeded"), TIRA LA IDEA A LA BASURA.**

No "3 interesados". No "3 reuniones agendadas". **3 PAGOS.**

---

### Por qué este experimento MATA la hipótesis (y por qué duele)

| Excusa típica del founder | Realidad de este test |
| :--- | :--- |
| *"Es que necesito el MVP para mostrar valor"* | **Mentira.** Si el dolor es real y el precio justo, compran el *resultado* (mockup) y la *promesa* (fundador). Si no compran sin ver código, **no comprarán con código**. |
| *"Es que $200 es mucho para decidir en una llamada"* | **Es barato.** Una agencia de 5 clientes factura $5k-$15k/mes. $200 es un redondeo de IVA. Si no sueltan $200 en 15 min, el dolor **no es de $200/mes**. |
| *"Es que el outbound no escala"* | **No buscas escalar.** Buscas **verdad**. 50 contactos = muestra estadísticamente significativa para *validar demanda de pago* en B2B ticket medio. |
| *"Necesito pulir el landing"* | **El landing es excusa.** El copy de arriba convierte si el problema existe. Si no convierte, el problema no existe o el precio es alto. |
| *"Me da corte pedir pasta sin producto"* | **Entonces no eres founder, eres empleado de tu propia quimera.** El dinero del cliente es la única validación que no miente. |

---

### Qué pasa si SÍ consigues los 3 pagos ✅
Tienes **$600 MRR validado**, 3 clientes reales exigiendo features, y **cero riesgo técnico**. *Entonces* te metes 2 meses a construir (o mejor: 2 semanas a no-code + 6 semanas a vender más).

---

### Checklist mental antes de empezar
- [ ] Tienes lista de 50 leads **hoy**.
- [ ] Tienes Stripe/Transferencia listo **hoy**.
- [ ] Tienes Calendly/Typeform listo **hoy**.
- [ ] Tienes el one-pager feo **hoy**.
- [ ] Tienes el mockup/Loom feo **hoy**.
- [ ] **Te has prometido a ti mismo:** "Si no hay 3 pagos en 48h, borro la carpeta del proyecto y paso a la siguiente idea".

**Empieza el cronómetro. Ahora.**