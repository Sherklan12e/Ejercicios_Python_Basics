agua = ["creep", "davis", "correr", "manejar", "comer"]
sal = [ "saldelmar", "saldelbolivia", "saldeperu"]
print(agua)
agua.append("leer")


agua.insert(0, "canciones")
print(agua)
agua.remove("leer")
del agua[2]
agua.pop(1)

print(agua)
pesa = len(agua)
print(pesa)



"""agua.extend(sal)
print(agua)"""