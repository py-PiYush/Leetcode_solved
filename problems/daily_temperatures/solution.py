class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer
        
        
        
        ''' Monotonic stack'''
        st = []
        ans = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]]<temperatures[i]:
                last_idx = st.pop()
                ans[last_idx] = i - last_idx
            st.append(i)
        return ans
        
        
        ''' Brute Force'''
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    ans[i] = j - i
                    break
        return ans