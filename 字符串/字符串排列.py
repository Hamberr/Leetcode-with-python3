
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
 
        size1 = len(s1)
        size2 = len(s2)
        
        c1 = collections.Counter(s1)
        c2 = collections.Counter()
        
        end = 0  #视窗末尾索引
        start = 0 #视窗起始索引
        len_same = 0  #统计出现数目相同的字符数，若其与s1中的字符类数（最多26）相同，则s1的某种排列是s2的一个子串
        
        while end < size2:
            #print(index_s2)
            c2[s2[end]] += 1
            if c2[s2[end]] == c1[s2[end]]:
                len_same += 1
            if len_same == len(c1):
                return True
                
            end += 1  #末尾索引推进
            
            if end - start + 1 > size1:
                if c2[s2[start]] == c1[s2[start]]:
                    len_same -= 1
                c2[s2[start]] -= 1
                
                if c2[s2[start]] == 0:
                    del c2[s2[start]]
                    
                start += 1 #起始索引推进
                    
        return False
