from termcolor import colored

def general_logger(message: str, bold: bool, symbol: str, color: str, start: str = '', end: str = '\n'):
    print(
        start + 
        colored(f"[{symbol}]", color, attrs=["bold"]),
        colored(message, "white", attrs=["bold"] if bold else None),
        end=end
    )

def info(message: str, bold: bool = False, start = '', end = '\n'):
    general_logger(message, bold, "*", "cyan", start, end)

def error(message: str, bold: bool = False, start = '', end = '\n'):
    general_logger(message, bold, "!", "yellow", start, end)

def success(message: str, bold: bool = False, start = '', end = '\n'):
    general_logger(message, bold, "+", "green", start, end)

def presentation(message: str):
    print(
        colored(">", "blue", attrs=["bold"]), 
        colored(message, "white", attrs=["bold"])
    )
