class Solution:
    def isHappy(self, n: int) -> bool:
        #Initilize a set to store the visited numbers
        #while loop 
            #Check weather the num is in set
                #if it is present, return False
            #convert the number to string
            #caluculate the square of each number and add it
            #if it equal's to 1, return True

        seen = set()
        while n:
            if n in seen:
                return False
            seen.add(n)
            num_array = [int(num)**2 for num in str(n)]
            n_sum = sum(num_array)
            if n_sum == 1:
                return True
            n=n_sum
