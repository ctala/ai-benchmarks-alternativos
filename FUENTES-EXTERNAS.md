<!-- doc: vigente | verificado: 2026-11-03 -->
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
| **Terminal-Bench** (Harbor / Laude) | Programar | **Sí, banda informativa** | Envíos por PR a un dataset Apache-2.0 con `result.json` por intento, mínimo 5 intentos por tarea, validación automática. Ojo: el sitio ya muestra **Terminal-Bench 4.0**; los envíos a 2.0 están cerrados a la espera de un proceso nuevo. Nuestro banco ya corre sobre Harbor. |
| **Toolathlon-Verified** (HKUST) | Automatizar | **No se ingesta: se enlaza** (3-nov-2026) | Cumplía los criterios 1, 2, 4 y 5, y falla el 3: ni el repo (`hkust-nlp/Toolathlon`) ni el dataset de trayectorias declaran licencia, y el dataset pide login. Dos issues abiertos preguntan exactamente eso y no tienen respuesta: [#87](https://github.com/hkust-nlp/Toolathlon/issues/87) (24-ago) y [#97](https://github.com/hkust-nlp/Toolathlon/issues/97) (1-oct). Automatizar sigue con la capa propia hasta que respondan. 7 modelos en la tabla principal; última fila 30-ago-2026. |
| **SWE-bench Pro público** (Scale) | Programar | **No se ingesta: se enlaza** (3-nov-2026) | 25 modelos, incluidos baratos y abiertos, pero la tabla pública se arma con JavaScript y no hay dataset con los resultados. El repo `scaleapi/SWE-bench_Pro-os` (MIT) solo trae trayectorias de 9 modelos de 2025 en `traj/`. Además el harness no es uniforme y lo corre una empresa, no la comunidad. |
| **τ²/τ³-bench** (Sierra) | Relación comercial | **Solo si lo corremos nosotros** | MIT y harness abierto, pero la tabla acepta cifras autodeclaradas y no exige trayectorias. Sirve el *método* (pass^k, usuario simulado); la tabla no. |
| **Arena** (ex LMArena) | ninguna como filtro | **Banda de preferencia, nada más** | 419 modelos y 9 M de votos: la mayor cobertura que existe, pero es preferencia humana, no verdad. Sin categoría *Spanish* visible (29 categorías ocultas por revisar). |
| **Artificial Analysis** | velocidad, precio | **No se ingesta** | Independiente, pero el tier gratis es «uso interno, sin redistribución» y republicar exige licencia comercial. Precio y velocidad ya los traemos de OpenRouter (`effort.py --actualizar`). Se enlaza, no se copia. |
| **AgentDojo** (ETH) | seguridad | **No** | Última fila de 2025; sus autores dicen que «no es un leaderboard». `prompt_injection_es` sigue siendo nuestro. |
| **IberBench / La Leaderboard** | Local, español | **Solo para modelos abiertos chicos** | Académicos, Apache-2.0, pero miden modelos de 0,1 a 14 B y ningún modelo de API. El Space de IberBench estaba dormido. Útil para «Local»; el gap español en modelos de pago sigue sin dueño: es nuestro. |

**Sin fuente comunitaria encontrada:** Escribir para publicar, Decidir con documentos (contexto largo con
verdad), seguridad en español. Ahí la capa propia no es complemento: es la única medición.

## El conjunto base de modelos

El **conjunto base** son los modelos rankeados vigentes en `models.py` (sin `retired`, `unavailable` ni
`pendiente_proveedor`) menos los que el último ping de `check_endpoints.py --ranked --guardar` dio MUERTOS.
Hoy son **<!-- AUTO:conjunto_base -->107<!-- /AUTO --> modelos**, con el ping del
<!-- AUTO:conjunto_base_ping -->2026-11-03<!-- /AUTO -->. El número lo calcula `fuentes_externas.py` desde `models.py`,
`models.json` y el ping guardado en `externos/endpoints/`, sin red; `sync_doc_counts.py` lo escribe acá.
Un modelo intermitente o sin credencial no sale del conjunto: existe, y un mal momento no es un retiro.
`python benchmarks/fuentes_externas.py` lista cuáles quedan fuera y por qué.

Las fuentes externas no lo recortan: son **banda informativa**, y una cifra se muestra solo si la fuente midió
la misma versión exacta del modelo. La cobertura medida el 3-nov (5 de 115 con Terminus 2, 12 con cualquier
agente tras la regla de versión, foto de mayo) hace que «sin dato comunitario» sea la norma, no la excepción.
Los modelos sin banda se eligen para medir con el harness oficial solo cuando le importan a un founder
(baratos, abiertos, locales: Qwen 3.8 Flash vs Ornith 1.5 es el primer caso).

**La ingesta (tarea 2.1, 3-nov-2026):** `benchmarks/fuentes_externas.py` guarda una foto fechada con
URL y licencia en `externos/fotos/`, mapea cada envío a nuestras `key` con una tabla explícita (nunca por
`name`) e imprime la cobertura sobre los rankeados, por versión y por agente. La cifra se lee de ahí, no
de este documento. Hoy entra solo Terminal-Bench 2.0: Toolathlon-Verified y SWE-bench Pro se enlazan.

**Cómo se lee Terminal-Bench:** puntúa pares agente + modelo. La cifra principal de un modelo es la del
agente de referencia del harness (Terminus 2); la del mejor agente va aparte y con su nombre. Nunca se
promedian agentes ni versiones.

## Fuentes consultadas

- Terminal-Bench: https://www.tbench.ai/ · dataset https://huggingface.co/datasets/harborframework/terminal-bench-2-leaderboard · envíos https://www.tbench.ai/docs/submitting-to-leaderboard
- Toolathlon: https://toolathlon.xyz/ · https://arxiv.org/abs/2510.25726 · trayectorias HF `hkust-nlp/Toolathlon-Verified_Trajectories`
- SWE-bench Pro público: https://labs.scale.com/leaderboard/swe_bench_pro_public
- τ-bench: https://taubench.com/ · https://github.com/sierra-research/tau2-bench
- Arena: https://arena.ai/leaderboard/text
- Artificial Analysis: https://artificialanalysis.ai/data-api · https://artificialanalysis.ai/data-access
- AgentDojo: https://agentdojo.spylab.ai/results/
- IberBench: https://arxiv.org/html/2504.16921v1 · La Leaderboard: https://arxiv.org/abs/2507.00999
