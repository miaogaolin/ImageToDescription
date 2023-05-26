import csv
import json
from collections import Counter
import re


def readAllImageName(path):
    data = {}
    try:
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                data[row[1]] = row[2]

    except FileNotFoundError:
        pass
    return data

def cut_sentence(text):
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        text = text.replace(ch, " ") 
    return text.split()

if __name__ == '__main__':
    saveData = []
    fast = readAllImageName("./fast.csv")
    classic = readAllImageName("./classic.csv")

    fastWords = []
    classicWords = []
    for key in fast:
        if key not in classic:
            continue
        fastWords.extend(cut_sentence(fast[key].lower()))
        classicWords.extend(cut_sentence(classic[key].lower()))
        saveData.append({'image': key, 'fast': fast[key], 'classic': classic[key]})
    
    fastWordCounts = Counter(fastWords)
    classicWordCounts = Counter(classicWords)

    fastWordCountsData = []
    classicWordCountsData = []
    for word, count in sorted(fastWordCounts.items(), key=lambda x: x[1], reverse=True):
        fastWordCountsData.append([word, count, round(count/len(fastWords), 4)])

    for word, count in sorted(classicWordCounts.items(), key=lambda x: x[1], reverse=True):
        classicWordCountsData.append([word, count,  round(count/len(classicWords), 4)]) 

    content = f'''
    export const images = {json.dumps(saveData)};
    export const fastWords = {fastWordCountsData};
    export const classicWords = {classicWordCountsData};
    '''
    with open('front/src/routes/data.js', 'w') as f:
        f.write(content)