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
