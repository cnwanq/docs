function searchRange(nums: number[], target: number): number[] {
    let size = nums.length;
    if (size == 0) return [-1, -1];

    let first = searchFirstPosition(nums, target);
    let last = searchLastPosition(nums, target);

    return [first, last];
};

function searchFirstPosition(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);
        if (nums[mid] == target && (mid == 0 || nums[mid - 1] < target)) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

function searchLastPosition(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);
        if (nums[mid] == target && (mid == nums.length - 1 || nums[mid + 1] > target)) {
            return mid;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}
