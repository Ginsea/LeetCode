#!/usr/bin/env python
#coding=utf-8

class TwoNums(object):
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/two-sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def practice1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i_index1 = 0
        i_index2 = 0
        for i_index in range(len(nums)):
            i_subnum = nums[i_index]
            i_othernum = target - i_subnum
            if i_othernum in nums:
                i_otherindex = nums.index(i_othernum)
                if i_otherindex != i_index:
                    i_index1 = i_index
                    i_index2 = i_otherindex
                    break
        return [i_index1, i_index2]
    
    def practice2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i_index1 = 0
        i_index2 = 0
        for index, value in enumerate(nums):
            i_othervalue = target - value
            if i_othervalue in nums:
                i_otherindex = nums.index(i_othervalue)
                if index != i_otherindex:
                    i_index1 = index
                    i_index2 = i_otherindex
                    break
        return [i_index1, i_index2]

class ThreeNums(object):
    """
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/3sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def practice1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
