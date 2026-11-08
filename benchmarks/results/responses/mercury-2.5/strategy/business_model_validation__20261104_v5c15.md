# Mercury 2.5 — strategy/business_model_validation

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.28 | quality: 10.0
- latency_total: 7.454s | tokens_per_second: 347.0
- input_tokens: 160 | output_tokens: 2587

## Entrada exacta (lo que recibió el modelo)

**user:**

Quiero crear una app que conecta restaurantes pequenos con proveedores de ingredientes locales. El modelo es marketplace con 15% de comision por transaccion.

Mi hipotesis: los restaurantes pequenos pierden mucho tiempo llamando a multiples proveedores y quieren una solucion digital.

Actua como un VC esceperico. Hazme las preguntas dificiles que me harian en un pitch:
1. Identifica los 5 riesgos principales de este modelo
2. Por que podria NO funcionar en LATAM especificamente?
3. Que tendria que ser verdad para que funcione? (key assumptions)
4. Cual es el escenario donde fracaso rapido y por que?
5. Si solo tuviera $10K para validar, que harias?

No seas amable. Se brutalmente honesto.


## Respuesta completa



No tengo tiempo para rodeos. Tu pitch suena a "unicornio de nicho" pero suena más a negocio de servicios con márgenes delgados. Aquí está el análisis frío.

### 1. Los 5 Riesgos Principales
1.  **Problema del Huevo y la Gallina:** Sin proveedores, los restaurantes no entran. Sin volumen, los proveedores no entran. Quemarás capital tratando de alimentar ambos lados simultáneamente.
2.  **Desintermediación Inevitable:** Una vez que restaurant y proveedor se conocen en tu app, ¿por qué seguir pagándote el 15%? Harán el trato directo por WhatsApp. Tu plataforma es un canal, no una barrera.
3.  **Económicas Unitarias Negativas:** Los ingredientes tienen márgenes de 10-20%. Cobrar 15% es impensable para el restaurante. Si te llevas eso, el proveedor sube el precio y el restaurante busca más barato. Si no, no cubres tus costos operativos.
4.  **Logística de Perishables:** Los productos frescos son un caos. Devoluciones, productos dañados, horarios de entrega estrictos. Gestionar esto sin flota propia es imposible; con flota propia, el CAPEX te hunde.
5.  **Fuga de Clientes (Churn):** Los restaurantes pequeños cierran o cambian de dueño en el primer año. Tu base de usuarios tiene una vida media corta. El CAC (Costo de Adquisición) nunca se amortiza.

### 2. Por qué NO funcionará en LATAM específicamente
*   **Cultura del Efectivo y "Fiado":** En LATAM, muchas transacciones son a crédito o efectivo. Tu app exige digitalización inmediata. ¿Vas a financiar la nómina del restaurante? Si no, el modelo falla.
*   **Informalidad Masiva:** Los proveedores locales más baratos son mercados informales, no empresas estructuradas. No tienen facturación digital ni integración con tu API.
*   **Sensibilidad al Precio Extrema:** El margen neto de un restaurante en LATAM es de un dígito. Un cargo del 15% los quiebra. Prefieren perder 2 horas de un encargado para ir a comprar ellos mismos.
*   **Logística Urbana:** Entregas en ciudades como Ciudad de México, Bogotá o Lima son impredecibles por tráfico y zonas de riesgo. El costo por entrega se comerá tu comisión.

### 3. Lo que tendría que ser verdad (Key Assumptions)
Para que esto no sea una estafa a ti mismo, estas premisas deben ser reales:
1.  El restaurante está dispuesto a pagar una prima del 15% sobre el costo del ingrediente por conveniencia (no te creo).
2.  Los proveedores tienen procesos estandarizados (stock, calidad, horario) listos para integrarse.
3.  El LTV (Valor de Vida del Cliente) es al menos 3x el CAC.
4.  Puedes automatizar la conciliación de pagos y facturas sin equipo manual.
5.  La competencia indirecta (WhatsApp y llamadas directas) no es gratuita e instantánea.

### 4. Escenario de Fracaso Rápido
**Tiempo:** 6 meses.
**Causa:** Liquidez cero.
**Por qué:** Logras registrar 50 restaurantes. Intentas activarlos. Ves que solo compran 1 vez al mes. El proveedor se queja porque los pedidos son pequeños y dispersos. Los restaurantes dicen que es más barato ir en persona. Te quedas sin "quema de capital" y los proveedores cancelan las cuentas por falta de ventas. Cierres porque no hay transacciones recurrentes.

### 5. Si solo tuvieras $10K para validar
No escribas una línea de código.
1.  **Concierge Manual:** Elige un barrio. Consigue 10 restaurantes con WhatsApp. Consigue 5 proveedores.
2.  **Gestión Manual:** Tú recibes el pedido, haces la llamada o WhatsApp al proveedor, coordinas la entrega.
3.  **Cobro Real:** Cobra el 15% de verdad en la primera transacción. Si no pagan, tu modelo es falso.
4.  **Métrica:** ¿Vuelve a pedir la semana siguiente? Si no hay repetición, muere el proyecto hoy.
5.  **Presupuesto:** $2K para visitas a restaurantes, $3K para incentivar proveedores iniciales, $5K para operatividad manual y marketing local.

No construyas una plataforma. Construye una agencia de compras. Si eso escala, entonces habla. Si no, ahorra tu dinero.