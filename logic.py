import ast
import operator

def evaluate_expression(expression):
    """
    Evaluates a mathematical expression string safely.
    Supports +, -, *, /, %, ^ (power), parentheses.
    """
    # Remove whitespace
    expression = expression.replace(" ", "")
    
    # Check for empty input
    if not expression:
        return ""

    try:
        # Use ast.literal_eval for basic safety, but it's limited
        # For a full calculator, we might need a custom parser or carefully used eval()
        # Given the "trending" request, a robust eval with sanitization is often preferred for complexity.
        # Let's use a safe evaluation approach with ast.
        
        # ast.literal_eval is too restrictive for math expressions (doesn't support operators).
        # So we will build a simple safe evaluator using ast.
        node = ast.parse(expression, mode='eval')
        return _eval(node.body)
    except Exception as e:
        return "Error"

_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def _eval(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        op = _operators[type(node.op)]
        return op(_eval(node.left), _eval(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        op = _operators[type(node.op)]
        return op(_eval(node.operand))
    else:
        raise TypeError(node)
