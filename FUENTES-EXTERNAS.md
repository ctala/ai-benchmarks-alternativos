<!-- doc: borrador -->
<!-- creado: 2026-11-03 | para corregir en la sesión de apertura del corte v5.0.0 -->
# Fuentes externas: qué benchmarks públicos usamos y cuáles no

> **Regla de Cristian (3-nov-2026):** *"usemos benchmarks públicos verificados por la comunidad. No
> cualquiera que encontremos. Estandaricemos los modelos que ya tienen los que usemos para los pilares que
> un emprendedor necesita y construimos sobre eso."*

## Criterio de entrada (los cinco, o no entra)

1. **Verificado por la comunidad:** envíos públicos con trayectorias o logs que cualquiera puede revisar, no
   cifras autodeclaradas en la tarjeta del modelo.
2. **Verdad objetiva:** el resultado sale de un check determinístico (test que pasa, estado final de la
   app), no de un juez ni de votos.
3. **Datos por modelo accesibles por script**, con licencia que permita republicarlos citando.
4. **Cubre modelos que un emprendedor hispanohablante paga o corre**, no solo frontera.
5. **Mide una ocasión nuestra.** Si no mapea a una, no importa lo bueno que sea.

## Veredicto por fuente (verificado en sus páginas el 3-nov-2026)

| Fuente | Ocasión | Entra | Por qué, con lo que se vio |
|---|---|---|---|
| **Terminal-Bench** (Harbor / Laude) | Programar | **Sí, filtro duro** | Envíos por PR a un dataset Apache-2.0 con `result.json` por intento, mínimo 5 intentos por tarea, validación automática. Ojo: el sitio ya muestra **Terminal-Bench 4.0**; los envíos a 2.0 están cerrados a la espera de un proceso nuevo. Nuestro banco ya corre sobre Harbor. |
| **Toolathlon-Verified** (HKUST) | Automatizar | **Sí, filtro duro** | Trayectorias públicas en HF, Pass@1 y Pass^3, estado final de la app. Cobertura chica: 7 modelos en la tabla principal (GLM 5.3 Flash, Kimi K3, Opus 4.8, Muse Spark 1.2, DeepSeek V4 Pro, GPT-5.5, Gemini 3.5 Flash). Última fila 30-ago-2026. |
| **SWE-bench Pro público** (Scale) | Programar | **Secundaria** | 25 modelos, incluye baratos y abiertos (Qwen3 Coder, GLM 4.6, Gemma 3, DeepSeek). Pero el harness no es uniforme (5 filas con mini-swe-agent, el resto sin declarar) y lo corre una empresa, no la comunidad. Se muestra como banda, no como filtro. |
| **τ²/τ³-bench** (Sierra) | Relación comercial | **Solo si lo corremos nosotros** | MIT y harness abierto, pero la tabla acepta cifras autodeclaradas y no exige trayectorias. Sirve el *método* (pass^k, usuario simulado); la tabla no. |
| **Arena** (ex LMArena) | ninguna como filtro | **Banda de preferencia, nada más** | 419 modelos y 9 M de votos: la mayor cobertura que existe, pero es preferencia humana, no verdad. Sin categoría *Spanish* visible (29 categorías ocultas por revisar). |
| **Artificial Analysis** | velocidad, precio | **No se ingesta** | Independiente, pero el tier gratis es «uso interno, sin redistribución» y republicar exige licencia comercial. Precio y velocidad ya los traemos de OpenRouter (`effort.py --actualizar`). Se enlaza, no se copia. |
| **AgentDojo** (ETH) | seguridad | **No** | Última fila de 2025; sus autores dicen que «no es un leaderboard». `prompt_injection_es` sigue siendo nuestro. |
| **IberBench / La Leaderboard** | Local, español | **Solo para modelos abiertos chicos** | Académicos, Apache-2.0, pero miden modelos de 0,1 a 14 B y ningún modelo de API. El Space de IberBench estaba dormido. Útil para «Local»; el gap español en modelos de pago sigue sin dueño: es nuestro. |

**Sin fuente comunitaria encontrada:** Escribir para publicar, Decidir con documentos (contexto largo con
verdad), seguridad en español. Ahí la capa propia no es complemento: es la única medición.

## El conjunto base de modelos

El **conjunto base** es la unión de lo que Terminal-Bench, Toolathlon-Verified y SWE-bench Pro público ya
midieron, cruzada con lo que podemos llamar por OpenRouter. Sobre ese conjunto se publica la recomendación
completa por ocasión. Los demás modelos de nuestros 115 se publican con la capa propia y la marca «sin dato
comunitario», y se eligen para medir con el harness oficial solo cuando le importan a un founder (baratos,
abiertos, locales: Qwen 3.8 Flash vs Ornith 1.5 es el primer caso).

**Primer paso de la sesión de apertura:** `benchmarks/fuentes_externas.py` que ingesta las tres fuentes,
mapea nombres a nuestras `key` (regla R5: por key, nunca por name) e imprime la cobertura real sobre los
115. Ese número decide el tamaño del conjunto base.

## Fuentes consultadas

- Terminal-Bench: https://www.tbench.ai/ · dataset https://huggingface.co/datasets/harborframework/terminal-bench-2-leaderboard · envíos https://www.tbench.ai/docs/submitting-to-leaderboard
- Toolathlon: https://toolathlon.xyz/ · https://arxiv.org/abs/2510.25726 · trayectorias HF `hkust-nlp/Toolathlon-Verified_Trajectories`
- SWE-bench Pro público: https://labs.scale.com/leaderboard/swe_bench_pro_public
- τ-bench: https://taubench.com/ · https://github.com/sierra-research/tau2-bench
- Arena: https://arena.ai/leaderboard/text
- Artificial Analysis: https://artificialanalysis.ai/data-api · https://artificialanalysis.ai/data-access
- AgentDojo: https://agentdojo.spylab.ai/results/
- IberBench: https://arxiv.org/html/2504.16921v1 · La Leaderboard: https://arxiv.org/abs/2507.00999
