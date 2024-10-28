你可以将一个数组 arr 称为 山脉数组 当且仅当：

arr.length >= 3
存在一些 0 < i < arr.length - 1 的 i 使得：
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
给定一个山脉数组 mountainArr ，返回 最小 的 index 使得 mountainArr.get(index) == target。如果不存在这样的 index，返回 -1 。

你无法直接访问山脉数组。你只能使用 MountainArray 接口来访问数组：

MountainArray.get(k) 返回数组中下标为 k 的元素（从 0 开始）。
MountainArray.length() 返回数组的长度。
调用 MountainArray.get 超过 100 次的提交会被判定为错误答案。此外，任何试图绕过在线评测的解决方案都将导致取消资格。

 

示例 1：

输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
示例 2：

输入：array = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。
