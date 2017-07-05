#CyberNexusBruno
#Number Pattern Finder - Ex: 42 126 378 = Multiplication: 6
#Computer Version 3.0
key = int(input("How many pairs (3-10):"))
if 3 > key:
    print("You need to use a valid number of pairs.")
elif key > 10:
    print("You need to use a valid number of pairs.")
else:
    if key >= 1:
        a = int(input("Pair 1:"))
    if key >= 2:
        b = int(input("Pair 2:"))
    if key >= 3:
        c = int(input("Pair 3:"))
    if key >= 4:
        d = int(input("Pair 4:"))
    if key >= 5:
        e = int(input("Pair 5:"))
    if key >= 6:
        f = int(input("Pair 6:"))
    if key >= 7:
        g = int(input("Pair 7:"))
    if key >= 8:
        h = int(input("Pair 8:"))
    if key >= 9:
        i = int(input("Pair 9:"))
    if key >= 10:
        j = int(input("Pair 10:"))

if 3 <= key and key <= 10:      
    start = str(input("Start Cracking (y/n):"))

#Detect highest and lowest values to stop keymore and keyless.
if 3 <= key and key <= 10:
    if key >= 1:
        numbers = [a]
    if key >= 2:
        numbers = [a, b]
    if key >= 3:
        numbers = [a, b, c]
    if key >= 4:
        numbers = [a, b, c, d]
    if key >= 5:
        numbers = [a, b, c, d, e]
    if key >= 6:
        numbers = [a, b, c, d, e, f]
    if key >= 7:
        numbers = [a, b, c, d, e, f, g]
    if key >= 8:
        numbers = [a, b, c, d, e, f, g, h]
    if key >= 9:
        numbers = [a, b, c, d, e, f, g, h, i]
    if key >= 10:
        numbers = [a, b, c, d, e, f, g, h, i, j]
    max_value = max(numbers)
    min_value = min(numbers)

#Functions
def main():
    def_main(keymore, keyless, keydivision, keymulti, keymore_ml, keyless_ml)

#Execution
keymore = 1
keyless = 0
keydivision = 1
keymulti = 1
keymore_ml = 1
keyless_ml = 0
def def_main(keymore, keyless, keydivision, keymulti, keymore_ml, keyless_ml):
    more = "y"
    while more == "y":
        if keymore == max_value:
            more = "f"
            print("Addition: Not Found")
        elif key == 3:
            if a + keymore == b and b + keymore == c:
                print("Addition:", keymore)
                more = "f"
            else:
                keymore += 1
        elif key == 4:
            if a + keymore == b and b + keymore == c and c + keymore == d:
                print("Addition:", keymore)
                more = "f"
            else:
                keymore += 1
        elif key == 5:
            if a + keymore == b and b + keymore == c and c + keymore == d and d + keymore == e:
                print("Addition:", keymore)
                more = "f"
            else:
                keymore += 1
        elif key == 6:
            if a + keymore == b and b + keymore == c and c + keymore == d and d + keymore == e and e + keymore == f:
                print("Addition:", keymore)
                more = "f"
            else:
                keymore += 1
        elif key == 7:
            if a + keymore == b and b + keymore == c and c + keymore == d and d + keymore == e and e + keymore == f and f + keymore == g:
                print("Addition:", keymore)
                more = "f"
            else:
                keymore += 1
        elif key == 8:
            if a + keymore == b and b + keymore == c and c + keymore == d and d + keymore == e and e + keymore == f and f + keymore == g and g + keymore == h:
                print("Addition:", keymore)
                more = "f"
            else:
                keymore += 1
        elif key == 9:
            if a + keymore == b and b + keymore == c and c + keymore == d and d + keymore == e and e + keymore == f and f + keymore == g and g + keymore == h and h + keymore == i:
                print("Addition:", keymore)
                more = "f"
            else:
                keymore += 1
        elif key == 10:
            if a + keymore == b and b + keymore == c and c + keymore == d and d + keymore == e and e + keymore == f and f + keymore == g and g + keymore == h and h + keymore == i and i + keymore == j:
                print("Addition:", keymore)
                more = "f"
            else:
                keymore += 1
            
    less = "y"
    while less == "y":
        if keyless == -max_value:
            less = "f"
            print("Subtraction: Not Found")
        elif key == 3:
            if a + keyless == b and b + keyless == c:
                print("Subtraction:", keyless)
                less = "f"
            else:
                keyless -= 1
        elif key == 4:
            if a + keyless == b and b + keyless == c and c + keyless == d:
                print("Subtraction:", keyless)
                less = "f"
            else:
                keyless -= 1
        elif key == 5:
            if a + keyless == b and b + keyless == c and c + keyless == d and d + keyless == e:
                print("Subtraction:", keyless)
                less = "f"
            else:
                keyless -= 1
        elif key == 6:
            if a + keyless == b and b + keyless == c and c + keyless == d and d + keyless == e and e + keyless == f:
                print("Subtraction:", keyless)
                less = "f"
            else:
                keyless -= 1
        elif key == 7:
            if a + keyless == b and b + keyless == c and c + keyless == d and d + keyless == e and e + keyless == f and f + keyless == g:
                print("Subtraction:", keyless)
                less = "f"
            else:
                keyless -= 1
        elif key == 8:
            if a + keyless == b and b + keyless == c and c + keyless == d and d + keyless == e and e + keyless == f and f + keyless == g and g + keyless == h:
                print("Subtraction:", keyless)
                less = "f"
            else:
                keyless -= 1
        elif key == 9:
            if a + keyless == b and b + keyless == c and c + keyless == d and d + keyless == e and e + keyless == f and f + keyless == g and g + keyless == h and h + keyless == i:
                print("Subtraction:", keyless)
                less = "f"
            else:
                keyless -= 1
        elif key == 10:
            if a + keyless == b and b + keyless == c and c + keyless == d and d + keyless == e and e + keyless == f and f + keyless == g and g + keyless == h and h + keyless == i and i + keyless == j:
                print("Subtraction:", keyless)
                less = "f"
            else:
                keyless -= 1

    division = "y"
    while division == "y":
        if keydivision == max_value:
            division = "f"
            print("Division: Not Found")
        elif key == 3:
            if a // keydivision == b and b // keydivision == c:
                print("Division:", keydivision)
                division = "f"
            else:
                keydivision += 1
        elif key == 4:
            if a // keydivision == b and b // keydivision == c and c // keydivision == d:
                print("Division:", keydivision)
                division = "f"
            else:
                keydivision += 1
        elif key == 5:
            if a // keydivision == b and b // keydivision == c and c // keydivision == d and d // keydivision == e:
                print("Division:", keydivision)
                division = "f"
            else:
                keydivision += 1
        elif key == 6:
            if a // keydivision == b and b // keydivision == c and c // keydivision == d and d // keydivision == e and e // keydivision == f:
                print("Division:", keydivision)
                division = "f"
            else:
                keydivision += 1
        elif key == 7:
            if a // keydivision == b and b // keydivision == c and c // keydivision == d and d // keydivision == e and e // keydivision == f and f // keydivision == g:
                print("Division:", keydivision)
                division = "f"
            else:
                keydivision += 1
        elif key == 8:
            if a // keydivision == b and b // keydivision == c and c // keydivision == d and d // keydivision == e and e // keydivision == f and f // keydivision == g and g // keydivision == h:
                print("Division:", keydivision)
                division = "f"
            else:
                keydivision += 1
        elif key == 9:
            if a // keydivision == b and b // keydivision == c and c // keydivision == d and d // keydivision == e and e // keydivision == f and f // keydivision == g and g // keydivision == h and h // keydivision == i:
                print("Division:", keydivision)
                division = "f"
            else:
                keydivision += 1
        elif key == 10:
            if a // keydivision == b and b // keydivision == c and c // keydivision == d and d // keydivision == e and e // keydivision == f and f // keydivision == g and g // keydivision == h and h // keydivision == i and i // keydivision == j:
                print("Division:", keydivision)
                division = "f"
            else:
                keydivision += 1

    multi = "y"
    while multi == "y":
        if keymulti == max_value:
            multi = "f"
            print("Multiplication: Not Found")
        elif key == 3:
            if a * keymulti == b and b * keymulti == c:
                print("Multiplication:", keymulti)
                multi = "f"
            else:
                keymulti += 1
        elif key == 4:
            if a * keymulti == b and b * keymulti == c and c * keymulti == d:
                print("Multiplication:", keymulti)
                multi = "f"
            else:
                keymulti += 1
        elif key == 5:
            if a * keymulti == b and b * keymulti == c and c * keymulti == d and d * keymulti == e:
                print("Multiplication:", keymulti)
                multi = "f"
            else:
                keymulti += 1
        elif key == 6:
            if a * keymulti == b and b * keymulti == c and c * keymulti == d and d * keymulti == e and e * keymulti == f:
                print("Multiplication:", keymulti)
                multi = "f"
            else:
                keymulti += 1
        elif key == 7:
            if a * keymulti == b and b * keymulti == c and c * keymulti == d and d * keymulti == e and e * keymulti == f and f * keymulti == g:
                print("Multiplication:", keymulti)
                multi = "f"
            else:
                keymulti += 1
        elif key == 8:
            if a * keymulti == b and b * keymulti == c and c * keymulti == d and d * keymulti == e and e * keymulti == f and f * keymulti == g and g * keymulti == h:
                print("Multiplication:", keymulti)
                multi = "f"
            else:
                keymulti += 1
        elif key == 9:
            if a * keymulti == b and b * keymulti == c and c * keymulti == d and d * keymulti == e and e * keymulti == f and f * keymulti == g and g * keymulti == h and h * keymulti == i:
                print("Multiplication:", keymulti)
                multi = "f"
            else:
                keymulti += 1
        elif key == 10:
            if a * keymulti == b and b * keymulti == c and c * keymulti == d and d * keymulti == e and e * keymulti == f and f * keymulti == g and g * keymulti == h and h * keymulti == i and i * keymulti == j:
                print("Multiplication:", keymulti)
                multi = "f"
            else:
                keymulti += 1
                
#Start
if 3 <= key and key <= 10:
    if start == "y":
        main()
    else:
        exit()
