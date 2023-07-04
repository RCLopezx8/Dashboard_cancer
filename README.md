# Spanish:

# Dashboard_cancer
Es un código en python que crea un dashboard en streamlit a partir de archivos tsv que se encuentran en tres carpetas, todo va dentro del archivo zip.

Esta cosa puede ser lanzada con streamlit ("streamlit run Dashboard.py" desde consola), crea un dashboard que nace a partir de tablas con estadísticas del cáncer en Chile, las cuales están colocadas en diferentes carpetas, en caso de mover de lugar las tablas, deben ser colocadas las nuevas posiciones de las tablas en el código, si se desea agregar una nueva tabla, debe seguir el formato de las otras y añadirse su nombre como value y el nombre que tendrá en el dashboard como key en su respectivo dictionary. No es un código perfecto (Al menos yo no estoy del todo conforme con él), y es que fue creado a partir del reciclaje de anteriores códigos (básicamente es un monstruo de Frankestein) que probablemente puede ser modificado para ser más eficiente, pero el caso es que funciona sin errores, es escalable y tiene pocas exigencias. Desconosco si las funciones de los cleveland dot plots al final del código son mejorables o unificables con el resto del código (probablemente sí), es que es la primera vez que escribo una función para crear ese tipo de gráficos ':D

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


# English:

# Dashboard_cancer

This is a code in python that creates a dashboard in Streamlit from TSV files located in three folders, all contained within a zip file.

To run this, use Streamlit ("streamlit run Dashboard.py" from the console). It creates a dashboard based on cancer statistics tables from Chile, which are located in different folders. If you move the tables to a different location, you need to update the file paths in the code. If you want to add a new table, it should follow the format of the existing tables and its name should be added as a value, while the name it will have in the dashboard should be added as a key in the respective dictionary. This code is not perfect (at least I'm not entirely satisfied with it). It was created by recycling previous codes (basically, it's a Frankenstein's monster) and could probably be modified to be more efficient. However, the important thing is that it works without errors, it's scalable, and it has few requirements. I'm not sure if the functions for the Cleveland dot plots at the end of the code can be improved or integrated with the rest of the code (probably yes). This is the first time I've written a function to create that type of graph. ':D

--> The code's requirements on Linux are quite simple and can be installed by running the following commands in the console:

sudo pip install pandas
sudo pip install streamlit
sudo pip install pmdarima
sudo pip install plotly


--> To install the requirements on a Mac through the command line:

Install pip according to the instructions you find on Google.

Once pip is installed, execute the following commands one by one in the Terminal:

   pip install pandas

   pip install streamlit

   To install pmdarima:

   pip install pmdarima

   pip install plotly

For Mac, it is recommended to use a virtual environment for Python projects, such as virtualenv or conda, to avoid conflicts between different projects and library versions.
