#!/bin/sh
echo "创建chatrobot_env环境..."
sleep 1

conda create -n chatrobot_env python=3.10 -y
conda activate chatrobot_env

echo "安装 Ollama 及其依赖..."
sleep 1

curl -fsSL https://ollama.com/install.sh | sh
pip install ollama
pip install catkin-pkg empy rospkg

# 测试安装是否成功
echo "测试安装是否成功..."
sleep 1
ollama --version

# 拉取模型
echo "默认拉取模型llama3:8b..."
sleep 1
ollama pull llama3:8b

echo "安装配置完成！"