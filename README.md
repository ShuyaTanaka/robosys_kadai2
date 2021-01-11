# robosys_kadai2 内容  
ロボットシステム学第10回で扱ったROSプログラミングのコードを改造して、ノードを立ち上げた際に得られたデータの変化量を観測する。  

# 動作環境  
Ubuntu 20.04  
ROS  

# 実験　-使用方法-   
|       |      実行手順      |  
|:-----:|:-----------------:|  
| 端末1 |  `roscore`を起動     |  
| 端末2 | `cd ~/catkin_ws/src/mypkg/scripts`でscriptsのディレクトリに入った後、`rosrun mypkg count.py`でノードを立ち上げておく|  
| 端末3 | `cd ~/catkin_ws/src/mypkg/scripts`でscriptsのディレクトリに入った後、`rosrun mypkg twice.py`でノードを立ち上げておく|  
| 端末4 | `rostopic echo /twice`で実行しデータが得られる。|  

# 実験内容詳細  
`実験　-使用方法-`を参考に実行をする  
              ↓  
データ量が200を超えるまでは1ずつ増加し、200を超えてからはデータ量が2ずつ増加する  
              ↓  
データ量が500超えると今度は3ずつ増加  
              ↓  
データ量が900超えると今度は4ずつ増加  
              ↓  
データ量が1500超えると5ずつ増加する  

# デモ動画  
https://youtu.be/gJnDkj2rk_Q  

# ライセンス  
> [BSD 3-Clause License](https://github.com/ShuyaTanaka/robosys_kadai2/blob/main/LICENSE)
