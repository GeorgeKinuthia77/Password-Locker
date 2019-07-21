#!/usr/bin/env python3.6
from password import User
from password import Credentials
import random
from getpass import getpass


def create_user(username, account,password):
    '''
    Function to create a new user
    '''
    new_user = User(username, account,password)
    return new_user

def create_paswad(account, password):
    '''
    Function to create new password
    '''
    new_pass = Credentials(account, password)
    return new_pass

def save_user(user):
    '''
    Function to save users
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(account):
    '''
    Function that finds a user by account name and returns the  user
    '''
    return User.find_by_account(account)
def check_existing_user(account):
    '''
    Function that checks if a user exists with that account and returns Boolean
    '''
    return User.user_exists(account)

def display_users():
    '''
    Function that returns all saved users
    '''
    return User.display_users()

def save_paswad(credentials):
    '''
    Function that saves new password
    '''
    return credentials.save_password()

def generate_paswad():
    '''
    Function that generates a password for the user
    '''
    return Credentials.generatePassword()

def main():
    print("Hello! Welcome.Kindly sign up below")
    while True:
        access_name = input("Password Locker Username: ").lower()
        if access_name == '':
            print("Invalid username")
        else:
            access_pass = getpass("Password Locker sign up key:  ")
            print("Log in using your sign-up credentials")
            login_name = input("Log in with your username: ").lower()
            login_pass = getpass("Please enter registered password: ")
            if access_pass == login_pass:
                print('\n')
                print(f"Welcome back {access_name}. What would you like to do?")
                print('\n')

            else:
                print("Invalid username or password!")
