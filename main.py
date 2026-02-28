from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

class Clave_sol:

    def __init__(self, razon_social): 
        self.razon_social = razon_social    

    def mostrar(self):
        
        completador = WordCompleter(sol.keys(), ignore_case=True)
        session = PromptSession(completer=completador)

        for key, value in self.razon_social.items():
            if key == session.prompt("Digitar razon social: "):                
                for dato in value:
                    print(dato)            

sol = {'alberto':['12345','usuario01','clave00a'],
        'carlos':['6789','usuario03','clave00c'],}

mi_sol = Clave_sol(sol)
mi_sol.mostrar()