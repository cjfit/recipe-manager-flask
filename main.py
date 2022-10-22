from recipe import Recipe
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxxxdemo'

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/list_dishes')
def list_dishes():
    return render_template('recipes.html', recipes=get_dishes())


@app.route('/add_dish', methods=["POST", "GET"])
def add_dish():
    if request.method == "GET":
        return render_template('add_recipe.html')
    if request.method == "POST":
        Recipe(request.form['text'])
        flash(request.form['text'] + " added!")
        return render_template('index.html')


@app.route("/edit/<dish>", methods =["GET"])
def update_dish(dish):
    Recipe.remove_dish(dish)
    flash(dish + " deleted!")
    return render_template('index.html')


def get_dishes():
    return [str(dish) for dish in Recipe.dishes]

if __name__ == "__main__":
    main()


