# Loops

alvos = [{'ip':'192.168.1.8', 'so':
    "windows", 'ativo': True, 'portas':[80, 22, 21]}, {'ip': '192.168.1.9', 'so': "linux",
    'ativo':True, 'portas': [80]}]


# nmap IP

for alvo in alvos:
    if alvo["so"] == "linux":
        print("atacando o linux")
        
        print("#############################")
        
        {'ip':'192.168.1.8', 'so':
    "windows", 'ativo': True, 'portas':[80, 22, 21]}
        
        for alvo in alvos:
            if alvo["ativo"]:
                print(["ip"])
            for porta in alvo["portas"]:
                   print("atacando a porta: " +str (porta))
                   print("#######")
        
        
        
        print("################################")
        
        def encontra_windows(alvos):
            for alvo in alvos:
                if alvo["so"] == "windows":
                    print("encontrei um windows")
                    break
                
                encontra_windows(alvos)
                
                
                print("######################")
                
                
                for alvo in alvos:
                    if alvo["so"] == "linux":
                        print("nao ataquei pq eh linux")
                        continue
                    print("atacando pq nao eh linux")
        
        