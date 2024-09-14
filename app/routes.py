from flask import render_template, request, send_file
from app.llm_module import generate_text_llm
from app.tts_module import text_to_speech
import os

def init_routes(app):
    @app.route('/')
    def home():
        return render_template('home.html')  # 기본 홈 페이지 -> welcome 홈페이지
    
    @app.route('/family')
    def family_memory():
        return render_template('family.html')  # 어르신들이 입력하는 페이지 -> 이름과 질문 텍스트 입력

                            ##### 기능 구현한 페이지 라우팅 코드 #####

# methods = POST 부분이 있어서 전의 페이지들을 거쳐야지 해당 페이지로 이동 가능한 것 -> 보안이 필요한 페이지에 주로 사용
    @app.route('/generate', methods=['POST'])
    def generate():
        prompt = request.form['prompt']
        speaker = request.form['speaker']
        
        # 텍스트 생성
        story = generate_text_llm(prompt)
        
        # 생성된 텍스트 저장 (DB에)
        # save_memory(story, speaker)

        # 생성된 텍스트와 함께 결과 페이지로 이동 (음성 파일 생성은 후에)
        return render_template('text.html', story=story)
    
    @app.route('/audio', methods=['POST'])
    def audio():
        story = request.form['story']
        # 텍스트를 음성으로 변환
        audio_path = text_to_speech(text = story, speed=0.8)
        return render_template('audio.html')