from loader import load_items, load_bag
import time

items = load_items()
craftingBag = load_bag()

fs = open("combinations_all.txt", "r")

def getName(id):
    filename = str(id).zfill(3) + " - "
    if id in items:
        filename += "".join(x for x in items[id].name if (x.isalnum() or x in "._- "))
    else:
        filename += "Unknown"
    return filename + ".txt"

def addCombo(id, combo):
    item_fs = open("./item_combinations/" + getName(id), "a+", encoding='utf-8')
    item_fs.write(str(combo) + "\n")
    item_fs.close()

addCombo(1, [1, 1, 1, 2])

total_items_count = sum(1 for line in open('combinations_all.txt', 'r', encoding='utf-8'))

start = time.time()
items_added = 0
items_prev = 0
for line in fs.readlines():
    combo = list(map(int, line.split(',')))
    result = craftingBag.calculate(combo)
    addCombo(result, combo)
    items_added += 1
    if(items_added - items_prev > 10000):
        items_prev = items_added
        print("Added " + str(items_added) + " in total. ~" + str((time.time() - start) * (total_items_count - items_added)) + " seconds left")

end = time.time()
print("done in " + str(end-start))

fs.close()
fsw.close()