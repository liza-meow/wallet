
class Transaction:
   def __init__(self, id, date, category, amount, description):
        self.id = id
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description



def get_balance(filename):
    spend = 0
    income = 0
    with open(filename, "r") as file1:
        for line in file1:
            trans = line.strip().split(",")
            if trans[2] == "Расход":
                spend += float(trans[3])
            if trans[2] == "Доход":
                income += float(trans[3])
        print("Расходы:", spend)
        print("Доходы:", income)
        print("Баланс:", income-spend)
    file1.close()


def insert_transaction(filename, id):
    correct_date = False

    while not correct_date:
        date = input("введите дату: ")
        if len(date) == 8 and date[2] == "-" and date[5] == "-":
            dd, mm, yy = date.split("-")
            if dd.isdigit() and mm.isdigit() and yy.isdigit():
                if 1 <= int(dd) <= 31 and 1 <= int(mm) <= 12 and 0 <= int(yy) <= 99:
                    correct_date = True
                else:
                    print("Неверный формат даты. Пожалуйста, введите дату в формате дд-мм-гг.")
            else:
                print("Неверный формат даты. Пожалуйста, введите дату в формате дд-мм-гг.")
        else:
            print("Неверный формат даты. Пожалуйста, введите дату в формате дд-мм-гг.")

    description = input("введите расход/доход: ")
    amount = input("введите сумму: ")
    category = input("введите категорию: ")
    meaning = [str(id), date, description, amount, category]

    with open(filename, "a") as file1:
        file1.write(",".join(meaning) + "\n")
        print("Запись номер: {}, дата: {}, описание: {}, сумма: {}, категория: {} успешно добавлена".format(*meaning))

def edit_transaction(filename):
    id_to_edit = input("Введите ID для редактирования: ")
    field_to_edit = input("Введите номер поля, которое нужно отредактировать (1, 2, 3, 4, 5): ")
    new_value = input("Введите новое значение: ")

    fields = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4}
    temp_file = filename + ".tmp"

    with open(filename, "r") as file1, open(temp_file, "w") as file2:
        for line in file1:
            trans = line.strip().split(",")
            if trans[0] == id_to_edit:
                trans[fields[field_to_edit]] = new_value
                edited_line = ",".join(trans)
                file2.write(edited_line + '\n')
            else:
                file2.write(line)

    import os
    os.replace(temp_file, filename)


def search_transaction(filename):
    fields = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4}
    choice = input("По какому полю поиск: id, Дата, Категория, Сумма, Описание? Введите 1, 2, 3, 4, 5: ")
    value = input("Введите значение: ")

    if choice in fields:
        with open(filename, "r") as file1:
            for line in file1:
                trans = line.strip().split(",")
                if trans[fields[choice]] == value:
                    print(line)
    else:
        print("Введите правильное значение")

def main():
    count = 0
    while True:

        choice = input("Введите цифру (1, 2, 3 или 4): ")
        if choice == "1":
            get_balance("filed.txt")
        elif choice == "2":
            insert_transaction("filed.txt", count)
            count += 1
        elif choice == "3":
            edit_transaction("filed.txt")
        elif choice == "4":
            search_transaction("filed.txt")
        else:
            print("Неверный ввод. Пожалуйста, введите цифру от 1 до 4.")

if __name__ == "__main__":
    main()