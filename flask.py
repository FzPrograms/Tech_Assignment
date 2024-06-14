from flask import Flask
from flask import request
from flask import jsonify
import time
import pandas as pd

app = Flask(__name__)

timestamp = []
suhu = []
kelembaban = []

@app.route('/', methods=['GET'])
def home():
    if len(suhu) > 0:
        data_dict = {'timestamp': timestamp, 'suhu': suhu, 'kelembaban': kelembaban}
        df = pd.DataFrame(data_dict)
        return df.to_html()
    else:
        return 'No Data Received'

@app.route('/data', methods=['POST'])
def data():
    print("Received request!")
    if request.is_json:
        print("Request is JSON")
        data = request.json
        print("Data:", data)
        temp = data.get('suhu')
        hum = data.get('kelembaban')
    else:
        print("Request is not JSON")
        temp = request.form.get('suhu')
        hum = request.form.get('kelembaban')

    timing = time.time()
    suhu.append(temp)
    kelembaban.append(hum)
    timestamp.append(timing)

    return jsonify({'suhu': temp, 'kelembaban': hum, 'timestamp': timing})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
