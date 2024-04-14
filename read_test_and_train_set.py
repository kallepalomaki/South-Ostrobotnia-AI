import json

if True:
    with open("../data/train_set.json") as f:
        for message in f:
            data=json.loads(message)
            print(data)

with open("../data/test_set.json") as f:
    for message in f:
        #print(message)
        data=json.loads(message)
        print(data)