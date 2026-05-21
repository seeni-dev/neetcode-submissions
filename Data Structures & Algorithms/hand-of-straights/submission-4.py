class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        cardCount = {}
        for c in hand:
            cardCount[c] = cardCount.get(c, 0)+ 1
    
        for num in hand:
            if cardCount[num]:
                for j in range(num, num+groupSize):
                    if cardCount.get(j, 0) == 0:
                        return False
                    cardCount[j] -=1
        return True
