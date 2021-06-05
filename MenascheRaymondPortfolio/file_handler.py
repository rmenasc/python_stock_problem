"""
   File: solo_exc.py
   Author: Raymond Menasche
   Purpose: Demonstrates file handling examples.
"""
import os

class FileHandler:
    def __init__(this, file):
        this.file = file
        this.create_file()

    # Creates if it does not exists
    def create_file(this):
        try:
            create_file = open(this.file, 'x')
            print(f"File: { this.file } has been created and it is ready to be used!")
            create_file.close()
        except:
            print(f"File: { this.file } does exists and it is ready to be used!")

    # Opens a file to write
    def write_to_file(this, line):
        try:
            write_file = open(this.file, 'w')
            write_file.write(f"{ line }\n")
            write_file.close()
        except:
            print("Error, file not found")

    #Opens a file to append
    def append_file(this, line):
        try:
            append_file = open(this.file, 'a')
            append_file.write(f"{ line }\n")
            append_file.close()
        except:
            print("Error, file not found")

    # Opens a file to read
    def read_file(this):
        try:
            read_file = open(this.file, 'r')
            lines = list()
            for line in read_file:
                lines.append(line)
            read_file.close()
            return lines
        except FileNotFoundError:
            print("Error, file not found")


    # Deletes the file
    def delete_file(this):
        try:
            os.remove(this.file)
        except FileNotFoundError:
            print("Error, no such file")
            

