# -*- coding: utf-8 -*-

# 동화-엄지둥이

import os, sys
import re
import csv
import random
from datetime import datetime
import time
import json

# sys.path.append('/home/kiro/workspace/Conversation_Scenarios/')
sys.path.append('/home/pi/Pibo_Package_01/Pibo_Conversation/')
from data.c_conversation_manage import ConversationManage, WordManage, NLP
from data.speech_to_text import speech_to_text
from data.text_to_speech import TextToSpeech, text_to_speech
from data.spread import google_spread_sheet

cm = ConversationManage()
wm = WordManage()
nlp = NLP()
audio = TextToSpeech()
gss = google_spread_sheet()

folder = "/home/pi/UserData"
filename = os.path.basename(__file__).strip('.py')
today = datetime.now().strftime('%y%m%d_%H%M')
csv_conversation = open(f'{folder}/{today}_{filename}.csv', 'a', newline='', encoding = 'utf-8')
csv_preference = open(f'{folder}/aa.csv', 'a', newline='', encoding = 'utf-8')
cwc = csv.writer(csv_conversation)
cwp = csv.writer(csv_preference)
crc = csv.reader(csv_conversation, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"')


class Fairytale():    
    
    def __init__(self): 
        with open('/home/pi/name_config.json', 'r') as f:
            config = json.load(f)        
            self.user_name = config['user_name'] 
                
        
    def Thumb(self):
        
        # 1. 동화 줄거리 대화
        pibo = cm.tts(bhv="do_joy_A", string=f"정말 다양한 모험을 하는 이야기였어! {wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?")
        answer = cm.responses_proc(re_bhv="do_joy_A", string=f"{wm.word(self.user_name, 0)}는 어떤 장면이 재미있었니?",
                                   neu_bhv="do_compliment_S", neu=f"그럴 수 있지.")

        pibo = cm.tts(bhv="do_question_S", string=f"동화 속 엄지 둥이는 생쥐보다 작을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"동화 속 엄지 둥이는 생쥐보다 작을까?")

        pibo = cm.tts(bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}가 생각하는 가장 작은 동물은 어떤 동물이니?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"{wm.word(self.user_name, 0)}가 생각하는 가장 작은 동물은 어떤 동물이니?", 
                                   pos_bhv="do_question_S", pos=f"작은 동물이 되면 뭐가 좋을까?", 
                                   act_bhv="do_question_S", act=f"작은 동물이 되면 뭐가 좋을까?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_S", string=f"작은 동물이 되면 뭐가 좋을까?", 
                                       pos_bhv="do_compliment_S! ", pos=f"그렇게 생각하는구나!", 
                                       neu_bhv="do_compliment_S", neu=f"괜찮아. 대답하기 어려울 수 있어.", 
                                       act_bhv="do_compliment_S", act=f"그렇게 생각하는구나!")

        pibo = cm.tts(bhv="do_question_S", string=f"만약에 {wm.word(self.user_name, 0)}가 엄지 둥이 처럼 작아질 수 있다면 어디를 가보고 싶니?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"만약에 {wm.word(self.user_name, 0)}가 엄지 둥이 처럼 작아질 수 있다면 어디를 가보고 싶니?")

        # 2. 등장인물 공감 대화
        pibo = cm.tts(bhv="do_question_S", string=f"엄지 둥이가 집에 돌아오지 못했을 때 힘들었겠지?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"엄지 둥이가 집에 돌아오지 못했을 때 힘들었겠지?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}도 최근에 비슷한 기분을 느낀 일이 있다면 말해 줄래?", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}도 최근에 비슷한 기분을 느낀 일이 있다면 말해 줄래?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}도 최근에 비슷한 기분을 느낀 일이 있다면 말해 줄래?", 
                                       act_bhv="do_compliment_S", act=f"그랬구나!")

        pibo = cm.tts(bhv="do_question_S", string=f"다시 엄지 둥이와 가족들이 만나게 되었을 때 기뻤을까?")
        answer = cm.responses_proc(re_bhv="do_question_S", string=f"다시 엄지 둥이와 가족들이 만나게 되었을 때 기뻤을까?", 
                                   pos_bhv="do_question_L", pos=f"{wm.word(self.user_name, 0)}도 가족들과 함께 기뻤던 일이 있었다면 말해 줄래?", 
                                   neu_bhv="do_compliment_S", neu=f"몰라도 괜찮아.", 
                                   act_bhv="do_question_L", act=f"{wm.word(self.user_name, 0)}도 가족들과 함께 기뻤던 일이 있었다면 말해 줄래?")

        if answer[0][0] == "positive" or answer[0][0] == "action":
            answer = cm.responses_proc(re_bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}도 가족들과 함께 기뻤던 일이 있었다면 말해 줄래?", 
                                       pos_bhv="do_compliment_S", pos=f"그런 일이 있었구나!", 
                                       act_bhv="do_compliment_S", act=f"그런 일이 있었구나!")

        # 3. 마무리 대화
        pibo = cm.tts(bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 다양한 모험을 하고 집으로 돌아온 엄지 둥이 에게 위로를 해줘볼까?")
        answer = cm.responses_proc(re_bhv="do_question_L", string=f"{wm.word(self.user_name, 0)}가 다양한 모험을 하고 집으로 돌아온 엄지 둥이 에게 위로를 해줘볼까?",  
                                   neu_bhv="do_compliment_S", neu=f"괜찮아. 모를 수 있지.")
        
        pibo = cm.tts(bhv="do_explain_C", string=f"오늘 동화 재미있었지? 다음에 또 재미있는 동화 들려줄게.")
            
        


        # 3. 피드백 수집
        time.sleep(1)                   
        pibo = cm.tts(bhv="do_question_S", string="파이보랑 얘기한 거 재미있었어? 재밌었는지, 별로였는지 얘기해줄래?")
        answer = cm.responses_proc(re_bhv="do_question_S", re_q=f"파이보랑 얘기한 거 재미있었어?") 
              
        if answer[0][0] == "negative":
            cm.tts(bhv="do_joy_A", string=f"파이보는 {wm.word(self.user_name, 0)}랑 놀아서 재미있었어!")
            self.score = [0.0, -0.5, 0.0, 0.0]
        
        if answer[0][0] == "positive":
            cm.tts(bhv="do_joy_A", string=f"나도야! 다음에 또 재미있는 놀이 알려줄게.")
            self.score = [0.0, 0.5, 0.0, 0.0]
            
        if answer[0][0] != "negative" and answer[0][0] != "positive": # if answer[0][0] == "neutral":
            cm.tts(bhv="do_joy_A", string=f"{wm.word(self.user_name, 0)}랑 노는 건 정말 재미있어.")
            self.score = [0.0, -0.25, 0.0, 0.0]
        
        cwp.writerow([today, filename, self.score[0], self.score[1], self.score[2],self.score[3]])

        # 종료 인사
        pibo = cm.tts(bhv="do_joy_A", string=f"나랑 놀아줘서 고마워~")

        # 4. Paradise framework 기록
        turns = sum((self.reject[i] + 1) * 2 for i in range(len(self.reject)))  
        reject = sum(self.reject) 
        
        cwc.writerow(['Turns', turns])
        cwc.writerow(['Rejections', reject])
        cwc.writerow(['Misrecognitions', ])

        cwc.writerow(['%Turns', ])
        cwc.writerow(['%Rejections', ])
        cwc.writerow(['%Misrecognitions', ])

        # 5. 활동 완료 기록
        gss.write_sheet(name=self.user_name, today=today, activities=filename)




if __name__ == "__main__":    
    
    fat = Fairytale()
    fat.Thumb()