# leetcode
## Day 1
### 两数之和：
1。 考虑两层嵌套循环  
2。 用dictionary以及 enumerate 函数
```
def twoSum1(self, nums: List[int], target: int) -> List[int]:
    dct ={}
    for index, number in enumerate(nums):
        cp = target-number
        if cp in dct:
            return [dct[cp],index]
        else:
            dct[number] = index

```

### 删除排序数组中的重复项
双指针问题: 首先注意数组是有序的，那么重复的元素一定会相邻。
要求删除重复元素，实际上就是将不重复的元素移到数组的左侧。
考虑用 2 个指针，一个在前记作 p，一个在后记作 q，算法流程如下：
比较 p 和 q 位置的元素是否相等。
如果相等，q 后移 1 位
如果不相等，将 q 位置的元素复制到 p+1 位置上，p 后移一位，q 后移 1 位
重复上述过程，直到 q 等于数组长度。
返回 p + 1，即为新数组长度。

```
def removeDuplicates(self, nums: List[int]) -> int:
    a = 0
    b = 1
    while b < len(nums):
        if nums[a] == nums[b]:
            b = b + 1
        else:
            a = a + 1
            nums[a]=nums[b]
    return a+1

```

## Day 2

