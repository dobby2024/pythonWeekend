'''
파일명 : BinaryTree.py

트리 자료구조
    단 하나의 루트 노드가 있고, 루트 노드에서 하위 노드들이
    연결된 비선형 계층구조이다.

이진트리(Binary Tree)
    모든 노드가 최대 2개의 자식 노드를 가질 수 있는 구조를 말한다.

    예)
    왼쪽 서브 트리의 값은 루트의 값보다 작고, 오른쪽 서브트리의 값은 루트보다
    큰 값을 가지도록 구성한다.

'''

# 이진 트리의 각 노드를 정의하는 클래스
class TreeNode:
    def __init__(self, value):
        self.value = value  # 노드의 값
        self.left = None    # 왼쪽 서브트리 루트 노드
        self.right = None   # 오른쪽 서브트리 루트 노드

# 이진 트리를 생성하고 순회, 탐색, 삽입 삭제하는 클래스
class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)  # 이진 트리의 루트 노드

    # 삽입 메소드: 이진 탐색을 사용하여 새 노드를 삽입합니다.
    # 삽입할 값(value)를 매개변수로 전달받습니다.
    def insert(self, value):
        # 이진 트리에 루트 노드가 없는 경우 새 노드를 루트 노드로 설정합니다.
        if not self.root:
            self.root = TreeNode(value)
        # 루트 노드가 있는 경우 _insert 메소드를 호출하여 삽입을 수행합니다.
        else:
            self._insert(value, self.root)

    # _insert 메소드: 재귀적으로 이진 탐색을 수행하며 삽입합니다.
    # 삽입할 값(value)과 현재 노드(current_node)를 매개변수로 전달받습니다.
    def _insert(self, value, current_node):
        # 삽입할 값이 현재 노드의 값보다 작은 경우
        if value < current_node.value:
            if not current_node.left:
                current_node.left = TreeNode(value)
            # 왼쪽 자식 노드가 있는 경우,. 왼쪽 자식노드를 기준으로 재귀적으로 삽입을
            # 수행합니다.
            else:
                self._insert(value, current_node.left)









