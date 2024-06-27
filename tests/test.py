from ..CustomMenuAPI import CustomMenu

def test():
    custom_menu = CustomMenu(name="You ____ Custom Menu!", choices=["Love", "Like"])
    response = custom_menu.ask()
    print(f"You {response} It!")

# Main Code
if __name__ == "__main__":
    test()
