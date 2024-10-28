impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut left, mut right) = (1, nums.len());
        let first = nums[0];

        while left < right {
            let mid = left + (right - left) / 2;
            match (nums[mid] < first, nums[mid] < nums[mid - 1]) {
                (true, true) => {
                    left = mid;
                    break;
                }
                (true, false) => right = mid,
                _ => left = mid + 1,
            }
        }

        fn binary_search(nums: &[i32], target: i32) -> i32 {
            let (mut left, mut right) = (0, nums.len());
            while left < right {
                let mid = left + (right - left) / 2;
                if nums[mid] == target {
                    return mid as i32;
                } else if nums[mid] > target {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            -1
        }
        let (big, small) = nums.split_at(left);
        if target == first {
            return 0;
        }
        if target > first {
            // 查大
            return binary_search(big, target);
        } else {
            // 查小
            let ans = binary_search(small, target);
            if ans == -1 {
                return -1;
            } else {
                return left as i32 + ans;
            }
        }
    }
}