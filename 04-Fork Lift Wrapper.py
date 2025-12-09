day_04_input = open("2025 AoC Advent Calander/04-input.txt","r")
#day_04_input = open("2025 AoC Advent Calander/04-test-input.txt","r")
warehouse : list = []
copy_house : list = []
total : int = 0

def clean_input()-> None: 
    global warehouse
    for row in day_04_input.readlines(): 
        hold = row.replace("\n","")
        warehouse.append(hold)

def do_thing_01() -> None: 
    print("\n\n")
    clean_input()
    global warehouse
    global copy_house
    global total
    copy_house = warehouse.copy()
    for x in range(len(warehouse)): 
        for y in range(len(warehouse[x])): 
            if warehouse[x][y] == ".": continue
            if check_vicinity(x,y): 
                copy_house[x] = replace_index(copy_house[x],y,".")
                total += 1
    #pretty_print_warehouse()
    warehouse = copy_house.copy()
    print(total)

def do_thing_02() -> None: 
    old_total = -1
    while old_total != total: 
        old_total = total
        do_thing_01()

def check_vicinity(x:int, y:int) -> bool: 
    wrappers : int = 0
    for width in range(3): 
        for height in range(3): 
            if x+width-1 < 0 or len(warehouse) <= x+width-1: 
                continue
            if y+height-1 < 0 or len(warehouse[x]) <= y+height-1: 
                continue
            if height == 1 and width == 1 : continue
            if warehouse[x+(width-1)][y+(height-1)] == "@": wrappers += 1
            if wrappers > 3: return False
    return True

def replace_index(start:str, idx:int, new:str) -> str: 
    if idx == 0: 
        return new+start[1:]
    return start[:idx] + new +start[idx+1:]

def pretty_print_warehouse()-> None: 
    for row in copy_house: 
        print(row)

do_thing_02()