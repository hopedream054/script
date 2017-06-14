import os
import sys
import urllib.request
import webbrowser
import json
import xml.etree.ElementTree as etree
import smtplib
import mysmtplib
from email.mime.text import MIMEText


class SERVICE:

    def __init__(self):
        pass

    def Exit(self):
        pass

    def Search(Moviename):
<<<<<<< HEAD
        fLetter = open("letter.txt", "w")
        fLetter.write("영화 제목 : "+Moviename+'\n')
=======
        print(Moviename)
        print(type(Moviename))
>>>>>>> 429cd42396ee6959fc6cf23c9c7691e31bfd9067
        encText = urllib.parse.quote(Moviename)
        key = '8be8eb002379e48966e30456fc238974'
        url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml?" + "key=" + key + "&movieNm=" + encText
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        #urllib.request 모듈 : 웹을 열어서 데이터를 읽어오는 역할
        if (rescode == 200):
            response_body = response.read()
            #print(response_body.decode('utf-8'))
            toto = urllib.request.urlopen(url).read()
            ff = open("sobi.xml", "wb")
            ff.write(toto)
            ff.close()

            tree = etree.parse("sobi.xml")
            root = tree.getroot()
            root = tree.getiterator("movie")
            for a in root:
                print(a.findtext('movieNm'))
                fLetter.write(a.findtext('movieNm')+ '\n')
                # cc="영화 개봉일자 : "+ a.findtext('openDt')[0:4]+"년 "+a.findtext('openDt')[4:6]+"월 "+a.findtext('openDt')[6:8]"일"
                cc = a.findtext('openDt')

                dayz = "영화의 개봉일자  : " + cc[0:4] + "년 " + cc[4:6] + "월 " + cc[6:8] + "일"
                # print( + ( + "년 "+ a.findtext('openDt')[4:6] + "월 " ++ a.findtext('openDt')[6:8]+"일"))
                print(dayz)
<<<<<<< HEAD
                fLetter.write(dayz + '\n')
                print("영화의 장르 : ", a.findtext('genreAlt'))
                fLetter.write("영화의 장르 : "+ a.findtext('genreAlt') + '\n')
=======
                print("영화의 장르 : ")
                print(a.findtext('genreAlt'))
>>>>>>> 429cd42396ee6959fc6cf23c9c7691e31bfd9067

                data = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml?" + "key=" + key + "&movieCd=" + a.findtext(
                    'movieCd')
                datapi = urllib.request.urlopen(data).read()
                fff = open("threeSample.xml", "wb")
                fff.write(datapi)
                fff.close()

                treeT = etree.parse("threeSample.xml")
                rootT = treeT.getroot()


                for cc in rootT.iter("movieInfo"):
                    print("상영시간")

                    print("    " + cc.findtext("showTm") + "분")
                    fLetter.write("상영시간" + '\n' + "    " + cc.findtext("showTm") + "분" + '\n')


                for aa in rootT.iter("director"):
                    if (aa.findtext("peopleNm") != None):
                        print("영화감독")
                        print("    " + aa.findtext("peopleNm"))
                        fLetter.write("영화감독" + '\n' + "    " + aa.findtext("peopleNm") + '\n')

                for aa in rootT.iter("actor"):
                    if(aa.findtext("peopleNm")!=None):
                        print("영화배우")
                        print("    " + aa.findtext("peopleNm"))
                        fLetter.write("영화배우"+ '\n' + "    " + aa.findtext("peopleNm") + '\n')
                print('----------------------')
                fLetter.write('----------------------'+ '\n')

            fLetter.close()
            # encoding=utf-8
            you = input("정보를 보낼 이메일을 입력해주세요. : ")
            textfile = 'letter.txt'
            me = 'kpuscript@gmail.com'
            # Open a plain text file for reading.  For this example, assume that
            # the text file contains only ASCII characters.
            fp = open(textfile, 'rb')
            # Create a text/plain message
            msg = MIMEText(fp.read(), "plain", _charset="utf-8")
            fp.close()


            msg['Subject'] = "%s에 대해 검색한 결과입니다!"%Moviename
            msg['From'] = me
            msg['To'] = you
            s = mysmtplib.MySMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(me, "kpu12345")
            s.sendmail(me, [you], msg.as_string())
            s.quit()

        else:
            print("Error Code:" + rescode)

    def Seach(Moviename):
        client_id = "2KUjl0QjQdmVCG7JbOW2"
        client_secret = "5Adsdn8g07"
        encText = urllib.parse.quote(Moviename)
        url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText  # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)

        data = urllib.request.urlopen(request).read()

        f = open("sample.xml", "wb")
        f.write(data)
        f.close()



        rescode = response.getcode()
        #urllib.request 모듈 : 웹을 열어서 데이터를 읽어오는 역할
        if (rescode == 200):
            response_body = response.read()
            print(response_body.decode('utf-8'))

        else:
            print("Error Code:" + rescode)

    def Blog_Review(Answer):
        client_id = "2KUjl0QjQdmVCG7JbOW2"
        client_secret = "5Adsdn8g07"
        encText = urllib.parse.quote(Answer)
        url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText# json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        #print(type(url))
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            print(response_body.decode('utf-8'))

        else:
            print("Error Code:" + rescode)

    def bestMovieDay(day):

        fLetter = open("letter.txt", "w")


        print("오늘의 박스오피스!")
        fLetter.write("오늘의 박스오피스!\n\n")

        key = '8be8eb002379e48966e30456fc238974'
        rankXml = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?" + "key=" + key + "&targetDt=" + day

        rankUrl=urllib.request.urlopen(rankXml).read()

        f= open("nowRank.xml", "wb")
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

            fLetter.write("영화 제목 : " + a.findtext('movieNm')+'\n')
            fLetter.write("순위 : " + a.findtext('rank')+'\n')
            fLetter.write("전날 대비 순위 변동 폭 : " + a.findtext('rankInten')+'\n')
            fLetter.write("개봉 날짜 : " + a.findtext('openDt')+'\n')
            fLetter.write("국내 누적 관객 수 : " + a.findtext('audiAcc')+'\n')
            fLetter.write("-----"+'\n')
        fLetter.close()
    def bestMovieWantDay(day):
        print(day[0:4]+"년"+day[4:6]+"월"+day[6:8]+"일"+" 박스오피스!"+'\n')

        key = '8be8eb002379e48966e30456fc238974'
        rankXml = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?" + "key=" + key + "&targetDt=" + day

        rankUrl=urllib.request.urlopen(rankXml).read()

        f= open("nowRank.xml", "wb")
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



