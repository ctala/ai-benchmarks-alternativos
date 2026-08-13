"""
⛔ SUITE DESCARTADA (13-ago-2026) — NO está registrada en el runner.

Se midió en los 82 rankeados y salió **saturada: 76% de respuestas perfectas**, el mismo
problema que las cinco suites que se acababan de jubilar por eso. Se endureció —
distractores que compiten por la misma pregunta, combinaciones de más de un paso, tests
de ausencia— y bajó solo a **70%**. No alcanza.

**La conclusión no es que los tests estén mal escritos: es que la tarea ya no discrimina.**
Extraer un dato de un documento de contexto moderado es un problema resuelto para los
modelos actuales. Los distractores agregan fricción, no dificultad. Para que separe hace
falta contexto largo — que es justo lo que `niah_es` cubre en 128K+, donde todavía hay
señal (46% de perfectos en 256K).

El archivo se conserva porque el intento dejó tres cosas útiles:
  · el scorer `exact_vs_distractor` (acertar SIN nombrar la cifra rival), que sirve a otras suites;
  · dos bugs reales encontrados — el gate del verificador solo miraba tests `reasoning`, y
    los distractores castigaban a los modelos por mostrar el cálculo;
  · la regla que salió de acá: **una suite se valida en ~8 modelos repartidos por el rango,
    nunca en dos** (RUNBOOK Regla 0.7 · `validate_suite.py`).

Si alguna vez se retoma: el camino no es más distractores, es documentos largos.

---

Retrieval con distractores — lo que `niah_es` dejó de medir.

POR QUÉ EXISTE (13-ago-2026)
----------------------------
`niah_es` mide **un** needle distintivo en un pajar. Medido sobre 4.480 runs, eso ya no
distingue: 78% de respuestas perfectas en 8K, 75% en 64K. Los tramos cortos se recortaron
de la grilla por esa razón — no informaban y eran la mitad de la suite más cara del examen.

Pero el recorte deja un hueco: **retrieval a contexto moderado sigue siendo lo que hace un
agente todo el día** (leer una conversación, un documento de proceso, un hilo de correo).
Lo que ya no cuesta es *encontrar* un dato único y llamativo. Lo que sí cuesta, y es donde
fallan de verdad, son tres cosas:

1. **Distractores plausibles** — cuatro cifras del mismo tipo en el documento y solo una
   responde la pregunta. El modelo tiene que leer la condición, no hacer *pattern matching*
   sobre el formato.
2. **Combinar dos datos separados** — la respuesta no está escrita en ningún lado; hay que
   juntar dos hechos que viven en párrafos distintos.
3. **Ausencia** — la respuesta NO está en el documento. Decir "no está" es la respuesta
   correcta, y es la que más se alucina.

DECISIÓN DE DISEÑO: la dificultad viene de los distractores, no del largo. Un documento de
~3.000 tokens con cuatro cifras confundibles discrimina más que un needle único en 128.000
tokens, y cuesta **40× menos**. `niah_es` sigue cubriendo el eje de contexto largo puro en
128K+, que es donde todavía tiene señal (46% de perfectos en 256K).

Scoring `verificable`: la respuesta es un dato exacto o un "no está". Sin juez — verdad
objetiva por sobre juez LLM, adoptado de LiveBench.

⚠️ Los prompts NO se editan una vez medidos (`prompt_sha` lo detecta). Para medir algo
nuevo se agrega un test. (PLAN-ESTABILIDAD.md R2.)
"""

# Documento base: un acta de directorio de pyme, con cifras deliberadamente
# confundibles. Todas son montos en pesos, todas tienen formato parecido, y varias
# corresponden a conceptos distintos. Ese es el punto.
ACTA = """ACTA DE SESIÓN ORDINARIA N.º 47 — COMERCIALIZADORA DEL VALLE SpA
Fecha: 14 de marzo de 2026. Asistentes: 4 de 5 directores.

1. APROBACIÓN DEL ACTA ANTERIOR
Se aprueba sin observaciones el acta de la sesión N.º 46.

2. ESTADO FINANCIERO AL CIERRE DE FEBRERO
La gerencia informa ingresos por $184.320.000 en el bimestre, con un costo de ventas
de $112.870.000. El resultado operacional del período asciende a $38.450.000 una vez
descontados los gastos de administración, que totalizaron $33.000.000.

Se deja constancia de que la línea de crédito vigente con Banco Consorcio es de
$95.000.000, de los cuales se encuentran utilizados $41.200.000 al cierre.

3. MOROSIDAD
La cartera vencida a más de 90 días alcanza los $27.640.000, concentrada en tres
clientes. Considerando también los tramos de 30 y 60 días, la cartera vencida total
llega a $34.910.000. El directorio instruye a la gerencia a no otorgar nuevas
condiciones de crédito a clientes con deuda vencida superior a $8.000.000, umbral que
sube a $12.000.000 para clientes con más de cinco años de relación.

4. INVERSIÓN EN BODEGA
Se presenta la cotización para la ampliación de la bodega de San Bernardo por
$146.900.000, con un plazo de ejecución de 7 meses. La propuesta alternativa de
arriendo de un galpón en Lampa implica $4.350.000 mensuales por 36 meses.

El directorio acuerda postergar la decisión hasta la sesión de mayo, solicitando una
tercera cotización.

5. DOTACIÓN
Se aprueba la contratación de 3 vendedores para la zona sur, con un costo anual
estimado de $58.200.000 incluidas cargas sociales; sin cargas sociales el costo anual
sería de $46.560.000. La incorporación se hará efectiva el 1 de junio de 2026, por lo
que en el ejercicio 2026 solo se devengan siete meses.

6. ARRIENDO ACTUAL
La bodega que hoy se ocupa en Quilicura tiene un arriendo de $3.100.000 mensuales,
con reajuste anual por IPC. El contrato vence en marzo de 2027.

7. VARIOS
Se fija la próxima sesión ordinaria para el 16 de mayo de 2026.
"""


def _t(name, desc, pregunta, correcto, distractores, rubrica):
    """Test de dato exacto con distractores. `expected_answer` usa el scorer
    `exact_vs_distractor`: premia acertar SIN nombrar la cifra confundible, porque
    medir solo presencia premiaría al modelo que escupe todas las cifras del acta."""
    return {
        "name": name,
        "description": desc,
        "messages": [
            {"role": "system", "content": "Respondes preguntas sobre documentos. Si el dato no está en el documento, dilo explícitamente en vez de estimarlo."},
            {"role": "user", "content": f"{ACTA}\n\n---\n\nPregunta: {pregunta}"},
        ],
        "expected_answer": {
            "type": "exact_vs_distractor",
            "correcto": correcto,
            "distractores": distractores,
        },
        "rubrica": rubrica,   # documentación, no la consume el scorer
    }


TESTS = [
    # ── 1. DISTRACTORES QUE COMPITEN POR LA MISMA PREGUNTA ───────────────────
    # Lección del primer lote (13-ago): de 8 tests, 6 salieron 88-99% perfectos y
    # solo `distractor_credito_utilizado` discriminó (37%). La diferencia: su
    # distractor —el total de la línea— es una respuesta **plausible a la misma
    # pregunta**, no otro número cualquiera del documento. Un distractor que se
    # distingue por escala o por contexto no distrae a nadie.
    _t("distractor_credito_utilizado",
       "Total de línea vs monto utilizado: ambos responden '¿cuánto crédito?'",
       "¿Cuánto de la línea de crédito está efectivamente utilizado?",
       "41.200.000", ["95.000.000", "53.800.000"],
       ["responde 41.200.000",
        "NO responde 95.000.000 (total) ni 53.800.000 (disponible)"]),

    _t("distractor_mora_90_vs_total",
       "Dos cifras de cartera vencida: a 90 días y total. La pregunta especifica el tramo",
       "¿A cuánto asciende la cartera vencida a más de 90 días?",
       "27.640.000", ["34.910.000"],
       ["responde 27.640.000, el tramo >90 días",
        "NO responde 34.910.000, que es la cartera vencida TOTAL"]),

    _t("distractor_umbral_por_antiguedad",
       "Dos umbrales de crédito: general y para clientes antiguos. La pregunta pide el general",
       "¿Sobre qué monto de deuda vencida se prohíbe dar nuevas condiciones de crédito a un cliente nuevo?",
       "8.000.000", ["12.000.000"],
       ["responde 8.000.000, el umbral general",
        "NO responde 12.000.000, que aplica solo a clientes con más de cinco años"]),

    _t("distractor_dotacion_con_cargas",
       "Costo anual con y sin cargas sociales, misma frase. La pregunta no aclara: la cifra por defecto del acta es CON cargas",
       "¿Cuál es el costo anual estimado de los 3 vendedores nuevos, incluidas las cargas sociales?",
       "58.200.000", ["46.560.000"],
       ["responde 58.200.000",
        "NO responde 46.560.000, que es sin cargas sociales"]),

    _t("distractor_arriendo_actual_vs_alternativo",
       "Dos arriendos mensuales en el mismo documento: el vigente y el propuesto",
       "¿Cuánto se paga hoy de arriendo mensual por la bodega?",
       "3.100.000", ["4.350.000"],
       ["responde 3.100.000 (Quilicura, el actual)",
        "NO responde 4.350.000, que es la alternativa de Lampa que aún no se aprueba"]),

    # ── 2. COMBINAR — ahora con más de un paso y una trampa de proporción ────
    _t("combinar_sobrecosto_mudanza",
       "Requiere restar dos arriendos y multiplicar: el ahorro/sobrecosto mensual × 36",
       "Si se mudaran a Lampa, ¿cuánto MÁS pagarían de arriendo en total durante los 36 meses del contrato?",
       # OJO: 1.250.000 (la diferencia mensual) NO va como distractor. Es un paso
       # intermedio legítimo: un modelo que muestra el cálculo lo nombra, y
       # penalizarlo sería castigar el razonamiento correcto. Solo van RESPUESTAS
       # FINALES equivocadas. (Detectado el 13-ago al ver 6,0 en los 4 tests de
       # combinación: acertaban y perdían puntos por mostrar el trabajo.)
       "45.000.000", ["156.600.000"],
       ["calcula (4.350.000 − 3.100.000) × 36 = 45.000.000",
        "NO responde 156.600.000, que es el costo total de Lampa sin descontar lo que ya se paga"]),

    _t("combinar_dotacion_prorrateada",
       "Requiere prorratear el costo anual por los meses que efectivamente se devengan en 2026",
       "¿Cuánto costarán los 3 vendedores nuevos en el ejercicio 2026, considerando que entran el 1 de junio?",
       "33.950.000", [],   # 58.200.000 es el dato de partida: nombrarlo es correcto
       ["prorratea 58.200.000 × 7/12 = 33.950.000",
        "NO responde 58.200.000, que es el año completo"]),

    _t("combinar_margen_bruto",
       "Ingresos menos costo de ventas: están en la misma frase pero sin calcular",
       "¿Cuál fue el margen bruto del bimestre (ingresos menos costo de ventas)?",
       "71.450.000", ["38.450.000"],   # 184.320.000 es operando, no respuesta rival
       ["calcula 184.320.000 − 112.870.000 = 71.450.000",
        "NO responde 38.450.000, que es el resultado operacional (ya lleva gastos)"]),

    # ── 3. AUSENCIA — la respuesta correcta es "no está" ─────────────────────
    # Va con `must_not_assert`, que usa el verificador semántico: un modelo que
    # responde BIEN también va a mencionar el resultado operacional, para aclarar
    # que es otra cosa. Un regex castigaría al que acertó.
    #
    # ⚠️ En el primer lote este test devolvió 5,00 EXACTO en los 82 modelos — un
    # empate perfecto, o sea el valor de fallback. La causa: el scorer espera la
    # clave `must_not_assert` y estaba escrita como `claim`. No medía nada.
    {
        "name": "ausencia_utilidad_neta",
        "description": "Pide un dato que el acta no contiene y que se confunde fácil con el resultado operacional",
        "messages": [
            {"role": "system", "content": "Respondes preguntas sobre documentos. Si el dato no está en el documento, dilo explícitamente en vez de estimarlo."},
            {"role": "user", "content": f"{ACTA}\n\n---\n\nPregunta: ¿Cuál fue la utilidad neta después de impuestos del bimestre?"},
        ],
        "expected_answer": {
            "type": "must_not_assert",
            "must_not_assert": [
                "que la utilidad neta después de impuestos del bimestre fue $38.450.000",
                "que el acta reporta una cifra de utilidad neta después de impuestos",
            ],
        },
        "rubrica": [
            "dice que el acta no reporta utilidad neta",
            "puede mencionar el resultado operacional para aclarar que es OTRA cosa — eso no penaliza",
            "lo que penaliza es AFIRMAR una utilidad neta",
        ],
    },
    {
        "name": "ausencia_ipc_reajuste",
        "description": "El acta menciona reajuste por IPC pero no da el porcentaje: no debe inventarlo",
        "messages": [
            {"role": "system", "content": "Respondes preguntas sobre documentos. Si el dato no está en el documento, dilo explícitamente en vez de estimarlo."},
            {"role": "user", "content": f"{ACTA}\n\n---\n\nPregunta: ¿En qué porcentaje se reajusta anualmente el arriendo de la bodega actual?"},
        ],
        "expected_answer": {
            "type": "must_not_assert",
            "must_not_assert": [
                "que el acta especifica un porcentaje concreto de reajuste anual del arriendo",
            ],
        },
        "rubrica": [
            "dice que el acta indica reajuste por IPC pero no da el porcentaje",
            "NO inventa una cifra de inflación",
        ],
    },
]
