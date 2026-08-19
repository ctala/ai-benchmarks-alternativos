# Nemotron 3 Nano Omni 30B-A3B Reasoning — agent_capabilities/agent_team_delegation

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 9.41 | quality: 9.8
- latency_total: 4.951s | tokens_per_second: 237.7
- input_tokens: 1350 | output_tokens: 1177
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente estructurada, proporcionando un plan detallado que un emprendedor podría usar directamente.

## Respuesta completa

**Plan de ejecución**

1. **Investigación de la competencia**  
   - *Agente*: **researcher**  
   - *Prioridad*: **alta**  
   - *Tarea*: Buscar información pública (páginas web, testimonios, precios, características) de los 3 principales competidores de AutoFlow AI.  
   - *Resultado esperado*: Resumen con fortalezas, debilidades, precios y estrategias de marketing de cada competidor.

2. **Definición del copy de la landing page**  
   - *Agente*: **writer** (una vez que tenga la información de investigación)  
   - *Prioridad*: **alta**  
   - *Tarea*: Redactar hero headline, subtítulo, lista de features, tabla de precios y CTA persuasiva.  
   - *Base*: Datos del researcher + lineamientos de tono y estilo (a confirmar si es necesario).

3. **Creación de assets visuales**  
   - *Agente*: **designer**  
   - *Prioridad*: **media**  
   - *Tarea*: Diseñar la imagen hero y los gráficos de features (tamaño web, estilo coherente con la marca).  
   - *Entrada*: Copy finalizado y guía de estilo (colores, tipografía) que recibiremos del equipo.

4. **Generación del código HTML/CSS**  
   - *Agente*: **coder**  
   - *Prioridad*: **alta**  
   - *Tarea*: Convertir el copy y los assets en una página web responsiva (HTML5 + CSS3, con posible uso de Bootstrap/Tailwind).  
   - *Entrada*: Texto final y archivos de imagenes.

5. **Revisión final**  
   - *Agente*: **reviewer**  
   - *Prioridad*: **media**  
   - *Tarea*: Verificar ortografía, consistencia del mensaje, correcto funcionamiento del código y calidad de los assets.  
   - *Entrada*: Todo el material entregado por writer, designer y coder.

6. **Publicación (opcional)**  
   - Si se requiere lanzar la landing, después de la revisión podemos usar un skill de publicación (p. ej., `publish_blog_post` o `create_social_media_campaign`).  
   - *Agente*: **coder** o **writer** según corresponda.

**Dependencias**  
- El **writer** necesita los datos del **researcher** → investigación primero.  
- El **designer** necesita el copy finalizado → después del writer.  
- El **coder** necesita copy y assets → después del writer y designer.  
- El **reviewer** revisa todo al final.

**Próximos pasos**  
1️⃣ Delegar la investigación de competencia al **researcher** (alta prioridad).  
2️⃣ Pedir al equipo información de estilo (paleta de colores, tipografía, tono de voz) para que el **writer** y **designer** trabajen con bases claras.  

A continuación, procederé a delegar la primera tarea al **researcher**. 

--- 

**Delegación 1:**  
- **agent_type:** researcher  
- **task:** "Investigar y proporcionar un informe sobre los 3 principales competidores de AutoFlow AI (información de productos, precios, características y estrategias de marketing)."  
- **priority:** high  

(Esperaré la respuesta del researcher antes de continuar con el siguiente paso.)