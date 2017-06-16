from tkinter import*
from tkinter import font
import os
import sys
import urllib.request
import webbrowser
import json
import xml.etree.ElementTree as etree
import datetime
import smtplib
import mysmtplib
from email.mime.text import MIMEText

count = 0
point = 0
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
        pass
    elif state == 3:
        times = inputentry3.get()
        SER.bestMovieWantDay(times)

def send_e():
    if state == 1:
        textfile = 'letter.txt'
        me = 'kpuscript@gmail.com'
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        fp = open(textfile, 'rb')
        # Create a text/plain message
        msg = MIMEText(fp.read(), "plain", _charset="utf-8")
        fp.close()

        msg['Subject'] = "%s에 대해 검색한 결과입니다!" % inputentry.get()
        msg['From'] = me
        msg['To'] = input_email_s.get()
        s = mysmtplib.MySMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(me, "kpu12345")
        s.sendmail(me, [input_email_s.get()], msg.as_string())
        s.quit()

    elif state == 2:
        textfile = 'letter_tb.txt'
        me = 'kpuscript@gmail.com'
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        fp = open(textfile, 'rb')
        # Create a text/plain message
        msg = MIMEText(fp.read(), "plain", _charset="utf-8")
        fp.close()

        msg['Subject'] = "현재 박스오피스 순위입니다!"
        msg['From'] = me
        msg['To'] = input_email_tb.get()
        s = mysmtplib.MySMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(me, "kpu12345")
        s.sendmail(me, [input_email_tb.get()], msg.as_string())
        s.quit()

    elif state == 3:
        textfile = 'letter_ab.txt'
        me = 'kpuscript@gmail.com'
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        fp = open(textfile, 'rb')
        # Create a text/plain message
        msg = MIMEText(fp.read(), "plain", _charset="utf-8")
        fp.close()

        msg['Subject'] = inputentry3.get()[0:4] + "년" + inputentry3.get()[4:6] + "월" + inputentry3.get()[6:8] + "일"  +" 박스오피스 순위!"
        msg['From'] = me
        msg['To'] = input_email_ab.get()
        s = mysmtplib.MySMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(me, "kpu12345")
        s.sendmail(me, [input_email_ab.get()], msg.as_string())
        s.quit()




def search():
    global frame_s
    global state
    global result, moviename, inputentry, input_email_s
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


    result = Text(frame_s, width=55, height=28, borderwidth=8)
    result.place(x=50, y=200)

    want_email = Label(frame_s, text="이메일을 입력하세요")
    want_email.place(x = 80, y = 590)

    input_email_s = Entry(frame_s, width=30)
    input_email_s.place(x=210, y= 590)

    send_email = Button(frame_s, text = "전송", width=10, height=1, command = send_e)
    send_email.place(x=210, y=650)

    back = Button(frame_s, text="뒤로", width=10, height=1, command=OP_MENU.op_menus)
    back.place(x=50, y=650)
    exit = Button(frame_s, text="종료", width=10, height=1, command=sys.exit)
    exit.place(x=370, y=650)


def production_tday():
    global frame_tb
    global state, result_t, input_email_tb
    state = 2
    frame_tb = Frame(frame_op, width=500, height=700)
    frame_tb.pack()

    TempFont = font.Font(frame_tb, size=30, weight='bold')

    mainlabel = Label(frame_tb, font=TempFont, text="오늘의 박스오피스 순위")
    mainlabel.place(x=37, y=50)

    result_t = Text(frame_tb, width=55, height=35, borderwidth=8)
    result_t.place(x=50, y=130)

    want_email = Label(frame_tb, text="이메일을 입력하세요")
    want_email.place(x=80, y=610)

    input_email_tb = Entry(frame_tb, width=30)
    input_email_tb.place(x=210, y=610)

    send_email = Button(frame_tb, text="전송", width=10, height=1, command=send_e)
    send_email.place(x=210, y=650)

    now = datetime.datetime.now() - datetime.timedelta(days=1)
    timeText = now.strftime('%Y%m%d')
    SER.bestMovieDay(timeText)

    back = Button(frame_tb, text="뒤로", width=10, height=1, command=OP_MENU.op_menus)
    back.place(x=50, y=650)
    exit = Button(frame_tb, text="종료", width=10, height=1, command=sys.exit)
    exit.place(x=370, y=650)


def production_all():
    global frame_ab
    global state, result3, inputentry3, input_email_ab
    state = 3
    frame_ab = Frame(frame_op, width=500, height=700)
    frame_ab.pack()

    TempFont = font.Font(frame_ab, size=15, weight='bold')

    mainlabel = Label(frame_ab, font=TempFont, text="검색하실 날짜를 입력하세요")
    mainlabel.place(x=135, y=50)

    form = Label(frame_ab, text="(YYYYMMDD)")
    form.place(x=215, y=80)

    inputlabel = Button(frame_ab, font=TempFont, width=7, height=1, text="입력", command=search_action)
    inputlabel.place(x=205, y=130)

    inputentry3 = Entry(frame_ab, width=12)
    inputentry3.place(x=212, y=100)

    result3 = Text(frame_ab, width=55, height=28, borderwidth=8)
    result3.place(x=50, y=200)

    want_email = Label(frame_ab, text="이메일을 입력하세요")
    want_email.place(x=80, y=590)

    input_email_ab = Entry(frame_ab, width=30)
    input_email_ab.place(x=210, y=590)

    send_email = Button(frame_ab, text="전송", width=10, height=1, command=send_e)
    send_email.place(x=210, y=650)


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
        fLetter = open("letter.txt", "w")
        fLetter.write("영화 제목 : " + Moviename)
        fLetter.write("\n\n")
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
                fLetter.write(a.findtext('movieNm') + '\n')
                result.insert(INSERT, '\n')
                # cc="영화 개봉일자 : "+ a.findtext('openDt')[0:4]+"년 "+a.findtext('openDt')[4:6]+"월 "+a.findtext('openDt')[6:8]"일"
                cc = a.findtext('openDt')
                dayz = "영화의 개봉일자  : " + cc[0:4] + "년 " + cc[4:6] + "월 " + cc[6:8] + "일"

                # print( + ( + "년 "+ a.findtext('openDt')[4:6] + "월 " ++ a.findtext('openDt')[6:8]+"일"))
                result.insert(INSERT, dayz)
                result.insert(INSERT, '\n')
                fLetter.write(dayz + '\n')

                result.insert(INSERT, "영화의 장르 : ")
                result.insert(INSERT, a.findtext('genreAlt'))
                result.insert(INSERT, '\n')
                fLetter.write("영화의 장르 : " + a.findtext('genreAlt') + '\n')

                data = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml?" + "key=" + key + "&movieCd=" + a.findtext(
                    'movieCd')
                datapi = urllib.request.urlopen(data).read()
                fff = open("threeSample.xml", "wb")
                fff.write(datapi)
                fff.close()

                treeT = etree.parse("threeSample.xml")
                rootT = treeT.getroot()

                result.insert(INSERT, "상영시간 : ")
                fLetter.write("상영시간 : ")
                for cc in rootT.iter("movieInfo"):
                    result.insert(INSERT, cc.findtext("showTm") + "분")
                    fLetter.write(cc.findtext("showTm") + "분" + '\n')


                result.insert(INSERT, '\n')
                result.insert(INSERT, "영화감독 : ")
                fLetter.write("영화감독 : ")
                for aa in rootT.iter("director"):
                    result.insert(INSERT, aa.findtext("peopleNm") + (" "))
                    fLetter.write(aa.findtext("peopleNm") + (" "))


                result.insert(INSERT, '\n')
                fLetter.write("\n")

                result.insert(INSERT, "영화배우 : ")
                fLetter.write("영화배우 : ")
                for aa in rootT.iter("actor"):
                    result.insert(INSERT, aa.findtext("peopleNm") + (", "))
                    fLetter.write(aa.findtext("peopleNm") + (", "))

                fLetter.write("\n")


                result.insert(INSERT, '\n')
                result.insert(INSERT, '----------------------')
                result.insert(INSERT, '\n')
                result.insert(INSERT, '\n')
                fLetter.write('----------------------' + '\n' + '\n')
            fLetter.close()
        else:
            print("Error Code:" + rescode)

    def bestMovieDay(day):
        fLetter = open("letter_tb.txt", "w")
        fLetter.write("오늘 박스오피스 순위!")
        fLetter.write("\n\n")

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
            result_t.insert(INSERT,  a.findtext('rank'))
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

            fLetter.write("영화 제목 : ")
            fLetter.write(a.findtext('movieNm'))
            fLetter.write('\n')
            fLetter.write("순위 : ")
            fLetter.write(a.findtext('rank'))
            fLetter.write('\n')
            fLetter.write("전날 대비 순위 변동 폭 : ")
            fLetter.write(a.findtext('rankInten'))
            fLetter.write( '\n')
            fLetter.write( "개봉 날짜 : ")
            fLetter.write( a.findtext('openDt'))
            fLetter.write( '\n')
            fLetter.write("국내 누적 관객 수 : ")
            fLetter.write(a.findtext('audiAcc'))
            fLetter.write('\n')
            fLetter.write("-----")
            fLetter.write('\n')
            fLetter.write('\n')
        fLetter.close()

    def bestMovieWantDay(day):
        fLetter = open("letter_ab.txt", "w")
        fLetter.write(day[0:4] + "년" + day[4:6] + "월" + day[6:8] + "일"  +" 박스오피스 순위!")
        fLetter.write("\n\n")

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
            result3.insert(INSERT, "영화 제목 : ")
            result3.insert(INSERT, a.findtext('movieNm'))
            result3.insert(INSERT, '\n')
            result3.insert(INSERT, "순위 : ")
            result3.insert(INSERT, a.findtext('rank'))
            result3.insert(INSERT, '\n')
            result3.insert(INSERT, "전날 대비 순위 변동 폭 : ")
            result3.insert(INSERT, a.findtext('rankInten'))
            result3.insert(INSERT, '\n')
            result3.insert(INSERT, "개봉 날짜 : ")
            result3.insert(INSERT, a.findtext('openDt'))
            result3.insert(INSERT, '\n')
            result3.insert(INSERT, "국내 누적 관객 수 : ")
            result3.insert(INSERT, a.findtext('audiAcc'))
            result3.insert(INSERT, '\n')
            result3.insert(INSERT, ("-----"))
            result3.insert(INSERT, '\n')
            result3.insert(INSERT, '\n')

            fLetter.write("영화 제목 : ")
            fLetter.write(a.findtext('movieNm'))
            fLetter.write('\n')
            fLetter.write("순위 : ")
            fLetter.write(a.findtext('rank'))
            fLetter.write('\n')
            fLetter.write("전날 대비 순위 변동 폭 : ")
            fLetter.write(a.findtext('rankInten'))
            fLetter.write('\n')
            fLetter.write("개봉 날짜 : ")
            fLetter.write(a.findtext('openDt'))
            fLetter.write('\n')
            fLetter.write("국내 누적 관객 수 : ")
            fLetter.write(a.findtext('audiAcc'))
            fLetter.write('\n')
            fLetter.write("-----")
            fLetter.write('\n')
            fLetter.write('\n')
        fLetter.close()

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

        exit = Button(frame_op, text="종료", width=10, height=1, command=sys.exit)
        exit.place(x=200, y=650)


        frame_op.mainloop()
