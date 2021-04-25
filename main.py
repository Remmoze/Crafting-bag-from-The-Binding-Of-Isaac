from pprint import pprint
from loader import load_bag
import time

fs = open("combinations_easy.txt", "r")
fsw = open("results_easy.txt", "w", encoding='utf-8')

craftingBag = load_bag()

i = 0
start = time.time()
for line in fs.readlines():
    result = craftingBag.calculate(list(map(int, line.split(','))))
    if(result == 585):
        fsw.write(line)
        i += 1
        print("FOUND " + str(i))

end = time.time()
print("done in " + str(end-start))

fs.close()
fsw.close()


print(craftingBag.calculate([7, 9, 10, 10, 12, 12, 12, 19]))
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