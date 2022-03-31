def circle_formula(r, name):
    # free variable
    pi = 3.14
    c_name = name
    
    def get_area():
        return f"Area of cirle {c_name} is {str(pi * r * r)}"

    def get_circumf():
        return f"Circum of cirlce {c_name} is {str(2 * pi * r)}"
    
    def diameter_len():
        return 2 * r
    
    return (get_area, get_circumf, diameter_len())

if __name__ == "__main__":
    c1 = circle_formula(4, "c1")
    c2 = circle_formula(8, "c2")
    
    print(c1)
    print(c2)
    
    print(c1[0]())
    print(c2[0]())
    
    print(c1[1]())
    print(c2[1]())
    
    # this returns a value rather than a function
    print(c1[2])
    print(c2[2])