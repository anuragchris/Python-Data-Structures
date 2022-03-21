from collections import Counter


class FrequencySort:

    # Link For Problem: https://leetcode.com/problems/sort-array-by-increasing-frequency/

    def frequencySort(self, nums: list[int]) -> list[int]:

        r = Counter(nums).most_common()
        r.sort(key=lambda x: x[0], reverse=True)
        r.sort(key=lambda x: x[1])

        t = []
        for i in r:
            a, b = i
            t.extend([a]*b)

        return t

    def another_solution(self, nums: list[int]) -> list[int]:
        r = Counter(nums)
        return sorted(nums, key=lambda x: (r[x], -x))

    def simple_solution(self, nums: list[int]) -> list[int]:
        return sorted(sorted(nums, reverse=True), key=nums.count)

    # Link For Problem: https://leetcode.com/problems/sort-characters-by-frequency/

    def frequencySort(self, s: str) -> str:

        myDict = Counter(s)
        size: int = len(myDict)

        ans = []

        occurence_pair = myDict.most_common(size)

        for char, occurrence in occurence_pair:
            ans += [char]*occurrence

        return ''.join(ans)

    def count_array(self, s: str) -> str:

        count = [[i, 0] for i in range(128)]

        for i in s:
            count[ord(i)][1] += 1

        count.sort(reverse=True, key=lambda x: x[1])

        ans = ''
        for i in count:
            ans += chr(i[0])*i[1]

        return ans

    def optimization(self, s: str) -> str:

        count = [0 for i in range(128)]

        for i in s:
            print(ord(i))
            count[ord(i)] += 1

        target: int = self.__findMax(count)
        ans = ''

        while(target > 0):

            while(count[target] > 0):
                ans += chr(target)
                count[target] -= 1

            target = self.__findMax(count)

        return ans

    def __findMax(self, count: list[int]) -> int:

        index: int = -1
        max: int = 0

        for i in range(128):
            if count[i] > max:
                max = count[i]
                index = i

        return index
