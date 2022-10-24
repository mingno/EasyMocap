import glob
import json

l = sorted(glob.glob('input/annots/*/*'))
for i in l:
    with open(i, 'r') as f:
        j = json.load(f)
        if len(j['annots']) != 2:
            print(i)
        if j['annots'][0]['bbox'][0] > j['annots'][1]['bbox'][0]:
            j['annots'][0],  j['annots'][1] =  j['annots'][1],  j['annots'][0]
            j['annots'][0]['personID'], j['annots'][1]['personID'] = j['annots'][1]['personID'], j['annots'][0]['personID']
        with open(i, 'w') as f:
            json.dump(j, f)
