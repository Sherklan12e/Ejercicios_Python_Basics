class alumno():
    def datos(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print('Nombre: ',self.nombre)
        print('Nota: ', self.nota)
    def resultado(self):
        if self.nota < 5:
            print('Has reprobado!HAHAHHAHAHA')
        else:
            print('Has aprobado! congratulations')
            
            
alumno1 = alumno()

alumno1.datos('dev', 4)
alumno2 = alumno()

alumno2.datos('michael', 8)

alumno1.resultado()