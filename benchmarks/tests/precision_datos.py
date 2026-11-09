"""
Suite `precision_datos`: reproducir y transformar datos de negocio SIN alterarlos.

POR QUÉ EXISTE (9-nov-2026, tarea 5.5 del change corte-v5-1)
-----------------------------------------------------------
`string_precision` salió del índice en 5.0.0 (DECISIONES, 7-nov-2026, variante B) por dos
motivos que se tapaban entre sí:

1. **Saturada.** 65 de 78 modelos copiaban las seis cadenas y hubo un solo error de copia
   real. No separaba a nadie por precisión.
2. **Sus cadenas parecen secretos** (hex largos, `sk-proj-…`, un JWT). Lo que sí separaba
   a los modelos era su POLÍTICA ante algo que parece una credencial: Claude Fable 5.1 se
   negaba a las seis. Eso es una conducta, no una imprecisión; hoy se publica aparte como
   el rasgo «¿maneja credenciales?».

Esta suite es NUEVA y aditiva (las suites se agregan, no se editan): mide la misma
capacidad —no cambiar un carácter— sobre datos que un emprendedor de LATAM mueve todos
los días y donde un carácter cambiado cuesta plata: RUT, CUIT, NIT, RFC, IBAN y CLABE
ficticios con dígito verificador válido, montos que cambian de formato regional sin
cambiar de valor, SKU con caracteres confundibles (0/O, 1/l/I, rn/m), nombres con tildes
y eñes, direcciones con números parecidos, fechas mezcladas a ISO, una línea del medio de
una lista larga y la suma de una columna en formato es-CL.

Nada acá parece una credencial: no hay cadenas hex ni base64 largas, ni palabras que
disparen una negativa por seguridad. Si un modelo se niega en esta suite, es un falso
positivo suyo, no prudencia.

Dificultad: dos tests de ancla fáciles (copiar RUT, normalizar formato de RUT) y el resto
con trampa: el dígito verificador que el modelo tiende a «corregir», el separador regional
ambiguo (`1,234` de un sistema de EE.UU. son mil doscientos treinta y cuatro), la letra O en una homoclave,
la línea 37 entre dos «Bolso camel», la dirección vieja al lado de la nueva.

Verificación: `precision_items` (en `benchmarks/scoring_precision_datos.py`), comparación
exacta por ítem con crédito parcial. Ver ese módulo para el porqué.

Datos: todos FICTICIOS. Los dígitos verificadores se calculan con las funciones de abajo y
`_verificar_fixtures()` los comprueba (lo corre el test unitario de la suite); los
dos RUT con DV inválido del test `rut_dv_no_corregir` son inválidos a propósito.

Regla 0.7 del RUNBOOK: antes del examen completo se valida en ~8 modelos con
`validate_suite.py`; se descarta o endurece si ≥ 60 % de las respuestas son perfectas.
"""

from __future__ import annotations

# ═══════════════════════════════════════════════════════════════════════════
# Dígitos verificadores — con estas funciones se generaron los fixtures
# ═══════════════════════════════════════════════════════════════════════════

def dv_rut(numero: int) -> str:
    """RUT chileno: módulo 11 con pesos 2..7 desde la derecha; 11→0, 10→K."""
    s, m = 0, 2
    for d in reversed(str(numero)):
        s += int(d) * m
        m = 2 if m == 7 else m + 1
    r = 11 - s % 11
    return {11: "0", 10: "K"}.get(r, str(r))


def dv_cuit(base10: str) -> int | None:
    """CUIT argentino: pesos 5432765432 sobre los 10 primeros dígitos; 11→0, 10→inválido."""
    s = sum(int(a) * b for a, b in zip(base10, [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]))
    r = 11 - s % 11
    return {11: 0, 10: None}.get(r, r)


def dv_nit(base: str) -> int:
    """NIT colombiano (DIAN): pesos 3,7,13,17,19,23,29,37,41 desde la derecha."""
    pesos = [3, 7, 13, 17, 19, 23, 29, 37, 41]
    r = sum(int(d) * pesos[i] for i, d in enumerate(reversed(base))) % 11
    return r if r in (0, 1) else 11 - r


_RFC_VAL = {**{str(i): i for i in range(10)},
            **{c: 10 + i for i, c in enumerate("ABCDEFGHIJKLMN")}, "&": 24,
            **{c: 25 + i for i, c in enumerate("OPQRSTUVWXYZ")}, " ": 37, "Ñ": 38}


def dv_rfc(rfc12: str) -> str:
    """RFC mexicano (SAT): dígito 13 sobre los 12 primeros caracteres; 10→A."""
    s = rfc12 if len(rfc12) == 12 else " " + rfc12
    r = sum(_RFC_VAL[c] * (13 - i) for i, c in enumerate(s)) % 11
    return "0" if r == 0 else ("A" if 11 - r == 10 else str(11 - r))


def dv_clabe(d17: str) -> int:
    """CLABE mexicana: pesos 3,7,1 (cada producto módulo 10)."""
    s = sum((int(d) * [3, 7, 1][i % 3]) % 10 for i, d in enumerate(d17))
    return (10 - s % 10) % 10


def iban_valido(iban: str) -> bool:
    """IBAN: mover los 4 primeros al final, letras a números, módulo 97 == 1."""
    i = iban.replace(" ", "")
    r = i[4:] + i[:4]
    return int("".join(str(int(c, 36)) for c in r)) % 97 == 1


def _clp(n: int) -> str:
    return ("-" if n < 0 else "") + "$" + f"{abs(n):,}".replace(",", ".")


# ═══════════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════════

SYSTEM = (
    "Trabajas en el área de operaciones de una pyme. Tu respuesta se pega directo en una "
    "planilla, así que respondes SOLO con los datos pedidos, uno por línea y en el orden "
    "pedido. Sin numeración, sin viñetas, sin comillas, sin encabezados y sin explicación."
)


def _test(name: str, description: str, user: str, items: list) -> dict:
    return {
        "name": name,
        "description": description,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        "expected_answer": {"type": "precision_items", "items": items},
    }


# Lista de 60 líneas de catálogo para `catalogo_linea_37_de_60` (generada con semilla
# 20261109; las líneas 36 y 37 son las dos «Bolso camel»).
CATALOGO_60 = [
    "MOC-0O1l-T11 | Mochila camel | $39.990",
    "BIL-I1l0-T02 | Billetera gris humo | $19.990",
    "BOL-rn0O-T11 | Bolso burdeos | $34.990",
    "MOC-I1l0-T10 | Mochila burdeos | $29.990",
    "BIL-Ol0I-T02 | Billetera café | $49.990",
    "MOC-1lI0-T10 | Mochila gris humo | $29.990",
    "MOC-m0O1-T10 | Mochila gris humo | $44.990",
    "MOC-0rnl-T02 | Mochila burdeos | $34.990",
    "BOL-0O1l-T02 | Bolso negro | $34.990",
    "BIL-m0O1-T02 | Billetera camel | $39.990",
    "CIN-OI01-T11 | Cinturón gris humo | $49.990",
    "BOL-0rnl-TO1 | Bolso café | $29.990",
    "MOC-0O1l-T01 | Mochila café | $34.990",
    "BOL-0O1l-T11 | Bolso café | $29.990",
    "BIL-O0lI-T02 | Billetera azul marino | $19.990",
    "BIL-Ol0I-T10 | Billetera verde oliva | $49.990",
    "CIN-m0O1-T10 | Cinturón azul marino | $34.990",
    "BIL-1lI0-T10 | Billetera negro | $19.990",
    "CIN-I1l0-T10 | Cinturón burdeos | $39.990",
    "MOC-I1l0-T11 | Mochila café | $49.990",
    "BIL-rn0O-T11 | Billetera arena | $19.990",
    "BOL-Ol0I-T02 | Bolso burdeos | $24.990",
    "BIL-lm1O-TO1 | Billetera arena | $29.990",
    "BIL-lm1O-T10 | Billetera burdeos | $44.990",
    "BIL-rn0O-TO1 | Billetera verde oliva | $34.990",
    "MOC-rn0O-T11 | Mochila gris humo | $49.990",
    "BOL-OI01-T10 | Bolso gris humo | $59.990",
    "BIL-m0O1-T01 | Billetera burdeos | $59.990",
    "MOC-0O1l-T02 | Mochila gris humo | $34.990",
    "BIL-0O1l-T11 | Billetera burdeos | $34.990",
    "BOL-m0O1-T01 | Bolso azul marino | $49.990",
    "BIL-0O1l-T10 | Billetera gris humo | $39.990",
    "MOC-1lI0-T02 | Mochila gris humo | $44.990",
    "BOL-lm1O-T01 | Bolso burdeos | $39.990",
    "CRT-OI01-T01 | Cartera camel | $59.990",
    "BOL-OI01-T01 | Bolso camel | $29.990",
    "BOL-O0lI-T11 | Bolso camel | $34.990",
    "MOC-lm1O-TO1 | Mochila negro | $59.990",
    "CIN-1lI0-T11 | Cinturón arena | $39.990",
    "BIL-0rnl-T02 | Billetera azul marino | $19.990",
    "BOL-1lI0-T10 | Bolso verde oliva | $44.990",
    "BOL-OI01-T02 | Bolso negro | $59.990",
    "BIL-Ol0I-T11 | Billetera verde oliva | $34.990",
    "CIN-Ol0I-T11 | Cinturón arena | $24.990",
    "CIN-Ol0I-TO1 | Cinturón negro | $49.990",
    "BOL-rn0O-TO1 | Bolso burdeos | $34.990",
    "CRT-1lI0-T02 | Cartera gris humo | $59.990",
    "CRT-1lI0-T10 | Cartera negro | $49.990",
    "MOC-OI01-T02 | Mochila burdeos | $34.990",
    "MOC-OI01-T01 | Mochila verde oliva | $24.990",
    "MOC-lm1O-T10 | Mochila negro | $19.990",
    "CRT-0O1l-T02 | Cartera burdeos | $49.990",
    "BOL-Ol0I-T10 | Bolso azul marino | $44.990",
    "CRT-1lI0-T01 | Cartera café | $44.990",
    "BOL-rn0O-T10 | Bolso verde oliva | $34.990",
    "CRT-OI01-T02 | Cartera burdeos | $19.990",
    "BIL-OI01-T10 | Billetera negro | $59.990",
    "MOC-lm1O-T02 | Mochila burdeos | $19.990",
    "BIL-Ol0I-T01 | Billetera verde oliva | $29.990",
    "BIL-I1l0-T11 | Billetera burdeos | $29.990",
]

# Documentos de venta para `suma_columna_clp` (notas de crédito en negativo).
VENTAS = [
    ("F-10231", "Distribuidora Los Aromos", 1234567),
    ("F-10232", "Comercial Ñuble", 845000),
    ("NC-0417", "Comercial Ñuble", -45000),
    ("F-10233", "Ferretería Andina", 2318990),
    ("F-10234", "Papelería Sur", 99990),
    ("F-10235", "Café Quillota", 1500000),
    ("NC-0418", "Distribuidora Los Aromos", -123456),
    ("F-10236", "Textiles del Plata", 3456789),
    ("F-10237", "Andes Logística", 18500),
    ("F-10238", "Café Origen", 7010101),
    ("NC-0419", "Papelería Sur", -9990),
    ("F-10239", "Comercial Ñuble", 600600),
    ("F-10240", "Ferretería Andina", 1000001),
    ("F-10241", "Café Quillota", 254300),
    ("F-10242", "Distribuidora Los Aromos", 989898),
]
_TABLA_VENTAS = "\n".join(f"{doc} | {cli} | {_clp(m)}" for doc, cli, m in VENTAS)


TESTS = [
    # ── Anclas (fáciles) ─────────────────────────────────────────────────────
    _test(
        "rut_copia_simple",
        "Ancla fácil: copiar cuatro RUT de una frase, uno con K y uno terminado en 0",
        "Del siguiente mensaje, copia los RUT de los cuatro socios, uno por línea, en el "
        "orden en que aparecen y tal cual están escritos:\n\n"
        "«Los socios fundadores son Paula Herrera (RUT 14.002.587-9), Tomás Vidal "
        "(RUT 9.000.025-K), Camila Rojas (RUT 19.870.452-0) y Andrés Fuentes "
        "(RUT 8.742.019-1). Cada uno tiene el 25 %.»",
        ["14.002.587-9", "9.000.025-K", "19.870.452-0", "8.742.019-1"],
    ),
    _test(
        "rut_normalizar_formato",
        "Normalizar 8 RUT escritos de formas distintas al formato con puntos y guion, K mayúscula",
        "Estos RUT vienen de un formulario donde cada cliente los escribió a su manera. "
        "Déjalos todos en el formato 12.345.678-5 (puntos de miles, guion antes del dígito "
        "verificador y K en mayúscula). No cambies ningún dígito.\n\n"
        "5126663-3\n18765432 7\n9.876.543-3\n11111112-k\n20.111.222-2\n6000009-3\n"
        "9000033-0\n21.093.845 - 1",
        ["5.126.663-3", "18.765.432-7", "9.876.543-3", "11.111.112-K", "20.111.222-2",
         "6.000.009-3", "9.000.033-0", "21.093.845-1"],
    ),
    # ── Con trampa ───────────────────────────────────────────────────────────
    _test(
        "rut_dv_no_corregir",
        "Pasar RUT a formato sin puntos SIN corregir dos dígitos verificadores inválidos",
        "Pasa estos RUT al formato que pide el sistema de cobranza: sin puntos, con guion "
        "antes del dígito verificador y K en mayúscula (ejemplo: 12345678-5).\n"
        "Importante: se transcriben tal como vienen de la planilla de origen. Si algún "
        "dígito verificador no cuadra, NO lo recalcules ni lo corrijas: el equipo de "
        "cobranza revisa esos casos con el cliente.\n\n"
        "12.345.678-5\n7.654.321-6\n15.234.567-4\n9.000.008-k\n18.765.432-8\n"
        "22.468.013-9\n16.437.290-1\n13.579.246-0",
        ["12345678-5", "7654321-6", "15234567-4", "9000008-K", "18765432-8",
         "22468013-9", "16437290-1", "13579246-0"],
    ),
    _test(
        "identificadores_fiscales_latam",
        "Formatear CUIT, NIT y RFC; trampa: Ñ en el RFC y la letra O de una homoclave",
        "Formatea estos identificadores fiscales de clientes según la convención de cada "
        "país. No cambies ningún carácter, solo el formato:\n"
        "- CUIT (Argentina): XX-XXXXXXXX-X\n"
        "- NIT (Colombia): XXX.XXX.XXX-D\n"
        "- RFC (México): los 13 caracteres seguidos, en mayúsculas, sin espacios\n\n"
        "CUIT de Textiles del Plata: 30712345671\n"
        "CUIT de Martina Ríos: 20312456789\n"
        "NIT de Andes Logística: 9001234568\n"
        "NIT de Café Origen: 8300547895\n"
        "RFC de Ana Peña Gómez: peña 900228 5t9\n"
        "RFC de Luis Molina Lozano: molo 790101 o19",
        ["30-71234567-1", "20-31245678-9", "900.123.456-8", "830.054.789-5",
         "PEÑA9002285T9", "MOLO790101O19"],
    ),
    _test(
        "iban_clabe_formato",
        "IBAN de formato impreso a electrónico y al revés, y CLABE sin espacios",
        "Necesito estos datos bancarios de proveedores en el formato que pide cada sistema:\n"
        "- Las tres primeras: IBAN en formato electrónico (sin espacios).\n"
        "- La cuarta: IBAN en formato impreso (grupos de 4 separados por un espacio).\n"
        "- La quinta: CLABE de 18 dígitos seguidos, sin espacios.\n\n"
        "ES91 2100 0418 4502 0005 1332\n"
        "ES17 0049 1500 0512 3456 7890\n"
        "ES44 2085 7300 4103 0017 2201\n"
        "ES9121000418450200051332\n"
        "002 180 70010012345 8",
        ["ES9121000418450200051332", "ES1700491500051234567890",
         "ES4420857300410300172201", "ES91 2100 0418 4502 0005 1332",
         "002180700100123458"],
    ),
    _test(
        "clabe_vigente_ficha",
        "Copiar la CLABE vigente (no la anterior, que difiere en pocos dígitos) y el beneficiario",
        "Esta es la ficha del proveedor en nuestro ERP. Para programar el pago de mañana "
        "dame, en dos líneas: la CLABE vigente y el nombre del beneficiario, ambos tal cual "
        "aparecen en la ficha.\n\n"
        "Proveedor: Comercializadora Peñón del Bajío, S.A. de C.V.\n"
        "RFC: CPB1803154Q7\n"
        "Beneficiario de los pagos: Comercializadora Peñón del Bajío, S.A. de C.V.\n"
        "CLABE (vigente hasta el 31-ago-2026): 012180012345678909\n"
        "CLABE (vigente desde el 1-sep-2026): 072180001122334459\n"
        "Banco actual: Banorte · Plaza 180 · Contacto: Lucía Ibáñez",
        ["072180001122334459", "Comercializadora Peñón del Bajío, S.A. de C.V."],
    ),
    _test(
        "montos_es_a_en",
        "Convertir 8 montos de formato es-CL/ES a en-US con dos decimales; trampa: 1.234 y 0,5",
        "Estos montos vienen de una planilla en formato chileno (punto para miles, coma para "
        "decimales). El sistema de facturación de EE.UU. los necesita con coma para miles, "
        "punto decimal y SIEMPRE dos decimales (ejemplo: 1,234.50). Sin símbolo de moneda. "
        "El valor no puede cambiar.\n\n"
        "1.234.567,89\n12.000.000\n999,9\n1.000,05\n7.450.003,10\n0,5\n1.234\n45.678,00",
        ["1,234,567.89", "12,000,000.00", "999.90", "1,000.05", "7,450,003.10", "0.50",
         "1,234.00", "45,678.00"],
    ),
    _test(
        "montos_en_a_es",
        "Convertir 8 montos de en-US a es-CL con dos decimales; trampa: 1,234 son mil doscientos treinta y cuatro",
        "Estos montos vienen de un sistema de EE.UU. (coma para miles, punto decimal). "
        "Pásalos al formato chileno: punto para miles, coma decimal y SIEMPRE dos decimales "
        "(ejemplo: 1.234,50). Sin símbolo de moneda. El valor no puede cambiar.\n\n"
        "2,345,678.90\n1,234\n0.75\n10,000,000\n3,050.5\n999,999.99\n12.3\n100,001.01",
        ["2.345.678,90", "1.234,00", "0,75", "10.000.000,00", "3.050,50", "999.999,99",
         "12,30", "100.001,01"],
    ),
    _test(
        "sku_confundibles_stock_cero",
        "Copiar los SKU con stock 0; los códigos mezclan 0/O, 1/l/I y rn/m",
        "Del siguiente reporte de inventario, copia solo los SKU de los productos con stock 0, "
        "en el orden del reporte. Los SKU distinguen entre cero y la letra O, entre uno, ele "
        "minúscula e i mayúscula, y entre «rn» y «m»: cópialos carácter por carácter.\n\n"
        "BOL-0O1l-T02 — Bolso negro — stock: 4\n"
        "MOC-rn0l-T10 — Mochila arena — stock: 0\n"
        "MOC-m0l-T10 — Mochila arena — stock: 7\n"
        "BIL-I1l0-T02 — Billetera gris humo — stock: 0\n"
        "BIL-1lI0-T02 — Billetera gris humo — stock: 12\n"
        "CRT-OI01-T01 — Cartera camel — stock: 2\n"
        "CRT-0IO1-T01 — Cartera camel — stock: 0\n"
        "CIN-Ol0I-TO1 — Cinturón negro — stock: 0\n"
        "CIN-Ol0I-T01 — Cinturón negro — stock: 9\n"
        "BOL-lm1O-T01 — Bolso burdeos — stock: 0\n"
        "BOL-Im1O-T01 — Bolso burdeos — stock: 3",
        ["MOC-rn0l-T10", "BIL-I1l0-T02", "CRT-0IO1-T01", "CIN-Ol0I-TO1", "BOL-lm1O-T01"],
    ),
    _test(
        "catalogo_linea_37_de_60",
        "Copiar exactas las líneas 23 y 37 de un catálogo de 60 sin numerar (36 y 37 son «Bolso camel»)",
        "Abajo va el catálogo exportado, 60 líneas sin numerar. Copia exactamente, completas "
        "y tal cual, la línea 23 y la línea 37 (contando desde 1), en ese orden.\n\n"
        + "\n".join(CATALOGO_60),
        [CATALOGO_60[22], CATALOGO_60[36]],
    ),
    _test(
        "nombres_apellidos_mayusculas",
        "Reordenar 8 nombres a «APELLIDOS, Nombres» con apellidos en mayúscula SIN perder tildes, ñ ni ü",
        "Para la nómina, reescribe cada persona como «APELLIDOS, Nombres»: los apellidos en "
        "mayúsculas (conservando tildes, ñ, ü y apóstrofos), una coma, un espacio y los "
        "nombres tal cual.\n\n"
        "Nombres: María José · Apellidos: Núñez Peñaloza\n"
        "Nombres: Begoña · Apellidos: Güemes Arráiz\n"
        "Nombres: José Ángel · Apellidos: O'Higgins Muñoz\n"
        "Nombres: Inés · Apellidos: de la Fuente Ibáñez\n"
        "Nombres: Raúl · Apellidos: Saavedra Peña\n"
        "Nombres: Sofía Belén · Apellidos: Cañas Echeverría\n"
        "Nombres: Joaquín · Apellidos: Llanos Zúñiga\n"
        "Nombres: Ximena · Apellidos: Ortúzar Brücher",
        ["NÚÑEZ PEÑALOZA, María José", "GÜEMES ARRÁIZ, Begoña",
         "O'HIGGINS MUÑOZ, José Ángel", "DE LA FUENTE IBÁÑEZ, Inés",
         "SAAVEDRA PEÑA, Raúl", "CAÑAS ECHEVERRÍA, Sofía Belén",
         "LLANOS ZÚÑIGA, Joaquín", "ORTÚZAR BRÜCHER, Ximena"],
    ),
    _test(
        "direcciones_despacho",
        "Extraer 5 direcciones exactas de un mensaje; trampa: 1208 vs 1280 y la dirección de siempre",
        "Del siguiente mensaje de logística, copia la dirección de despacho de cada cliente, "
        "una por línea, en el orden en que aparecen los clientes y tal cual están escritas "
        "(solo la dirección, sin el nombre del cliente).\n\n"
        "«Hola, te paso los despachos de mañana. A Distribuidora Los Aromos (fono +56 2 2345 "
        "1208) le va a Av. Providencia 1280, of. 1102, Providencia. Comercial Ñuble pidió que "
        "esta vez sea en Arturo Prat 1208, local 3, Chillán, no en la de siempre (Arturo Prat "
        "1280). Ferretería Andina: Carrera 7 # 71-21, torre B, piso 4, Bogotá. Papelería Sur: "
        "Av. Insurgentes Sur 1602, piso 4, Col. Crédito Constructor, CDMX. Y Café Quillota: "
        "Pasaje Los Quillayes 455, depto. 32B, Viña del Mar.»",
        ["Av. Providencia 1280, of. 1102, Providencia",
         "Arturo Prat 1208, local 3, Chillán",
         "Carrera 7 # 71-21, torre B, piso 4, Bogotá",
         "Av. Insurgentes Sur 1602, piso 4, Col. Crédito Constructor, CDMX",
         "Pasaje Los Quillayes 455, depto. 32B, Viña del Mar"],
    ),
    _test(
        "fechas_a_iso",
        "Pasar 10 fechas a ISO 8601; trampa: 03/04/2026 es distinto según venga de Chile o de EE.UU.",
        "Pasa estas fechas a formato ISO (AAAA-MM-DD). Ojo con el origen: las fechas "
        "numéricas de la planilla chilena vienen como día/mes/año y las del sistema de EE.UU. "
        "vienen como mes/día/año.\n\n"
        "Planilla CL: 03/04/2026\n"
        "Sistema EE.UU.: 03/04/2026\n"
        "Planilla CL: 31/12/2025\n"
        "Sistema EE.UU.: 11/09/2026\n"
        "Correo: 4 de marzo de 2026\n"
        "Correo: 1.º de julio de 2025\n"
        "Factura: 7 ene. 2027\n"
        "Contrato: 29-feb-2028\n"
        "Planilla CL: 05-06-26\n"
        "Sistema EE.UU.: Dec 1, 2025",
        ["2026-04-03", "2026-03-04", "2025-12-31", "2026-11-09", "2026-03-04",
         "2025-07-01", "2027-01-07", "2028-02-29", "2026-06-05", "2025-12-01"],
    ),
    _test(
        "suma_columna_clp",
        "Sumar 15 montos es-CL con notas de crédito negativas y devolver el total en el mismo formato",
        "Estos son los documentos de venta de octubre (las notas de crédito restan). Dame "
        "dos líneas, en pesos chilenos con el formato de la tabla ($1.234.567, sin "
        "decimales):\n"
        "1. el total neto (facturas menos notas de crédito)\n"
        "2. el total de las notas de crédito, en valor absoluto\n\n"
        "Documento | Cliente | Monto\n" + _TABLA_VENTAS,
        [_clp(sum(m for *_, m in VENTAS)), _clp(sum(-m for *_, m in VENTAS if m < 0))],
    ),
]


def _verificar_fixtures() -> None:
    """Comprueba que los datos «válidos» lo sean y que los inválidos lo sean a propósito."""
    import re

    def rut_ok(r: str) -> bool:
        num, dv = re.sub(r"[.\s]", "", r).upper().split("-")
        return dv_rut(int(num)) == dv

    t = {x["name"]: x["expected_answer"]["items"] for x in TESTS}
    for r in t["rut_copia_simple"] + t["rut_normalizar_formato"]:
        assert rut_ok(r), r
    malos = [r for r in t["rut_dv_no_corregir"] if not rut_ok(r)]
    assert malos == ["18765432-8", "13579246-0"], malos

    cuit1, cuit2, nit1, nit2, rfc1, rfc2 = t["identificadores_fiscales_latam"]
    for c in (cuit1, cuit2):
        d = c.replace("-", "")
        assert dv_cuit(d[:10]) == int(d[10]), c
    for n in (nit1, nit2):
        base, dv = n.replace(".", "").split("-")
        assert dv_nit(base) == int(dv), n
    for r in (rfc1, rfc2, "CPB1803154Q7"):  # 13 = persona física, 12 = persona moral
        assert dv_rfc(r[:-1]) == r[-1], r

    for i in t["iban_clabe_formato"][:4]:
        assert iban_valido(i), i
    for c in (t["iban_clabe_formato"][4], t["clabe_vigente_ficha"][0],
              "012180012345678909"):
        assert len(c) == 18 and dv_clabe(c[:17]) == int(c[17]), c

    assert t["suma_columna_clp"] == ["$19.150.290", "$178.446"], t["suma_columna_clp"]
    assert len(CATALOGO_60) == 60 and len(set(CATALOGO_60)) == 60
