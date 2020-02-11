## 最长上升子序列
定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

[通过动态规划，复杂度O(n**2)](https://github.com/Hamberr/Leetcode-with-python3/blob/master/LIS/300_Longest_Increasing_Subsequence_dp.py)
<br>
[通过二分查找改进，复杂度O(n*logn)](https://github.com/Hamberr/Leetcode-with-python3/blob/master/LIS/LIS_with_binarysearch.py)
<br>
以及基于LIS的[俄罗斯套娃信封问题](https://github.com/Hamberr/Leetcode-with-python3/blob/master/LIS/354_Russian_Doll_Envelopes.py)

## 字符串
### [字符串排列](https://github.com/Hamberr/Leetcode-with-python3/blob/master/%E5%AD%97%E7%AC%A6%E4%B8%B2/%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8E%92%E5%88%97.py)
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例：
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

若s1的某种排列是s2的一个子串，则s1的字母集合以及每个字母的出现次数与s2的某个字串完全相同，这个可以根据 __collections.Counter()__ 判断。
然后再用视窗推移的方法遍历。
