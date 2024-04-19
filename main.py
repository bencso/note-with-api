from flask import Flask, redirect , request, make_response,render_template

app = Flask(__name__)

@app.get("/")
def get_all():
    titles = []
    notes = []
    for element in request.cookies:
        titles.append(element)
        notes.append(request.cookies.get(element))
    return render_template("main.html", data={"title": titles,
                                            "notes": notes
                                                })

@app.get("/titles")
def get_titles():
    titles = []
    for element in request.cookies:
        titles.append(element)
    return titles


@app.get("/search/<titles>")
def get_gcookie(titles):
    return "<a href='/'> <- Vissza a főoldalra</a>"+"<h1>"+titles+"</h1>"+"<p>"+request.cookies.get(titles)+"</p>" 

@app.post("/")
def post_form():
    res = make_response(redirect("/"))
    res.set_cookie(key=request.form["title"],value=request.form["element"],expires= "Session")
    return res

@app.post("/delete")
def post_querydelete():
    res = make_response(redirect("/"))
    for elemnt in request.cookies:
        if(elemnt==request.args.get("t")):
            res.set_cookie(request.args.get("t"), '', expires=0)
    return res


if __name__ == "__main__":
    app.run(debug=True)