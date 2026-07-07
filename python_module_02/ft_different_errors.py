def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        x = 10 / 0
    elif operation_number == 2:
        open("this_file_does_not_exist.txt")
    elif operation_number == 3:
        x = "flowers" + 5
    else:
        return

def test_error_types():
    print("=== Testing Individual Errors ===")

    try:
        garden_operations(0)
    except ValueError: # bir fonksiyona doğru türde ancak geçersiz bir değer verildiğinde oluşan hata türüdür.
        print("ValueError: Invalid data was given to int()")
    print("program continues... \n")

    try:
        garden_operations(1)
    except ZeroDivisionError: # bir sayıyı sıfıra bölmeye çalıştığınızda oluşan hata türüdür.
        print("ZeroDivisionError: Cannot divide by zero")
    
    print("Program Continues... \n")

    try:
        garden_operations(2)
    except FileNotFoundError: # var olmayan veya bulunamayan bir dosya açılmaya çalışıldığında oluşan hata türüdür.
        print("FileNotFoundError: The file dos not exist")

    print("Program Continues...\n")
    print("=== Catching Multiple Errors Together ===")

    for i in range(4):
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
            print("An Error occurrred during operation", i)
    print("Program finished successfully!")

test_error_types() 