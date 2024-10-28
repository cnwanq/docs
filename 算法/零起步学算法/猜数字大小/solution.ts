/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

var guess = function(num) {
    if (num > 2) return -1;
    else if (num < 2) return 1;
    return 0;
};

function guessNumber(n: number): number {
    let left = 1;
    let right = n;
    while (left <= right) {
        const mid = Math.floor((right - left) / 2 + left);
        if (guess(mid) === 0) return mid;
        else if (guess(mid) < 0) right = mid - 1;
        else left = mid + 1;
    }
    return -1;
};