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

_Respuesta:_ El agente permite cargar una imagen que se puede redimensionar para aumentar o disminuir los tokens que podrían ser usados con esta a la hora de mostrarla o representarla, estos aparecen en la parte inferior de la imagen junto con las dimensiones objetivo. Cabe destacar que este proceso de redimensión puede implicar una pérdida de calidad en la imagen resultante.

------------------------------------------------------------------------

## 3. Análisis PEAS
  
**Performance**   ¿Qué significa que el agente haga bien su trabajo?
- Logró representar la imagen con la cantidad de detalle, manteniendo su relación de aspecto o presupuesto visual como lo menciona él mismo.
- Utiliza eficientemente el presupuesto de tokens.
- Tiene una mayor conservación de información visual a mayor uso de tokens, mientras que un uso menor permite un procesamiento más rápido.
  
**Environment**   ¿Con qué interactúa el agente?
- Interfaz de Hugging Face Spaces.
- Imagen de usuario.
- Opciones de presupuesto dadas por el usuario.

**Actuators**     ¿Qué acciones produce?
- Redimensión de imagen.
- Renderizado de la imagen redimensionada y visualización de las métricas en pantalla.
- Relación y comparación de redimensión por medio de las distintas opciones de redimensión.

**Sensors**       ¿Qué información recibe como entrada?
- Recibe la imagen de usuario y la configuración (el presupuesto de tokens).
- Proporciones de la imagen.

------------------------------------------------------------------------

## 4. Clasificación del entorno

Complete la siguiente tabla y justifique brevemente cada respuesta.

 | **Elemento** | **Clasificación** | **Justificación**                                                                                                                                                                                                                                                                                  |
| ------------ | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Observable   | Total             | Total. Para realizar su tarea, el sistema recibe la información como: la imagen y la configuración seleccionada por el usuario. Tiene acceso total a las entradas que son proporcionadas por el usuario y eso es especificamente lo único que necesita para su debido trabajo.                     |
| Determinista | Sí                | Sí. Puesto que si le das una misma imagen y el mismo presupuesto de tokens, el resultado de la redimensión debería ser el mismo. La acción depende de las entradas recibidas por el usuario. (Imagen y configuración)                                                                              |
| Episódico    | Si                | Si. Cada interacción puede considerarse un episodio independiente porque: se carga una imagen, se selecciona el presupuesto que se quiere y el sistema procesa la imagen. Y puedo repetir este proceso varias veces, porque mi entrada anterior no es necesaria para procesar la siguiente imagen. |
| Estático     | Si                | Si. El entorno no cambia mientras el agente está tomando una decisión. La imagen y la configuración permanecen iguales durante el procesamiento.                                                                                                                                                   |
| Discreto     | Si                | Si. Porque las acciones principales realizadas por el agente tienen y se basan en opciones definidas previamente, como los diferentes presupuestos de tokens, además, el resultado se produce mediante un proceso computacional específico que explican por medio de una formula matemática.       |
| Conocido     | Si                | Si. El usuario conoce las entradas que proporciona al agente y las opciones disponibles, por lo que el funcionamiento del sistema es conocido. Adicional a eso, el presupuesto visual determina cuánto detalle se conserva en la representación de la imagen al final.                             |


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

_Respuesta:_ En mi opinión, parece un agente de reflejo simple, ya que utiliza información sobre la imagen, sus dimensiones y el presupuesto de tokens para decidir cómo procesarla y ya. Es decir, opera mendiantemediante reglas definidas, el agente no recuerda las imagenesimágenes anteriores, no traza caminos para intentar ganarle a algo porque no es un juego, y a mi parecersegún el comportamiento observado no está entrenando a medida que tenemos interacción.

Esa es mi percepción a lo que logré identificar por la página, no puedo decir con total certeza qu enoque no sea un modelo decon aprendizaje porque no sé por dentródentro cómo ha sido creado el agente. 

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
  
**Otro ejemplo**
- Space seleccionado: OvisOCR2
- Enlace: https://huggingface.co/spaces/ATH-MaxS/OvisOCR2
<img width="1918" height="846" alt="image" src="https://github.com/user-attachments/assets/af1067fa-ed0b-4e82-9b6e-1cdc291eb30c" />

_Justificación:_
- Totalmente Observable:
El agente tiene acceso a la totalidad de la información que requiere, porque cuando cargamos el documento o la imagen, el sistema percibe el contenido, todos los píxeles del texto, tablas o estructura.

- Determinista:
La tarea de extraer texto en OCR y convertirlo a Markdown persigue un resultado exacto. Si se ingresa exactamente la misma imagen, el sistema debería devolver la misma transcripción. A diferencia de un modelo de chat no se presenta algo que pueda alterar las salidas a la hora de ser extraidas (a menos que se entregue una imagen o PDF con particularidades espaciales)

- Episódico:
El agente lo que hace es recibir un documento, procesarlo y entregar el texto. No requiere de guardar documentos anteriores, porque la conversión de un archivo no tiene ningún impacto en cómo se procesará el siguiente. No hay un recuento o historial que afecte las interacciones futuras.

Esta herramienta resulta ser muy directa, por ejemplo, si uno necesita extraer rápidamente un bloque de código de una captura de pantalla, el agente simplemente hace la conversión y termina. No tiene flujo de conversación, no necesita hacer uso de la memoria ni analizar el contexto de lo que se subió o lo que se le envió como entrada antes. 

2.  **Parcialmente observable, estocástico y secuencial.**

- Space seleccionado: HF Realtime Voice

- Enlace: https://huggingface.co/spaces/smolagents/hf-realtime-voice

<img width="1913" height="768" alt="image" src="https://github.com/user-attachments/assets/6a506725-c4e3-4b61-bb4e-02c1c98d14c3" />

_Justificación:_ 
- Parcialmente Observable:
El agente es parcialmente observable debido a que escucha lo que el usuario dice en cada interacción, no tiene acceso a todo el contexto interno (emociones, intenciones, pensamientos, tono, etc). Su percepción del entorno es limitada a la entrada de voz que se le da.

- Estocástico: 
El resultado de cada interacción no es igual: El reconocimiento de voz varia por ruido, acento o entonación en la entrada dada. Inclusive la respuesta a un intento de misma entrada es diferente, lo que deja una incertidumbre clara en las respuestas pro parte del agente.

- Secuencial:
La conversación se va moldeando a medida que se avanza en la misma, ya que lo que responda cada uno de los entes participantes (el usuario y el agente) va a influenciar en el camino que tome la interacción. Aunque el sistema hace uso de la memoria para mantener el flujo del diálogo, su capacidad de asociación a largo plazo es limitada frente a conceptos similares presentados anteriormente. Sin embargo, sí se evidencia que es capaz de seguir un flujo de conversación y hacer uso de lo previamente dicho.

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
