class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        left, right, boats = 0, len(people) -1,0
        while left <= right:
            if people[left] + people[right] <= limit:
                left +=1
            right -= 1
            boats += 1
        return boats