#momo#s Py server für berechnungen die im browser nicht gehen

from flask import Flask, request, jsonify
import sympy


app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/req', methods=["GET"])
def galaxy2():
    return app.send_static_file('requester.html')

    
@app.route('/', methods=["GET"])
def galaxy():
    return app.send_static_file('index.html')


@app.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    holder = data["info"] # holds DATA as string
    # now stuff happpens
    x = sympy.Symbol("x")
    a = sympy.Symbol("a")
    b = sympy.Symbol("b")
    expr = sympy.parse_expr(holder.replace("^", "**"), evaluate=False) #parse
    u = sympy.re(expr).subs(sympy.re(x), a).subs(sympy.im(x), b)# substitute
    v = sympy.im(expr).subs(sympy.re(x), a).subs(sympy.im(x), b)# substitute
    u_x = sympy.diff(u, a)
    u_y = sympy.diff(u, b)
    v_x = sympy.diff(u, a)
    v_y = sympy.diff(u, b)
    holder = [str(sympy.simplify((1/(u_x**2+v_x**2)*(u*u_x+v*v_x)))), str(sympy.simplify((1/(u_x**2+v_x**2)*(u*u_y+v*v_y))))] # [im, re] of f/f'
    #holder should be reeturned a string
    return jsonify({"info" : holder}), 201
    
    
if __name__ == "__main__":
    app.run(debug=True)