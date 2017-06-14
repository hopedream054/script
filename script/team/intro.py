import datetime
from service import SERVICE
class FIRST_INTRO:

    def __init__(self):
        pass

    def printMenu_number():
        print("영화위키에 오신걸 환영합니다!!")
        print("========Menu==========")
        print("영화검색 : 1")
        print("영화리뷰 : 2")
        print("원하는 날짜 영화 순위  : 3")
        print("금일의 박스오피스 : 4")
        print("끝내기 :   5")
        print("======================")
        answer = input("선택하세요 : ")
        return answer

    def Movie_name_service(answer):
        if answer == '1':
            moviename = input("영화명을 입력하세요 : ")
            SERVICE.Search(moviename)


        elif answer == '2':
            moviename = input("영화명을 입력하여 리뷰를 찾아보세요 : ") + '리뷰' or 'review'
            SERVICE.Blog_Review(moviename)
            return moviename

        elif answer == '3':
            moviename = input("검색하실 날짜를 YYYYMMDD로 입력해주세요. ex)20160520 : ")

            SERVICE.bestMovieWantDay(moviename)
            pass

        elif answer == '4':

            now = datetime.datetime.now() - datetime.timedelta(days=1)
            timeText = now.strftime('%Y%m%d')
            SERVICE.bestMovieDay(timeText)

        elif answer == '5':
            pass

        elif answer == '6':
            pass



