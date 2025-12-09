#day_07_input = open("2025 AoC Advent Calander/07-test-input.txt","r")
day_07_input = open("2025 AoC Advent Calander/07-input.txt","r")

laser_board : list = []

def clean_input() -> None: 
    global laser_board
    for line in day_07_input.readlines(): 
        hold = line.replace("\n","")
        laser_board.append(hold)

def do_thing_01() -> None:
    print("\n") 
    clean_input()
    split_count : int = 0
    laser_pos : list = []
    laser_pos.append(laser_board[0].find("S"))
    for line in laser_board: 
        hold = line
        old_l_pos = laser_pos.copy()
        while hold.find("^") > -1: 
            idx = hold.find("^")
            hold = hold[:idx]+"!"+hold[idx+1:]
            if idx in old_l_pos: 
                laser_pos.remove(idx)
                split_count += 1
                if idx-1 not in laser_pos: 
                    laser_pos.append(idx-1)
                if idx+1 not in laser_pos: 
                    laser_pos.append(idx+1)
        print(hold)
    print(split_count)

def kinda_do_thing_02() -> None:
    print("\n") 
    clean_input()
    timeline_count : int = 0
    all_laser : list = []
    all_line : list = []
    all_laser.append(laser_board[0].find("S"))
    old_l_pos : list = all_laser.copy()
    iter : int = 0
    for line in laser_board: 
        hold = line
        hold_idx : list = []
        while hold.find("^") > -1: 
            idx = hold.find("^")
            hold_idx.append(idx)
            hold = hold[:idx]+"*"+hold[idx+1:]
        if line.find("^") == -1: continue
        for id in hold_idx: 
            if id in old_l_pos: 
                for x in range(old_l_pos.count(id)):
                    all_line.append(id-1)
                    all_line.append(id+1)
                    old_l_pos.remove(id)
        all_line.extend(old_l_pos)
        hold_idx.clear()
        old_l_pos = all_line.copy()
        print(f"{iter} {line}")
        iter += 1
        if line == laser_board[-2]: 
            print(len(all_line))
        all_line.clear()
        #print(hold)
    #print(len(all_laser[-1]))

def do_thing_02()-> None: 
    print("\n") 
    clean_input()
    new_line : list = []
    old_line : list = []
    for chara in laser_board[0]: 
        if chara == "S": 
            new_line.append(1)
        else: new_line.append(0)
    old_line = new_line.copy()
    for line in laser_board: 
        hold = line
        hold_idx : list = []
        if line.find("^") == -1: continue
        while hold.find("^") > -1: 
            idx = hold.find("^")
            hold_idx.append(idx)
            hold = hold[:idx]+"*"+hold[idx+1:]
        for i in range(len(old_line)): 
            if i in hold_idx: 
                new_line[i] = 0
                new_line[i-1] += old_line[i]
                new_line[i+1] += old_line[i]
        old_line = new_line.copy()
    print(sum(new_line))
        
        

do_thing_02()
