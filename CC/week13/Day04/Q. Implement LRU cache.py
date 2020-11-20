## self.recentlyused.pop(0)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lrucache = {}
        self.recentlyused = []

    def get(self, key: int) -> int:
        if key in self.lrucache:
            self.recentlyused.remove(key)
            self.recentlyused.append(key)
            return self.lrucache[key]
        else:
            if key in self.recentlyused:
                self.recentlyused.remove(key)
            return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.lrucache) < self.capacity:
            if key in self.lrucache:
                self.recentlyused.remove(key)
                self.recentlyused.append(key)
                self.lrucache[key]=value
            else:
                if key not in self.recentlyused:
                    self.recentlyused.append(key)
                else:
                    self.recentlyused.remove(key)
                    self.recentlyused.append(key)                    
                    
                self.lrucache[key] = value
        else:
            if key in self.lrucache:
                self.recentlyused.remove(key)
                self.recentlyused.append(key)
                self.lrucache[key]=value
            else:

                self.lrucache.pop(self.recentlyused[0])
                self.recentlyused.pop(0)
                self.recentlyused.append(key)
                self.lrucache[key] = value
                
        # print(self.recentlyused)
        # print(self.lrucache)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)