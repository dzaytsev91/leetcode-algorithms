class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
      
        def can_ship(cap):
            total_days = 1
            current_weight = 0

            for weight in weights:
                current_weight += weight

                if current_weight > cap:
                    current_weight = weight
                    total_days += 1
            return total_days <= days
                    
        
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right-left) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return right
