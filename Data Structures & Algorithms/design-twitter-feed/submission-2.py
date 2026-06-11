import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.followers = {}
        self.tweets = defaultdict(list)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t +=1
        tweet = [
            self.t,
            tweetId
        ]
        self.tweets[userId].append(tweet)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        q = []
        for followee in self.followers.get(userId, []):
            # print("Ts", self.tweets[userId])
            for tweet in self.tweets[followee][-10:]:
                heapq.heappush_max(q, tweet)
        if userId not in self.followers.get(userId, []):
            for tweet in self.tweets[userId][-10:]:
                    heapq.heappush_max(q, tweet)

        print(q)
        res = []
        while q and len(res) < 10:
            print("Picking ", q[0])
            res.append(heapq.heappop_max(q)[1])
        print("res", res)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            return
        if followeeId not in self.followers[followerId]:
            return
        self.followers[followerId].remove(followeeId)
