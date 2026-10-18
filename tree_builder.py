class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if current_node is None:
            current_node = self.root

        if current_node is None:
            print(f"❌ No team lead exists yet. Add a team lead first.")
            return

        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                else:
                    print(f"❌ {manager_name} already has someone on the LEFT.")
            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                else:
                    print(f"❌ {manager_name} already has someone on the RIGHT.")
            else:
                print(f"❌ '{side}' is not a valid side. Choose LEFT or RIGHT.")
            return

        found = False
        if current_node.left is not None:
            if self._contains(current_node.left, manager_name):
                self.insert(manager_name, employee_name, side, current_node.left)
                found = True
        if not found and current_node.right is not None:
            if self._contains(current_node.right, manager_name):
                self.insert(manager_name, employee_name, side, current_node.right)
                found = True

        if not found and current_node is self.root:
            print(f"❌ Manager '{manager_name}' not found in the team structure.")

    def _contains(self, node, name):
        if node is None:
            return False
        if node.name == name:
            return True
        return self._contains(node.left, name) or self._contains(node.right, name)

    def print_tree(self, node=None, level=0):
        if node is None and level == 0:
            node = self.root
        if node is None:
            return

        print("  " * level + f"- {node.name}")
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here
company_directory_test = TeamTree()
company_directory_test.root = EmployeeNode("Jordan")
company_directory_test.insert("Jordan", "Taylor", "right")
company_directory_test.insert("Jordan", "Riley", "left")
company_directory_test.insert("Riley", "Dana", "right")
company_directory_test.insert("Riley", "Morgan", "left")
company_directory_test.print_tree()


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    company_directory()