## Purpose

Define cómo el benchmark recomienda un modelo a un emprendedor hispanohablante por ocasión de uso, apoyado en benchmarks públicos verificados por la comunidad y enriquecido con la capa propia.

## ADDED Requirements

### Requirement: Seis ocasiones con volumen declarado
La recomendación MUST organizarse en seis ocasiones (Escribir, Relación comercial, Automatizar, Decidir con documentos, Programar, Local). Cada ocasión MUST tener un volumen mensual por defecto y la calculadora MUST permitir cambiarlo; el precio mensual MUST calcularse al volumen declarado.

#### Scenario: El usuario cambia el volumen
- **WHEN** el usuario edita el volumen de una ocasión en la calculadora
- **THEN** el precio mensual de cada modelo se recalcula con ese volumen y el orden de la recomendación puede cambiar

### Requirement: Fuente comunitaria como banda informativa
Una fuente externa es banda informativa y MUST NOT filtrar qué modelos se recomiendan. MUST entrar solo si cumple los cinco criterios de `FUENTES-EXTERNAS.md` (verificada por la comunidad con trayectorias públicas, verdad objetiva, datos por modelo leíbles por script con licencia para republicar, cobertura de modelos que un emprendedor paga o corre, y mapeo a una ocasión). Toda cifra externa MUST viajar con fuente, versión, fecha y licencia, y MUST mostrarse como banda. Cifras de harnesses distintos MUST NOT promediarse entre sí ni con las propias. La banda MUST mostrarse solo si la fuente midió la misma versión exacta del modelo que está en el índice.

#### Scenario: Versión distinta
- **WHEN** la fuente midió otra versión o variante del modelo (otro snapshot, otra cuantización, otro modo)
- **THEN** la cifra no se muestra en ese modelo

#### Scenario: Cifra externa en models.json
- **WHEN** `fuentes_externas.py` ingesta una fila de una fuente aceptada
- **THEN** la cifra se guarda bajo `externos` con fuente, versión, fecha y licencia, y `quality_avg` no cambia

#### Scenario: Fuente que no cumple el criterio
- **WHEN** una fuente mide por juez LLM o por votos, o acepta cifras autodeclaradas sin trayectorias
- **THEN** no se ingesta; como mucho se enlaza o se muestra como banda de preferencia rotulada

### Requirement: Conjunto base y marca «sin dato comunitario»
El conjunto base MUST ser la intersección entre los modelos vigentes del índice y los que se pueden llamar por OpenRouter, contada desde `models.py`, y MUST publicarse como número y lista. Las fuentes externas MUST NOT recortarlo. Todo modelo sin banda externa de su misma versión MUST llevar `sin_dato_comunitario: true`, y la calculadora MUST mostrarlo como estado normal, sin alarma.

#### Scenario: Modelo sin fuente
- **WHEN** un modelo rankeado no aparece en ninguna fuente aceptada
- **THEN** se publica con la capa propia y la marca visible «sin dato comunitario», sin banda externa

### Requirement: Medir con el harness oficial lo que nadie midió
Un modelo sin dato comunitario que importe a un founder MUST medirse con el harness oficial de la fuente correspondiente, con la versión fijada y el mínimo de intentos que esa fuente exige, por un camino declarado en `check_caminos.py`. La publicación MUST decir «medido por nosotros con el harness oficial vX, N intentos, fecha» y MUST NOT presentarse como cifra oficial de la fuente.

#### Scenario: Corrida propia de Terminal-Bench
- **WHEN** se corre Qwen 3.8 Flash y Ornith 1.5 con el harness oficial
- **THEN** quedan `result.json` por intento y `metadata.yaml`, la cifra se publica como corrida independiente con su etiqueta, y la referencia desde Hugging Face apunta al benchmark

### Requirement: La capa propia es la única medición donde no hay fuente
Para Escribir, Decidir con documentos y la seguridad en español, donde no existe fuente comunitaria, la recomendación MUST apoyarse solo en la capa propia y MUST decirlo.

#### Scenario: Ocasión sin fuente
- **WHEN** el usuario elige Escribir
- **THEN** la página declara que no hay fuente comunitaria para esa ocasión y muestra solo la medición propia
