# Getting data from textboxes
from pyscript import display, document


def get_name(e):
    document.getElementById('div1').innerHTML = ' '

    # Variables
    f_name = document.getElementById('fname').value.title().strip()
    l_name = document.getElementById('lname').value.title().strip()
    member_full_name = ["Lucian Veran", "Pocholo Comanda", "Juan Piansay", "Daphne Mariano", "Shiloh Briones", "Juan Miguel Velarde"]
    full_name = f_name + " " + l_name

    # True(1) or False(0)
    name_check1 = full_name in member_full_name
    
    # Message to be displayed
    display_message = ('Sorry, you\'re not in our club!', f'Congratulations, {f_name + " " + l_name}! Welcome to the club!')

    # Display result based on name_check result
    display(display_message[name_check1], target="div1")
