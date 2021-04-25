class ItemPoolItem:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

class ItemPool:
    def __init__(self, name, items = []):
        self.name = name
        self.items = items

    def addItem(self, item):
        self.items.append(item)

class ItemQualities:
    def __init__(self):
        self.map = {}

    def get(self, ItemId):
        return self.map[ItemId]
    
    def add(self, ItemId, quality):
        self.map[ItemId] = quality

class Item:
    def __init__(self, type, name, id):
        self.type = type
        self.name = name
        self.id = id

class Items:
    def __init__(self):
        self.map = {}

    def add(self, id, item):
        self.map[id] = item

