impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let len = nums.len();
        if len == 0 {
            return vec![-1, -1];
        }
        
        let first = Self::search_first_position(&nums, target);
        let last = Self::search_last_position(&nums, target);
        return vec![first, last];
    }

    fn search_first_position(nums: &Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len() as i32 - 1;
        while left <= right {
            let mid = left + (right - left) / 2;
            if nums[mid as usize] == target && (mid == 0 || nums[mid as usize - 1] < target) {
                return mid;
            } else if nums[mid as usize] < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    fn search_last_position(nums: &Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len() as i32 - 1;
        while left <= right {
            let mid = left + (right - left) / 2;
            if nums[mid as usize] == target
                && (mid == nums.len() as i32 - 1 || nums[mid as usize + 1] > target)
            {
                return mid;
            } else if nums[mid as usize] > target {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }
}
