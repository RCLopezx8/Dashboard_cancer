''' Create a dashboard
by Rodrigo Celis López
'''
# Llamamos las librerias:
import pandas as pd
import streamlit as st
import pmdarima as pm
import plotly.graph_objects as go

# Definir las rutas de las carpetas y los diccionarios
carpeta_tendencia_mortalidad = "Tablas_tendencia_mortalidad"
carpeta_AVPP = "carpeta_AVPP"

mapa_tendencia_mortalidad_cancer = {
    "Cáncer Gástrico": "Tendencia_de_Mortalidad_por_Cancer_Gastrico.tsv",
    "Cáncer de Colon": "Tendencia_Mortalidad_Cancer_Colon.tsv",
    "Cáncer de Mama": "Tendencia_Mortalidad_Cáncer_Mama.tsv",
    "Cáncer de Traquea, Bronquio y Pulmón": "Tendencia_Mortalidad_Cancer_Traquea_Bronquio_Pulmon.tsv",
    "Cáncer de Vesícula": "Tendencia_Mortalidad_Cáncer_Vesícula.tsv",
    "Cáncer Cervicouterino": "Tendencia_Mortalidad_Cancer_Cervicouterino.tsv",
    "Cáncer de Prostata": "Tendencia_Mortalidad_Cáncer_Próstata.tsv",
    "Neoplasias Malignas": "Tendencia_Mortalidad_Neoplasias_Malignas.tsv"
}

mapa_AVPP_cancer = {
    "Cáncer Gástrico": "AVPP_cancer_gastrico.tsv",
    "Cáncer de Colon": "AVPP_cancer_colon.tsv",
    "Cáncer de Mama": "AVPP_cancer_mama.tsv",
    "Cáncer de Traquea, Bronquio y Pulmón": "AVPP_cancer_traquea_bronquio_pulmon.tsv",
    "Cáncer de Vesícula": "AVPP_cancer_vesicula.tsv",
    "Cáncer Cervicouterino": "AVPP_cancer_cervicouterino.tsv",
    "Cáncer de Prostata": "AVPP_cancer_prostata.tsv",
    "Neoplasias Malignas": "AVPP_Neoplasias_Malignas.tsv"
}

# Función para cargar los datos de un archivo tsv
def cargar_datos(nombre_archivo):
    return pd.read_csv(nombre_archivo, delimiter="\t", decimal=",")

# Función para graficar la tendencia de mortalidad por tipo de cáncer
def graficar_tendencia_mortalidad(datos):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_ambos"], name="Tasa ajustada (ambos)", line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_hombres"], name="Tasa ajustada (hombres)", line=dict(color='green')))
    fig.add_trace(go.Scatter(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_mujeres"], name="Tasa ajustada (mujeres)", line=dict(color='red')))
    fig.update_layout(title="Tendencia de mortalidad", xaxis_title="Año", yaxis_title="Tasa ajustada")
    st.plotly_chart(fig)

# Función para graficar la tendencia de mortalidad por tipo de cáncer
def graficar_tendencia_AVPP(datos):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_ambos"], name="Tasa ajustada (ambos)", line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_hombres"], name="Tasa ajustada (hombres)", line=dict(color='green')))
    fig.add_trace(go.Scatter(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_mujeres"], name="Tasa ajustada (mujeres)", line=dict(color='red')))
    fig.update_layout(title="Tendencia AVPP", xaxis_title="Año", yaxis_title="Tasa ajustada")
    st.plotly_chart(fig)

# Función para graficar la comparación de la tendencia de mortalidad entre hombres y mujeres
def graficar_comparacion_mortalidad(datos):
    fig = go.Figure(data=[
        go.Bar(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_hombres"], name="Hombres", marker_color='blue'),
        go.Bar(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_mujeres"], name="Mujeres", marker_color='red')
    ])
    fig.update_layout(title="Comparación de tendencia de mortalidad entre hombres y mujeres", xaxis_title="Año", yaxis_title="Tasa ajustada")
    st.plotly_chart(fig)

# Función para graficar la comparación de la tendencia de mortalidad entre hombres y mujeres
def graficar_comparacion_AVPP(datos):
    fig = go.Figure(data=[
        go.Bar(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_hombres"], name="Hombres", marker_color='blue'),
        go.Bar(x=datos["Año_de_defunción"], y=datos["Tasa_ajustada_mujeres"], name="Mujeres", marker_color='red')
    ])
    fig.update_layout(title="Comparación AVPP entre hombres y mujeres", xaxis_title="Año", yaxis_title="Tasa ajustada")
    st.plotly_chart(fig)

# Función para predecir la tendencia de mortalidad utilizando ARIMA
def predecir_tendencia_mortalidad(datos):
    datos_hombres = datos["Tasa_ajustada_hombres"]
    datos_mujeres = datos["Tasa_ajustada_mujeres"]

    # Ajustar el modelo ARIMA para los datos de hombres
    modelo_hombres = pm.auto_arima(datos_hombres)
    prediccion_hombres = modelo_hombres.predict(n_periods=5)

    # Ajustar el modelo ARIMA para los datos de mujeres
    modelo_mujeres = pm.auto_arima(datos_mujeres)
    prediccion_mujeres = modelo_mujeres.predict(n_periods=5)

    # Crear el gráfico de líneas para las predicciones
    años_prediccion = list(range(2024, 2029))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=años_prediccion, y=prediccion_hombres, name="Predicción Hombres"))
    fig.add_trace(go.Scatter(x=años_prediccion, y=prediccion_mujeres, name="Predicción Mujeres"))
    fig.update_layout(title="Predicción de tendencias entre años 2024 y 2028", xaxis_title="Año", yaxis_title="Tasa Ajustada")
    st.plotly_chart(fig)

# Función para predecir la tendencia de mortalidad utilizando ARIMA
def predecir_tendencia_AVPP(datos):
    datos_hombres = datos["Tasa_ajustada_hombres"]
    datos_mujeres = datos["Tasa_ajustada_mujeres"]

    # Ajustar el modelo ARIMA para los datos de hombres
    modelo_hombres = pm.auto_arima(datos_hombres)
    prediccion_hombres = modelo_hombres.predict(n_periods=5)

    # Ajustar el modelo ARIMA para los datos de mujeres
    modelo_mujeres = pm.auto_arima(datos_mujeres)
    prediccion_mujeres = modelo_mujeres.predict(n_periods=5)

    # Crear el gráfico de líneas para las predicciones
    años_prediccion = list(range(2024, 2029))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=años_prediccion, y=prediccion_hombres, name="Predicción Hombres"))
    fig.add_trace(go.Scatter(x=años_prediccion, y=prediccion_mujeres, name="Predicción Mujeres"))
    fig.update_layout(title="Predicción AVPP entre años 2024 y 2028", xaxis_title="Año", yaxis_title="Tasa Ajustada")
    st.plotly_chart(fig)

# Función para mostrar el dashboard
def mostrar_dashboard():
    st.title("Tendencias de Mortalidad y Años de Vida Potencialmente Perdidos (AVPP) por tipo de cáncer")
    opcion_datos = st.sidebar.selectbox("Selecciona el tipo de datos", ("Tendencias de Mortalidad", "Años de Vida Potencialmente Perdidos"))
    tipo_cancer = st.sidebar.selectbox("Selecciona el tipo de cáncer", list(mapa_tendencia_mortalidad_cancer.keys()))

    if opcion_datos == "Tendencias de Mortalidad":
        archivo_tendencia_mortalidad = mapa_tendencia_mortalidad_cancer[tipo_cancer]
        datos_tendencia_mortalidad = cargar_datos(carpeta_tendencia_mortalidad + "/" + archivo_tendencia_mortalidad)

        st.header("Tendencias de Mortalidad por tipo de cáncer: " + tipo_cancer)
        graficar_tendencia_mortalidad(datos_tendencia_mortalidad)
        graficar_comparacion_mortalidad(datos_tendencia_mortalidad)

        # Llamada a la función predecir_tendencia_mortalidad
        predecir_tendencia_mortalidad(datos_tendencia_mortalidad)

    else:
        archivo_AVPP = mapa_AVPP_cancer[tipo_cancer]
        datos_AVPP = cargar_datos(carpeta_AVPP + "/" + archivo_AVPP)

        st.header("Años de Vida Potencialmente Perdidos (AVPP) por tipo de cáncer: " + tipo_cancer)
        graficar_tendencia_AVPP(datos_AVPP)
        graficar_comparacion_AVPP(datos_AVPP)

        # Llamada a la función predecir_tendencia_mortalidad
        predecir_tendencia_AVPP(datos_AVPP)

# Ejecutar el dashboard
mostrar_dashboard()

def create_cleveland_plot(ruta_archivo, region_column, x_column, y_column, x_label, title):
    # Leer el archivo TSV en un DataFrame de pandas
    data = pd.read_csv(ruta_archivo, sep="\t")

    # Filtrar los datos excluyendo la última fila (suma total)
    data = data.iloc[:-1]

    # Obtener las columnas para los ejes Y, X inferior y X superior
    regiones = data[region_column]
    x_values = data[x_column]
    y_values = data[y_column]

    # Crea el gráfico de puntos de Cleveland con Plotly
    fig = go.Figure()

    # Configura el eje Y con las regiones
    fig.update_yaxes(tickvals=list(range(len(regiones))), ticktext=regiones, autorange="reversed")

    # Configura el eje X inferior con los valores de X
    fig.add_trace(go.Scatter(x=x_values, y=list(range(len(regiones))), mode='markers', marker=dict(color='red'), name=x_label))

    # Configura el eje X superior con los valores de Y
    fig.add_trace(go.Scatter(x=y_values, y=list(range(len(regiones))), mode='markers', marker=dict(color='blue'), name=y_column))

    # Los ejes
    fig.update_xaxes(title=x_label)
    fig.update_layout(title=title)

    # Mostrar el gráfico con Streamlit
    st.plotly_chart(fig)

def main():
    # Ruta al archivo TSV con los datos
    ruta_archivo = "Distribucion/Distribución_porcentual_fallecidos_menores_80_años_tasa_AVPP_tipo_cáncer_sexo.tsv"

    create_cleveland_plot(ruta_archivo, "Tipo de cáncer", "Fallecidos cualquier edad hombres", "Fallecidos cualquier edad mujeres", "Fallecidos cualquier edad", "Resumen de fallecidos por tipo de cáncer")

if __name__ == "__main__":
    main()

def create_cleveland_plot(ruta_archivo, region_column, x_column, y_column, x_label, title):
    # Leer el archivo TSV en un DataFrame de pandas
    data = pd.read_csv(ruta_archivo, sep="\t")

    # Filtrar los datos excluyendo la última fila (suma total)
    data = data.iloc[:-1]

    # Obtener las columnas para los ejes Y, X inferior y X superior
    regiones = data[region_column]
    x_values = data[x_column]
    y_values = data[y_column]

    # Crear el gráfico de puntos de Cleveland con Plotly
    fig = go.Figure()

    # Configurar el eje Y con las regiones
    fig.update_yaxes(tickvals=list(range(len(regiones))), ticktext=regiones, autorange="reversed")

    # Configurar el eje X inferior con los valores de X
    fig.add_trace(go.Scatter(x=x_values, y=list(range(len(regiones))), mode='markers', marker=dict(color='red'), name=x_label))

    # Configurar el eje X superior con los valores de Y
    fig.add_trace(go.Scatter(x=y_values, y=list(range(len(regiones))), mode='markers', marker=dict(color='blue'), name=y_column))

    # Etiquetas de los ejes
    fig.update_xaxes(title=x_label)
    fig.update_layout(title=title)

    # Mostrar el gráfico con Streamlit
    st.plotly_chart(fig)

def main():
    # Ruta al archivo TSV con los datos
    ruta_archivo = "Distribucion/Distribución_porcentual_fallecidos_menores_80_años_tasa_AVPP_región_residencia_sexo.tsv"

    create_cleveland_plot(ruta_archivo, "Región residencia", "Fallecidos cualquier edad hombres", "Fallecidos cualquier edad mujeres", "Fallecidos cualquier edad", "Resumen fallecimientos por Región de residencia")

if __name__ == "__main__":
    main()
