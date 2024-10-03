import requests,os
server = 'server.domain.local'
patchbd = '\\\\server\\share\'
username = os.getlogin()
link = f'http://{server}:8500/v1/kv/{username}?raw'
response = requests.get(link)
response.encoding = 'UTF-8'
bases = response.text
if len(bases) > 0:
    bases = [base.replace('\n', '').strip() for base in bases.split(',')]
    cfg = f'C:\\Users\\{username}\\AppData\\Roaming\\1C\\1CEStart\\1cestart.cfg'
    patch_cfg = f'C:\\Users\\{username}\\AppData\\Roaming\\1C\\1CEStart\\'
    os.makedirs(patch_cfg, exist_ok=True)
    file = open(cfg, mode="w")
    for i in bases:
        w = f'CommonInfoBases={patch-db}\{i}.v8i'
        file.write(w + '\n')
    file.write('UseHWLicenses=1' + '\n')
    file.write('AppAutoInstallLastVersion=1')
    file.close()
    os.system('"C:/Program Files/1cv8/common/1cestart.exe"')
else:
    os.system('"C:/Program Files/1cv8/common/1cestart.exe"')
