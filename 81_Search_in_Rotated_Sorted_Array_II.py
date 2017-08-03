
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    length = len(nums)
    if length == 0:
        return False
    s, e = 0, length - 1
    while s <= e:
        mid = (s + e) / 2
        if nums[mid] == target:
            return True
        if nums[s] < nums[mid]:
            if nums[s] <= target < nums[mid]:
                e = mid - 1
            else:
                s = mid + 1
        elif nums[mid] < nums[e]:
            if nums[mid] < target <= nums[e]:
                s = mid + 1
            else:
                e = mid - 1
        else:
            if (nums[s] == nums[mid] and nums[mid] != nums[e]):
                s = mid + 1
            elif (nums[mid] == nums[e] and nums[s] != nums[mid]):
                e = mid - 1
            else:
                s += 1
                e -= 1
    return False

test = [3,1,1]
print search(test, 3)