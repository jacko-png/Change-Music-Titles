import os
import re
from sys import argv

ordered_list = []
def do_this_file(input_file, max_num = 0):
    with open(input_file) as f:
        data = f.read()
        for match in re.findall(r'\d+\.', data):
            match = re.match(r'\d+', match).group(0)
            this_num = int(match)
            if this_num > max_num:
                max_num = this_num
        # print(max_num)
        
        i=0
        while i < max_num:
            i += 1
            matches = re.search(r'\b0?(?P<num>' + str(i) + r')\.\s?(?P<tit>.*?)(?=\b\d+\.|$)', data, re.MULTILINE) #does 0-9 cause issues there? there is still the edge case of numbers at the end of the name
            if matches != None:
                track_number = matches.group('num')
                title = matches.group('tit').rstrip()
                ordered_list.append(f'{track_number}. {title}')
            

    with open(os.path.splitext(os.path.basename(input_file))[0] + '_out.txt', 'a') as f:
        for item in ordered_list:
            if item != None:
                f.write(item + '\n')

try:
    argv[1]
    there_is_input = True
except:
    there_is_input = False

if there_is_input:
    input_file = argv[1:]
    for f in input_file:
        do_this_file(f)
        ordered_list = []
else:
    input_file = input('Input file is ')
    do_this_file(input_file)