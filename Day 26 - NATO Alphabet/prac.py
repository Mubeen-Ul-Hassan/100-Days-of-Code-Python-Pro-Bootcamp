# def main():
#     health = 10
#     armor = 5
#     add_armor(health, armor)


# def add_armor(health, armor):
#     new_health = health + armor
#     print_health(new_health)

# def print_health(new_health):
#     print(f"The player now has {new_health} health.")


# main()

# ?

# Don't touch below this line

READ = 1
WRITE = 2
DELETE = 4
ADMIN = 8
SHARE = 16
DOWNLOAD = 32


class User:
    """
    Each permission --> represented by a single power of 2
    Combine --> use bitwiser OR 
    Check --> use bitwise AND
    Remove --> use bitwise AND with NOT 
    Stored as --> one integer containing multiple ON/OFF bits
    """
    def __init__(self, username):
        self.username = username
        self.permissions = 0

    def grant_permission(self, perm):
        self.permissions |= perm

    def revoke_permission(self, perm):
        self.permissions &= ~perm
    
    def has_permission(self, perm):
        self.permission &= perm

    def show_permission(self):
        print(f"Username: {self.username}")
        if self.permissions & READ: print("READ")
        if self.permissions & WRITE: print("WRITE")
        if self.permissions & DELETE: print("DELETE")
        if self.permissions & ADMIN: print("ADMIN")
        if self.permissions & SHARE: print("SHARE")
        if self.permissions & DOWNLOAD: print("DOWNLOAD")
        if self.permissions == 0: print("None");


user = User("Mubeen")
user.grant_permission(READ)
user.grant_permission(WRITE)
user.grant_permission(DELETE)
user.show_permission()