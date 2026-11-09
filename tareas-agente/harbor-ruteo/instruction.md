Sos quien decide qué modelo de IA usa cada proceso del negocio. En `/app` tenés:

- `catalogo.json` — los modelos disponibles con sus mediciones
- `trabajos.json` — la cola de trabajos del mes, con su volumen y el presupuesto
- `politica.md` — las reglas de asignación. **Se cumplen todas.**

Registrá una decisión por cada trabajo con la herramienta `asignar.py`, que es la única
forma de dejarlas asentadas:

```
python /app/asignar.py --estado
python /app/asignar.py J-01 modelo-B --motivo "por qué"
python /app/asignar.py J-05 --escalar --motivo "por qué ninguno sirve"
```

Terminás cuando los seis trabajos tengan decisión y el total respete el presupuesto.
