from pymongo import MongoClient

# 连接到 MongoDB 数据库
client = MongoClient('mongodb://localhost:27017/')  # 替换为你的 MongoDB URI
db = client['test_database']  # 创建或选择数据库
collection = db['test_collection']  # 创建或选择集合

# 创建（插入）文档
def create_document(data):
    result = collection.insert_one(data)
    print(f'插入文档 ID: {result.inserted_id}')

# 读取（查询）文档
def read_documents():
    documents = collection.find()
    for doc in documents:
        print(doc)

# 更新文档
def update_document(query, new_values):
    result = collection.update_one(query, {'$set': new_values})
    print(f'更新的文档数量: {result.modified_count}')

# 删除文档
def delete_document(query):
    result = collection.delete_one(query)
    print(f'删除的文档数量: {result.deleted_count}')

# 示例操作
if __name__ == "__main__":
    # 创建文档
    create_document({'name': 'Alice', 'age': 25})
    
    # 读取文档
    print("所有文档:")
    read_documents()
    
    # 更新文档
    update_document({'name': 'Alice'}, {'age': 26})
    
    # 删除文档
    # delete_document({'name': 'Alice'})