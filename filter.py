
fs = open("results.txt", "r")
fsw = open("results_filtered.txt", "w", encoding='utf-8')

weights_values = [1000, 1, 3, 5, 5, 6, 5, 5, 1, 3, 5, 5, 1, 5, 10, 1, 5, 50, 3, 3, 10, 3, 3, 3, 10, 10]


results = {}
def add(combo, weight):
    if weight not in results:
        results[weight] = []
    results[weight].append(combo)    

for line in fs.readlines():
    combo = list(map(int, line.split(',')))
    weight = sum([weights_values[i] for i in combo])
    add(combo, weight)

sorted_dict = {k: results[k] for k in sorted(results)}
print(sorted_dict)
for weight in sorted_dict:
    for combo in sorted_dict[weight]:
        fsw.write(str(combo) + " -> " + str(weight) + "\n")

fsw.close()
fs.close()

"""
#0  - empty
1   - red heart
2   - soul heart
#3  - black heart
#4  - white heart
#5  - gold heart
#6  - bone heart
#7  - rotten heart
8   - penny
#9  - nickle
#10 - dime
#11 - lucky penny
12  - key
#13 - golden key
#14 - charged key 
15  - bomb
#16 - golden bomb
#17 - giga bomb
18  - micro battery
19  - lil battery
#20 - mega battery
21  - card
22  - pill
23  - rune
#24 - dice shard
#25 - key piece

"""