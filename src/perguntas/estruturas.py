from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Node:
    value: str
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def insert_left(self, value: str) -> 'Node':
        self.left = Node(value)
        return self.left

    def insert_right(self, value: str) -> 'Node':
        self.right = Node(value)
        return self.right


def dfs_path(root: Optional[Node], target: str) -> Optional[List[str]]:
  
    path: List[str] = []

    def _dfs(node: Optional[Node]) -> bool:
        if not node:
            return False
        path.append(node.value)
        if node.value == target:
            return True
        if _dfs(node.left):
            return True
        if _dfs(node.right):
            return True
        path.pop()
        return False

    found = _dfs(root)
    return path if found else None


