import csv
import json


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

if __name__ == '__main__':
    saveData = []
    fast = readAllImageName("./fast.csv")
    classic = readAllImageName("./classic.csv")
    for key in fast:
        if key not in classic:
            continue
        saveData.append({'image': key, 'fast': fast[key], 'classic': classic[key]})
    
    with open('front/src/routes/data.js', 'w') as f:
        f.write('export const images ='+json.dumps(saveData)+';')