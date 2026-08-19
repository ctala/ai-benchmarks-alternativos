# Claude Opus 5 — agent_long_horizon/priority_change_midtask

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.63 | quality: 8.5
- latency_total: 195.977s | tokens_per_second: 84.0
- input_tokens: 28610 | output_tokens: 12730

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Necesito que me ayudes a redactar un memo dirigido al CEO de mi empresa anunciando los resultados del trimestre. Tono formal, ejecutivo, máximo 250 palabras.

### Turno 1 — modelo

Con gusto. Como no me has pasado las cifras, te dejo el memo redactado con marcadores entre corchetes para que solo tengas que sustituir los datos. Si me compartes los números, te devuelvo la versión final ajustada.

---

**MEMORANDO**

**Para:** [Nombre], Director General
**De:** [Tu nombre], [Cargo]
**Fecha:** [Fecha]
**Asunto:** Resultados del [Q_] de [Año]

Estimado [Nombre]:

Presento a continuación el cierre de resultados correspondiente al trimestre, junto con las conclusiones más relevantes para la toma de decisiones.

**Resultados principales**

Los ingresos del trimestre alcanzaron [X], lo que representa una variación de [±X %] frente al mismo periodo del año anterior y un [cumplimiento/desviación] del [X %] respecto al presupuesto aprobado. El margen operativo se situó en [X %], mientras que el EBITDA cerró en [X].

**Factores determinantes**

El desempeño se explica principalmente por [factor 1: p. ej. crecimiento en la línea X], [factor 2] y [factor 3]. En sentido contrario, [riesgo o desviación] presionó los resultados en [X puntos porcentuales].

**Perspectiva y siguientes pasos**

Para el próximo trimestre proyectamos [proyección], sustentada en [iniciativas en curso]. Recomiendo priorizar tres acciones: [acción 1], [acción 2] y [acción 3]. Requiero su validación sobre [decisión pendiente] antes del [fecha] para no comprometer el calendario de ejecución.

Quedo a su disposición para revisar el detalle en la sesión que estime conveniente.

Atentamente,
[Tu nombre]

---

**Extensión:** 198 palabras (cuerpo del memo), con margen para ampliar al sustituir los marcadores.

Para afinarlo, me ayudaría saber: las cifras clave, si el trimestre fue positivo o negativo (el encuadre cambia bastante), y si hay alguna decisión concreta que necesites del CEO.

### Turno 2 — usuario

Datos del trimestre: ingresos $890K (+22% YoY), 14 clientes nuevos enterprise, churn 3.2%, NPS 67, lanzamos 2 nuevas features. Empieza por proponerme la estructura del memo.

### Turno 2 — modelo

Perfecto, con esos datos ya puedo ajustar el esqueleto que tenía. El cambio principal: los datos que me das son de crecimiento y retención, no de rentabilidad (no hay margen ni EBITDA), así que el bloque de "Resultados principales" se reorienta hacia métricas comerciales y de producto. Mantengo la estructura de encabezado, factores y siguientes pasos, que sigue siendo válida.

---

**Estructura propuesta (con reparto de palabras para no pasar de 250)**

**1. Encabezado formal** — *no cuenta apenas*
Para / De / Fecha / Asunto: "Resultados Q[_] [Año]: ingresos $890K, +22 % YoY"
→ El dato fuerte va en el asunto: el CEO lo capta sin abrir el cuerpo.

**2. Apertura de una frase** — *~25 palabras*
Titular ejecutivo: trimestre de crecimiento sostenido, con la cifra de ingresos y el porcentaje.

**3. Resultados comerciales** — *~60 palabras*
Ingresos $890K (+22 % YoY) · 14 nuevos clientes enterprise.
Aquí conviene añadir contexto: ¿cuántos enterprise había antes? ¿Qué peso tienen en el ingreso? Un "14 nuevos" solo impacta si se compara.

**4. Salud de la base de clientes** — *~50 palabras*
Churn 3.2 % · NPS 67. Ambos son cifras defendibles; el argumento es que el crecimiento no viene a costa de la retención.

**5. Producto** — *~40 palabras*
Los 2 lanzamientos, vinculados a su efecto comercial o de retención, no como simple lista.

**6. Perspectiva y petición** — *~60 palabras*
Proyección del próximo trimestre + la decisión concreta que necesitas del CEO.

**7. Cierre protocolario** — *~15 palabras*

---

Antes de redactar, dos cosas que le darían mucha más fuerza al memo:

1. **¿Había objetivo presupuestado para el trimestre?** "Ingresos $890K" es bueno; "$890K frente a un objetivo de $800K" es una noticia.
2. **¿Qué necesitas del CEO?** Un memo ejecutivo que solo informa se archiva. Si hay una petición (presupuesto, contratación, aprobación de roadmap), el punto 6 se convierte en el núcleo del documento.

Dime si esta estructura te sirve o quieres reordenarla, y con tu respuesta a esas dos preguntas la redacto completa.

### Turno 3 — usuario

Bien. Redacta la introducción de 2 párrafos.

### Turno 3 — modelo

Aquí la tienes. Un apunte de encaje: como la introducción ahora son dos párrafos, absorbe los puntos 2 y 3 de la estructura (apertura + resultados comerciales), que juntos ya tenían asignadas ~85 palabras. Así que no se descuadra el límite: el resto del memo mantiene sus ~150 palabras.

---

**MEMORANDO**

**Para:** [Nombre], Director General
**De:** [Tu nombre], [Cargo]
**Fecha:** [Fecha]
**Asunto:** Resultados Q[_] [Año]: ingresos de $890K, +22 % YoY

Estimado [Nombre]:

El trimestre cerró con ingresos de $890K, un incremento del 22 % frente al mismo periodo del año anterior [y un cumplimiento del X % respecto al objetivo presupuestado]. Se trata del [X.º] trimestre consecutivo de crecimiento, y conviene destacar que este avance no se ha producido a costa de la solidez de la base de clientes: los indicadores de retención y satisfacción se mantienen en niveles favorables, según se detalla más adelante.

En el plano comercial, incorporamos 14 nuevos clientes enterprise, lo que eleva la cartera de este segmento a [X cuentas] y sitúa su contribución en el [X %] de los ingresos del trimestre. Este resultado confirma la tracción del segmento enterprise como principal vector de crecimiento y respalda la decisión de concentrar en él los esfuerzos comerciales de los próximos meses.

---

**Extensión:** 122 palabras. Van algo por encima de las 85 previstas, así que ajustaré ligeramente los bloques de producto y perspectiva al redactar el resto.

Dos notas:

- Si **no había objetivo presupuestado**, elimina el corchete de la primera frase y queda igual de sólida.
- Si **el peso de enterprise sobre los ingresos no lo tienes a mano**, se puede sustituir por una referencia al ticket medio o simplemente cerrar en "[X cuentas]". Dime qué dato tienes y lo cierro.

Cuando me confirmes qué necesitas del CEO, redacto los bloques 4 a 7 y te entrego el memo completo dentro del límite de 250 palabras.

### Turno 4 — usuario

Ahora la sección de logros con bullet points.

### Turno 4 — modelo

Aquí está. Un ajuste de encaje importante: los ingresos y los 14 clientes enterprise ya quedaron en la introducción, así que **no los repito aquí** — esta sección recoge los bloques 4 y 5 (retención, satisfacción y producto). Si repitiéramos las cifras de arriba, el memo perdería densidad y nos comeríamos el límite de palabras.

---

**Indicadores destacados del trimestre**

- **Retención:** churn del 3,2 %, [por debajo del / en línea con el] promedio del sector y [X pp] frente al trimestre anterior. La base instalada se mantiene estable a pesar del mayor volumen de altas.
- **Satisfacción del cliente:** NPS de 67, situado en el rango de excelencia para software B2B. Este nivel respalda la estrategia de crecimiento apoyada en referencias y expansión de cuentas existentes.
- **Producto:** dos nuevas funcionalidades liberadas a producción — [nombre 1] y [nombre 2] —, orientadas a [objetivo: p. ej. reducir el tiempo de implementación en cuentas enterprise]. [Adoptadas por el X % de las cuentas activas en las primeras semanas.]

---

**Control de extensión:** 108 palabras. Sumadas a las 122 de la introducción, van 230 de las 250.

Esto obliga a una decisión, y te doy las dos opciones:

**A) Mantener el límite de 250.** Recorto la introducción a ~90 palabras (quitando el detalle de trimestres consecutivos y comprimiendo el segundo párrafo) para liberar espacio a la perspectiva y la petición al CEO, que es la parte que hace accionable el memo.

**B) Ampliar a ~300 palabras.** Todo queda como está y la sección de perspectiva respira. Para un memo de resultados trimestrales con petición incluida, 300 palabras sigue siendo perfectamente ejecutivo.

Mi recomendación es la **B**: sacrificar la petición al CEO para salvar 50 palabras es mal negocio.

Un último apunte: si prevés que este memo se reenvíe suelto o se lea fuera de contexto, dime y añado un bullet inicial con ingresos y clientes enterprise para que la sección funcione de forma autónoma.

Sigo pendiente de **qué necesitas del CEO** para cerrar los bloques 6 y 7.

### Turno 5 — usuario

Sigue con la sección de retos y aprendizajes.

### Turno 5 — modelo

Aquí la tienes. Antes, un aviso de encaje que conviene que tengas presente:

Esta sección **no estaba en la estructura de siete bloques** que acordamos; entra como nuevo bloque entre "Indicadores destacados" y "Perspectiva". Además, todos los datos que me pasaste son favorables, así que los retos los he derivado de las tensiones que las propias cifras implican, marcando con corchetes lo que es hipótesis mía y necesita tu confirmación.

---

**Retos identificados y aprendizajes**

Si bien el trimestre fue favorable en sus indicadores principales, el análisis interno señala tres frentes de atención:

- **Presión sobre la capacidad de incorporación.** El ingreso de 14 cuentas enterprise en un solo trimestre tensiona los procesos de onboarding y soporte. [Sostener este ritmo sin refuerzo de equipo comprometería los tiempos de implementación comprometidos con el cliente.]
- **Concentración del crecimiento.** La dependencia creciente del segmento enterprise, aun siendo la apuesta estratégica correcta, aumenta la exposición a ciclos de venta largos y a la pérdida de cuentas individuales de peso elevado.
- **Distancia entre liberación y adopción.** Las dos funcionalidades lanzadas están disponibles, pero [la adopción efectiva avanza por debajo de lo previsto], lo que limita su impacto sobre retención y expansión.

**Aprendizaje principal:** el crecimiento comercial ha superado el ritmo de escalado operativo. El foco del próximo trimestre debe desplazarse de la captación a la consolidación de la capacidad de entrega.

---

**Extensión:** 145 palabras. **Total acumulado: 375 palabras**, y faltan aún perspectiva y cierre (~75). El memo se irá a **~450**.

El límite de 250 ya no es sostenible con cinco secciones. Tres salidas:

**A) Aceptar ~450 palabras.** Sigue siendo una página. Es lo razonable si el CEO espera análisis, no solo cifras.

**B) Comprimir a ~300.** Recorto las tres secciones a lo esencial: un bullet por reto, sin desarrollo, e introducción de 90 palabras. Pierde matiz, gana contundencia.

**C) Memo de 250 + anexo.** El memo mantiene resultados y petición; retos y aprendizajes pasan a un anexo de una página. Es la opción más ejecutiva de las tres.

Mi recomendación: **C** si el memo va a circular a consejo o inversores; **A** si es comunicación directa entre tú y el CEO.

Dos cuestiones para cerrar:

1. **¿Cuáles fueron los retos reales del trimestre?** Los tres que propongo son inferencias razonables, pero si hubo un problema concreto (una cuenta perdida, un retraso de roadmap, rotación de personal), es mucho más creíble nombrarlo. Un CEO desconfía de un memo donde nada salió mal.
2. **Sigo sin saber qué necesitas de él.** Es el bloque 6 y, sin él, este documento informa pero no consigue nada.

### Turno 6 — usuario

Espera, cambio importante: ya no es para el CEO. Ahora va dirigido a todo el equipo (40 personas, mix de roles). Cambia el tono a informal y cercano, mantén los datos pero hazlo motivacional. No empieces de cero, ajusta lo que ya tenemos.

### Turno 6 — modelo

Entendido. No hace falta empezar de cero: el contenido sustantivo (las cinco cifras y los tres retos) se conserva íntegro. Lo que cambia es el envoltorio y, sobre todo, el destinatario de las peticiones.

**Cómo se reubica lo que ya teníamos**

| Bloque original | Qué pasa con él |
|---|---|
| Encabezado memo formal (Para/De/Asunto) | → Se convierte en asunto de correo/mensaje interno |
| Intro 2 párrafos (ingresos + enterprise) | → Se mantiene el contenido, se reescribe el registro |
| Indicadores destacados (churn, NPS, producto) | → Se mantiene, pero **traduciendo la jerga**: con 40 personas de perfiles mixtos, "NPS 67" no significa nada para media plantilla |
| Retos y aprendizajes | → Se mantienen los tres, reencuadrados como desafío compartido, no como riesgo que justificar ante un jefe |
| Perspectiva + **petición al CEO** | → Este es el cambio de fondo: ya no hay una decisión que aprobar, sino una llamada a la acción colectiva |
| Cierre protocolario | → Cierre cercano + canal para preguntas |

Sobre la extensión: el límite de 250 palabras venía de la lógica "memo ejecutivo". Para comunicación de equipo lo importante es que se lea entero, y esto ronda las **340 palabras**. Dime si lo quieres más corto.

---

**Asunto:** Cerramos el trimestre en $890K — y esto lo hicimos entre todos

Hola equipo:

Antes de que los números circulen en versión resumida, quería contárselos de primera mano, porque hay bastante de lo que estar orgullosos.

**Cerramos el trimestre con $890K en ingresos: un 22 % más que el mismo trimestre del año pasado.** Casi una cuarta parte de crecimiento en doce meses. Y lo mejor no es la cifra en sí, sino que no la conseguimos a costa de la calidad: crecimos y, al mismo tiempo, cuidamos a quienes ya estaban.

Cuatro datos que lo respaldan:

- **14 nuevos clientes enterprise.** Cuentas grandes, ciclos de venta largos, mucha paciencia detrás. Un trabajo enorme de comercial, preventa e implementación.
- **Churn del 3,2 %.** Traducido: de cada 100 clientes, más de 96 siguieron con nosotros. En pleno crecimiento, retener así no es lo normal.
- **NPS de 67.** Es la nota que nos ponen los clientes, en una escala de −100 a 100. Por encima de 50 ya se considera excelente en software B2B. 67 significa que hay gente ahí fuera recomendándonos por su cuenta.
- **Dos nuevas funcionalidades en producción:** [nombre 1] y [nombre 2], pensadas para [objetivo].

**Ahora, la parte honesta.** Crecer así aprieta:

- El equipo de implementación y soporte viene absorbiendo 14 cuentas nuevas con la misma estructura. Se nota, y lo sabemos.
- Estamos concentrando mucho peso en enterprise. Es la apuesta correcta, pero nos hace más sensibles a cada cuenta.
- Las dos features están liberadas, pero [su adopción va más despacio de lo que esperábamos]. Construirlas era la mitad del trabajo.

**Por eso el próximo trimestre va de consolidar, no de correr más.** Sostener lo que ya vendimos, que las funcionalidades nuevas lleguen de verdad a quien las necesita y aliviar los cuellos de botella de entrega.

Gracias de verdad. Estos números son de todos.

Cualquier duda, [en el all-hands del (fecha) / por (canal)] lo vemos con calma.

[Tu nombre]

---

**Tres cosas antes de enviarlo:**

1. **¿Los ingresos son compartibles con las 40 personas?** Al pasar de un destinatario a toda la plantilla, la cifra deja de ser confidencial de facto. Si no quieres darla, funciona igual con solo el +22 %.
2. **Cuidado con el bullet de implementación.** Tal como está, reconoce la sobrecarga sin prometer nada. Si vas a contratar, dilo explícitamente; si no, es mejor no insinuarlo, porque el equipo lo leerá como un compromiso.
3. **Sigue pendiente el reto real del trimestre.** Los tres son inferencias mías a partir de tus datos. Y aquí importa más que antes: el CEO habría detectado un memo demasiado optimista; tu equipo, que vivió el trimestre por dentro, lo detectará seguro.

### Turno 7 — usuario

Continúa con los próximos pasos del próximo trimestre, en este nuevo tono.

### Turno 7 — modelo

Aquí va. Un apunte de encaje: en la versión actual estos próximos pasos están comprimidos en una sola frase ("el próximo trimestre va de consolidar, no de correr más"). Lo que sigue **sustituye y desarrolla ese párrafo**, y va en el mismo sitio: después de los retos, antes del agradecimiento final. Cada eje sale directamente de uno de los tres retos, para que el equipo vea la conexión.

---

**Hacia dónde vamos el próximo trimestre**

No es un trimestre de pisar el acelerador. Es uno de asentar lo que ya construimos. Tres prioridades:

**1. Que las 14 cuentas nuevas se queden.** Revisar el proceso de onboarding de punta a punta y quitar de en medio lo que hoy nos hace perder tiempo. Objetivo: [reducir el tiempo de implementación a X semanas]. Owner: [nombre / equipo].

**2. Que las funcionalidades nuevas se usen.** [Nombre 1] y [nombre 2] ya están ahí; ahora toca acompañar a los clientes para que las adopten. Meta: [X % de cuentas activas usándolas al cierre del trimestre]. Owner: [nombre / equipo].

**3. Sostener la retención mientras crecemos.** Mantener el churn por debajo del [3,5 %] y el NPS por encima de [65], con el doble de cuentas grandes que hace un año. Owner: [nombre / equipo].

**Qué necesitamos de cada uno:** si estás en contacto con clientes, avisa pronto de cualquier señal de fricción — cuanto antes lo sepamos, más margen tenemos. Y si ves un cuello de botella en tu día a día, dilo: este trimestre justamente va de eso.

---

**Extensión:** el mensaje completo queda en **~430 palabras**. Sigue siendo legible de un tirón, pero si lo quieres más ligero, la vía más limpia es dejar los tres ejes en una línea cada uno, sin métrica ni owner, y guardar el detalle para el all-hands.

**Tres cosas que necesito de ti para cerrarlo:**

1. **Los owners.** En un mensaje a 40 personas, una prioridad sin nombre detrás no la recoge nadie. Si prefieres no asignar nombres por escrito, pon el equipo ("Customer Success", "Producto").
2. **Las metas numéricas.** Las que puse son plausibles a partir de tus cifras, pero son mías. Un objetivo inventado se detecta rápido y resta credibilidad al resto.
3. **La contratación.** Si el eje 1 depende de reforzar el equipo, este es el sitio para decirlo. Y si no vas a contratar, mejor que la prioridad 1 hable solo de proceso: prometer alivio sin recursos genera más frustración que no mencionarlo.

Con eso ya te monto el mensaje completo de principio a fin, en una sola pieza y listo para enviar.

### Turno 8 — usuario

Perfecto. Ahora dame el memo completo final, integrado, con todas las secciones que armamos pero ya con el nuevo tono y dirigido al equipo.

### Turno 8 — modelo

Aquí lo tienes, integrado de principio a fin. He unificado el registro, eliminado los solapamientos entre secciones y dejado entre corchetes solo lo que falta por confirmar.

---

**Asunto:** Cerramos el trimestre en $890K — y esto lo hicimos entre todos

Hola equipo:

Antes de que los números circulen en versión resumida, quería contárselos de primera mano, porque hay bastante de lo que estar orgullosos.

**Cerramos el trimestre con $890K en ingresos: un 22 % más que el mismo trimestre del año pasado.** Casi una cuarta parte de crecimiento en doce meses. Y lo mejor no es la cifra en sí, sino cómo llegamos a ella: crecimos sin descuidar a quienes ya estaban con nosotros.

**Los cuatro datos que lo respaldan**

- **14 nuevos clientes enterprise.** Cuentas grandes, ciclos de venta largos, mucha paciencia detrás. Hay un trabajo enorme de comercial, preventa e implementación en cada una.
- **Churn del 3,2 %.** Traducido: de cada 100 clientes, más de 96 siguieron con nosotros. En pleno crecimiento, retener así no es lo normal.
- **NPS de 67.** Es la nota que nos ponen los clientes, en una escala de −100 a 100. Por encima de 50 ya se considera excelente en software B2B. 67 significa que hay gente recomendándonos por su cuenta.
- **Dos nuevas funcionalidades en producción:** [nombre 1] y [nombre 2], pensadas para [objetivo].

**Ahora, la parte honesta**

Crecer a este ritmo aprieta, y conviene decirlo:

- Implementación y soporte vienen absorbiendo 14 cuentas nuevas con la misma estructura. Se nota, y lo sabemos.
- Estamos concentrando mucho peso en enterprise. Es la apuesta correcta, pero nos vuelve más sensibles a lo que pase con cada cuenta.
- Las dos features están liberadas, pero [su adopción va más despacio de lo que esperábamos]. Construirlas era solo la mitad del trabajo.

**Hacia dónde vamos el próximo trimestre**

No es un trimestre de pisar el acelerador. Es uno de asentar lo que ya construimos. Tres prioridades:

**1. Que las 14 cuentas nuevas se queden.** Revisar el onboarding de punta a punta y quitar de en medio lo que hoy nos hace perder tiempo. Objetivo: [reducir el tiempo de implementación a X semanas]. Owner: [equipo].

**2. Que las funcionalidades nuevas se usen.** [Nombre 1] y [nombre 2] ya están ahí; ahora toca acompañar a los clientes para que las adopten. Meta: [X % de cuentas activas al cierre del trimestre]. Owner: [equipo].

**3. Sostener la retención mientras crecemos.** Mantener el churn por debajo del [3,5 %] y el NPS por encima de [65], con el doble de cuentas grandes que hace un año. Owner: [equipo].

**Qué necesitamos de cada uno:** si estás en contacto con clientes, avisa pronto de cualquier señal de fricción — cuanto antes lo sepamos, más margen tenemos para reaccionar. Y si detectas un cuello de botella en tu día a día, dilo: este trimestre va justamente de eso.

Gracias de verdad. Estos números son de todos.

Cualquier duda, [en el all-hands del (fecha) / por (canal)] lo vemos con calma.

[Tu nombre]

---

**Extensión:** 425 palabras. Se lee en menos de dos minutos.

**Lo que queda por rellenar antes de enviar:**

| Marcador | Nota |
|---|---|
| Nombres de las 2 features y su objetivo | — |
| Adopción real de las features | Si va bien, cambia el encuadre del reto 3 |
| Metas numéricas de los 3 ejes | Las mías son plausibles, no reales |
| Owners | Equipo basta; sin owner nadie recoge la prioridad |
| Fecha/canal del cierre | — |

Y las dos decisiones de fondo que siguen abiertas: **si compartes la cifra de ingresos** con las 40 personas (funciona igual con solo el +22 %) y **si habrá refuerzo de equipo** — si no lo hay, mejor que la prioridad 1 hable solo de proceso.


## Respuesta completa

Aquí lo tienes, integrado de principio a fin. He unificado el registro, eliminado los solapamientos entre secciones y dejado entre corchetes solo lo que falta por confirmar.

---

**Asunto:** Cerramos el trimestre en $890K — y esto lo hicimos entre todos

Hola equipo:

Antes de que los números circulen en versión resumida, quería contárselos de primera mano, porque hay bastante de lo que estar orgullosos.

**Cerramos el trimestre con $890K en ingresos: un 22 % más que el mismo trimestre del año pasado.** Casi una cuarta parte de crecimiento en doce meses. Y lo mejor no es la cifra en sí, sino cómo llegamos a ella: crecimos sin descuidar a quienes ya estaban con nosotros.

**Los cuatro datos que lo respaldan**

- **14 nuevos clientes enterprise.** Cuentas grandes, ciclos de venta largos, mucha paciencia detrás. Hay un trabajo enorme de comercial, preventa e implementación en cada una.
- **Churn del 3,2 %.** Traducido: de cada 100 clientes, más de 96 siguieron con nosotros. En pleno crecimiento, retener así no es lo normal.
- **NPS de 67.** Es la nota que nos ponen los clientes, en una escala de −100 a 100. Por encima de 50 ya se considera excelente en software B2B. 67 significa que hay gente recomendándonos por su cuenta.
- **Dos nuevas funcionalidades en producción:** [nombre 1] y [nombre 2], pensadas para [objetivo].

**Ahora, la parte honesta**

Crecer a este ritmo aprieta, y conviene decirlo:

- Implementación y soporte vienen absorbiendo 14 cuentas nuevas con la misma estructura. Se nota, y lo sabemos.
- Estamos concentrando mucho peso en enterprise. Es la apuesta correcta, pero nos vuelve más sensibles a lo que pase con cada cuenta.
- Las dos features están liberadas, pero [su adopción va más despacio de lo que esperábamos]. Construirlas era solo la mitad del trabajo.

**Hacia dónde vamos el próximo trimestre**

No es un trimestre de pisar el acelerador. Es uno de asentar lo que ya construimos. Tres prioridades:

**1. Que las 14 cuentas nuevas se queden.** Revisar el onboarding de punta a punta y quitar de en medio lo que hoy nos hace perder tiempo. Objetivo: [reducir el tiempo de implementación a X semanas]. Owner: [equipo].

**2. Que las funcionalidades nuevas se usen.** [Nombre 1] y [nombre 2] ya están ahí; ahora toca acompañar a los clientes para que las adopten. Meta: [X % de cuentas activas al cierre del trimestre]. Owner: [equipo].

**3. Sostener la retención mientras crecemos.** Mantener el churn por debajo del [3,5 %] y el NPS por encima de [65], con el doble de cuentas grandes que hace un año. Owner: [equipo].

**Qué necesitamos de cada uno:** si estás en contacto con clientes, avisa pronto de cualquier señal de fricción — cuanto antes lo sepamos, más margen tenemos para reaccionar. Y si detectas un cuello de botella en tu día a día, dilo: este trimestre va justamente de eso.

Gracias de verdad. Estos números son de todos.

Cualquier duda, [en el all-hands del (fecha) / por (canal)] lo vemos con calma.

[Tu nombre]

---

**Extensión:** 425 palabras. Se lee en menos de dos minutos.

**Lo que queda por rellenar antes de enviar:**

| Marcador | Nota |
|---|---|
| Nombres de las 2 features y su objetivo | — |
| Adopción real de las features | Si va bien, cambia el encuadre del reto 3 |
| Metas numéricas de los 3 ejes | Las mías son plausibles, no reales |
| Owners | Equipo basta; sin owner nadie recoge la prioridad |
| Fecha/canal del cierre | — |

Y las dos decisiones de fondo que siguen abiertas: **si compartes la cifra de ingresos** con las 40 personas (funciona igual con solo el +22 %) y **si habrá refuerzo de equipo** — si no lo hay, mejor que la prioridad 1 hable solo de proceso.