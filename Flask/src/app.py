from flask import (
    Flask,
    request,
    render_template,
    make_response,
    jsonify,
    redirect,
    abort,
)

app = Flask("Hello Flask")


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/hello")
def hello():
    return render_template("hello.html")


@app.route("/about")
def about():
    return "This is an about page."


@app.route("/user/<username>", methods=["GET", "PUT"])
def user(username):
    if request.method == "GET":
        return f"Nice to meet you, {username}"
    elif request.method == "PUT":
        return f"Created user sucessfully"


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    if request.method == "GET":
        return f"This is the {post_id}th post."
    elif request.method == "POST":
        return f"Updated post successfully"


@app.route("/search")
def search():
    searching_text = request.args.get("text")
    return f"You searched with text: {searching_text}"


@app.route("/cookie/set")
def set_cookie():
    rsp = make_response(jsonify({"id": "hoya", "password": "1234"}), 200)
    rsp.set_cookie("id", "hoya")
    return rsp


@app.route("/cookie/get")
def get_cookie():
    id = request.cookies.get("id")
    return f"Get ID {id} from cookie"


@app.route("/wrong_path")
def wrong_path():
    return redirect("/")


@app.route("/abort")
def error_abort():
    abort(401)


@app.errorhandler(404)
def not_found(error):
    return render_template("not_found.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")