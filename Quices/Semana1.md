# Actividad de Clase: Analizando Agentes de IA con Hugging Face Spaces

## Instrucciones

1.  Ingresen a **https://huggingface.co/spaces**.
2.  Exploren diferentes Spaces.
3.  Seleccionen uno que les parezca interesante.
4.  Interactúen con el sistema durante algunos minutos.
5.  Completen la siguiente ficha de análisis.

------------------------------------------------------------------------

# Ficha de análisis

## 1. Nombre del Space

**Nombre: Gemma 4 - Vision Token Budget**
**Enlace: https://huggingface.co/spaces/google/gemma4_vision_token_budget**

------------------------------------------------------------------------

## 2. ¿Qué hace el agente?

Describa en dos o tres líneas cuál es la función del sistema.
El agente permite cargar una imagen que se puede redimensionar para aumentar o disminuir los tokens que podrían ser usados con esta a la hora de mostrarla o representarla, estos aparecen en la parte inferior de la imagen junto con las dimensiones objetivo. 
Algo a tener en cuenta es que al redimensionarla se puede perder calidad.

------------------------------------------------------------------------

## 3. Análisis PEAS

  Elemento          Respuesta
  ----------------- ----------------------------------------------------
  
**Performance**   ¿Qué significa que el agente haga bien su trabajo?
- Logró representar la imagen con la cantidad de detalle, manteniendo su relación de aspecto o presupuesto visual como lo menciona él mismo
- Utiliza eficientemente el presupuesto de tokens
- Tiene una mayor conservación de información visual a mayor uso de tokens, mientras que un uso menor permite un procesamiento más rápido
  
**Environment**   ¿Con qué interactúa el agente?
- Interfaz de Higging Space
- imagen de usurio
- opciones de presupuesto dadas por el usuario

**Actuators**     ¿Qué acciones produce?
- Redimensión de imagen
- Procesamiento de tokens 
- Relación y comparación de redimensión por medio de las distintas opciones de redimensión

**Sensors**       ¿Qué información recibe como entrada?
- Recibe la imagen de usuario y la configuración (El presupuesto de tokens)
- Proporciones de imagen

------------------------------------------------------------------------

## 4. Clasificación del entorno

Complete la siguiente tabla y justifique brevemente cada respuesta.

  Propiedad      Clasificación     Justificación
  -------------- ----------------- ---------------
  Observable     Total / Parcial   
Total. Para realizar su tarea, el sistema recibe la información como: la imagen y la configuración seleccionada por el usuario. Tiene acceso total a las entradas que son proporcionadas por el usuario y eso es especificamente lo único que necesita para su debido trabajo.

  Determinista   Sí / No  
Sí. Puesto que si le das una misma imagen y el mismo presupuesto de tokens, el resultado de la redimensión debería ser el mismo. La acción depende de las entradas recibidas por el usuario. (Imagen y configuración)

  Episódico      Sí / No   
Si. Cada interacción puede considerarse un episodio independiente porque: se carga una imagen, se selecciona el presupuesto que se quiere y el sistema procesa la imagen. Y puedo repetir este proceso varias veces, porque mi entrada anterior no es necesaria para procesar la siguiente imagen.

  Estático       Sí / No
Si. El entorno no cambia mientras el agente está tomando una decisión. La imagen y la configuración permanecen iguales durante el procesamiento. 

  Discreto       Sí / No           
Si. Porque las acciones principales realizadas por el agente tienen y se basan en opciones definidas previamente, como los diferentes presupuestos de tokens, además, el resultado se produce mediante un proceso computacional específico que explican por medio de una formula matemática.
  
Conocido       Sí / No  
Si. El usuario conoce las entradas que proporciona al agente y las opciones disponibles, por lo que el funcionamiento del sistema es conocido. Adicional a eso, el presupuesto visual determina cuánto detalle se conserva en la representación de la imagen al final.

------------------------------------------------------------------------

## 5. ¿Qué tipo de programa de agente creen que es?

Seleccione la opción que consideren más adecuada y explique por qué.

-   Agente de reflejo simple
-   Agente basado en modelo
-   Agente basado en objetivos
-   Agente basado en utilidad
-   Agente con aprendizaje

> **Importante:** No existe una única respuesta correcta. Lo importante
> es justificar la elección a partir del comportamiento observado.

Respuesta: En mi opinión, parece un agente de reflejo simple, ya que utiliza información sobre la imagen, sus dimensiones y el presupuesto de tokens para decidir cómo procesarla y ya.
Es decir, opera mendiante reglas definidas, el agente no recuerda las imagenes anteriores, no traza caminos para intentar ganarle a algo porque no es un juego, y a mi parecer no está entrenando a medida que tenemos interacción.

Esa es mi percepción a lo que logré identificar por la página, no puedo decir con total certeza qu eno sea un modelo de aprendizaje porque no sé por dentró cómo ha sido creado el agente. 

------------------------------------------------------------------------

# Discusión en clase

Después de las presentaciones, discutiremos preguntas como:

-   ¿Dos Spaces diferentes pueden compartir el mismo tipo de entorno?
-   ¿Es posible saber con certeza qué tipo de agente implementa un Space
    únicamente observándolo?
-   ¿Qué diferencia existe entre el comportamiento observable de un
    agente y su implementación interna?

------------------------------------------------------------------------

# Reto adicional

Encuentre un Space que pueda clasificarse como:

1.  **Totalmente observable, determinista y episódico.**
- Este de Gemma 4 es un gran ejemplo de totalmente observable, deterministico y episódico.

2.  **Parcialmente observable, estocástico y secuencial.**
- Space seleccionado: HF Realtime Voice (Voice chat over WebSocket contra un modelo HF speech-to-speech)

Justifique su respuesta:
Parcialmente observable: El agente no tiene acceso a toda la información del mundo exterior. Solo "percibe" el fragmento de audio que el usuario le envía a través del micrófono en ese instante. No conoce las verdaderas intenciones del usuario, el entorno en el que se encuentra, ni qué le va a decir en la siguiente interacción.
Estocástico: Al estar basado en modelos generativos (tanto para procesar el lenguaje como para generar la voz de respuesta), su comportamiento tiene un grado de aleatoriedad. Si le haces exactamente la misma pregunta dos veces, es muy probable que genere respuestas con estructuras de oraciones distintas, o incluso con ligeras variaciones en la entonación y el ritmo de la voz. No hay un solo resultado matemático exacto y predecible.
Secuencial: Al tratarse de un "chat de voz", las acciones pasadas afectan directamente las acciones futuras. Lo que el agente te responda en el turno número 10 de la conversación dependerá de la memoria y el contexto de todo lo que hablaron en los turnos del 1 al 9. No son episodios aislados.

------------------------------------------------------------------------

# Rúbrica (10 puntos)

| Criterio | Puntos |
|-----------|:------:|
| Descripción correcta del Space | 2 |
| Identificación de PEAS | 3 |
| Clasificación del entorno | 3 |
| Justificación del tipo de agente | 2 |
| **Total** | **10** |

------------------------------------------------------------------------
