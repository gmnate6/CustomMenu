from CustomMenuAPI import CustomMenu

# Main Code
if __name__ == "__main__":
    custom_menu = CustomMenu(name="You ____ Custom Menu!", choices=["Love", "Like"])
    response = custom_menu.ask()
    print(f"You {response} It!")
