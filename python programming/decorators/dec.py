#######################################
# HTML Text generator
#######################################

def html_tag(tag):
    
    def wrap_text(text):
        print(f"<{tag}>{text}</{tag}>")
        
    return wrap_text

if __name__ == "__main__":
    # creating a function that will return heading in h1 tag
    h1_wrapper = html_tag("h1")
    # in context, h1_wrapper is a function and below is its defnition
    # def wrap_text(text):
    #   print(f"<h1>{text}<\h1>")
    h1_wrapper("Heading..")
    
    p_wrapper = html_tag("p")
    p_wrapper("This is body text..")