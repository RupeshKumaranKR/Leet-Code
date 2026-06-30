class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
188 GB
        """
        passenger_changes = [0] * 1001
        
        for num_passengers, start, end in trips:
            passenger_changes[start] += num_passengers
            passenger_changes[end] -= num_passengers
            
        current_passengers = 0
        for change in passenger_changes:
            current_passengers += change
            if current_passengers > capacity:
                return False
                
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna