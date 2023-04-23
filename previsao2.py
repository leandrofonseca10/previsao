import requests
import win32com.client as win32

Api_Key = "8838be9516f93ece70b22d3865b9acc3"
cidade = "Longueuil"

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={Api_Key}&lang=pt_br"

link2 = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?q={cidade}&appid={Api_Key}"


requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = round(requisicao_dic['main']['temp'] - 273.15)
sensacao = round(requisicao_dic['main']['feels_like'] - 273.15)


print(descricao)
print(f"{temperatura}ºC")
print(f"{sensacao}ºC")


if sensacao > 4:

    #enviando e-mail
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'lg_fonseca@hotmail.com'
    mail.Subject = "Informacao do Tempo"
    mail.Body = "Teste"
    mail.HTMLBody = f"""
    <p>Olá Leandro, aqui é o código Python</p>

    <p>A Temperatura baixou e esta {temperatura}ºC</p>
    <p>E a sensacao termica esta {sensacao}ºC</p>"""
   

    # To attach a file to the email (optional):
    #attachment  = "C:\Python\Commodities\commodities.xlsx"
    #mail.Attachments.Add(attachment)

    mail.Send()
