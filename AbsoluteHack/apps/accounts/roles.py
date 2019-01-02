from rolepermissions.roles import AbstractUserRole
from . import permissions as p

class SuperUser(AbstractUserRole):
    available_permissions = {
        p.READ_USERS = True
        p.EDIT_USERS = True
        p.DELETE_USERS = True
        p.SUSPEND_USERS = True
    }

    display_name = 'SuperUser'


class NormalUser(AbstractUserRole):
    available_permissions = {

    }
    display_name = 'NormalUser'
