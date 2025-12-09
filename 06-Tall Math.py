#day_06_input = open("2025 AoC Advent Calander/06-test-input.txt","r")
day_06_input = open("2025 AoC Advent Calander/06-input.txt","r")
number_list : list = []


def clean_input()-> None: 
    for line in day_06_input.readlines(): 
        hold = line.replace("\n","")
        number_list.append(hold)

def do_thing_01() -> None: 
    print("\n")
    clean_input()
    global number_list
    strawman = number_list[0]
    strawman = strawman.split()
    totals : list = []
    methods : list = number_list[-1].split()
    for i in range(len(strawman)): 
        for line in range(len(number_list)-1): 
            hold_line = number_list[line].split()
            if line == 0: 
                totals.append(int(hold_line[i])) 
                continue
            if methods[i] == "*": 
                totals[i] *= int(hold_line[i])
                continue
            if methods[i] == "+": 
                totals[i] += int(hold_line[i])
                continue
    print(sum(totals))

#Fuck u part 2!! 
#cant use split... spaces matter!!

def do_thing_02()-> None: 
    print("\n")
    clean_input()
    global number_list
    totals : list = []
    methods : str = number_list[-1]
    fixed_line : list = []
    for i in range(len(number_list[0])): 
        for line in range(len(number_list)-1):
            if line == 0: 
                fixed_line.append(number_list[line][i])
            else:
                fixed_line[i] = fixed_line[i]+number_list[line][i]
    hold : list = []
    method_list = methods.split()
    start_val : int = 0
    for var in range(len(fixed_line)): 
        if fixed_line[var].strip() == "": 
            if method_list[0] == "+": 
                start_val = 0 
                for h in hold: start_val += h
            if method_list[0] == "*" : 
                start_val = 1 
                for h in hold: start_val *= h
            method_list.pop(0)
            totals.append(start_val)
            hold.clear()
            continue
        else: 
            hold.append(int(fixed_line[var].strip()))
        if var+1 == len(fixed_line): 
            if method_list[0] == "+": 
                start_val = 0 
                for h in hold: start_val += h
            if method_list[0] == "*" : 
                start_val = 1 
                for h in hold: start_val *= h
            method_list.pop(0)
            totals.append(start_val)
            hold.clear()
            continue
        
    print(sum(totals))
            
            

do_thing_02()