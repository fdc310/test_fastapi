import requests




def Chat_msg(data):
    print(1)
    # 目标 URL
    target_url = "http://43.155.168.172:5000/chat"

    # 使用 requests 发送 POST 请求，并开启流式响应
    print(data)
    resp = requests.post(target_url, json=data, stream=True)

    # 检查响应状态码
    if resp.status_code == 200:
        # 如果响应成功，收集完整的流式数据
        complete_data = resp.raw.read()  # 读取完整的响应数据

    # 返回一个流式响应
    print(complete_data.decode())
    # str.split('：')
    # text = complete_data.decode()
    return complete_data.decode()