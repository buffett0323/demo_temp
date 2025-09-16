from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
from datetime import datetime

app = Flask(__name__)

# 確保result資料夾存在
if not os.path.exists('result'):
    os.makedirs('result')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('Audio', filename)

@app.route('/submit', methods=['POST'])
def submit_results():
    try:
        data = request.get_json()
        
        # 生成文件名（使用時間戳）
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"result/audio_evaluation_{timestamp}.json"
        
        # 保存結果到JSON文件
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return jsonify({"status": "success", "message": "結果已成功保存"})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5324, debug=True)
