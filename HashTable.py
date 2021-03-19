# Hash Entry Class************************************************
class HashEntry:

	def _init_(self, key, item):
		self.key = key
		self.item = item

#Hash Table Class **********************************************
class HashTable:

    def __init__(self, initial_capacity=150):
		self.table = []
		for i in range(initial_capacity):
			self.table.append([])

#Creating Hash Key function ************************************
	def create_hash_key(self, key):
		bucket = int(key) % len(self.map)
		return bucket

# Look Up Function ******************************************
    def look_up(self, key):
        hash_key = self._get_hash(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None

# Insert function ***********************************************
	def insert(self,key,value):
		hash_key = self.createHashKey(key)
		key_value = [key, value]

		if self.map[hash_key] is None:
			self.map[hash_key] = list([key_value])
			return True
		else:
			for pair in self.map[hash_key]:
				if pair[0] == key:
					pair[1] == key_value
					return True

# Delete Function *********************************************
    def delete(self, key):
        hash_key = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True
        return False