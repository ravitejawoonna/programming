#https://medium.com/@punitkmr/contains-duplicates-i-74f28bf315f0

def containsDuplicate(nums):
        ref_dict = {}
        
        for num in nums:
            if str(num) in ref_dict and ref_dict[str(num)] == 1:
                return True
            
            else:
                ref_dict[str(num)] = 1
                
                
        return False
    
if __name__ == "__main__":
    l = [1,2,3,1]
    print(containsDuplicate(l))