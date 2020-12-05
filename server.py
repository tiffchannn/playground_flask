from flask import Flask, render_template
app = Flask(__name__)

# renders 3 blue boxes
@app.route('/play')
def renderBoxes():
  print('this is from the renderBoxes function')
  return render_template('index.html', times = int(3))

# render x times the number of blue boxes
@app.route('/play/<int:times>')
def multipleBoxes(times):
  print("*"*70)
  print('this is from multipleBoxes function')
  return render_template('index.html', times = int(times))

@app.route('/play/<int:times>/<color>')
def showColoredBoxesXtimes(times, color):
  print("*"*70)
  print('this is from showColoredBoxesXtimes function')
  myContainer = f'<div class="clrBox" style="background: {color};"> </div>'
  myContainer *= times
  return render_template('index.html', times = times, color=color)

if __name__ == "__main__":
    app.run(debug = True)