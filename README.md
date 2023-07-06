# Dashboard_cancer

This is a code that creates a dashboard in Streamlit from TSV files located in three folders, all contained within a zip file.

To run this, use Streamlit ("streamlit run Dashboard.py" from the console). It creates a dashboard based on cancer statistics tables from Chile, which are located in different folders. If you move the tables to a different location, you need to update the file paths in the code. If you want to add a new table, it should follow the format of the existing tables and its name should be added as a value, while the name it will have in the dashboard should be added as a key in the respective dictionary. This code is not perfect (at least I'm not entirely satisfied with it). Could probably be modified to be more efficient. However, the important thing is that it works without errors, and it has few requirements. I'm not sure if the functions for the Cleveland dot plots at the end of the code can be improved or integrated with the rest of the code (probably yes). This is the first time I've written a function to create that type of graph. ':D

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

   pip install pmdarima

   pip install plotly

For Mac, it is recommended to use a virtual environment for Python projects, such as virtualenv or conda, to avoid conflicts between different projects and library versions.
