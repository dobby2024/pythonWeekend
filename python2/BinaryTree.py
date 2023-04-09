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
        # 삽입할 값이 현재 노드의 값보다 큰 경우
        elif value > current_node.value:
            # 오른쪽 자식 노드가 없으면 새 노드를 오른쪽 자식 노드로 설정합니다.
            if not current_node.right:
                current_node.right = TreeNode(value)
            # 오른쪽 자식 노드가 있는 경우, 오른쪽 자식 노드를 기준으로
            # 재귀적으로 삽입을 수행합니다.
            else:
                self._insert(value, current_node.right)
        else:
            print("이미 존재하는 값입니다.")

    # 전위 순회 메소드 : root -> left -> right
    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + ' ')   # root 노드의 값을 추가
            traversal = self.preorder_traversal(start.left, traversal)  # 왼쪽 서브트리 순회
            traversal = self.preorder_traversal(start.right, traversal) # 오른쪽 서브트리 순회
            print(traversal)
        return traversal
    
    # 중위 순회 메소드: left -> root -> right
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal) # 왼쪽 서브트리 순회
            traversal += (str(start.value)+ ' ') # root 노드의 값을 추가
            traversal = self.inorder_traversal(start.right, traversal) # 오른쪽 서브트리 순회
        return traversal

    # 후위 순회 메소드: left -> right -> root
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.preorder_traversal(start.left, traversal) # 왼쪽 서브트리 순회
            traversal = self.preorder_traversal(start.right, traversal) # 오른쪽 서브트리 순회
            traversal += (str(start.value) + ' ') # root 노드의 값을 추가
        return traversal


# 실행코드
# 이진 트리 객체를 생성합니다. 루트 노드의 값은 5입니다.
bt = BinaryTree(5)

# 값을 삽입합니다.
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

# 이진 트리를 전위 순회한 결과를 출력합니다.
print("전위 순회: ", bt.preorder_traversal(bt.root, ""))

# 이진 트리를 중위 순회한 결과를 출력합니다.
print("중위 순회: ", bt.inorder_traversal(bt.root, ""))

# 이진 트리를 후위 순회한 결과를 출력합니다.
print("후위 순회: ", bt.postorder_traversal(bt.root, ""))











