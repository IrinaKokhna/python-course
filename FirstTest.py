from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.webdriver.support.ui import Select
import os


def test_first():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    print("рыба")
    button = browser.find_element_by_id("submit")
    button.click()

def test_two():
    browser = webdriver.Chrome()
    browser.get("https://www.google.com/")

def test_three():
    browser = webdriver.Chrome()
    browser.get("https://www.yandex.ru/")
    print("хамса")
    button = browser.find_element_by_id("submit")
    button.click()

def test_fourth():
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element_by_css_selector(
                'form > div.first_block > div.form-group.first_class > input')
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_class_name(
                'form-control third')
            input2.send_keys("Petrov@gamail.com")
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


def test_fifth():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('.first_block .form-control.first')
        input1.send_keys("ок")
        input2 = browser.find_element_by_css_selector('.first_block .form-control.second')
        input2.send_keys("ок")
        input3 = browser.find_element_by_css_selector('.first_block .form-control.third')
        input3.send_keys("ок")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_sixth():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    try:
        link = "http://suninjuly.github.io/get_attribute.html"
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element_by_id('treasure')
        x_value = x_element.get_attribute("valuex")
        y = calc(x_value)

        element1 = browser.find_element_by_css_selector('#answer')
        element1.send_keys(y)

        option1 = browser.find_element_by_id("robotCheckbox")
        option1.click()
        option2 = browser.find_element_by_id("robotsRule")
        option2.click()
        option2 = browser.find_element_by_css_selector("form > div > div > button")
        option2.click()
    finally:
        time.sleep(10)
        browser.quit()


def test_seventh():
    try:
        link = "http://suninjuly.github.io/selects1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # находим элементы
        num1_in_text = browser.find_element_by_id("num1")
        num2_in_text = browser.find_element_by_id("num2")

        # вытаскиваем заданные числа
        num1 = int(num1_in_text.text)
        num2 = int(num2_in_text.text)

        # находим и выбираем значение, которое является суммой этих 2 чисел
        select = Select(browser.find_element_by_class_name("custom-select"))
        select.select_by_value(str(num1 + num2))

        # нажимаем на кнопку
        send_button = browser.find_element_by_class_name("btn-default")
        send_button.click()
    finally:
        time.sleep(10)
        browser.quit()


def test_eight():
    try:
        browser = webdriver.Chrome()
        link = "https://SunInJuly.github.io/execute_script.html"
        browser.get(link)
        button = browser.find_element_by_tag_name("button")
        button.click()
    finally:
        time.sleep(10)
        browser.quit()


def test_ninght():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    try:
        link = "http://suninjuly.github.io/execute_script.html"
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element_by_css_selector('#input_value')
        x = x_element.text
        y = calc(x)
        element1 = browser.find_element_by_css_selector('#answer')
        element1.send_keys(y)

        option1 = browser.find_element_by_id("robotCheckbox")
        option1.click()
        browser.execute_script("window.scrollBy(0, 100);")
        option2 = browser.find_element_by_id("robotsRule")
        option2.click()
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
    finally:
        time.sleep(10)
        browser.quit()


def test_tenth():
    try:
        link = 'http://suninjuly.github.io/file_input.html'
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_name('firstname')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name('lastname')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_name('email')
        input3.send_keys("Smolensk@mail.ru")
        element = browser.find_element_by_css_selector('#file')
        element.send_keys("/Users/irina/PycharmProjects/pythonProject1/requirements.txt")
        button = browser.find_element_by_css_selector("form > button")
        button.click()
    finally:
        time.sleep(10)
        browser.quit()



def test_eleventh():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    try:
        link = 'http://suninjuly.github.io/alert_accept.html'
        browser = webdriver.Chrome()
        browser.get(link)
        button1 = browser.find_element_by_css_selector("div > div > button")
        button1.click()
        confirm = browser.switch_to.alert
        confirm.accept()
        x_element = browser.find_element_by_css_selector('#input_value')
        x = x_element.text
        y = calc(x)
        element1 = browser.find_element_by_css_selector('#answer')
        element1.send_keys(y)
        button = browser.find_element_by_css_selector('div > div > button')
        button.click()
    finally:
        time.sleep(10)
        browser.quit()

def test_twelfth():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    try:
        link = 'http://suninjuly.github.io/redirect_accept.html'
        browser = webdriver.Chrome()
        browser.get(link)
        button1 = browser.find_element_by_css_selector("div > div > button")
        button1.click()
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        x_element = browser.find_element_by_css_selector('#input_value')
        x = x_element.text
        y = calc(x)
        element1 = browser.find_element_by_css_selector('#answer')
        element1.send_keys(y)
        button = browser.find_element_by_css_selector('div > div > button')
        button.click()
    finally:
        time.sleep(10)
        browser.quit()

def test_thirteenth():
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

def test_fifteenth():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn = browser.find_element_by_id('book')
    btn.click()
    browser.execute_script("window.scrollBy(0, 100);")
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    element1 = browser.find_element_by_css_selector('#answer')
    element1.send_keys(y)
    button = browser.find_element_by_css_selector('#solve')
    button.click()
    time.sleep(10)
    browser.quit()





