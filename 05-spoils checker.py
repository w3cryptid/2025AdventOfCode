#day_05_input = open("2025 AoC Advent Calander/05-test-input.txt","r")
day_05_input = open("2025 AoC Advent Calander/05-input.txt","r")

spoil_range : list = []
foods_list : list = []

def clean_input() -> None: 
    for line in day_05_input.readlines(): 
        if line.find("-") > -1: 
            hold = line.replace("\n","")
            spoil_range.append(hold)
        elif len(line)>1: 
            hold = line.replace("\n","")
            foods_list.append(hold)

def do_thing_01() -> None: 
    clean_input()
    print("\n")
    total : int = 0
    for food_str in foods_list:
        food = int(food_str)
        food_recorded : bool = False
        for good_range in spoil_range: 
            if food_recorded: continue
            good = good_range.split("-")
            if int(good[0]) <= food and food <= int(good[1]): 
                total +=1
                food_recorded = True
                continue
    print(total)

def do_thing_02() -> None: 
    clean_input()
    print("\n")
    total : int = 0
    true_range : list = spoil_range.copy()
    before_list : list = []
    while before_list != true_range: 
        before_list = true_range
        true_range = search_for_overlap(true_range)
    for true_r in true_range: 
        hold = true_r.split("-")
        hold[0] = int(hold[0])
        hold[1] = int(hold[1])
        total += hold[1] - hold[0] + 1
    print(true_range)
    print(total)

def search_for_overlap(input_range:list) -> list: 
    re_list : list = []
    for base_range in input_range: 
        base = base_range.split("-")
        base[0] = int(base[0])
        base[1] = int(base[1])
        for compare_range in input_range: 
            compare = compare_range.split("-")
            compare[0] = int(compare[0])
            compare[1] = int(compare[1])
            if compare[0] <= base[0] and base[0] <= compare[1]: 
                base[0] = compare[0]
            if compare[0] <= base[1] and base[1] <= compare[1]: 
                base[1] = compare[1]
        if re_list.count(f"{base[0]}-{base[1]}") > 0: continue
        re_list.append(f"{base[0]}-{base[1]}")
    #print(re_list)
    return re_list


do_thing_02()
