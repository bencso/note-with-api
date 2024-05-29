# Flask Notes App Documentation

This application uses the Flask web framework to create a simple notes app. The notes are stored in cookies, so they persist across user sessions until the user decides to delete a note or clear their browser cookies.

🇭🇺 Ez az alkalmazás a Flask webes keretrendszert használja egy egyszerű jegyzetalkalmazás létrehozásához. A jegyzeteket sütik tárolják, így azok a felhasználói munkameneteken keresztül megmaradnak, amíg a felhasználó úgy nem dönt, hogy törli a jegyzetet vagy törli a böngésző sütiket.

## Code Overview

### Imports

```python
from flask import Flask, redirect , request, make_response, render_template
```

The application uses Flask for the web server, and several helper functions from Flask for handling requests and responses. These include redirecting users to different pages, accessing request data (like form parameters and cookies), creating HTTP responses, and rendering HTML templates.

🇭🇺 Az alkalmazás Flask-ot használ a webkiszolgálóhoz, és a Flask számos segédfüggvényét a kérések és válaszok kezeléséhez. Ezek közé tartozik a felhasználók átirányítása különböző oldalakra, a kérési adatok (például űrlapparaméterek és cookie-k) elérése, HTTP-válaszok létrehozása és HTML-sablonok megjelenítése.

### Initialize Flask

```python
app = Flask(__name__)
```

This line creates a new Flask web application.

🇭🇺 Ez a sor egy új Flask webalkalmazást hoz létre.


### Routes and Handlers

There are five URL routes defined in this app:

1. `@app.get("/")`: This route displays all notes by reading the titles and contents from the cookies and passing them to the main.html template.

2. `@app.get("/titles")`: This route returns all note titles.

3. `@app.get("/search/<titles>")`: This route displays a specific note's content. The note title is provided in the URL path.

4. `@app.post("/")`: This route handles the form submission for creating a new note. It sets a new cookie with the note title as the key and the note content as the value.

5. `@app.post("/delete")`: This route deletes a specified note by setting its cookie value to an empty string and its expiration date to 0.

🇭🇺 Ebben az alkalmazásban öt URL-útvonal van definiálva:

1. `@app.get("/")`: Ez az útvonal az összes jegyzetet megjeleníti a címek és tartalmak cookie-kból történő beolvasásával és a main.html sablonba történő átadásával.

2. `@app.get("/titles")`: Ez az útvonal visszaadja az összes jegyzet címét.

3. `@app.get("/search/<címek>")`: Ez az útvonal egy adott jegyzet tartalmát jeleníti meg. A jegyzet címe az URL elérési útvonalában van megadva.

4. `@app.post("/")`: Ez az útvonal kezeli az új jegyzet létrehozásához szükséges űrlap beküldését. Új cookie-t állít be, amelynek kulcsa a jegyzet címe, értéke pedig a jegyzet tartalma.

5. `@app.post("/delete")`: Ez az útvonal törli a megadott jegyzetet úgy, hogy a cookie értékét üres karakterláncra, a lejárati dátumát pedig 0-ra állítja.

## Running the App

To run this app, you need to have Flask installed in your Python environment. You can then run the app by running the Python file in your terminal.

🇭🇺 Az alkalmazás futtatásához a Python környezetedben telepített Flask-ra van szükséged. Ezután az alkalmazást a Python fájl futtatásával futtathatja a termináljában.

## Notes

- The application uses cookies to store notes, which means that the notes are stored in the user's browser and persist across sessions until the user clears their cookies or deletes a specific note.
- The application uses the `render_template` function to render HTML templates, which should be stored in a `templates` directory in the same directory as the Python script.
- To delete notes, the note title is passed as a query parameter in the delete route.
- Notes are displayed in the main route ("/") and can also be searched for using the search route.

🇭🇺 
- Az alkalmazás cookie-kat használ a jegyzetek tárolására, ami azt jelenti, hogy a jegyzetek a felhasználó böngészőjében tárolódnak, és mindaddig fennmaradnak a munkameneteken keresztül, amíg a felhasználó nem törli a cookie-kat vagy nem törli az adott jegyzetet.
- Az alkalmazás a `render_template` függvényt használja a HTML sablonok megjelenítésére, amelyeket a Python szkripttel azonos könyvtárban lévő `templates` könyvtárban kell tárolni.
- A jegyzetek törléséhez a jegyzet címe a törlési útvonalban lekérdezési paraméterként kerül átadásra.
- A jegyzetek a fő útvonalon ("/") jelennek meg, és a keresési útvonalon is kereshetők.