from flask import Flask, render_template, request, redirect, flash, url_for, session, Response
from forms import LoginForm
import bcrypt
import json
import time
import sys
import os
from termcolor import colored
import sqlite3

# Instancia de objeto Flask
app = Flask(__name__)

# Configuración de llave secreta
app.secret_key='SICSI_SESSION'
app.config['SESSION_PERMANENT'] = False

# Forms
login_form = LoginForm()



@app.route('/')
def main():
    print(colored('Main','green'))
    if 'username' in session:
        return render_template('index.html')
    else:
        return render_template('login.html',form=login_form)

# Función con sesión iniciada
@app.route('/index')
def index():
    print('Index')
    if 'username' in session:
        print(colored('Sesión activa','green'))
        return render_template('index.html')
    else:
        print(colored('Sesión inactiva','yellow'))
        return render_template('login.html',form=login_form)

# Función para iniciar sesión
@app.route('/plataforma', methods=['GET','POST'])
def plataforma():
    form = LoginForm(request.form)
    if(request.method == 'GET'):
        print('plataforma GET. Redirigiendo a main()')
        return redirect(url_for('main'))
    else:
        print('Login POST')
        if form.validate():
            # validación de form de login
            print(colored('Login validado pero no verificado','yellow'))
            # Obtención de datos
            user = request.form['login_user']
            password = request.form['login_password']
            password_encoded = password.encode('utf-8')
            print('User: ',user)
            print('Password: ',password)
            # Proceso de consulta a BDD
            # Cursor y conector sqlite3
            db_connector = sqlite3.connect('contacts_monitor.db')
            db_cursor = db_connector.cursor()
            # Query para consultas
            sQuery = "SELECT id,username,password_hash FROM users where username = '%s'" %user
            #Ejecución de sentencia
            db_cursor.execute(sQuery)
            #Obtención del dato
            usuario = db_cursor.fetchone()
            #Cerrar cursor 
            db_cursor.close()
            #Verificar que se obtuvieron datos
            if(usuario != None):
                # Obtiene password encriptado y codificado 
                hash = usuario[2]
                hash_encoded = hash.encode('utf-8')
                print('Password codificado: ',password_encoded)
                print('Password codificado y cifrado: ',hash_encoded)
                # Verifica el password
                if(bcrypt.checkpw(password_encoded,hash_encoded)):
                    print(colored('Contraseña correcta','green'))
                    #Registra la sesión
                    session['user'] = usuario[1]
                    session.permanent = False
                    #redirige a index
                    return render_template('index.html')
                else:
                    print(colored('Contraseña incorrecta','red'))
                    flash("Contraseña incorrecta","alert-warning")
                    return render_template('login.html',form=login_form)
            else:
                print(colored('El usuario no existe','red'))
                flash("El usuario no existe","alert-warning")
                return render_template('login.html',form=login_form)
        else:
            print(colored('Login no validado y no verificado','red'))
            flash("Verificar datos de sesión","alert-warning")
            return render_template('login.html',form=login_form)


@app.route('/logout')
def logout():
    print('Limpiando sesión mediante logout')
    # Limpia sesiones
    session.clear()
    # Redirige
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)