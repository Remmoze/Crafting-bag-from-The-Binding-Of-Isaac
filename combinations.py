fs = open("combinations_easy.txt", "w", encoding='utf-8')

def pickfrom(list, n):
    if(n == 0):
        return [[]]
    if len(list) == 0:
        return []
    return [[list[0]] + rest for rest in pickfrom(list, n-1)] + pickfrom(list[1:], n)

pickups = [1, 2, 8, 12, 15]

for line in pickfrom(pickups, 8):
    fs.write(str(line)[1:-1] + "\n")
fs.close()

"""
function pickfrom(list, n) {
  if (n === 0) return [[]];
  else if (list.length === 0) return [];
  else {
    let [x, ...xs] = list;
    return [...pickfrom(list, n-1).map(rest => [x, ...rest]), ...pickfrom(xs, n)];
  }
}

[...pickfrom(list, n-1).map(rest => 
        [x, ...rest]
    ), ...pickfrom(xs, n)];

"""
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