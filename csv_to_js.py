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
    items = text.split(",")
    items_stripped = [item.strip() for item in items]
    return items_stripped

if __name__ == '__main__':
    saveData = []
    fast = readAllImageName("./fast.csv")
    classic = readAllImageName("./classic.csv")
    best = readAllImageName("./best.csv")

    fastWords = []
    classicWords = []
    bestWords = []
    for key in fast:
        if key not in classic:
            continue
        if key not in best:
            continue

        fastWords.extend(cut_sentence(fast[key].lower()))
        classicWords.extend(cut_sentence(classic[key].lower()))
        bestWords.extend(cut_sentence(best[key].lower()))
        saveData.append({'image': key, 'fast': fast[key], 'classic': classic[key], 'best': best[key]})
    
    fastWordCounts = Counter(fastWords)
    classicWordCounts = Counter(classicWords)
    bestWordCounts = Counter(bestWords)

    fastWordCountsData = []
    classicWordCountsData = []
    bestWordCountsData = []
    for word, count in sorted(fastWordCounts.items(), key=lambda x: x[1], reverse=True):
        fastWordCountsData.append([word, count, round(count/len(fastWords), 4)])

    for word, count in sorted(classicWordCounts.items(), key=lambda x: x[1], reverse=True):
        classicWordCountsData.append([word, count,  round(count/len(classicWords), 4)]) 


    i = 0
    for word, count in sorted(bestWordCounts.items(), key=lambda x: x[1], reverse=True):
        i += 1
        if i > 10000:
            break
        bestWordCountsData.append([word, count,  round(count/len(bestWords), 4)]) 

    content = f'''
    export const images = {json.dumps(saveData)};

    export const fastWords = {fastWordCountsData};

    export const classicWords = {classicWordCountsData};

    export const bestWords = {bestWordCountsData};
    '''
    with open('front/src/routes/data.js', 'w') as f:
        f.write(content)