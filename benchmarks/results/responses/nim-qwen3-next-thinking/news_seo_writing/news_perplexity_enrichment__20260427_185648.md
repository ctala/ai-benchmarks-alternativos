# Qwen 3-Next 80B Thinking (NIM) — news_seo_writing/news_perplexity_enrichment

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.41 | quality: 6.88
- latency_total: 22.154s | tokens_per_second: 92.4
- input_tokens: 507 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

Okay, I need to write a 1,000-word article in Spanish about DeepSeek's V4 release, integrating the original extract and the additional data from Perplexity. Let me start by understanding the requirements.

First, the user specified that I'm a journalist for ecosistemastartup.com, so the tone should be professional but accessible, informative with concrete data. Structure with H2 subtitles (using ## in markdown), no H1. Must include a "Que significa esto para tu startup" section, cite verified sources, don't invent data, end with a reflective conclusion, avoid clichés, use SEO keywords naturally.

The original extract says DeepSeek released V4 under MIT license, $0.30 per million input tokens. Additional data from Perplexity includes URLs, key points like MoE architecture, 236B total params, 21B active, trained on 15T tokens, token cache costs $0.03/M (90% discount), company in Hangzhou, spin-off of High-Flyer hedge fund, competes with GPT-4o and Claude Sonnet. Additional data: ~300 employees, no external funding, autofinanced by High-Flyer.

Important: URLs must be in the sources section. Integrate both sources coherently, don't lose any key data.

So, first, I need to structure the article. Let me outline the sections.

Possible H2 sections:

- Introducción: Briefly introduce DeepSeek V4 release, mention MIT license and cost.

- Arquitectura y capacidades técnicas: Detail MoE, parameters, training data, token cache costs.

- Modelo de negocio y financiamiento: No external funding, spin-off from High-Flyer, 300 employees.

- Competencia en el mercado: Comparison with GPT-4o and Claude Sonnet.

- Implicaciones para startups: The "Que significa esto para tu startup" section.

- Conclusión: Reflective ending.

Check if there are other sections needed. Maybe "El camino de DeepSeek hacia la independencia" for the funding part.

Wait, the original extract has the cost as $0.30 per million input tokens, but the additional data says cache de tokens cuesta $0.03/M (90% descuento). Wait, the original extract says $0.30 per million input tokens, but the additional data says cache de tokens costs $0.03/M (90% discount). So maybe the $0.30 is for input tokens, and the cache is cheaper. Need to clarify that.

Looking at the Perplexity data: "Cache de tokens cuesta solo $0.03/M (90% descuento)" — so the cache cost is $0.03 per million, which is a 90% discount compared to something. But the original extract says the model costs $0.30 per million input tokens. So maybe the input tokens are $0.30, and the cache (maybe for output?) is $0.03? Or perhaps the cache is a specific part. Need to check the sources.

The URLs are https://deepseek.com/blog/v4-release and https://techcrunch.com/2026/03/deepseek-v4. But wait, TechCrunch 2026? That's in the future. Maybe a typo? But the user provided that, so I have to use it as is, even if it's a future date. Maybe it's a mistake, but I can't change it. So the TechCrunch article is dated March 2026, which is odd, but perhaps the user made a typo. However, since the instruction says to use the URLs as provided, I should include them.

Now, structure:

- Introduction: DeepSeek launches V4 under MIT license, cost $0.30M input tokens. Mention it's a significant move in open-source AI.

- Arquitectura y capacidades técnicas: MoE with 236B total, 21B active. Trained on 15T tokens. Cache tokens $0.03M (90% discount). Source: DeepSeek blog and TechCrunch.

- Modelo de negocio: Spin-off of High-Flyer hedge fund, based in Hangzhou. No external funding, 300 employees. Self-funded by High-Flyer.

- Competencia: Directly competes with GPT-4o and Claude Sonnet. How? Maybe cost, performance, openness.

- Que significa esto para tu startup: For startups, lower costs, open-source flexibility, no need for expensive cloud services. Can use V4 for custom applications without licensing fees. Cache savings mean cheaper inference costs.

- Conclusion: Reflect on the impact of self-funded AI companies, how open-source models can democratize access, and the potential for more innovation.

Need to make sure all data points are included. Let's check each data point:

- URLs: must be in sources section.

- Key points from Perplexity: MoE 236B total, 21B active; 15T tokens; cache $0.03/M (90% discount); Hangzhou, spin-off High-Flyer; competes with GPT-4o, Claude Sonnet; ~300 employees; $0 external funding.

Original extract: V4 released under MIT license, $0.30 per million input tokens.

So, the cost of $0.30 is for input tokens, and cache is $0.03 per million, which is 90% cheaper than something. Maybe the regular token cost was $0.30, and cache is $0.03? But the original says model costs $0.30 per million input tokens, and cache is $0.03. So perhaps the cache is a different metric. Need to phrase it correctly.

For example: "El costo de procesar tokens de entrada es de $0.30 por millón, mientras que la caché de tokens tiene un costo de solo $0.03 por millón, lo que representa un descuento del 90%."

Yes, that makes sense. So the input tokens are $0.30, cache (maybe output or something else) is $0.03, which is a 90% discount compared to the input cost? Or compared to previous versions or competitors? The Perplexity data says "Cache de tokens cuesta solo $0.03/M (90% descuento)" — so the cache cost is $0.03 per million, which is 90% less than something. Maybe compared to other models' cache costs? But the original extract mentions $0.30 for input tokens. So perhaps the cache cost is a separate figure. Need to present accurately.

Also, the MIT license is important for startups because they can use it freely, modify it, etc.

For the "Que significa esto para tu startup" section: Startups can leverage the open-source model to build custom solutions without licensing fees. Lower costs for inference (especially cache), so they can scale without high expenses. Competing with big models but cheaper, which is good for cost-sensitive startups. Also, since it's self-funded, maybe more stable long-term? Or less reliance on external investors.

Now, sources: include the URLs in a "Fuentes" section at the end, as per the instruction. The URLs provided are https://deepseek.com/blog/v4-release and https://techcrunch.com/2026/03/deepseek-v4.

Need to write in Spanish, no markdown H1, only H2.

Let me start drafting.

First, title: something like "DeepSeek lanza V4: un modelo open-source de alto rendimiento a bajo costo para startups"

But the user didn't specify the title, but in the article, the first section is usually the intro. However, in the structure, the user didn't specify a title, but in practice, articles have titles. But since the instructions say to use H2 for subtitles, and no H1, perhaps the title is not included as a header, but the first paragraph is the intro. Wait, but the instruction says "estructura: usa subtitulos H2 (## en markdown), nunca H1" — so the main title would be H1, but the rule says never H1. So maybe the article doesn't have a title, or the title is part of the intro. But typically, articles have a title. However, the user's instruction says "nunca H1", so the title must be written as plain text, not a header. Or perhaps the first section is the intro without a header, then H2 for the rest. But the instruction says "usa subtitulos H2 (## en markdown), nunca H1" — so the article should not have any H1 headers. So the main title would be outside of the markdown headers, but since it's an article, the title is usually H1. However, per instructions, no H1, so perhaps the title is written as a paragraph, but that's unusual. But the user says "nunca H1", so the article starts with a paragraph, then H2 sections.

But in standard practice, the title is H1. But since the rule says never H1, I'll proceed with no H1, and the first section is the intro paragraph without a header, then the first H2 is for the next section. Alternatively, perhaps the title is written as a regular sentence, but the user didn't specify. To be safe, I'll start with an introductory paragraph without a header, then use H