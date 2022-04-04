from dec_caltime import time_dec

@time_dec
def leet_code_344(s):
    l = len(s)
    
    #0.0166646 - size 3000
    # for i in range(0, int(l/2)):
    #     s[i], s[l-1-i] = s[l-1-i], s[i]
    
    #0.0145738 - size 3000
    # s=s[::-1]
    
    #0.016303699999999997 - Size 3000
    #inbuilt function of lists
    # s.reverse()
    
    #0.0003944
    #increases memeory usage
    #sometimes can hit "maximum recursion depth exceeded in comparison" error
    def recur_str(left, right, s):
        if left < right:
            s[left], s[right] = s[right], s[left]
            recur_str(left+1, right-1, s)
    recur_str(0, len(s)-1, s)   
    
    print(s)


if __name__ == "__main__":
    #size = 3000
    input_str = "ravitejaw"
    leet_code_344(list(input_str))