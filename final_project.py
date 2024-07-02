'''
file management Application.
'''
import os
def create_file(filename):
    try:
        with open(filename,'x')as f:
            print(f"file name{filename}:created successfully!")
    except FileExistsError:
        print(f'file name {filename} already existed!')
    except Exception as e:
        print('an error occured!')
def view_all_files():
    files= os.listdir()
    if not files:
        print('not files found')
    else:
        print('files in directory')
        for file in files:
            print(file)
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been delete successfully!')
    except FileNotFoundError:
        print('file not found')
    except Exception as e:
        print('An error occurred')
def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"content of '{filename}' :\n{content}")

    except FileNotFoundError:
        print(f"{filename}does not exist!")
    except Exception as e:
        print('An error occurred!')
def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content = input('enter data to add =')
            f.write(content +"\n")
            print(f'Content added to "{filename}" successfully')
    except FileNotFoundError:
        print(f"file'{filename}'does not exist")
    except Exception as e:
        print('An error occurred!')
def main():
    while True:
        print("file management App")
        print('1: creat file')
        print('2: view all file')
        print('3: delete file')
        print('4: read file')
        print('5: edit file')
        print('6: exit file')

        choice =input('enter your choice (1-6)=::-')
        if choice =="1":
            filename=input("enter the file-name to create =")
            create_file(filename)
        elif choice =="2":
            view_all_files()
        elif choice =="3":
            filename = input("enter the name of file that you want to delete")
            delete_file(filename)
        elif choice =="4":
            filename = input("enter the name of file that you want to read")
            read_file(filename)
        elif choice =="5":
            filename = input("enter the name of file that you want to edit")
            edit_file(filename)
        elif choice=="6":
            print("closing the App....")
            break
        else:
            print("invelid syntex")

if __name__ == "__main__":
    main()

            












