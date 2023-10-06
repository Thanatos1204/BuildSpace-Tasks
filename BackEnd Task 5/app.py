from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/search")
def search():
  query = request.args.get("query")

  # Define the hard-coded responses for specific keywords
  responses = {
    "Flask": "A micro web framework written in Python.",
    "Django": "A Python web framework that encourages rapid development and clean, pragmatic design.",
    "Web.py": "A lightweight Python web framework."
  }

  # Get the response for the given query
  response = responses.get(query, "No results found.")

  # Render the search results template
  return render_template("search.html", query=query, response=response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 