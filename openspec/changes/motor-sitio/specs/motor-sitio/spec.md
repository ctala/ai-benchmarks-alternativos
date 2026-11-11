## ADDED Requirements

### Requirement: Cada URL del sitio está declarada en el registro
El sitio SHALL tener una sola declaración de sus URLs (`registro_paginas.py`). Cada entrada lleva tipo, familias u ocasión, motor, y, si corresponde, congelada (fecha y motivo) o redirect.

#### Scenario: Una página compilada sin entrada
- **WHEN** `dist` contiene un `index.html` que no está en el registro
- **THEN** el build falla (R4)

#### Scenario: Una URL publicada que desaparece
- **WHEN** una URL de `docs/sitemap.xml` o de `docs/` no existe en `dist` ni como página ni como redirect
- **THEN** el build falla (R3)

### Requirement: Ninguna página muestra en silencio un modelo fuera del ranking vigente
Una página SHALL mostrar modelos con `ranked` falso solo si está congelada, con fecha y motivo.

#### Scenario: Comparación que muestra un modelo reemplazado
- **WHEN** una página no congelada muestra un modelo con `ranked` falso
- **THEN** el build falla (R1)

#### Scenario: Comparación por familia con versiones fuera del ranking
- **WHEN** una familia tiene modelos con `ranked` falso
- **THEN** la tabla lleva solo los rankeados y el pie enlaza a las fichas de los demás («Versiones anteriores →»)

#### Scenario: Un modelo fuera del ranking sin motivo
- **WHEN** un modelo tiene `ranked` falso y su elegibilidad no registra motivo
- **THEN** el export no publica y `check_registro` falla (R5)

#### Scenario: Página congelada
- **WHEN** la página está congelada con fecha y motivo
- **THEN** compila y muestra arriba el aviso con la fecha, el motivo y el enlace a lo vigente

### Requirement: Ninguna cifra escrita a mano
Toda cifra visible del HTML compilado SHALL venir de un componente que la toma de los datos y la marca con `data-cifra`.

#### Scenario: Cifra en una plantilla
- **WHEN** una plantilla escribe una cifra literal en texto visible
- **THEN** el build falla (R2)

### Requirement: Colores solo desde los tokens
Los estilos del sitio SHALL usar solo los tokens generados desde `brand.json`, con el tema claro y el nivel Cercano.

#### Scenario: Un hex fuera de los tokens
- **WHEN** un archivo de `sitio/src` distinto de `tokens.css` contiene un color hex
- **THEN** `check_paleta` falla

### Requirement: Publicación sin corte y con reversa
El corte SHALL ser un solo commit que compila hacia `docs/`, después de la paridad en verde y del OK de Cristian. La configuración de Pages no cambia.

#### Scenario: Paridad antes del corte
- **WHEN** una página migrada publica un contrato distinto del de su versión de Python sin una diferencia declarada
- **THEN** la paridad falla y no hay corte
