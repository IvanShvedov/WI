from flask import Flask, render_template, request, redirect, url_for
import logging
import configparser

from storage import SQLiteStorage
from repos import InviteService

app = Flask(__name__, static_folder='static')

config = configparser.ConfigParser()
config.read('config.ini')

logger = logging.getLogger('main')
logging.basicConfig(
    filename='example.log', 
    level=logging.INFO,
    format="%(asctime)s %(name)s:%(levelname)s:%(message)s", 
    datefmt="%F %A %T"
)


storage = SQLiteStorage(config['Storage']['url'])
storage._up('up.sql')

invite_service = InviteService(storage)


@app.get('/admin')
def admin():
    invite_list = invite_service.get_list()
    return render_template('admin.html', invite_list=invite_list)
        
        
@app.post('/addguest')
def add():
    invite_service.create(request.form)
    return redirect(url_for('admin'))
   
   
@app.get('/guests/<invite_id>')
def show_invite(invite_id):
    invite = invite_service.get_invite(invite_id)[0]
    return render_template('invite.html', invite=invite)
    
   
@app.post('/guest/<invite_id>')
def delete_guest(invite_id):
    invite_service.delete(invite_id)
    return redirect(url_for('admin'))
   
@app.post('/invite/<invite_id>')
def invite_guest(invite_id):
    invite_service.invite(invite_id)
    return redirect(url_for('show_invite', invite_id=invite_id))
    
