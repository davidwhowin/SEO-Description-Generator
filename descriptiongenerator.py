from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
import pyperclip as pc
from selenium.webdriver.support import expected_conditions as ec
import random
from threading import Thread

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm, trange
from selenium.webdriver.common.action_chains import ActionChains

from threading import Thread

# the browser is still trying render so we must import time so we can wait for the browser for our changes
import time

# company Login Information
companyEmail = 'companyEmail.com'
companyPassword = 'companyPassword1'

#company Retail Login Information
companyRetailIGN = 'company@emailhere.com'
companyRetailPassword = 'companyPassword2'

# Static Locators
bodyDescriptionLocation = '/html/body/div[1]/div[3]/form/section[2]/div/div[2]/div/div[2]/div/div/div[2]'

# Description Template
packagingVariation = "NOTE: Please take into consideration that color samples and images may vary depending on screen and monitor settings. It is the buyer's responsibility to conduct research on the products they wish to purchase. Packaging may vary."

# tells python im using the chrome browser
from selenium.webdriver.common.by import By

# Descriptions - Keywords/Product Name
keywords = []
productName = ""

# login to Lightspeed
loginName = "lightspeedEmail"
passwordName = "lightspeedPassword"


def clearText(xpath):
    field = web.find_element((By.XPATH, xpath))
    field.clear()


def fillText(text, xpath):
    field = wait.until(ec.presence_of_element_located((By.XPATH,xpath)))
    field.send_keys(text)
def fillTextLogin(text, xpath):
    wait = WebDriverWait(web,4)
    field = wait.until(ec.presence_of_element_located((By.XPATH,xpath)))
    field.send_keys(text)
    wait = WebDriverWait(web,10)


def clickButton(xpath):
    field = wait.until(ec.presence_of_element_located((By.XPATH,xpath)))
    field.click()


def fillTextByCSS(text, css):
    field = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,css)))
    field.send_keys(text)


def pressButton(xpath):
    try:
        button = wait.until(ec.presence_of_element_located((By.XPATH,xpath)))
        web.execute_script("arguments[0].click();", button)

    except NoSuchElementException:
        print("")


def removeValueAttribute(xpath):
    web.execute_script("arguments[0].removeAttribute('value')", WebDriverWait(web, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))))


def removeAttribute(xpath):
    web.execute_script("arguments[0].removeAttribute('id')", WebDriverWait(web, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))))


# Fills in Text(HTML, <p> tags and other HTML tags with Action Chains
'''ActionChains are a way to automate low-level interactions such as mouse movements, mouse button actions, keypress, and context menu interactions.
                     This is useful for doing more complex actions like hover over and drag and drop. Action chain methods are used by advanced scripts where we need to
                      drag an element, click an element, double click, etc.'''


def deleteAllViaAC(xpath):
    # body description text box
    element = wait.until(ec.presence_of_element_located((By.XPATH,xpath)))
    # Populate Text in Body Paragraph
    action = ActionChains(web)
    # click the item
    action.click(on_element=element)
    # send keys
    action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
    action.send_keys(Keys.DELETE)
    # perform the operation
    action.perform()

def checkIfEmptyViaAC(xpath):
    pc.copy('')
    # body description text box
    element = wait.until(ec.presence_of_element_located((By.XPATH,xpath)))
    # Populate Text in Body Paragraph
    action = ActionChains(web)
    # click the item
    action.click(on_element=element)
    # send keys
    time.sleep(1)
    action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
    time.sleep(1)
    action.key_down(Keys.CONTROL).send_keys('C')
    action.key_up(Keys.CONTROL)
    time.sleep(1)
    # perform the operation
    action.perform()
    #copy windows clipboard
    textInsideBox = pc.paste()

    if not textInsideBox:
        print("\nNo Description Found.\n")
        return True
    else:
        return False


def fillTextViaAC(text, xpath):
    # body description text box
    element = wait.until(ec.presence_of_element_located((By.XPATH,xpath)))
    # Populate Text in Body Paragraph
    action = ActionChains(web)
    # click the item
    action.click(on_element=element)
    # go to end of document
    action.key_down(Keys.CONTROL).send_keys(Keys.END).key_up(Keys.CONTROL)
    # send keys
    action.send_keys(text)
    time.sleep(1)
    action.send_keys(Keys.ENTER)
    time.sleep(1)
    action.send_keys(Keys.ENTER)
    # perform the operation
    action.perform()


def check_exists_by_xpath(xpath):
    try:
        web.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def listToString(list):
    # initialize an empty string
    str = list[0]

    # traverse string
    for element in list[1:]:
        str = str + ", " + element

    # return str1
    return str


def copyOutputToClipboard(array):
    toString = listToString(array)
    pc.copy(toString)
    print(toString)


def copyText(xpath):
    word = web.find_element(By.XPATH, xpath).text
    return word


def enquiry(list):
    if not list:
        return 1
    else:
        return 0


def waitForButton(xpath):
    WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


# function that returns true if the text box is true
def textIsEmpty(xpath):
    inputBox = web.find_element(By.XPATH, xpath)
    textInsideInputBox = inputBox.get_attribute('value')

    if textInsideInputBox == '':
        return True
    else:
        return False


def getButtonURL(xpath):
    for a in web.find_elements(By.XPATH, xpath):
        text = a.get_attribute('href')
        print(a.get_attribute('href'))
        return text


def getKeywords(productName, url):
    array = []
    print("Get Keywords")

    web.execute_script("window.open('');")

    # switch to the new window and open URL B
    web.switch_to.window(web.window_handles[2])
    web.get(
        'https://www.wordstream.com/keywords?camplink=mainnavbar&campname=KWT&cid=Web_Any_Products_Keywords_Grader_KWTool')

    # Enter input to message box
    fillText(url, '/html/body/div[2]/div/article/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')


    # click the search keyword term
    clickButton('/html/body/div[2]/div/article/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[2]/input[1]')

    # click the refine your search with industry/location
    clickButton('/html/body/div[3]/div[3]/div/div/form/div/div[3]/div/div/div/button')

    time.sleep(8)

    count = 1
    while count < 5:
        value = '/html/body/div[2]/div/div[2]/div/div/div/div[2]/div[3]/table/tbody/tr[' + str(count) + ']/th'

        try:
            word = web.find_element(By.XPATH, value).text
            array.append(word)
            count = count + 1
        except NoSuchElementException:
            print("No more elements.")
            break

    # splice the array to to only grab 12 elements from the web page
    descriptionList = [
        'beautiful', 'gorgeous', 'amazing',
        'durable', 'strong',
        'professional', 'luxurious', 'undefined beauty',
        'lovely', 'exquisite', 'heavenly',
        'breathtaking', 'stunning', 'aesthetic',
        'glorious', 'magnificent', 'ravishing',
        'brilliant', 'impressive', 'marvelous',
        'elegant','refreshing'
    ]
    random.shuffle(descriptionList)

    array.append(descriptionList[0])
    array.append(descriptionList[1])
    array.append(descriptionList[2])

    # Splices the array to only include a # of elements
    # array = array[:11]

    # close wordstream and go back to other tab
    web.close()
    web.switch_to.window(web.window_handles[1])

    time.sleep(2)
    return array


def getDashwordDescription(productName, keywords):
    try:
        fillText('emailAddress', '/html/body/div[1]/div/div/div/form/div[1]/input')
        fillText('!t6WxJ6gGk8WmWw', '/html/body/div[1]/div/div/div/form/div[2]/input')
        clickButton('/html/body/div[1]/div/div/div/form/div[4]/button')
    except NoSuchElementException:
        print("Already log in.")

    fillTextByCSS(productName, '#subject')
    fillTextByCSS(keywords, '#keywords')

    try:
        button = web.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[2]/div/div[1]/form/div[3]/button')
        web.execute_script("arguments[0].click();", button)

        time.sleep(2)
    except NoSuchElementException:
        print("")

    time.sleep(4)

    description = copyText('/html/body/div[2]/div/div[3]/main/div[2]/div/div[2]/div/div[1]/p')

    # description = copyText('/html/body/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/p')

    return description


# Seo Meta Description by WriteCream
def getSeoMetaDescription(productName, keywords):
    web.execute_script("window.open('');")

    # switch to the new window and open URL B
    web.switch_to.window(web.window_handles[2])
    web.get(
        'https://app.writecream.com/seo-meta-description')

    time.sleep(2)

    # WriteCream Home Page
    # Writecream Username and Password Fields
    try:
        fillTextLogin(companyEmail, '/html/body/div[1]/div[3]/div/div/div[2]/form/div[1]/input')
        fillTextLogin(companyPassword, '/html/body/div[1]/div[3]/div/div/div[2]/form/div[2]/input')

        # Log In Button
        pressButton('/html/body/div[1]/div[3]/div/div/div[2]/button')
    except NoSuchElementException:
        print("Already Logged In")
    except TimeoutException:
        print("Bypassing Login Screen")

    # Clear Product/Brand Names
    removeValueAttribute(
        '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[2]/input')
    fillText(productName,
             '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[2]/input')

    # Clear Product Description
    textBox = web.find_element(By.XPATH,
                               '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/textarea')
    textBox.send_keys(Keys.CONTROL, 'a')
    textBox.send_keys((Keys.BACKSPACE))

    fillText(keywords,
             '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/textarea')

    # Generate SEO Meta Description
    pressButton('/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')

    time.sleep(3)

    # Copy Text and check to see if 160 Characters
    seoMetaDescription = copyText(
        '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[3]/div/div[1]/p/strong')
    print(seoMetaDescription)
    print("The Description has " + str(len(seoMetaDescription)) + " characters")

    count = 2

    # Get Seo Meta Description around 120-160 characters long
    while len(seoMetaDescription) > 160 or len(seoMetaDescription) < 120:
        # Cycle through each description and check if they have 120-160 characters
        if count < 4:
            try:
                # Copy The Text
                seoMetaDescription = copyText(
                    '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[3]/div/div[' + str(
                        count) + ']/p/strong')
                print(seoMetaDescription)
                print("The Description has " + str(len(seoMetaDescription)) + " characters")
                # Increases the count of the meta description
                count += 1
            except:
                # If element on page fails, the machine presses this button to generate a new set of tasks
                pressButton(
                    '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')
                time.sleep(2)
        else:
            # No more elements remain, generates a new set of tasks
            pressButton('/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')
            # Sets the Meta XPATH Description to the first element and then repeats the process.
            count = 1
            time.sleep(2)

    print()
    print("Description Found.")

    # close dashword and go back to other tab
    web.close()
    web.switch_to.window(web.window_handles[1])

    time.sleep(2)

    return seoMetaDescription


def getWriteCreamDescription(productName, keywords):
    web.execute_script("window.open('');")

    # switch to the new window and open URL B
    web.switch_to.window(web.window_handles[2])
    web.get(
        'https://app.writecream.com/product-description')

    # WriteCream Home Page
    # Writecream Username and Password Fields
    try:
        fillTextLogin(companyEmail, '/html/body/div[1]/div[3]/div/div/div[2]/form/div[1]/input')
        fillTextLogin(companyPassword, '/html/body/div[1]/div[3]/div/div/div[2]/form/div[2]/input')

        # Log In Button
        pressButton('/html/body/div[1]/div[3]/div/div/div[2]/button')
    except NoSuchElementException:
        print("Already Logged In")
    except TimeoutException:
        print("Bypassing Login Screen")

    # Clear Product/Brand Names
    removeValueAttribute(
        '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[2]/input')
    fillText(productName,
             '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[2]/input')

    # Clear Product Description
    textBox = web.find_element(By.XPATH,
                               '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/textarea')
    textBox.send_keys(Keys.CONTROL, 'a')
    textBox.send_keys((Keys.BACKSPACE))

    fillText(keywords,
             '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/textarea')

    # Generate SEO Meta Description
    pressButton('/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')

    time.sleep(3)

    # Copy Text and check to see if 160 Characters
    ecommerceProductDescription = copyText(
        '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[3]/div/div[1]/p/strong')
    print(ecommerceProductDescription)
    print("The Description has " + str(len(ecommerceProductDescription)) + " characters")

    count = 2

    # Get Seo Meta Description around 120-160 characters long
    while len(ecommerceProductDescription) > 256 or len(ecommerceProductDescription) < 140:
        # Cycle through each description and check if they have 120-160 characters
        if count < 4:
            try:
                # Copy The Text
                ecommerceProductDescription = copyText(
                    '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[3]/div/div[' + str(
                        count) + ']/p/strong')
                print(ecommerceProductDescription)
                print("The Description has " + str(len(ecommerceProductDescription)) + " characters")
                # Increases the count of the meta description
                count += 1
            except:
                # If element on page fails, the machine presses this button to generate a new set of tasks
                pressButton(
                    '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')
                time.sleep(2)
        else:
            # No more elements remain, generates a new set of tasks
            pressButton('/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')
            # Sets the Meta XPATH Description to the first element and then repeats the process.
            count = 1
            time.sleep(2)

    print()
    print("Description Found.")

    # close dashword and go back to other tab
    web.close()
    web.switch_to.window(web.window_handles[1])

    time.sleep(2)

    return ecommerceProductDescription


def getFeatureBenefit(productName, keywords):
    web.execute_script("window.open('');")

    # switch to the new window and open URL B
    web.switch_to.window(web.window_handles[2])
    web.get(
        'https://app.writecream.com/blog-heading-expand')

    # WriteCream Home Page
    # Writecream Username and Password Fields
    try:
        fillTextLogin(companyEmail, '/html/body/div[1]/div[3]/div/div/div[2]/form/div[1]/input')
        fillTextLogin(companyPassword, '/html/body/div[1]/div[3]/div/div/div[2]/form/div[2]/input')

        # Log In Button
        pressButton('/html/body/div[1]/div[3]/div/div/div[2]/button')
    except NoSuchElementException:
        print("Already Logged In")
    except TimeoutException:
        print("Bypassing Login Screen")

    # Clear Product/Brand Names
    removeValueAttribute(
        '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[2]/input')
    fillText(productName,
             '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[2]/input')

    # Clear Product Description
    textBox = web.find_element(By.XPATH,
                               '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/textarea')
    textBox.send_keys(Keys.CONTROL, 'a')
    textBox.send_keys((Keys.BACKSPACE))

    fillText(keywords,
             '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/textarea')

    # Clear Section Headline
    textBox = web.find_element(By.XPATH,
                               '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[6]/input')
    textBox.send_keys(Keys.CONTROL, 'a')
    textBox.send_keys(Keys.BACKSPACE)

    fillText(productName,
             '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[6]/input')

    # Generate SEO Meta Description
    pressButton('/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')

    time.sleep(3)

    # Copy Text and check to see if 160 Characters
    ecommerceProductDescription = copyText(
        '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[3]/div/div[1]/p/strong')
    print(ecommerceProductDescription)
    print("The Description has " + str(len(ecommerceProductDescription)) + " characters")

    count = 2

    # Get Seo Meta Description around 120-160 characters long
    while len(ecommerceProductDescription) > 250 or len(ecommerceProductDescription) < 150:
        # Cycle through each description and check if they have 120-160 characters
        if count < 4:
            try:
                # Copy The Text
                ecommerceProductDescription = copyText(
                    '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[3]/div/div[' + str(
                        count) + ']/p/strong')
                #print(ecommerceProductDescription)
                #print("The Description has " + str(len(ecommerceProductDescription)) + " characters")
                # Increases the count of the meta description
                count += 1
            except:
                # If element on page fails, the machine presses this button to generate a new set of tasks
                pressButton(
                    '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')
                time.sleep(2)
        else:
            # No more elements remain, generates a new set of tasks
            pressButton('/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')
            # Sets the Meta XPATH Description to the first element and then repeats the process.
            count = 1
            time.sleep(2)

    print(ecommerceProductDescription)
    print("The Description has " + str(len(ecommerceProductDescription)) + " characters")
    print()
    print("Feature Benefits Found.")

    # close dashword and go back to other tab
    web.close()
    web.switch_to.window(web.window_handles[1])

    time.sleep(2)

    return ecommerceProductDescription


def getCompellingPoints(productName, keywords):
    web.execute_script("window.open('');")

    # switch to the new window and open URL B
    web.switch_to.window(web.window_handles[2])
    web.get(
        'https://app.writecream.com/bullet-points')

    # WriteCream Home Page
    # Writecream Username and Password Fields
    try:
        fillTextLogin(companyEmail, '/html/body/div[1]/div[3]/div/div/div[2]/form/div[1]/input')
        fillTextLogin(companyPassword, '/html/body/div[1]/div[3]/div/div/div[2]/form/div[2]/input')

        # Log In Button
        pressButton('/html/body/div[1]/div[3]/div/div/div[2]/button')
    except NoSuchElementException:
        print("Already Logged In")
    except TimeoutException:
        print("Already Logged In")


    # Clear Product/Brand Names
    removeValueAttribute(
        '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[2]/input')
    fillText(productName,
             '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/div[2]/input')

    # Clear Product Description
    textBox = web.find_element(By.XPATH,
                               '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/textarea')
    textBox.send_keys(Keys.CONTROL, 'a')
    textBox.send_keys((Keys.BACKSPACE))

    fillText(keywords,
             '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/textarea')

    # Generate SEO Meta Description
    pressButton('/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')

    time.sleep(3)

    # Copy Text and check to see if 160 Characters
    ecommerceProductDescription = copyText(
        '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[3]/div/div[1]/p/strong')
    print(ecommerceProductDescription)
    print("The Description has " + str(len(ecommerceProductDescription)) + " characters")

    count = 2

    # Get Seo Meta Description around 120-160 characters long
    while len(ecommerceProductDescription) > 300 or len(ecommerceProductDescription) < 100:
        # Cycle through each description and check if they have 120-160 characters
        if count < 4:
            try:
                # Copy The Text
                ecommerceProductDescription = copyText(
                    '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[3]/div/div[' + str(
                        count) + ']/p/strong')
                #print(ecommerceProductDescription)
                #print("The Description has " + str(len(ecommerceProductDescription)) + " characters")
                # Increases the count of the meta description
                count += 1
            except:
                # If element on page fails, the machine presses this button to generate a new set of tasks
                pressButton(
                    '/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')
                time.sleep(2)
        else:
            # No more elements remain, generates a new set of tasks
            pressButton('/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/ul/div/div[1]/button')
            # Sets the Meta XPATH Description to the first element and then repeats the process.
            count = 1
            time.sleep(2)

    print(ecommerceProductDescription)
    print("The Description has " + str(len(ecommerceProductDescription)) + " characters")
    print()
    print("Bullet Points Found")
    # close dashword and go back to other tab
    web.close()
    web.switch_to.window(web.window_handles[1])

    time.sleep(2)

    return ecommerceProductDescription

#5 Main Description Getters
def getBodyDescription(bodyParagraphsAdded):
    # Body Description
    # Must go through a unique check to see it works
    if checkIfEmptyViaAC(bodyDescriptionXPATH):
        print("Your body description is empty, creating body description...")
        # click the body description button and fill in text according to Product
        clickButton('/html/body/div[1]/div[3]/form/section[2]/div/div[2]/div/div[2]/div/div/div[2]')

        print("Getting Body Description...")
        fillTextViaAC('Product Name: ' + productName, bodyDescriptionXPATH)

        print("Generating Feature Benefits...")
        featureBenefits = getFeatureBenefit(productName, keywords)

        print(featureBenefits)
        fillTextViaAC(featureBenefits, bodyDescriptionXPATH)

        # time.sleep(2)

        fillTextViaAC('Features: ', bodyDescriptionXPATH)
        # time.sleep(2)

        print("Generating Compelling Points...")
        compellingPoints = getCompellingPoints(productName, keywords)
        fillTextViaAC(compellingPoints, bodyDescriptionXPATH)

        # time.sleep(2)

        '''ActionChains are a way to automate low-level interactions such as mouse movements, mouse button actions, keypress, and context menu interactions.
             This is useful for doing more complex actions like hover over and drag and drop. Action chain methods are used by advanced scripts where we need to
              drag an element, click an element, double click, etc.'''

        #fillTextViaAC(packagingVariation, bodyDescriptionXPATH)

        # time.sleep(2)

        bodyParagraphsAdded += 1

        print("Body Description Added")
        return bodyParagraphsAdded

def getHeaderDescription(descriptionsAdded):
    # Header Description
    if textIsEmpty(descriptionXPATH):
        print("Getting Description for Header...\n")

        # fill in Header Description
        headerDescription = getWriteCreamDescription(productName, keywords)
        fillText(headerDescription, descriptionXPATH)

        descriptionsAdded += 1

        print("Header Description Added")
        return descriptionsAdded

def getMetaKeywords(metaKeywordsAdded):
    # Adding in Meta Keywords
    if textIsEmpty(metaKeywordsXPATH):
        print("Getting Meta Keywords...\n")
        # Fill in meta keywords
        fillText(keywords, metaKeywordsXPATH)
        metaKeywordsAdded += 1
        print('Meta Keywords Added')
        return metaKeywordsAdded

def getMetaDescription(metaDescriptionsAdded):
    if textIsEmpty(metaDescriptionXPATH):
        print("Getting Meta Description...\n")

        # fill in Meta Keywords
        metaDescription = getSeoMetaDescription(productName, keywords)
        fillText(metaDescription, metaDescriptionXPATH)

        metaDescriptionsAdded += 1
        print('Meta Description Added')
        return metaDescriptionsAdded

def getGoogleCategory(googleCategoriesAdded):
    if textIsEmpty(googleCategoryXPATH):
        print("Getting Google Category Number...\n")

        # fill in google category number
        fillText('2683', googleCategoryXPATH)

        googleCategoriesAdded += 1
        print('Google Category Added')
        return googleCategoriesAdded

menu = 0
while menu < 100:
    print()
    print('1. Get Keywords\n'
          '2. Get Product Description\n'
          '3. Update Product\n'
          '4. Shuffle List\n'
          '5. Get Keywords via Semrush')

    menu = int(input("Pick a menu option: "))

    # Get Keywords
    if menu == 1:
        keywords.clear()
        productName = ""
        print("Getting Keywords, Please Standby...")
        productName = input("Enter the product name: ")

        web = webdriver.Chrome()
        web.get(
            'https://www.wordstream.com/keywords?camplink=mainnavbar&campname=KWT&cid=Web_Any_Products_Keywords_Grader_KWTool')
        time.sleep(2)

        # Enter input to message box
        wordSearch = web.find_element(By.XPATH,
                                      '/html/body/div[2]/div/article/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')
        wordSearch.send_keys(productName)
        # click the search keyword term
        findMyKeywords = web.find_element(By.XPATH,
                                          '/html/body/div[2]/div/article/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[2]/input[1]')
        findMyKeywords.click()

        time.sleep(3)
        # click the refine your search with industry/location
        findMyKeywords = web.find_element(By.XPATH,
                                          '/html/body/div[3]/div[3]/div/div/form/div/div[3]/div/div/div/button')
        findMyKeywords.click()

        time.sleep(8)

        count = 1
        while count < 20:

            value = '/html/body/div[2]/div/div[2]/div/div/div/div[2]/div[3]/table/tbody/tr[' + str(count) + ']/th'
            if (check_exists_by_xpath(value)):
                word = web.find_element(By.XPATH, value).text
                keywords.append(word)

            count = count + 1

        # splice the array to to only grab 12 elements from the web page
        keywords = keywords[:5]
        # random.shuffle(keywords)

        # keywords.append('nail supply')
        # keywords.append('salon supply')
        # keywords.append('spa supply')

        copyOutputToClipboard(keywords)
        web.close()  # closes the browser

    elif menu == 2:
        print('2')


    # Lightspeed Access
    elif menu == 3:
        print()

        dashwordURL = 'https://app.dashword.com/meta-description-generator'

        product = input('Enter the name of the product you want to search: ')

        web = webdriver.Chrome()
        print("Log into Lightspeed")

        web.get('Paste Shop Lightspeed link here')
        web.maximize_window()

        wait = WebDriverWait(web, 10)

        #Static Wait Element
        wait = WebDriverWait(web,10)

        # login description
        loginName = loginName
        passwordName = passwordName

        # log into Lightspeed
        fillText(loginName, '/html/body/div[1]/div/form/div/div[1]/input')
        fillText(passwordName, '/html/body/div[1]/div/form/div/div[2]/input')
        clickButton('/html/body/div[1]/div/form/div/div[3]/button')

        # Clicking through a series of buttons to product page of lightspeed

        clickButton('/html/body/div[1]/div[2]/nav/ul/li[4]/div/a')

        clickButton('/html/body/div[1]/div[3]/div[4]/div/div/table/thead/tr/th[6]/span')
        clickButton('/html/body/div[1]/div[3]/div[4]/div/div/table/thead/tr/th[6]/span')

        # while page elements exist, loops through each element and checks for a description

        # inventory position
        count = 43

        # search function to search for a specific product
        print("Searching for " + product)

        fillText(product, '/html/body/div[1]/div[3]/div[3]/div/div[1]/div/div[1]/form/input')

        clickButton('/html/body/div[1]/div[3]/div[3]/div/div[2]/a/i')

        # Enter the page number you want to access and this will go right to it
        field = web.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[5]/div/div/form/input[1]')

        pageCount = 29

        field.send_keys(pageCount, Keys.ENTER)
        field.send_keys(Keys.ENTER)

        time.sleep(4)

        descriptionsAdded = 0
        metaKeywordsAdded = 0
        metaDescriptionsAdded = 0
        numberOfUnitsProcessed = 0
        bodyParagraphsAdded = 0
        googleCategoriesAdded = 0

        xpath = '/html/body/div[1]/div[3]/div[4]/div/div/table/tbody/tr[' + str(count) + ']/td[3]/a'

        #Max Number of Inventory Pages - I probably could change this to be more technically but im lazy
        while pageCount <= 220:

            print(
                '-------------------- \n'
                + '     Page ' + str(pageCount) + '\n' +
                '--------------------')

            while check_exists_by_xpath(xpath):
                lightspeedListingURL = getButtonURL(xpath)

                # open a new window
                web.execute_script("window.open('');")

                # switch to the new window and open URL B
                web.switch_to.window(web.window_handles[1])
                web.get(lightspeedListingURL)

                # The element you are targeting is a TEXTAREA. .text gets the text between the open and close tags of an element, e.g. <div>.text gets this text<div>.
                # The TEXTAREA element holds it's text inside the value attribute. You can get this using

                time.sleep(2)
                productName = web.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/section[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/input').get_attribute("value")

                print(str(count) + '.' + ' ' + productName)
                descriptionXPATH = '/html/body/div[1]/div[3]/form/section[1]/div/div[2]/div[1]/div/div[4]/div[2]/div/textarea'
                metaDescriptionXPATH = '/html/body/div[1]/div[3]/form/section[1]/div/div[2]/div[2]/div/div/div/div[3]/label[3]/textarea'
                metaKeywordsXPATH = '/html/body/div[1]/div[3]/form/section[1]/div/div[2]/div[2]/div/div/div/div[3]/label[4]/input'
                bodyDescriptionXPATH = '/html/body/div[1]/div[3]/form/section[2]/div/div[2]/div/div[2]/div/div/div[2]'
                googleCategoryXPATH = '/html/body/div[1]/div[3]/form/section[1]/div/div[2]/div[2]/div/div/div/div[3]/label[6]/input'

                clickButton('/html/body/div[1]/div[3]/form/section[1]/div/div[2]/div[2]/div/div/div/div[2]/div/button')

                #Go through multiple checks to see if Input Field is empty.
                #if textIsEmpty(metaKeywordsXPATH):

                if textIsEmpty(descriptionXPATH) or textIsEmpty(metaKeywordsXPATH) or textIsEmpty(
                        bodyDescriptionXPATH) or textIsEmpty(metaDescriptionXPATH) or textIsEmpty(googleCategoryXPATH) or checkIfEmptyViaAC(bodyDescriptionXPATH):
                    keywordList = []
                    keywords = ''

                    print("Description does not exist, creating description...")

                    # productName = copyText('/html/body/div[1]/div[3]/form/section[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/input')
                    button = '/html/body/div[1]/div[3]/form/section[1]/div/div[1]/div[2]/div[2]/a[2]'
                    buttonURL = getButtonURL(button)

                    print('Progress: ░░░░░░░░░░░░░ 0%')


                    if buttonURL is None:
                        try:
                            button = '/html/body/div[1]/div[3]/form/section[1]/div/div[1]/div[2]/div[2]/a'
                            buttonURL = getButtonURL(button)
                        except NoSuchElementException:
                            buttonURL = productName

                    print(buttonURL)

                    keywordList = getKeywords(productName, buttonURL)

                    keywords = listToString(keywordList)

                    #Function that check each input box values

                    threads=[
                        Thread(target=getBodyDescription(bodyParagraphsAdded)),
                        Thread(target=getHeaderDescription(descriptionsAdded)),
                        Thread(target=getMetaKeywords(metaKeywordsAdded)),
                        Thread(target=getMetaDescription(metaDescriptionsAdded)),
                        Thread(target=getGoogleCategory(googleCategoriesAdded))
                    ]

                   #run in separate threads
                    for thread in threads:
                        print("Starting thread")
                        thread.start()

                    #wait until all threads have finished
                    for thread in threads:
                        thread.join()



                    # Save button
                    time.sleep(2)
                    pressButton('/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[2]/button')

                    time.sleep(2)
                    print('Progress: ████████████ 100%\n')
                    print()

                    print("Header Descriptions Added: ", format(descriptionsAdded, '>12,.2f'))
                    print("Meta Keywords Added: ", format(metaKeywordsAdded, '>18,.2f'))
                    print("Meta Descriptions Added: ", format(metaDescriptionsAdded, '>14,.2f'))
                    print("Body Descriptions Added: ", format(bodyParagraphsAdded, '>14,.2f'))
                    print("Google Categories Added: ", format(googleCategoriesAdded, '>14,.2f'))



                else:
                    print('Progress: ████████████ 100%')
                    print("Description already finished")

                    print("Header Descriptions Added: ", format(descriptionsAdded, '>12,.2f'))
                    print("Meta Keywords Added: ", format(metaKeywordsAdded, '>18,.2f'))
                    print("Meta Descriptions Added: ", format(metaDescriptionsAdded, '>14,.2f'))
                    print("Body Descriptions Added: ", format(bodyParagraphsAdded, '>14,.2f'))
                    print("Google Categories Added: ", format(googleCategoriesAdded, '>14,.2f'))

                    # print('Total Meta Keywords Added')
                    # print('Total Meta Descriptions Added')
                    print('')

                    time.sleep(2)

                web.close()
                web.switch_to.window(web.window_handles[0])

                time.sleep(2)

                count += 1
                numberOfUnitsProcessed += 1

                print("Number of Units Processed: ", format(numberOfUnitsProcessed, '>12,.2f'))

                print('\nCurrent Page: ' + str(pageCount) + ' | Current Item Number: ' + str(count))
                print()

                xpath = '/html/body/div[1]/div[3]/div[4]/div/div/table/tbody/tr[' + str(count) + ']/td[3]/a'

            # access the next page

            count = 1
            xpath = '/html/body/div[1]/div[3]/div[4]/div/div/table/tbody/tr[' + str(count) + ']/td[3]/a'
            clickButton('/html/body/div[1]/div[3]/div[5]/div/div/div[4]/button[1]')
            pageCount += 1
            time.sleep(4)

    # shuffle keywords
    elif menu == 4:

        if enquiry(keywords):
            print("You have no keywords")
            continue
        else:
            random.shuffle(keywords)
            copyOutputToClipboard(keywords)

    else:
        print("Invalid option")
