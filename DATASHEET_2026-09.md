<!-- doc: snapshot -->
---
title: "Datasheet septiembre 2026 — v4.9: la versión cara dejó de comprar calidad, y ahora está medido dentro de la misma familia"
mes: "2026-09"
fecha_snapshot: "2026-09-01"
version_benchmark: "v4.9.0"
audiencia: "Quien tiene que decidir hoy qué modelo pone en producción, con un presupuesto real"
---

# 📊 Datasheet septiembre 2026

> 📍 **Qué es y qué no.** Esto no reemplaza a HumanEval, MMLU ni SWE-bench. Los
> complementa con lo que esos no miden y a un emprendedor sí le importa: **español que no
> suene traducido, precio del proveedor real, y tareas de negocio ejecutadas de verdad
> dentro de un agente.** Snapshot anterior: [DATASHEET_2026-06.md](DATASHEET_2026-06.md).

## TL;DR

**99 modelos con el examen completo. Los cuatro primeros están dentro de dos centésimas
y tres de ellos cuestan menos de $3 al mes.**

- **Qwen 3.8 Flash es el nuevo #1** con 8,53, a unos **$2 al mes**.
- **GLM 5.3 saca 8,52 y cuesta $21 al mes. Su versión Flash saca 8,51 y cuesta $1.**
  Una centésima de diferencia, dieciocho veces el precio — y son el mismo modelo, del
  mismo proveedor.
- **Claude Opus 4.8 queda #8** con 8,48 y **$117 al mes**: cincuenta y ocho veces el
  precio del líder por cinco centésimas menos.
- Del primero al último de los 99 hay **1,27 puntos sobre 10**. La calidad está apretada;
  el precio no.

## El hallazgo del mes: la versión cara ya no compra calidad, y se puede probar

Que un modelo barato le gane a uno caro siempre admite una réplica: *«son modelos
distintos, de gente distinta»*. Este mes el dato aparece **dentro de la misma familia**,
donde esa réplica no aplica.

| | Calidad | Al mes | Diferencia |
|---|---:|---:|---|
| **GLM 5.3** | 8,52 | $21 | — |
| **GLM 5.3 Flash** | 8,51 | **$1** | −0,01 por 1/18 del precio |

Y en **escribir contenido**, el caso es todavía más marcado:

| | Calidad en Contenido | Al mes |
|---|---:|---:|
| **Claude Opus 5 Fast** | 9,11 | $234 |
| **Qwen 3.8 Flash** | 9,10 | **$2** |

Una centésima. **Ciento diecisiete veces el precio.**

No decimos que los caros sean malos: decimos que **la diferencia que justifica su precio
no aparece en la medición**. Si tu caso es escribir en español, hoy hay que argumentar
muy bien para pagar cien veces más.

## Modelos nuevos

| Modelo | Precio $/M in-out | Estado |
|---|---|---|
| **Qwen 3.8 Flash** | $0,15 / $0,47 | **#1**, calidad 8,53 |
| **GLM 5.3** | $1,40 / $4,40 | **#3**, calidad 8,52 |
| **GLM 5.3 Flash** | $0,07 / $0,25 | **#4**, calidad 8,51 |
| LFM2 24B A2B | — | Sin medir: no está en ningún proveedor al que lleguemos |

## Top por categoría

Ningún modelo gana dos veces. Esa es la respuesta corta a *«¿cuál es el mejor?»*.

### Programar
| | Calidad | Al mes |
|---|---:|---:|
| Qwen 3.8 27B | 9,95 | $15 |
| **Qwen 3.8 Flash** | 9,85 | **$2** |
| Gemma 4 31B | 9,84 | $2 |

### Escribir contenido
| | Calidad | Al mes |
|---|---:|---:|
| Claude Opus 5 Fast | 9,11 | $234 |
| **Qwen 3.8 Flash** | 9,10 | **$2** |
| Claude Fable 5 | 9,09 | $234 |

### Razonar
| | Calidad | Al mes |
|---|---:|---:|
| MiniMax M3 | 8,60 | $6 |
| GPT-5.6 Luna | 8,58 | $3 |
| GLM 5 | 8,56 | $12 |

### Correr dentro de un agente
| | Calidad | Al mes |
|---|---:|---:|
| DeepSeek V3.2 | 8,70 | $5 |
| Qwen 3.6 Max | 8,14 | $29 |
| Tencent Hy3 | 8,05 | $2 |

**Lo más barato que se mantiene arriba** (calidad ≥ 8,4): GLM 5.3 Flash y Qwen 3.7 Flash
a **$1 al mes**; Qwen 3.8 Flash y Gemma 4 31B a **$2**.

## Lo que casi publicamos mal

El primer lote de **Qwen 3.8 Flash** devolvió **8,61** — habría sido el mejor número del
catálogo. Tenía **107 runs de 213 tests**: sesenta y cuatro errores de límite de tasa del
proveedor se llevaron cuarenta pruebas, y no cualesquiera, sino **las más pesadas**
(planificación de negocio 0 de 5, auditoría 4 de 10, razonamiento profundo 3 de 6).

Al completarlas, la nota **bajó a 8,53**. Ocho centésimas de sesgo de supervivencia:
el promedio de los exámenes que alcanzaron a rendirse. Suficiente para inventar un
liderazgo.

No llegó a ninguna página porque un modelo **no rankea hasta rendir el examen entero**.
Es la regla que más incomoda cuando uno quiere publicar rápido, y la que evitó esto.

La causa fue nuestra: cuatro procesos en paralelo contra un modelo lanzado cinco días
antes. Medido — 4 procesos: 64 errores. 2: uno. 1: ninguno.

## Cobertura

| | Junio (v3.0.1) | **Septiembre (v4.9)** |
|---|---:|---:|
| Catálogo | 143 | **209** |
| En el ranking | 91 | **99** |
| Runs válidos | 10.508 | **67.035** |
| Con tarea de agente ejecutada | — | **99 de 99** |

**Los dos «91» no significan lo mismo, y conviene decirlo.** En junio bastaban 50 runs
para rankear; desde agosto hace falta **rendir el examen entero** —las 29 pruebas que
puntúan, con todos sus casos—. El criterio se endureció y aun así el número subió, porque
lo que creció fue la medición: seis veces más runs válidos que en junio.

Los 99 tienen además **una tarea real ejecutada dentro de un agente**, en Docker y con
herramientas. Hasta agosto había once publicados sin eso.

## Caveats honestos

- **La calidad está apretada: 1,27 puntos separan al primero del último.** Leer la tabla
  por posición engaña. Dos modelos con cuatro puestos de diferencia suelen ser
  indistinguibles estadísticamente — lo verificamos este mes con los snapshots de DeepSeek
  y con Claude Opus 5 contra sus antecesores: **empatan dentro del margen de error**.
- **Claude Opus 5 no es top-3 en ninguna de las 29 pruebas.** Es parejo en todo y
  sobresaliente en nada, cuesta $117 al mes y tarda 42 segundos en responder, contra los
  20 de Opus 4.8. Su nota de agosto estaba deprimida por un techo de tokens nuestro; ese
  problema está corregido y aun así el resultado se sostiene.
- **El juez es Phi-4**, un modelo de Microsoft de 14B con licencia MIT, corriendo fuera de
  las casas que fabrican lo que evaluamos. No elimina el sesgo, pero quita el conflicto de
  interés.
- **Precio de lista, no negociado.** Quien tenga acuerdo con un proveedor verá otros
  números.

## Qué sigue

- Una prueba de **responder a un miembro de una comunidad**, que es distinto de responder
  un ticket de soporte: hay contexto de la persona y de la historia. Salió de un caso real
  —el #1 del ranking se sintió genérico haciéndolo— y hoy no lo mide nadie.
- Completar once dimensiones que se publican sobre parte de su examen.
- Subir la cobertura de pruebas del núcleo, hoy en 68% contra un piso de 80%.

---

*Datos abiertos, con la entrada y la salida de cada prueba guardadas para auditar:*
[github.com/ctala/ai-benchmarks-alternativos](https://github.com/ctala/ai-benchmarks-alternativos)
· *Calculadora:* [benchmarks.cristiantala.com](https://benchmarks.cristiantala.com/)
