#importa la libreria de flask
from flask import Flask, render_template, request, flash, session, redirect, url_for, escape
from flask_login import LoginManager, login_user, logout_user, login_required
import os
import sqlite3

from werkzeug.security import generate_password_hash, check_password_hash
from sqlite3 import Error
from form import Registro,Inicio, IniSesion,logout
from datetime import timedelta, datetime
app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=5)


#Registro de nuevos usuarios
@app.route('/Registro',methods=['POST','GET'])
def Usuarios():      
 frm = Registro()
 if request.method=="POST":  
   name =  frm.nombre.data
   username = frm.username.data
   password =frm.contrasena.data
   correo =frm.correo.data
   empresa =frm.empresa.data   
 
            # Conecta a la BD
   with sqlite3.connect("energy.db") as con:
      cursor = con.cursor()  # Manipular la BD
                # Prepara la sentencia SQL 

      cursor.execute("SELECT usuario FROM users WHERE usuario= ? ",[username])
      con.commit()
      comp=cursor.fetchone()
      if comp:
       flash("Este usuario ya existe, por favor intenta con otro")
       return redirect('/Registro')
     
      else:   
       cursor.execute("INSERT INTO users (usuario,nombre, password,correo,empresa) VALUES(?,?,?,?,?)", [
                            username,name, password, correo, empresa])
                # Ejecuta la sentencia SQL
      con.commit()
    
      return redirect('/')#cambiar a donde se redirige
 else:
   return render_template('Registro.html',frm=frm)

#inicio de sesion
  
@app.route('/',methods=['POST','GET'])
def Sesion():
 frm = IniSesion()
  
 if request.method=="POST":  
   
   username = frm.username.data
   password = frm.contrasena.data
    
            # Conecta a la BD
   with sqlite3.connect("energy.db") as con:
     cursor = con.cursor()  # Manipular la BD
                # Prepara la sentencia SQL 
     cursor.row_factory= sqlite3.Row
     cursor.execute("SELECT usuario,password FROM users WHERE usuario= ? AND password = ?",[username,password])
     data=cursor.fetchone() 
     
     
     
     if data :
       session["username"]=data["usuario"]
       session["password"]=data["password"]
       session.permanent = True
       global now 
       now = datetime.now() # current date and time
       global date_time 
       date_time= now.strftime("%d/%m/%Y, %H:%M:%S")  

       return redirect('/home')#cambiar a donde se redirige
     else:
       
      flash("El nombre de usuario y la contraseña no concuerdan")
      return redirect('/')



 else:
   return render_template('inicio_sesion.html',frm=frm)

@app.route('/home',methods=['POST','GET'])
def home():
  
  if "username" in session:
       
       frm = logout()
       if request.method=="POST": 
        out =datetime.now()
        date_time_out= out.strftime("%d/%m/%Y, %H:%M:%S")

        with sqlite3.connect("energy.db") as con:
         cursor = con.cursor()  # Manipular la BD
                # Prepara la sentencia SQL 
         cursor.row_factory= sqlite3.Row
         cursor.execute("SELECT empresa FROM users WHERE usuario= ? ",[session["username"]])
         emp=cursor.fetchone();        
         comp=emp["empresa"]                             
         cursor.execute("INSERT INTO loggin (user,company,act_time,time_out) VALUES (?,?,?,?)",[session["username"],comp,date_time,date_time_out])
                # Ejecuta la sentencia SQL
         con.commit()   
        return redirect('/')  
       else:
         return   render_template('index.html',frm=frm)
  else:
    return "you are no login"