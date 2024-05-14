from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
  if request.method == 'POST':
    return redirect(url_for('test'))
  return render_template('main.html')

@app.route('/test')
def test():
  return 'This is New Page!'

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)