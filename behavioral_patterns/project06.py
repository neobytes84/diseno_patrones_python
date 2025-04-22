# Behavioral patterns - Mediator in Python -example 02
# Developed by Neobytes.io

import pandas as pd
import datetime
import csv

class Chat(object):
    def display_message(self, user, message):
        print(f'{user}: {message}')
    
    def display_notification(self, user, message):
        print(f'Notification: {user}: {message}')
    
    def display_user_connected(self, user):
        print(f'{user} has connected')
    
    def login_user(self, user, password):
        if self.verify_credentials(user, password):
            self.display_user_connected(user)
        else:
            self.display_message(user, 'Invalid credentials')

class Mediator(Chat):
    def __init__(self):
        self.users = {}
        self.chat_logs = []
        self.notification_logs = []
        self.message_logs = []
        self.connection_logs = []
        self.login_logs = []
    
    def add_user(self, user, password):
        if user not in self.users:
            self.users[user] = password
            self.display_message(user, 'User added successfully')
        else:
            self.display_message(user, 'User already exists')
            self.display_message(user, 'Please try a different username')
            self.display_message(user, 'Or login with your existing credentials')
            self.display_message(user, 'To add a new user, please contact the system administrator')
            self.display_message(user, 'For more information, please visit our website at www.neobytes.io')
            self.display_message(user, 'Thank you for your cooperation')
    
    def remove_user(self, user):
        if user in self.users:
            del self.users[user]
            self.display_message(user, 'User removed successfully')
        else:
            self.display_message(user, 'User does not exist')
            self.display_message(user, 'Please try a different username')
            self.display_message(user, 'Or login with your existing credentials')
    
    def verify_credentials(self, user, password):
        return user in self.users and self.users[user] == password
    
    def send_message(self, sender, recipient, message):
        if recipient in self.users:
            self.message_logs.append((sender, recipient, message, datetime.datetime.now()))
            self.display_message(sender, f'Message sent to {recipient}: {message}')
        else:
            self.display_message(sender, f'User {recipient} does not exist')
    
    def send_notification(self, sender, recipient, message):
        if recipient in self.users:
            self.notification_logs.append((sender, recipient, message, datetime.datetime.now()))
            self.display_notification(sender, f'Notification sent to {recipient}: {message}')
        else:
            self.display_message(sender, f'User {recipient} does not exist')
            self.display_message(sender, 'Please try a different recipient')
            self.display_message(sender, 'Or contact the system administrator')
    
    def logout_user(self, user):
        if user in self.users:
            self.display_user_connected(user)
            self.display_message(user, 'User logged out successfully')
        else:
            self.display_message(user, 'User does not exist')
            self.display_message(user, 'Please try a different username')
            self.display_message(user, 'Or login with your existing credentials')
            self.display_message(user, 'To log out, please contact the system administrator')
    def save_logs_to_csv(self):
        with open('chat_logs.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Sender', 'Recipient', 'Message', 'Timestamp'])
            writer.writerows(self.message_logs)
        
        with open('notification_logs.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Sender', 'Recipient', 'Message', 'Timestamp'])
            writer.writerows(self.notification_logs)
        
        self.display_message('System', 'Chat logs saved to chat_logs.csv and notification_logs.csv')
    
    def display_all_users(self):
        self.display_message('System', 'All users:')
        for user in self.users:
            self.display_message('System', f'- {user}')
            self.display_message('System', f'  - Password: {self.users[user]}')
            self.display_message('System', '---')
# Example usage

mediator = Mediator()

mediator.add_user('user1', 'password1')
mediator.add_user('user2', 'password2')
mediator.add_user('user3', 'password3')

mediator.login_user('user1', 'password1')

mediator.send_message('user1', 'user2', 'Hello, user2!')

mediator.logout_user('user1')

mediator.login_user('user2', 'password2')

mediator.send_notification('user2', 'user1', 'Hello, user1! This is a notification.')

mediator.send_message('user2', 'user3', 'Hello, user3!')

# Save chat logs to CSV file

mediator.save_logs_to_csv()

# Display all users

mediator.display_all_users()