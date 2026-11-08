# Qwen 3.6 Plus — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 7.1 | quality: 8.0
- latency_total: 58.656s | tokens_per_second: 58.0
- input_tokens: 179 | output_tokens: 3403

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

### 🧪 EL EXPERIMENTO: Pre-venta con checkout real (sin construir nada)

**Qué haces exactamente:**
1. Monta una landing de 1 página (Carrd, Webflow o incluso Notion). Título claro: `Reportes de agencia automatizados. Sin hojas de cálculo. Sin horas perdidas.`
2. Incluye: 
   - 3 bullets de dolor que resuelve
   - Precio fijo: `$200/mes`
   - Botón: `Reservar acceso anticipado`
   - Checkout real con Stripe (modo test desactivado). Mensaje debajo: `Pre-lanzamiento. Entrega en 14 días. Reembolso completo si no cumplimos o cambias de opinión.`
3. No hagas anuncios. No hagas encuestas. No hagas demos.
4. Contacta manualmente a **100 dueños/gerentes de agencias pequeñas** (5-15 personas, 10+ clientes activos). Usa LinkedIn, email frío o grupos de founders. Envía este mensaje exacto:
   > `Hola [Nombre], estoy lanzando una herramienta que elimina el trabajo manual de reportes a clientes. Cuesta $200/mes y abre en 14 días. Si pagas hoy, te doy 3 meses gratis y precio vitalicio. Si no te funciona, reembolso inmediato. ¿Te interesa probarlo o prefiero no molestarte?`
5. Mide solo una métrica: **pagos completados**.

---

### 💰 Costo real
- Dominio + landing: `$10-15`
- Stripe: `$0` (solo cobra al pagar)
- Outreach: `$0` (manual)
- **Total: ≤$20**

---

### ⏱️ Tiempo
- Montar landing + checkout: `1-2 días`
- Outreach + esperar respuestas: `3-4 días`
- **Total: ≤1 semana**

---

### ☠️ CRITERIO DE MUERTE (exacto)
- **0-1 pagos reales de 100 contactos calificados → MATAR.**
- **≥2 pagos → CONSTRUIR.** (2% es el piso mínimo para un pre-venta en frío. Si no lo alcanzas, no escalarás.)

*Señales secundarias de muerte:*
- >60% responden: `¿Tienen demo?`, `¿Pueden bajarlo a $99?`, `Ya usamos Looker/AgencyAnalytics gratis` → El valor percibido no justifica $200. Pivota o mata.
- >80% ignoran o dicen `no nos interesa` → No hay dolor agudo o no es prioridad. Mata.

---

### 🔪 Por qué este experimento MATA (y no valida)
- Las entrevistas mienten. La gente dice "sí" por educación. El dinero no.
- $200/mes es un umbral alto para una herramienta no probada. Si no están dispuestos a arriesgar $200 hoy con reembolso garantizado, no lo pagarán mañana cuando tengas la app.
- El diseño es **asimétrico**: tú arriesgas 1 semana y $20. Ellos arriesgan $200. Si no cruzan, la hipótesis está muerta. Punto.

---

### 🚫 Qué NO hacer
- No preguntes `¿pagarías $200?`
- No muestres mockups, videos o "próximamente".
- No aceptes "te aviso cuando lances". Eso es ruido.
- No ajustes el precio a mitad de camino. $200 es la hipótesis. Pruébala o entiérrala.

---

### 📊 Resultado → Acción
- **0-1 pagos**: Archiva la idea. Ahorraste 2 meses de desarrollo, ~$8k-15k en costos de oportunidad y la ilusión de un mercado que no existe.
- **2-3 pagos**: Construye solo para ellos. Entrega manual si hace falta. Valida retención a los 30 días.
- **≥4 pagos**: Escala outreach. Empieza a codear. Tienes tracción real, no esperanza.

Si quieres, te paso el template exacto de la landing (estructura + copy) y el flujo de Stripe para que lo tengas listo en 2 horas. Solo dime.