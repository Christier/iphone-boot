import requests

# 接收商品信息和店铺信息作为命令行参数
def check_store(product,store):
    api_url = "https://www.apple.com/jp/shop/retail/pickup-message?pl=true&parts.0="+product+"&store="+store
    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            json_data = response.json()
            if json_data["body"]["stores"][0]["partsAvailability"][product]["messageTypes"]["regular"]["storeSelectionEnabled"] == True :
                print("")
                return True
            else:
                return False
        except ValueError:
            return False
    else:
        return False
    

