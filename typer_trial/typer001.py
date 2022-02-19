import typer

obj = typer.Typer()

@obj.command()
def finder():
    print("Ener the comment below to print name")
    print("python3 typer001.py hello <Your name>")
    print("Ener the comment below to print age")
    print("python3 typer001.py how <Your age>")

@obj.command()
def hello(name : str):
    print(f"Hello {name}")

@obj.command()
def how(age : int):
    print(f"You are {age} year old")


if __name__ == "__main__":
    obj()
