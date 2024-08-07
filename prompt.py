# -*- coding: utf-8 -*-

import openai
import os
import datetime
import time
import tiktoken

#import json
#import requests


def determine_stamp_type(stamp):
    start=time.time()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content":f"너는 아래 '''로 구분된 내용에 대해, 그 내용이 필자의 생각에서 비롯된 것인지, 필자가 경험한 사건에서 비롯된 것인지 구분해줘.\n아래 내용에 생각과 사건이 함께 존재한다면, 결론은 무조건 '사건'이야.\n아래 내용에 대해 하나의 결론만 내고, 대답은 '생각' 또는 '사건'으로만 해.\n'''\n{stamp}\n'''"}],
        temperature=0.1
        )
    end=time.time()
    #print(end-start,'sec')
    """
    print(response.usage)
    output=response.choices[0].message.content
    print(output)
    """
    #print(response.choices[0].message.content)
    return response.choices[0].message.content


def generate_journal(prompt):
    #d = datetime.datetime.now() - datetime.timedelta(days=1) #어제 날짜로 일기 작성
    #date=f'{str(d.year%100):0>2}.{str(d.month):0>2}.{str(d.day):0>2}'
    #week=['월','화','수','목','금','토','일']
    #weekday=week[d.weekday()]
    #tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
    #print(text)

    start=time.time()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content":f"{prompt}"}],
        temperature=0.1
        )
    end=time.time()
    #print(end-start,'sec')
    """
    print(response.usage)
    output=response.choices[0].message.content
    print(output)
    """
    #print(response.choices[0].message.content)
    return response.choices[0].message.content, end-start

def make_prompt(age,gender,job,memolet_list):
    let=''
    for i in range(len(memolet_list)):
        date=datetime.datetime.fromisoformat(memolet_list[i].get('dateTime').replace('Z','+00:00'))+datetime.timedelta(hours=9)
        print(date)
        let+=f"{i+1}. {date[:10]} {date[11:16]} {memolet_list[i].get('memoLet')}\n"
    text=f"너는 {age}세 {gender} {job}의 입장에서 주어진 조건에 따라 일기를 작성해주는 assistant야.\n아래 \'\'\'로 구분된 내용중 1.,2.,3.과 같이 구분된 내용들을 합쳐 하나의 글로 된 일기를 써줘.\n이때 일기에는 [제목], [내용], [키>워드]가 포함되도록 해줘.\n키워드는 반드시 3개로 뽑아줘.\n1.,2.,3.과 같이 구분된 각 내용들은 오늘 하루 있었던 일들이야.\n일기에 구체적인 시간은 절대 포함하지 마.\n그리고 시간의 흐름만 반영해 일기를 과거형으로 써줘.\n일기 내용은 아래 \'\'\'로 구분된 내용을 기반으로, 과도한 추측은 하지 마.\n제목은 오늘 하루 있었던 일의 핵심을 요약해줘.\n\n\'\'\'\n{let}\'\'\'"

    return text

def generate_DR(prompt):
    #d = datetime.datetime.now() - datetime.timedelta(days=1) #어제 날짜로 일기 작성
    #date=f'{str(d.year%100):0>2}.{str(d.month):0>2}.{str(d.day):0>2}'
    #week=['월','화','수','목','금','토','일']
    #weekday=week[d.weekday()]
    #tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
    #print(text)

    start=time.time()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content":f"{prompt}"}],
        temperature=0.1
        )
    end=time.time()
    #print(end-start,'sec')
    """
    print(response.usage)
    output=response.choices[0].message.content
    print(output)
    """
    #print(response.choices[0].message.content)
    return response.choices[0].message.content, end-start

def make_prompt_DR(age,gender,job,memo_list):
    let=''
    for i in range(len(memo_list)):
        date=datetime.datetime.fromisoformat(memo_list[i].get('dateTime').replace('Z','+00:00'))+datetime.timedelta(hours=9)
        print(date,type(date))
        date=str(date)
        let+=f"{i+1}. {date[:10]} {date[11:16]} {memo_list[i].get('memo')}\n"
    text=f"너는 {age}세 {gender} {job}의 입장에서 주어진 조건에 따라 일기를 작성해주는 assistant야.\n아래 \'\'\'로 구분된 내용중 1.,2.,3.과 같이 구분된 내용들을 합쳐 하나의 글로 된 일기를 써줘.\n이때 일기에는 [제목], [내용], [키워드]가 포함되도록 해줘.\n키워드는 반드시 3개로 뽑아줘.\n1.,2.,3.과 같이 구분된 각 내용들은 오늘 하루 있었던 일들이야.\n일기에 구체적인 시간은 절대 포함하지 마.\n그리고 시간의 흐름만 반영해 일기를 과거형으로 써줘.\n일기 내용은 아래 \'\'\'로 구분된 내용을 기반으로, 과도한 추측은 하지 마.\n제목은 오늘 하루 있었던 일의 핵심을 요약해줘.\n\n\'\'\'\n{let}\'\'\'"

    return text

def generate_keyword():
    text=f"아래 \'\'\'로 구분된 각 문단을 대표할 수 있는 키워드를 1~3개 정도 콤마(,)로 구분해서 뽑아줘.\n\n\
    \'\'\'\n\
    1. 과제... 할 건 많은데 막상 과제 하러 들어가면 뭐부터 손대야 할지 감이 안 온다. 그래도 제일 어려운 부분 오늘 끝내서 내일이면 얼추 완성시킬 수 있을 것 같다\n\
    2. 점심으로 친구들이랑 초밥 먹었다 맛은 그냥 무난! 지금 밥 다 먹고 친구들이랑 대외활동 자료 작성 잠깐 하다가 헤어져서 학사 가는 길인데... 너무 피곤하다\n\
    3. 넘졸려서 조금만 자고 과제해야할듯... 진짜피곤하다아악\n\
    4. 저녁먹고 산책나왔다! 기분 좋음\n\
    5. 저녁 먹고 잔깐 산책나왔는데 메가커피 앞에서 사감쌤 마주쳤다! 사감쌤이 먹고싶은 거 사주신다고 얼른 고르래서 박웬수랑 나랑 마카롱 하나 슈크림빵 하나 골랐음... 아껴뒀다 나중에 먹어야지\n\
    \'\'\'"
    start=time.time()
    openai.api_key = os.getenv("OPENAI_API_KEY") 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"너는 주어진 문장을 대표할 수 있는 적절한 키워드를 추출하는 assistant야."},
            {"role": "user", "content": f"{text}"}]
        )
    end=time.time()
    print(end-start,'sec')
    output=response.choices[0].message.content
    return output


if __name__=="__main__":
    """
    user = {
        "userDto": {
            "kakaoId": "101010",
            "username": "민서",
            "age": 23,
            "gender": "여자",
            "job": "제빵사"
        },
        "todayStampList": [
            {
                "kakaoId": "101010",
                "dateTime": "2023-07-04T20:12:00",
                "stamp": "피곤",
                "memoLet": "오늘 시원하게 입어서 기분이 좋다"
            },
            {
                "kakaoId": "101010",
                "dateTime": "2023-07-04T22:22:00",
                "stamp": "우울",
                "memoLet": "개발이 잘 안된다무....."
            },
            {
                "kakaoId": "101010",
                "dateTime": "2023-07-04T22:23:00",
                "stamp": "피곤",
                "memoLet": "남자친구가 데리러 온댕 ㅎㅎ"
            },
            {
                "kakaoId": "101010",
                "dateTime": "2023-07-04T22:24:00",
                "stamp": "우울",
                "memoLet": "그냥 한 번 더 눌러봤어"
            }
        ]
    }

    # 딕셔너리를 JSON으로 변환 
    
    user_data=user.get('userDto')
    prompt=make_prompt(user_data.get('age'),user_data.get('gender'),user_data.get('job'),user.get('todayStampList'))
    print(prompt)
    
    for i in range(3):
        print('-----------',i+1,'회차------------')
        journal,running_time=generate_journal(prompt)
        print(journal)
        print(running_time)
    """





"""
{
    "userDto": {
        "kakaoId": "101010",
        "username": "이민규",
        "age": 22,
        "gender": "남자",
        "job": "대학생"
    },
    "todayStampList": [
        {
            "kakaoId": "101010",
            "localDate": "2023-06-25",
            "localTime": "13:12:00",
            "dateTime": "2023-06-25T13:12:00",
            "stamp": "기쁨",
            "memoLet": "점심으로 맛있는 타코야끼와 불닭볶음면을 먹었어요."
        },
        {
            "kakaoId": "101010",
            "localDate": "2023-06-25",
            "localTime": "14:50:00",
            "dateTime": "2023-06-25T14:50:00",
            "stamp": "슬픔",
            "memoLet": "퇴검을 위해 청소하느라 허리가 아파요"
        },
        {
            "kakaoId": "101010",
            "localDate": "2023-06-25",
            "localTime": "19:10:00",
            "dateTime": "2023-06-25T19:10:00",
            "stamp": "졸림",
            "memoLet": "드디어 청소가 끝났어요. 저녁으로 배달긱에 새로 생긴 닭강정을 먹었어요. 예상보다 맛있고 양이 많아서 종종 시켜먹어야겠어요."
        },
        {
            "kakaoId": "101010",
            "localDate": "2023-06-25",
            "localTime": "23:03:00",
            "dateTime": "2023-06-25T23:03:00",
            "stamp": "졸림",
            "memoLet": "힘든 하루를 보냈어요"
        }
    ]
}
--------------------------------------------------------------------------------------------------------------------
{
    "userDto": {
        "kakaoId": "101010",
        "username": "민서",
        "age": 23,
        "gender": "여자",
        "job": "대학생"
    },
    "todayStampList": [
        {
            "kakaoId": "101010",
            "localDate": "2023-06-25",
            "localTime": "12:04:00",
            "dateTime": "2023-06-25T13:12:00",
            "stamp": "피곤",
            "memoLet": "피곤하지만 일단 포항에 도착했음!!!! 고속버스 4시간 진짜 쉽지않다"
        },
        {
            "kakaoId": "101010",
            "localDate": "2023-06-25",
            "localTime": "13:00:00",
            "dateTime": "2023-06-25T14:50:00",
            "stamp": "기쁨",
            "memoLet": "패들보드 너무 재밌었어!!!! 진짜 오랜맘에 해양스포츠 넘 재밌었다"
        },
        {
            "kakaoId": "101010",
            "localDate": "2023-06-25",
            "localTime": "18:00:00",
            "dateTime": "2023-06-25T19:10:00",
            "stamp": "우울",
            "memoLet": "너무 걱정했는데 괜찮아 졌다고 하더라도 승재랑 같이 간 곳은 여전히 너무 힘들다 많이 보고싶다"
        },
        {
            "kakaoId": "101010",
            "localDate": "2023-06-25",
            "localTime": "21:00:00",
            "dateTime": "2023-06-25T23:03:00",
            "stamp": "기쁨",
            "memoLet": "꽃돼지식당 돼지고기 존맛진짜..."
        },
        {
            "kakaoId": "101010",
            "dateTime": "2023-06-26T02:03:00",
            "stamp": "기쁨",
            "memoLet": "새벽까지 친구들이랑 술 마시니까 재밌다!"
        }
    ]
}

---------------------------------------------------------------------------------------------------------------------

{
    "userDto": {
        "kakaoId": "101010",
        "username": "민서",
        "age": 23,
        "gender": "여자",
        "job": "대학생"
    },
    "todayStampList": [
        {
            "kakaoId": "101010",
            "dateTime": "2023-06-30T12:00:00",
            "stamp": "피곤",
            "memoLet": "앨리스교수님이 학교에서 343으로 학점 준다고 해서 좀 당황스러움.. 혹시 이번에 A+안주는거 아니겠지 나 좃돼요 안돼.."
        },
        {
            "kakaoId": "101010",
            "dateTime": "2023-06-30T16:00:00",
            "stamp": "우울",
            "memoLet": "다행히 저널은 에이쁠 나옴!"
        },
        {
            "kakaoId": "101010",
            "dateTime": "2023-06-30T22:00:00",
            "stamp": "기쁨",
            "memoLet": "앨리스 교수님이 초대해서 오랜만에 박종훈 선배랑 뵀는데 너무 좋은 시간이었다. 나도 선배님따라 멋진 선배되고싶다.."
        }
    ]
}

---------------------------------------------------------------------------------------------------------------------

{
    "userDto": {
        "kakaoId": "101010",
        "username": "민서",
        "age": 23,
        "gender": "여자",
        "job": "대학생"
    },
    "todayStampList": [
        {
            "kakaoId": "101010",
            "dateTime": "2023-06-30T14:00:00",
            "stamp": "피곤",
            "memoLet": "진짜 영상 학점 미친듯이 짜게줌 미친거아니냐 아.. 그래서 교수님한테 재평가 메일드렷다"
        },
        {
            "kakaoId": "101010",
            "dateTime": "2023-06-30T15:00:00",
            "stamp": "우울",
            "memoLet": "개열받음 영상 학점 정정해준게 에이제로 아 시발"
        },
        {
            "kakaoId": "101010",
            "dateTime": "2023-06-30T18:00:00",
            "stamp": "기쁨",
            "memoLet": "지원이랑 소하염전이랑 규카츠 먹으러 홍온기 다녀옴 기분 좀 좋아짐"
        }
    ]
}

------------------------------------------------------------------------------------------------------------------------
{
    "userDto": {
        "kakaoId": "101010",
        "username": "민서",
        "age": 26,
        "gender": "여자",
        "job": "취준생"
    },
    "todayStampList": [
        {
            "kakaoId": "101010",
            "dateTime": "2023-06-30T11:07:00",
            "stamp": "피곤",
            "memoLet": "우리 팀장님이 팀원들 컨디션 챙기라고 반나절 휴가를 기획하셨다. 근데 팀장님의 배려랑은 별개로 오늘 아침에 개인 일정때문에 어차피 일찍 7시에 일어나야 했다.. 생각만으로도 피곤했는데, 마침(?) 알람을 잘못들어서 9시 반에 일어나버렸다 ㅋㅋㅋㅋ 개인 일정에는 무려 두 시간이나 지각하겠지만.. 지각 덕분에 푹 잔 것 같아서 좋다 ㅎㅎ"
        },
        {
            "kakaoId": "101010",
            "dateTime": "2023-06-30T23:14:00",
            "stamp": "우울",
            "memoLet": "오늘 하루 종일 열심히 살았다..내일도 아침일찍부터 하루를 시작해야한다..🔥 오늘은 일찍 잠에 들어보자"
        }
    ]
}

-----------------------------------------------------------------------------------------------------------------------------
{
    "userDto": {
        "kakaoId": "101010",
        "username": "민서",
        "age": 22,
        "gender": "남자",
        "job": "대학생"
    },
    "todayStampList": [
        {
            "kakaoId": "101010",
            "dateTime": "2023-07-04T01:53:00",
            "stamp": "피곤",
            "memoLet": "아침에 일어나면 청소부터 해야겠다... 페트병이 너무 많다 일도 내일 아침부터 하고 제발 일찍 일어나자 좀"
        }
    ]
}

------------------------------------------------------------------------------------------------------------------------------
{
    "userDto": {
        "kakaoId": "101010",
        "username": "민서",
        "age": 26,
        "gender": "여자",
        "job": "취준생"
    },
    "todayStampList": [
        {
            "kakaoId": "101010",
            "dateTime": "2023-07-04T14:24:00",
            "stamp": "피곤",
            "memoLet": "오늘 점심도 너무 맛있었다 어제부터 이틀째 한식 먹는중인데 집밥 먹는 기분이랄까나… 요새 집밥을 너무 못먹어서 아쉬워 바쁜탓에 가족들이랑 밥 한 번 못먹고~~"
        },
        {
            "kakaoId": "101010",
            "dateTime": "2023-07-05T00:13:00",
            "stamp": "우울",
            "memoLet": "노트북 두고 올 목표로 개발 열심히 하다가 막차 되었는데도 마무리 안되어서 ㅅㅂ 냅다 그냥 가방에 넣고 비오는데도 개뛰었는데 지하철을 못탐. 나는 제시간에 왔는데 2호선이 6분 연착되어서 왔음. 덕분에 신분당선 막차 놓쳤음 이런 개같은"
        }
    ]
}
"""    
