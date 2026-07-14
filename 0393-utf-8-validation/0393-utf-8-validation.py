class Solution:
    def validUtf8(self, data):
        remaining_bytes = 0
        
        for num in data:
            
            byte = num & 255

            
            if remaining_bytes == 0:

                if byte >> 7 == 0b0:
                    remaining_bytes = 0
                
                elif byte >> 5 == 0b110:
                    remaining_bytes = 1
                
                elif byte >> 4 == 0b1110:
                    remaining_bytes = 2
                
                elif byte >> 3 == 0b11110:
                    remaining_bytes = 3
                
                else:
                    return False
            
            
            else:
                
                if byte >> 6 == 0b10:
                    remaining_bytes -= 1
                else:
                    return False
                    
        
        return remaining_bytes == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna