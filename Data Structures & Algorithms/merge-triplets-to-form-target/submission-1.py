class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        filteredTriplets = []
        good = set()
        for triplet in triplets:
            invalidTuple = False
            for i, v in enumerate(target):
                if triplet[i] > v:
                    invalidTuple = True
                    break
            if not invalidTuple:
                for i, v in enumerate(target):
                    if triplet[i] == v:
                        good.add(i)
        return len(good) == 3

        