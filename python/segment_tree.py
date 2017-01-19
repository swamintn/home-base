#!/usr/bin/python env

from __future__ import print_function

from math import floor, ceil, log
from operator import add

class SegmentTree(object):
    """
    A Segment Tree
    
    1) n represents the number of leaf nodes
    2) A segment tree is a full balanced binary tree. So, the number of internal
       nodes is n-1 and the height is ceil(log n).

    operation specifies the operation to perform for computing internal nodes.
    For sum of values in a range, use add. For range minimum queries, use min.
    Others can also be used.

    See: http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
         http://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/
    """
    ALLOWED_OPERATIONS = [add, min, max]
    NULL_VALUES = {add: 0, min: float("inf"), max: -float("inf")}

    def __init__(self, in_arr, operation=add):
        self.in_arr = in_arr
        self.op = operation
        self.construct_ST(in_arr)

    def _construct_ST_util(self, arr, start, end, tree_node):
        """
        Recursive function for constructing Segment Tree
        start and end represent positions in input array, arr and tree_node
        represents the position in the tree_arr

        Computes and returns the value at self.tree_arr[tree_node]
        """
        if start == end:
            self.tree_arr[tree_node] = arr[start]
            return self.tree_arr[tree_node]
        mid = start + ((end - start) // 2)
        new_val = self.op(
                      self._construct_ST_util(arr, start, mid, 2*tree_node + 1),
                      self._construct_ST_util(arr, mid+1, end, 2*tree_node + 2))
        self.tree_arr[tree_node] = new_val
        return self.tree_arr[tree_node]

    def construct_ST(self, in_arr):
        """
        Construct Segment Tree from an input array

        The actual tree is stored in a tree_arr, an array implementation of a 
        tree
        """
        self.n      = len(in_arr)
        # Height is max. number of edges from root to some leaf
        # Number of levels in the tree is height + 1
        tree_ht     = int(ceil(log(self.n, 2)))
        tree_arr_sz = 2**(tree_ht+1) - 1
        self.tree_arr = [None for _ in xrange(tree_arr_sz)]
        self._construct_ST_util(in_arr, 0, self.n - 1, 0)

    def _update_ST_util(self, start, end, pos, tree_node):
        """Recursive implementation for updating a value"""
        """
        ALTERNATE IMPLEMENTATION THAT WORKS ONLY FOR SUM, assuming we are 
        initially given a diff between new_val and old_val for in_arr[pos]
        # if pos is outside this node's range, nothing to do
        if pos < start or pos > end:
            return
        # diff is new_value - old_value
        self.tree_arr[tree_node] += diff
        # if non-leaf node, recurse and update in sub_trees as well
        if start != end:
            mid = start + ((end - start) // 2)
            self._update_ST_util(start, mid, pos, diff, 2*tree_node + 1)
            self._update_ST_util(mid+1, end, pos, diff, 2*tree_node + 2)
        """
        # if pos is outside this node's range, nothing to update
        if pos < start or pos > end:
            return self.tree_arr[tree_node]
        if start == end:
            self.tree_arr[tree_node] = arr[pos]
            return self.tree_arr[tree_node]
        mid = start + ((end - start) // 2)
        new_val = self.op(
                      self._update_ST_util(start, mid, pos, 2*tree_node + 1),
                      self._update_ST_util(mid+1, end, pos, 2*tree_node + 2))
        self.tree_arr[tree_node] = new_val
        return self.tree_arr[tree_node]

    def update_ST(self, pos, new_val):
        """Updates a value in the input array and in the Segment tree"""
        self.in_arr[pos] = new_val
        self._update_ST_util(0, self.n - 1, pos, 0)

    def _calc_range_util(self, seg_start, seg_end, qs, qe, tree_node):
        """
        seg_start and seg_end represent the range covered by this tree_node
        qs and qe represent the query range we want

        If segment of this node is part of given range, return the sum value
        If segment of this node is outside the given range, return 0
        Else, recurse to the left and right sub-trees

        """
        if qs <= seg_start and qe >= seg_end:
            return self.tree_arr[tree_node]
        if qe < seg_start or qs > seg_end:
            return self.NULL_VALUES[self.op]
        mid = seg_start + ((seg_end - seg_start) // 2)
        return self.op(
                 self._calc_range_util(seg_start, mid, qs, qe, 2*tree_node + 1),
                 self._calc_range_util(mid+1, seg_end, qs, qe, 2*tree_node + 2))

    def calc_range(self, start, end):
        """
        Get the sum for the specified range, start and end inclusive
        """
        return self._calc_range_util(0, self.n - 1, start, end, 0)


if __name__ == '__main__':
    print("Testing segment tree")
    arr = [1,3,5,7,9,11]
    s = SegmentTree(arr, operation=min)
    print("Array", s.in_arr)
    print("SegmentTree", s.tree_arr)
    print("Range(1,4)", s.calc_range(1, 4))
    print("Updating node 1 from 3 to 5")
    s.update_ST(1, 5)
    print("Array", s.in_arr)
    print("SegmentTree", s.tree_arr)
    print("Range(1,4)", s.calc_range(1, 4))
    print("Updating node 1 from 5 to -5")
    s.update_ST(1, -5)
    print("Array", s.in_arr)
    print("SegmentTree", s.tree_arr)
    print("Range(1,4)", s.calc_range(1, 4))
