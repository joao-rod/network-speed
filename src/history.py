from datetime import datetime

def history(info, download, upload):
  try:
    with open('src/history', 'a') as file:
      file.write(f"{datetime.now().strftime('%d/%m/%Y')} - {datetime.now().strftime('%H:%M')}\n")
      file.write(f'local: {info["name"]}/{info["cc"]}\n')
      file.write(f'host: {info["host"]}\n')
      file.write(f'provedor: {info["sponsor"]}\n')
      file.write(f'download: {download}Mb/s\n')
      file.write(f'upload: {upload}Mb/s\n')
      file.write(f'latencia: {info["latency"]}/s\n\n')
  except FileNotFoundError:
    pass
  finally:
    file.close()
    print('\nUm log dessas informações estão salvas no arquivo history.')