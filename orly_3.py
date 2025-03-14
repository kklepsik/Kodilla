print('Zadania dla orłów - moduł 3')

print('Zadanie 1')

numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

for index in range(len(numbers)):
  numbers[index] = round(numbers[index], -1)

numbers.sort()
minimum = min(numbers)
maximum = max(numbers)

numbers = [number for number in numbers if number != minimum and number != maximum]

print(numbers)


mean_number = sum(numbers)/len(numbers)

print(round(mean_number))


print('Zadanie 2')

def build_bridge(chunk,goal):
  n = 1
  while True:
    most = n * chunk + (n - 1) * chunk / 2
    if most == goal:
      return True
    elif most > goal:
      return False
    else:
      n = n + 1

print(build_bridge(3,8))
print(build_bridge(10,30))
print(build_bridge(2, 98))


print('Zadanie 3')

models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','   Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = zip(models, sales2018, sales2017, sales2016)
for auto in cars:
  brand, model = auto[0].split(" - ")
  
print(list(cars))