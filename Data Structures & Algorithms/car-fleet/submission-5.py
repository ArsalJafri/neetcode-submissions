class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = sorted(zip(position, speed))

        print(arr)

        stack = [] 

        for i in range(len(arr) - 1, -1, -1):
    
            position, speed = arr[i]

            arrival_speed = (target - position) / speed

            if stack and stack[-1] >= arrival_speed:
                continue
            
            print(arrival_speed)
            stack.append(arrival_speed)
        
        return len(stack)