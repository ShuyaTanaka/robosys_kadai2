# robosys_kadai2 内容  
ロボットシステム学第10回で扱ったROSプログラミングのコードを改造して、ノードを立ち上げた際に得られたデータの変化量を観測する。  

# 動作環境  
Ubuntu 20.04  
ROS  

# 実験　~使用方法~  
|       |      実行手順      |  
|:-----:|:-----------------:|  
| 端末1 |  `roscore`を起動     |  
| 端末2 | `cd ~/catkin_ws/src/mypkg/scripts`でscriptsのディレクトリに入った後、`rosrun mypkg count.py`でノードを立ち上げておく|  
| 端末3 | `cd ~/catkin_ws/src/mypkg/scripts`でscriptsのディレクトリに入った後、`rosrun mypkg twice.py`でノードを立ち上げておく|  
| 端末4 | `rostopic echo /twice`で実行しデータが得られる。|  
