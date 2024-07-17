# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options



def parser()-> str:
    display = Display(visible=0, size=(1920, 1080))
    display.start()

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    result = ''
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    search_text = "160-798-193-99"
    itmo_number = '16079819399'

    #КФУ
    url_itis1 = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=47&p_speciality=1416&p_inst=0&p_typeofstudy=1'
    url_itis2 = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=47&p_speciality=1435&p_inst=0&p_typeofstudy=1'
    url_iirsi1 = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=94&p_speciality=2132&p_inst=0&p_typeofstudy=1'
    url_iirsi2 = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=94&p_speciality=2133&p_inst=0&p_typeofstudy=1'
    url_vmk1 = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=9&p_speciality=1084&p_inst=0&p_typeofstudy=1' #прикладная инфа
    url_vmk2 = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=9&p_speciality=166&p_inst=0&p_typeofstudy=1' 

    #ИТМО
    url1_itmo = 'https://abit.itmo.ru/rating/bachelor/budget/1851'
    url2_itmo = 'https://abit.itmo.ru/rating/bachelor/budget/1859'
    url3_itmo = 'https://abit.itmo.ru/rating/bachelor/budget/1853'

    itmo = [url1_itmo, url2_itmo, url3_itmo]
    kfu = [url_itis1, url_itis2, url_iirsi1, url_iirsi2, url_vmk1, url_vmk2]
    kfu_insts = {0: 'Современная разработка ПО ИТИС',
                1: 'Разработка цифровых продуктов ИТИС',
                2: 'Разработчик ИИ ИИРСИ',
                3: 'Архитектор ИИ платформ ИИРСИ',
                4: 'Прикладная информатика ВМК',
                5: 'Прикладная информатика ВМК'}

    itmo_insts = {0: 'Информационная безопасность',
                1: 'Искусственный интеллект и робототехника',
                2: 'Технологии защиты информации'}

    result += 'КФУ:\n'

    for ls in range(len(kfu)):
        driver.get(kfu[ls])
        row = driver.find_element(By.XPATH, f"//tr[td[contains(text(), '{search_text}')]]")
        place = row.find_element(By.XPATH, "./td[1]")
        result += f'\n{kfu_insts[ls]}: {place.text}'

    result += '\n\nИТМО:\n'

    for ls in range(len(itmo)):
        driver.get(itmo[ls])
        element = driver.find_element(By.XPATH, f"//span[contains(text(), '{itmo_number}')]")
        number = element.find_element(By.XPATH, ".//ancestor::div[contains(@class, 'RatingPage_table__item__qMY0F')]//p[contains(@class, 'RatingPage_table__position__uYWvi')]")
        result += f'\n{itmo_insts[ls]}: {number.text.split()[0]}'

    driver.quit()
    display.stop()


    return result