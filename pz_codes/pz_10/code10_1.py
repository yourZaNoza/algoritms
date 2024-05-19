# Вариант 20
# Известны марки машин, выпускаемые в данной стране и экспортируемых в № заданных стран.
# Определить какие марки машин были доставлены во все указанные страны,
# какие в некоторые из стран и какие не доставлены ни в одну страну.

delivery_info = {
    "Lada": [""],
    "UAZ": [""],
    "GAZ": [""],
    "Mercedes-Benz": ["Германия", "Россия", "CША", "Китай"],
    "BMW": ["Германия", "Россия", "CША", "Китай"],
    "Volkswagen": ["Германия", "Россия", "CША", "Китай"],
    "Ford": ["Германия", "Россия", "CША", "Китай"],
    "Chevrolet": ["Германия", "Россия", "CША", "Китай"],
    "Tesla": ["США", "Китай"],
    "Toyota": ["Германия", "Россия", "США"],
    "Nissan": ["Китай", "Германия", "Россия"],
    "Honda": [""],
}


countries = ["Россия", "Германия", "США", "Китай"]
all_delivered_cars = set()
some_delivered_cars = set()
not_delivered_cars = set()

for car_brand, delivery_countries in delivery_info.items():
    delivery_countries_set = set(delivery_countries)

    if delivery_countries_set.intersection(countries):
        if delivery_countries_set.issubset(countries):
            some_delivered_cars.add(car_brand)
        else:
            all_delivered_cars.add(car_brand)
    else:
        not_delivered_cars.add(car_brand)


print("Машины, доставленные во все страны из списка:")
for car_brand in all_delivered_cars:
    print(f"- {car_brand}")

print("Машины, доставленные в некоторые страны из списка:")
for car_brand in some_delivered_cars:
    print(f"- {car_brand}")

print("Машины, не доставленные ни в одну страну из списка:")
for car_brand in not_delivered_cars:
    print(f"- {car_brand}")
    print(type(not_delivered_cars))
