# Gemini 3.5 Flash — extraer_claims/cobertura_ocho_claims

- model_id: `google/gemini-3.5-flash`
- success: True  | final: 2.4 | quality: 1.25
- latency_total: 9.37s | tokens_per_second: 218.1
- input_tokens: 258 | output_tokens: 2044

## Entrada exacta (lo que recibió el modelo)

**system:**

Extraé de la nota TODOS los datos verificables: cifras, fechas, nombres de empresas con su acción, y afirmaciones factuales que un verificador podría contrastar contra una fuente.

Devolvé SOLO un JSON:
{"claims": [{"texto": "<el dato, en una frase>", "tipo": "cifra|fecha|evento|cita"}]}

Reglas:
- NO extraigas opiniones, adjetivos ni proyecciones sin cifra.
- NO inventes: si no está en el texto, no va.
- Una cifra usada como EJEMPLO o comparación general no es un hecho de la nota.
- Respetá las negaciones: «no cerró» no es «cerró».

**user:**

Nordvia cerró una ronda semilla de US$ 4,2 millones el 14 de agosto de 2026, liderada por Aurora Ventures. La empresa, fundada en 2024 en Montevideo, emplea a 50 personas y opera en 3 países. Su facturación anual llegó a € 1,8 millones en 2025. Según su CEO, Marta Iribarne, la compañía abrirá oficinas en Chile durante el primer trimestre de 2027.


## Respuesta completa


        },
        {
          "texto": "Marta Iribarne afirmó que la compañía abrirá oficinas en Chile durante el primer trimestre de 2027",
          "tipo": "cita"
        }
      ]
    }
    ```
    Wait, "Marta Iribarne es la CEO de Nordvia" -> tipo: