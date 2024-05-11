from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#Declaración de usuario y contraseña
USERNAME = 'hscroot
PASSWORD = 'abcd1234'


#Importación del path para el modulo webdriver
service = Service(r"C:\chromedriver-win64\chromedriver.exe")


#Importación de cabeceras
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')


#Ignoramos los certificados
driver = webdriver.Chrome(service=service, options=chrome_options)


#Declaración de la url y metodo get
driver.get("https://192.168.3.11/hmc/connect")


#Mandanos a llamar el xpath del campo user
xpath_query="//input[contains(@id,'ccfw_username')]"
user_input = driver.find_element("xpath", xpath_query ) 
user_input.send_keys(USERNAME)

#Mandamos a llamar el xpath del campo pasvord
xpath_quary2"//input[contains(@id, 'ccfw_password')]" 
password_input = driver.find_element("xpath", xpath_query2) 
password_input.send_keys(PASSWORD)

#Mandamos a llamar el xpath del campo Button 
xpath_login = "//input[contains(@id, 'submitButton'))" 
login_button = driver.find_element("xpath", xpath_login) 

#Mandamos a llamar la funcion click() para loggearnos 
login_button.click()