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
  · Tensión deliberada: el brief pide 900-1.300 palabras y la fuente trae 400-700 (con el contexto, las citas y el relleno que trae una noticia
    real y que el redactor tiene que filtrar). Un
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

In a statement, the company said the investment would help it remain independent and keep offering both open and commercial models. Its executives have argued in public interviews that Europe needs its own players in a technology that is becoming strategic for governments and businesses, and that relying entirely on foreign providers creates risks for sovereignty and competitiveness.

Mistral's products include a chat assistant for consumers and businesses, as well as models specialized in tasks such as programming. The company sells access through an application programming interface, which lets developers pay according to how much they use, and it also signs agreements with large corporate clients that want dedicated deployments.

The startup has built partnerships with several of the large cloud providers, which distribute its models to their own customers. Those agreements give a young company access to sales channels that would take years to build alone.

European policymakers have followed the company's progress closely. The debate over how to regulate artificial intelligence in the European Union included discussions about how the rules would affect local developers of foundation models, and Mistral took part in those conversations.

Competition in the sector remains intense. American companies keep releasing new models at a fast pace, and Chinese developers have published capable open-weight systems of their own, which puts pressure on prices across the market.

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

Vélez has said in interviews that the idea for the company came from his own frustration as a customer of Brazilian banks, where opening an account involved long lines, paperwork and security procedures that seemed designed for the bank rather than for the client. Nubank built its brand around the opposite experience: simple language, quick answers and a purple card that became recognizable across the country.

Much of the bank's early growth came from word of mouth. Customers who were satisfied with the service invited friends and family, which allowed the company to acquire users at a low cost compared with traditional advertising.

The business relies on several sources of revenue. Nubank earns a fee every time a customer uses the card at a store, collects interest on loans and on credit card balances, and sells additional financial products to its existing base. Analysts pay close attention to how much revenue the bank earns per customer and how that figure evolves, because the low cost of serving each client is only an advantage if those clients eventually generate meaningful income.

Credit risk is another key variable. Lending to people who previously had little or no access to formal credit can open a large market, but it also exposes the bank to higher losses when the economy slows down. According to the company, its own data on how customers use the app helps it decide how much credit to offer to each of them.

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

According to the company's founding story, García Ottati, a Venezuelan entrepreneur based in Mexico, came up with the idea after a difficult experience trying to buy a used car himself. Kavak presents itself as a technology business rather than a car dealer: it uses data to decide which vehicles to buy, how much to offer for them and at what price to resell them.

Pricing is one of the central challenges of the model. If Kavak pays too much for a car, it loses money when it sells it; if it offers too little, sellers go elsewhere. The company relies on algorithms that estimate the value of each vehicle based on its brand, model, mileage and condition, and on how quickly similar cars have sold.

Financing is also an important part of the business. Many buyers in Mexico do not have access to traditional car loans, or find the process slow and complicated. By offering credit at the moment of purchase, Kavak can sell to customers who would otherwise not be able to buy, and it earns income from the loans themselves.

The used-car market in Latin America has historically been fragmented, with many small dealers and private sellers and little reliable information about prices. Several startups in the region have tried to bring more transparency to it, with different degrees of success, and some have shut down after struggling with the cost of holding inventory.

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

The Collison brothers, who grew up in Ireland, started Stripe with a simple product: a way for developers to accept card payments on a website by adding a few lines of code, at a time when setting up online payments often required long negotiations with banks and complex technical integrations.

Since then, Stripe has expanded into a wide range of financial infrastructure: billing for subscription businesses, tools to calculate and collect sales taxes, fraud prevention, corporate cards and services that let platforms pay out money to sellers and freelancers. The company's strategy is to become the financial back office of internet businesses, so that customers add more of its products as they grow.

The annual letter has become a regular event in the technology industry. Each year the founders use it to describe the state of the business, comment on trends in online commerce and explain the bets the company is making. Because Stripe does not publish quarterly results like a listed company, the letter is one of the few official windows into its performance.

Stripe competes with traditional payment processors, with banks and with other technology companies, some of them listed on the stock market. Competition has pushed the sector to offer more features, such as local payment methods that vary from country to country and tools that help merchants recover failed payments.

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

The company was founded by Liang Wenfeng, who also co-founded the quantitative hedge fund that finances it. According to people familiar with the company, it hired many young researchers from Chinese universities and focused on research rather than on building commercial products quickly.

In its technical documentation, DeepSeek described several engineering techniques that helped it reduce costs, including an architecture that activates only part of the model for each request and methods that make training more efficient on the chips it had available. Researchers in other countries said the papers were detailed and that some of the ideas could be adopted by other labs.

The release also reopened the debate over American export controls. The United States has limited the sale of its most advanced chips to China, arguing that they could be used for military purposes. Some commentators said DeepSeek's results showed that the restrictions were pushing Chinese companies to become more efficient; others said they proved that the controls needed to be tightened further.

Several American technology leaders reacted publicly to the news, some praising the work and others questioning whether the company had disclosed all the resources it used. OpenAI said it was reviewing whether its models had been used improperly to train competing systems.

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

Part of the shares in the offering were sold by Klarna itself and the rest by existing shareholders, among them several venture capital funds that backed the company during its years as a private business.

Klarna has expanded beyond installments. Its app now works as a shopping tool where consumers can compare products, track deliveries and manage their payments, and the company has introduced a debit card and savings features in some markets. The goal, according to the company, is to become a broader financial service that customers use every day, not only at the moment of checkout.

Partnerships with large retailers and payment platforms have been key to its distribution. When a big online store offers Klarna as an option at checkout, the company reaches a large audience without having to acquire each customer directly.

Competition in buy now, pay later is intense. Klarna competes with other specialized firms, with large technology companies that have launched their own installment options and with banks that let customers split card purchases. Margins depend heavily on the cost of funding and on how many customers fail to repay.

Investors who bought shares in the offering will follow the company's quarterly reports closely, especially indicators such as credit losses, growth in transaction volume and the revenue Klarna earns from each purchase it finances. The first trading day is often read as a signal of market appetite, but analysts tend to look at how a stock performs over several months before drawing conclusions.

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

Field, who serves as chief executive, started working on the idea while still at university and later left his studies to focus on the company with the support of a fellowship for young founders. The product took a long time to develop before it was released to the public, partly because running a professional design tool inside a browser required solving difficult technical problems.

Figma grew through a model that combines a free plan for individuals with paid plans for teams and large organizations. Designers often adopted the tool on their own and then brought it into their companies, where developers, product managers and marketing teams also began to use it to review and comment on designs.

When the acquisition was announced, many users expressed concern on social media that Adobe would raise prices or change the product. Adobe said at the time that it intended to keep Figma running as a separate product and to learn from its collaborative approach.

Regulators focused on the possibility that Adobe was buying Figma to remove a future competitor, a type of deal sometimes described as a "killer acquisition." The case was followed closely by technology lawyers and investors because it was among the largest acquisitions of a private software company ever attempted.

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

The founders met while serving in Unit 8200, the Israeli military intelligence unit known for training many of the country's technology entrepreneurs, and the company keeps a large research and development center in Israel.

Wiz's product became popular because it can be connected to a company's cloud accounts without installing software on each server, a design known as an agentless approach. Security teams get a map of their systems and can see how a single misconfiguration could be combined with other weaknesses to expose sensitive data.

According to Google, Wiz will join Google Cloud after the transaction closes, and its team will keep working on products for customers that use several cloud providers at the same time. Executives from both companies said that most large organizations today use more than one cloud, and that security tools must work across all of them.

Investors in Wiz include several of the best-known venture capital firms in the United States and Israel. The startup raised money at increasingly higher valuations in a short period, which made it one of the fastest-growing software companies of its generation.

The deal is also significant for the Israeli technology ecosystem, which has produced many cybersecurity companies that ended up in the hands of large international buyers.

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

The Amodei siblings left OpenAI together with a group of colleagues who shared concerns about how quickly the technology was advancing and how its risks were being managed. Anthropic was organized as a public benefit corporation, a legal structure that requires its directors to consider the impact of their decisions on society, not only on shareholders.

The company has published research on topics such as how to make models follow a set of written principles, how to interpret what happens inside a neural network and how to evaluate dangerous capabilities before releasing a new system. According to Anthropic, this work shapes the way it trains and deploys its products.

Its models are available through its own platform and through cloud providers such as Amazon Web Services and Google Cloud, both of which are also investors in the company. Those partnerships give Anthropic access to computing capacity and to large corporate customers that already buy services from those clouds.

The company has invested in tools for programmers, including an assistant that can write, review and run code from the command line. Competitors have launched similar products, and AI coding assistants have become one of the most dynamic areas of the industry.

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

Under a restricted license, a new bank goes through a mobilization period in which it builds its systems and processes before it can operate fully. Revolut said it would use that period to prepare the launch of its banking services in the United Kingdom.

The road to the license was not easy. Regulators and auditors had raised questions in the past about the company's internal controls, and press reports attributed part of the delay to those issues and to the complexity of its shareholder structure.

Storonsky, who is chief executive, has been outspoken about his ambitions, saying in interviews that he wants Revolut to become a global financial platform present in many countries. The company is known for a demanding work culture and for launching new products at a fast pace.

Revolut's revenue comes from several sources: subscription plans that offer extra features, fees on currency exchange above certain limits, interest earned on customer deposits, card transaction fees and trading services. That diversification has been part of its argument to investors that it can grow profitably.

Competition comes from traditional banks, which have improved their own apps, and from other digital banks and payment companies that also target travelers, freelancers and small businesses.

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

ChatGPT was launched as a free research preview and quickly became one of the fastest-adopted consumer applications ever. Since then, OpenAI has added paid subscriptions for individuals and plans for businesses, schools and large organizations, along with new capabilities such as voice conversations, image generation and web search.

The company's developer platform lets other businesses use its models through an application programming interface, paying according to the volume of text they process. Many startups have built products on top of it, from customer-service tools to programming assistants.

At the same event, OpenAI presented new tools for developers. The most notable was the ability to build apps that run inside ChatGPT conversations: a user can call a service by name while chatting and interact with it without leaving the conversation. The company said that several large consumer brands were among the first partners.

OpenAI also introduced tools to create AI agents, programs that can carry out multi-step tasks on behalf of a user, such as looking up information, filling forms or connecting to other software. The company presented a visual builder intended to let teams design these agents with less code.

Altman told the audience that the developer community building on OpenAI's platform keeps growing, and that the company wants ChatGPT to become a place where people discover and use other services.

According to OpenAI, the new apps are built on an open standard that lets developers connect their services to AI assistants, which in principle could make it easier to adapt the same app to other platforms. The company said it would publish guidelines for developers and review apps before making them available to all users.

OpenAI has also signed agreements with chipmakers and cloud providers to expand its computing capacity, an effort that requires very large investments in data centers. Demand for AI services has grown faster than the available infrastructure, and providers sometimes have to limit access to new features.

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

The founders took part in a well-known startup accelerator in Silicon Valley, and they have described the early days of Rappi as an experiment to test whether people in Bogotá would pay to have almost anything delivered to their door. The app's mustache logo and the orange backpacks carried by its couriers became a familiar sight in the streets of many Latin American cities.

Rappi has received investment from large international funds over the years, which allowed it to grow quickly across the region at a time when its competitors were also expanding aggressively.

The company's financial services include payment cards and credit products offered in partnership with banks in some countries. Fintech is seen as an attractive area because it can generate higher margins than delivery, and because the app already knows its users' purchasing habits, which can help evaluate credit risk.

Executives have said that the company wants users to open the app several times a week, not only when they order dinner. The more services a person uses within the same app, the lower the cost of keeping that customer and the higher the revenue the company can obtain from each one.

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

Según la empresa, la idea surgió al ver que muchos negocios pequeños perdían ventas porque no podían aceptar tarjetas, mientras que sus clientes llevaban cada vez menos efectivo. La propuesta fue eliminar las barreras de entrada: un dispositivo barato, una aplicación sencilla y un registro que se completa sin visitar una sucursal.

El modelo de Clip se basa en cobrar una comisión por cada venta procesada, sin rentas mensuales ni contratos de permanencia. Para un comercio pequeño, eso significa que el costo crece solo cuando crecen sus ventas. La empresa vende sus lectores y terminales en tiendas y en línea, lo que le permitió llegar a negocios que nunca habían tenido relación con un banco.

Con el tiempo, la compañía empezó a ofrecer adelantos de capital a los comercios que usan sus terminales. Como Clip conoce el historial de ventas de cada negocio, puede evaluar el riesgo de prestarle dinero con información que un banco tradicional no siempre tiene.

SoftBank, a través de su fondo para la región, invirtió durante esos años en varias empresas latinoamericanas de pagos, crédito y comercio electrónico, y se convirtió en uno de los inversionistas más activos de América Latina. Viking Global Investors, por su parte, es un fondo estadounidense que invierte tanto en empresas cotizadas como en compañías privadas.

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

Esas obligaciones incluyen preparar documentación técnica, informar sobre los datos usados en el entrenamiento y respetar las normas europeas de derechos de autor. Los modelos considerados de riesgo sistémico, por su capacidad y su alcance, tendrán obligaciones adicionales de evaluación y mitigación de riesgos.

El texto fue propuesto por la Comisión Europea y pasó por una larga negociación entre la Comisión, el Parlamento Europeo y el Consejo, que reúne a los gobiernos de los Estados miembros. Durante ese proceso, la aparición de asistentes conversacionales de uso masivo llevó a los legisladores a incorporar las reglas para los modelos de uso general, que no figuraban en la propuesta original.

Las empresas tecnológicas y algunas asociaciones de startups advirtieron durante la negociación que reglas demasiado estrictas podían frenar la innovación en Europa y favorecer a los competidores de otras regiones. Los defensores de la norma sostienen que unas reglas claras dan seguridad jurídica a las empresas y generan confianza en los usuarios.

Cada Estado miembro debe designar autoridades nacionales encargadas de vigilar el cumplimiento. En España se creó la Agencia Española de Supervisión de la Inteligencia Artificial, con sede en A Coruña.

Las sanciones pueden ser altas. Para las prácticas prohibidas, las multas pueden llegar a 35 millones de euros o al 7% del volumen de negocio anual mundial de la empresa, la cifra que resulte mayor.

La ley se aplica a las empresas que ofrecen sistemas de IA en el mercado europeo, aunque estén fuera de la Unión. Eso incluye a startups latinoamericanas que venden software con funciones de IA a clientes en España o en otros países europeos.

Para una startup que vende software, el primer paso práctico es identificar en qué categoría de riesgo cae cada uno de sus productos, porque de eso dependen las obligaciones. Un asistente de atención al cliente no exige lo mismo que una herramienta que filtra candidatos para un puesto de trabajo.

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

Muchnick, el director ejecutivo, ha contado en entrevistas que se interesó en la industria de alimentos por la ineficiencia de la producción animal. Pichara, académico del área de computación, aportó la base del algoritmo, mientras que Zamora, científico especializado en biotecnología vegetal, trabajó en el estudio de las plantas y sus propiedades.

Uno de los productos más conocidos de la empresa es NotMilk, una bebida vegetal que busca parecerse a la leche de vaca en sabor y textura. Según la compañía, el algoritmo propuso ingredientes que a primera vista no parecían relacionados con la leche, como la piña y el repollo, y que combinados logran un resultado similar.

Además de vender en supermercados, la compañía ha llegado a acuerdos con cadenas de comida rápida y otras empresas de alimentos que usan su tecnología para desarrollar recetas. Ese segundo negocio, el de poner su plataforma al servicio de terceros, es parte de la tesis de los inversionistas: NotCo no sería solo una marca de alimentos, sino una compañía de tecnología aplicada a la alimentación.

Tiger Global, el fondo que lideró la ronda, fue en ese periodo uno de los inversionistas más activos en startups de todo el mundo, incluidas varias de América Latina.

Las grandes empresas de alimentos, por su parte, han lanzado sus propias líneas de productos vegetales, lo que aumenta la competencia en los estantes de los supermercados.

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

Según la empresa, su propuesta busca resolver dos problemas al mismo tiempo: que las personas tengan incentivos concretos para cuidar su salud y que más familias cuenten con un seguro de vida, un producto que en América Latina tiene una penetración baja en comparación con otras regiones.

La compañía se define como una empresa con propósito y cuenta con la certificación de Empresa B, que reconoce a las compañías que cumplen estándares de impacto social y ambiental. Para muchos de sus clientes corporativos, ese componente social, como las donaciones que los trabajadores activan con sus hábitos, es parte del atractivo del beneficio.

Para operar en seguros, Betterfly trabaja con compañías aseguradoras que respaldan las pólizas, mientras que la startup se encarga de la plataforma, la experiencia de usuario y la relación con las empresas clientes. Este modelo, en el que la startup actúa como intermediaria tecnológica, es común en el sector insurtech porque evita reunir desde el inicio el capital que la regulación exige a una aseguradora.

QED Investors, uno de los inversionistas que participaron en la ronda, es un fondo especializado en empresas de servicios financieros con presencia activa en América Latina.

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

Barbieri estudió en Estados Unidos y publicó un libro de historia económica antes de dedicarse a emprender. Ha dicho en entrevistas que su objetivo es que cualquier persona pueda gestionar su dinero desde el teléfono con la misma facilidad con la que usa una red social.

La tarjeta de Ualá funciona con una de las grandes redes internacionales de pago, lo que permite usarla en comercios físicos y en compras en línea, incluidas las plataformas extranjeras. Para muchos jóvenes argentinos fue la primera tarjeta propia, porque se obtiene sin trámites en una sucursal ni requisitos de ingresos.

La empresa gana dinero con las comisiones que pagan los comercios cada vez que se usa la tarjeta, con los intereses de los préstamos y con otros servicios financieros. Como ocurre con otras fintech, el desafío es que los usuarios no solo abran una cuenta, sino que la usen todos los días y adopten más productos.

SoftBank y Tencent tienen amplia experiencia invirtiendo en tecnología financiera. Tencent, la empresa china detrás de WeChat, participa en fintech de distintos mercados, mientras que SoftBank creó un fondo dedicado a América Latina con el que invirtió en varias empresas de la región.

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

El corredor de remesas entre Estados Unidos y México es uno de los más grandes del mundo. Muchos trabajadores mexicanos envían dinero a sus familias cada mes, y tradicionalmente lo hacen a través de empresas especializadas o bancos que cobran comisiones y aplican tipos de cambio poco favorables.

Los fundadores vieron una oportunidad en un momento en que comprar criptomonedas en América Latina era complicado y poco confiable. Bitso se presentó desde el inicio como una plataforma que trabaja con las autoridades y aplica controles para prevenir el lavado de dinero, un punto clave para ganar la confianza de usuarios e instituciones.

Además de su aplicación para personas, la empresa ofrece servicios para empresas, como herramientas que permiten a otras compañías enviar y recibir pagos usando criptomonedas como medio de transferencia. En ese modelo, el usuario final puede ni siquiera saber que su dinero pasó por un activo digital: solo ve que llegó más rápido.

Bitso también ha promovido el uso de monedas estables, criptomonedas cuyo valor está atado al dólar, que permiten a los usuarios protegerse de la volatilidad de otros activos digitales y de la depreciación de las monedas locales.

Tiger Global y Coatue figuraron entre los fondos más activos en las rondas de startups latinoamericanas durante ese periodo, con inversiones en fintech, comercio electrónico y software.

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

En materia de opciones sobre acciones, la ley eleva el importe exento de tributación cuando las acciones se entregan a los trabajadores y permite diferir el pago del impuesto hasta que el empleado pueda vender sus participaciones, por ejemplo en una salida a bolsa o en la venta de la empresa. Antes, un trabajador podía tener que pagar impuestos por acciones que todavía no podía convertir en dinero.

Para los inversores, la ley amplía la deducción en el impuesto sobre la renta por invertir en empresas de nueva creación, con el fin de atraer capital privado a las primeras etapas.

Los profesionales extranjeros que se trasladan a España para trabajar en una empresa emergente pueden acogerse además a un régimen fiscal especial para trabajadores desplazados, con condiciones más favorables que el régimen general durante sus primeros años en el país.

La norma forma parte de una estrategia más amplia del Gobierno para convertir a España en un país atractivo para la creación de empresas tecnológicas, y se negoció con asociaciones del ecosistema emprendedor, que llevaban tiempo reclamando un marco específico. Algunas de esas asociaciones la celebraron como un avance, aunque advirtieron que ciertos requisitos podían dejar fuera a empresas que sí son innovadoras y que el proceso de acreditación ante ENISA debía ser ágil para que los beneficios llegaran a tiempo.

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

Sosa, el director ejecutivo, y sus socios comenzaron con un equipo pequeño en Buenos Aires y decidieron entrar muy pronto en Brasil, el mercado de comercio electrónico más grande de América Latina. Esa apuesta convirtió a Nuvemshop en la marca más conocida de la empresa y en su motor de crecimiento.

El modelo de negocio se basa en planes de suscripción que pagan las marcas por usar la plataforma, a los que se suman ingresos por servicios integrados de pagos y envíos. Cuanto más venden las tiendas, más usan esos servicios, de modo que la empresa crece junto con sus clientes.

La compañía también tiene una tienda de aplicaciones donde otros desarrolladores ofrecen herramientas complementarias, como sistemas de facturación, programas de fidelización o integraciones con plataformas de mensajería. Ese ecosistema permite a la plataforma ofrecer más funciones sin tener que construirlas todas.

Insight Partners y Tiger Global, los fondos que lideraron la ronda, tienen amplia experiencia en empresas de software. Para ellos, Tiendanube representa una apuesta por una región donde el comercio electrónico todavía tiene mucho espacio para crecer en comparación con Estados Unidos o Europa.

Según la empresa, muchas de las marcas que usan la plataforma son emprendimientos que comenzaron vendiendo por redes sociales y luego necesitaron una tienda propia para ordenar pedidos, cobros y envíos.

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

Romero, el director ejecutivo, y Ramon ya habían trabajado juntos en otra startup de software antes de fundar la compañía. Según la empresa, el producto nació de una necesidad que conocían de cerca: la de las empresas que crecen y contratan personal sin tener todavía un equipo dedicado a gestionarlo.

La compañía empezó ofreciendo una versión gratuita de su software para atraer a pequeñas empresas y luego pasó a un modelo de suscripción, en el que cada cliente paga según la cantidad de empleados que gestiona y los módulos que contrata. Ese enfoque permitió que muchas pymes probaran el producto sin riesgo antes de comprometerse.

La empresa ha dicho que quiere ampliar su plataforma hacia áreas cercanas a los recursos humanos, como el control de gastos de los empleados y la planificación de turnos. La lógica es que una pyme prefiere usar una sola herramienta en lugar de contratar varias que no se comunican entre sí.

Tiger Global, el fondo que lideró la ronda, fue en ese periodo uno de los inversionistas más activos en startups de software de todo el mundo, con una estrategia basada en invertir rápido y en muchas compañías a la vez.

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

El cambio se comunicó en una publicación del blog de Privacy Sandbox firmada por Anthony Chavez, vicepresidente de Google a cargo del proyecto. Según la empresa, la decisión responde a los comentarios recibidos de anunciantes, editores, reguladores y desarrolladores, y a la constatación de que la transición tendría un impacto significativo en muchas empresas.

Las cookies de terceros son pequeños archivos que permiten a empresas distintas del sitio que se visita seguir a una persona mientras navega por internet. La publicidad digital las usa para mostrar anuncios según los intereses de cada usuario y para medir qué anuncios generan ventas.

Google había anunciado en enero de 2020 su intención de dejar de admitir estas cookies en Chrome. Desde entonces, la fecha se aplazó varias veces, en parte por las dudas de la industria publicitaria y por la revisión de las autoridades de competencia del Reino Unido.

Como alternativa, Google desarrolló un conjunto de tecnologías llamado Privacy Sandbox, pensado para permitir publicidad relevante sin seguir a cada persona de forma individual. La compañía dijo que seguirá trabajando en esas herramientas.

Las herramientas de Privacy Sandbox agrupan a los usuarios por intereses generales o procesan la información dentro del propio navegador, de modo que los anunciantes reciben datos agregados en lugar de perfiles individuales.

Los editores de sitios web, en especial los medios de comunicación y los blogs que viven de la publicidad, habían advertido que perder las cookies de terceros podía reducir sus ingresos, porque los anuncios dirigidos suelen pagarse mejor que los genéricos. Los anunciantes, por su parte, temían perder la capacidad de medir con precisión el retorno de sus campañas.

La autoridad de competencia británica vigiló el proyecto porque Google es a la vez dueño de Chrome y una de las mayores empresas de publicidad digital. Al eliminar las cookies, Google podía fortalecer su posición frente a otras empresas de publicidad que dependen de ellas, mientras conservaba los datos que obtiene de los usuarios de sus propios servicios.

Otros navegadores, como Safari de Apple y Firefox, bloquean las cookies de terceros por defecto desde hace tiempo.

Para una tienda en línea, la diferencia práctica está en la medición: saber qué anuncio llevó a una compra es más difícil cuando el navegador limita el seguimiento entre sitios.

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

El programa forma parte del Plan de Recuperación, Transformación y Resiliencia, con el que España canaliza los fondos europeos aprobados tras la crisis sanitaria, y lo gestiona Red.es, una entidad pública adscrita al ministerio responsable de la transformación digital.

Los agentes digitalizadores deben cumplir requisitos para adherirse, como acreditar experiencia previa en proyectos de digitalización y una facturación mínima. Cuando la pyme recibe el bono, firma con el agente un acuerdo de prestación de soluciones, y el proveedor cobra con cargo a la ayuda, de modo que la empresa no paga directamente la parte cubierta por el bono.

Cada solución tiene un importe máximo subvencionable y unos requisitos mínimos definidos en las bases. Por ejemplo, un sitio web debe incluir dominio, alojamiento y un diseño adaptable a teléfonos móviles, y el proveedor debe mantener el servicio durante un período mínimo.

Las asociaciones de autónomos y de pymes valoraron que el programa llegara a negocios muy pequeños, que habitualmente quedaban fuera de las ayudas públicas por la complejidad de los trámites. Los agentes digitalizadores, que en muchos casos gestionan la solicitud en nombre del cliente, fueron clave para ese alcance.

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

Los anuncios se hicieron durante Conversations, la conferencia de Meta dedicada a la mensajería con empresas, que se celebró en São Paulo. Brasil es uno de los mercados donde los negocios más usan WhatsApp para vender y atender a sus clientes.

Entre las novedades, Meta anunció que las empresas podrán crear anuncios que llevan a una conversación de WhatsApp sin necesidad de tener una cuenta de Facebook. Hasta ahora, ese paso era una barrera para muchos negocios pequeños que solo usaban WhatsApp para vender.

La compañía también dijo que estaba probando una herramienta de pago para enviar mensajes personalizados y automatizados a los clientes, como recordatorios o novedades de productos. Mark Zuckerberg, director ejecutivo de Meta, adelantó que pronto los negocios podrán publicar anuncios de Facebook o Instagram directamente desde la aplicación.

La aplicación WhatsApp Business es gratuita y está pensada para pequeños negocios: permite crear un perfil con horarios y catálogo de productos, usar respuestas rápidas y etiquetar conversaciones. Las empresas más grandes, que manejan miles de mensajes, suelen usar la plataforma empresarial de WhatsApp a través de proveedores especializados, con costos que dependen del tipo de conversación.

En la plataforma empresarial, las conversaciones se clasifican según su propósito, por ejemplo de marketing, de servicio al cliente o de autenticación, y cada categoría tiene un precio distinto que además varía según el país del destinatario. Para muchas empresas, entender esa estructura es clave para calcular cuánto les cuesta atender por chat.

Los proveedores que integran la plataforma empresarial, conocidos como socios de soluciones, ofrecen herramientas para que varios agentes atiendan desde un mismo número, conectar el chat con sistemas de gestión de clientes y automatizar respuestas con bots. Muchas startups latinoamericanas construyeron su negocio en ese espacio.

Meta también ha impulsado los pagos dentro de WhatsApp en algunos mercados, como Brasil e India, con el objetivo de que el cliente pueda completar una compra sin salir de la conversación.

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

Antes de Canva, Perkins y Obrecht crearon una empresa más pequeña dedicada al diseño de anuarios escolares, que les sirvió para probar la idea de una herramienta de diseño sencilla y en línea. Según la historia que la compañía cuenta con frecuencia, la fundadora recibió muchas negativas de inversionistas antes de conseguir el respaldo para lanzar el producto. Adams, el tercer cofundador, había trabajado en Google y aportó la experiencia técnica para construir el editor en el navegador.

El producto permite crear presentaciones, publicaciones para redes sociales, documentos, carteles y videos desde el navegador, a partir de plantillas que se editan arrastrando elementos. La mayoría de sus funciones son gratuitas, y la empresa gana dinero con suscripciones que desbloquean herramientas y contenido adicional para personas y equipos.

La compañía dijo que usará los recursos para seguir desarrollando productos para empresas, un segmento donde busca competir con las herramientas tradicionales de oficina y de diseño profesional.

Canva también destacó su compromiso de destinar parte de su patrimonio a causas sociales, un tema que sus fundadores han convertido en parte de la identidad de la marca.

La empresa tiene su sede en Australia, un país que no suele asociarse con grandes compañías de software de consumo, y se convirtió en uno de los casos más citados de su ecosistema tecnológico. Tiene oficinas en otras regiones y un equipo que produce plantillas en muchos idiomas, incluido el español.

Canva ofrece gratis su versión de pago a escuelas y organizaciones sin fines de lucro, una política que le permitió llegar a estudiantes y profesores que luego llevan la herramienta a su trabajo.

En el segmento empresarial, la compañía compite con suites de oficina y con herramientas profesionales de diseño. Su argumento es que permite a equipos de marketing y ventas crear materiales sin depender siempre de un diseñador, mientras el área de marca mantiene el control sobre logotipos, colores y tipografías.

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
