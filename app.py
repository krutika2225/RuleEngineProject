from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    data = request.json
    rule = data.get('rule')
    try:
        rule_node = create_rule(rule)
        return jsonify({'condition': rule_node.condition}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    data = request.json
    rules = data.get('rules', [])
    try:
        combined_rule_node = combine_rules(rules)
        return jsonify({'combined_condition': combined_rule_node.condition}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    data = request.json
    rule = data.get('rule')
    user_data = data.get('user_data')
    try:
        rule_node = create_rule(rule)
        eligibility = evaluate(rule_node, user_data)
        return jsonify({'result': 'Eligible' if eligibility else 'Not Eligible'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
