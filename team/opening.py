from tkinter import*
from tkinter import font

window = Tk()
window.title("영화위키!")
window.geometry("500x700+30+30")

state = 0

class SERVICE_GUI:

    def search():
        global frame_s
        global state
        state = 1

        frame_s = Frame(frame_op, width=500, height=700)
        frame_s.pack()

        TempFont = font.Font(frame_s, size = 15, weight = 'bold')

        mainlabel = Label(frame_s, font = TempFont, text="영화 이름을 입력하세요")
        mainlabel.place(x=150, y=50)

        inputentry = Entry(frame_s, width=24)
        inputentry.place(x=170, y=100)

        inputlabel = Button(frame_s, font = TempFont, width=7, height=1, text="입력")
        inputlabel.place(x=205, y=140)

        viewmovie = Text(frame_s, width=55, height=30, borderwidth=8)
        viewmovie.place(x=50, y=200)
        viewscroll = Scrollbar(frame_s)
        viewscroll.pack()
        viewscroll.place(x=480, y=200)

        back = Button(frame_s, text="뒤로", width=10, height=1, command=OP_MENU.op_menus)
        back.place(x=50, y= 650)
        exit = Button(frame_s, text="종료", width=10, height=1, command=sys.exit)
        exit.place(x=370, y=650)

    def production_tday():
        global frame_tb
        global state
        state = 2
        frame_tb = Frame(frame_op, width=500, height=700)
        frame_tb.pack()

        TempFont = font.Font(frame_tb, size=30, weight='bold')

        mainlabel = Label(frame_tb, font=TempFont, text="오늘의 박스오피스 순위")
        mainlabel.place(x=37, y=50)

        viewmovie = Text(frame_tb, width=55, height=35, borderwidth=8)
        viewmovie.place(x=50, y=130)
        viewscroll = Scrollbar(frame_tb)
        viewscroll.pack()
        viewscroll.place(x=480, y=130)

        back = Button(frame_tb, text="뒤로", width=10, height=1, command=OP_MENU.op_menus)
        back.place(x=50, y=650)
        exit = Button(frame_tb, text="종료", width=10, height=1, command=sys.exit)
        exit.place(x=370, y=650)

    def production_all():
        global frame_ab
        global state
        state = 3
        frame_ab = Frame(frame_op, width=500, height=700)
        frame_ab.pack()

        TempFont = font.Font(frame_ab, size=15, weight='bold')

        mainlabel = Label(frame_ab, font=TempFont, text="검색하실 날짜를 입력하세요")
        mainlabel.place(x=135, y=50)

        form = Label(frame_ab, text="(YYYYMMDD)")
        form.place(x=215, y=80)

        inputlabel = Button(frame_ab, font=TempFont, width=7, height=1, text="입력")
        inputlabel.place(x=205, y=130)

        inputentry = Entry(frame_ab, width=12)
        inputentry.place(x=212, y=100)

        viewmovie = Text(frame_ab, width=55, height=30, borderwidth=8)
        viewmovie.place(x=50, y=200)
        viewscroll = Scrollbar(frame_ab)
        viewscroll.pack()
        viewscroll.place(x=480, y=200)



        back = Button(frame_ab, text="뒤로", width=10, height=1, command=OP_MENU.op_menus)
        back.place(x=50, y=650)
        exit = Button(frame_ab, text="종료", width=10, height=1, command=sys.exit)
        exit.place(x=370, y=650)


class OP_MENU:

    def op_menus():
        global frame_op
        if state == 0:
            frame_op = Frame(window, width=500, height=800)
            frame_op.pack()
        elif state == 1:
            frame_op = Frame(frame_s, width=500, height=800)
            frame_op.pack()
        elif state == 2:
            frame_op = Frame(frame_tb, width=500, height=800)
            frame_op.pack()
        elif state == 3:
            frame_op = Frame(frame_ab, width=500, height=800)
            frame_op.pack()

        TempFont = font.Font(frame_op, size=15, weight='bold')

        l1 = Label(frame_op, font = TempFont, text="영화 위키에 오신걸 환영합니다")
        l2 = Label(frame_op, font = TempFont, text="사용하실 서비스를 입력해주세요")

        l1.place(x = 110, y = 50)
        l2.place(x = 110, y = 80)

        menu1 = Button(frame_op, text="영화 검색", width=60, height=5, command = SERVICE_GUI.search)
        menu2 = Button(frame_op, text="오늘의 박스오피스", width=60, height=5, command = SERVICE_GUI.production_tday)
        menu3 = Button(frame_op, text="역대 박스오피스", width=60, height=5, command = SERVICE_GUI.production_all)


        menu1.place(x = 35, y = 200)
        menu2.place(x = 35, y = 350)
        menu3.place(x = 35, y = 500)


        frame_op.mainloop()
