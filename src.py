def countSubstring(Str, n) : 
  
    # To store the total count 
    # of substrings 
    ans = 0; 
  
    ideaOne = 0; 
  
    # Traversing the string 
    while (ideaOne < n) : 
  
        # Count of consecutive 
        # 0's & 1's 
        count0 = 0; count1 = 0; 
  
        # Counting subarrays of 
        # type "01" 
        if (Str[ideaOne] == '0') : 
  
            # Count the consecutive 
            # 0's 
            while (ideaOne < n and Str[ideaOne] == '0') : 
                count0 += 1; 
                ideaOne += 1; 
  
            # If consecutive 0's 
            # ends then check for 
            # consecutive 1's 
            jump = ideaOne; 
  
            # Counting consecutive 1's 
            while (jump < n and Str[jump] == '1') : 
                count1 += 1; 
                jump += 1; 
  
        # Counting subarrays of 
        # type "10" 
        else : 
  
            # Count consecutive 1's 
            while (ideaOne < n and Str[ideaOne] == '1') : 
                count1 += 1; 
                ideaOne += 1; 
  
            # If consecutive 1's 
            # ends then check for 
            # consecutive 0's 
            jump = ideaOne; 
  
            # Count consecutive 0's 
            while (jump < n and Str[jump] == '0') : 
                count0 += 1; 
                jump += 1; 
  
        # Update the total count 
        # of substrings with 
        # minimum of (count0, count1) 
        ans += min(count0, count1); 
  
    # Return answer 
    return ans; 
  
#next 
if __name__ == "__main__" : 
    Str = "0001110010"; 
    n = len(Str); 
  
    # Function to print the 
    # count of substrings 
    print(countSubstring(Str, n));
