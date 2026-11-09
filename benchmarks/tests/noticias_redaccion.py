"""
Noticias · redacción — de una fuente a una nota publicable, sin juez.

POR QUÉ EXISTE (9-nov-2026)
---------------------------
Cualquier founder hispanohablante que publica contenido con un LLM (un medio, el blog de
su startup, un newsletter, una comunidad) hace la misma operación: toma una fuente, casi
siempre en inglés, y pide una nota en español de largo de noticia. En el pipeline medido
(Ecosistema Startup) esa operación falló de cuatro formas, y ninguna la ve un juez LLM
porque la nota *parece* buena:

  · **cifras que nadie dijo** — el año del hecho tomado del reloj, la valuación que el
    modelo «sabe», un porcentaje de contexto. El 5-ago-2026, 24 de 29 notas bloqueadas
    en un día fueron por eso, y casi todas por rellenar para llegar al largo;
  · **el dato clave ausente** — 1.000 palabras de contexto y el monto no aparece;
  · **voseo** — excluye a la mayor parte de la audiencia hispanohablante;
  · **fuga de CJK** — un carácter chino en medio de la nota (el fallo que originó
    `integridad_idioma`).

`news_seo_writing` cubre el formato SEO con juez; aquí todo se verifica con código y la
VERDAD ES POR CONSTRUCCIÓN: la fuente va dentro del prompt, así que lo que no está en
ella es ajeno, sea cierto o no en el mundo.

DISEÑO
------
  · Fuentes REESCRITAS desde hechos públicos (no copiadas), 12 en inglés y 13 en español,
    con su URL de origen en un comentario `# fuente:`. Temas de cualquier founder:
    rondas, salidas a bolsa, compras, regulación, ayudas públicas, producto.
  · **Trampas de cifra ajena**: la fuente omite a propósito un dato que el modelo
    probablemente conoce (el año del hecho, la valuación, la cantidad de clientes). Se
    omite, nunca se falsea: la fuente sigue siendo cierta.
  · Tensión deliberada: el brief pide 900-1.300 palabras y la fuente trae 300-450. Un
    modelo que rellena con cifras pierde más (35 %) que uno que se queda corto (15 %).
    Es la misma prioridad del prompt de producción: exactitud antes que largo.
  · Prompt común en `SYSTEM_PROMPT` y `PLANTILLA`; lo que varía son los datos de cada caso.
  · Ningún prompt avisa de la trampa más allá de lo que diría un brief real («solo con
    datos de la fuente»).

Scorer: `benchmarks/scoring_noticias_redaccion.py` (`type: noticias_redaccion`); la
fórmula y los límites de la normalización están documentados allí.
"""

SYSTEM_PROMPT = (
    "Eres redactor de contenido para un founder hispanohablante que publica noticias y "
    "análisis para emprendedores de América Latina y España. Escribes en español neutro, "
    "claro y directo, con subtítulos en Markdown (##)."
)

PLANTILLA = """{brief}

Escribe la nota en español neutro, de 900 a 1.300 palabras, solo con datos de la fuente.

FUENTE:
{fuente}"""


# Cada caso: name, brief, fuente, datos_clave [{valor, entidades}], trampa (documental).
CASOS = [
    # ── En inglés ──────────────────────────────────────────────────────────────
    {
        # fuente: https://en.wikipedia.org/wiki/Mistral_AI
        "name": "mistral_ronda_europea",
        "brief": "Es para el newsletter semanal de una comunidad de founders de software B2B.",
        "trampa": "la fuente no dice el año de la ronda (fue 2024)",
        "datos_clave": [{"valor": 600e6, "entidades": ["Mistral"]},
                        {"valor": 5.8e9, "entidades": ["Mistral", "valuación", "valoración"]}],
        "fuente": """Paris-based Mistral AI has closed a funding round of €600 million, one of the largest ever raised by a European artificial intelligence startup. The round was led by General Catalyst, and it values the company at €5.8 billion.

Mistral was founded by three researchers who previously worked at Google DeepMind and Meta. Arthur Mensch, a former DeepMind researcher, is the chief executive. Since its creation the company has released several large language models, some of them with open weights that developers can download, run on their own servers and modify. Others are offered only through the company's paid platform and through cloud partners.

The startup has positioned itself as a European alternative to American AI labs. Its pitch to large companies and public institutions is that they can deploy powerful models while keeping control of their data, a concern that weighs heavily in sectors such as banking, healthcare and government.

The new capital will be used to expand computing capacity, hire researchers and engineers, and grow the commercial team that sells to enterprises. The company did not give a breakdown of how much would go to each area.

Investors have been pouring money into a small number of companies that train foundation models, because building them requires access to thousands of specialized chips and large teams of scarce researchers. The size of this round puts Mistral among the best-funded model developers outside the United States and China.

For startups that build products on top of language models, the arrival of well-funded alternatives matters: more providers usually mean more pricing options and less dependence on a single supplier. Open-weight models also allow companies to run AI on their own infrastructure, which can lower costs at scale and simplify compliance with data-protection rules.

The announcement was made this week in Paris.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Nubank
        "name": "nubank_salida_a_bolsa",
        "brief": "Es para el blog de una fintech que quiere explicar a sus clientes pymes qué significa una salida a bolsa.",
        "trampa": "la fuente no da la valuación ni el año (diciembre de 2021)",
        "datos_clave": [{"valor": 2.6e9, "entidades": ["Nu", "Nubank"]}],
        "fuente": """Nu Holdings, the parent company of Brazilian digital bank Nubank, made its debut on the New York Stock Exchange on Thursday under the ticker NU. The company priced its initial public offering at $9 per share and raised about $2.6 billion, making it one of the largest listings ever by a Latin American company in the United States.

Nubank was founded in São Paulo by David Vélez, a Colombian-born former venture capitalist, together with Cristina Junqueira and Edward Wible. The company started with a single product: a no-fee credit card managed entirely from a mobile app, at a time when Brazil's banking market was dominated by a handful of large incumbents that charged high fees.

From that first card, Nubank expanded into checking accounts, personal loans, insurance and investment products. It also launched operations in Mexico and Colombia, the two largest markets in Spanish-speaking Latin America.

The bank has no physical branches. Customers open accounts and solve problems through the app and customer-service agents, a model that keeps operating costs low compared with traditional banks.

Among the investors in the offering was Berkshire Hathaway, the conglomerate led by Warren Buffett, which had already invested in the company before it went public.

The listing was closely watched by founders and investors across the region. A large and successful offering by a Latin American startup in New York signals to global investors that companies built in the region can reach a scale comparable to their peers in the United States and Europe.

At the same time, public companies must report results every quarter and face pressure from shareholders, which changes how management makes decisions. Analysts noted that the bank would now have to show investors a path to sustained profitability while it keeps growing in new countries.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Kavak
        "name": "kavak_serie_e",
        "brief": "Es para el blog de una consultora que asesora a marketplaces de América Latina.",
        "trampa": "no dice el año (2021) ni quiénes lideraron la ronda",
        "datos_clave": [{"valor": 700e6, "entidades": ["Kavak"]},
                        {"valor": 8.7e9, "entidades": ["Kavak", "valuación", "valoración"]}],
        "fuente": """Kavak, the Mexican platform for buying and selling used cars, has raised $700 million in a Series E round that values the company at $8.7 billion. The round makes Kavak the most valuable startup in Mexico.

Kavak was founded in Mexico City by Carlos García Ottati together with a group of co-founders. The company buys used cars from individuals, inspects and reconditions them in its own facilities, and resells them online with a warranty and financing options. Buyers can also trade in their current car as part of the purchase.

The model attacks a market known for its lack of trust. Buying a used car from a stranger often involves hidden mechanical problems, paperwork risks and difficult negotiations. Kavak's bet is that customers will pay for certainty: a car that was inspected, a fixed price and a return period.

Kavak operates in Mexico and has expanded to other countries in Latin America, and it has also announced its arrival in Turkey. The company said the new funds will go to geographic expansion, technology and the financing products it offers to buyers.

Operating this kind of business requires a lot of capital. Unlike a pure marketplace that only connects buyers and sellers, Kavak owns the inventory: it buys the cars before it sells them, and it pays for the reconditioning centers and the logistics. That makes the company sensitive to interest rates and to how fast cars move off its lots.

For founders in the region, the round showed that global investors were willing to back capital-intensive models in Latin America when the market is large enough and the problem of trust is clear. It also raised the bar: a company of this size is expected to prove that its unit economics hold up as it grows.""",
    },
    {
        # fuente: https://stripe.com/annual-updates/2024
        "name": "stripe_carta_anual",
        "brief": "Es para el newsletter de un founder de e-commerce que comenta tendencias de pagos.",
        "trampa": "pide convertir «trillion» bien (billón) y no trae la cantidad de empleados ni de clientes",
        "datos_clave": [{"valor": 1.4e12, "entidades": ["Stripe"]},
                        {"valor": 38, "entidades": ["Stripe", "volumen", "creci"]}],
        "fuente": """Stripe, the payments company founded by brothers Patrick and John Collison, published its annual letter to users and investors. According to the letter, businesses running on Stripe processed $1.4 trillion in total payment volume during the year, an increase of 38% compared with the year before.

The company, which has its headquarters in San Francisco and Dublin, said the growth came from businesses of every size, from small online stores to large enterprises that moved more of their operations to the platform.

The letter highlighted artificial intelligence as one of the fastest-growing segments among Stripe's users. AI companies, the founders wrote, are reaching meaningful revenue faster than previous generations of software startups, and many of them sell globally from their first months. Stripe also said it has been using machine learning in its own products, especially in fraud detection.

Another theme of the letter was stablecoins, digital currencies pegged to the value of a traditional currency such as the dollar. The Collisons described them as a useful tool for moving money across borders, an area where traditional transfers can still be slow and expensive.

Alongside the letter, Stripe announced a tender offer for current and former employees that values the company at $91.5 billion. In a tender offer, investors buy shares from employees, which allows staff to turn part of their equity into cash without the company going public.

Stripe remains private and has said repeatedly that it is in no hurry to list its shares on a stock exchange.

For founders who sell online, the letter is a useful reference because it reflects the behavior of a very large sample of internet businesses. The figures describe where the money is moving: more cross-border sales, more software-based businesses and more transactions involving AI products.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/DeepSeek
        "name": "deepseek_caida_nvidia",
        "brief": "Es para el blog de una agencia de automatización que explica a pymes qué pasa con los modelos de IA.",
        "trampa": "no da el año ni el precio de la acción; tienta a dar la cifra exacta de la caída en dólares",
        "datos_clave": [{"valor": 17, "entidades": ["Nvidia"]},
                        {"valor": 600e9, "entidades": ["Nvidia"]}],
        "fuente": """Shares of chipmaker Nvidia fell about 17% on Monday after Chinese startup DeepSeek released an artificial intelligence model that matched the performance of leading American systems while, according to the company, costing a fraction as much to train. The drop erased close to $600 billion of Nvidia's market value in a single session, one of the largest one-day losses in the history of the U.S. stock market.

DeepSeek, based in Hangzhou, is backed by a Chinese hedge fund. The company published a technical report saying that the final training run of one of its models cost about $5.6 million in computing time and used 2,048 Nvidia H800 chips, a version of the company's processors designed to comply with American export restrictions.

Experts quickly pointed out that the figure only covered the final training run and excluded research, earlier experiments and the cost of the hardware itself. Even so, the number challenged the widespread belief that building frontier models requires billions of dollars in chips.

DeepSeek's reasoning model was released with open weights, which means any company can download it and run it on its own infrastructure. Within days, the company's assistant app climbed to the top of download charts in several countries.

Investors worried that if powerful models can be trained with fewer chips, demand for Nvidia's most expensive processors could slow. Other analysts argued the opposite: cheaper models tend to increase total usage, which in the end requires more computing power.

For small companies that use AI, the episode had a practical reading. Competition among model providers was pushing prices down, and open models were becoming a real option for businesses that want to control costs or keep their data in-house.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Klarna
        "name": "klarna_debut_bolsa",
        "brief": "Es para el blog de una startup de pagos a plazos en México que quiere comentar el caso a su audiencia.",
        "trampa": "no da la valuación total ni la cantidad de usuarios de Klarna",
        "datos_clave": [{"valor": 1.37e9, "entidades": ["Klarna"]},
                        {"valor": 40, "entidades": ["Klarna", "acción"]}],
        "fuente": """Swedish payments company Klarna began trading on the New York Stock Exchange on Wednesday under the ticker KLAR. The company priced its initial public offering at $40 per share, above the range it had initially marketed, and raised $1.37 billion.

Klarna is best known for "buy now, pay later," a service that lets shoppers split a purchase into several interest-free installments at checkout. The company pays the merchant up front and earns most of its money from the fees merchants pay, betting that offering installments increases sales enough to make the fee worthwhile.

Founded in Stockholm by Sebastian Siemiatkowski, Victor Jacobsson and Niklas Adalberth, Klarna grew across Europe and then pushed hard into the United States, its most important market in recent years. Siemiatkowski remains chief executive.

The road to the listing was not straight. The company's private valuation dropped sharply during the downturn that hit technology companies after the pandemic boom, and Klarna spent several years cutting costs and trying to show investors it could make money. It also postponed its offering earlier in the year amid market turbulence.

Klarna has spoken publicly about using artificial intelligence to handle a large share of its customer-service conversations, which the company presents as a way to keep costs down as it grows.

Buy now, pay later has drawn attention from regulators in several countries, who worry that consumers may take on debt without fully understanding it. Companies in the sector argue that their products are more transparent than traditional credit cards.

For founders in Latin America, where installment payments are common and card penetration is uneven, the listing showed that investors are willing to back payment models that change how people pay at the checkout, as long as the company can show discipline on costs and credit losses.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Figma
        "name": "figma_adobe_cancelada",
        "brief": "Es para el newsletter de una comunidad de diseñadores de producto y founders SaaS.",
        "trampa": "no dice el año del anuncio (2022) ni de la cancelación (2023)",
        "datos_clave": [{"valor": 20e9, "entidades": ["Adobe", "Figma"]},
                        {"valor": 1e9, "entidades": ["Adobe", "Figma"]}],
        "fuente": """Adobe and Figma have called off their planned merger. The software giant had agreed to buy the collaborative design startup for about $20 billion in cash and stock, but the two companies said there was no clear path to obtain the regulatory approvals needed in Europe and the United Kingdom.

Under the terms of the agreement, Adobe will pay Figma a termination fee of $1 billion.

Figma was founded by Dylan Field and Evan Wallace, who met as students at Brown University. Its product lets teams design interfaces directly in the web browser, with several people editing the same file at the same time. That collaborative approach made it a favorite among product teams and put it in direct competition with Adobe's own design tools.

Competition authorities had expressed concern that the deal would eliminate a rival that was growing quickly and could reduce innovation in design software. The European Commission and the United Kingdom's Competition and Markets Authority had both opened in-depth investigations.

In a statement, both companies said they disagreed with the regulators' conclusions but had decided that it was in their best interest to move forward independently.

The decision means Figma will continue as an independent company, with the termination payment adding to its cash. Adobe, for its part, will keep developing its own collaborative products.

For founders, the case illustrates a risk that is easy to underestimate when an acquisition is announced: the deal is not closed until regulators approve it, and that process can take many months. During that time, the startup must keep its team motivated and its customers calm, without knowing whether it will end up inside a large company or on its own. Large technology deals now face closer scrutiny than in previous years, especially when the buyer is a market leader.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Wiz,_Inc.
        "name": "google_compra_wiz",
        "brief": "Es para el blog de un fondo de capital de riesgo latinoamericano que comenta salidas relevantes.",
        "trampa": "no da los ingresos de Wiz ni el año de su fundación; tienta a mencionar la oferta rechazada con su monto",
        "datos_clave": [{"valor": 32e9, "entidades": ["Google", "Wiz", "Alphabet"]}],
        "fuente": """Google's parent company Alphabet has agreed to acquire Wiz, a cloud security startup based in New York, for $32 billion in cash. It is the largest acquisition in Google's history.

Wiz was founded by Assaf Rappaport, Ami Luttwak, Yinon Costica and Roy Reznik, a team that had previously built a security company that Microsoft acquired. Rappaport is the chief executive. Wiz's software scans the cloud environments of large companies to find vulnerabilities, misconfigurations and exposed data, and shows security teams which risks to fix first.

The company grew very quickly by selling to large enterprises, which have moved more of their systems to cloud providers such as Amazon, Microsoft and Google. Wiz said its products will remain available on all the major clouds after the acquisition, not only on Google's.

The agreement came after an earlier round of talks between the two companies ended without a deal. At that time Wiz decided to stay independent and said it intended to keep growing toward a public listing.

The transaction must still be approved by regulators. Google said it expected the deal to close the following year.

Google Cloud has been investing heavily to compete with Amazon Web Services and Microsoft Azure, which have larger shares of the cloud market. Security is one of the main concerns of companies when they decide which cloud to use, and analysts said the acquisition gives Google a stronger offer in that area.

For founders, the deal is a reminder that rejecting an offer can pay off when the business keeps growing, but it is not a guaranteed outcome. It also shows that strategic buyers are still willing to pay very high prices for software companies that solve a critical problem for large enterprises.""",
    },
    {
        # fuente: https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation
        "name": "anthropic_serie_f",
        "brief": "Es para el newsletter de un founder que usa modelos de IA en su producto y comenta el mercado.",
        "trampa": "no dice el año, ni los ingresos, ni la cantidad de clientes empresariales",
        "datos_clave": [{"valor": 13e9, "entidades": ["Anthropic"]},
                        {"valor": 183e9, "entidades": ["Anthropic", "valuación", "valoración"]}],
        "fuente": """Anthropic, the artificial intelligence company that develops the Claude family of models, has raised $13 billion in a Series F round at a post-money valuation of $183 billion. The round was led by ICONIQ, and other investment firms joined it.

Anthropic was founded by former OpenAI researchers, including siblings Dario and Daniela Amodei. Dario Amodei is chief executive. The company describes itself as focused on AI safety research and sells access to its models to businesses and developers, as well as through a subscription product for individuals.

The company said the new capital will support its enterprise growth, investment in safety research and expansion of computing capacity. Anthropic has also been expanding outside the United States.

A large share of Anthropic's business comes from companies that integrate its models into their own products, and from software developers. Programming has become one of the most visible uses of AI models, and the company has launched tools aimed specifically at developers.

Training and serving frontier models requires enormous amounts of computing power, which explains the size of the funding rounds in the sector. Several AI developers have raised multibillion-dollar rounds in a short period, and investors are betting that a few companies will capture a large share of the value of the technology.

For founders who build products on top of these models, the competition among providers has practical consequences: prices per use, the speed at which new capabilities arrive and the risk of depending on a single supplier. Many startups now design their products so they can switch from one model to another with little effort.

The valuation places Anthropic among the most valuable private technology companies in the world.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Revolut
        "name": "revolut_venta_secundaria",
        "brief": "Es para el blog de una startup de pagos internacionales que habla con freelancers de habla hispana.",
        "trampa": "no da la cantidad de clientes de Revolut ni el año de la licencia bancaria británica",
        "datos_clave": [{"valor": 45e9, "entidades": ["Revolut"]}],
        "fuente": """Revolut, the London-based financial technology company, has completed a secondary share sale that values it at $45 billion, making it one of the most valuable private fintech companies in Europe. In a secondary sale, existing shareholders, in this case employees, sell part of their shares to new or existing investors. The company itself does not raise new money.

Investors taking part included Coatue, D1 Capital Partners and Tiger Global.

Revolut was founded by Nik Storonsky, a former trader, and Vlad Yatsenko, a software engineer. It started with a prepaid card that let travelers spend abroad without the high exchange fees charged by traditional banks, and later added current accounts, stock and crypto trading, savings products and business accounts.

The company recently obtained a banking license in the United Kingdom with restrictions, a long-awaited step that allows it to begin offering more traditional banking products in its home market, after a lengthy process with regulators.

The share sale gives employees a way to turn part of their equity into cash while the company remains private. Startups increasingly use this mechanism to retain talent when a public listing is still far away.

Revolut has been expanding in several regions, including Latin America, where it has announced operations in Mexico and Brazil.

For founders who serve freelancers and small businesses that get paid from abroad, the case shows the size of the market for cross-border payments and multicurrency accounts. Charging less than traditional banks for exchanging and sending money was the entry point that Revolut used to win customers, and the same problem remains very relevant for people across Latin America who work for clients in other countries.""",
    },
    {
        # fuente: https://openai.com/devday/
        "name": "chatgpt_usuarios_semanales",
        "brief": "Es para el newsletter de una consultora que ayuda a pymes a adoptar IA en ventas y atención.",
        "trampa": "no dice la fecha del evento ni los ingresos de OpenAI",
        "datos_clave": [{"valor": 800e6, "entidades": ["ChatGPT", "OpenAI"]}],
        "fuente": """OpenAI chief executive Sam Altman said at the company's annual developer conference in San Francisco that ChatGPT now has 800 million weekly users. The figure makes ChatGPT one of the most widely used software products in the world.

At the same event, OpenAI presented new tools for developers. The most notable was the ability to build apps that run inside ChatGPT conversations: a user can call a service by name while chatting and interact with it without leaving the conversation. The company said that several large consumer brands were among the first partners.

OpenAI also introduced tools to create AI agents, programs that can carry out multi-step tasks on behalf of a user, such as looking up information, filling forms or connecting to other software. The company presented a visual builder intended to let teams design these agents with less code.

Altman told the audience that the developer community building on OpenAI's platform keeps growing, and that the company wants ChatGPT to become a place where people discover and use other services.

For small businesses, the announcements raised a practical question: if a growing share of customers start their searches and purchases inside a chat assistant, companies will need to be present there, just as they once had to be present in search engines and social networks. Several analysts compared the moment with the early days of app stores.

Experts also warned that depending on a single platform carries risks. The rules for apps inside ChatGPT, including how they are ranked and how they can charge users, are still being defined. Founders who build on top of a platform they do not control have historically faced sudden changes in visibility and costs.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Rappi
        "name": "rappi_ronda_t_rowe",
        "brief": "Es para el blog de una startup colombiana de logística de última milla.",
        "trampa": "no dice el año (2021) ni la cantidad de ciudades o repartidores",
        "datos_clave": [{"valor": 500e6, "entidades": ["Rappi"]},
                        {"valor": 5.25e9, "entidades": ["Rappi", "valuación", "valoración"]}],
        "fuente": """Colombian delivery company Rappi has raised $500 million in a new funding round led by T. Rowe Price, at a valuation of $5.25 billion.

Rappi was founded in Bogotá by Simón Borrero, Sebastián Mejía and Felipe Villamarín. It started as a grocery delivery app and expanded into restaurant delivery, pharmacy orders, cash withdrawals delivered to the door and a digital wallet called RappiPay. The company describes itself as a "super app": a single application where users can solve many daily needs.

The company operates in several countries in Latin America, including Colombia, Mexico, Brazil, Argentina, Chile and Peru. Competition in delivery is intense in the region, with global players and local companies fighting for both customers and couriers.

Rappi said it would use the new funds to strengthen its fintech business and to expand its "turbo" service, which promises deliveries in a few minutes from small warehouses located close to customers, known as dark stores.

Quick-commerce models like this one require heavy investment: the company must rent and stock warehouses in dense neighborhoods and keep couriers available nearby. In exchange, it controls the inventory and can earn higher margins than when it simply picks up orders from third-party stores.

Delivery apps across Latin America have also faced debates about the working conditions of couriers, who in most countries are classified as independent workers rather than employees. Several governments in the region have discussed rules to change that.

For founders building logistics or commerce businesses in the region, the round was a sign that investors were still betting on the delivery market's long-term potential, even as the economics of fast delivery remained under scrutiny.""",
    },
    # ── En español ─────────────────────────────────────────────────────────────
    {
        # fuente: https://www.businesswire.com/news/home/20210610005759/en/
        "name": "clip_softbank",
        "brief": "Es para el blog de un proveedor de software para comercios de barrio en México.",
        "trampa": "la fuente no da la valuación (se publicó en 2.000 millones) ni el año",
        "datos_clave": [{"valor": 250e6, "entidades": ["Clip"]}],
        "fuente": """La fintech mexicana Clip anunció una inversión de 250 millones de dólares encabezada por SoftBank, a través de su fondo para América Latina, y por Viking Global Investors. Con esta operación, la empresa se convirtió en una de las startups más valiosas de México.

Clip fue fundada por Adolfo Babatz, quien sigue como director general. Su primer producto fue un lector de tarjetas que se conecta al teléfono y permite a cualquier comercio cobrar con tarjeta de débito o crédito sin contratar una terminal bancaria tradicional. Con el tiempo sumó terminales propias, cobros a distancia mediante enlaces de pago y otros servicios financieros para comercios.

El público de Clip son negocios pequeños y medianos: tiendas de barrio, consultorios, talleres, restaurantes y profesionales independientes. En México, una parte importante de los pagos todavía se hace en efectivo, y muchos comercios no aceptaban tarjeta por los costos y requisitos de los bancos.

La compañía dijo que usará los recursos para desarrollar nuevos productos, ampliar su equipo de tecnología y llegar a más comercios en todo el país.

Para los comercios, aceptar tarjeta tiene ventajas claras: evita perder ventas de clientes que no traen efectivo, reduce el riesgo de manejar dinero en el local y deja un registro de las ventas que sirve para pedir crédito. El costo es la comisión que cobra el proveedor por cada transacción.

El mercado de cobros para pequeños comercios en México es competido. Además de los bancos, participan otras empresas tecnológicas y plataformas de comercio electrónico que ofrecen sus propias terminales.

Para los founders de la región, la operación mostró que los inversionistas globales estaban dispuestos a apostar por empresas que atienden a los negocios más pequeños, un segmento que la banca tradicional atendió poco durante años.""",
    },
    {
        # fuente: https://digital-strategy.ec.europa.eu/es/policies/regulatory-framework-ai
        "name": "ley_ia_europea",
        "brief": "Es para el blog de una startup latinoamericana de software que vende a clientes en España.",
        "trampa": "no da fechas de cada etapa de aplicación ni el año de entrada en vigor (2024)",
        "datos_clave": [{"valor": 35e6, "entidades": ["multa", "sancion", "sanción"]},
                        {"valor": 7, "entidades": ["multa", "sancion", "sanción", "factura", "volumen de negocio"]}],
        "fuente": """El Reglamento de Inteligencia Artificial de la Unión Europea, conocido como Ley de IA, entró en vigor el 1 de agosto. Es la primera norma integral sobre inteligencia artificial aprobada por una gran economía y se aplicará por etapas a lo largo de los próximos años.

La ley clasifica los sistemas de IA según su nivel de riesgo. Los de riesgo inaceptable quedan prohibidos: por ejemplo, los sistemas de puntuación social de personas o ciertos usos de reconocimiento de emociones en el trabajo y en la escuela. Los de alto riesgo, como los que se usan para seleccionar personal, otorgar créditos o en infraestructura crítica, deberán cumplir requisitos de calidad de datos, documentación, supervisión humana y ciberseguridad.

Para los sistemas de riesgo limitado, como los asistentes conversacionales, la principal obligación es de transparencia: la persona debe saber que está interactuando con una máquina. Los contenidos generados o manipulados con IA, como las imágenes o videos falsos de personas reales, deberán identificarse como tales.

La norma también incluye reglas específicas para los modelos de IA de uso general, que son la base de muchos productos actuales.

Las sanciones pueden ser altas. Para las prácticas prohibidas, las multas pueden llegar a 35 millones de euros o al 7% del volumen de negocio anual mundial de la empresa, la cifra que resulte mayor.

La ley se aplica a las empresas que ofrecen sistemas de IA en el mercado europeo, aunque estén fuera de la Unión. Eso incluye a startups latinoamericanas que venden software con funciones de IA a clientes en España o en otros países europeos.

La Comisión Europea creó una Oficina de IA para supervisar la aplicación de la norma y prevé espacios controlados de pruebas para que las pymes y startups puedan probar sus sistemas con acompañamiento de las autoridades.""",
    },
    {
        # fuente: https://techcrunch.com/2021/07/26/notco-gets-its-horn-following-235m-round-to-expand-plant-based-food-products
        "name": "notco_serie_d",
        "brief": "Es para el newsletter de una aceleradora de startups de alimentos en Chile y Perú.",
        "trampa": "no dice el año (2021) ni los países donde vende",
        "datos_clave": [{"valor": 235e6, "entidades": ["NotCo"]},
                        {"valor": 1.5e9, "entidades": ["NotCo", "valuación", "valoración"]}],
        "fuente": """La startup chilena NotCo levantó 235 millones de dólares en una ronda Serie D liderada por Tiger Global, con una valuación de 1.500 millones de dólares. Con esta operación, la empresa se convirtió en el primer unicornio de Chile.

NotCo fue fundada por Matías Muchnick, Karim Pichara y Pablo Zamora. La compañía desarrolla alimentos de origen vegetal que buscan imitar el sabor y la textura de productos de origen animal, como la leche, la mayonesa, el helado y la carne molida.

Su diferencia está en el uso de inteligencia artificial. NotCo creó un algoritmo, al que llama Giuseppe, que analiza la estructura molecular de los alimentos de origen animal y propone combinaciones de ingredientes vegetales para reproducir sus características. Según la empresa, esto le permite desarrollar productos más rápido que con los métodos tradicionales de prueba y error.

Entre los inversionistas de la compañía figuran personas conocidas del mundo tecnológico, como Jeff Bezos, a través de su fondo personal.

La empresa dijo que usará los recursos para expandirse a nuevos mercados, ampliar su línea de productos y seguir desarrollando su tecnología.

El mercado de alimentos de origen vegetal creció con fuerza en los últimos años, impulsado por consumidores que buscan reducir el consumo de carne por razones de salud, medioambiente o bienestar animal. Sin embargo, el sector también enfrenta desafíos: los precios suelen ser más altos que los de los productos tradicionales y no todos los consumidores repiten la compra.

Para los founders de la región, NotCo mostró que una startup nacida en Chile puede competir en una categoría global combinando tecnología propia con marcas de consumo, y que los fondos internacionales están dispuestos a invertir en empresas latinoamericanas fuera de los sectores habituales de software y fintech.""",
    },
    {
        # fuente: https://latamlist.com/insurtech-betterfly-becomes-a-unicorn-latamlist/
        "name": "betterfly_unicornio",
        "brief": "Es para el blog de una consultora de recursos humanos que trabaja con pymes en Chile y Colombia.",
        "trampa": "la fuente no da una valuación exacta, solo «supera los 1.000 millones»; tampoco el año",
        "datos_clave": [{"valor": 125e6, "entidades": ["Betterfly"]}],
        "fuente": """La insurtech chilena Betterfly cerró una ronda Serie C de 125 millones de dólares liderada por Glade Brook Capital Partners, con la participación de inversionistas anteriores como QED Investors. Con la operación, la empresa superó una valuación de 1.000 millones de dólares y se sumó a la lista de unicornios latinoamericanos.

Betterfly fue fundada por Eduardo della Maggiora, un emprendedor con experiencia previa en otras empresas tecnológicas. La compañía ofrece a las empresas una plataforma de bienestar para sus colaboradores que combina hábitos saludables con seguros.

El modelo funciona así: los trabajadores registran en la aplicación actividades como caminar, meditar o hacer ejercicio, y acumulan una moneda virtual. Esa moneda se puede canjear por donaciones a causas sociales o por mejoras en la cobertura de un seguro de vida. Los empleadores contratan la plataforma como un beneficio para su personal.

La compañía dijo que usará los nuevos recursos para crecer en América Latina, entrar en nuevos mercados y ampliar los productos de seguros y bienestar que ofrece.

El mercado de beneficios para colaboradores ganó relevancia después de la pandemia, cuando muchas empresas buscaron nuevas formas de cuidar la salud física y mental de sus equipos y de retener talento. Los seguros, por su parte, son un sector tradicional en el que pocas empresas habían cambiado la forma de llegar a los clientes.

Para los founders, el caso de Betterfly muestra una estrategia de distribución que vale estudiar: en lugar de venderle un seguro a cada persona, la empresa le vende a un empleador que lo entrega a todo su equipo. Eso reduce el costo de adquirir cada usuario, aunque obliga a convencer a áreas de recursos humanos que suelen tener presupuestos acotados y ciclos de decisión largos.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Ual%C3%A1
        "name": "uala_serie_d",
        "brief": "Es para el newsletter de una comunidad de founders fintech de habla hispana.",
        "trampa": "no da la cantidad de usuarios ni el año (2021)",
        "datos_clave": [{"valor": 350e6, "entidades": ["Ualá", "Uala"]},
                        {"valor": 2.45e9, "entidades": ["Ualá", "Uala", "valuación", "valoración"]}],
        "fuente": """La fintech argentina Ualá levantó 350 millones de dólares en una ronda Serie D liderada por SoftBank y Tencent, con una valuación de 2.450 millones de dólares. Es una de las rondas más grandes de la historia del ecosistema emprendedor argentino.

Ualá fue fundada por Pierpaolo Barbieri. La compañía comenzó con una tarjeta prepaga asociada a una aplicación móvil, pensada para personas que no tenían cuenta bancaria o que estaban cansadas de los costos y trámites de los bancos tradicionales. Con los años sumó inversiones, préstamos personales, pagos de servicios y una solución de cobros para comercios.

La empresa opera en Argentina y en México, y anunció su llegada a Colombia. El capital nuevo se destinará a esa expansión regional, a desarrollar nuevos productos financieros y a contratar talento.

Uno de los atractivos de Ualá para los inversionistas es la inclusión financiera. En varios países de América Latina, una parte importante de la población no tiene acceso a productos bancarios básicos, como una cuenta o una tarjeta, y opera principalmente con efectivo.

La competencia en el sector es intensa. Además de los bancos, que lanzaron sus propias aplicaciones, compiten otras fintech locales y regionales. Para diferenciarse, las empresas buscan ofrecer más productos dentro de la misma aplicación y aumentar el uso diario.

Para los founders, el caso de Ualá también muestra cómo una startup puede crecer en un país con alta inflación y controles cambiarios, condiciones que complican la planificación financiera y la relación con inversionistas extranjeros. Expandirse a otros países de la región es, en parte, una forma de diversificar ese riesgo.""",
    },
    {
        # fuente: https://news.crunchbase.com/fintech-ecommerce/tiger-global-coatue-lead-bitsos-250m-series-c-as-company-gains-unicorn-status
        "name": "bitso_serie_c",
        "brief": "Es para el blog de una startup que procesa pagos internacionales para freelancers en México.",
        "trampa": "no dice el año (2021) ni la cantidad de clientes",
        "datos_clave": [{"valor": 250e6, "entidades": ["Bitso"]},
                        {"valor": 2.2e9, "entidades": ["Bitso", "valuación", "valoración"]}],
        "fuente": """La plataforma de criptomonedas Bitso, con sede en México, levantó 250 millones de dólares en una ronda Serie C liderada por Tiger Global y Coatue, con una valuación de 2.200 millones de dólares. Con esta operación se convirtió en el primer unicornio cripto de México.

Bitso fue fundada por Daniel Vogel, Pablo González y Ben Peters. Su plataforma permite comprar, vender y guardar criptomonedas como bitcoin y ether usando pesos mexicanos y otras monedas locales.

Uno de los usos que más ha impulsado la empresa son las remesas. Las personas que viven en Estados Unidos pueden enviar dinero a sus familias en México a través de criptomonedas, que luego se convierten a pesos. Según la compañía, este mecanismo puede ser más rápido y barato que algunos servicios tradicionales de envío de dinero.

Además de México, Bitso opera en otros países de la región, como Argentina y Brasil. La empresa dijo que usará el capital para crecer en América Latina, desarrollar nuevos productos y fortalecer sus áreas de cumplimiento regulatorio.

El sector de las criptomonedas es volátil. Los precios de los activos digitales cambian con fuerza en periodos cortos, y eso afecta el volumen de operaciones y los ingresos de las plataformas. Además, la regulación varía de un país a otro y sigue en desarrollo en buena parte de la región.

Para los founders que trabajan con pagos internacionales, el caso de Bitso muestra que el problema de mover dinero entre países sigue abierto y que hay espacio para nuevos modelos. También recuerda que construir sobre una infraestructura nueva exige invertir temprano en cumplimiento y en la relación con los reguladores.""",
    },
    {
        # fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2022-21739
        "name": "ley_startups_espana",
        "brief": "Es para el blog de una gestoría online que asesora a founders latinoamericanos que quieren abrir empresa en España.",
        "trampa": "no da el año de la ley (2022) ni cifras de cuántas empresas se acogieron",
        "datos_clave": [{"valor": 15, "entidades": ["Impuesto sobre Sociedades", "impuesto de sociedades", "Sociedades"]},
                        {"valor": 25, "entidades": ["Impuesto sobre Sociedades", "impuesto de sociedades", "Sociedades", "general"]}],
        "fuente": """España cuenta con una Ley de fomento del ecosistema de las empresas emergentes, conocida como Ley de Startups, que busca atraer emprendedores, inversión y talento al país.

Para acogerse a la ley, una empresa debe ser de nueva creación o tener como máximo 5 años de antigüedad, o 7 años en el caso de empresas de biotecnología, energía o industria. También debe tener un modelo de negocio innovador y escalable, y su volumen de negocio anual no puede superar los 10 millones de euros. La condición de empresa emergente la acredita la Empresa Nacional de Innovación, ENISA.

Uno de los beneficios principales es fiscal. Las empresas emergentes tributan en el Impuesto sobre Sociedades a un tipo reducido del 15%, frente al tipo general del 25%, durante el primer ejercicio con base imponible positiva y los tres siguientes, siempre que mantengan la condición de empresa emergente.

La ley también mejora el tratamiento de las opciones sobre acciones para empleados, una herramienta común en las startups para atraer talento cuando no pueden pagar sueldos altos. Además, facilita la llegada de trabajadores extranjeros mediante un régimen de visados para teletrabajadores de carácter internacional y para emprendedores.

Otra medida relevante es la simplificación de trámites: la ley busca que constituir una sociedad sea más rápido y barato, con procesos telemáticos.

Para los founders latinoamericanos que piensan en España como puerta de entrada a Europa, la ley ofrece incentivos concretos. Sin embargo, conviene revisar con un asesor los requisitos exactos antes de tomar decisiones: la condición de empresa emergente no es automática, y algunos beneficios dependen de mantener ciertos requisitos a lo largo del tiempo.""",
    },
    {
        # fuente: https://latamlist.com/e-commerce-platform-nuvemshop-raises-500m-series-e/
        "name": "tiendanube_serie_e",
        "brief": "Es para el newsletter de una agencia que ayuda a marcas pequeñas a vender en línea.",
        "trampa": "no da la cantidad de tiendas ni el año (2021)",
        "datos_clave": [{"valor": 500e6, "entidades": ["Tiendanube", "Nuvemshop"]},
                        {"valor": 3.1e9, "entidades": ["Tiendanube", "Nuvemshop", "valuación", "valoración"]}],
        "fuente": """Tiendanube, la plataforma de comercio electrónico conocida como Nuvemshop en Brasil, levantó 500 millones de dólares en una ronda Serie E liderada por Insight Partners y Tiger Global, con una valuación de 3.100 millones de dólares.

La empresa fue fundada en Argentina por Santiago Sosa junto a un grupo de cofundadores. Su producto permite a pequeñas y medianas marcas crear su propia tienda en línea sin saber programar, con herramientas para gestionar pagos, envíos, inventario y marketing.

La compañía tiene su mayor mercado en Brasil y también opera en Argentina y México. Compite con plataformas globales de comercio electrónico y con los grandes marketplaces de la región.

Tiendanube dijo que usará los recursos para desarrollar nuevos productos, sumar talento y crecer en México y en el resto de América Latina.

La propuesta de la empresa se apoya en una tendencia: cada vez más marcas pequeñas quieren vender por su cuenta, con su propio sitio, en lugar de depender solo de los marketplaces, donde compiten con miles de vendedores y tienen poco control sobre la relación con sus clientes.

Tener una tienda propia, sin embargo, exige que la marca atraiga tráfico por su cuenta, a través de redes sociales, publicidad o comunidad. Por eso muchas plataformas de este tipo ofrecen integraciones con redes sociales y herramientas de marketing.

Para los founders de comercio electrónico, la ronda mostró el interés de los inversionistas por la infraestructura que permite a miles de negocios pequeños vender en línea, un segmento que creció con fuerza durante la pandemia y que sigue siendo una de las apuestas más claras del ecosistema latinoamericano.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Factorial_(company)
        "name": "factorial_unicornio",
        "brief": "Es para el blog de una startup de software de nómina que vende a pymes en España y México.",
        "trampa": "no da la cantidad de clientes ni el año (2022)",
        "datos_clave": [{"valor": 120e6, "entidades": ["Factorial"]},
                        {"valor": 1e9, "entidades": ["Factorial", "valuación", "valoración", "unicornio"]}],
        "fuente": """La startup española Factorial, con sede en Barcelona, levantó 120 millones de dólares en una ronda Serie C liderada por Tiger Global, con una valuación de 1.000 millones de dólares. Con esta operación se convirtió en uno de los pocos unicornios de España.

Factorial fue fundada por Jordi Romero, Pau Ramon y Bernat Farrero. La compañía desarrolla un software de recursos humanos para pequeñas y medianas empresas que centraliza tareas como el control horario, la gestión de vacaciones y ausencias, la documentación de los empleados, la evaluación del desempeño y la preparación de la nómina.

Su punto de partida fue un problema muy común en las pymes: la gestión de personas se hace con hojas de cálculo, correos y papeles, lo que consume tiempo y genera errores. Factorial ofreció una herramienta sencilla, pensada para empresas que no tienen un área de recursos humanos grande.

La empresa dijo que usará los recursos para ampliar su producto, contratar talento y crecer en otros mercados, entre ellos América Latina.

El mercado de software de recursos humanos para pymes es competido, con actores globales y locales. Para diferenciarse, las empresas del sector buscan ofrecer más funciones dentro de una misma plataforma y adaptarse a las reglas laborales de cada país, que cambian de un mercado a otro.

Para los founders que venden software a pymes, el caso de Factorial muestra la importancia de resolver un problema cotidiano con una herramienta fácil de adoptar. También muestra el desafío de expandirse a otros países: cada mercado tiene su propia legislación laboral, y eso obliga a adaptar el producto antes de vender.""",
    },
    {
        # fuente: https://privacysandbox.com/news/privacy-sandbox-update/
        "name": "google_cookies_marcha_atras",
        "brief": "Es para el newsletter de una agencia de marketing digital que trabaja con tiendas en línea.",
        "trampa": "no dice cuándo se anunció el cambio (2024) ni el porcentaje de usuarios de Chrome",
        "datos_clave": [{"entidades": ["Google", "Chrome"], "frases": ["cookies de terceros"]}],
        "fuente": """Google anunció que ya no eliminará las cookies de terceros de su navegador Chrome, como había planeado durante años. En su lugar, la compañía propuso un enfoque en el que los usuarios puedan tomar una decisión informada sobre su privacidad al navegar, una elección que podrán ajustar en cualquier momento.

Las cookies de terceros son pequeños archivos que permiten a empresas distintas del sitio que se visita seguir a una persona mientras navega por internet. La publicidad digital las usa para mostrar anuncios según los intereses de cada usuario y para medir qué anuncios generan ventas.

Google había anunciado en enero de 2020 su intención de dejar de admitir estas cookies en Chrome. Desde entonces, la fecha se aplazó varias veces, en parte por las dudas de la industria publicitaria y por la revisión de las autoridades de competencia del Reino Unido.

Como alternativa, Google desarrolló un conjunto de tecnologías llamado Privacy Sandbox, pensado para permitir publicidad relevante sin seguir a cada persona de forma individual. La compañía dijo que seguirá trabajando en esas herramientas.

Otros navegadores, como Safari de Apple y Firefox, bloquean las cookies de terceros por defecto desde hace tiempo.

Para las tiendas en línea y las agencias de marketing, la decisión de Google reduce la urgencia de cambiar sus sistemas de medición, pero no elimina la tendencia de fondo: los usuarios y los reguladores exigen más privacidad. Por eso muchos especialistas recomiendan seguir construyendo datos propios, como listas de correo y registros de clientes, que no dependen de lo que decidan los navegadores.

La medida fue recibida con alivio por parte de la industria publicitaria y con críticas de algunos grupos de defensa de la privacidad.""",
    },
    {
        # fuente: https://www.acelerapyme.gob.es/kit-digital
        "name": "kit_digital_espana",
        "brief": "Es para el blog de una agencia que vende servicios de digitalización a pymes en España.",
        "trampa": "no da el año de lanzamiento ni la cantidad de bonos concedidos",
        "datos_clave": [{"valor": 12000, "entidades": ["10 y 49", "10 a 49", "segmento I", "Segmento I"]},
                        {"valor": 3067e6, "entidades": ["Kit Digital"]}],
        "fuente": """El Kit Digital es un programa de ayudas del Gobierno de España para que pequeñas empresas, microempresas y trabajadores autónomos incorporen soluciones digitales en su negocio. Está financiado con fondos europeos Next Generation EU y cuenta con un presupuesto de 3.067 millones de euros.

La ayuda se entrega en forma de un bono digital que la empresa usa para contratar soluciones con proveedores adheridos al programa, llamados agentes digitalizadores. El monto del bono depende del tamaño de la empresa. En el segmento I, para empresas de entre 10 y 49 empleados, el bono es de 12.000 euros. En el segmento II, para empresas de entre 3 y 9 empleados, es de 6.000 euros. En el segmento III, para empresas de menos de 3 empleados y autónomos, el bono inicial fue de 2.000 euros.

Las soluciones que se pueden contratar incluyen sitio web y presencia en internet, comercio electrónico, gestión de redes sociales, gestión de clientes, inteligencia empresarial y analítica, gestión de procesos, factura electrónica, comunicaciones seguras y ciberseguridad.

Para solicitarla, la empresa debe registrarse en la plataforma Acelera pyme, completar un test de diagnóstico digital y cumplir requisitos como estar al corriente con Hacienda y la Seguridad Social.

El programa se convirtió en una oportunidad de negocio para miles de proveedores tecnológicos, que se adhirieron como agentes digitalizadores para vender sus soluciones a pymes con el bono.

También generó críticas. Algunas pymes se quejaron de soluciones de baja calidad o de proveedores que ofrecían productos genéricos sin adaptarlos a cada negocio.

Para los founders que venden software a pymes en España, el Kit Digital mostró cómo una ayuda pública puede acelerar la adopción de tecnología, pero también que el cliente necesita acompañamiento real para sacarle provecho a la herramienta que compra.""",
    },
    {
        # fuente: https://techcrunch.com/2023/06/27/whatsapp-business-crosses-200m-maus-introduces-personlized-messages-feature/
        "name": "whatsapp_business_empresas",
        "brief": "Es para el blog de una startup que automatiza la atención al cliente por WhatsApp en Colombia y Perú.",
        "trampa": "no dice el año (2023) ni la cantidad total de usuarios de WhatsApp ni el crecimiento desde 2020",
        "datos_clave": [{"valor": 200e6, "entidades": ["WhatsApp Business", "WhatsApp"]}],
        "fuente": """Meta informó que la aplicación WhatsApp Business, la versión de su servicio de mensajería pensada para empresas, superó los 200 millones de usuarios activos mensuales. La compañía presentó además nuevas funciones para que los negocios lleguen a sus clientes dentro de los chats.

Entre las novedades, Meta anunció que las empresas podrán crear anuncios que llevan a una conversación de WhatsApp sin necesidad de tener una cuenta de Facebook. Hasta ahora, ese paso era una barrera para muchos negocios pequeños que solo usaban WhatsApp para vender.

La compañía también dijo que estaba probando una herramienta de pago para enviar mensajes personalizados y automatizados a los clientes, como recordatorios o novedades de productos. Mark Zuckerberg, director ejecutivo de Meta, adelantó que pronto los negocios podrán publicar anuncios de Facebook o Instagram directamente desde la aplicación.

La aplicación WhatsApp Business es gratuita y está pensada para pequeños negocios: permite crear un perfil con horarios y catálogo de productos, usar respuestas rápidas y etiquetar conversaciones. Las empresas más grandes, que manejan miles de mensajes, suelen usar la plataforma empresarial de WhatsApp a través de proveedores especializados, con costos que dependen del tipo de conversación.

Para Meta, la mensajería con empresas es una fuente de ingresos que busca hacer crecer, porque cobra a las compañías por ciertas conversaciones y por los anuncios que llevan a los chats.

En América Latina, WhatsApp es una de las herramientas de comunicación más usadas, tanto entre personas como entre clientes y empresas. Para muchos negocios pequeños es el canal principal de ventas: reciben pedidos, envían fotos de productos y confirman pagos por chat.

Para los founders que construyen software sobre WhatsApp, el anuncio confirma el tamaño del canal, pero también recuerda que dependen de las reglas de Meta. Cambios en precios, políticas o funciones de la plataforma pueden afectar directamente su modelo de negocio. Diversificar canales y entender bien las condiciones de uso es parte del trabajo de cualquier empresa que opera sobre una plataforma de terceros.""",
    },
    {
        # fuente: https://en.wikipedia.org/wiki/Canva
        "name": "canva_valuacion",
        "brief": "Es para el newsletter de una comunidad de creadores de contenido y freelancers de diseño.",
        "trampa": "no dice el año (2021) ni la cantidad de usuarios",
        "datos_clave": [{"valor": 200e6, "entidades": ["Canva"]},
                        {"valor": 40e9, "entidades": ["Canva", "valuación", "valoración"]}],
        "fuente": """La plataforma de diseño australiana Canva levantó 200 millones de dólares en una nueva ronda que valúa a la compañía en 40.000 millones de dólares, lo que la ubicó entre las startups privadas más valiosas del mundo.

Canva fue fundada en Sídney por Melanie Perkins, Cliff Obrecht y Cameron Adams. Perkins, que es directora ejecutiva, tuvo la idea mientras daba clases de programas de diseño en la universidad y veía lo difícil que era para sus estudiantes aprender herramientas profesionales.

El producto permite crear presentaciones, publicaciones para redes sociales, documentos, carteles y videos desde el navegador, a partir de plantillas que se editan arrastrando elementos. La mayoría de sus funciones son gratuitas, y la empresa gana dinero con suscripciones que desbloquean herramientas y contenido adicional para personas y equipos.

La compañía dijo que usará los recursos para seguir desarrollando productos para empresas, un segmento donde busca competir con las herramientas tradicionales de oficina y de diseño profesional.

Canva también destacó su compromiso de destinar parte de su patrimonio a causas sociales, un tema que sus fundadores han convertido en parte de la identidad de la marca.

El crecimiento de Canva se apoyó en un modelo que muchos founders estudian: un producto gratuito y fácil de usar que atrae a millones de personas, y una versión de pago que convierte a una parte de ellas en clientes. Para que funcione, el producto gratuito debe ser realmente útil y el paso a la versión de pago debe ofrecer un valor claro.

Para los creadores de contenido y los freelancers, la ronda confirmó que las herramientas de diseño accesibles se convirtieron en parte central del trabajo diario de marketing de pequeñas y grandes empresas.""",
    },
]


TESTS = [
    {
        "name": c["name"],
        "description": f"Nota de 900-1.300 palabras solo con datos de la fuente · trampa: {c['trampa']}",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": PLANTILLA.format(brief=c["brief"], fuente=c["fuente"])},
        ],
        "expected_answer": {
            "type": "noticias_redaccion",
            "fuente": c["fuente"],
            "datos_clave": c["datos_clave"],
            "rango_palabras": (900, 1300),
        },
    }
    for c in CASOS
]
