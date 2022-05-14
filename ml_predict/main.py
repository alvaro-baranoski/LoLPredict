import h2o

h2o.init()

model = h2o.import_mojo("ml_predict\model")

data = h2o.import_file("D:\Alvaro\Estudos\LoLPredict\match_data.csv")

prediction = model.predict(data)

print(prediction)