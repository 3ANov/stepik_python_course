import json

answer = {}

with open('input.json') as f:
    for cls in json.load(f):
        print(cls)
        if not answer.get(cls['name']):
            answer[cls['name']] = 0
        for pr in cls['parents']:
            if answer.get(pr) is None:
                answer[pr] = 1
                answer[cls['name']] = 0
            else:
                i = answer[pr]
                answer[pr] = i+1


        print(answer)


        # print(cls['parents'])
        # if not cls['parents']:
        #     answer[cls['name']] = 0
        # else:
        #     answer[cls['name']] = 0
        #     for pr in cls['parents']:
        #         if answer.get(pr) is None:
        #             answer[pr] = 1
        #         else:
        #             i = answer[pr]
        #             answer[pr] = i+1

    #print(answer)
    print()

    sd = sorted(answer.items())
    for k, v in sd:
        print(k, v)
