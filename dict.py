class My_table:
    def __init__(self, h, v, k):
        self.hash = h
        self.key = k
        self.value = v
        
class Mydict:
    def __init__(self):
        self.size = 8
        self.ma_used = 0
        self.ma_version = 0
        self.ma_table = [None] * self.size 
    
    def __setitem__(self, key, value):
        h = hash(key)
        slot = h % self.size
        while self.ma_table[slot] != None:
            if self.ma_table[slot].key == key:
                self.ma_table[slot].value = value
                return

            else:
                slot = (slot + 1) % self.size
        
        self.ma_table[slot] = My_table(h,value,key)
        self.ma_used += 1
        self.ma_version += 1

    def __getitem__(self, key):
        slot = hash(key) % self.ma_size
        start_slot = slot

        while self.ma_table[slot] != None:
            if self.ma_table[slot].key == key:
                return self.ma_table[slot].value
            slot = (slot + 1) % self.ma_size
            if slot == start_slot:
                break
        raise KeyError(f"Key {key} not found")
            
    def __contains__(self, key):
        slot = hash(key) % self.ma_size
        start_slot = slot

        while self.ma_table[slot] != None:
            if self.ma_table[slot].key == key:
                return True
            slot = (slot + 1) % self.ma_size
            if slot == start_slot:
                break
        return False