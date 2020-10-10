import requests
import json
import string
import random
from random import randint

mailsCreated = []


def randomChar(y):
    return "".join(random.choice(string.ascii_letters) for x in range(y))


def generateRandomMail():
    return "{}@stressingYourDB.com".format(randomChar(randint(10, 35)))


def getMailsCreated():
    for emails in mailsCreated:
        return(emails)


def getToken():
    url = "https://api.xgrow.com/login"
    payload = {
        "email": "-2@gmail.com",
        "password": "12345678"
    }
    headers = {"content-type": "application/json"}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    tokenHere = r.json().get('token')
    f = open("validToken.txt", "w")
    f.write("Basic {}\n".format(tokenHere))
    f.close()
    print("Token created in validToken.txt!")
    return tokenHere


def testRegisterAnAccount():  # envia um requerimento de registro
    url = "https://api.xgrow.com/register"
    payload = {
        "name": "Testando o registro de contas",
        "lastName": "[TESTE]",
        "email": mailsCreated.append(generateRandomMail()),
        "password": "12345678",
        "type_user": "producer",
    }
    headers = {"content-type": "application/json"}
    return requests.post(url, data=json.dumps(payload), headers=headers)


def testSendingMail():
    url = "https://api.xgrow.com/forgot-password"
    payload = {"email": getMailsCreated()}
    headers = {"content-type": "application/json"}
    return requests.post(url, data=json.dumps(payload), headers=headers)


def testGetCourseInformation():
    url = 'https://api.xgrow.com/list-all-products'
    auth = getToken()
    headers = {'Authorization': auth}
    return requests.get(url, headers=headers).json()
    '''
    auth tirada de: 
    {
    "email": "-2@gmail.com",
    "password": "12345678"
    }
    '''


def testGetCheckoutInfo():
    url = 'https://api.xgrow.com/checkout-product/{}'.format(randint(1, 6))
    headers = {"content-type": "application/json", "Authorization": getToken()}
    return requests.get(url, headers=headers).json()


def switchValue(value):
    if value == 1:
        return testRegisterAnAccount()
    elif value == 2:
        return testSendingMail()
    elif value == 3:
        return testGetCheckoutInfo()
    elif value == 4:
        return testGetCourseInformation()
    elif value == 5:
        return getToken()


if __name__ == "__main__":
    while True:
        value = int(input("""\nVocê deseja:
[1] Teste de registro de contas
[2] Teste de disparo de emails
[3] Teste de múltiplos cliques de checkout
[4] Pegar a informação de todos os cursos
[5] Pegar o Token do Usuário produtor

[!] Digite aqui a sua escolha: """))
        howManyTestsDoYouWant = int(
            input("[!] Digite também o valor máximo de testes que será feito: "))
        for i in range(0, howManyTestsDoYouWant+1):
            print(switchValue(value))
