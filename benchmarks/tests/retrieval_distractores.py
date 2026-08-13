"""
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
clientes. El directorio instruye a la gerencia a no otorgar nuevas condiciones de
crédito a clientes con deuda vencida superior a $8.000.000.

4. INVERSIÓN EN BODEGA
Se presenta la cotización para la ampliación de la bodega de San Bernardo por
$146.900.000, con un plazo de ejecución de 7 meses. La propuesta alternativa de
arriendo de un galpón en Lampa implica $4.350.000 mensuales por 36 meses.

El directorio acuerda postergar la decisión hasta la sesión de mayo, solicitando una
tercera cotización.

5. DOTACIÓN
Se aprueba la contratación de 3 vendedores para la zona sur, con un costo anual
estimado de $58.200.000 incluidas cargas sociales. La incorporación se hará efectiva
el 1 de junio de 2026.

6. VARIOS
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
    # ── 1. DISTRACTORES: varias cifras del mismo tipo, una sola correcta ──────
    _t("distractor_credito_utilizado",
       "Dos cifras de crédito (total y utilizado): hay que leer cuál pide",
       "¿Cuánto de la línea de crédito está efectivamente utilizado?",
       "41.200.000", ["95.000.000"],
       ["responde 41.200.000",
        "NO responde 95.000.000, que es el total de la línea, no lo utilizado"]),

    _t("distractor_umbral_vs_cartera",
       "Un umbral de política y un monto de cartera, ambos en la sección de morosidad",
       "¿Sobre qué monto de deuda vencida el directorio prohíbe dar nuevas condiciones de crédito?",
       "8.000.000", ["27.640.000"],
       ["responde 8.000.000 (el umbral de la instrucción)",
        "NO responde 27.640.000, que es el total de la cartera vencida"]),

    _t("distractor_inversion_vs_arriendo",
       "Dos alternativas de bodega con montos de escala muy distinta",
       "¿Cuánto cuesta la ampliación de la bodega de San Bernardo?",
       "146.900.000", ["4.350.000"],
       ["responde 146.900.000",
        "NO responde 4.350.000, que es el arriendo mensual de la alternativa en Lampa"]),

    _t("distractor_resultado_vs_ingresos",
       "Cuatro cifras en la misma sección financiera",
       "¿Cuál fue el resultado operacional del período?",
       "38.450.000", ["184.320.000", "112.870.000"],
       ["responde 38.450.000",
        "NO responde 184.320.000 (ingresos) ni 112.870.000 (costo de ventas)"]),

    # ── 2. COMBINAR DOS DATOS SEPARADOS ──────────────────────────────────────
    # La respuesta NO está escrita en el acta: hay que calcularla. El distractor es
    # el operando suelto, que es lo que responde quien busca en vez de razonar.
    _t("combinar_costo_total_arriendo",
       "Requiere multiplicar dos datos del mismo párrafo",
       "Si se optara por el galpón de Lampa, ¿cuánto se pagaría en total durante los 36 meses?",
       "156.600.000", [],
       ["calcula 4.350.000 × 36 = 156.600.000",
        "no confunde el total con la cuota mensual"]),

    _t("combinar_credito_disponible",
       "Requiere restar dos cifras que están en párrafos distintos",
       "¿Cuánto crédito le queda disponible a la empresa?",
       "53.800.000", [],
       ["calcula 95.000.000 − 41.200.000 = 53.800.000",
        "identifica que hay que restar lo utilizado del total"]),

    _t("combinar_margen_bruto",
       "Requiere restar ingresos menos costo de ventas, que están en la misma frase pero no calculados",
       "¿Cuál fue el margen bruto del bimestre (ingresos menos costo de ventas)?",
       "71.450.000", ["38.450.000"],
       ["calcula 184.320.000 − 112.870.000 = 71.450.000",
        "NO responde 38.450.000, que es el resultado operacional (ya lleva gastos descontados)"]),

    # ── 3. AUSENCIA: la respuesta correcta es "no está" ──────────────────────
    # Acá NO se usa `exact_vs_distractor` porque no hay cifra correcta que buscar:
    # lo que se mide es que NO afirme una. `must_not_assert` es el scorer que ya
    # distingue mencionar una cifra de afirmarla — un modelo que responde bien va a
    # nombrar el resultado operacional para aclarar que es OTRA cosa.
    {
        "name": "ausencia_utilidad_neta",
        "description": "Pide un dato que el acta no contiene; se puede confundir con el resultado operacional",
        "messages": [
            {"role": "system", "content": "Respondes preguntas sobre documentos. Si el dato no está en el documento, dilo explícitamente en vez de estimarlo."},
            {"role": "user", "content": f"{ACTA}\n\n---\n\nPregunta: ¿Cuál fue la utilidad neta después de impuestos?"},
        ],
        "expected_answer": {
            "type": "must_not_assert",
            "claim": "una cifra de utilidad neta después de impuestos",
            "note": "El acta no reporta utilidad neta. Afirmar cualquier cifra como tal es el fallo; el resultado operacional ($38.450.000) es otra cosa y confundirlos es el error típico.",
        },
        "rubrica": [
            "dice explícitamente que el dato no está en el acta",
            "NO afirma 38.450.000 como utilidad neta (es el resultado operacional)",
            "no estima ni inventa una cifra",
        ],
    },
]
