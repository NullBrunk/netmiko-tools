from termcolor import colored

def general_logger(message: str, bold: bool, symbol: str, color: str, end = '\n'):
    print(
        colored(f"[{symbol}]", color, attrs=["bold"]),
        colored(message, "white", attrs=["bold"] if bold else None),
        end=end
    )

def info(message: str, bold: bool = False, end = '\n'):
    general_logger(message, bold, "*", "cyan", end)

def error(message: str, bold: bool = False, end = '\n'):
    general_logger(message, bold, "!", "yellow", end)

def success(message: str, bold: bool = False, end = '\n'):
    general_logger(message, bold, "+", "green", end)

def presentation(message: str):
    print(
        colored(">", "blue", attrs=["bold"]), 
        colored(message, "white", attrs=["bold"])
    )
