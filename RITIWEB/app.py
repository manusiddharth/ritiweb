from flask import Flask, render_template, request, jsonify 


app=Flask(__name__)
n=[]
#break point one 
@app.route('/')
def home():
    return render_template('index.html')

##break point 2 
@app.route('/num', methods=['GET', 'POST'])
def num():
    if request.method == 'POST':
        number = request.form.get('number')
        if number and number.isdigit():
            n.append(int(number))
    return render_template('num.html')

##break point 3
@app.route('/data',methods=["GET"])
def data():
    return jsonify({"number": n})


    


if __name__=='__main__':
    app.run(debug = True)