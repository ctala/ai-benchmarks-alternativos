# Llama 3.1 8B Instant — orchestration/parallel_vs_sequential_judgment

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 4.55 | quality: 2.86
- latency_total: 3.829s | tokens_per_second: 139.2
- input_tokens: 1448 | output_tokens: 533

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente orquestador que optimiza la ejecucion.
Clasifica cada tarea como parallelizable o secuencial, justificando por que.
Las tareas paralelas se ejecutan al mismo tiempo para mayor velocidad.
Las tareas secuenciales dependen del resultado de una tarea anterior.

**user:**

Tengo estas 6 tareas para preparar el lanzamiento de un producto:

A. Buscar precios de competidores en el mercado
B. Generar la descripcion del producto basada en las specs tecnicas (archivo: /docs/specs.md)
C. Calcular el precio optimo basado en costos + margen + precios de competidores
D. Crear la landing page con la descripcion y precio
E. Enviar email al equipo de marketing con el enlace de la landing
F. Publicar anuncio en redes sociales

Analiza las dependencias y presenta:
1. Un diagrama de dependencias (que tarea depende de cual)
2. Un plan de ejecucion optimizado (que se puede hacer en paralelo)
3. El tiempo estimado si cada tarea toma ~5 minutos

Ejecuta las tareas que se pueden iniciar inmediatamente.


## Respuesta completa

import networkx as nx

# Creamos un grafo vacío
G = nx.DiGraph()

# Agregamos las tareas como nodos
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")
G.add_node("F")

# Agregamos las dependencias como arcos
G.add_edge("B", "C")  # C depende de B
G.add_edge("C", "D")  # D depende de C
G.add_edge("D", "E")  # E depende de D
G.add_edge("F", "E")  # E depende de F

# Imprimimos el grafo
print("Diagrama de dependencias:")
print(G)

# Identificamos las tareas que se pueden hacer en paralelo
tareas_paralelas = []
for nodo in G.nodes():
    if G.in_degree(nodo) == 0:
        tareas_paralelas.append(nodo)

# Imprimimos las tareas que se pueden hacer en paralelo
print("\nTareas que se pueden hacer en paralelo:")
print(tareas_paralelas)

# Identificamos las tareas que se pueden hacer en paralelo
tareas_secuenciales = []
for nodo in G.nodes():
    if G.in_degree(nodo) > 0:
        tareas_secuenciales.append(nodo)

# Imprimimos las tareas que se deben hacer secuencialmente
print("\nTareas que se deben hacer secuencialmente:")
print(tareas_secuenciales)

# Calculamos el tiempo estimado para cada tarea
tiempo_estimado = 5  # ~5 minutos

# Imprimimos el plan de ejecución optimizado
print("\nPlan de ejecución optimizado:")
print("Tareas que se pueden hacer en paralelo:")
for tarea in tareas_paralelas:
    print(f"- {tarea}")
print("\nTareas que se deben hacer secuencialmente:")
for tarea in tareas_secuenciales:
    print(f"- {tarefa}")

# Calculamos el tiempo total estimado
tiempo_total_estimado = len(tareas_paralelas) * tiempo_estimado + sum([G.in_degree(tarea) * tiempo_estimado for tarea in tareas_secuenciales])

# Imprimimos el tiempo total estimado
print(f"\nTiempo total estimado: {tiempo_total_estimado} minutos")