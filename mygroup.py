groupmates = [
    {
        "name": "Павел",
        "surname": "Охримчук",
        "exams": ["АИГ", "ВВИТ", "Философия"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Магомед",
        "surname": "Керимов",
        "exams": ["АИГ", "ВВИТ", "Философия"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Александр",
        "surname": "Плешаков",
        "exams": ["АИГ", "ВВИТ", "Философия"],
        "marks": [5, 5, 5]
    },

    {
        "name": "Артем",
        "surname": "Сарафанников",
        "exams": ["АИГ", "ВВИТ", "Философия"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Михаил",
        "surname": "Ющенко",
        "exams": ["АИГ", "ВВИТ", "Философия"],
        "marks": [3, 3, 3]
    }

]


def filtr_for_students(students, middle):
    print(u'Имя'.ljust(15), u'Фамилия'.ljust(10), u'Экзамены'.ljust(35), u'Оценки'.ljust(20), u'Средний балл'.ljust(15))
    for student in students:
        summa = 0
        for bal in student["marks"]:
            summa +=bal
        medium = summa/len(student["marks"])
        if (round(medium,2)>middle):
            print(student["name"].ljust(15),student["surname"].ljust(10),str(student["exams"]).ljust(35),str(student["marks"]).ljust(15),str((medium)).ljust(10))
sredbl = float(input("Введите средний балл учащегося:  "))
filtr_for_students(groupmates,sredbl)
