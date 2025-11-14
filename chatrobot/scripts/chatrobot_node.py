#!/usr/bin/env python3
# coding=utf-8

import rospy
from std_msgs.msg import String
import ollama

# 初始化系统提示
SYSTEM = "1、你的名字是小派，擅长与人交流，回复要相对简洁，必须始终使用简体中文回答问题。" \
        "2、回答时请尽量结合上下文进行回复，确保连贯性和相关性。" \
        "3、如果用户的问题涉及敏感或不适当的内容，请礼貌地拒绝回答。" \
        "4、在回答中尽量避免使用过于专业的术语，确保回答易于理解。" \
        "5、如果不确定用户的问题，请请求更多的信息以提供更准确的回答。"\
        "6、保持友好和专业的态度，确保用户有良好的体验。"\
        "7、当识别到“前进”、“向前”、“往前走”等表示向前的指令时，输出数字： 1 "\
        "8、当识别到“后退”、“向后”、“后退走”等表示向后的指令时，输出数字： 2 "\
        "9、当识别到“向左”、“左转”、“左走”等表示向左的指令时，输出数字： 3 "\
        "10、当识别到“向右”、“右转”、“右走”等表示向右的指令时，输出数字： 4 "\
        "11、当听见以上动作指令时，你**只能**回复数字代码，禁止任何其他文字、符号、表情或说明，所有回复必须连续排列，中间不能有任何间隔或标点。"

conversation_history = [{"role": "system", "content": SYSTEM}]
model = None
temperature = None

def ChatRobot(msg):
    global conversation_history

    user_input = msg.data
    conversation_history.append({"role": "user", "content": user_input})
    if user_input.lower() in ['exit', 'quit']:
        print("聊天结束，期待下次再见！")
        return

    response = ollama.chat(
        model= model,
        messages=conversation_history,
        stream=False,    # 启用流式响应
        options={ "temperature": temperature }  # 控制输出的随机性/创造性​ 0.1 (严谨) - 1.5 (创意)
    )

    ai_response = response['message']['content']
    conversation_history.append({"role": "assistant", "content": ai_response})
    if len(conversation_history) > 20:
        conversation_history = conversation_history[-20:]
        conversation_history.insert(0, {"role": "system", "content": SYSTEM})

    print("用户: " + user_input)
    print("小派: " + ai_response + "\n")

if __name__ == "__main__":
    rospy.init_node("chatrobot_node")
    model = rospy.get_param("~ollama/model", "llama3:8b")
    temperature = rospy.get_param("~ollama/temperature", 0.7)

    rospy.logwarn("ChatRobot: 当前使用模型 %s", model)
    print("聊天机器人初始化完毕！")
    print("开始聊天吧！\n")
    
    response_pub = rospy.Publisher("/chatrobot_answer", String, queue_size=1)
    question_sub = rospy.Subscriber("/wpr_ask", String, ChatRobot, queue_size=1)

    rospy.spin()