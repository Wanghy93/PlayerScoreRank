"""客户端上传客户端号和分数(注意：并不会上传排名,客户端无法上传排名),同一个客户端可以多次上传分数，取最新的一次分数"""

def uploading():
    """客户端上传客户编号和分数"""
    client_no = input("请输入您的客户编号：")
    score = int(input("请输入您的分数："))
    return client_no, score

uploading()

# 创建客户表，存储客户编号,分数和排名
class Client(BaseModel):