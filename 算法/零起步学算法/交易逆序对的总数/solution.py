class Solution:
    def reversePairs(self, record: List[int]) -> int:
        def merge_sort(l, r):
            # 终止条件
            if l >= r: return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = record[l:r + 1]
            for k in range(l, r + 1):
                if i == m + 1:
                    record[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    record[k] = tmp[i]
                    i += 1
                else:
                    record[k] = tmp[j]
                    j += 1
                    res += m - i + 1 # 统计逆序对
            return res
        
        tmp = [0] * len(record)
        return merge_sort(0, len(record) - 1)