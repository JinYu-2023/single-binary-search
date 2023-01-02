# -*- coding = utf-8 -*-
# @CreateTime : 2022/12/30 15:23
# @Author : 20866
# @Project: Pycharm
# @File : binary_search.py
# @Software : PyCharm
# @InterpreterLocation : !C:\Windows.old\Users\20866\AppData\Local\Programs\Python\Python310\python.exe
# @Site : https://gitee.com/qiongjulingjun


# 二分查找 左闭右闭

# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
# 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def main() -> int:
    nums = [1, 5, 6, 9, 18, 20, 30, 36, 40, 45]
    if binary_search(nums, 20) != -1:
        print('search successfully! ', 20, ' offset: ', binary_search(nums, 20))
        print('OK好')
    else:
        print('can not find! ', 20, ' ', binary_search(nums, 20))

    if binary_search(nums, 100) != -1:
        print('search successfully! ', 100, ' offset: ', binary_search(nums, 100))
    else:
        print('can not find! ', 100, ' ', binary_search(nums, 100))
        print('OK好')
    return 0


if __name__ == "__main__":
    main()

# END
