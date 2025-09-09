# 6.5 List Comprehension: Lista de Comprensión

nombres = ["Juan", "Ana", "Pedro", "Marta"]

algongP = [p for p in nombres if p[0] == "P"] # lista de comprensión para filtrar nombres que empiezan con "P"
print(algongP)

bottleC = [{"name": "qulmes", "country": "argentina"},
            {"name": "corona", "country": "mexico"},
            {"name": "budweiser", "country": "eeuu"},
            {"name": "stella artois", "country": "belgica"}]

argentina = [b for b in bottleC if b["country"] == "argentina"]
print(argentina)