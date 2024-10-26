class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left
        self.right = right
        self.value = value

def create_rule(rule_string):
    try:
        # Basic example of parsing the rule string into a Node (this will depend on your parsing logic)
        # For simplicity, assume the rule string is valid
        return Node(type="operand", value=rule_string)
    except Exception as e:
        print(f"Error creating rule: {e}")

def combine_rules(rules):
    combined_ast = None
    for rule in rules:
        node = create_rule(rule)  # Convert each rule string to AST
        if combined_ast is None:
            combined_ast = node
        else:
            # Combine with OR for simplicity
            combined_ast = Node(type="operator", value="OR", left=combined_ast, right=node)
    return combined_ast

def evaluate_rule(ast, data):
    # Simple evaluation based on the node type
    if ast.type == "operand":
        # Assume the rule can be evaluated directly (implement your logic)
        return eval(ast.value, {}, data)  # This is dangerous; better to parse the rule properly
    elif ast.type == "operator":
        left_eval = evaluate_rule(ast.left, data)
        right_eval = evaluate_rule(ast.right, data)
        if ast.value == "OR":
            return left_eval or right_eval
        elif ast.value == "AND":
            return left_eval and right_eval
    return False

def save_rules(rules):
    import json
    with open('rules.json', 'w') as f:
        json.dump(rules, f)

def load_rules():
    import json
    try:
        with open('rules.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return empty list if no file exists

if __name__ == "__main__":
    # Example usage
    rules = ["age > 18", "income > 30000"]
    combined_ast = combine_rules(rules)
    data = {"age": 20, "income": 35000}
    print(evaluate_rule(combined_ast, data))  # Output: True
