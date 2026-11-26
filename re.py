def open_box():
    global count
    count -= 1
    print("count:", count)
    if count == 0:
        return
    open_box()
    print("The box is open., count:", count)


count = 10
open_box()