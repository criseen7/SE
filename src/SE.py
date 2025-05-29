import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def RegresionLineal():
    # Datos de entrenamiento
    dias_entrenamiento = [37.5, 52.5, 67.5, 82.5, 97.5, 112.5]  # Promedio de intervalos de días
    n_abs_entrenamiento = [50, 90, 115, 40, 20, 0]  # Absorción de N (mg/pl/día)
    k_abs_entrenamiento = [60, 140, 140, 60, 20, 0]  # Absorción de K (mg/pl/día)
    p_abs_entrenamiento = [15, 25, 28, 13, 7, 0]  # Absorción de P (mg/pl/día)

    # Datos de prueba (valores actuales y los ingresados por el usuario)
    dias_prueba = [30, 60, 90, 110, edad_actual]  # Días actuales más los del usuario
    n_abs_prueba = [70, 100, 30, 10, npk_actual['N']]  # N actuales más los del usuario
    k_abs_prueba = [80, 120, 50, 15, npk_actual['K']]  # K actuales más los del usuario
    p_abs_prueba = [20, 25, 10, 5, npk_actual['P']]  # P actuales más los del usuario
    # Combinar datos de entrenamiento y prueba
    dias_total = np.array(dias_entrenamiento + dias_prueba).reshape(-1, 1)
    n_total = np.array(n_abs_entrenamiento + n_abs_prueba)
    k_total = np.array(k_abs_entrenamiento + k_abs_prueba)
    p_total = np.array(p_abs_entrenamiento + p_abs_prueba)

    # Ajustar modelos de regresión lineal
    model_n = LinearRegression().fit(dias_total, n_total)
    model_k = LinearRegression().fit(dias_total, k_total)
    model_p = LinearRegression().fit(dias_total, p_total)

    # Predicciones en el rango completo
    dias_pred = np.linspace(0, 120, 100).reshape(-1, 1)
    n_pred = model_n.predict(dias_pred)
    k_pred = model_k.predict(dias_pred)
    p_pred = model_p.predict(dias_pred)

    # Métricas R²
    r2_n = r2_score(n_total, model_n.predict(dias_total))
    r2_k = r2_score(k_total, model_k.predict(dias_total))
    r2_p = r2_score(p_total, model_p.predict(dias_total))

    # Resultados
    print(f"N: Coeficiente = {model_n.coef_[0]:.2f}, Intercepto = {model_n.intercept_:.2f}, R² = {r2_n:.3f}")
    print(f"K: Coeficiente = {model_k.coef_[0]:.2f}, Intercepto = {model_k.intercept_:.2f}, R² = {r2_k:.3f}")
    print(f"P: Coeficiente = {model_p.coef_[0]:.2f}, Intercepto = {model_p.intercept_:.2f}, R² = {r2_p:.3f}")

    # Gráfico combinado
    plt.figure(figsize=(10, 6))
    plt.plot(dias_pred, n_pred, label="N (Regresión)", color='yellow')
    plt.plot(dias_pred, k_pred, label="K (Regresión)", color='blue')
    plt.plot(dias_pred, p_pred, label="P (Regresión)", color='green')

    plt.scatter(dias_total, n_total, label="N (Datos)", color='orange', marker='o')
    plt.scatter(dias_total, k_total, label="K (Datos)", color='purple', marker='x')
    plt.scatter(dias_total, p_total, label="P (Datos)", color='lime', marker='s')

    plt.title("Regresión Lineal: Absorción de Nutrientes en Cultivo de Papa")
    plt.xlabel("Días después de Emergencia")
    plt.ylabel("Absorción (mg/pl/día)")
    plt.legend()
    plt.grid()
    plt.show()

# Función de recomendaciones permanece igual
def recomendaciones_fertilizacion(dias, npk, humedad, ph):
    # Recomendaciones basadas en la edad del cultivo y condiciones actuales
    if dias < 30:
        if npk['N'] < 80:
            print("Recomendación: Aplicar nitrógeno en bandas o lateralmente para estimular el crecimiento temprano.")
            print("Fertilizante recomendado: 20-0-0 (Agua amoníaco) o 32-0-0 (Urea y nitrato de amonio).")
            print("Cantidad recomendada: 50-60 kg/ha.")
        if npk['P'] < 20:
            print("Recomendación: Aplicar fósforo para favorecer el desarrollo temprano y la formación de tubérculos.")
            print("Fertilizante recomendado: 8-24-0 (Ortofosfato de amonio) o 9-30-0 (Ortofosfato de amonio).")
            print("Cantidad recomendada: 30-40 kg/ha.")
    elif 30 <= dias < 60:
        if npk['N'] < 120:
            print("Recomendación: Realizar aplicaciones fraccionadas de nitrógeno y considerar la inyección por riego.")
            print("Fertilizante recomendado: 28-0-0 (Urea y nitrato de amonio).")
            print("Cantidad recomendada: 40-50 kg/ha.")
        if npk['K'] < 100:
            print("Recomendación: Asegurarse de que haya suficiente potasio para el desarrollo adecuado de los tubérculos.")
            print("Fertilizante recomendado: 0-0-30 (Carbonato de potasio) o 8-8-8 (Mezcla de amoniaco).")
            print("Cantidad recomendada: 30-40 kg/ha.")
    elif 60 <= dias < 90:
        if npk['N'] > 150:
            print("Recomendación: Evitar dosis excesivas de nitrógeno para prevenir crecimiento vegetativo excesivo.")
            print("Fertilizante recomendado: 20-0-0 (Nitrato de amonio) o 17-0-0 (Nitrato de calcio y amonio).")
            print("Cantidad recomendada: 30-40 kg/ha.")
        if humedad < 60:
            print("Recomendación: Asegurar una humedad adecuada en el suelo para evitar estrés hídrico.")
    else:
        if npk['P'] < 40:
            print("Recomendación: Aplicar fósforo adicional para asegurar una adecuada maduración.")
            print("Fertilizante recomendado: 10-34-0 (Ortofosfato y polifosfatos de amonio).")
            print("Cantidad recomendada: 20-30 kg/ha.")
        if ph > 7:
            print("Recomendación: Considerar la aplicación de ácido sulfúrico para corregir el pH del suelo.")
    
    if ph < 5.5:
        print("Recomendación: El pH del suelo está bajo. Considerar la aplicación de cal.")
    elif ph > 7.5:
        print("Recomendación: El pH está alto. Considerar la aplicación de enmiendas ácidas como ácido sulfúrico.")
    if humedad < 50:
        print("Recomendación: Aumentar la frecuencia de riego para asegurar una buena absorción de nutrientes.")

# Ejemplo de uso
npk_actual = {'N': 12, 'K': 17, 'P': 35}
humedad_actual = 13.60
ph_actual = 3
edad_actual = 0
recomendaciones_fertilizacion(edad_actual, npk_actual, humedad_actual, ph_actual)
