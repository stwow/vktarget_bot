from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from webdriver_manager.firefox import GeckoDriverManager
import time
import threading
import os
from random import randint
import traceback


def login_in_social_networks(driver, login_yt, password_yt,mail_yt, login_tw, password_tw, mail_tw, login_ok, password_ok, login_vk, password_vk, login_yandex, password_yandex, login_vktarget, password_vktarget, count):
    print(f'Осуществление входа на Youtube. {count} поток')
    try:
        driver.get(
            'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dru%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=ru&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        driver.implicitly_wait(10)
        field1 = driver.find_element_by_id('identifierId')
        field1.send_keys(login_yt + Keys.ENTER)
        time.sleep(randint(4, 6))
        field2 = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
        time.sleep(randint(1, 2))
        field2.send_keys(password_yt + Keys.ENTER)
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_xpath('/html/body/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div').click()
            driver.implicitly_wait(10)
            time.sleep(randint(2, 4))
        except Exception:
            pass
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]/div').click()
            driver.implicitly_wait(10)
            reserv_email = driver.find_element_by_xpath('//*[@id="knowledge-preregistered-email-response"]')
            time.sleep(randint(2, 3))
            reserv_email.send_keys(mail_yt + Keys.ENTER)
            driver.implicitly_wait(10)
        except Exception:
            pass
        time.sleep(randint(4,6))
    except Exception:
        pass

    # авторизация в soundcloud через гугл
    print(f'Авторизация в soundcloud. {count} поток')
    try:
        driver.get('https://soundcloud.com/')
        time.sleep(4)
        cookies = driver.find_element_by_xpath('//*[@id="onetrust-banner-sdk"]').find_element_by_xpath(
            '//*[@id="onetrust-accept-btn-handler"]').click()
        #actions.move_to_element(cookies).click(cookies).perform()
        time.sleep(2)
        log_in = driver.find_element_by_xpath('//div[@class="frontHero__signin"]').find_element_by_tag_name('button')
        log_in.click()
        iframe = driver.find_element_by_css_selector('iframe.webAuthContainer__iframe')
        driver.switch_to.frame(iframe)
        google_click = driver.find_element_by_xpath(
            '//button[@class="sc-button sc-button-large provider-button google-plus-signin sc-button-google"]')
        google_click.click()
        # print(driver.window_handles)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_tag_name('li').click()
        # print(driver.window_handles)
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(10)
        time.sleep(3)
        # print(driver.window_handles)
    except Exception:
        pass
    time.sleep(3)
    print(f'Осуществление входа в Twitter. {count} поток')
    try:
        driver.get('https://twitter.com/login')
        driver.implicitly_wait(10)
        field1 = driver.find_element_by_css_selector(
            'div.css-1dbjc4n:nth-child(6) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)')
        field1.send_keys(login_tw)
        time.sleep(randint(3, 5))
        field2 = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        field2.send_keys(password_tw + Keys.ENTER)
        driver.implicitly_wait(10)
        time.sleep(randint(2, 3))

        try:
            driver.implicitly_wait(10)
            mail_input = driver.find_element_by_xpath('//input[@type="text" and @id="challenge_response"]')
            mail_input.send_keys(mail_tw + Keys.ENTER)
            time.sleep(randint(3, 5))
        except Exception:
            pass
        driver.refresh()
        driver.implicitly_wait(10)
        time.sleep(randint(5, 7))
    except Exception:
        # Twitter стал банить подключения из России, так что это исключение для этих целей
        pass

    print(f'Осуществление входа в Одноклассники. {count} поток')
    try:
        driver.get('https://ok.ru/')
        driver.implicitly_wait(10)
        field1 = driver.find_element_by_id('field_email')
        field1.send_keys(login_ok)
        time.sleep(randint(3, 5))
        field2 = driver.find_element_by_id('field_password')
        field2.send_keys(password_ok + Keys.ENTER)
        driver.implicitly_wait(10)
        time.sleep(randint(5, 7))
    except Exception:
        pass

    print(f'Осуществление входа в ВК. {count} поток')
    try:
        driver.get('https://vk.com/')
        driver.implicitly_wait(10)
        time.sleep(randint(3, 5))
        field1 = driver.find_element_by_id('index_email')
        field1.send_keys(login_vk)
        time.sleep(randint(3, 5))
        field2 = driver.find_element_by_id('index_pass')
        field2.send_keys(password_vk + Keys.ENTER)
        driver.implicitly_wait(10)
        time.sleep(randint(5, 7))
    except Exception:
        pass


    print(f'Осуществление входа в Яндекс Дзен. {count} поток')
    try:
        driver.get(
            'https://passport.yandex.ru/auth?origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fyandex.ru')
        driver.implicitly_wait(10)
        field1 = driver.find_element_by_id('passp-field-login')
        field1.send_keys(login_yandex + Keys.ENTER)
        driver.implicitly_wait(10)
        time.sleep(randint(3, 6))
        field2 = driver.find_element_by_id('passp-field-passwd')
        field2.send_keys(password_yandex + Keys.ENTER)
        driver.implicitly_wait(10)
        time.sleep(randint(5, 7))
    except Exception:
        pass


    print(f'Осуществление входа в vktarget {count} поток')
    driver.get('https://vktarget.ru/login/')
    driver.implicitly_wait(10)
    time.sleep(randint(1, 3))
    field1 = driver.find_element_by_id('loginEmail')
    field1.send_keys(login_vktarget)
    time.sleep(randint(1, 3))
    field2 = driver.find_element_by_id('password')
    field2.send_keys(password_vktarget)
    time.sleep(randint(4, 6))
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(10)
    if check_xpath(driver, '//div[@id="loginAlert"]'):
        driver.find_element_by_xpath('//button[@id="uloginOk"]').click()
        driver.implicitly_wait(5)
        time.sleep(randint(3, 5))
        driver.get('https://vktarget.ru')
    time.sleep(randint(3, 4))
    driver.get('https://vktarget.ru/list/?')

    print('-' * 20)


def complete_quest(text, link, button, name, close, driver, actions):
    try:
        print(f'Выполнение задания "{text}". Ссылка: {link}')
        driver.execute_script(f"window.open('{link}')")
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(20)
        time.sleep(randint(4, 6))
        if name == 'youtube':
            if text == 'Подпишитесь на канал':     #проверил, работает
                try:
                    link_button = driver.find_element_by_xpath(
                        '//tp-yt-paper-button[@class="style-scope ytd-subscribe-button-renderer"]')
                except Exception:
                    link_button = driver.find_element_by_xpath('//tp-yt-paper-button[@class="style-scope ytd-button-renderer style-destructive size-default"]')
                link_button.click()
                time.sleep(randint(1, 3))
            elif text == "Поставьте 'Лайк' под видео": #тут вроде всё работает, хотя не с первого раза - не понятно
                link_button = driver.find_elements_by_xpath(
                    '//yt-icon-button[@class="style-scope ytd-toggle-button-renderer style-text"]')[-2]
                link_button.click()
                time.sleep(randint(1, 3))
            elif text == "Поставьте 'Не нравится' под видео":
                #
                link_button = driver.find_elements_by_xpath(
                    '//yt-icon-button[@class="style-scope ytd-toggle-button-renderer style-text"]')[-1]
                link_button.click()
                time.sleep(randint(1, 3))
        elif name == 'vk':
            if text == 'Вступите в сообщество':  #проверил, тут вроде всё норм
                try:
                    link_button = driver.find_element_by_xpath('//button[@id="public_subscribe"]')
                except exceptions.NoSuchElementException:
                    link_button = driver.find_element_by_xpath('//button[@id="join_button"]')
                link_button.click()
                time.sleep(randint(1, 3))
            elif text == 'Нажмите поделиться записью':  #исправил
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 1080)")
                time.sleep(1)
                link_button = driver.find_element_by_class_name('PostBottomAction.share._share').click()
                time.sleep(randint(2, 3))
                share_my = driver.find_element_by_css_selector('#like_share_my')
                share_my.click()
                time.sleep(randint(2, 4))
                share_send = driver.find_element_by_css_selector('#like_share_send')
                share_send.click()
                time.sleep(randint(1, 3))
                # link_button = driver.find_element_by_class_name('PostBottomAction.share._share')
                # driver.execute_script("arguments[0].scrollIntoView(true);", link_button)
                # time.sleep(randint(1, 2))
                # driver.execute_script("scrollBy(0,-60);")
                # time.sleep(randint(1, 2))
                # link_button.click()
                # time.sleep(randint(2, 3))
                # share_my = driver.find_element_by_css_selector('#like_share_my')
                # share_my.click()
                # time.sleep(randint(2, 4))
                # share_send = driver.find_element_by_css_selector('#like_share_send')
                # share_send.click()
                # time.sleep(randint(1, 3))
            elif text == 'Поставьте лайк на странице': #тут тоже норм
                link_button = driver.find_element_by_class_name('_like_button_label')   #тут изменил
                driver.execute_script("arguments[0].scrollIntoView(true);", link_button)
                time.sleep(randint(1, 2))
                driver.execute_script("scrollBy(0,-60);")
                time.sleep(randint(1, 2))
                link_button.click()
                time.sleep(randint(2, 3))
            elif text == 'Добавить в друзья':
                link_button = driver.find_element_by_xpath(
                    '//button[@class="flat_button button_wide Profile__addFriendButton"]')
                link_button.click()
                time.sleep(randint(2, 4))
            elif text == 'Расскажите о группе':
                time.sleep(randint(2,4))
                link_button = driver.find_element_by_id('page_menu_group_share')
                link_button.click()
                time.sleep(randint(2, 4))
                share_send = driver.find_element_by_css_selector('#like_share_send')
                share_send.click()
                time.sleep(randint(1, 3))
        elif name == 'twitter':
            if text == 'Ретвитните запись':
                link_button = driver.find_element_by_xpath(
                    '//div[@role="button" and @data-testid="retweet"]')
                driver.execute_script("arguments[0].scrollIntoView(true);", link_button)
                time.sleep(randint(1, 2))
                driver.execute_script("scrollBy(0,-60);")
                time.sleep(randint(1, 2))
                link_button.click()
                time.sleep(randint(1, 2))
                link_button = driver.find_element_by_xpath(
                    '//div[@role="menuitem" and @data-testid="retweetConfirm"]')
                link_button.click()
                time.sleep(randint(1, 4))
            elif text == 'Поставить лайк на твит':
                link_button = driver.find_element_by_xpath('//div[@role="button" and @data-testid="like"]')
                driver.execute_script("arguments[0].scrollIntoView(true);", link_button)
                time.sleep(randint(1, 2))
                driver.execute_script("scrollBy(0,-60);")
                time.sleep(randint(1, 2))
                link_button.click()
                time.sleep(randint(2, 3))
            elif text == 'Подпишитесь на аккаунт':
                link_button = driver.find_element_by_xpath(
                    '//div[@class="css-18t94o4 css-1dbjc4n r-1niwhzg r-p1n3y5 r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-ero68b r-1gg2371 r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr"]')
                link_button.click()
                time.sleep(randint(1, 3))
        elif name == 'zen':
            if text == 'Подпишитесь на пользователя':  # исправил путь
                link_button = driver.find_element_by_xpath(
                    '//button[@class="zen-ui-button-base _is-transition-enabled zen-ui-button _size_l _view-type_yellow _width-type_wide"]')
                link_button.click()
                time.sleep(randint(2, 4))
            elif text == 'Поставьте лайк на пост': # правки есть
                try:
                    link_button = driver.find_element_by_class_name(
                        'ui-lib-mitten-icon._state_passive._theme_white._animation_none')  #тут исправил
                except Exception:
                    link_button = driver.find_element_by_xpath('//button[@class="left-column-button left-column-button_theme_none left-column-button_is-meta-move left-block-redesign-view__button"]')
                time.sleep(randint(1, 2))
                link_button.click()
                time.sleep(randint(2, 3))
        elif name == 'yandex':
            if text == 'Поставить лайк на запись':   #изменил тут имя и новый код
                link_button = driver.find_element_by_xpath(
                    '//button[@class="AydKZJS5RA _21Al5c3lu- _1NIguM8mCn _1gXOx3yDdz _2iaGxKKGsR CTE2P-0nMj"]')
                link_button.click()
                time.sleep(randint(2, 3))
                # answer_id = link.split('answer_id=')[-1]
                # div = driver.find_element_by_xpath(f'//div[@data-id="{answer_id.split("#")[0]}"]')
                # link_button = div.find_element_by_xpath(
                #     '//button[@class="_1TkYR0zJ0l _2T7KhH1RCd _3ZVku36pbO _15BWlE3fhn _232EbbQLtE MDU_ab9TJm"]')
                # link_button.click()
                # time.sleep(randint(2, 3))
        elif name == 'ok':
            if text == 'Поделиться записью':  # не разобрался тут :((
                if link.split('/')[3] != 'video':
                    link_button = driver.find_element_by_xpath(
                        '//div[@class="widget"]//button')
                    driver.execute_script("arguments[0].scrollIntoView(true);", link_button)
                    time.sleep(randint(1, 2))
                    driver.execute_script("scrollBy(0,-60);")
                    time.sleep(randint(1, 2))
                    actions.move_to_element(link_button).click(link_button).perform()
                    time.sleep(randint(1, 2))
                    try:
                        share = driver.find_element_by_xpath('//a[@class="u-menu_li js-doNotHide"]')
                    except Exception:
                        share = driver.find_element_by_xpath('//a[@class="u-menu_li u-menu_a"]')
                    share.click()
                    time.sleep(randint(2, 3))
                else:
                    link_button = driver.find_elements_by_xpath(
                        '//button[@class="h-mod widget_cnt"]')[0]
                    time.sleep(randint(1, 2))
                    actions.move_to_element(link_button).click(link_button).perform()
                    time.sleep(randint(1, 2))
                    share = driver.find_element_by_xpath(
                        '//a[@class="u-menu_li js-doNotHide"]')
                    share.click()
            elif text == 'Вступить в группу': #работает
                link_button = driver.find_element_by_xpath('//a[@class="button-pro __wide"]')
                link_button.click()
                time.sleep(randint(1, 2))
            elif text == 'Добавить в друзья': #путь не изменился, должно работать
                link_button = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[4]/div[5]/div[1]/div/div[5]/div/div[1]/div[2]/div/div[2]/div[1]/div/div/ul/li[1]/a')
                link_button.click()
                time.sleep(randint(1, 2))
            elif text == 'Поставьте класс под записью':  # исправил кусок кода
                if link.split('/')[3] != 'video':
                    link_button = driver.find_element_by_xpath(
                        '//div[@class="widget react-button  __compact __like"]')  # вот тут исправил
                    time.sleep(randint(1, 2))
                    actions.move_to_element(link_button).click(link_button).perform()
                    time.sleep(randint(1, 2))
                else:
                    link_button = driver.find_elements_by_xpath(
                        '//span[@data-like-icon="like"]')[0]
                    time.sleep(randint(1, 2))
                    actions.move_to_element(link_button).click(link_button).perform()
                    time.sleep(randint(1, 2))
        elif name == 'soundcloud':
            if text == 'Поделиться трэком':
                try:
                    driver.find_element_by_xpath(
                        '//button[@class="sc-button-repost sc-button-secondary sc-button sc-button-medium sc-button-responsive"]').click()
                    time.sleep(3)
                except Exception:
                    pass
            elif text == 'Воспроизвести трэк':
                try:
                    driver.find_element_by_xpath(
                        '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a').click()
                    time.sleep(randint(5, 8))
                    driver.find_element_by_xpath(
                        '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a').click()
                    time.sleep(randint(2, 4))
                except Exception:
                    pass
            elif text == 'Поставить лайк на трэк':
                try:
                    time.sleep(randint(2, 5))
                    driver.find_element_by_xpath(
                        '//button[@class="sc-button-like sc-button-secondary sc-button sc-button-medium sc-button-responsive"]').click()
                    time.sleep(3)
                except Exception:
                    pass
            elif text == 'подпишитесь на аккаунт':
                try:
                    time.sleep(randint(2, 5))
                    driver.find_element_by_xpath(
                        '/html/body/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/button[1]').click()
                    time.sleep(randint(2, 5))#подписаться если выкинуло на страничку юзера главную
                except Exception:
                    pass
    except Exception as e:
        pass
    finally:
        driver.implicitly_wait(randint(3, 5))
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(randint(2, 3))
        try:
            button.click()
        except Exception:
            pass


def check_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except Exception:
        return False


def get_info_from_questions(driver, actions, key, count):
    try:
        check = driver.find_element_by_class_name('user-menu__balance').text
        day=driver.find_element_by_class_name('stats__sum').text
        global result
        result[count] = float(check[0:-2])
        print(f'Файл {key}, заработано за день {day}, баланс аккаунта {check}')
        print(f'Итог по всем запущенным потокам: {sum(result)}, всего было запущено потоков: {len(result)}')
    except Exception:
        pass
    """Считывание информации из заданий"""
    try:
        if driver.find_element_by_xpath('//span[@class="user-menu__balance px-3 py-2 white--text"]'):
            print(f'Поток {count + 1} работает')
    except Exception:
        print(f'Поток {count + 1} возможно не работает')
    if check_xpath(driver, '//button[@id="skipGuideBtn"]'):
        driver.find_element_by_xpath('//button[@id="skipGuideBtn"]').click()
    driver.implicitly_wait(randint(2, 4))
    block = driver.find_elements_by_xpath('//div[@class="mdl-grid available__row bb-grey-1 pa-0"]')
    if block != []:
        for i in block:
            try:
                text = i.find_element_by_xpath('.//span[@class="task-name"]')
                link = i.find_element_by_xpath('.//a[@href]')
                button = i.find_element_by_xpath('.//button')
                close = i.find_element_by_xpath('.//div[@class="close-task-btn cursor-pointer d-flex"]')
                text = text.text.replace('&nbsp;', ' ')
                link = link.get_attribute('href')
                name = link.split('//')[1].split('.')[0]
            except Exception as e:
                print('Ошибка:\n', traceback.format_exc())
            else:
                complete_quest(text, link, button, name, close, driver, actions)
                time.sleep(randint(3, 5))
    else:
        print('Заданий нету')
    driver.refresh()
    print('-' * 20)

if __name__ == '__main__':
    list_files = os.listdir()
    text_files = filter(lambda x: x[-4:] == '.txt', list_files)

    def start_w(key, count):
        with open(f'{key}', mode='r') as f:
            text = f.read().split('\n')
            for i in text:
                data = i.split(';')
                if data[0] == 'VK':
                    password_vk = data[2]
                    login_vk = data[1]
                elif data[0] == 'OK' or data[0] == 'ОК':
                    password_ok = data[2]
                    login_ok = data[1]
                elif data[0] == 'Youtube':
                    password_yt = data[2]
                    login_yt = data[1]
                    mail_yt = data[3]
                elif data[0] == 'Twitter':
                    password_tw = data[2]
                    login_tw = data[1]
                    mail_tw = data[3]
                elif data[0] == 'Yandex':
                    password_yandex = data[2]
                    login_yandex = data[1]
                elif data[0] == 'Vktarget':
                    password_vktarget = data[2]
                    login_vktarget = data[1]
                elif data[0] == 'proxy':
                    ip = data[1]
                    port = int(data[2])
                elif data[0] == 'useragent':
                    agent = i[10:]
        # options
        options = webdriver.FirefoxOptions()
        # options.set_preference('network.proxy.type', 1)
        # options.set_preference('network.proxy.http', ip)
        # options.set_preference('network.proxy.http_port', port)
        # options.set_preference('network.proxy.https', ip)
        # options.set_preference('network.proxy.https_port', port)
        # options.set_preference('network.proxy.ssl', ip)
        # options.set_preference('network.proxy.ssl_port', port)
       # change useragent
        options.set_preference("general.useragent.override",
                               f"{agent}")
        print(agent)
        options.set_preference("dom.webdriver.enabled", False)
        options.headless = False
        driver = webdriver.Firefox(
 #           executable_path=GeckoDriverManager().install(),
            options=options
        )
        actions = webdriver.ActionChains(driver)
        start = time.time()
        try:
            login_in_social_networks(driver, login_yt, password_yt,mail_yt, login_tw, password_tw, mail_tw, login_ok, password_ok, login_vk, password_vk, login_yandex, password_yandex, login_vktarget, password_vktarget,count)
            time.sleep(1)
            while True:
                if time.time() - start > 7200:
                    driver.get('https://google.com')
                    time.sleep(3600)
                    driver.get('https://vktarget.ru/login/')
                    start = time.time()
                else:
                    get_info_from_questions(driver, actions, key, count)
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
        finally:
            driver.close()
            driver.quit()
            input('Press ENTER to close this program')

    threads = list()
    count = -1
    result = list()
    result_day = list()
    for key in list(text_files):
        count += 1
        result.append(count)
        thread = threading.Thread(target=start_w, args=(key,count,))
        threads.append(thread)
    for i in threads:
        i.start()
        time.sleep(randint(20,30))

