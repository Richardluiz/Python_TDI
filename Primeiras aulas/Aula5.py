# Controle de Fluxo

def check_admin(username):
    admin = 'root@tdi'
    
    if username == admin:
     msg = "eh admin"
     
     
    elif username == "lucas@tdi":
         msg = "nao eh admin mas eh o lucas"
    
    else:
            msg = "nao eh admin"
        
    return msg


print(check_admin("bruno@tdi"))
print(check_admin("root@tdi"))
print(check_admin("lucas@tdi"))