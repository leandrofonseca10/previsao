import requests
from twilio.rest import Client

Api_Key = "8838be9516f93ece70b22d3865b9acc3"
cidade = "Longueuil"

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={Api_Key}&lang=pt_br"


requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = round(requisicao_dic['main']['temp'] - 273.15)
sensacao = round(requisicao_dic['main']['feels_like'] - 273.15)


print(descricao)
print(f"A temperatura esta {temperatura}ºC")
print(f"A sensacao termica esta {sensacao}ºC")

Account_SID = "ACb9aa983d53e3806413ee952ad07c624b"
Auth_Token = "8e48bc5cec2b474105de3bcaed57031f"
remetente = "+16813456079"
destino = "+14383042232","+14384666400"


if sensacao < 7:

    client = Client(Account_SID, Auth_Token)

    message = client.messages.create(
    to = destino,
    from_ = remetente,
    body = f"Hoje o tempo está {descricao}, a temperatura está {temperatura}°C com a sensação Térmica de {sensacao}°C , se for sair leve um casaco")

    print(message.sid)






#if sensacao < 4:

    # #enviando e-mail
    # import win32com.client as win32
    # outlook = win32.Dispatch('outlook.application')
    # mail = outlook.CreateItem(0)
    # mail.To = 'lg_fonseca@hotmail.com'
    # mail.Subject = "Informacao do Tempo"
    # mail.Body = "Teste"
    # mail.HTMLBody = f"""
    # <p>Olá Leandro, aqui é o código Python</p>

    # <p>A Temperatura baixou e esta {temperatura}ºC</p>
    # <p>E a sensacao termica esta {sensacao}ºC</p>"""
   

    # # To attach a file to the email (optional):
    # #attachment  = "C:\Python\Commodities\commodities.xlsx"
    # #mail.Attachments.Add(attachment)

    # mail.Send()