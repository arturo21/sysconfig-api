import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from flask import Flask,session,url_for,request
from flask import abort,render_template,make_response,redirect, jsonify
from flask_login import current_user
import mysql.connector

api = Flask(__name__)
#gets de Módulo CMS
@api.route("/getAllUsers",methods=['GET'])
def getAllUsers():
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM usuarios")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/getUser/<iduser>",methods=['GET'])
def getUser(iduser):
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM usuarios WHERE ID='" + iduser + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/getAllPerfiles",methods=['GET'])
def getAllPerfiles():
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM perfiles")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/getPerfil/<idperfil>",methods=['GET'])
def getPerfil(idperfil):
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM perfiles WHERE ID='" + iduser + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/getAllPerfilesAsignados",methods=['GET'])
def getAllPerfilesAsignados():
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM perfilesasignados")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/getPerfilAsignado/<idperfil>",methods=['GET'])
def getPerfilAsignado(idperfil):
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM perfilesasignados WHERE ID='" + idperfil + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/getAllNotif",methods=['GET'])
def getAllNotif():
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM notificaciones")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/getNotif/<idnotif>",methods=['GET'])
def getNotif(idnotif):
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM notificaciones WHERE ID='" + idnotif + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

@api.route("/getAllPosts",methods=['GET'])
def getAllPosts():
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM notificaciones")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

#getPost aplica para post y página
@api.route("/getPost/<idpost>",methods=['GET'])
def getPost(idpost):
    mydb = mysql.connector.connect(host="localhost",user="arturo",password="Arat5uro",database="sysconfig")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM notificaciones WHERE ID='" + idpost + "'")
    myresult = mycursor.fetchall()
    return jsonify(myresult)

#método post Módulo CMS
