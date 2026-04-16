"""
Tests de OCR y extraccion de texto desde descripciones de imagenes.
Evalua la capacidad del modelo de interpretar texto estructurado
(facturas, recibos, tarjetas de presentacion, capturas de pantalla)
a partir de descripciones detalladas del contenido visual.

Para modelos multimodales (MiMo-V2-Omni, Gemini, GPT-4o) se podrian
enviar imagenes reales en el futuro. Por ahora usamos descripciones
textuales que simulan la tarea de extraccion estructurada.
"""

TESTS = [
    {
        "name": "invoice_extraction",
        "description": "Extraer datos estructurados de una factura",
        "messages": [
            {"role": "system", "content": "Eres un sistema de OCR inteligente. Extraes datos estructurados de documentos."},
            {"role": "user", "content": """Tengo una factura escaneada con el siguiente contenido visible:

---
FACTURA N° 00234-2026
Fecha: 15 de Marzo de 2026

Emisor: TechFlow SpA
RUT: 77.432.198-3
Direccion: Av. Providencia 1234, Of. 501, Santiago

Cliente: Startup Labs Ltda.
RUT: 76.891.234-K
Direccion: Calle Moneda 920, Santiago

Detalle:
| Descripcion                | Cant | Precio Unit | Total      |
|---------------------------|------|-------------|------------|
| Licencia API Enterprise   | 1    | $890.000    | $890.000   |
| Soporte Premium (3 meses) | 3    | $150.000    | $450.000   |
| Integracion N8N custom    | 12   | $45.000     | $540.000   |

Neto: $1.880.000
IVA (19%): $357.200
Total: $2.237.200

Condicion de pago: 30 dias
Banco: Banco de Chile
Cuenta: 00-123-45678-90
---

Extrae TODOS los datos en formato JSON con esta estructura exacta:
{
  "numero_factura": "",
  "fecha": "",
  "emisor": {"nombre": "", "rut": "", "direccion": ""},
  "cliente": {"nombre": "", "rut": "", "direccion": ""},
  "items": [{"descripcion": "", "cantidad": 0, "precio_unitario": 0, "total": 0}],
  "neto": 0,
  "iva": 0,
  "total": 0,
  "condicion_pago": "",
  "banco": "",
  "cuenta": ""
}

Responde SOLO con el JSON, sin texto adicional."""},
        ],
        "criteria": {
            "min_words": 20,
            "required_sections": ["77.432.198-3", "76.891.234-K", "2237200", "00234"],
            "language": "es",
        },
        "expected_answer": {
            "type": "multi_string_check",
            "must_contain_exact": [
                "77.432.198-3",
                "76.891.234-K",
                "00234-2026",
                "TechFlow",
                "Startup Labs",
                "00-123-45678-90",
            ],
        },
    },
    {
        "name": "business_card_extraction",
        "description": "Extraer datos de una tarjeta de presentacion",
        "messages": [
            {"role": "system", "content": "Eres un sistema de OCR. Extraes informacion de contacto de tarjetas de presentacion."},
            {"role": "user", "content": """Tengo una tarjeta de presentacion que dice:

Lado frontal:
  MARIA JOSE RODRIGUEZ SOTO
  Chief Technology Officer

  NexaFlow Intelligence
  "Transforming Data into Decisions"

  +56 9 8765 4321
  mj.rodriguez@nexaflow.ai
  linkedin.com/in/mjrodriguez

Lado trasero:
  Av. Apoquindo 4500, Piso 12
  Las Condes, Santiago, Chile
  www.nexaflow.ai

Extrae la informacion en este formato JSON exacto:
{
  "nombre_completo": "",
  "cargo": "",
  "empresa": "",
  "slogan": "",
  "telefono": "",
  "email": "",
  "linkedin": "",
  "direccion": "",
  "ciudad": "",
  "pais": "",
  "website": ""
}

Solo el JSON, nada mas."""},
        ],
        "criteria": {
            "min_words": 10,
            "required_sections": [],
        },
        "expected_answer": {
            "type": "multi_string_check",
            "must_contain_exact": [
                "MARIA JOSE RODRIGUEZ SOTO",
                "Chief Technology Officer",
                "NexaFlow Intelligence",
                "+56 9 8765 4321",
                "mj.rodriguez@nexaflow.ai",
                "linkedin.com/in/mjrodriguez",
                "Apoquindo 4500",
                "www.nexaflow.ai",
            ],
        },
    },
    {
        "name": "receipt_math_verification",
        "description": "Extraer y verificar calculos de un recibo",
        "messages": [
            {"role": "user", "content": """Tengo un recibo de restaurante:

===============================
  RESTAURANTE EL PARRILLERO
  Av. Italia 1890, Nunoa
  Boleta N° 0082341
  Fecha: 12/04/2026 21:45
===============================
Mesa: 7          Mesero: Carlos

2x Lomo vetado         $18.900 c/u
1x Ensalada cesar      $7.500
3x Pisco sour          $6.900 c/u
1x Postre brownie      $5.800
1x Agua mineral 1.5L   $3.200

-------------------------------
Subtotal:              $73.000
Propina sugerida (10%): $7.300
-------------------------------
TOTAL:                 $80.300
===============================
Pago: Tarjeta credito ****4521

Tareas:
1. Extrae todos los items con sus precios en JSON
2. Verifica si el subtotal esta correcto sumando los items
3. Verifica si la propina esta bien calculada
4. Indica si hay algun error en los calculos

Responde en JSON con formato:
{
  "items": [...],
  "subtotal_facturado": 0,
  "subtotal_calculado": 0,
  "subtotal_correcto": true/false,
  "propina_correcta": true/false,
  "total_correcto": true/false,
  "errores": []
}"""},
        ],
        "criteria": {
            "min_words": 20,
            "required_sections": [],
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "2x18900 = 37800",
                "1x7500 = 7500",
                "3x6900 = 20700",
                "1x5800 = 5800",
                "1x3200 = 3200",
                "suma real = 75000",
                "subtotal facturado 73000 es incorrecto",
                "la propina sobre 73000 es correcta",
            ],
        },
    },
    {
        "name": "screenshot_table_extraction",
        "description": "Extraer tabla de datos de una captura de pantalla descrita",
        "messages": [
            {"role": "user", "content": """Tengo una captura de pantalla de un dashboard de metricas. El contenido visible es:

DASHBOARD - KPIs Marzo 2026

+------------------+--------+--------+--------+---------+
| Metrica          | Enero  | Feb    | Marzo  | Var M/M |
+------------------+--------+--------+--------+---------+
| MRR              | $45.2K | $48.7K | $52.1K | +7.0%   |
| Churn Rate       | 4.2%   | 3.8%   | 3.1%   | -0.7pp  |
| NPS              | 42     | 45     | 51     | +6      |
| CAC              | $234   | $198   | $187   | -$11    |
| LTV              | $1,890 | $2,010 | $2,340 | +$330   |
| Active Users     | 1,234  | 1,456  | 1,678  | +15.3%  |
| Support Tickets  | 89     | 76     | 63     | -17.1%  |
| Avg Response (h) | 4.2    | 3.1    | 2.4    | -0.7    |
+------------------+--------+--------+--------+---------+

Tendencia general: ↑ Positiva en todas las metricas

Extrae los datos en formato JSON y ademas:
1. Calcula el LTV/CAC ratio para cada mes
2. Identifica la metrica con mayor mejora porcentual
3. Proyecta los valores de Abril si la tendencia se mantiene

Responde en JSON estructurado."""},
        ],
        "criteria": {
            "min_words": 50,
            "required_sections": ["LTV", "CAC", "ratio"],
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "LTV/CAC enero: 1890/234 = 8.08",
                "LTV/CAC febrero: 2010/198 = 10.15",
                "LTV/CAC marzo: 2340/187 = 12.51",
                "ratio LTV/CAC mejora cada mes",
                "support tickets tiene mayor mejora porcentual",
            ],
        },
    },
    {
        "name": "handwritten_notes_extraction",
        "description": "Interpretar notas manuscritas con abreviaciones",
        "messages": [
            {"role": "system", "content": "Eres un sistema de OCR que interpreta notas manuscritas. Debes descifrar abreviaciones y organizar la informacion."},
            {"role": "user", "content": """Tengo una foto de notas manuscritas de una reunion. El texto reconocido (con errores tipicos de OCR en escritura a mano) es:

"Reunlon equlpo prod - 14/04/26
Asist: JP, MaJo, Seba, Cami (falt0 Nico)

1) Lanzamient0 v2.0 - mover de abr 28 a may 5
   - falta QA en modul0 pagos
   - bug crit en API webho0ks (Seba lo toma)

2) Metricas Q1:
   - MRR 52.1k (+15% vs Q4)
   - churn baj0 a 3.1% (obj era 3.5%)
   - NPS subio a 51 (re bueno!!)

3) Contratar 2 devs sr + 1 QA
   - presup aprob: $8M CLP/mes x 3 pax
   - JP hace JD p/ lunes

4) Prox reunion: lun 21/04 10am

Action items:
- Seba: fix webhook bug p/ mierc 16/04
- MaJo: actualzr roadmap en Notion
- Cami: prep demo p/ cliente Falabella (23/04)
- JP: publicar JDs en LinkedIn + GetOnBrd"

Tareas:
1. Corrige los errores de OCR y presenta el texto limpio
2. Extrae los action items en formato estructurado
3. Identifica las fechas mencionadas y crea un timeline

Responde en JSON:
{
  "texto_corregido": "",
  "fecha_reunion": "",
  "asistentes": [],
  "ausentes": [],
  "action_items": [{"responsable": "", "tarea": "", "fecha_limite": ""}],
  "fechas_clave": [{"fecha": "", "evento": ""}],
  "decisiones": []
}"""},
        ],
        "criteria": {
            "min_words": 50,
            "required_sections": [],
        },
        "expected_answer": {
            "type": "multi_string_check",
            "must_contain_exact": [
                "Seba",
                "MaJo",
                "webhook",
                "Falabella",
                "21/04",
                "16/04",
                "23/04",
            ],
        },
    },
]
