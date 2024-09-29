from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("Welcome", 
        H1("Hello World!"),
        P("Welcome to my website powered by FastHTML.")
    )

serve()