# Python3 字典模拟，代码如下：
class UndergroundSystem:

    def __init__(self):
        self.checkInDic = dict()
        self.dic = dict()


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInDic[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        val = t - self.checkInDic[id][1]
        name = self.checkInDic[id][0] +"_"+ stationName
        if name not in self.dic:
            self.dic[name] = [val]
        else:
            self.dic[name] += [val]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        alist = self.dic[startStation+"_"+ endStation]
        return sum(alist) / len(alist)



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)