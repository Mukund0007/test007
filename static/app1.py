from flask import Flask, render_template,request,jsonify
import requests
import websocket
import json
#import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route("/get")
def getBotResponse():
    query = request.args.get('msg')
    response = requests.get("http://localhost:5000/parse",params={"q":query})
    response = response.json()
    topresponse = response["topScoringIntent"]
    intent = topresponse.get("intent")
    #return str(intent)
    if intent == "ARoverdue":
        var = []
        try:
            import thread
        except ImportError:
            import _thread as thread
        import time
        def on_message(ws, message):
            msg = json.loads(message)
            var.append(msg)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")
            global var
            return var

        def on_open(ws):
            def run(*args):
                for i in range(3):
                    time.sleep(1)
                    ws.send(json.dumps(methods[i]))
                time.sleep(1)
                ws.close()
                print("thread terminating...")
            thread.start_new_thread(run, ())
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://localhost:4848/app/",
                                      on_message = on_message,
                                      on_error = on_error,
                                      on_close = on_close)
        methods = [{
	                "handle": -1,
	                "method": "OpenDoc",
	                "params": {
		                "qDocName": "Executive Dashboard",
		                "qUserName": "",
		                "qPassword": "",
		                "qSerial": "",
		                "qNoData": 0
	                }
                },{
	            "handle": 1,
	            "method": "GetObject",
	            "params": {
		              "qId": "MdpsUpA"
	            }
               },{
	            "handle": 2,
	            "method": "GetLayout",
	            "params": {}
            }]
        ws.on_open = on_open
        ws.run_forever()
        result = var[3]['result']['qLayout']['title'] + " against " + var[3]['result']['qLayout']['subtitle']
        response_text = result
    elif intent == "Revenue%":
        var = []
        try:
            import thread
        except ImportError:
            import _thread as thread
        import time
        def on_message(ws, message):
            msg = json.loads(message)
            var.append(msg)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")
            global var
            return var

        def on_open(ws):
            def run(*args):
                for i in range(3):
                    time.sleep(1)
                    ws.send(json.dumps(methods[i]))
                time.sleep(1)
                ws.close()
                print("thread terminating...")
            thread.start_new_thread(run, ())
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://localhost:4848/app/",
                                      on_message = on_message,
                                      on_error = on_error,
                                      on_close = on_close)
        methods = [{
	                "handle": -1,
	                "method": "OpenDoc",
	                "params": {
		                "qDocName": "Executive Dashboard",
		                "qUserName": "",
		                "qPassword": "",
		                "qSerial": "",
		                "qNoData": 0
	                }
                },{
	            "handle": 1,
	            "method": "GetObject",
	            "params": {
		              "qId": "tcxTY"
	            }
               },{
	            "handle": 2,
	            "method": "GetLayout",
	            "params": {}
            }]
        ws.on_open = on_open
        ws.run_forever()
        result = var[3]['result']['qLayout']['title'] + " against " + var[3]['result']['qLayout']['subtitle']
        response_text = result
    elif intent == "ExpTar":
        var = []
        try:
            import thread
        except ImportError:
            import _thread as thread
        import time
        def on_message(ws, message):
            msg = json.loads(message)
            var.append(msg)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")
            global var
            return var

        def on_open(ws):
            def run(*args):
                for i in range(3):
                    time.sleep(1)
                    ws.send(json.dumps(methods[i]))
                time.sleep(1)
                ws.close()
                print("thread terminating...")
            thread.start_new_thread(run, ())
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://localhost:4848/app/",
                                      on_message = on_message,
                                      on_error = on_error,
                                      on_close = on_close)
        methods = [{
	                "handle": -1,
	                "method": "OpenDoc",
	                "params": {
		                "qDocName": "Executive Dashboard",
		                "qUserName": "",
		                "qPassword": "",
		                "qSerial": "",
		                "qNoData": 0
	                }
                },{
	            "handle": 1,
	            "method": "GetObject",
	            "params": {
		              "qId": "KxdNL"
	            }
               },{
	            "handle": 2,
	            "method": "GetLayout",
	            "params": {}
            }]
        ws.on_open = on_open
        ws.run_forever()
        result = var[3]['result']['qLayout']['title'] + " against " + var[3]['result']['qLayout']['subtitle']
        response_text = result
    elif intent == "SaleMargin":
        response_text = "http://localhost:4848/single/?appid=C%3A%5CUsers%5CMukund%20Kumar%5CDocuments%5CQlik%5CSense%5CApps%5CExecutive%20Dashboard.qvf&obj=fzrxtjq"    
    elif intent == "ProductRevenue":
        response_text = "http://localhost:4848/single/?appid=C%3A%5CUsers%5CMukund%20Kumar%5CDocuments%5CQlik%5CSense%5CApps%5CExecutive%20Dashboard.qvf&obj=ZxDKp"
    elif intent == "DSO":
        response_text = "http://localhost:4848/single/?appid=C%3A%5CUsers%5CMukund%20Kumar%5CDocuments%5CQlik%5CSense%5CApps%5CExecutive%20Dashboard.qvf&obj=mVPztHm"
    elif intent == "CustomersOverdue":
        response_text = "http://localhost:4848/single/?appid=C%3A%5CUsers%5CMukund%20Kumar%5CDocuments%5CQlik%5CSense%5CApps%5CExecutive%20Dashboard.qvf&obj=ARNmpdM"
    else:
        response_text = "Sorry I am not trained to do that yet..."
    return str(response_text)
if __name__ == '__main__':
    app.run(debug=True,port = 8080)
    
