import math

print("\n---------------------")
print("start")
print("---------------------")

input_array : list = ["16100064-16192119","2117697596-2117933551","1-21","9999936269-10000072423","1770-2452","389429-427594","46633-66991","877764826-877930156","880869-991984","18943-26512","7216-9427","825-1162","581490-647864","2736-3909","39327886-39455605","430759-454012","1178-1741","219779-244138","77641-97923","1975994465-1976192503","3486612-3602532","277-378","418-690","74704280-74781349","3915-5717","665312-740273","69386294-69487574","2176846-2268755","26-45","372340114-372408052","7996502103-7996658803","7762107-7787125","48-64","4432420-4462711","130854-178173","87-115","244511-360206","69-86"]
#input_array : list = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"]
hold_array : list = []

def parse_array() -> None: 
    for range in input_array: 
        hold_range : list = range.split("-")
        #print(range)
        find_fake_values(int(hold_range[0]),int(hold_range[1]))
        #print("\n")
    #print(hold_array)
    #print(sum(hold_array))


def find_fake_values(begin:int, end:int) -> None: 
    bigger : bool = False
    begin_string : str = str(begin)
    cut_to = math.floor(len(begin_string)*0.5)
    if cut_to < 1 : cut_to = 1
    num_half = int(begin_string[:cut_to])
    while not bigger: 
        potential_num = int(str(num_half)+str(num_half))
        if potential_num < begin: 
            num_half += 1
            continue
        if potential_num > end: 
            bigger = True
        else: 
            hold_array.append(potential_num)
            #print(" - "+str(potential_num))
            num_half += 1

#parse_array()

# PART 2 -----------------------

def day_two_parse_array() -> None: 
    for range in input_array: 
        hold_range : list = range.split("-")
        print(f" =={range}==")
        day_two_fake_values(int(hold_range[0]),int(hold_range[1]))
    print(sum(hold_array))

def day_two_fake_values(two_begin:int, two_end:int) -> None: 
    iterate : int = 1
    end_string : str = str(two_end)
    biggest : int = math.ceil(len(str(end_string))*0.5)
    biggest = int(end_string[:biggest])
    hold_string : str = ""
    while iterate <= biggest: 
        begin_string : str = str(two_begin)
        while len(hold_string) < len(begin_string): 
            hold_string += str(iterate)
            #print(hold_string)
        if int(hold_string) < two_begin: 
            hold_string += str(iterate)
        if two_begin <= int(hold_string) and int(hold_string) <= two_end:
            if hold_array.count(int(hold_string)) == 0 and len(hold_string) > 1:
                hold_array.append(int(hold_string))
                print (f" - {hold_string}")
            hold_string += str(iterate)
        if  two_end < int(hold_string):
            hold_string : str = ""
            iterate += 1

day_two_parse_array()