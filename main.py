from flask import Flask, redirect , request, make_response,render_template
import urllib
app = Flask(__name__)

@app.get("/")
def get_all():
    titles = []
    notes = []
    for element in request.cookies:
        titles.append(urllib.parse.unquote(element))
        notes.append(request.cookies.get(element))
    return render_template("main.html", data={"title": titles,"notes": notes})

@app.get("/titles")
def get_titles():
    titles = []
    for element in request.cookies:
        titles.append(element)
    return titles


@app.get("/search/<titles>")
def get_gcookie(titles):
    title = urllib.parse.quote(titles)
    return "<a href='/'> <- Vissza a főoldalra</a>"+"<h1>"+titles+"</h1>"+"<p>"+request.cookies.get(title)+"</p>" 

@app.post("/")
def post_form():
    res = make_response(redirect("/"))
    title = urllib.parse.quote(request.form["title"])
    res.set_cookie(key=title,value=request.form["element"],expires= "Session")
    return res

@app.post("/delete")
def post_querydelete():
    res = make_response(redirect("/"))
    for elemnt in request.cookies:
        title = urllib.parse.quote(request.args.get("t"))
        if(elemnt==title):
            res.set_cookie(title, '', expires=0)
    return res


if __name__ == "__main__":
    app.run(debug=True)