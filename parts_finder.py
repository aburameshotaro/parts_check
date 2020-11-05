# Load code of parts that we are looking for or we have found already
with open('PartsToSearch.txt', 'r') as file:
    czesci = file.readlines()
czesci = [x.strip() for x in czesci]

with open('Found.txt', 'r') as file:
    znalezione = file.readlines()
znalezione = [x.strip() for x in znalezione]

    
#%% User scan number and program prints message if this part is ok or not ok
a=1
while True:
    a = input("Podaj numer części (0 aby zakończyć): ")
    if a=='0':
        break
    if a in czesci:
        print(chr(7))
        print(f"Część {a} jest do odrzucenia.")
        print("@    @    @    @  @")
        print("@@   @  @   @  @ @")
        print("@ @  @  @   @  @@")
        print("@  @ @  @   @  @ @")
        print("@   @@    @    @  @")
        if a not in znalezione:
            znalezione.append(a)
            with open('Found.txt', 'a') as file:
                print(a, file=file)
    else:
        print(f"Część {a} jest dobra.")
        print("  @       @   @")
        print("@   @     @ @")
        print("@   @     @@")
        print("@   @     @ @")
        print("  @       @   @")
        
