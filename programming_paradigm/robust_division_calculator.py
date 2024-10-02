def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        
        if denom == 0:
            return "Error: Division by zero is not allowed."
        
        result = num / denom
        return f"The result of dividing {num} by {denom} is {result}"
    
    except ValueError:
        return "Error: Non-numeric input. Please enter valid numbers."
