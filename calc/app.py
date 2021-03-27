# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div
# need to import the operations that will allow us to build the code simpler

app = Flask(__name__)


@app.route("/add")
def do_add():
    """Adds a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route("/sub")
def do_sub():
    """Subtract a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route("/mult")
def do_mult():
    """Multiply a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route("/div")
def do_div():
    """Divide a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

# part 2
# found solution on stack overflow website
# create a operators list


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<operator>")
def do_math(operator):
    """Do math with a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operator](a, b)

    return str(result)
