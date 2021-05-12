from flask import Flask, jsonify
from datetime import datetime
import pytz
import socket

app = Flask(__name__)

@app.route('/pucsd')
def myapi():
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)
    hostname=socket.gethostname()
    return jsonify(Current_Time=datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'), IP_Addr=socket.gethostbyname(hostname), Hostname=hostname,City="Pune", Region="Asia", Country="India")

if __name__ == '__main__':
    app.run()
