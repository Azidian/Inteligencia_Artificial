# Challenge 2: Entrenamiento y Selección del Modelo

Este repositorio contiene la resolución del segundo reto (Challenge 2) de nuestro proyecto de Machine Learning para la clasificación de vinos. El objetivo principal de este notebook es construir flujos de trabajo (*pipelines*) reproducibles, comparar distintas familias de algoritmos, optimizar sus hiperparámetros mediante validación cruzada y guardar el modelo campeón sin comprometer los datos de prueba (*test*).

## Descripción del Proyecto

En el notebook `02_training_challenge.ipynb` se llevaron a cabo las siguientes tareas:
1. **Carga de Artefactos:** Importación de los datos de entrenamiento (`train.csv`) y del contrato de datos (`data_contract.json`) generados en el Challenge 1.
2. **Pipelines de Preprocesamiento:** Creación de transformadores (`ColumnTransformer`) para imputación de valores faltantes y escalado de datos (`StandardScaler`), encapsulados correctamente para evitar fuga de información (*data leakage*).
3. **Comparación de Modelos:** Evaluación inicial de tres algoritmos: `DecisionTree`, `LogisticRegression` y `KNN`.
4. **Optimización de Hiperparámetros:** Búsqueda exhaustiva con `GridSearchCV` y validación cruzada estratificada (5 *folds*).
5. **Selección del Campeón:** Elección de la **Regresión Logística (C=1)** por su excelente balance entre exactitud (0.979), estabilidad (menor desviación estándar) e interpretabilidad.
6. **Persistencia:** Guardado del modelo entrenado y sus métricas para la fase de evaluación.

---

## Estructura de Archivos Esperada

El código asume que tu entorno de trabajo tiene la siguiente estructura de directorios:

```text
Proyecto/
│
├── 02_training_challenge.ipynb      # Notebook principal de esta fase
├── data/
│   └── processed/ 
│       └── train.csv                # Dataset de entrada (Generado en Challenge 1)
├── artifacts/
│   ├── data_contract.json           # Metadatos de entrada (Generado en Challenge 1)
│   ├── champion_model.joblib        # Salida: Modelo entrenado campeón
│   └── training_metadata.json       # Salida: Parámetros y métricas del entrenamiento
└── reports/                      
    └── cv_results.csv               # Salida: Resultados completos de la validación cruzada
