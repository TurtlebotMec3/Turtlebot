#!/bin/bash

#read -rsp $'Appuez sur entree pour lancer le minimal bringup\n';
xterm -e roslaunch turtlebot_bringup minimal.launch &
#read -rsp $'Appuez sur entree pour lancer openni\n';
sleep 5 ;
xterm -e roslaunch openni2_launch openni2.launch &
#read -rsp $'Appuez sur entree pour lancer le son\n';
sleep 5 ;
xterm -e roslaunch sound_play soundplay_node.launch &
#read -rsp $'Appuez sur entree pour lancer cob\n';
sleep 5 ;
xterm -e roslaunch roslaunch facedetector_kinect.launch &
sleep 5 ;
read -rsp $'Appuez sur entree pour lancer le scenario\n';
xterm -e python scenario_v2.py &
read -rsp $'Appuez sur entree pour arreter le scenario\n';
killall xterm
