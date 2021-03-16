def countSubstring(Str, n) : 
    ans = 0; 
  
    atm = 0; 
  
    while (atm < n) : 
        cnt0 = 0; cnt1 = 0; 
  
        if (Str[atm] == '0') : 
  
            while (atm < n and Str[atm] == '0') : 
                cnt0 += 1; 
                atm += 1; 
  
            jump = atm; 
            while (jump < n and Str[jump] == '1') : 
                cnt1 += 1; 
                jump += 1; 
        else : 
            while (atm < n and Str[atm] == '1') : 
                cnt1 += 1; 
                atm += 1; 
  
            jump = atm; 
  
            while (jump < n and Str[jump] == '0') : 
                cnt0 += 1; 
                jump += 1; 
  
        ans += min(cnt0, cnt1); 
    return ans; 
  
#next 
if __name__ == "__main__" : 
    Str = "0001110010"; 
    n = len(Str); 
    print(countSubstring(Str, n));
