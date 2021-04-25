from jsonParser import loadPools, loadMeta
from BagOfCrafting import Bag

def load_bag():    
    fs1 = open("itempools.json", "r", encoding="utf-8")
    fs2 = open("items_metadata.json", "r", encoding="utf-8")

    pools = loadPools(fs1.read())
    meta = loadMeta(fs2.read())

    fs1.close()
    fs2.close()

    return Bag(pools, meta)