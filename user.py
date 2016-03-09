#-------------------------------------------------------------------------------
# Name:        user
# Purpose:
#
# Author:      Jeremy Nelson
#
# Created:     2014/08/18
# Copyright:   (c) Jeremy Nelson 2014
# Licence:     MIT
#-------------------------------------------------------------------------------
from flask.ext.login import make_secure_token, UserMixin

class User(UserMixin):

    def __init__(self, id, iri, active=True, **kwargs):
        self.id = id
        self.iri = iri
        self.active = active

    def is_active(self):
        return self.active

    def get_id(self):
        return self.id

    def get_auth_token(self):
        return make_secure_token(self.iri,
                                 key='deterministic')

class Admin(User):

    def is_admin(self):
        return True







def main():
    pass

if __name__ == '__main__':
    main()
