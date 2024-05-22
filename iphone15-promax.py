from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# 接收用户信息和商品信息作为命令行参数
username = sys.argv[1]
password = sys.argv[2]
store = sys.argv[3]
product_name = sys.argv[4]
product_color = sys.argv[5]
product_storage = sys.argv[6]


# iphone15 自动化测试
print("iphone15-pro-max start")

# 访问测试的url定义
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-15-pro"

# 1. 创建浏览器对象  这里的Chrome中的变量是chromedriver的驱动地址
driver = webdriver.Chrome()

# 2. 跳转到apple官网
driver.get(url)

# 3. 隐式等待 设置 防止预售的网络的阻塞
driver.implicitly_wait(10)

try:

    # 4.  モデル
    if product_name == "iPhone 15 Pro Max":
        # iPhone 15 Pro Max
        element_sku = driver.find_element(By.XPATH, '//*[@value="6_7inch"]')
        driver.execute_script("arguments[0].click();", element_sku)
    else:
        # iPhone 15 Pro
        element_sku = driver.find_element(By.XPATH, '//*[@value="6_1inch"]')
        driver.execute_script("arguments[0].click();", element_sku)

    # 4.2  仕上げ
    if product_color == "ナチュラルチタニウム":
        element_color = driver.find_element(By.XPATH, '//*[@value="naturaltitanium"]')
    elif  product_color == "ブルーチタニウム":
        element_color = driver.find_element(By.XPATH, '//*[@value="bluetitanium"]')
    elif  product_color == "ホワイトチタニウム":
        element_color = driver.find_element(By.XPATH, '//*[@value="whitetitanium"]')
    elif  product_color == "ブラックチタニウム":
        element_color = driver.find_element(By.XPATH, '//*[@value="blacktitanium"]')

    driver.execute_script("arguments[0].click();",  element_color)
    driver.implicitly_wait(10)

    # 4.3 ストレージ
    if product_storage == "256GB":
        element_storage = driver.find_element(By.XPATH, '//*[@value="256gb"]')
    elif  product_storage == "512GB":
        element_storage = driver.find_element(By.XPATH, '//*[@value="512gb"]')
    elif  product_storage == "1TB":
        element_storage = driver.find_element(By.XPATH, '//*[@value="1tb"]')
        
    driver.execute_script("arguments[0].click();",  element_storage)
    driver.implicitly_wait(10)

    # 4.4 Apple Trade In
    #  【没有旧机折扣】
    element_old = driver.find_element(By.XPATH, '//*[@id="noTradeIn"]')
    driver.execute_script("arguments[0].click();", element_old)
    driver.implicitly_wait(20)

    # 4.5 支払い方法
    # 【一括払い】
    #element_purchase = driver.find_element(By.XPATH, '//*[@value="fullprice"]')
    element_purchase = driver.find_element(By.XPATH, '//*[@name="purchase_option_group"and @value="fullprice"]')
    driver.execute_script("arguments[0].click();", element_purchase)
    #element_purchase.click()
    driver.implicitly_wait(20)

    # 4.6 通信キャリア接続
    # 【あとで通信キャリアと接続する】
    element_carrier = driver.find_element(By.XPATH, '//*[@value="UNLOCKED_JP"]')
    driver.execute_script("arguments[0].click();", element_carrier) 
    driver.implicitly_wait(20)

    # 4.7 Applecare 
    # 【保証なし】
    element_care = driver.find_element(By.ID, 'applecareplus_59_applecare_59_open')
    element_nocare = driver.find_element(By.ID, 'applecareplus_59_noapplecare')
    driver.execute_script("arguments[0].click();", element_care)
    driver.implicitly_wait(20)
    driver.execute_script("arguments[0].click();", element_nocare)
    driver.implicitly_wait(20)
    

    # 4.8 添加到购物袋
    element_car = driver.find_element(By.XPATH, '//*[@value="add-to-cart"]')
    driver.execute_script("arguments[0].click();", element_car)
    driver.implicitly_wait(50)


    # 5 页面跳转查看购物袋
    element_check = driver.find_element(By.XPATH, '//*[@value="proceed"]')
    driver.execute_script("arguments[0].click();", element_check)
    driver.implicitly_wait(10)

    # 6 结账
    element_check_out = driver.find_element(By.XPATH, '//*[@id="shoppingCart.actions.checkout"]')
    driver.execute_script("arguments[0].click();", element_check_out)
    driver.implicitly_wait(10)

    driver.execute_script("return document.readyState == 'complete'")
    
    # iframe 
    iframe = driver.find_element(By.ID, 'aid-auth-widget-iFrame')
    driver.switch_to.frame(iframe)

    # 7.1 输入用户名
    element_username_check = driver.find_element_by_xpath(
        '//*[@can-field="accountName"]')
    driver.execute_script("arguments[0].click();", element_username_check)
    driver.implicitly_wait(10)

    element_username = driver.find_element_by_id(
        'account_name_text_field')
    element_username.send_keys(username)
    driver.implicitly_wait(10)

    element_login = driver.find_element_by_id(
        'sign-in')
    element_login.click()
    driver.implicitly_wait(10)

    # 7.2 输入密码
    element_password_check = driver.find_element_by_xpath(
        '//*[@can-field="password"]')
    driver.execute_script("arguments[0].click();", element_password_check)
    driver.implicitly_wait(10)

    element_password = driver.find_element_by_id(
        'password_text_field')
    element_password.send_keys(password)
    driver.implicitly_wait(10)

    # 7.3 点击登录
    element_login = driver.find_element_by_id(
        'sign-in')
    element_login.click()
    driver.implicitly_wait(10)

    # 8.1 你希望如何收到订单商品  
    # 【取货】
    element_want_order = driver.find_element_by_id(
        'fulfillmentOptionButtonGroup1')
    driver.execute_script("arguments[0].click();", element_want_order)
    time.sleep(2)

    print(f"受け取るストア："+store)
    # 8.2 受け取り場所をさらに表示
    select_store = driver.find_element_by_xpath(
        '//*[@value="'+store+'"]')
    driver.execute_script("arguments[0].click();", select_store)
    time.sleep(2)

    # 8.3 詳細に進む
    selectdistrict = driver.find_element_by_xpath(
        '//*[@data-autom="fulfillment-continue-button"]')
    driver.execute_script("arguments[0].click();", selectdistrict)
    time.sleep(2)

    # 因为无货需要判断元素是否可以点击
    isOK = driver.find_element_by_xpath(
        '//*[@class="rt-storelocator-store-list"]/fieldset/ul/li[1]/input').is_enabled()
    isOKFlag = bool(1 - isOK)
    #print("准备isOKFlag   " + str(isOKFlag))

    # while循环查看是否有货
    while isOKFlag:
        try:
            # 重新调用省市区
            #print("进来了isOKFlag   " + str(isOKFlag))
            selectdistrict = driver.find_element_by_xpath('//*[@data-autom="fulfillment-pickup-store-search-button"]')
            driver.execute_script("arguments[0].click();", selectdistrict)
            time.sleep(1)

            isOK = driver.find_element_by_xpath('//*[@class="rt-storelocator-store-list"]/fieldset/ul/li[1]/input').is_enabled()
            isOKFlag = bool(1 - isOK)
            #print("最后了isOK   " + str(isOKFlag))
        except:
            print("异常了   ")
            break

    # 8.6 选择取货零售店 【此处我选择了-Apple 青岛万象城】
    #element_pickupTab = driver.find_element_by_xpath('//*[@class="rt-storelocator-store-list"]/fieldset/ul/li[1]/input')
    #driver.execute_script("arguments[0].click();", element_pickupTab)
    #driver.implicitly_wait(20)

    # 8.7 继续填写取货详情
    #element_checkout = driver.find_element_by_id(
    #    'rs-checkout-continue-button-bottom')
    #driver.execute_script("arguments[0].click();", element_checkout)
    #time.sleep(2)

    # 8.8 选择取货时间 
    # 【根据时间自己定】
    element_pickup_time = driver.find_element_by_xpath(
        '//*[@value="18"]')
    driver.execute_script("arguments[0].click();", element_pickup_time)
    time.sleep(2)

    # 8.9 选择取货时间段 
    # 【默认第一个时间段】
    element_time_quantum = driver.find_element_by_xpath(
        '//*[@id="checkout.fulfillment.pickupTab.pickup.timeSlot.dateTimeSlots.timeSlotValue"]')
    Select(element_time_quantum).select_by_index(1)
    time.sleep(2)

    # 8.10 继续填写取货详情
    element_checkout = driver.find_element_by_id(
        'rs-checkout-continue-button-bottom')
    driver.implicitly_wait(15)
    driver.execute_script("arguments[0].click();", element_checkout)
    element_checkout.click()
    driver.implicitly_wait(20)

    # 9.1 请填写姓氏
    lastName = driver.find_element_by_id(
        'checkout.pickupContact.selfPickupContact.selfContact.address.lastName')
    lastName.send_keys('アプール')
    driver.implicitly_wait(10)

    # 9.2 请填写名字
    firstName = driver.find_element_by_id(
        'checkout.pickupContact.selfPickupContact.selfContact.address.firstName')
    firstName.send_keys('太郎')
    driver.implicitly_wait(10)

    # 9.3 请填写电子邮件
    emailAddress = driver.find_element_by_id(
        'checkout.pickupContact.selfPickupContact.selfContact.address.emailAddress')
    emailAddress.send_keys('123456@qq.com')
    driver.implicitly_wait(10)

    # 9.4 请填写手机号
    emailAddress = driver.find_element_by_id(
        'checkout.pickupContact.selfPickupContact.selfContact.address.fullDaytimePhone')
    emailAddress.send_keys('080123456789')
    driver.implicitly_wait(10)

    # 9.6 继续选择付款方式
    element_checkoutPay = driver.find_element_by_id(
        'rs-checkout-continue-button-bottom')
    driver.execute_script("arguments[0].click();", element_checkoutPay)
    driver.implicitly_wait(10)

    # 10 ご希望の支払い方法
    element_billingOptions = driver.find_element_by_id(
        'checkout.billing.billingoptions.credit')
    driver.execute_script("arguments[0].click();", element_billingOptions)
    driver.implicitly_wait(10)

    # 9.1 カード情報を入力
    cardNumber = driver.find_element_by_id(
        'checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.cardNumber')
    cardNumber.send_keys('1234567890')
    driver.implicitly_wait(10)

    # 9.2 有効期限
    cardMonth = driver.find_element_by_id(
        'checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.expiration')
    cardMonth.send_keys('01/26')
    driver.implicitly_wait(10)

    # 9.2 CVV
    cardCvv = driver.find_element_by_id(
        'checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.securityCode')
    cardCvv.send_keys('999')
    driver.implicitly_wait(10)

    # 11.1 确定
    element_orderPay = driver.find_element_by_id(
        'rs-checkout-continue-button-bottom')
    driver.execute_script("arguments[0].click();", element_orderPay)
    time.sleep(2)

    # 12 确认订单
    element_endPay = driver.find_element_by_id(
        'rs-checkout-continue-button-bottom')
    driver.execute_script("arguments[0].click();", element_endPay)
    driver.implicitly_wait(15)

except Exception as e:
    shopping_info = f"Error:{str(e)}"

# 11 退出浏览器
time.sleep(10)

# driver.quit()
shopping_info = "iphone15-pro-max end"

# 返回购物信息，主程序将其写入日志
print(shopping_info)