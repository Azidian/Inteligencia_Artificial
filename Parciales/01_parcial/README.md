# Examen Práctico: Q-Learning Tabular con Pac-Man

Implementación de un agente inteligente basado en **Aprendizaje por Refuerzo (Reinforcement Learning)** utilizando el algoritmo **Q-Learning tabular** para resolver un entorno discreto y simplificado del juego Pac-Man. El objetivo del agente consiste en aprender de forma autónoma una política óptima para comer la mayor cantidad de comida, minimizar el número de pasos y evitar ser atrapado por el fantasma.

---

## Estructura del Repositorio

* `04_qlearning_pacman_examen_IA.ipynb`: Cuaderno de Jupyter/Colab con el desarrollo paso a paso del examen, entrenamiento, métricas y análisis de resultados.
* `tabular_pacman_env.py`: Definición del entorno (`TabularPacmanEnv`), lógica del tablero, acciones legales y renderizado gráfico.
* `README.md`: Documentación general de instalación, configuración y ejecución del proyecto.

---

## Configuración del Entorno y Manejo de Rutas en Google Colab

Si al ejecutar las primeras celdas de importación aparece el error:
```bash
ModuleNotFoundError: No module named 'tabular_pacman_env'
Se debe a que Google Colab busca los módulos en su directorio raíz local (/content) en lugar de la carpeta de Google Drive donde está alojado el archivo tabular_pacman_env.py.  Opción A: Carga directa al entorno local de Colab (Recomendada)En la barra lateral izquierda de Google Colab, haz clic en el icono de Archivos (📁).Arrastra el archivo tabular_pacman_env.py a la raíz del panel de archivos (/content).En el notebook, importa el módulo directamente sin montar Google Drive:Pythonfrom tabular_pacman_env import TabularPacmanEnv, ACTIONS

env = TabularPacmanEnv(seed=7)
print("Número de estados:", env.n_states)
print("Número de acciones:", env.n_actions)
Opción B: Montar Google Drive y cambiar al directorio del proyectoSi prefieres mantener los archivos en tu Google Drive, monta la unidad y apunta explícitamente a la carpeta que contiene el archivo:Pythonfrom google.colab import drive
import sys
from pathlib import Path

# 1. Montar Google Drive
drive.mount('/content/drive')

# 2. Definir la ruta exacta de la carpeta del proyecto
# Modifica esta ruta según la ubicación real en tu Google Drive
RUTA_PROYECTO = "/content/drive/MyDrive/Universidad/Semestre 5/IA/pacman"

# 3. Cambiar de directorio y agregar la carpeta al sys.path
%cd "$RUTA_PROYECTO"
if RUTA_PROYECTO not in sys.path:
    sys.path.insert(0, RUTA_PROYECTO)

# 4. Importar el entorno
from tabular_pacman_env import TabularPacmanEnv, ACTIONS

env = TabularPacmanEnv(seed=7)
```
