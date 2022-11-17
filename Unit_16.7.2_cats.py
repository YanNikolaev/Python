from cat import Cat

cats = [
    {
     "name": "Сэм",
     "gender": "мальчик",
     "age": 2,
    },
    {
     "name": "Мурка",
     "gender": "девочка",
     "age": 1,
    },
{
     "name": "Пушок",
     "gender": "мальчик",
     "age": 3,
    },
]

for cat in cats:
    cat_obj = Cat()
    cat_obj._Cat__init__from_dict(cat)
    print(cat_obj.name)
    print(cat_obj.gender)
    print(cat_obj.age)