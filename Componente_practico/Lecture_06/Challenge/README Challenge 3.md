# 🏆 Challenge 3: Evaluación Final e Inferencia

Este repositorio contiene la resolución del tercer y último reto (Challenge 3) de nuestro proyecto de Machine Learning para la clasificación de vinos. El objetivo principal de este notebook es destapar el conjunto de prueba (*test set*) por primera vez para evaluar el modelo campeón, analizar su capacidad de generalización y construir un *pipeline* de inferencia robusto para nuevos datos.

## Descripción del Proyecto

En el notebook `03_evaluation_deployment_challenge.ipynb` se llevaron a cabo las siguientes tareas:
1. **Carga del Sistema:** Importación del modelo campeón (`champion_model.joblib`), el contrato de datos y el conjunto de prueba (`test.csv`).
2. **Evaluación Final:** Medición del desempeño del modelo ante datos nunca vistos utilizando métricas como Exactitud (*Accuracy*) y *F1-score macro*, además de la visualización de la Matriz de Confusión.
3. **Función de Inferencia:** Construcción de una función de predicción defensiva que valida el esquema de los datos de entrada (comprobando que no falten columnas) antes de generar predicciones.
4. **Predicción por Lotes:** Simulación de un entorno de producción donde el modelo recibe un lote de nuevos registros y devuelve las clases predichas junto con sus probabilidades.
5. **Reporte y Persistencia:** Guardado de las métricas finales y las predicciones en archivos para auditoría y uso futuro.

---

## Estructura de Archivos Esperada

El código asume que tu entorno de trabajo cuenta con los artefactos de los retos anteriores y generará los nuevos reportes en la siguiente estructura:

```text
Proyecto/
│
├── 03_evaluation_deployment_challenge.ipynb  # Notebook principal de esta fase
├── data/
│   └── processed/ 
│       └── test.csv                 # Dataset de prueba (Generado en Challenge 1)
├── artifacts/
│   ├── data_contract.json           # Metadatos (Generado en Challenge 1)
│   ├── training_metadata.json       # Metadatos de entrenamiento (Generado en Challenge 2)
│   └── champion_model.joblib        # Modelo campeón entrenado (Generado en Challenge 2)
└── reports/                      
    ├── test_metrics.json            # Salida: Métricas finales de evaluación
    └── batch_predictions.csv        # Salida: Resultados de la predicción por lotes
