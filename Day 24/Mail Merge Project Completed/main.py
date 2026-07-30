from pathlib import Path

PLACEHOLDER = "[name]"
base_dir = Path(__file__).resolve().parent

with open(base_dir / "Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open(base_dir / "Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

output_dir = base_dir / "Output/ReadyToSend"
output_dir.mkdir(exist_ok=True)

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    with open(output_dir / f"letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)

