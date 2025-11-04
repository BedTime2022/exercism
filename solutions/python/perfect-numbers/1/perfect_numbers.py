def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1 and isinstance(number,int):
        raise ValueError("Classification is only possible for positive integers.")
    else:
        count = -number
        for i in range(1,number+1):
           if number % i == 0:
               count = count + i 
        if count == number:
            return "perfect"
        elif count > number:
            return "abundant"
        else:
            return "deficient"
        
        