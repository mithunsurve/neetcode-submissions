class Solution:
    def binaryRow(self, top, bottom, matrix, target):
        if top>bottom:
            return None
        mid=(top+bottom)//2
        if matrix[mid][0]<=target<=matrix[mid][-1]:
            return matrix[mid]
        elif matrix[mid][0] < target:
            return self.binaryRow(mid+1, bottom, matrix, target)
        else:
            return self.binaryRow(top, mid-1, matrix, target)

    def binary(self, left, right, arr, target):
        if left> right:
            return False
        mid=(left+right)//2
        if arr[mid]==target:
            return True
        elif target > arr[mid]:
            return self.binary(mid+1, right, arr, target)
        else:
            return self.binary(left, right-1, arr, target)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=self.binaryRow(0, len(matrix)-1, matrix, target)
        if not row:
            return False
        return self.binary(0, len(row)-1, row, target)