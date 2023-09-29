from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2
import mutagen
import re
import os
from sys import argv

# now that parse.py exists, assume an ordered list.

try:
    input_file = argv[1]
except:
    input_file = input('Input file is ')

subdir = input('Music files are in ')
subdir = os.path.basename(subdir)

supported_filetypes = [ 'mp3' ]
music_files = []

def rename_title(file, title):
    audio = ID3(file)
    audio.add(TIT2(encoding = 3, text = title))
    audio.save()

def v_test_index(anchor):
    for item in title_list:
        test_index = int(re.match(r'\d+', item).group(0))
        if anchor == test_index:
            return(item)
    return None

try:
    with open(input_file, 'r') as f:
        title_list = re.findall(r'^.*$', f.read(), re.MULTILINE)
except:
    raise Exception(f'Does the file {input_file} exist in location {(os.getcwd)}?')

# scandir is preferable to os.walk, unless you want subdirs
try:
    with os.scandir(os.path.join(os.getcwd(), subdir)) as children:
        for child in children:
            if child.is_file():
                extension = os.path.splitext(child)[1]
                if extension == '.mp3':
                    music_files.append(child.path)
except:
    raise Exception(f'Music files must be in .\\{subdir} and in these filetypes: {supported_filetypes}')

do_title_rename = True
for file in music_files:
    if not do_title_rename:
        do_title_rename = True
    
    audio = EasyID3(file)
    track_number = int(audio['tracknumber'][0])
    raw_title = title_list[track_number - 1]
    test_index = int(re.match(r'\d+', raw_title).group(0))
    if track_number == test_index:
        # good ending
        title = re.match(r'\d+\.\s(?P<tit>.*)', raw_title).group('tit')
    else:
        result = v_test_index(track_number)
        if result == None:
            do_title_rename = False
            # should have a log
            open('Change titles.log', 'a').append(f'No name found for {file}\n') # now I have a log
        else:
            title = re.match(r'\d+\.\s(?P<tit>.*)', result).group('tit')

    if do_title_rename:
        rename_title(file, title)
    