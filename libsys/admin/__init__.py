from flask import Blueprint

admin = Blueprint('admin', 
                  __name__, 
                  static_folder='static',
                  template_folder='template')