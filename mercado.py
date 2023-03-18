frutas = {'Plátano':5000, 'Manzana':10000, 'Pera':10000, 'Naranja':5000, 'Mandarina':3800,'Uva':8500,'Fresa':14000 ,'Maracuya':22000 }
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, 'cop')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")