from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_pymongo import PyMongo
from model.model import predict_compatibility

app = Flask(__name__)
CORS(app)

# MongoDB 配置
app.config["MONGO_URI"] = "mongodb+srv://291165681:SkBp7AsY6Bx6OveI@cluster0.dlahl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # 替换为你从MongoDB Atlas获取的连接字符串
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    name1 = data.get('name1')
    name2 = data.get('name2')
    compatibility_score = predict_compatibility(name1, name2)

    # 将数据存储到 MongoDB
    mongo.db.predictions.insert_one({
        "name1": name1,
        "name2": name2,
        "compatibility_score": compatibility_score
    })

    return jsonify({"compatibility_score": compatibility_score})

if __name__ == '__main__':
    app.run(debug=True)
