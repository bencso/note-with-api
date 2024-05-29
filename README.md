# Flask Notes App Documentation

This application uses the Flask web framework to create a simple notes app. The notes are stored in cookies, so they persist across user sessions until the user decides to delete a note or clear their browser cookies.

## Code Overview

### Imports

```python
from flask import Flask, redirect , request, make_response, render_template
```

The application uses Flask for the web server, and several helper functions from Flask for handling requests and responses. These include redirecting users to different pages, accessing request data (like form parameters and cookies), creating HTTP responses, and rendering HTML templates.

### Initialize Flask

```python
app = Flask(__name__)
```

This line creates a new Flask web application.

### Routes and Handlers

There are five URL routes defined in this app:

1. `@app.get("/")`: This route displays all notes by reading the titles and contents from the cookies and passing them to the main.html template.

2. `@app.get("/titles")`: This route returns all note titles.

3. `@app.get("/search/<titles>")`: This route displays a specific note's content. The note title is provided in the URL path.

4. `@app.post("/")`: This route handles the form submission for creating a new note. It sets a new cookie with the note title as the key and the note content as the value.

5. `@app.post("/delete")`: This route deletes a specified note by setting its cookie value to an empty string and its expiration date to 0.

## Running the App

To run this app, you need to have Flask installed in your Python environment. You can then run the app by running the Python file in your terminal.

## Notes

- The application uses cookies to store notes, which means that the notes are stored in the user's browser and persist across sessions until the user clears their cookies or deletes a specific note.
- The application uses the `render_template` function to render HTML templates, which should be stored in a `templates` directory in the same directory as the Python script.
- To delete notes, the note title is passed as a query parameter in the delete route.
- Notes are displayed in the main route ("/") and can also be searched for using the search route.