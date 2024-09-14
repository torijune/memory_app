from gtts import gTTS
from pydub import AudioSegment
import os
from flask import current_app

def text_to_speech(text, speed):
    try:
        # 텍스트를 음성으로 변환
        tts = gTTS(text=text, lang='ko')
    except Exception as e:
        print(f"TTS 변환 중 오류 발생: {e}")
        return "텍스트를 음성으로 변환하는 중 오류 발생"
    
    try:
        # Flask의 루트 경로에서 static/audio 폴더로 경로 설정
        audio_path = os.path.join(current_app.root_path, 'static', 'audio')
        
        # 디렉토리가 존재하지 않으면 생성
        if not os.path.exists(audio_path):
            os.makedirs(audio_path)
        
        # 음성 파일을 저장
        output_file = os.path.join(audio_path, "output.mp3")
        tts.save(output_file)
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")
        return "음성 파일을 저장하는 중 오류 발생"

    return "변환 완료"