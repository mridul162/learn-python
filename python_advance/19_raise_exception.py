class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print("accident occurred, take detour.")

try:
    raise Accident('crash between two cars')
except Accident as e:
    e.handle()
    print(e)

######################################
# try:
#     raise MemoryError('memory error')  #python built-in exception
# except MemoryError as e:
#     print(e)

###################
# def process_file():
#     try:
#         f=open("C:\\code\\python_advance\\text.txt")
#         x=1/0
#     except FileNotFoundError as e:
#         print("inside except")
#     finally:
#         print("cleaning up the file")
#         f.close()
#
# process_file()