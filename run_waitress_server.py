import sys, os  
from waitress import serve  
sys.path.insert(0, './app')
from app import APP

serve(APP,host="0.0.0.0",port=os.environ["PORT"])  
#serve(APP,host="localhost",port="5000")  
#APP.run(debug=True)