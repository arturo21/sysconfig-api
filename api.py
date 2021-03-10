import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from flask import Flask,session,url_for,request
from flask import abort,render_template,make_response,redirect,jsonify
from flask_login import current_user
from datetime import date
import mysql.connector
from hashlib import sha256,sha512
import json
import secrets

#Leer archivo de configuración en JSON###############
with open('config.json', 'r') as file:
    config = json.load(file)
database_host = config['DEFAULT']['DB_HOST']
database_name = config['DEFAULT']['DB_NAME']
database_user = config['DEFAULT']['DB_USER']
database_password = config['DEFAULT']['DB_PASSWORD']
######################################################
api = Flask(__name__)
#################################################################################################################################################################
#######################################################################################################GENERATE API KEYS#####################################################
#################################################################################################################################################################
@api.route("/api/genAPIKey",methods=['GET'])
def genAPIKey():
    generated_key = secrets.token_urlsafe(512)
    return jsonify({'apiKEY':generated_key})

@api.route("/api/genSecretKey",methods=['GET'])
def genSecretKey():
    generated_key = secrets.token_urlsafe(512)
    return jsonify({'SecretKEY':generated_key})
#gets de Módulo CMS
@api.route("/api/getConn",methods=['GET'])
def getConn():
    cnx = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    return jsonify(cnx.is_connected())

@api.route("/api/getAllUsers",methods=['GET'])
def getAllUsers():
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM usuarios")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/api/getUser/<iduser>",methods=['GET'])
def getUser(iduser):
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM usuarios WHERE ID='" + iduser + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/api/getAllPerfiles",methods=['GET'])
def getAllPerfiles():
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM perfiles")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/api/getPerfil/<idperfil>",methods=['GET'])
def getPerfil(idperfil):
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM perfiles WHERE ID='" + idperfil + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/api/getAllPerfilesAsignados",methods=['GET'])
def getAllPerfilesAsignados():
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM perfilesasignados")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/api/getPerfilAsignado/<idperfil>",methods=['GET'])
def getPerfilAsignado(idperfil):
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM perfilesasignados WHERE ID='" + idperfil + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/api/getAllNotif",methods=['GET'])
def getAllNotif():
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM notificaciones")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/api/getNotif/<idnotif>",methods=['GET'])
def getNotif(idnotif):
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM notificaciones WHERE ID='" + idnotif + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/api/getAllPosts",methods=['GET'])
def getAllPosts():
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM posts")
    myresult = mycursor.fetchall()
    return jsonify(myresult)
#getPost aplica para post y página
@api.route("/api/getPost/<idpost>",methods=['GET'])
def getPost(idpost):
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM posts WHERE ID='" + idpost + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)
#################################################################################################################################################################
#método post Módulo CMS
@api.route("/api/savePost",methods=['POST'])
def savePost():
	req = request.form
	today = date.today()
	mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
	mycursor = mydb.cursor()
	sql="INSERT INTO posts (titulo, descripcion, tipo, imagenref, autor, timestamp) VALUES (%s, %s,%s, %s,%s, %s)"
	val=(req.titulo,req.descripcion,'post',req.imagenref,current_user.id,today)
	mycursor.execute(sql, val)
	mydb.commit()
	return 0

@api.route("/api/savePage",methods=['POST'])
def savePage():
	req = request.form
	today = date.today()
	mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
	mycursor = mydb.cursor()
	sql="INSERT INTO posts (titulo, descripcion, tipo, imagenref, autor, timestamp) VALUES (%s, %s,%s, %s,%s, %s)"
	val=(req.titulo,req.descripcion,'page',req.imagenref,current_user.id,today)
	mycursor.execute(sql, val)
	mydb.commit()
	return 0

@api.route("/api/saveCategory",methods=['POST'])
def saveCategory():
	req = request.form
	today = date.today()
	mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
	mycursor = mydb.cursor()
	sql="INSERT INTO categorias(categoria, descripcion, autor) VALUES (%s, %s,%s)"
	val=(req.titulo,req.descripcion,req.imagenref)
	mycursor.execute(sql, val)
	mydb.commit()
	return jsonify(myresult)

@api.route("/api/saveTag",methods=['POST'])
def saveTag():
	req = request.form
	today = date.today()
	mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
	mycursor = mydb.cursor()
	sql="INSERT INTO etiquetas(etiqueta, descripcion, autor) VALUES (%s, %s,%s)"
	val=(req.titulo,req.descripcion,req.imagenref)
	mycursor.execute(sql, val)
	mydb.commit()
	return jsonify(myresult)

@api.route("/api/savePost",methods=['POST'])
def clonePost():
	req = request.form
	today = date.today()
	mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
	mycursor = mydb.cursor()
	sql="INSERT INTO posts (titulo, descripcion, tipo, imagenref, autor, timestamp) VALUES (%s, %s,%s, %s,%s, %s)"
	val=(req.titulo,req.descripcion,req.tipo,req.imagenref,'admin',today)
	mycursor.execute(sql, val)
	mydb.commit()
	return 0

@api.route("/api/savePage",methods=['POST'])
def clonePage():
	mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
	mycursor = mydb.cursor()
	sql="INSERT INTO customers (name, address) VALUES (%s, %s)"
	val=("John", "Highway 21")
	mycursor.execute(sql, val)
	mydb.commit()
	return 0

@api.route("/api/saveCategory",methods=['POST'])
def cloneCategory():
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM notificaciones WHERE ID='" + idpost + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/api/saveTag",methods=['POST'])
def cloneTag():
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM notificaciones WHERE ID='" + idpost + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

#################################################################################################################################################################
#Login and Register Sistem
@api.route("/api/LoginUser",methods=['POST'])
def LoginUser():
    username = request.json.get('username')
    password = request.json.get('password')
    clavefinal=sha256(str(password).encode('utf-8'))
    mydb = mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    sql="SELECT * FROM usuarios WHERE usuario='" + username + "' AND clave='" + clavefinal.hexdigest() + "'";
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    if(myresult):
        return jsonify(myresult)
    else:
        return "NO\n"

@api.route("/api/registerUser",methods=['POST'])
def registerUser():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')

    mydb =mysql.connector.connect(host=database_host,user=database_user,password=database_password,database=database_name)
    mycursor = mydb.cursor()
    if(len(username)!=0):
        if(len(email)!=0):
            if(len(nombre)!=0):
                if(len(apellido)!=0):
                    if(len(password)!=0):
                        clavefinal=sha256(str(password).encode('utf-8'))
                        print(clavefinal)
                        sql="INSERT INTO usuarios (usuario, email, nombre, apellido, clave) VALUES (%s, %s,%s, %s,%s)"
                        val=(username,email,nombre,apellido,clavefinal.hexdigest())
                        try:
                            mycursor.execute(sql, val)
                            mydb.commit()
                            return jsonify({"response":"OK"})
                        except mysql.connector.Error as err:
                            return jsonify({"response":err})
