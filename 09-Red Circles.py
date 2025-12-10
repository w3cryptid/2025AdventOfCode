import math
#day_09_input = open("2025 AoC Advent Calander/09-test-input.txt","r")
day_09_input = open("2025 AoC Advent Calander/09-input.txt","r")

vec2_list : list = []

def clean_input() -> None: 
    global vec2_list
    for line in day_09_input.readlines(): 
        hold : str = line.strip()
        hold = hold.replace("\n","")
        new_hold = hold.split(",")
        vec2_list.append([int(new_hold[0]), int(new_hold[1])])

def do_thing_01() -> None: 
    clean_input()
    print("\n")
    global vec2_list
    largest : int = 0
    for start in vec2_list: 
        for end in vec2_list:
            length = abs(start[0]-end[0])+1
            height = abs(start[1]-end[1])+1
            area = length * height
            if area > largest: largest = area
    print(largest)

def populate_map()->list: 
    map_list : list = []
    sort_vec2 = vec2_list.copy()
    sort_vec2.sort(reverse=True)
    default_line : str = ""
    for x in range(sort_vec2[0][0]+3): 
        default_line += "."
    sort_vec2.sort(reverse=True, key=lambda k:k[1])
    for y in range(sort_vec2[0][1]+2): 
        map_list.append(default_line)
    for coord in range(len(vec2_list)): 
        start_coord : list = vec2_list[coord]
        if start_coord == vec2_list[-1]: end_coord = vec2_list[0]
        else: end_coord = vec2_list[coord+1]
        for line in range(abs(start_coord[1]-end_coord[1])+1): 
            line_idx = start_coord[1]+int(math.copysign(line,(end_coord[1]-start_coord[1])))
            #replace_line = map_list[line_idx][start_coord[0]:end_coord[0]+1].replace(".","#")
            if start_coord[0] <= end_coord[0]:
                replace_line = map_list[line_idx][start_coord[0]:end_coord[0]+1].replace(".","#")
                replace_line = map_list[line_idx][0:start_coord[0]] + replace_line
                replace_line = replace_line + map_list[line_idx][end_coord[0]+1:]
            else: 
                replace_line = map_list[line_idx][end_coord[0]:start_coord[0]+1].replace(".","#")
                replace_line = map_list[line_idx][0:end_coord[0]] + replace_line
                replace_line = replace_line + map_list[line_idx][start_coord[0]+1:]
            map_list[line_idx] = replace_line
    for line in range(len(map_list)): 
        l =  map_list[line]
        start = l.find("#")
        end = l.rfind("#")
        map_list[line] = l[:start] + l[start:end].replace(".","#") + l[end+1:]
        #print( map_list[line])
    return map_list

        ### here, draw lines along perimeter

def do_thing_02() -> None: 
    clean_input()
    print("\n")
    global vec2_list
    map_list : list = []
    map_list = populate_map()
    largest_list : list = []
    largest : int = 0
    for start_idx in range(len(vec2_list)): 
        start = vec2_list[start_idx]
        for end_idx in range(len(vec2_list)-start_idx):
            end = vec2_list[end_idx+start_idx]
            if start == end: continue
            length = abs(start[0]-end[0])+1
            height = abs(start[1]-end[1])+1
            area = length * height
            largest_list.append({"start":start,"end":end,"area":area})
        
    largest_list.sort(reverse=True,key=lambda k:k["area"])
    for large in largest_list: 
        print(f"Start {large}")
        height = abs(large["start"][1]-large["end"][1])+1
        start_y = min(large["start"][1],large["end"][1])
        start_x = min(large["start"][0],large["end"][0])
        end_x = max(large["start"][0],large["end"][0])
        invalid : bool = False
        for r in range(height): 
            if map_list[start_y+r][start_x:end_x].count(".") > 0: 
                invalid = True
                break
        if invalid: continue
        largest = large["area"]
        break
    print(largest)
    
    
# string_a = "01234500000000000"
# string_b = string_a[0:5].replace("0","X")
# print(string_b)
do_thing_02()
