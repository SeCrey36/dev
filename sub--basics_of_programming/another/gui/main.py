# import gui
import backend as bk




def main():
    """main"""
    main_thread = bk.Main()
    data = main_thread.load_json()
    info = ('plane1', 20,10,10,10,10,10)
    #main_thread.add_airplane(data, info)
    #main_thread.select_airplane()
    #main_thread.plane_info()


if __name__ == '__main__':
    main()
