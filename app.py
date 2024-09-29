from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("Welcome", 
        H1("Hello World!"),
        P("Welcome to my GitHub Pages site powered by FastHTML.")
    )

if __name__ == "__main__":
    serve()