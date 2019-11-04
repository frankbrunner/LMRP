
	
"""Webservice"""
mcp = Flask(__name__)

@mcp.route('/')	
def index():
	return(render_template("start.html", name="this ist Frank"))

@mcp.route('/initiate')
def initiate():
	return(render_template("test.html", name="this ist Frank"))
		
@mcp.route('/move')
def move():
	if request.args.get("function") == "forward":
		moveRobot.forward()
	if request.args.get("function") == "right":
		moveRobot.turn("right")
	if request.args.get("function") == "left":
		moveRobot.turn("left")
	if request.args.get("function") == "backward":
		moveRobot.backward()
	if request.args.get("function") == "stop":
		moveRobot.stop()
	"""render Template"""
	return(render_template("move.html", name="this ist Frank"))

if __name__=='__main__':
	print("has been starting")
	mcp.run(debug=True, host = '0.0.0.0')
	


