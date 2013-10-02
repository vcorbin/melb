from rodents import Rodent

rodents = {}

inF = open("rodents.csv","r")

for line in inF:
    info = line.strip("\n").split(",")
    if info[0] not in rodents:
        rodents[info[0]] = Rodent(info[0])
    else:
        pass
    rodents[info[0]].add_weight(info[1])

print rodents
for key in rodents:
    print rodents[key].tag_id, rodents[key].weights
