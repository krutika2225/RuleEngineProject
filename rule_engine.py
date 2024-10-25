class RuleNode:
    def __init__(self, condition, left=None, right=None):
        """
        Initialize a rule node with a condition and optional left and right children.
        condition: a string representing the condition (e.g., 'age > 18')
        left, right: child nodes (for combining conditions with AND/OR)
        """
        self.condition = condition
        self.left = left
        self.right = right

def evaluate(node, user_data):
    if node is None:
        return False
    
    # Base cases for evaluation:
    if node.condition == 'age > 18':
        return user_data.get('age', 0) > 18
    elif node.condition == 'income > 30000':
        return user_data.get('income', 0) > 30000
    elif node.condition == 'department == Engineering':
        return user_data.get('department', '') == 'Engineering'
    
    # Logic operations
    if node.condition == 'AND':
        return evaluate(node.left, user_data) and evaluate(node.right, user_data)
    elif node.condition == 'OR':
        return evaluate(node.left, user_data) or evaluate(node.right, user_data)
    
    return False


# Example usage
if __name__ == "__main__":
    # Get user input
    user_data = {
        'age': int(input("Enter age: ")),
        'income': int(input("Enter income: ")),
        'department': input("Enter department: ")
    }
    
    # Constructing the AST for the rule: age > 18 AND income > 30000 AND department == Engineering
    root = RuleNode('AND', 
                    RuleNode('AND', 
                              RuleNode('age > 18'), 
                              RuleNode('income > 30000')), 
                    RuleNode('department == Engineering'))
    
    # Evaluating eligibility
    eligibility = evaluate(root, user_data)
    print("User eligibility:", "Eligible" if eligibility else "Not Eligible")