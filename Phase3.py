# -*- coding: utf-8 -*-
"""Phase 3: Optimization, Scaling, and Final Evaluation
"""

import time
import random
from functools import lru_cache

class TreeNode:
    """Node structure for AVL tree"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # For AVL balancing

class AVLTree:
    """Optimized Binary Search Tree using AVL balancing"""

    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        return y

    def _balance(self, node):
        """Ensures tree remains balanced after insertion"""
        if not node:
            return None

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert(self, node, key):
        """Recursive insertion while maintaining balance"""
        if not node:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        return self._balance(node)

    def insert(self, key):
        """Public method to insert a node"""
        self.root = self._insert(self.root, key)

    @lru_cache(maxsize=1000)
    def _search(self, node, key):
        """Optimized search using memoization"""
        if not node or node.key == key:
            return node is not None

        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search(self, key):
        """Public search method"""
        return self._search(self.root, key)

    def _inorder(self, node):
        """Inorder traversal using a generator for efficient memory usage"""
        if node:
            yield from self._inorder(node.left)
            yield node.key
            yield from self._inorder(node.right)

    def inorder(self):
        """Public inorder traversal"""
        return list(self._inorder(self.root))

# Performance testing and scaling
def generate_large_dataset(size=100000):
    """Generates a large dataset of random unique integers"""
    return random.sample(range(1, size * 10), size)

def test_performance():
    """Comprehensive performance testing"""
    tree = AVLTree()
    dataset = generate_large_dataset(50000)

    start_time = time.time()
    for num in dataset:
        tree.insert(num)
    insertion_time = time.time() - start_time

    search_sample = random.sample(dataset, 1000)
    start_time = time.time()
    for num in search_sample:
        tree.search(num)
    search_time = time.time() - start_time

    print(f"Insertion Time (50K elements): {insertion_time:.4f} sec")
    print(f"Search Time (1K elements): {search_time:.4f} sec")

# Run performance tests
if __name__ == "__main__":
    test_performance()