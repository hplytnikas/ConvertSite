from flask import Flask, request, jsonify, send_file
import Converter
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, expose_headers=['Content-Disposition'])

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.json
        link = data['link']
        file_path = Converter.convert_audio(link)
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404
        filename = os.path.basename(file_path)
        file = send_file(file_path, mimetype='audio/mpeg', as_attachment=True, download_name=filename)
        return file
    except Exception as e:
        print("error: ", e)
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    # app.run(debug=False)
    app.run(host='0.0.0.0', port=5001) # Use this line if you want to run the server on your local network