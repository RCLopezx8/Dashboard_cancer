# Dashboard_cancer
Es un código que crea un dashboard en streamlit a partir de archivos tsv que se encuentran en tres carpetas.

by Rodrigo Celis López

Esta cosa puede ser lanzada con streamlit ("streamlit run Dashboard.py" desde consola), crea un dashboard que nace a partir de tablas con estadísticas del cáncer en Chile, las cuales están colocadas en diferentes carpetas, en caso de mover de lugar las tablas, deben ser colocadas las nuevas posiciones de las tablas en el código, si se desea agregar una nueva tabla, debe seguir el formato de las otras y añadirse su nombre como value y el nombre que tendrá en el dashboard como key en su respectivo dictionary. No es un código perfecto (Al menos yo no estoy del todo conforme con él), y es que fue creado a partir del reciclaje de anteriores códigos (básicamente es un monstruo de Frankestein) que probablemente puede ser modificado para ser más eficiente, pero el caso es que funciona sin errores, es escalable y tiene pocas exigencias. Desconosco si las funciones de los cleveland dot plots al final del código son mejorables o unificables con el resto del código (probablemente sí), es que es la primera vez que escribo una función para crear este tipo de gráficos ':D

--> Las exigencias del código en Linux son bastante sencillas y se pueden instalar escribiendo los siguientes comandos por consola:

sudo pip install pandas
sudo pip install streamlit
sudo pip install pmdarima
sudo pip install plotly


--> Para instalar las exigencias en una Mac a través de la línea de comandos:

Instala pip según lo que diga google.

Una vez esté pip instalado, ejecuta los siguientes comandos en la Terminal uno por uno:

   pip install pandas

   pip install streamlit

   Para instalar pmdarima:

   pip install pmdarima

   pip install plotly

Para Mac es recomendable utilizar un entorno virtual para cosas con Python, como virtualenv o conda, para evitar conflictos entre diferentes proyectos y versiones de las bibliotecas.
'''
