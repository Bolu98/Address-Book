# Getting Started with the Address-Book API

Download to the entire folder to your local machine


## Running the API

Ensure a recent version of Python is installed computer (the project was tested using version `3.8.1`. 

Open a terminal window and navigate to the `api` directory. 

Set up a virtual environment and download the required packages using `pip install -r requirements.txt` (assuming pip is already installed on your machine). 

Navigate back to the Address-Book directory and run the flask server using `npm run start-flask-api`. Make a note of the URL provided

Open a new terminal window and navigate to the `api` directory. Activate the virtual environment and run the react frontend using the command `npm start`. This automatically opens up the address book's web page


## Running the unit tests

To test that the server is running correctly, open a new terminal window and navigate to the `api` directory.

Activate the virtual environment and run the tests using `python test.py`.

Passing all 3 unit tests confirms the API runs correctly


## Sending API requests and visualising the results

Requests can be made to the API with cURL requests using the URL provided when the flask server was run. The arguments for the requests are `First name`, `Last name`, and `Phone number`.

### Add an entry

Run a cURL POST command, ensuring that the correct URL is used. For example `curl http://127.0.0.1:5000/addEntry -d "First name=John" -d "Last name=Doe" -d "Phone number=123" -X POST`

Note that the `Phone number` argument is optional but `First name` and `Last name` are mandatory. The response is the added entry or an error message.

### Remove an entry

Run a cURL POST command, ensuring that the correct URL is used. For example `curl http://127.0.0.1:5000/removeEntry -d "First name=John" -d "Last name=Doe" -d "Phone number=123" -X POST`.

The response is the removed entry or an error message.

### Sort the list

Run a cURL GET command, ensuring that the correct URL is used. For example `curl http://127.0.0.1:5000/retrieveSortedList/f -X GET` to sort by first name and `curl http://127.0.0.1:5000/retrieveSortedList/l -X GET` to sort by last name.

The response is the sorted list or an error message.

### Show exact or partial matches

Run a cURL GET command, ensuring the correct URL is used. For example `curl http://127.0.0.1:5000/retrieveMatches/jo -X GET` to show exact or partial matches to the string "jo".

The response is the list with matches or an error message.


## Visualising the address book

After an entry is added or removed, the full address list is displayed by clicking the relevant button on the webpage. 

Similarly, after a sort or match command is sent successfully, the results can also be viewed on the web page by clicking the relevant button.

## Limitations and extensions

Due to timing constraints, some features were omitted from this project that could improve functionality.

Entries in the address book are stored in memory whilst the server is running. This could be improved by storing the address list in an sqlite or mongo-DB database and querying the entries when needed. 

Instead of sending terminal cURL requests, fetch and post requests could be performed by the react frontend and components could be included to allow the user input arguments.

Additional arguments such as email addresses, pictures or voice clips could be added to the address book entries to form more complete entries.
