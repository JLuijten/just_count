import click

import just_count.square as square


@click.command()
@click.option(
    "-n",
    "--number",
    default=5,
    help="number to square.",
    show_default=True,
)
def main(number):
    print(f"The square of {number} is {square.square(number)}")


if __name__ == "__main__":
    main()
