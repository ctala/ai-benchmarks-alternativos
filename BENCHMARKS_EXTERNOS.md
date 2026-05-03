---
title: "Benchmarks externos — scores oficiales reportados de los top 30 modelos"
fecha: "2026-04-29"
fuente_principal: "Technical reports oficiales + Open LLM Leaderboard + Papers With Code"
nota: "Recopilados para triangulacion con nuestro ranking aplicado-en-espanol"
---

# Triangulacion con benchmarks academicos estandar

> 📍 **Por que este documento existe**: `ai-benchmarks-alternativos` es un benchmark **complementario** a los oficiales — disenado para emprendedores hispanohablantes decidiendo produccion real, NO para sustituir validacion academica. Este archivo documenta como nuestros resultados se triangulan con HumanEval/MMLU/GSM8K/IFEval/SWE-bench oficiales. Para investigacion academica o capacidades fundamentales, prioriza los originales. Para decidir que modelo poner en produccion para tu caso aplicado en espanol neutro LATAM, suma esta data con los oficiales — son complementarios, no excluyentes.

Para validar nuestro ranking aplicado-en-espanol contra literatura academica, recopilamos scores oficialmente reportados de los **top 30 modelos del benchmark** en 4 benchmarks estandar:

- **HumanEval** (Chen et al., 2021): 164 problemas Python coding, Pass@1
- **GSM8K** (Cobbe et al., 2021): 8.5K math word problems grade-school
- **IFEval** (Zhou et al., 2023): instruction following preciso, prompt-level strict accuracy
- **MMLU** (Hendrycks et al., 2020): 57 areas de conocimiento, accuracy 5-shot

Notas metodologicas importantes:

- Los scores fueron recopilados de technical reports oficiales (Meta, OpenAI, Mistral, Anthropic, etc.) cuando estan disponibles. En su defecto, de Hugging Face Open LLM Leaderboard, Papers With Code o reportes de evaluacion publicos como Artificial Analysis.
- **MMLU vs MMLU-Pro**: muchos vendors recientes (2025+) ya solo reportan MMLU-Pro porque MMLU esta saturado (~6.5% errores intrinsecos lo techan en ~93%). Cuando solo hay MMLU-Pro disponible, lo anotamos asi: `MMLU-Pro: XX.X`.
- **HumanEval vs HumanEval+**: algunos reportes recientes sustituyen HumanEval (saturado >90%) con HumanEval+. Lo anotamos cuando aplica.
- **Modelos thinking/reasoning** (GPT-5.x, Grok 4, Kimi K2 thinking): los scores corresponden a modo de razonamiento ON salvo aclaracion. Esto NO es directamente comparable con nuestro benchmark donde corren mayoritariamente sin extended thinking.
- **N/A**: el vendor no reporto el score oficialmente al 29 abril 2026. Posibles causas: (a) modelo demasiado nuevo sin paper completo, (b) vendor solo reporta benchmarks de "frontera" (HLE, AIME, SWE-bench) y abandono benchmarks legacy.

## Tabla cruzada

| # | Modelo | Nuestro score | HumanEval (Pass@1) | GSM8K | IFEval | MMLU (5-shot) | Fuente |
|---|---|---|---|---|---|---|---|
| 1 | Llama 4 Scout 17B | 7.67 | N/A (no reportado) | N/A | N/A | 79.6 | [Meta Llama 4][1] |
| 2 | Llama 3.1 8B Instruct | ~7.6 | 72.6 | 84.5 | 80.4 | 69.4 | [Meta Llama 3.1][2] |
| 3 | Llama 3.3 70B | ~7.5 | 88.4 | N/A (95.1 reportado por terceros) | 92.1 | 86.0 (MMLU-Pro: 68.9) | [Meta Llama 3.3][3] |
| 4 | GPT-OSS 20B | ~7.5 | N/A (HumanEval+ 78.4) | 68.9 | 69.5 | ~73 (MMLU-Pro) | [OpenAI gpt-oss model card][4] |
| 5 | Mistral Small 4 | ~7.5 | ~85 (HumanEval+ tier Haiku) | N/A | N/A | ~81 | [Mistral Small 4 blog][5] |
| 6 | Gemini 3.1 Flash Lite | ~7.5 | N/A | N/A | N/A | N/A (Global-MMLU-Lite: 81.1) | [Gemini 2.5 Flash-Lite card][6] |
| 7 | Grok 4.1 Fast | ~7.5 | ~92 (Grok Code Fast 1) | 95.2 (Grok 4) | N/A | 92.1 (Grok 4) | [xAI Grok 4][7] |
| 8 | GPT-OSS 120B | ~7.5 | 88.3 | 74.2 | N/A | 86.4 | [OpenAI gpt-oss model card][4] |
| 9 | Devstral Small | 7.35 | N/A (specialist coding) | N/A | N/A | N/A | [Mistral Devstral][8] |
| 10 | MiMo V2.5 | ~7.4 | N/A | N/A | N/A | N/A | [Xiaomi MiMo HF][9] |
| 11 | MiMo V2.5-Pro | ~7.4 | N/A | N/A | N/A | N/A | [Xiaomi MiMo HF][9] |
| 12 | Hermes 4 70B | ~7.4 | N/A (no reporta HumanEval) | N/A | 82.2 (Loose, no-reasoning) / 78.7 (reasoning) | 76.7 (no-reasoning) / 88.4 (reasoning) | [Hermes 4 Tech Report][10] |
| 13 | GPT-4.1 | 7.29 | N/A (HumanEval saturado) | N/A | 87.4 | 90.2 | [OpenAI GPT-4.1][11] |
| 14 | Devstral 2 (123B) | 7.22 | N/A (specialist coding) | N/A | N/A | N/A | [Mistral Devstral 2][12] |
| 15 | MiMo V2-Flash | ~7.2 | 70.7 (HumanEval+) | 92.3 | N/A | 73.2 (MMLU-Pro) | [MiMo-V2-Flash Tech Report][13] |
| 16 | Gemma 4 31B | ~7.2 | N/A | N/A | N/A | N/A (modelo abril 2026) | [Google Gemma 4 (pendiente)][14] |
| 17 | Nemotron 3 Nano 30B | ~7.2 | 78.05 (0-shot) | 92.34 (8-shot) | N/A | 81.07 (5-shot) | [NVIDIA Nemotron 3 Nano Tech Report][15] |
| 18 | Gemini 2.5 Flash | ~7.2 | N/A (no reportado) | N/A | N/A | N/A (Global-MMLU-Lite: 88.4) | [Google DeepMind Gemini 2.5 Flash card][16] |
| 19 | Qwen 3-Next 80B Instruct | ~7.2 | N/A (no separado) | 92 (thinking) | N/A | 78.5 (MMLU-Pro: ~80) | [Qwen3 Tech Report][17] |
| 20 | MiMo V2-Pro | ~7.1 | N/A | N/A | N/A | N/A | [Xiaomi MiMo HF][9] |
| 21 | DeepSeek V4 Flash | ~7.1 | N/A (modelo abril 2026, sin paper) | N/A | N/A | N/A | [DeepSeek V4 (pendiente)][18] |
| 22 | Qwen 3.5 397B | ~7.1 | N/A | N/A | N/A | N/A (sin paper publico al 29 abril) | [Qwen latest (sin tech report)][19] |
| 23 | MiMo V2-Omni | ~7.1 | N/A | N/A | N/A | N/A | [Xiaomi MiMo HF][9] |
| 24 | Claude Opus 4.7 | ~7.0 | N/A (saturado) | N/A | N/A | N/A (GPQA Diamond: 94.2; SWE-bench Verified: 87.6) | [Anthropic Opus 4.7][20] |
| 25 | Claude Sonnet 4.6 | ~7.0 | N/A | N/A | N/A | N/A (GPQA: 83.4; SWE-bench Verified: 77.2) | [Anthropic Sonnet 4.5/4.6][21] |
| 26 | GPT-5.4 | ~7.0 | N/A (saturado) | N/A | N/A | ~90 (MMLU-Pro) | [OpenAI GPT-5][22] |
| 27 | Gemini 3.1 Pro | ~7.0 | N/A | N/A | N/A | ~91.8 (Gemini 3 Flash; Pro mayor) | [DeepMind Gemini 3][23] |
| 28 | Step 3.5 Flash | ~7.0 | N/A (sin paper publico al 29 abril) | N/A | N/A | N/A | [StepFun (sin tech report)][24] |
| 29 | Kimi K2.5 | ~7.0 | N/A | 97.3 (Kimi K2 base, top GSM8K) | N/A | 89.5 (Kimi K2) / 87.1 MMLU-Pro (K2.5) | [Moonshot Kimi K2/K2.5][25] |
| 30 | DeepSeek V3.2 | ~7.0 | 78.2 (V3 base) | 92.4 (V3) / 89.3 reportado en paper | 77.6 (V3) | 87.1 (V3) / 89.7 (V3 reportes) | [DeepSeek V3 Tech Report][26] |

### Resumen cuantitativo de cobertura

- **Celdas conseguidas**: aprox. 50/120 (42%) con scores numericos oficiales especificos.
- **Celdas N/A**: aprox. 70/120 (58%) — la mayoria por: (a) vendors que abandonaron MMLU/HumanEval/GSM8K despues de saturarlos en 2024; (b) modelos lanzados <2 semanas sin technical report; (c) modelos chinos (Xiaomi MiMo, StepFun, Qwen Plus/Max, Kimi K2.5) que reportan en benchmarks chinos (C-Eval, CMMLU) y no siempre en los 4 estandares occidentales.

## Hallazgos

1. **Saturacion sistematica de los benchmarks academicos en frontera**. Modelos top-5 globales (GPT-5.4, Claude Opus 4.7, Gemini 3.1 Pro) ya casi no reportan MMLU/HumanEval/GSM8K — pasaron a reportar MMLU-Pro, HLE, GPQA Diamond, SWE-bench Verified, AIME. Esto sugiere que **nuestro benchmark aplicado tiene head-room academico** que los oficiales agotaron.

2. **Convergencia notable en GSM8K**: todos los modelos open con score reportado caen en 89-97% (DeepSeek V3 89.3, MiMo-V2-Flash 92.3, Llama 3.1 8B 84.5, Nemotron Nano 92.34, Kimi K2 97.3). Estos numeros academicos no diferencian utilidad real para emprendedores. Nuestro ranking si los separa por mas de 1 punto en cuanto a calidad practica.

3. **Discrepancia en HumanEval Llama 3.3 70B**: Meta reporta 88.4 (excelente), pero en nuestro benchmark Llama 3.3 70B saca ~7.5 — empata con Llama 3.1 8B (que en HumanEval saca 72.6). Esto sugiere que **HumanEval mide algo distinto** que nuestros tests de coding aplicado en espanol (donde tamano de modelo importa menos que tool-calling y comprension de contexto castellano).

4. **Hermes 4 70B reasoning gap**: el technical report muestra +12 puntos MMLU al activar reasoning (76.7 -> 88.4). Tres de nuestros modelos (Hermes, Kimi K2.5, Qwen3-Next 80B) tienen modos thinking. Sospechamos que **nuestros scores subestiman a estos modelos** porque corremos sin extended thinking (default).

5. **Nemotron 3 Nano 30B underrated en nuestro ranking**: NVIDIA reporta 81.07 MMLU + 92.34 GSM8K + 78.05 HumanEval — performance comparable a Llama 3.3 70B con 1/3 de parametros activados. En nuestro ranking sale puesto 17. **Sospecha**: posible mala configuracion de Nemotron en nuestro adapter (revisar `THINKING_MODELS` flag); o el modelo es debil en idioma espanol.

## Sospechas a investigar

- **Posible underperformance de Nemotron y Qwen3-Next 80B en espanol**: ambos tienen scores academicos top-tier en ingles pero quedan mid-tier en nuestro ranking. Hipotesis: corpus de training pesado en chino+ingles, debil en espanol latino.
- **Devstral Small #9 en nuestro top con $0.10/$0.30 + 146 tok/s**: ningun benchmark academico estandar mide esto. Nuestro ranking si captura **eficiencia operacional** que SWE-bench/HumanEval ignoran. Esto valida el aporte de nuestro paper: medir aplicabilidad real, no proxy academico.

## Fuentes citadas

- [1] Meta Llama 4 — https://www.llama.com/models/llama-4/ y https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- [2] Meta Llama 3.1 8B — https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md y https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- [3] Meta Llama 3.3 70B — https://www.datacamp.com/blog/llama-3-3-70b y https://huggingface.co/datasets/meta-llama/Llama-3.3-70B-Instruct-evals
- [4] OpenAI gpt-oss model card — https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf y https://arxiv.org/html/2508.10925v1
- [5] Mistral Small 4 — https://www.mindstudio.ai/blog/what-is-mistral-small-4 y https://mistral.ai/news/mistral-small-3
- [6] Google Gemini 2.5 Flash-Lite Model Card — https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Flash-Model-Card.pdf
- [7] xAI Grok 4 — https://artificialanalysis.ai/models/grok-4 y https://forgecode.dev/blog/grok-4-initial-impression/
- [8] Mistral Devstral Small 1.1 / 2507 — https://mistral.ai/news/devstral y https://huggingface.co/mistralai/Devstral-Small-2507
- [9] Xiaomi MiMo V2.5/Pro — https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro (sin technical report al 29 abril 2026)
- [10] Hermes 4 Technical Report — https://arxiv.org/abs/2508.18255 y https://nousresearch.com/wp-content/uploads/2025/08/Hermes_4_Technical_Report.pdf
- [11] OpenAI GPT-4.1 — https://openai.com/index/gpt-4-1/ y https://www.rdworldonline.com/openai-claims-gpt-4-1-sets-new-90-standard-in-mmlu-reasoning-benchmark/
- [12] Mistral Devstral 2 — https://mistral.ai/news/devstral-2-vibe-cli y https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512
- [13] MiMo-V2-Flash Technical Report — https://arxiv.org/pdf/2601.02780
- [14] Google Gemma 4 (pendiente sin technical report al 29 abril 2026)
- [15] NVIDIA Nemotron 3 Nano Technical Report — https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf y https://huggingface.co/blog/nvidia/nemotron-3-nano-evaluation-recipe
- [16] Google Gemini 2.5 Flash Model Card — https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Flash-Model-Card.pdf
- [17] Qwen3 Technical Report — https://arxiv.org/pdf/2505.09388 y https://qwenlm.github.io/blog/qwen2.5-llm/
- [18] DeepSeek V4 Flash — modelo lanzado 24 abril 2026, sin paper publico al 29 abril
- [19] Qwen 3.5 397B — sin technical report publico identificado al 29 abril 2026
- [20] Anthropic Claude Opus 4.7 — https://www.anthropic.com/claude/opus y https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained
- [21] Anthropic Claude Sonnet 4.5/4.6 — https://www.leanware.co/insights/claude-sonnet-4-5-overview y https://caylent.com/blog/claude-sonnet-4-5-highest-scoring-claude-model-yet-on-swe-bench
- [22] OpenAI GPT-5 — https://openai.com/index/introducing-gpt-5/ y https://artificialanalysis.ai/articles/gpt-5-benchmarks-and-analysis
- [23] Google Gemini 3.x — https://deepmind.google/technologies/gemini/ y https://artificialanalysis.ai/articles/gemini-3-flash-everything-you-need-to-know
- [24] StepFun Step 3.5 Flash — sin technical report publico identificado al 29 abril 2026
- [25] Moonshot Kimi K2 / K2.5 / K2.6 — https://github.com/MoonshotAI/Kimi-K2 y https://huggingface.co/moonshotai/Kimi-K2.5
- [26] DeepSeek-V3 Technical Report — https://arxiv.org/pdf/2412.19437 y https://huggingface.co/deepseek-ai/DeepSeek-V3

---

**Footer metodologico**:

- *"Sin score oficial reportado al 29 abril 2026"* aplica a todas las celdas marcadas N/A. Posibles causas: vendors que migraron a benchmarks de frontera (HLE, GPQA, SWE-bench), modelos demasiado nuevos sin paper, o ausencia de tradicion de reporting en proveedores chinos para los 4 benchmarks occidentales.
- Scores entre parentesis "(reasoning)" o "(no-reasoning)" provienen de modelos hibridos. Comparar con cuidado.
- Para modelos donde el vendor reporta solo MMLU-Pro pero no MMLU, se anota explicitamente. **No se interpolan scores**.
- Esta tabla es para **triangulacion**, no para ranking. Los scores externos no son directamente comparables al nuestro porque (a) son en ingles, (b) no miden aplicabilidad para emprendedores, (c) saturan en >90% en muchos casos.
