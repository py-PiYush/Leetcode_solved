class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        s = set()
        j, last = 0, 0
        for i in range(len(buses)):
            cnt = 0
            while cnt<capacity and j<len(passengers) and passengers[j]<=buses[i]:
                last = passengers[j]
                s.add(last)
                j+=1
                cnt+=1
            if i==len(buses)-1 and cnt<capacity and last<buses[i]: return buses[-1]
        if len(s)==0:
            return buses[-1]
        
        while last in s:
            last-=1
        return last