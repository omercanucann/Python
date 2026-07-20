import sys

print("=== Cyber Archives Recovery & Preservation ===")

if len(sys.argv) != 2:
    sys.stderr.write("[STDERR] Usage: python3 ft_stream_management.py <file>\n")
    sys.exit()

filename = sys.argv[1]

print(f"Accessing file '{filename}'")

try:
    file = open(filename, "r")
    content = file.read()
    file.close()
except Exception as e:
    sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
    sys.exit()

print("---")
print(content, end="")
print("---")
print(f"File '{filename}' closed.")

lines = content.split("\n")
new_content = ""

for i in range(len(lines)):
    if lines[i] != "":
        new_content += lines[i] + "#"

    if i != len(lines) - 1:
        new_content += "\n"

print("Transform data:")
print("---")
print(new_content)
print("---")

sys.stdout.write("Enter new file name (or empty): ")
sys.stdout.flush() # ekrana yazılmayı bekleyen (tamponda tutulan) çıktıları hemen gösterir, beklemeden kullanıcıya ulaştırır.

new_filename = sys.stdin.readline().rstrip("\n") # readline() girişten veya bir dosyadan tek satır okuyan metottur.
# rstrip() bir metnin sonundaki belirtilen karakterleri (veya varsayılan olarak boşlukları) silen metottur.

if new_filename == "":
    sys.exit()

print(f"Saving data to '{new_filename}'")

try:
    new_file = open(new_filename, "w")
    new_file.write(new_content)
    new_file.close()
    print("Data saved.")
except Exception as e:
    sys.stderr.write(f"[STDERR] Error opening file '{new_filename}': {e}\n")
    print("Data not saved.")