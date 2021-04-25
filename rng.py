class Random:
    def __init__(self, seed, shift):
        self.seed = seed
        self.shift = shift
    
    def next(self):
        number = self.seed
        number ^= ((number % 0x100000000) >> self.shift[0]) & 0xffffffff
        number ^= (number << self.shift[1]) & 0xffffffff
        number ^= ((number % 0x100000000) >> self.shift[2]) & 0xffffffff
        self.seed = (number % 0x100000000) >> 0
        return self.seed
    
    def nextFloat(self):
        return self.next() * 2.3283061589829401E-10

"""
export class Rng
{
    seed: number = 0;
    shift: [number, number, number] = [0,0,0];
    next() : number
    {
        let num = this.seed;
        num ^= (num >>> this.shift[0]) & 0xffffffff;
        num ^= (num << this.shift[1]) & 0xffffffff;
        num ^= (num >>> this.shift[2]) & 0xffffffff;
        this.seed = num >>> 0;
        return this.seed;
    }

    constructor(seed: number, shift: [number, number, number])
    {
        this.seed = seed;
        this.shift = shift;
    }

    nextFloat() : number
    {
        const multi = Math.fround(2.3283061589829401E-10);
        return Math.fround(this.next() * multi);
    }
};
"""