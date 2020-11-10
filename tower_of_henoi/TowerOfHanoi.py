from tower import *
from functions import *
class TowerOfHanoi:  
    def __init__(self, numdisk): 
        self.numdisk = numdisk
        self.n_move = 0
        self.prepare_towers()

    def prepare_towers(self): 
        a = Tower('a', self.numdisk)
        b = Tower('b')
        c = Tower('c')

        self.towers = [a, b, c] 
#should add functions here 
    def run(self): 
        self.showtower()
        a, b, c = self.towers
        self.mdisk(a, b, c, self.numdisk)

    def mdisk(self, a, b, c, n): 
        if n <= 0: 
            return

        self.mdisk(a, c, b, n - 1)

        self.n_move += 1
        print('disk is moved-{} from {} to {} ({}).'.format(str(n), a.name, b.name, self.n_move))
        disk = a.pop()
        b.push(disk)
        self.showtower()
        self.mdisk(c, b, a, n - 1)

    def showtower(self): 
        for tx in self.towers: 
            print(tx)