# NewsRoom
The application is divided in two sections:
- Graphic User Interface with 4 files and
- Back-end with 3 files.

### Graphic User Interface section
contains code for the front-end:
- [Welcome.py](Welcome.py) has the first window that the user will see when the application is run. It will show the current date and time and with a simple button a second small window will be display.
- [DB_GUI.py](DB_GUI.py) is in charged of asking the parameters needed to stablish a connection in Workbench, hiding the password itself. The button will save the values or skip this step in which case a message will be display informing the user that the parameters will need to be set manually. If any of the parameters entries is not fulfil and “SAVE” is pressed, a popup message will be display asking for the parameters. The windows will be showed until either the four parameters are fulfil or the “CANCEL” button is pressed.
- [News_GUI.py](News_GUI.py) which is still part of the Graphic User Interface section show in the upper part a series of labels, entries and buttons where the user select and enter the boundaries to obtain data from the API. The website field was added as clickable text which will redirect the user to the website of the news. The button that allow to save the news is located at the right side in the form of a checkbox.
- [Saves_GUI.py](Saves_GUI.py) is another window that the user could have access to. This one has the purpose of showing all the information saved previously from the user and will give the option to delete any portion of that information using the buttons in the last column. When the info is deleted from the database the window will be refreshed automatically with the updated table.
### The second section in the back-end:
[API.py](API.py) file must be supply with the boundaries from the [News_GUI.py](News_GUI.py) in order to perform the functions. This portion of the code concentrate the interactions with the API and deconstruct the data given by the API. I decided to give back to the user: brief, website, category, country and date and exclude the rest of the data. I took the Object Oriented approach because it allows me to break the project in essentially two sections:

Back-end with code to interact with API , Database and deal with the variables given by the user through the GUI.

Front-end with the code for all the windows that the user will see.

Database section is part of the back-end as well. Together with the parameters from the [DB_GUI.py](DB_GUI.py) will stablish a connection with a Database. It will manage the queries through Workbench such as:
- Creating a database / Checking if already exist
- Creating a table / Checking if already exist
- Sending new data to the Database
- Retrieving all the Database

All this information is send back to the user using the Graphic User Interface, specifically [Saves_GUI.py](Saves_GUI.py)

