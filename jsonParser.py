import json
from isaac import ItemPoolItem, ItemPool, ItemQualities

def loadPools(js):
    data = json.loads(js)
    pools = []
    for datapool in data:
        pool = ItemPool(datapool["Name"], [])
        for dataitem in datapool["Item"]:
            item = ItemPoolItem(int(dataitem["Id"]), float(dataitem["Weight"]))
            pool.addItem(item)
        pools.append(pool)
    return pools

def loadMeta(js):
    data = json.loads(js)["item"]
    items = ItemQualities()
    for dataitem in data:
        items.add(int(dataitem["id"]), int(dataitem["quality"]))
    return items
