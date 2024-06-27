class CustomMenu:
    def __init__(self, name="Menu", choices: list=["Yes", "No"]):
        self.choices_dict = {}
        for index, choice in enumerate(choices):
            self.choices_dict[str(index+1)] = choice
        self.name = name

    def __str__(self):
        max_length = self.max_length_needed()

        # Add Top
        length_needed = max_length - len(f"~~~ {self.name} ~~~")
        result = ("~" * int(length_needed/2)) + f"~~~ {self.name} ~~~" + ("~" * int(length_needed/2))

        # Add Choices
        for index, choice in self.choices_dict.items():
            length_needed = max_length - len(f" -{choice}  [{index}]")
            result += f"\n -{choice}  " + (" " * length_needed) + f"[{index}]"

        # Add Bottom
        result += "\n" + "~" * max_length

        return result

    def max_length_needed(self):
        max_length = len(f"~~~ {self.name} ~~~")
        for index, choice in self.choices_dict.items():
            length = len(f" -{choice}  [{index}]")
            if length > max_length:
                max_length = length
        
        # If self.name is even, make max_length even
        if len(self.name) % 2 == 0:
            if max_length % 2 != 0:
                max_length += 1
        # If self.name is odd, make max_length odd
        else:
            if max_length % 2 == 0:
                max_length += 1
        return max_length

    def ask(self):
        print(self)
        choice_index = input("Enter Option: ")
        print()
        if choice_index not in self.choices_dict:
            return None
        return self.choices_dict[choice_index]
