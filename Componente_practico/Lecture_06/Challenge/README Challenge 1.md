# Challenge 1: Datos y Análisis Exploratorio

Este repositorio contiene la resolución del primer reto (Challenge 1) de nuestro proyecto de clasificación de vinos. El objetivo principal de este notebook es preparar una fuente de datos confiable, realizar un análisis exploratorio (EDA) y asegurar la persistencia de los datos para las siguientes etapas del ciclo de vida del modelo de Machine Learning.

## Descripción del Proyecto

En el notebook `01_data_challenge.ipynb` se llevan a cabo las siguientes tareas:
1. **Carga y Validación:** Importación del dataset `wine.csv` original.
2. **Profiling (Calidad de Datos):** Revisión de valores nulos, duplicados, tipos de datos y distribución de la variable objetivo (`target`).
3. **Split Estratificado:** División de los datos en conjuntos de entrenamiento (80%) y prueba (20%) asegurando un balance de clases mediante `stratify`.
4. **Análisis Exploratorio (EDA):** Visualización de la distribución de clases, diagramas de caja (boxplots) para identificar dispersiones y un mapa de calor (heatmap) para evaluar correlaciones métricas **únicamente sobre el conjunto de entrenamiento**.
5. **Persistencia y Contrato de Datos:** Exportación de los conjuntos limpios y guardado de un archivo JSON con los metadatos requeridos.

---

## Estructura de Archivos Esperada

El notebook asume (y crea en caso de no existir) la siguiente estructura de carpetas en tu directorio de trabajo:

```text
Proyecto/
│
├──  01_data_challenge.ipynb       # Notebook principal
├── data/
│   ├── wine.csv                     # ⬅️ Dataset de entrada (Requerido)
│   └── processed/                
│       ├── train.csv                # Salida generada por el notebook
│       └── test.csv                 # Salida generada por el notebook
├── artifacts/
│   └── data_contract.json           # Salida generada con metadatos del proyecto
└── reports/                      # Carpeta reservada para reportes futuros
```

---

## Posibles Errores en Google Colab y Cómo Solucionarlos

Si estás ejecutando este notebook en **Google Colab**, es muy probable que al correr la celda de lectura de datos obtengas un error como este:

`FileNotFoundError: [Errno 2] No such file or directory: '/content/data/wine.csv'`

**¿Por qué sucede?**
Google Colab es un entorno temporal. El código intenta buscar el archivo en la ruta `/content/data/wine.csv`, pero como la sesión es nueva, la carpeta `data` y el archivo `wine.csv` no existen físicamente en esa máquina virtual.

### Solución 1: Subida Manual (Recomendado)
1. Ve al menú lateral izquierdo de Colab y haz clic en el ícono de la carpeta (**Archivos**).
2. Haz clic derecho en el espacio vacío, selecciona **"Nueva carpeta"** y nómbrala `data`.
3. Arrastra tu archivo `wine.csv` desde tu computador hacia adentro de la carpeta `data` recién creada.
4. Vuelve a ejecutar la celda. ¡El error desaparecerá!

### Solución 2: Usar Código para Crear la Ruta y Descargar
Si prefieres automatizarlo, puedes crear una nueva celda al principio de tu notebook con este ejemplo para que Python cree la carpeta y descargue un dataset estándar desde la web, apuntando a la ruta correcta que pide tu código:

```python
import os
import urllib.request

# 1. Creamos la carpeta 'data' que el código necesita
os.makedirs('/content/data', exist_ok=True)

# 2. Descargamos el archivo directamente a esa carpeta
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
urllib.request.urlretrieve(url, '/content/data/wine.csv')

print("Archivo descargado y guardado en /content/data/wine.csv exitosamente.")
```

---

## Requisitos e Instalación

Para ejecutar este notebook localmente, asegúrate de tener instaladas las siguientes librerías de Python:

* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`
* `scikit-learn`

Puedes instalarlas usando pip:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## 🎯 Resultados (Outputs)

Al finalizar la ejecución completa del notebook, se habrán generado tres artefactos nuevos en tu entorno:
1. `data/processed/train.csv`: Conjunto de datos de entrenamiento limpio y procesado.
2. `data/processed/test.csv`: Conjunto de datos de validación (intacto tras el split).
3. `artifacts/data_contract.json`: Diccionario de configuración con las variables, el target, y parámetros reproducibles como el `random_state`.
