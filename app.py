from flask import Flask, render_template


app = Flask('Blog')





def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
