import requests # Fazer requisições http
from pathlib import Path


def send_file():
    # Caminho do arquivo para upload
    file_path = Path(r"C:\Users\luana\Downloads\produtos_informatica.xlsx")

    # Enviar arquivo
    server = "store7"
    request = requests.post(url=f'https://{server}.gofile.io/contents/uploadfile', files={'file': open(file_path, 'rb')})
    request_output = request.json()

    print(request_output)
    url = request_output.get('data', {}).get('downloadPage', 'Chave não encontrada')
    print("Arquivo enviado. Link para acesso:", url)

def receive_file(file_url):
    request = requests.get(file_url)

    # Salvar o arquivo
    if request.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(request.content)
            print("Arquivo baixado com sucesso.")
    else:
        print("Erro ao baixar o arquivo: ", request.json())

def send_key_file():
    # Caminho do arquivo e chave para upload
     file_path= Path(r"C:\Users\luana\Downloads\produtos_informatica.xlsx")
     api_key = 'YMqL7St6HRlz4vNn8fNetz7RoINLxrHO'

     server = "store7"
     request = requests.post(
         url=f'https://{server}.gofile.io/contents/uploadfile',
         files={'file': open(file_path, 'rb')},
         headers={'Authorization': api_key}
     )
     request_output = request.json()

     print(request_output)
     url = request_output.get('data', {}).get('downloadPage', 'Chave não encontrada')
     print("Arquivo enviado. Link para acesso:", url)

send_file()
receive_file('https://gofile.io/d/EOXZ87')
send_key_file()