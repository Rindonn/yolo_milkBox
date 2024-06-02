import pyttsx3

def text_to_speech(text):
    # 初始化Text-to-Speech引擎
    engine = pyttsx3.init()

    # 将文字输入，使其被读出来
    engine.say(text)

    # 等待朗读完成
    engine.runAndWait()

if __name__ == "__main__":
    # 输入要朗读的文字
    text = input("请输入要朗读的文字：")

    # 调用函数，将输入的文字转换为语音
    text_to_speech(text)
