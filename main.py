import json


# task 1
with open("t1input", "r", encoding="UTF-8") as f:
    data = f.read().split("\n\n")
    data = [x.split("\n") for x in data]

cook_book = {}

for i in data:
    cook_book[i[0]] = []
    for ii in range(2, len(i)):
        temp = i[ii].split(" | ")
        cook_book[i[0]].append({'ingredient_name': temp[0], 'quantity': int(temp[1]), 'measure': temp[2]})

print(cook_book)

with open("t1output", "w", encoding="UTF-8") as f:
    json.dump(cook_book, f, indent=4, )


# task 2
def get_shop_list_by_dishes(dishes, person_count):
    output_cook_list = {}
    for cb in dishes:
        for cb in cook_book[cb]:
            if output_cook_list.get(cb["ingredient_name"]):
                print("Есть в списке -", cb["ingredient_name"])
                temp = output_cook_list[cb["ingredient_name"]]["quantity"] + cb["quantity"] * person_count
                output_cook_list[cb["ingredient_name"]]["quantity"] = temp
            else:
                output_cook_list[cb["ingredient_name"]] = \
                    {'measure': cb["measure"], 'quantity': cb["quantity"] * person_count}

    print(output_cook_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)
