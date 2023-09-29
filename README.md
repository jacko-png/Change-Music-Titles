# Change-Music-Titles
After translating a track list from the back of your CD, you can use this toolset to apply this translation to the titles of your ripped music. It does not apply to the filename (but can be easily edited to do so by renaming the file when the title is changed, and grabbing the track number <(start here)[`https://mutagen.readthedocs.io/en/latest/api/id3.html#mutagen.easyid3.EasyID3`]> when the title is grabbed.

Steps:
1. Translate your music such that each song title is prefixed with its track number and a full stop. //The patterns are made to work with English words iirc. Mileage may vary when translating from the Latin alphabet into other character sets ([A-Za-z] was used in at least one version).
2. Run `Parse from printed list.py` with the 'raw' data as the input.

   — This generates an ordered list.
4. Move `Change titles.py` to the directory with the music
5. Run `Change titles.py` with the file generated by `Parse from printed list.py` as the input
6. Input the path to the music files when prompted with `Music files are in `

   — If the music files and `Change titles.py` are in the same directory, press enter.
7. Wait for the script to finish

Disclaimer:
This is probably coded really poorly, as I haven't formally learned coding yet. You could liken me to a ten-year-old on his C64 following his BASIC manual, kinda, but also someone with a goal in mind.
