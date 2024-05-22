
import csv
from re import T
from checkInventory import check_store
import subprocess
import logging
import datetime
import os
import json


# 创建日志文件夹
log_folder = "logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
    
# 配置日志
log_filename = datetime.datetime.now().strftime("%Y-%m-%d.log")
log_file_path = os.path.join(log_folder,log_filename)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    )

# 店铺信息
store_info ={
    'R079': '銀座',
    'R119': '渋谷',
    'R128': '新宿',
    'R224': '表参道',
    'R710': '川崎',
    'R718': '丸の内'
}

def buy_product(user_data,product,store):
    product_name = product["name"]
    product_color = product["color"]
    product_storage = product["storage"]    

    # 循环遍历用户信息
    for user in user_data:
        username = user['USERNAME']
        password = user['PASSWORD']
        status = user['STATUS']
    
    # 检查状态是否为 'NO'，表示用户可以购物
    if status == 'NO':
        print(username+" start buy :"+product_color+","+product_storage+","+product_name)
        # 调用 iphone15-promax.py 并传递用户信息和商品信息作为参数
        command = ["python", "iphone15-promax.py", username, password,store,product_name,product_color,product_storage]
        
        # order
        try:
            result = subprocess.check_output(command,text=True,timeout=60) # 超时时间
            logging.info(f"User: {username} - {result.strip()}")
            
            user['STATUS'] = 'YES'
            
            if "Error:" in result :
                logging.error(f"User:{username} - Purchase failed: {result} ")
            else:
                logging.info(f"User:{username} - {result.strip()}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Timeout: Operation in order.py took too long")
        except subprocess.TimeoutExpired as e:
            logging.error("Command timed out:", e)
        except Exception as e:
            logging.error("An unexpected error occurred:", e)
    else:
        logging.error(f"User: {username} - Skipped (Already purchased)")
       
    # 更新用户信息到 CSV 文件
    with open('./db/userInfo.csv', 'w', newline='') as user_file:
        user_writer = csv.DictWriter(user_file, delimiter='\t', fieldnames=user_data[0].keys())
        user_writer.writeheader()
        user_writer.writerows(user_data)


# 读取用户信息
user_data = []
with open('./db/userInfo.csv','r',newline='') as user_file:
    user_reader = csv.DictReader(user_file,delimiter=',')
    #next(user_reader)
    for row in user_reader:
        user_data.append(row)

# 读取商品信息
with open("./db/products.json","r",encoding="utf-8" ) as json_file:
    product_info_json = json.load(json_file)
    
for product_key,product_data in product_info_json.items():
    product_name = product_data["name"]
    product_color = product_data["color"]
    product_pattern = product_data["pattern"]

    for store_id in store_info.keys():
        # 获取库存信息
        flag = check_store(product_pattern,store_id)
        if flag == True:
            print(f"商品: {product_key} -在库( {store_info[store_id]})可以进行购买。")
            buy_product(user_data,product_data,store_id)
    

print(f"over。")



        

    