## Contexto

Cambio de presentación: no se mide nada, se recombina lo que ya está en disco. El porqué y las
decisiones de Cristian están en `DECISIONES.md` (fila del 9-nov-2026, índice v6.0.0); acá solo el
cómo.

## Decisiones de diseño

**Una definición.** `benchmarks/indice.py` tiene el peso (`PESO_HARBOR_EN_CALIDAD = 0.25`), la nota
de Harbor (0,6 × media + 0,4 × piso) y la combinación. El export la calcula una vez y publica
`score_calidad`, `calidad_ci95`, `nota_harbor`, `nota_harbor_se` e `indice_calidad` (los pesos). Las
páginas, el README y la calculadora leen esos campos: no recalculan. `check_indice_calidad` (I1-I6)
lo hace cumplir y es bloqueante.

**Margen, método B.** Bootstrap estratificado por tarea (las 4 tareas fijas, 3 intentos remuestreados
con reposición), con la varianza de cada tarea encogida hacia la varianza agrupada de esa tarea en
todos los rankeados (K0 = 1 frente a k = 3). Sin el encogimiento, 3 de 3 iguales daban error cero.
Semilla fija para que el export sea reproducible. Los dos errores se combinan como independientes:
`1,96 × √((0,75·se_examen)² + (0,25·se_harbor)²)`.

**Sin recalibrar.** `score_calidad` es una escala absoluta 0-10: no pasa por el z-score ni toca la
media/std congeladas de `scoring_reference.json`. El compuesto (`score_global`) y los pilares siguen
sobre el examen y se rotulan «Examen». Que Harbor entre al compuesto queda en `corte-v5-1`, tarea 2.3,
junto a la recalibración.

**Sin dato agéntico.** Sin las tareas no hay nota (no se inventa la mitad que falta): el modelo sale
del ranking con el motivo `sin_dato_agentico` y conserva su ficha.

**Grupo de cabeza.** `bands.grupo_cabeza` global usa la nota nueva y su margen; `MAX_BAND_SHARE` se
queda en 20 %. El export publica `grupo_cabeza` con `n`, `de`, `margen` (mediana de los márgenes del
grupo) y `mas_barato`. Las tablas muestran «≈» en vez de puesto; los parsers que leían la fila «1»
(`check_cortes`, sus pruebas) aceptan «≈».

**Checks que no cuentan.** Un check cuya trampa el agente no puede conocer por lo que ve no
cuenta hasta que su tarea se corrija (`indice.CHECKS_SIN_CONTAR`; hoy 3 de facturación).
`export_harbor` recalcula el reward de cada intento desde el `ctrf.json` sin esos checks y publica
la lista por tarea; I7 exige que cada nombre exista en su `test_outputs.py`. Con la regla apagada
el export reproduce el publicado (control de la simulación). Consecuencia conocida: Harbor queda
como piso (48 de 68 con 4 de 4) hasta las tareas nuevas de `corte-v5-1`.

**Tier.** `cloud_*` es una ruta. El tier publicado se deriva del precio mezclado (3:1) cuando el
declarado es una ruta; la ruta va en el campo `ruta`.

## Riesgos

- Superficies con texto fechado (reviews) cambian de columna: se ordenan por lo que muestran y su
  línea de método sale del export.
- El blog cita cifras del ranking: va por `--check` y la lista de cambios antes del `--write` (parada c).
