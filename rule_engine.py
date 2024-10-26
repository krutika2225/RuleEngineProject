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

def create_rule(rule_string):
    # Validate input type
    if not isinstance(rule_string, str):
        raise ValueError("The rule_string must be a string.")

    if not rule_string:
        raise ValueError("The rule_string cannot be empty.")
    
    # Split rules based on AND/OR
    tokens = rule_string.replace('(', ' ( ').replace(')', ' ) ').split()
    return parse_expression(tokens)

def parse_expression(tokens):
    if not tokens:
        return None
    
    token = tokens.pop(0)
    
    if token == '(':
        left = parse_expression(tokens)
        operator = tokens.pop(0)
        right = parse_expression(tokens)
        tokens.pop(0)  # Remove ')'
        return RuleNode(operator, left, right)
    else:
        # Return a RuleNode with the full condition for comparison
        condition = token
        # Check if there's a comparison operator and grab the next token
        if len(tokens) > 0 and tokens[0] in ['>', '<', '==']:
            operator = tokens.pop(0)
            right_operand = tokens.pop(0)  # This should be the value to compare
            condition = f"{condition} {operator} {right_operand}"
        return RuleNode(condition)

def combine_rules(rules):
    if not rules:
        return None
    
    # Combine rules using OR logic (or modify based on requirements)
    root = None
    for rule in rules:
        if root is None:
            root = create_rule(rule)
        else:
            root = RuleNode('OR', root, create_rule(rule))
    
    return root

def evaluate(node, user_data):
    if node is None:
        return False
    
    # Evaluate conditions
    if '>' in node.condition:
        left_operand, right_operand = node.condition.split('>')
        left_operand = left_operand.strip()
        right_operand = float(right_operand.strip())
        return user_data.get(left_operand, 0) > right_operand

    elif '<' in node.condition:
        left_operand, right_operand = node.condition.split('<')
        left_operand = left_operand.strip()
        right_operand = float(right_operand.strip())
        return user_data.get(left_operand, 0) < right_operand

    elif '==' in node.condition:
        left_operand, right_operand = node.condition.split('==')
        left_operand = left_operand.strip()
        right_operand = right_operand.strip().strip("'")  # Strip quotes if present
        return user_data.get(left_operand, '') == right_operand

    # Logic operations
    if node.condition == 'AND':
        return evaluate(node.left, user_data) and evaluate(node.right, user_data)
    elif node.condition == 'OR':
        return evaluate(node.left, user_data) or evaluate(node.right, user_data)
    
    return False
