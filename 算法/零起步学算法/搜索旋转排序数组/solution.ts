function search(nums: number[], target: number): number {
    let index = searchMinIndex(nums);
    let frontNums = nums.slice(index)
    let behindNums = nums.slice(0, index)
    let originNums = [...frontNums, ...behindNums];
    let left = 0;
    let right = originNums.length - 1;
    while (left < right) {
        let mid = Math.floor((left + right) / 2);
        if (originNums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    if (originNums[left] === target) {
        if (left + index >= nums.length) {
            return left + index - nums.length;
        } else {
            return left + index;
        }

    }
    return -1;
};

function searchMinIndex(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        const mid = Math.floor((right + left) / 2);
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
};
