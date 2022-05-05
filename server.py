from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.method)
    if request.method == 'POST':
        print(request.json)
        return 'working', 200
    else:
        abort(400)    

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)