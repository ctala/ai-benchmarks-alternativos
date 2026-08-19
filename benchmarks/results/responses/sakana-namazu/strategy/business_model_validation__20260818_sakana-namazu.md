# Sakana Namazu — strategy/business_model_validation

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 10.483s | tokens_per_second: 195.4
- input_tokens: 277 | output_tokens: 2048

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

El usuario quiere que actúe como un VC escéptico y le haga preguntas difíciles sobre su startup de marketplace B2B para restaurantes pequeños y proveedores locales en LATAM. Quiere respuestas en español.

Necesito ser brutalmente honesto, directo, sin azúcar. El VC debe ser escéptico, casi agresivo pero profesional.

Las 5 preguntas/áreas a cubrir:
1. 5 riesgos principales del modelo
2. Por qué podría NO funcionar en LATAM específicamente
3. Key assumptions qué tendrían que ser verdaderas
4. Escenario de fracaso rápido
5. Cómo validar con $10K

Estructura: Voy a responder directamente como el VC, quizás empezando con una frase de desdén, luego atacando cada punto duramente.

Tone check: Brutalmente honesto. Significa decir verdades incómodas sobre el modelo de marketplace B2B en LATAM, que es conocido por ser difícil (bajos márgenes, comportamiento offline, preferencia por crédito/relaciones personales, etc.).

Let me think about each section:

1. Five principal risks:
- Chicken-and-egg (liquidez): sin proveedores no hay restaurantes, sin restaurantes no hay proveedores
- Retención / Habit stickiness: los chefs prefieren WhatsApp, voice notes y crédito informal. Una app es fricción.
- Unit economics: 15% de comisión suena bien pero en LATAM los restaurantes pequeños operan con márgenes de 5-10%. Un 15% sobre ingredientes es inviable o se lo pasan al restaurante, lo cual no pasa. Además, ticket sizes bajos, frecuencia alta, costo de adquisición alto.
- Logistics / Fulfillment: en LATAM si no controlas la logística, la experiencia es mala. Si la controlas, eres logística, no tech. Y logística es capital intensivo.
- Credit risk / Working capital: los restaurantes pequeños pagan a 15-30-45 días. Los proveedores quieren cash. Si tú cobras comisión solo sobre transacción, pero la transacción es a crédito, te conviertes en factoraje o quiebras.

2. Why it might NOT work in LATAM specifically:
- WhatsApp is the real OS of LATAM B2B commerce. It's not just a channel, it's the infrastructure.
- Informality and cash economy. Vendors often don't issue facturas/comprobantes properly or don't want to pay taxes on platform sales.
- Trust is face-to-face. The supplier relationship is built on daily visits, free samples, last-minute emergency deliveries ("me falta un kilo de cebolla para la cena"). An app can't replicate this.
- Price sensitivity. Restaurants in LATAM operate on knife-edge margins. They won't pay 15% more for "convenience" when a mocho (runner/delivery boy) from the central de abastos costs them effectively zero and gives credit.
- Logistics chaos. Traffic, lack of addressing, violence in some areas, perishable goods. If you're just matching but not delivering, the experience breaks. If you deliver, your moat is thin because Rappi, Uber Direct, etc. exist but B2B is different.

3. Key assumptions that need to be true:
- Restaurant owners actually value time saved on ordering enough to change behavior AND pay extra.
- Supplier willingness to digitalize (they are often old-school family businesses with Excel or pen and paper).
- 15% commission is feasible within existing margins or someone else pays (suppliers).
- Frequency and basket size justify CAC. This means restaurants must order several times a week with high AOV.
- Payment terms can be standardized (e.g., net 7 days via the platform, or prepayment works). If not, platform is dead.

4. Fast failure scenario:
- Spend 3 months building perfect app. Launch with 20 suppliers and 50 restaurants. Restaurants check it once, see prices 15% higher or identical, go back to WhatsApp. Suppliers get 2-3 orders, realize it's more work to update inventory in the app than just send a WhatsApp broadcast list, abandon it. Six months in, you have $400 monthly GMV and 15% of that is $60. You burn cash trying to subsidize logistics. A regional player (like a cash-and-carry like Makro, or Cornershop-style B2B, or even Rappi launching B2B) turns on a toggle and crushes you because they already have the trucks and warehouses. You die having "educated the market" for someone else.

5. Validation with $10K:
Don't build an app. Absolutely no code. Use $10K to manually simulate the marketplace.
- Spend $2K on a WhatsApp Business API and a simple landing page (Carrd or similar, maybe a simple Glide app if absolutely necessary, but better just WhatsApp).
- Hire a "mvalorero" (granjero/sales intern) for $1K to manually aggregate orders from 10 restaurants via WhatsApp/phone for 1 month.
- Go to central de abastos with $3K cash, negotiate prices directly, fulfill orders yourself with a rented van/staff for a month (or use on-demand couriers).
- Give restaurants a slight discount or net-7 terms (subsidized by your $10K) to try you.
- Metrics to validate: Repeat rate after 4 weeks, AOV, willingness to continue without subsidy, supplier stickiness.
- If after 4 weeks restaurants aren't demanding you come back and asking to add more SKUs, kill it. If they are, then you know the pain is real and you can raise pre-seed to build a thin V1.
- Actually, with $10K I wouldn't even touch tech beyond a spreadsheet and WhatsApp. 100% concierge MVV (Minimum Viable Voodoo).

Tone refinement:
Start with something like: "Con todo respeto, pero este pitch ya lo escuché unas 20 veces y la gran mayoría están muertos en menos de 18 meses. No me hagas perder el tiempo con el 'Uber de los insumos'. Vamos directo a tus problemas."

Make sure to address the user directly and harshly as a founder in a pitch meeting. Use strong language like "obvio", "fantasía", "mata tu startup", "miento si", etc.

Wait, the user said "Hazme las preguntias dificiles que me harian en un pitch" but then listed 5 specific deliverables that sound like direct answers, not just questions. The prompt structure is:
1. Identifica los 5 riesgos... (Identify)
2. Por qué podría...? (Why)
3. Qué tendría que ser verdad...? (What would have to be true)
4. Cual es el escenario...? (What is the scenario)
5. Si solo tuvieras $10K...? (What would you do)

So I should answer these directly, while maintaining the VC persona. The title says "hazme las preguntas difíciles", but the instructions are "1. Identifica... 2. Por qué..." So I'll frame it as the brutal VC giving the interrogation/feedback directly.

Let's write.

Structure:
- Intro brutal.
- 1. Cinco riesgos que matan tu startup (lista clara).
- 2. Por qué LATAM es tu cementerio (bullet points).
- 3. Tus fantasías convertidas en assumptions (lista de lo que DEBE ser verdad).
- 4. Tu funeral en 12 meses (narrativa de fracaso).
- 5. Con $10K: el test de la verdad (concierge, no code).

Tone: Peruvian/Mexican VC style (LATAM VC), direct, uses words like "chamba", "mocho", "fiado", "central de abastos".

Specific risks to emphasize:
- Risk 1: Chicken and egg / Liquidity risk.
- Risk 2: Unit economics / Commission spread is a lie. Suppliers already have thin margins; restaurants won't absorb 15%. So who pays? If nobody pays 15% net, your model is broken. Maybe 3-5% is possible.
- Risk 3: Trust & credit risk (el fiado). This is huge. The corner store relationship is built on lending.
- Risk 4: Fulfillment/logistics default. If it's just discovery, it's not defensible. If it's delivery, it's heavy.
- Risk 5: Retention/CAC mismatch. Restaurants churn fast (business dies) and AOV might be too low.

On LATAM specifics:
- WhatsApp is not a feature, it's the competitor.
- La confianza es física. The "route salesman" (vendedor de ruta/mocho) already does this job. He knows the kitchen, brings new products, takes back bad produce, extends credit when the owner is short. You're trying to digitize a human relationship.
- Informality: suppliers don't want digital tracks for taxes.
- Price: in LATAM, price rules everything. If the app adds any cost, it's dead.

Key assumptions (must be true