day_08_input = open("2025 AoC Advent Calander/08-test-input.txt", "r")
#day_08_input = open("2025 AoC Advent Calander/08-input.txt", "r")
box_dict : list = []
relative_dict : list = []
num_of_shortest : int = 1000
unconnected_list : list = []

def clean_input()-> None: 
    hold_list : list = []
    global box_dict
    for line in day_08_input.readlines(): 
        hold = line.replace("\n","")
        hold_list.append(hold)
    default_box_dict : dict = {"source":"","nearest":"","vec_sqr":-1,"circut":-1}
    default_relative_dict : dict = {"compare":"","vec_sqr":-1}
    for key in range(len(hold_list)): 
        box_dict.append(default_box_dict.copy()) 
        box_dict[key]["source"] = hold_list[key]
        relative_dict.append(default_relative_dict.copy())
        relative_dict[key]["compare"] = hold_list[key]
        unconnected_list.append(hold_list[key])
    
# def doesnt_do_thing_01()->None:
#     print("\n") 
#     clean_input()
#     populate_box_dict()
#     circut_list : list = []
#     for key in box_dict: 
#         near : str = box_dict[key]["nearest"]
#         if box_dict[near]["circut"] == -1: 
#             circut_list.append([key,near])
#             box_dict[key]["circut"] = len(circut_list)-1
#             box_dict[near]["circut"] = len(circut_list)-1
#         else: 
#             circut_list[box_dict[near]["circut"]].append(key)
#         print(f"{key} => {box_dict[key]}")
    #print(circut_list)

def populate_box_dict()-> None: 
    global box_dict
    for source in box_dict: 
        for compare in box_dict: 
            if source["source"] == compare["source"]: 
                continue
            vec_sqr : int = return_veq_sqr(source["source"], compare["source"])
            if vec_sqr < source["vec_sqr"] or source["vec_sqr"] == -1:
                source["vec_sqr"] = vec_sqr
                source["nearest"] = compare["source"]

def populate_relative_list(source_box: str)->None:
    global relative_dict 
    for key in range(len(relative_dict)): 
        if source_box == relative_dict[key]["compare"]: 
            relative_dict[key]["vec_sqr"] = -1
            continue
        veq_sqr = return_veq_sqr(source_box,relative_dict[key]["compare"])
        relative_dict[key]["vec_sqr"] = veq_sqr
    relative_dict.sort(key=sort_box_dict)

def return_veq_sqr(source:str, compare:str) -> int: 
    s_vec3 : list = source.split(",")
    comp_vec3 : list = compare.split(",")
    for x in range(len(s_vec3)): 
        s_vec3[x] = int(s_vec3[x])
        comp_vec3[x] = int(comp_vec3[x])
    vec_sqr : int = ((comp_vec3[0]-s_vec3[0])**2)+((comp_vec3[1]-s_vec3[1])**2)+((comp_vec3[2]-s_vec3[2])**2)
    return vec_sqr

def sort_box_dict(dic) -> int: 
    return dic["vec_sqr"]

def find_idx(lis: list, key:str, desire:str) -> int: 
    for idx in range(len(lis)): 
        if lis[idx][key] == desire: return idx
    return -1

def update_circut(idx:int) -> None: 
    if box_dict[idx]["circut"] == -1: 
        box_dict[idx]["circut"] = {box_dict[idx]["source"]}
        unconnected_list.remove(box_dict[idx]["source"])
    comp_idx = find_idx(box_dict,"source",box_dict[idx]["nearest"])
    if box_dict[comp_idx]["circut"] == -1: 
        box_dict[idx]["circut"].add(box_dict[comp_idx]["source"])
        box_dict[comp_idx]["circut"] = box_dict[idx]["circut"]
        unconnected_list.remove(box_dict[comp_idx]["source"])
        return
    box_dict[comp_idx]["circut"].update(box_dict[idx]["circut"])
    old_set = box_dict[idx]["circut"]
    for s in old_set: 
        set_idx = find_idx(box_dict, "source", s)
        box_dict[set_idx]["circut"] = box_dict[comp_idx]["circut"]
    #old_set.clear()

def update_next_nearest(idx:int)->None: 
    populate_relative_list(box_dict[idx]["source"])
    for search in range(len(relative_dict)): 
        if relative_dict[search]["vec_sqr"] == -1: continue
        if box_dict[idx]["vec_sqr"] < relative_dict[search]["vec_sqr"]: 
            box_dict[idx]["nearest"] = relative_dict[search]["compare"]
            box_dict[idx]["vec_sqr"] = relative_dict[search]["vec_sqr"]
            box_dict.sort(key=sort_box_dict)
            return

def do_thing_01() -> None: 
    clean_input()
    print("\n")
    circut_list : list = []
    circut_len : list = []
    populate_box_dict()
    box_dict.sort(key=sort_box_dict)
    connection_list : list = []
    i : int = 0
    while len(connection_list) < num_of_shortest: 
        s_box_str = box_dict[i]["source"]
        comp_box_str = box_dict[i]["nearest"]
        unconnected : bool = True
        while unconnected: 
            if connection_list.count(f"{s_box_str}-{comp_box_str}") <= 0 and connection_list.count(f"{comp_box_str}-{s_box_str}") <= 0:
                connection_list.append(f"{s_box_str}-{comp_box_str}")
                update_circut(i)
                unconnected = False
                update_next_nearest(i)
                #i += 1
                continue
            update_next_nearest(i)
            s_box_str = box_dict[i]["source"]
            comp_box_str = box_dict[i]["nearest"]
            continue
    for k in box_dict: 
        if circut_list.count(k["circut"]) > 0 or k["circut"] == -1: continue
        circut_list.append(k["circut"])
        # print(k["circut"])
        # print(len(k["circut"]))
        circut_len.append(len(k["circut"]))
        circut_len.sort()
    print(circut_len)
    #print(box_dict)      



def do_thing_02() -> None: 
    clean_input()
    print("\n")
    circut_list : list = []
    circut_len : list = []
    populate_box_dict()
    box_dict.sort(key=sort_box_dict)
    connection_list : list = []
    i : int = 0
    global unconnected_list
    while len(unconnected_list) > 0: 
        s_box_str = box_dict[i]["source"]
        comp_box_str = box_dict[i]["nearest"]
        unconnected : bool = True
        while unconnected: 
            if connection_list.count(f"{s_box_str}-{comp_box_str}") <= 0 and connection_list.count(f"{comp_box_str}-{s_box_str}") <= 0:
                connection_list.append(f"{s_box_str}-{comp_box_str}")
                update_circut(i)
                unconnected = False
                update_next_nearest(i)
                print(connection_list[-1])
                continue
            update_next_nearest(i)
            s_box_str = box_dict[i]["source"]
            comp_box_str = box_dict[i]["nearest"]
            continue
    for k in box_dict: 
        if circut_list.count(k["circut"]) > 0 or k["circut"] == -1: continue
        circut_list.append(k["circut"])
        circut_len.append(len(k["circut"]))
        circut_len.sort()
    print(circut_len)

do_thing_02()
#do_thing_01()