# 🌱 Sistema Experto de Recomendación para Cultivo de Papa

Este proyecto implementa un sistema experto que recomienda prácticas de fertilización para el cultivo de papa. Basado en parámetros como pH, humedad del suelo y niveles de nitrógeno (N), fósforo (P) y potasio (K), el sistema sugiere la mejor forma y momento para aplicar fertilizantes.

---

## 🧠 Objetivo

Brindar recomendaciones precisas para mejorar la eficiencia en la aplicación de fertilizantes, evitar lixiviación y maximizar la calidad y el rendimiento del cultivo de papa.

---

## 📁 Estructura del Proyecto

```plaintext
SE/
├── SE.py                # Script principal: lógica del sistema experto
├── regresionLineal.py   # Módulo de regresión lineal para predicción de absorción
├── Diagrama.png         # Diagrama funcional del sistema
├── README.md            # Documentación
└── requirements.txt     # Dependencias necesarias


1.	Sistema de recomendaciones experto
![alt text](Diagrama.png)
1.1	Captura de datos del sensor
Esta etapa corresponde a los valores iniciales que el sensor puede proporcionar, como:
•	Niveles actuales en mg/Kg de Nitrógeno, Fósforo, Potasio.
•	Porcentaje de humedad del suelo.
•	Nivel de pH del suelo.
1.2	Análisis de regresión lineal
Se utiliza un modelo de regresión lineal para identificar relaciones entre las variables medidas (como niveles de nutrientes) y los objetivos (rendimiento esperado, condiciones óptimas).
El objetivo es estimar cómo los nutrientes nitrógeno (N), fósforo (P) y potasio (K) son absorbidos por las plantas en función de los días transcurridos desde la emergencia del cultivo. Esto se hace ajustando modelos de regresión lineal, donde:

Variables independientes (X): PH, porcentaje humedad y absorción de nutrientes (N, P, K).
Variable dependiente (Y): Cantidad de fertilizante (Kg).
Esto permitirá predecir los valores de absorción futura y ajustar las recomendaciones de fertilización.
1.3	Preparación del Dataset
Los datos obtenidos son procesados, normalizados y organizados en un formato adecuado para el modelo de aprendizaje. 
Se organizan los datos históricos (entrenamiento) y los datos actuales (prueba). Representan cómo se comporta la absorción de nutrientes a lo largo del tiempo en situaciones previas.
En la función de la regresión lineal, se combinan los datos de entrenamiento con los de prueba para formar un conjunto de datos completo.
Esto asegura que los modelos de regresión tengan información suficiente para generalizar las predicciones, así como a su vez proporcionar recomendaciones personalizadas y estas no sean memorizadas.
1.4	Construcción y entrenamiento del modelo
Este paso se enfoca en desarrollar un modelo de aprendizaje supervisado que utiliza los datos históricos y actuales para capturar patrones de absorción de nutrientes (N, P, K) en el tiempo y así realizar predicciones útiles para el sistema experto.
El algoritmo elegido para este análisis es regresión lineal. Esta técnica es ideal porque permite modelar relaciones lineales entre la variable dependiente (absorción de nutrientes) y la variable independiente (días después de la emergencia del cultivo). La regresión lineal es adecuada porque: Proporciona una ecuación matemática simple y explicativa, es rápida de entrenar y evaluar y genera resultados interpretables, lo que es útil para ajustar recomendaciones agronómicas.
Se crean tres modelos de regresión lineal, uno para cada nutriente (N, P, K). Este modelo ajusta una relación entre los días y la absorción de nitrógeno. Captura la evolución del potasio en función del tiempo. Cada modelo ajusta los parámetros β1(pendiente) y β0 (intercepto) utilizando los datos de entrenamiento.
1.5	Generación de predicciones
Una vez entrenado, el modelo se utiliza para realizar predicciones basadas en nuevos datos del sensor.
Estas predicciones permiten estimar la absorción futura de nutrientes según el progreso del cultivo y la predicción es esencial para planificar y optimizar las estrategias de fertilización.
Primero se genera un rango de días, desde 0 hasta 120, dividido en 100 puntos. Esto simula la progresión del tiempo desde la emergencia hasta la madurez del cultivo. Se usan los modelos entrenados para predecir la absorción en el rango definido. Cada modelo predice la cantidad de un nutriente en función de los días. Las predicciones son vectores que contienen valores estimados de absorción para cada día en el rango.
1.6	Ajuste de coeficientes
Esta etapa consiste en calcular los coeficientes y el intercepto de la línea de regresión lineal. Estos valores definen la relación matemática entre los días de cultivo y la absorción de nutrientes (N, P, K). El ajuste de coeficientes ocurre durante el entrenamiento del modelo.
El ajuste se realiza utilizando un método fit. Este método minimiza el error cuadrático medio entre los valores reales (N, P, K) y los predichos para encontrar la mejor línea que ajuste los datos.
El coeficiente indica cuánto cambia la absorción del nutriente (N, P o K) por cada unidad de tiempo (días).
El intercepto es el valor de la absorción de nutrientes cuando el tiempo es igual a cero.
Por ejemplo: Si el coeficiente de modelo es 0.85, significa que la absorción de nitrógeno aumenta 0.85 mg/pl/día por cada día transcurrido. Si el intercepto es 10, significa que la absorción inicial (en el día 0) es de 10 mg/pl/día.
1.7	Validación y evaluación del modelo
Se evalúa el modelo para comprobar su precisión y confiabilidad. Esto se realiza comparando las predicciones con los datos reales no utilizados en el entrenamiento. Determina qué tan bien se ajusta el modelo a los datos históricos y cómo de precisas son las predicciones que genera.
Se utiliza el coeficiente de determinación R^2 (R-cuadrado), que mide la proporción de la variabilidad en la variable dependiente (absorción de nutrientes) explicada por el modelo.
Un valor de R^2 cercano a 1 indica que el modelo se ajusta muy bien a los datos.
Un valor cercano a 0 indica que el modelo no explica bien la variación de los datos.
Ejemplo: Si el R^2 para nitrógeno es 0.95, significa que el 95 porciento de la variabilidad en la absorción de nitrógeno está explicada por el modelo, lo cual indica una muy buena precisión.
Además del cálculo numérico, el sistema grafica los datos reales junto con las predicciones. Esto permite validar visualmente si la línea de regresión sigue la tendencia de los datos. Por lo que, Si los puntos reales (N, P, K) están cerca de las líneas predichas (N, P, K), el modelo es confiable.
El ajuste de coeficientes asegura que el modelo sea lo más preciso posible al encontrar la mejor línea de regresión para los datos.
La validación evalúa si ese ajuste realmente refleja la realidad (mediante R^2 y gráficas).
1.8	Visualización de resultados y representación de la regresión
Los resultados se grafican para representar las predicciones y los datos históricos. 
Datos históricos y valores ingresados por el usuario o el sensor se combinan para entrenar los modelos y generar predicciones futuras.
Se generan predicciones para un rango de días (0 a 120 días) utilizando los modelos de regresión lineal. Las predicciones y los datos históricos se grafican para representar cómo los modelos ajustan las absorciones de nutrientes y se añaden títulos, etiquetas y leyendas ayudan a interpretar la visualización. Dando como resultados gráficos que muestran cómo se ajustan las curvas de regresión (predicciones) en comparación con los datos históricos que facilita la validación visual del modelo y detecta posibles anomalías en los datos.

1.9	Generación de recomendaciones
A partir de las predicciones, el sistema genera recomendaciones prácticas para mejorar las condiciones del suelo o del cultivo. Se toman los valores actuales y genera recomendaciones específicas según la edad del cultivo, los niveles de NPK, la Humedad y el pH del suelo. 
Esta etapa utiliza la información proporcionada por el usuario (edad del cultivo, niveles de NPK, humedad, y pH) para generar recomendaciones específicas de fertilización. La lógica se implementa en una función y sigue un enfoque basado en reglas condicionales.
Según la edad del cultivo:
Las recomendaciones se adaptan a las etapas de crecimiento del cultivo:

•	< 30 días: Promoción del crecimiento inicial mediante aplicaciones de nitrógeno (N) y fósforo (P).
•	30-60 días: Apoyo al desarrollo de tubérculos con nitrógeno fraccionado y potasio (K).
•	60-90 días: Evitar exceso de nitrógeno para prevenir problemas de calidad.
•	> 90 días: Enfoque en la maduración y calidad final de los tubérculos.
Si la humedad es menor al 50 porciento, se sugiere incrementar la frecuencia de riego para optimizar la absorción de nutrientes.
Para un pH bajo, se recomienda aplicar cal para corregir la acidez.
Para un pH alto, se sugieren enmiendas ácidas como ácido sulfúrico.
Las recomendaciones incluyen fertilizantes específicos y cantidades estimadas en kg/ha.
Por lo que la recomendación es una lista detallada de acciones recomendadas para optimizar la fertilización y el manejo del cultivo según las condiciones actuales.

## 🛠️ Instalación

1. Clona el repositorio:
    git clone https://github.com/criseen7/SE.git
    cd SE

## 👥 Créditos

Desarrollado por Cristofer Raziel HB (https://github.com/criseen7).
