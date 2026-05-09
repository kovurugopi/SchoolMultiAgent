from google.adk.agents.llm_agent import Agent


def calculator(expression: str) -> str:
    """Evaluate a mathematical expression and return the result.

    Args:
        expression: A mathematical expression to evaluate (e.g. '2 + 2', '3 * (4 + 5)', 'pow(2, 10)').

    Returns:
        The result of the calculation as a string.
    """
    import math

    allowed_names = {
        "abs": abs, "round": round, "min": min, "max": max,
        "pow": pow, "sum": sum,
        "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "pi": math.pi, "e": math.e,
    }
    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"


maths_teacher_agent = Agent(
    model='gemini-2.0-flash',
    name='maths_teacher_agent',
    description='A specialized agent that helps with mathematics.',
    instruction='You are an expert maths teacher. Help the user with arithmetic, algebra, geometry, calculus, and problem solving. Use the calculator tool to compute mathematical expressions when needed.',
    tools=[calculator],
)
