from shutil import get_terminal_size

def justify_space_between(left, right):
    width = get_terminal_size().columns
    space = width - len(left) - len(right)
    
    if space < 1:
        print(f"{left} {right}")  # fallback si trop long
    else:            
        print(f"{left}{' ' * (space - 1)}{right}")