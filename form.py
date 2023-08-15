from tkinter import E
from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired

class Inicio(FlaskForm):
    nombre=StringField('nombre', validators=[DataRequired(message='No dejar vacio, completar')])
    username=StringField('username', validators=[DataRequired(message='No dejar vacio, completar')])
    contrasena = PasswordField('contrasena',validators=[DataRequired(message='No dejar vacio, completar')])
    correo = EmailField('correo',validators=[DataRequired(message='No dejar vacio, completar')])
    empresa = StringField('empresa',validators=[DataRequired(message='No dejar vacio, completar')])
    crear = SubmitField("Crear")  

class Registro(FlaskForm):
    nombre=StringField('nombre', validators=[DataRequired(message='No dejar vacio, completar')])
    username=StringField('username', validators=[DataRequired(message='No dejar vacio, completar')])
    contrasena = PasswordField('contrasena',validators=[DataRequired(message='No dejar vacio, completar')])
    correo = EmailField('correo',validators=[DataRequired(message='No dejar vacio, completar')])
    empresa = StringField('empresa',validators=[DataRequired(message='No dejar vacio, completar')])
    crear = SubmitField("Crear")  

class IniSesion(FlaskForm):
   username=StringField('username', validators=[DataRequired(message='No dejar vacio, completar')]) 
   contrasena = PasswordField('contrasena',validators=[DataRequired(message='No dejar vacio, completar')])
   entrar = SubmitField("entrar") 

class logout(FlaskForm):
    logout = SubmitField("salir")   
    