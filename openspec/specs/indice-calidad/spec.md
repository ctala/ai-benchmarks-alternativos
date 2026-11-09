# indice-calidad Specification

## Purpose
TBD - created by archiving change indice-calidad-harbor. Update Purpose after archive.

## Requirements

### Requirement: La nota de calidad incluye Harbor con un peso único
La nota publicada (`score_calidad`) SHALL ser `(1 − PESO_HARBOR_EN_CALIDAD) × examen + PESO_HARBOR_EN_CALIDAD × nota_harbor`, con el peso definido una sola vez en Python y publicado por el export. Ninguna superficie SHALL recalcularla.

#### Scenario: una superficie recalcula con otro peso
- **WHEN** `app.js` o un generador combina examen y Harbor por su cuenta
- **THEN** el guardrail da rojo

### Requirement: El margen incluye el ruido de Harbor
`calidad_ci95` SHALL combinar el error del examen y el bootstrap de los intentos de Harbor, y el grupo de cabeza SHALL calcularse sobre la nota y ese margen.

#### Scenario: un modelo que acierta los 3 intentos
- **WHEN** las 3 recompensas de una tarea son iguales
- **THEN** su error de Harbor no es cero (varianza encogida hacia la de la tarea)

### Requirement: Sin dato agéntico no rankea
Un modelo con `agentico.sin_dato` SHALL quedar `ranked: false` con motivo `sin_dato_agentico`, sin `score_calidad`, y fuera de todo orden por la nota y de todo grupo de cabeza.

#### Scenario: GPT-OSS en una tabla ordenada por la nota
- **WHEN** una superficie que ordena por la nota lista a GPT-OSS 120B
- **THEN** el guardrail da rojo

### Requirement: El grupo de cabeza se publica desde el export
El export SHALL publicar `grupo_cabeza` con `n`, `de`, `margen` y `mas_barato`; las superficies SHALL mostrar «≈» en el grupo, la línea con N y margen, y la etiqueta del más barato, leyendo esos campos.

#### Scenario: una cifra del grupo escrita a mano
- **WHEN** la línea del grupo dice un N distinto al del export
- **THEN** el guardrail da rojo
