class prova():
    def __init__(self):
        self.nome = "prova"
        self.nota 
    
    def get_nome(self):
        return self.nome
    
    def nota(self):
        if(self.nota >=0 and self.nota < 5):
           return "Suspes"
        elif(self.nota >= 5 and self.nota < 7):
            return "Aprovat"
        else:
            return "Excelent"

