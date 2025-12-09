day_08_input = open("2025 AoC Advent Calander/08-test-input.txt", "r")
#day_08_input = open("2025 AoC Advent Calander/08-input.txt", "r")
box_dict : list = []


def clean_input()-> None: 
    hold_list : list = []
    global box_dict
    for line in day_08_input.readlines(): 
        hold = line.replace("\n","")
        hold_list.append(hold)
    default_dict_val : dict = {"source":"","nearest":"","vec_sqr":-1,"circut":-1}
    for key in range(len(hold_list)): 
        box_dict.append(default_dict_val.copy()) 
        box_dict[key]["source"] = hold_list[key]
    

def doesnt_do_thing_01()->None:
    print("\n") 
    clean_input()
    populate_box_dict()
    circut_list : list = []
    for key in box_dict: 
        near : str = box_dict[key]["nearest"]
        if box_dict[near]["circut"] == -1: 
            circut_list.append([key,near])
            box_dict[key]["circut"] = len(circut_list)-1
            box_dict[near]["circut"] = len(circut_list)-1
        else: 
            circut_list[box_dict[near]["circut"]].append(key)
        print(f"{key} => {box_dict[key]}")
    #print(circut_list)

def populate_box_dict()-> None: 
    global box_dict
    for source in box_dict: 
        for compare in box_dict: 
            if source["source"] == compare["source"]: 
                continue
            s_vec3 : list = source["source"].split(",")
            comp_vec3 : list = compare["source"].split(",")
            for x in range(len(s_vec3)): 
                s_vec3[x] = int(s_vec3[x])
                comp_vec3[x] = int(comp_vec3[x])
            vec_sqr = ((comp_vec3[0]-s_vec3[0])**2)+((comp_vec3[1]-s_vec3[1])**2)+((comp_vec3[2]-s_vec3[2])**2)
            #vec_sqr = abs(vec_sqr)
            if vec_sqr < source["vec_sqr"] or source["vec_sqr"] == -1:
                source["vec_sqr"] = vec_sqr
                source["nearest"] = compare["source"]

def sort_box_dict(dic) -> int: 
    return dic["vec_sqr"]
    
def do_thing_01() -> None: 
    clean_input()
    print("\n")
    populate_box_dict()
    box_dict.sort(key=sort_box_dict)
    for i in range(len(box_dict)): 
        pass

    


do_thing_01()