# The file must be in the folder with the script.
file = "file.txt"


def list_of_string(file):
    f = open(file, 'r')
    los = [line.strip() for line in f]
    return los


def time_codes(file):
    tc = []
    los = list_of_string(file)
    for i in range(1, len(los) - 1, 2):
        tc.append(los[i])
    return tc


def list_of_phrases(file):
    lop = []
    los = list_of_string(file)
    for i in range(2, len(los) - 1, 2):
        lop.append(los[i])
    return lop

def count_of_words_in_phrase(file):
    cow = []
    lop = list_of_phrases(file)
    for i in range(len(lop)):
        cow.append((len(lop[i].split())))
    return cow

def lineal_string(file):
    ls = ""
    lop = list_of_phrases(file)
    for i in range(len(lop)):
        ls += " "+lop[i]
    return ls


def list_of_transleted(file):
    from googletrans import Translator
    text = lineal_string(file)
    translator = Translator()

    w = translator.translate(text)
    lot = w.text.split()
    return lot


def list_of_transleted_phrases(file):
    cow = count_of_words_in_phrase(file)
    lotph = []
    count_of_words = 0
    lotph_string = ""
    lot = list_of_transleted(file)
    for i in range(len(cow)):
        count_of_words += cow[i]
        lotph_string = " ".join(map(str, lot[(count_of_words - cow[i]):(count_of_words)]))
        lotph.append(lotph_string)
    return lotph

def time_for_framerate(file):
    list_of_time = [0]
    time = 0
    tc = time_codes(file)
    for i in range(1, len(tc)):
        time = int(tc[i][0] + tc[i][1])*60 + int(tc[i][3] + tc[i][4]) - (int(tc[i-1][0] + tc[i-1][1])*60 + int(tc[i-1][3] + tc[i-1][4]))
        list_of_time.append(time)
    return list_of_time

print(time_for_framerate(file))
print(time_codes(file))
print(len(time_for_framerate(file)))
print(len(time_codes(file)))
