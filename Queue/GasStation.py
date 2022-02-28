# Link For Problem : https://leetcode.com/problems/gas-station/

from ast import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pos = 0
        sumTemp = 0
        total = 0

        for i in range(len(gas)):
            sumTemp += gas[i]-cost[i]
            if(sumTemp < 0):
                total += sumTemp
                sumTemp = 0
                pos = i+1

        total += sumTemp
        return -1 if total < 0 else pos
