# Dashboard_cancer

This is a code that creates a dashboard in Streamlit from TSV files located in three folders, all contained inside a zip file.

To run it, use Streamlit ("streamlit run Dashboard.py" from the console). It creates a dashboard based on the Chile cancer statistics tables, which are located in different folders. If you move the tables to a different location, you must update the file paths in the code. If you want to add a new table, it must follow the format of the existing tables and its name must be added as a value, while the name it will have in the dashboard must be added as a key in the respective dictionary. This code is not perfect (at least I am not entirely satisfied with it). It could probably be modified to be more efficient. However, the important thing is that it works 😀👍, and has few requirements. I'm not sure if the functions for the Cleveland dot plots at the end of the code can be improved (probably yes). 
If I feel like it, I will improve it in the future, perhaps making it easier to enter new tables of information with some function that allows non-programmers to do so, but for now, it will be fine as is. 

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
