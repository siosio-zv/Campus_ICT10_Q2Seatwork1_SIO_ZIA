from pyscript import document

club_members = ["Brixen Rabacca", "Zyren Naguit", "Miko Alvis", "Kristoff Dotado"]

result_messages = {
    True: "Congratulations {name}! You are now part of the ICT club.",
    False: "Sorry {name}, your name is not on the list."
}

result_styles = {
    True: "alert alert-success",
    False: "alert alert-danger"
}


def get_full_name():
    """Get the first and last name from the inputs and combine them."""
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    return f"{first_name} {last_name}".title()


def check_membership(full_name):
    """Return True if the full name is in the club members list."""
    return full_name in club_members


def show_result(full_name, is_member):
    """Display the message and color in the result area."""
    result = document.getElementById("result")
    result.className = result_styles[is_member]
    result.innerHTML = result_messages[is_member].format(name=full_name)


def clear_inputs():
    """Empty both input fields."""
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""


def verify_candidate(e):
    """Respond to the click: get the name, check it, show the result."""
    full_name = get_full_name()
    is_member = check_membership(full_name)  # stored result of the check

    show_result(full_name, is_member)
    clear_inputs()
