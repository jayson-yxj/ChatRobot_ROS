# ChatRobot_ROS
在 ROS 上run的 llama3.1-8b 聊天机器人，无需联网，直接 ollama 本地部署调用！
## 安装与使用

###  prerequisites (前置依赖)

确保您的系统已安装以下软件和库：

*   Miniconda

### 安装步骤

1.  **克隆本仓库**:
```
mkdir -p chatrobot_ws/src
cd chatrobot_ws/src

git clone https://github.com/jayson-yxj/ChatRobot_ROS.git
```
2.  **运行下载依赖脚本**:
```
cd chatrobot/scripts
./install_deps.sh
```
3.  **运行示例程序脚本**:
```
./example.sh
```
