import os
import sys
import urllib.request
import webbrowser
import json
import xml.etree.ElementTree as etree



class SERVICE:

    def __init__(self):
        pass

    def Exit(self):
        pass

    def Search(Moviename):
        print(Moviename)
        print(type(Moviename))
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
                # cc="영화 개봉일자 : "+ a.findtext('openDt')[0:4]+"년 "+a.findtext('openDt')[4:6]+"월 "+a.findtext('openDt')[6:8]"일"
                cc = a.findtext('openDt')
                dayz = "영화의 개봉일자  : " + cc[0:4] + "년 " + cc[4:6] + "월 " + cc[6:8] + "일"
                # print( + ( + "년 "+ a.findtext('openDt')[4:6] + "월 " ++ a.findtext('openDt')[6:8]+"일"))
                print(dayz)
                print("영화의 장르 : ")
                print(a.findtext('genreAlt'))

                data = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml?" + "key=" + key + "&movieCd=" + a.findtext(
                    'movieCd')
                datapi = urllib.request.urlopen(data).read()
                fff = open("threeSample.xml", "wb")
                fff.write(datapi)
                fff.close()

                treeT = etree.parse("threeSample.xml")
                rootT = treeT.getroot()

                print("상영시간")
                for cc in rootT.iter("movieInfo"):
                    print("    " + cc.findtext("showTm") + "분")

                print("영화감독")
                for aa in rootT.iter("director"):
                    print("    " + aa.findtext("peopleNm"))
                print("영화배우")
                for aa in rootT.iter("actor"):
                    print("    " + aa.findtext("peopleNm"))
                print('----------------------')
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
        print("오늘의 박스오피스!")


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



