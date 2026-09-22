def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    return f"The flavor of chai is {flavor}."

print(chai_flavor.__doc__)
print(chai_flavor.__name__)

# help(len)

def generate_bil (chai = 0, samosa = 0):
    """
    Calculate the total bill for chai and samosa.

    :param chai: The number of cups of chai(10 rupees each).
    :param samosa: The number of samosas(20 rupees each).
    :return: (total amount, Thank you message as a string)
    """

    total = (chai * 10) + (samosa * 20)
    return total, "Thank you for your purchase!"