# note-with-api 📝🍪

> Flask-alapú jegyzetalkalmazás cookie tárolással - Iskolai API gyakorlás

## 🎯 Projekt célja

Ez egy egyszerű jegyzetalkalmazás, amely Flask keretrendszert használ, és kifejezetten API gyakorlás céljából készült iskolai projektként. A jegyzetek cookie-kban tárolódnak, így megmaradnak a böngésző újraindítása után is, amíg a felhasználó nem törli őket.

## ✨ Funkciók

- 📝 **Jegyzet létrehozása** - Cím és tartalom megadásával új jegyzet rögzítése
- 📋 **Jegyzetek listázása** - Összes mentett jegyzet megtekintése
- 🔍 **Jegyzet keresése** - Konkrét jegyzet megkeresése cím alapján
- 🗑️ **Jegyzet törlése** - Egyedi jegyzet eltávolítása a cookie-kból
- 🍪 **Cookie alapú tárolás** - Adatok megmaradása böngésző-sessionon keresztül

## 🛠️ Technológiák

- **Flask** - Python framework
- **Python** - Programozási nyelv
- **HTML templates** - Jinja2 template engine

## 🔧 API útvonalak

### GET `/`
Az összes jegyzet megjelenítése a főoldalon. A címek és tartalmak cookie-kból töltődnek be és kerülnek átadásra a `main.html` sablonnak.

### GET `/titles`
Az összes jegyzet címének visszaadása.

### GET `/search/<titles>`
Konkrét jegyzet tartalmának megjelenítése. A jegyzet címe az URL-ben kerül megadásra.

### POST `/`
Új jegyzet létrehozása. A jegyzet címe lesz a cookie kulcsa, a tartalom pedig az értéke.

### POST `/delete`
Megadott jegyzet törlése úgy, hogy a cookie értékét üres stringre állítja és a lejárati dátumot 0-ra.

## 💭 Fejlesztési folyamat

Ez egy iskolai projekt volt, amelynek célja a Flask framework és az API-k működésének gyakorlása. A cookie-alapú tárolás egyszerű megoldást kínál adatmegőrzésre adatbázis nélkül, így tökéletes oktatási célokra.

## 🎓 Tanulási célok

A projekt során gyakoroltam:
- Flask framework használata
- RESTful API útvonalak tervezése és implementálása
- HTTP kérések és válaszok kezelése
- Cookie-alapú adattárolás
- HTML template renderelés (Jinja2)
- Python webfejlesztés alapjai

## 🚀 Futtatás

A projekt futtatásához szükséges lépések:

1. Flask telepítése: `pip install flask`
2. Python fájl futtatása: `python app.py`
3. Böngészőben megnyitni: `http://localhost:5000`

**Megjegyzés:** A HTML sablonokat a `templates` mappában kell tárolni, a Python scripttel azonos könyvtárban.

## 🤝 Közreműködés

Ez egy lezárt iskolai projekt, amely API gyakorlás céljából készült.

---

**Státusz:** ✅ Befejezett

---

## 💭 Megjegyzések

Ez az alkalmazás kifejezetten Flask és API gyakorlás céljából készült iskolai feladatként. A cookie-alapú tárolás egyszerű, de hatékony megoldást nyújt kis mennyiségű adat böngészőben történő megőrzésére, adatbázis használata nélkül.

---

**⭐ Ha tetszik a projekt, örülök egy csillagnak!**

***

Kész! Folytassuk a következővel? 🚀
