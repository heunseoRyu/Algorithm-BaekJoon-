#음계
def ascend(nums):
    for i in range(7):
        if nums[i] != nums[i+1]-1:
            return False
    else:
        return True

def descend(nums):
    for i in range(7):
        if nums[i] != nums[i+1]+1:
            return False
    else:
        return True

nums = list(map(int,input().split()))
if ascend(nums):
    print("ascending")
elif descend(nums):
    print("descending")
else:
    print("mixed")