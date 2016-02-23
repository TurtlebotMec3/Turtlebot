#!/bin/bash

#read -rsp $'Appuez sur entree pour lancer le minimal bringup\n';
xterm -e roslaunch turtlebot_bringup minimal.launch &
#read -rsp $'Appuez sur entree pour lancer openni\n';
sleep 10 ;
xterm -e roslaunch openni2_launch openni2.launch &
#read -rsp $'Appuez sur entree pour lancer le son\n';
sleep 10 ;
xterm -e roslaunch sound_play soundplay_node.launch &
#read -rsp $'Appuez sur entree pour lancer cob\n';
sleep 10 ;
xterm -e roslaunch cob_people_detection people_detection.launch &
sleep 10 ;
read -rsp $'Appuez sur entree pour lancer le scenario\n';
xterm -e python scenario_v2.py &
read -rsp $'Appuez sur entree pour arreter le scenario\n';
killall xterm
