def secure_archive(filename, action="read", content=""):
    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
            return (True, data)
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action")
    except Exception as error:
        return (False, str(error))
    
def main():
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("archive.txt")
    print(result)

    if result[0]: # Bu kısım, okuma işlemi başarılı olduysa okunan veriyi başka bir dosyaya yazdırıyor.
        print("\nUsing 'secure_archive' to write previous content to a new file:")
        print(secure_archive("backup.txt", "write", result[1]))

if __name__ == "__main__":
    main()