<!-- doc: snapshot -->
---
title: "Lo que el mundo usa no es lo que mejor rinde — nuestro ranking cruzado con el uso real de OpenRouter"
fecha_snapshot: "2026-09-02"
version_benchmark: "v4.9.0"
fuente_uso: "openrouter.ai/rankings — tokens procesados, semana al 1-sep-2026"
audiencia: "Quien está por elegir un modelo mirando qué usan los demás"
---

# Lo que el mundo usa no es lo que mejor rinde

Hay dos formas de responder *«¿qué modelo uso?»*. Una es mirar qué usa todo el mundo. La
otra es medir. **Casi nunca dan lo mismo**, y este documento es el cruce.

A la izquierda, el ranking de OpenRouter por **tokens procesados** — la evidencia más
directa que existe de qué está corriendo hoy en producción, sobre millones de
desarrolladores. A la derecha, nuestro **índice de calidad**: 100 modelos que rindieron el
mismo examen en español, con tareas de negocio y agentes reales.

## El cruce

| Uso | Modelo | Tokens/semana | Calidad | Nuestro puesto |
|---:|---|---:|---:|---:|
| **#1** | DeepSeek V4 Flash 0731 | 12,1T | 8,05 | **#67 de 99** |
| **#2** | GLM 5.3 Flash | 10,0T | 8,51 | **#4** |
| **#3** | GPT-5.6 Luna | 9,52T | 8,52 | **#2** |
| **#4** | MiMo-V2.5 | 7,2T | 8,10 | **#60** |
| **#5** | Tencent Hy3 | 5,89T | 8,49 | **#6** |
| **#6** | Hy4 preview | 5,72T | 8,39 | **#19** |
| **#7** | DeepSeek V4 Flash 0423 | 5,16T | 8,16 | **#49** |
| **#8** | Nemotron 3 Ultra *(free)* | 4,63T | 8,01 | **#74** |
| **#9** | Ox Alpha *(stealth)* | 4,0T | — | *no medible* |
| **#10** | MiniMax M3 *(free)* | 3,77T | 8,17 | **#48** |

## Lo que salta

**El modelo más usado del planeta está en la mitad de abajo de la tabla.** DeepSeek V4
Flash 0731 procesa **12,1 billones de tokens por semana** —más que ningún otro— y queda
**#67 de 99** en calidad. No es malo: saca 8,05 sobre 10 en una población que entera cabe
en 1,27 puntos. Pero hay sesenta y seis modelos que lo hacen mejor, y varios cuestan lo
mismo.

**Y sin embargo, en la cima sí coinciden.** GLM 5.3 Flash es **#2 en uso y #4 en calidad**;
GPT-5.6 Luna, **#3 y #2**; Tencent Hy3, **#5 y #6**. Cuando un modelo es bueno *y* barato,
el mercado lo encuentra rápido.

O sea que el uso no es ciego — es **lento**. Los tres que coinciden son los que llevan
semanas arriba. Los que desentonan son otra historia.

## Por qué se separan

Tres causas, y ninguna es que la gente elija mal:

**El precio del primer día pesa más que la calidad.** Los cuatro más usados cuestan
alrededor de **$1 al mes** con uso normal. Cuando algo es prácticamente gratis, la
diferencia de 0,4 puntos de calidad no aparece en la decisión — no porque no importe, sino
porque nadie la mide antes de integrar.

**El free tier distorsiona.** Dos del top 10 —Nemotron 3 Ultra y MiniMax M3— aparecen ahí
en su versión `:free`. Nosotros **no medimos endpoints gratuitos**, y no es purismo: los
runs contra ids `:free` fallan **69,2%** contra **10,9%** de los pagos, seis veces más.
Un free tier trae límites agresivos y puede servirse con otra cuantización. Lo que la
gente usa gratis no es necesariamente el mismo modelo que compraría.

**La inercia es real.** DeepSeek V4 Flash 0423 —la versión anterior— sigue **#7 en uso**
con 5,16T tokens, tres meses después de que saliera la nueva. Nadie migra un workflow que
funciona.

## Lo incómodo para nosotros

**Dos de los diez modelos más usados del mundo no están en nuestro ranking**, y cada uno
por una razón distinta:

- **Hy4 preview** (#6, 5,72T tokens) — **ya está medido** (3-sep-2026): saca
  8,39 y queda **#19 de 100**. Era un hueco nuestro y se corrigió midiéndolo,
  que es exactamente para lo que sirve publicar este cruce.
- **Ox Alpha** (#9, 4T tokens) — un modelo *stealth*: no figura en el catálogo público, no
  se sabe quién lo hace ni qué versión sirve. **No es medible con nuestro estándar**, que
  exige poder repetir el examen contra el mismo endpoint.
- **Los `:free`** — decisión deliberada, explicada arriba.

Publicar el cruce obliga a mostrar eso. Un ranking que solo se compara consigo mismo nunca
descubre lo que le falta.

## Qué hacer con esto

Si estás por elegir un modelo mirando qué usan los demás, el atajo funciona **solo en la
cima**: los tres primeros en uso están también entre los seis primeros en calidad. Del
cuarto para abajo, el ranking de popularidad deja de predecir el rendimiento.

Y el caso que más se repite —el #1 en uso rindiendo como #67— tiene una lectura práctica:
**no estás eligiendo lo mejor, estás heredando lo que alguien integró primero.** A $1 al
mes de diferencia, cambiar sale casi gratis.

---

*Uso: [openrouter.ai/rankings](https://openrouter.ai/rankings), tokens procesados en la
semana al 1-sep-2026. Calidad: nuestro examen de 29 pruebas en español, datos abiertos en*
[github.com/ctala/ai-benchmarks-alternativos](https://github.com/ctala/ai-benchmarks-alternativos)
*· Calculadora:* [benchmarks.cristiantala.com](https://benchmarks.cristiantala.com/)
