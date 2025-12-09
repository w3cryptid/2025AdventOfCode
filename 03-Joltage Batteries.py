import copy
import math
day_03_input = open('2025 AoC Advent Calander/03-input.txt','r')
#day_03_input = open('2025 AoC Advent Calander/03-test-input.txt','r')
batteries_list : list = [] 

def batteries() -> None: 
    global batteries_list
    for batt in day_03_input.readlines():
        hold = batt.strip() 
        hold = hold.replace("\n","")
        batteries_list.append(hold)

def do_the_thing_1() -> None: 
    batteries()
    biggest_batteries:list = []
    for battery in batteries_list:
        first_big = find_highest(battery,0,len(battery)-1)
        second_big = find_highest(battery,first_big[1]+1,len(battery))
        #print(f"{first_big[0]}{second_big[0]}")
        biggest_batteries.append(int(str(first_big[0])+str(second_big[0])))
    print(sum(biggest_batteries))

def do_the_thing_2() -> None: 
    batteries()
    print('\n')
    big_list:list = []
    bigbig : list = []
    bat_len = len(batteries_list)
    for b in range(bat_len):
        battery = batteries_list[b]
        bigbig = find_highest(battery,0,len(battery)-11)
        big_list.append(str(bigbig[0]))
        for x in range(11):
            bigbig = find_highest(battery,bigbig[1]+1,len(battery)-(10-x))
            big_list[b] = big_list[b] + str(bigbig[0])
        for big in range(len(big_list)): 
            big_list[big] = int(big_list[big])
    print(sum(big_list))

def find_highest(battery:str, start:int, end:int) -> list: 
    highest : int = 0 
    position_a : int = -1
    for i in range(9): 
        if highest > 9-i: continue
        search = 9-i
        position_a = battery.find(str(search),start,end)
        if position_a != -1: highest = 9-i
    return [highest, position_a]


do_the_thing_2()
#do_the_thing_1()