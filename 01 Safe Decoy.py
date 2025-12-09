import copy
day_01_input = open('2025 AoC Advent Calander/01-input.txt','r')
#day_01_input = open('2025 AoC Advent Calander/01-test-input.txt','r')
safe_turns : list = [] 

def cleanup_safe_turns() -> None: 
    global safe_turns 
    safe_turns = day_01_input.readlines()
    new_turns : list = []
    for turn in safe_turns: 
        hold = turn
        hold = hold.strip()
        hold = hold.replace("\\n","")
        new_turns.append(hold)
    safe_turns.clear
    safe_turns = copy.deepcopy(new_turns)

def do_the_thing_day_1() -> None: 
    cleanup_safe_turns()
    current_num : int = 50
    times_hit_zero : int = 0
    #print(len(safe_turns))
    for turn in safe_turns: 
        if turn[0] == "R":
            current_num += int(turn[1:])
        if turn[0] == "L":
            current_num -= int(turn[1:])
        while current_num < 0 : 
            current_num += 100
            #times_hit_zero += 1
            #print(str(current_num))
        while 100 <= current_num: 
            current_num -= 100
            #times_hit_zero += 1
            #print(str(current_num))
        if current_num == 0 or current_num == 100: 
            times_hit_zero += 1
            print("- " +str(current_num))
    print(times_hit_zero)

def doesnt_do_the_thing_day_2() -> None: 
    print("\n")
    cleanup_safe_turns()
    current_num : int = 50
    times_hit_zero : int = 0
    before_num : int = current_num
    var_change : int = 0
    for turn in safe_turns: 
        if turn[0] == "R": 
            var_change = int(turn[1:])
            if current_num == 100: current_num -= 100
            current_num += var_change
        if turn[0] == "L": 
            var_change = -int(turn[1:])
            if current_num == 0: current_num += 100
            current_num += var_change
            if current_num == 0: 
                times_hit_zero += 1
                print(f"vvv +0 = {times_hit_zero}")
        print(f"{current_num - var_change} {var_change} = {current_num}")
        while current_num >= 100 : 
            current_num -= 100
            times_hit_zero += 1
            print(f"+0 = {times_hit_zero}")
        while current_num < 0 : 
            current_num += 100
            times_hit_zero += 1
            print(f"+0 = {times_hit_zero}")
            
    print(times_hit_zero)

def do_the_thing_day_2() -> None: 
    print("\n")
    cleanup_safe_turns()
    current_num : int = 50
    times_hit_zero : int = 0
    var_change : int = 0
    for turn in safe_turns: 
        if turn[0] == "R":
            var_change = int(turn[1:])
        if turn[0] == "L": 
            var_change = -int(turn[1:])
        if abs(var_change) >= 100: 
            #print (f"%%%%%%{var_change} => {abs(int(var_change/100))}%%%%%%")
            times_hit_zero += abs(int(var_change/100))
            if var_change < 0: var_change = (abs(var_change)%100)*-1
            else: var_change = abs(var_change)%100
        #print(f"{current_num}+{var_change}={current_num+var_change}")
        current_num += var_change
        if var_change == 0: 
            continue
        if current_num == 0: 
            times_hit_zero += 1
            #print("0 === Ping! === 0")
        if current_num == 100: 
            times_hit_zero += 1
            current_num = 0
            #print("100 === Ping!  === 100")
        if current_num > 100: 
            times_hit_zero +=1
            current_num -= 100
            #print("+++++  Ping!  ++++++")
        if current_num < 0: 
            if current_num != var_change: 
                #print("-----   Ping!  ------")
                times_hit_zero += 1
            current_num += 100
    print(times_hit_zero)
do_the_thing_day_2()
#do_the_thing_day_1()
#cleanup_safe_turns()