from tkinter import*
from tkinter import font
from service import SERVICE
import os
import sys
import urllib.request
import webbrowser
import json
import xml.etree.ElementTree as etree

window = Tk()
window.title("영화위키!")
window.geometry("500x700+30+30")

state = 0


def search_action():
    global searchlist
    if state == 1:
        moviename = inputentry.get()
        SER.Search(moviename)
    elif state == 2:
        SER.bestMovieDay()
    elif state == 3:
        SERVICE.bestMovieWantDay()


def search():
    global frame_s
    global state
    global result, moviename, inputentry
    state = 1

    frame_s = Frame(frame_op, width=500, height=700)
    frame_s.pack()

    TempFont = font.Font(frame_s, size=15, weight='bold')

    mainlabel = Label(frame_s, font=TempFont, text="영화 이름을 입력하세요")
    mainlabel.place(x=150, y=50)

    inputentry = Entry(frame_s, width=24)
    inputentry.place(x=170, y=100)

    inputbutton = Button(frame_s, font=TempFont, width=7, height=1, text="입력", command=search_action)
    inputbutton.place(x=205, y=140)


    result = Text(frame_s, width=55, height=30, borderwidth=8)
    result.place(x=50, y=200)

    back = Button(frame_s, text="뒤로", width=10, height=1, command=OP_MENU.op_menus)
    back.place(x=50, y=650)
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

    result_t = Text(frame_tb, width=55, height=35, borderwidth=8)
    result_t.place(x=50, y=130)

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

    inputlabel = Button(frame_ab, font=TempFont, width=7, height=1, text="입력", command=SERVICE_GUI.search_action)
    inputlabel.place(x=205, y=130)

    inputentry = Entry(frame_ab, width=12)
    inputentry.place(x=212, y=100)

    result3 = Text(frame_ab, width=55, height=30, borderwidth=8)
    result3.place(x=50, y=200)


    back = Button(frame_ab, text="뒤로", width=10, height=1, command=OP_MENU.op_menus)
    back.place(x=50, y=650)
    exit = Button(frame_ab, text="종료", width=10, height=1, command=sys.exit)
    exit.place(x=370, y=650)


class SER:
    def __init__(self):
        pass

    def Exit(self):
        pass

    def Search(Moviename):
        encText = urllib.parse.quote(Moviename)
        key = '8be8eb002379e48966e30456fc238974'
        url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml?" + "key=" + key + "&movieNm=" + encText
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        # urllib.request 모듈 : 웹을 열어서 데이터를 읽어오는 역할
        if (rescode == 200):
            response_body = response.read()
            # print(response_body.decode('utf-8'))
            toto = urllib.request.urlopen(url).read()
            ff = open("sobi.xml", "wb")
            ff.write(toto)
            ff.close()

            tree = etree.parse("sobi.xml")
            root = tree.getroot()
            root = tree.getiterator("movie")
            for a in root:
                result.insert(INSERT, a.findtext('movieNm'))
                result.insert(INSERT, '\n')
                # cc="영화 개봉일자 : "+ a.findtext('openDt')[0:4]+"년 "+a.findtext('openDt')[4:6]+"월 "+a.findtext('openDt')[6:8]"일"
                cc = a.findtext('openDt')
                dayz = "영화의 개봉일자  : " + cc[0:4] + "년 " + cc[4:6] + "월 " + cc[6:8] + "일"
                # print( + ( + "년 "+ a.findtext('openDt')[4:6] + "월 " ++ a.findtext('openDt')[6:8]+"일"))
                result.insert(INSERT, dayz)
                result.insert(INSERT, '\n')
                result.insert(INSERT, "영화의 장르 : ")
                result.insert(INSERT, a.findtext('genreAlt'))
                result.insert(INSERT, '\n')

                data = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml?" + "key=" + key + "&movieCd=" + a.findtext(
                    'movieCd')
                datapi = urllib.request.urlopen(data).read()
                fff = open("threeSample.xml", "wb")
                fff.write(datapi)
                fff.close()

                treeT = etree.parse("threeSample.xml")
                rootT = treeT.getroot()

                result.insert(INSERT, "상영시간")
                for cc in rootT.iter("movieInfo"):
                    result.insert(INSERT, "    " + cc.findtext("showTm") + "분")

                result.insert(INSERT, '\n')
                result.insert(INSERT, "영화감독")
                for aa in rootT.iter("director"):
                    result.insert(INSERT, "    " + aa.findtext("peopleNm"))
                result.insert(INSERT, '\n')
                result.insert(INSERT, "영화배우")
                for aa in rootT.iter("actor"):
                    result.insert(INSERT, "    " + aa.findtext("peopleNm"))
                result.insert(INSERT, '\n')
                result.insert(INSERT, '----------------------')
                result.insert(INSERT, '\n')
                result.insert(INSERT, '\n')
        else:
            print("Error Code:" + rescode)

    def bestMovieDay(day):
        print("오늘의 박스오피스!")

        key = '8be8eb002379e48966e30456fc238974'
        rankXml = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?" + "key=" + key + "&targetDt=" + day

        rankUrl = urllib.request.urlopen(rankXml).read()

        f = open("nowRank.xml", "wb")
        f.write(rankUrl)
        f.close()

        tree = etree.parse("nowRank.xml")
        root = tree.getroot()
        root = tree.getiterator("dailyBoxOffice")

        for a in root:
            result_t.insert(INSERT, "영화 제목 : ")
            result_t.insert(INSERT, a.findtext('movieNm'))
            result_t.insert(INSERT, '\n')
            result_t.insert(INSERT, "순위 : ")
            result_t.insert(INSERT,  + a.findtext('rank'))
            result_t.insert(INSERT, '\n')
            result_t.insert(INSERT, "전날 대비 순위 변동 폭 : ")
            result_t.insert(INSERT,  a.findtext('rankInten'))
            result_t.insert(INSERT, '\n')
            result_t.insert(INSERT, "개봉 날짜 : ")
            result_t.insert(INSERT,  a.findtext('openDt'))
            result_t.insert(INSERT, '\n')
            result_t.insert(INSERT, "국내 누적 관객 수 : ")
            result_t.insert(INSERT, a.findtext('audiAcc'))
            result_t.insert(INSERT, '\n')
            result_t.insert(INSERT, ("-----"))
            result_t.insert(INSERT, '\n')
            result_t.insert(INSERT, '\n')

    def bestMovieWantDay(day):
        print(day[0:4] + "년" + day[4:6] + "월" + day[6:8] + "일" + " 박스오피스!" + '\n')

        key = '8be8eb002379e48966e30456fc238974'
        rankXml = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?" + "key=" + key + "&targetDt=" + day

        rankUrl = urllib.request.urlopen(rankXml).read()

        f = open("nowRank.xml", "wb")
        f.write(rankUrl)
        f.close()

        tree = etree.parse("nowRank.xml")
        root = tree.getroot()
        root = tree.getiterator("dailyBoxOffice")

        for a in root:
            print("영화 제목 : " + a.findtext('movieNm'))
            print("순위 : " + a.findtext('rank'))
            print("전날 대비 순위 변동 폭 : " + a.findtext('rankInten'))
            print("개봉 날짜 : " + a.findtext('openDt'))
            print("국내 누적 관객 수 : " + a.findtext('audiAcc'))
            print("-----")





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

        menu1 = Button(frame_op, text="영화 검색", width=60, height=5, command = search)
        menu2 = Button(frame_op, text="오늘의 박스오피스", width=60, height=5, command = production_tday)
        menu3 = Button(frame_op, text="역대 박스오피스", width=60, height=5, command = production_all)


        menu1.place(x = 35, y = 200)
        menu2.place(x = 35, y = 350)
        menu3.place(x = 35, y = 500)


        frame_op.mainloop()
