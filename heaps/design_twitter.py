from collections import deque, defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.tweets = deque()
        self.follows = defaultdict(lambda : set())

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = list()
        for tweet in self.tweets:
            if (tweet[0] == userId or tweet[0] in self.follows[userId]) and len(res) < 10:
                res.append(tweet[1])
            if len(res) == 10:
                break

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
