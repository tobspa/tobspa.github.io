import os
import yaml

for fn in os.listdir('./raw'):
     if fn.endswith("yml"):
        endfile = open(fn[1:], 'w')
        src = open('./raw/' + fn, 'r')

        i = 1
        data = []
        awardee = dict()
        print fn
        council = ""
        name = ""
        for row in src:
            print i
            if i%2:
                name = str(row).strip()
            else:
                council = str(row).strip()
                awardee["council"] = council
                awardee["name"] = name
                print awardee
                data.append(awardee)
                awardee = dict()
            i += 1

        yaml.dump(data, endfile, default_flow_style=False)
        endfile.close()
        src.close()
