from history import history
import speedtest

def conection():
  print('Carregando teste de rede...')

  conection = speedtest.Speedtest()
  print('Iniciando busca por servidores...')
  conection.get_servers()
  server = conection.get_best_server()

  print(f'''
  Local: {server['name']}/{server['cc']}
  Host: {server['host']}
  Provedor: {server['sponsor']}
  ''')

  print('Aguarde enquanto é calculada a velocidade da sua internet...')
  download = round(conection.download(threads=None)*(10**-6))
  print(f'Download: {download}Mb/s')
  upload = round(conection.upload(threads=None)*(10**-6))
  print(f'Upload: {upload}Mb/s')

  print(f'Latência: {server["latency"]}/s')

  history(server, download, upload)