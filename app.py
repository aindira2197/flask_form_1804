from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def res():
    if request.method == 'POST':
        n = request.form.get('name').title()
        e = request.form.get('email').lower()
        p = request.form.get('password')

        if len(n) > 3 and "@"  in e and len(p) >= 6:
            res = [n, e, p]
        else:
            res = ['Malumotlar xato kiritildi']
        
        return render_template('res.html',res=res)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
