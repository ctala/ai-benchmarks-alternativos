# GPT-5.6 Sol — creativity/depth_vs_superficial

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.59 | quality: 9.68
- latency_total: 108.999s | tokens_per_second: 32.8
- input_tokens: 139 | output_tokens: 3575
- judge_score: 5 | justificación: La respuesta ofrece ideas específicas y profundas, como modelar la cocina y resolver los últimos 150 metros, con estimaciones concretas y un riesgo no obvio, todo presentado de manera clara y organizada, lo que la hace altamente útil y original para un emprendedor.

## Respuesta completa

La pregunta correcta no es “¿dónde pongo IA?”, sino **“qué incertidumbre está destruyendo mi margen?”**. En delivery suelen ser dos: no saber cuándo estará realmente listo el pedido y no saber cuánto demorará la entrega dentro del edificio. La ruta entre ambos puntos ya está razonablemente resuelta por Google, Mapbox y otros proveedores.

Antes de construir nada, haría una cuenta simple. Ejemplo ilustrativo para Santiago:

- Ticket promedio: $18.000 CLP  
- Comisión al restaurante, 25%: $4.500  
- Tarifa al cliente: $1.500  
- Ingreso bruto por pedido: $6.000  
- Reparto: $3.000–$4.000  
- Pago, soporte, devoluciones y fraude: $700–$1.200  
- Promoción o descuento promedio: $500–$1.500  

Es fácil terminar con una contribución de apenas **$500–$1.000 por pedido**, incluso antes de costos fijos. Por eso, una IA que “aumenta engagement” pero agrega descuentos puede hacer crecer los pedidos y destruir más caja.

## Mi primera apuesta: modelar la cocina, no la ruta

Construiría un sistema que estime el **momento real de preparación**, incluyendo incertidumbre: no “estará listo en 18 minutos”, sino “50% de probabilidad a los 18 minutos y 90% a los 27”.

Se puede inferir usando:

- Restaurante y sucursal.
- Hora, día y feriados.
- Cantidad y combinación de platos.
- Pedidos recientemente aceptados por esa cocina.
- Diferencia histórica entre “pedido listo” y retiro efectivo.
- Cantidad de repartidores esperando.
- Lluvia, partidos o eventos que generan demanda concentrada.
- Comportamiento del restaurante: algunos marcan “listo” anticipadamente para proteger sus métricas.

La acción no es solamente despachar más tarde al repartidor. El sistema también debería:

- Reducir temporalmente la visibilidad de una cocina saturada.
- Alargar la promesa antes de que se produzca el atraso.
- Promover restaurantes cercanos con capacidad ociosa.
- Limitar platos de alta varianza durante una sobrecarga, en vez de cerrar toda la tienda.

Esto último es importante: una cocina podría preparar sándwiches en 8 minutos pero tardar 30 en platos al horno. El cuello de botella está a nivel de **producto y estación de cocina**, no solo de restaurante.

### Magnitud posible

Con 500 pedidos diarios, reducir la espera del repartidor en 2,5 minutos equivale a:

\[
500 \times 2,5 / 60 = 20,8 \text{ horas de repartidor por día}
\]

Valoradas conservadoramente en $5.500 CLP por hora productiva, son aproximadamente **$115.000 diarios o $3,4 millones mensuales**. No siempre se transforma directamente en ahorro —depende de cómo pagues—, pero sí puede convertirse en más pedidos por hora, menor necesidad de incentivos y mayor aceptación de viajes.

No usaría deep learning al principio. Una regresión cuantílica o gradient boosting con variables bien instrumentadas probablemente superará a un modelo sofisticado. Si tienes pocos datos por restaurante, usaría un modelo jerárquico que comparta información entre cocinas similares.

## Mi segunda apuesta: resolver “los últimos 150 metros”

En comunas con alta densidad de departamentos y oficinas, una parte importante del atraso no ocurre en la calle, sino entre la llegada al edificio y la entrega:

- Entrada distinta de la dirección oficial.
- Conserjería que no permite subir.
- Torre o departamento incompleto.
- Estacionamiento imposible.
- Ascensores lentos.
- Cliente que espera que el repartidor suba, mientras el repartidor espera que el cliente baje.

Crearía una **memoria operativa por edificio**, no una optimización de rutas. Para cada inmueble aprendería:

- Entrada correcta para delivery.
- Minutos típicos desde llegada hasta entrega.
- Si normalmente se entrega en conserjería o puerta.
- Franjas con mayor demora.
- Calidad de las instrucciones del cliente.
- Probabilidad de necesitar llamada o chat.

El checkout podría hacer una sola pregunta adaptativa, por ejemplo: “En este edificio, ¿recibes en conserjería o debe subir el repartidor?”. No un formulario largo.

Si el 45% de 500 pedidos llega a edificios y ahorras solo 1,5 minutos en esos casos, recuperas otras **5,6 horas operativas diarias**. El efecto posiblemente más valioso sería reducir llamadas, entregas fallidas y la cola larga del tiempo de entrega, no el promedio.

Además, esto crea una ventaja difícil de copiar: Google conoce la calle, pero no necesariamente sabe que la entrada útil de una torre está por una calle lateral o que después de las 22:00 la conserjería cambia el protocolo.

## Cómo lo probaría

No lanzaría en todo Santiago. Escogería una zona compacta, por ejemplo un corredor de alta densidad en Providencia–Ñuñoa, y 20–30 restaurantes con volumen suficiente.

Durante el primer mes instrumentaría correctamente:

- Creación y aceptación del pedido.
- Inicio estimado de preparación.
- Marcado como listo.
- Llegada del repartidor al restaurante.
- Retiro.
- Llegada al edificio.
- Primer contacto con el cliente.
- Entrega efectiva.
- Cancelaciones, compensaciones y recompra.

Luego probaría primero el modelo en modo silencioso: genera predicciones, pero no toma decisiones. Si no mejora claramente una regla simple por restaurante y franja horaria, no merece producción.

Para el experimento no usaría un A/B convencional por pedido. En una red logística hay interferencia: si el tratamiento libera repartidores, también mejora indirectamente al grupo de control. Usaría un **switchback test**, alternando tratamiento y control por bloques de tiempo y zona, comparando días equivalentes.

Las métricas serían:

- Minutos de espera en restaurante.
- Error p50 y p90 de la promesa de entrega.
- Pedidos por hora de repartidor.
- Contribución por pedido, después de compensaciones.
- Cancelaciones y reclamos.
- Recompra a 30 días.

No optimizaría solamente el ETA promedio: bajar el promedio mientras empeora el percentil 90 suele producir más clientes furiosos.

## Riesgo no obvio: la predicción puede empeorar aquello que predice

Supón que el modelo clasifica a un restaurante como lento. Empieza a enviar repartidores más tarde y a mostrarlo menos. Como recibe menos pedidos y menos observaciones recientes, el modelo conserva la etiqueta de “lento”. Se crea un ciclo de castigo difícil de revertir.

También puede premiar a restaurantes que manipulan el botón “pedido listo” y castigar a los honestos. Eso termina favoreciendo cadenas con operaciones estables y eliminando restaurantes pequeños, que podrían ser precisamente lo que diferencia tu marketplace.

Mitigaría esto con:

- Un 5–10% de exploración aleatoria controlada.
- Métricas separadas entre demora observada y conducta de reporte.
- Reentrenamiento con decaimiento temporal.
- Mecanismo para que el restaurante dispute datos incorrectos.
- No usar una sola predicción para decidir ranking, comisión o exclusión.

La memoria por edificio tiene otro riesgo: puede convertirse accidentalmente en una base de datos de seguridad con códigos de acceso, horarios y rutinas de residentes. **Nunca almacenaría códigos de portón como atributo reutilizable del modelo**; usaría expiración, cifrado y separación estricta entre instrucciones de un pedido y características agregadas del edificio.

## Mi opinión contrarian

**No construiría un chatbot para que el cliente “converse con la comida”, ni vendería la startup como una empresa de IA.** Elegir qué comer no suele ser el principal cuello de botella, y un LLM sobre catálogos desordenados puede inventar ingredientes, algo especialmente peligroso con alergias.

Tampoco entrenaría un motor propio de rutas al inicio. Compraría mapas y routing, y concentraría el desarrollo en datos que otros no tienen: **estado real de las cocinas y fricción real de los edificios**.

La IA debería ser una capa de control operacional invisible. Si después de 8–12 semanas no reduce al menos **1–2 minutos por pedido, el p90 de atraso o $300–$500 CLP de costo esperado**, probablemente hay problemas más importantes que resolver manualmente: densidad insuficiente, mala selección de zona, exceso de promociones o unit economics estructuralmente débiles.