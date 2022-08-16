
def calculate_area(name):


    name = name.lower()

    # check for the conditions
    if name == "rectangle":
        l = int(input("Enter rectangle's length: "))
        b = int(input("Enter rectangle's breadth: "))
        
        # calculate area of rectangle
        rect_area = l * b
        print(f"The area of rectangle is{rect_area}.")



    elif name == "circle":
        r = int(input("Enter circle's radius length: "))
        pi = 3.14
            
        # calculate area of circle
        circ_area = pi * r * r
        print(f"The area of circle is{circ_area}.")
            

        
    else:
        print("Sorry! This shape is not available")

    # driver code
    if __name__ == "__main__" :

     print("Calculate Shape Area")
    shape_name = input("Enter the name of shape whose area you want to find: ")

   
    calculate_area(shape_name)
