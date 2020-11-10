from toh import *
from tower import *
from TowerOfHanoi import *
def run(self): 
    self.showtower()
    a, b, c = self.towers
    self.mdisk(a, b, c, self.numdisk)

def mdisk(self, a, b, c, n): 
    if n <= 0: 
        return
    self.mdisk(a, c, b, n - 1)
    self.n_move += 1
    print('moving  disk-{} from {} to {} ({}).'.format(str(n), a.name, b.name, self.n_move))
    disk = a.pop()
    b.push(disk)
    self.showtower()
    self.mdisk(c, b, a, n - 1)


def showtower(self): 
    for tower  in self.towers: 
        print(tower)