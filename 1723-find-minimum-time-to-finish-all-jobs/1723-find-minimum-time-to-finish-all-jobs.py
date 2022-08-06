class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        left = max(jobs)
        jobs.sort(reverse=True)
        total = sum(jobs)
        right = total
        n = len(jobs)
        
        def condition(target,bucket,index):
            nonlocal n,k
            # we need to find if we can divide jobs in k subseq qith max subseq sum <= time
            if index == n:
                return True
            for i in range(k):
                bucket[i] += jobs[index]
                if bucket[i] <= target and condition(target,bucket,index + 1):
                    return True
                
                bucket[i] -= jobs[index]
                
                if bucket[i] == 0:
                    break
            return False
        
        while left < right:
            mid = left + (right - left) // 2
            bucket = [0] *k
            if condition(mid,bucket,0):
                right = mid
            else:
                left = mid + 1
            
        return left
        