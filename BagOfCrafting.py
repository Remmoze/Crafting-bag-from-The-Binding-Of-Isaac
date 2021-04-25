from rng import Random

class Bag:
    def __init__(self, pools, itemQual):
        self.pools = pools
        self.itemQualities = itemQual
        self.maxId = max(self.itemQualities.map.keys())

    def calculate(self, components):
        rng = Random(0x77777770, [0, 0, 0])

        if len(components) != 8 or components is None:
            print("invalid items")
            return None
        
        components.sort()
        compTotalWeight = 0
        compCounts = [0] * len(ComponentShifts)
        for compId in components:
            compCounts[compId] += 1
            compTotalWeight += ComponentWeights[compId]
            rng.shift = ComponentShifts[compId]
            rng.next()
        rng.shift = ComponentShifts[6]

        poolWeights = [
            { "idx": 0, "weight": 1 },
            { "idx": 1, "weight": 2 },
            { "idx": 2, "weight": 2 },
            { "idx": 4, "weight": compCounts[4] * 10 },
            { "idx": 3, "weight": compCounts[3] * 10 },
            { "idx": 5, "weight": compCounts[6] * 5 },
            { "idx": 8, "weight": compCounts[5] * 10 },
            { "idx": 12, "weight": compCounts[7] * 10 },
            { "idx": 9, "weight": compCounts[25] * 10 },
        ]

        if (compCounts[8] + compCounts[1] + compCounts[12] + compCounts[15] == 0):
            poolWeights.append({ "idx": 26, "weight": compCounts[23] * 10 })
        
        totalWeight = 0
        itemWeights = [0] * 730

        for poolWeight in poolWeights:
            if poolWeight["weight"] <= 0:
                continue
            
            qualityMin = 0
            qualityMax = 1
            n = compTotalWeight
            if poolWeight["idx"] >= 3 and poolWeight["idx"] <= 5:
                n -= 5

            if n > 34: 
                qualityMin = 4
                qualityMax = 4
            elif n > 30: 
                qualityMin = 3
                qualityMax = 4
            elif n > 26:
                qualityMin = 2
                qualityMax = 4
            elif n > 22:
                qualityMin = 1
                qualityMax = 4
            elif n > 18:
                qualityMin = 1
                qualityMax = 3
            elif n > 14:
                qualityMin = 1
                qualityMax = 2
            elif n > 8:
                qualityMin = 0
                qualityMax = 2

            pool = self.pools[poolWeight["idx"]]
            for item in pool.items:
                quality = self.itemQualities.get(item.id)
                if quality < qualityMin or quality > qualityMax:
                    continue
                
                w = item.weight * poolWeight["weight"]
                itemWeights[item.id] += w
                totalWeight += w
        
        if totalWeight <= 0:
            return 25
        
        target = rng.nextFloat() * totalWeight
        for i in range(len(itemWeights)):
            if target < itemWeights[i]:
                return i
            target -= itemWeights[i]
        
        return 25


ComponentShifts = [
    [0x00000001, 0x00000005, 0x00000010],
    [0x00000001, 0x00000005, 0x00000013],
    [0x00000001, 0x00000009, 0x0000001D],
    [0x00000001, 0x0000000B, 0x00000006],
    [0x00000001, 0x0000000B, 0x00000010],
    [0x00000001, 0x00000013, 0x00000003],
    [0x00000001, 0x00000015, 0x00000014],
    [0x00000001, 0x0000001B, 0x0000001B],
    [0x00000002, 0x00000005, 0x0000000F],
    [0x00000002, 0x00000005, 0x00000015],
    [0x00000002, 0x00000007, 0x00000007],
    [0x00000002, 0x00000007, 0x00000009],
    [0x00000002, 0x00000007, 0x00000019],
    [0x00000002, 0x00000009, 0x0000000F],
    [0x00000002, 0x0000000F, 0x00000011],
    [0x00000002, 0x0000000F, 0x00000019],
    [0x00000002, 0x00000015, 0x00000009],
    [0x00000003, 0x00000001, 0x0000000E],
    [0x00000003, 0x00000003, 0x0000001A],
    [0x00000003, 0x00000003, 0x0000001C],
    [0x00000003, 0x00000003, 0x0000001D],
    [0x00000003, 0x00000005, 0x00000014],
    [0x00000003, 0x00000005, 0x00000016],
    [0x00000003, 0x00000005, 0x00000019],
    [0x00000003, 0x00000007, 0x0000001D],
    [0x00000003, 0x0000000D, 0x00000007],
    [0x00000003, 0x00000017, 0x00000019],
    [0x00000003, 0x00000019, 0x00000018],
    [0x00000003, 0x0000001B, 0x0000000B],
    [0x00000004, 0x00000003, 0x00000011],
    [0x00000004, 0x00000003, 0x0000001B],
    [0x00000004, 0x00000005, 0x0000000F],
    [0x00000005, 0x00000003, 0x00000015],
    [0x00000005, 0x00000007, 0x00000016],
    [0x00000005, 0x00000009, 0x00000007],
    [0x00000005, 0x00000009, 0x0000001C],
    [0x00000005, 0x00000009, 0x0000001F],
    [0x00000005, 0x0000000D, 0x00000006],
    [0x00000005, 0x0000000F, 0x00000011],
    [0x00000005, 0x00000011, 0x0000000D],
    [0x00000005, 0x00000015, 0x0000000C],
    [0x00000005, 0x0000001B, 0x00000008],
    [0x00000005, 0x0000001B, 0x00000015],
    [0x00000005, 0x0000001B, 0x00000019],
    [0x00000005, 0x0000001B, 0x0000001C],
    [0x00000006, 0x00000001, 0x0000000B],
    [0x00000006, 0x00000003, 0x00000011],
    [0x00000006, 0x00000011, 0x00000009],
    [0x00000006, 0x00000015, 0x00000007],
    [0x00000006, 0x00000015, 0x0000000D],
    [0x00000007, 0x00000001, 0x00000009],
    [0x00000007, 0x00000001, 0x00000012],
    [0x00000007, 0x00000001, 0x00000019],
    [0x00000007, 0x0000000D, 0x00000019],
    [0x00000007, 0x00000011, 0x00000015],
    [0x00000007, 0x00000019, 0x0000000C],
    [0x00000007, 0x00000019, 0x00000014],
    [0x00000008, 0x00000007, 0x00000017],
    [0x00000008, 0x00000009, 0x00000017],
    [0x00000009, 0x00000005, 0x0000000E],
    [0x00000009, 0x00000005, 0x00000019],
    [0x00000009, 0x0000000B, 0x00000013],
    [0x00000009, 0x00000015, 0x00000010],
    [0x0000000A, 0x00000009, 0x00000015],
    [0x0000000A, 0x00000009, 0x00000019],
    [0x0000000B, 0x00000007, 0x0000000C],
    [0x0000000B, 0x00000007, 0x00000010],
    [0x0000000B, 0x00000011, 0x0000000D],
    [0x0000000B, 0x00000015, 0x0000000D],
    [0x0000000C, 0x00000009, 0x00000017],
    [0x0000000D, 0x00000003, 0x00000011],
    [0x0000000D, 0x00000003, 0x0000001B],
    [0x0000000D, 0x00000005, 0x00000013],
    [0x0000000D, 0x00000011, 0x0000000F],
    [0x0000000E, 0x00000001, 0x0000000F],
    [0x0000000E, 0x0000000D, 0x0000000F],
    [0x0000000F, 0x00000001, 0x0000001D],
    [0x00000011, 0x0000000F, 0x00000014],
    [0x00000011, 0x0000000F, 0x00000017],
    [0x00000011, 0x0000000F, 0x0000001A]
]

ComponentWeights = [
    0x00000000,
    0x00000001,
    0x00000004,
    0x00000005,
    0x00000005,
    0x00000005,
    0x00000005,
    0x00000001,
    0x00000001,
    0x00000003,
    0x00000005,
    0x00000008,
    0x00000002,
    0x00000005,
    0x00000005,
    0x00000002,
    0x00000006,
    0x0000000A,
    0x00000002,
    0x00000004,
    0x00000008,
    0x00000002,
    0x00000002,
    0x00000004,
    0x00000004,
    0x00000002
]