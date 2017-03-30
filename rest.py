from bottle import run, get, post, request, delete
import pymysql

conn = pymysql.connect('localhost','username','password','Webshop')
a = conn.cursor()



animals = [
    {'name': 'Calle', 'type': 'Tiger'},
    {'name': 'Waleed', 'type': 'Katt'},
    {'name': 'Magnus', 'type': 'Orm'}
]

@get('/animals')
def getAllAnimals():
    sql = "SELECT * FROM T_ANIMALS"
    a.execute(sql)
    print(a.fetchall())

    return {'animals': animals}

@get('/animals/<name>')
def getAnimalByName(name):
    the_animal = [animal for animal in animals if animal['name'] == name]
    return {'animal': the_animal[0]}

@post('/animal')
def addOne():
    new_animal = {'name': request.json.get('name'), 'type': request.json.get('type')}
    animals.append(new_animal)
    return {'animals': animals}

@delete('/animals/<name>')
def deleteOne(name):
    delete_animal = [animal for animal in animals if animal['name'] == name]
    animals.remove(delete_animal[0])
    return {'animals': animals}


run(reloader=True, debug=True)
