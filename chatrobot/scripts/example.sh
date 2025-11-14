# 运行示例
echo "运行 chatrobot_node 节点..."
sleep 1

echo "激活 chatrobot_env 环境。"
source /home/sunteng/miniconda3/etc/profile.d/conda.sh
conda activate chatrobot_env
sleep 1

echo "编译 catkin 工作空间..."
cd ../../..
catkin_make

echo "运行 chatrobot_node 节点..."
source devel/setup.bash
sleep 1

echo "在新终端中打开一个示例终端窗口..."
gnome-terminal -- bash -c "source devel/setup.bash; sleep 1; rosrun chatrobot str_pub.py 你是谁; exec bash"

echo "启动 chat.launch 启动文件..."
roslaunch chatrobot chat.launch
