class Solution:
    def maximumUnits(self, boxes: List[List[int]], truckSize: int) -> int:
        boxes.sort(key = lambda x:-x[1])
        totalBox = 0
        totalUnit = 0
        
        for num,unit in boxes:
            if totalBox + num <= truckSize:
                currBox =  min(num,truckSize - totalBox)
                totalUnit += currBox * unit
                totalBox += currBox
            else:
                currBox =  min(num,truckSize - totalBox)
                totalUnit += currBox * unit
                totalBox += currBox
                return totalUnit
        
        return totalUnit
        