import array as arr

size = 5
array = arr.array("i",[])

def push(value):
    # Checks whether value is valid 
    try:
        value = int(value)
    except Exception:
        print("Insert a valid value!")

    top = len(array)

    if top == size:
        print("Overflow")
        return array
    else:
        array.append(value)

push(5)
push(1)
push(6)
push(3)
push(0)
push(9)
print(array)