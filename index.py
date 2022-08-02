from flask import Flask
from main import data_bp,country_name,urbanData,ruralData,developmentRatio,urbanised_dataByYear,rural_dataByYear
from main import data_by_year,countrydataBy_date,predictions
app = Flask(__name__)



app.register_blueprint(data_bp)
app.register_blueprint(country_name)
app.register_blueprint(urbanData)
app.register_blueprint(ruralData)
app.register_blueprint(developmentRatio)
app.register_blueprint(urbanised_dataByYear)
app.register_blueprint(rural_dataByYear)
app.register_blueprint(data_by_year)

app.register_blueprint(countrydataBy_date)
app.register_blueprint(predictions)


@app.route('/',methods=['GET','POST'])
def home():
    return {'response':"app working fine!"}

def appRun(): 
  if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=105)
  else:
      app.logger.error('This is an ERROR message')

appRun()
