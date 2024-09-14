from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Ollama 모델 초기화
llm = ChatOllama(model="RGRG:latest")

# 템플릿 설정
prompt_template = (
    "당신은 70~80대인 할머니, 할아버지와 대화를 즐겨하는 요양원에서 근무하는 사회복지사입니다. 이름은 효돌이 입니다. \n"
    "할머니, 할아버지들의 질문과 대답에 정성스럽고 착하게 답변해주세요. \n"
    "할머니, 할아버지: {prompt}\nAssistant:\n"
)

def generate_text_llm(prompt):
    try:
        # 프롬프트를 템플릿에 적용
        formatted_prompt = prompt_template.format(prompt=prompt)

        # Ollama 모델에 텍스트 입력 및 출력 생성
        chain = ChatPromptTemplate.from_template(formatted_prompt) | llm | StrOutputParser()

        # 결과 생성
        response = chain.invoke({})
        print(response)
        
        return response

    except Exception as e:
        print(f"Error occurred: {e}")
        return "Error generating text"

# # 테스트: 오류를 확인하기 위한 예제 프롬프트
# text = "재밌는 옛날 이야기를 해줘."
# print(generate_text_llm(text))