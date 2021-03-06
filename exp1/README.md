《机器人技术》第一次作业

题目:  在机器人足球比赛中，server 和球员 client 之间通过发送字符串来进行信息交互，其中 server 要把某球员的听觉和视觉信息发送给该球员，信息的格式如下所示：

（hear Time Sender Message）

（see Time ObjInfo ObjInfo …）

其中

（hear Time Sender Message）的具体含义如下：

  Time：前的仿真周期。

  Sender

  如果是其他球员发送的消息，那么是发送者的相当方向（Direction）

  self：发送者是自己本人。

  referee：裁判是发送者。

  online_coach_left  或者 online_coach_ringt：发送者是在线教练。

  Message：消息内容。 

（see Time ObjInfo ObjInfo …）的具体含义如下：

  Time：当前时间。

  ObjInfo 表示了可视对象的信息。其格式为：

（ObjName Distance Direction DistChng DirChng BodyDir HeadDir）

  ObjName =  （player Teamname Unum）

            |（goal Side）

            |（ball）

            |（flag c）

            |（flag [ l | c | r] [ t | b ]）

            |（flag p [ l | r] [ t | c | b ]）

            |（flag [ t | b] [ l | r ] [10 | 20 | 30 | 40 |50 ]）

            |（flag [ l | r] [ t | b ] [10 | 20 | 30 ]）

            |（flag [ l | r | t | b ] 0）

            |（line [ l | r | t | b ]）

  Distance，Direction 表示目标的相对距离和相对方向 

  DistChng 和 DirChng 分别表示目标距离和方向的相对变化，如果是固定物体（球和球员以外的所有对象）则没有改项值 BodyDir  和 HeadDir，分别是被观察球员相对观察者的身体和头部的相对角度，只有是球队对象才有这一项值。 

要求：编写程序解析球员所看到和听到的信息。

示例：(hear 1022 -30 passto(23,24))(see 1022 ((ball) 20 -20 1 -2) ((player hfut1  2) 23 45 0.5 1 22 40 ) ((goal r) 12 20)))

输出：

在 1022 周期  hear   从  -30  方向  听到了  passto(23,24)；

在 1022 周期  see   Ball  距离我的  Distance  是  20，   Direction 是  -20， DistChng 是 1， DirChng是-2；player hfut 2 距离我的 Distance  是  23，  Direction 是  45，DistChng 是 0.5，DirChng 是
1，它的 BodyDir 是  22 和 HeadDir  是  44； goal r  距离我的 Distance  是  12，   Direction 是  20。  

一些参考建议：

场上对象: (f r b 10)表示场上某个点,具体见教材 28 页，教材上写的是（flag r b 10），大家写程序的时候以 f 为准。

本示例中球队的名称分别为 hfut1 和 hfut2,  大家写程序的时候 hfut1 的球员信息存储在在队友里面，hfut2 存储在对手里面。

对象的参考名称如下：

OBJECT_BALL, /*!< Ball */

OBJECT_GOAL_L, /*!< Left goal */ // 2 goals

OBJECT_GOAL_R, /*!< Right goal */

OBJECT_LINE_L, /*!< Left line    */ // 4 lines

OBJECT_LINE_R, /*!< Right line */

OBJECT_LINE_B, /*!< Bottom line */

OBJECT_LINE_T, /*!< Top line */

OBJECT_FLAG_L_T, /*!< Flag left top    */ // 53 flags

OBJECT_FLAG_T_L_50, /*!< Flag top left 50 */

OBJECT_FLAG_T_L_40, /*!< Flag top left 40 */

OBJECT_FLAG_T_L_30, /*!< Flag top left 30 */

OBJECT_FLAG_T_L_20, /*!< Flag top left 20    */

OBJECT_FLAG_T_L_10, /*!< Flag top left 10 */

OBJECT_FLAG_T_0, /*!< Flag top left 0 */

OBJECT_FLAG_C_T, /*!< Flag top center */

OBJECT_FLAG_T_R_10, /*!< Flag top right 10 */

OBJECT_FLAG_T_R_20, /*!< Flag top right 20 */

OBJECT_FLAG_T_R_30, /*!< Flag top right 30 */

OBJECT_FLAG_T_R_40, /*!< Flag top right 40 */

OBJECT_FLAG_T_R_50, /*!< Flag top right 50 */

OBJECT_FLAG_R_T,    /*!< Flag right top */

OBJECT_FLAG_R_T_30, /*!< Flag right top 30 */

OBJECT_FLAG_R_T_20, /*!< Flag right top 20 */

OBJECT_FLAG_R_T_10, /*!< Flag right top 10 */

OBJECT_FLAG_G_R_T, /*!< Flag goal right top */

OBJECT_FLAG_R_0, /*!< Flag right 0 */

OBJECT_FLAG_G_R_B, /*!< Flag goal right bottom */

OBJECT_FLAG_R_B_10, /*!< Flag right bottom 10 */

OBJECT_FLAG_R_B_20, /*!< Flag right bottom 20  */

OBJECT_FLAG_R_B_30, /*!< Flag right bottom 30 */

OBJECT_FLAG_R_B, /*!< Flag right bottom */

OBJECT_FLAG_B_R_50, /*!< Flag bottom right 50 */

OBJECT_FLAG_B_R_40, /*!< Flag bottom right 40 */

OBJECT_FLAG_B_R_30, /*!< Flag bottom right 30 */

OBJECT_FLAG_B_R_20, /*!< Flag bottom right 20 */

OBJECT_FLAG_B_R_10, /*!< Flag bottom right 10 */

OBJECT_FLAG_C_B, /*!< Flag center bottom */

OBJECT_FLAG_B_0, /*!< Flag bottom 0 */ 

OBJECT_FLAG_B_L_10, /*!< Flag bottom left 10 */

OBJECT_FLAG_B_L_20, /*!< Flag bottom left 20 */

OBJECT_FLAG_B_L_30, /*!< Flag bottom left 30 */

OBJECT_FLAG_B_L_40, /*!< Flag bottom left 40 */

OBJECT_FLAG_B_L_50, /*!< Flag bottom left 50 */

OBJECT_FLAG_L_B, /*!< Flag left bottom */

OBJECT_FLAG_L_B_30, /*!< Flag left bottom 30 */

OBJECT_FLAG_L_B_20, /*!< Flag left bottom 20 */

OBJECT_FLAG_L_B_10, /*!< Flag left bottom 10 */

OBJECT_FLAG_G_L_B, /*!< Flag goal left bottom */

OBJECT_FLAG_L_0, /*!< Flag left 0 */

OBJECT_FLAG_G_L_T, /*!< Flag goal left top */

OBJECT_FLAG_L_T_10, /*!< Flag left bottom 10 */

OBJECT_FLAG_L_T_20, /*!< Flag left bottom 20 */

OBJECT_FLAG_L_T_30, /*!< Flag left bottom 30 */

OBJECT_FLAG_P_L_T, /*!< Flag penaly left top */

OBJECT_FLAG_P_L_C, /*!< Flag penaly left center */

OBJECT_FLAG_P_L_B, /*!< Flag penaly left bottom */

OBJECT_FLAG_P_R_T, /*!< Flag penaly right top */

OBJECT_FLAG_P_R_C, /*!< Flag penaly right center */

OBJECT_FLAG_P_R_B, /*!< Flag penaly right bottom */

OBJECT_FLAG_C, /*!< Flag center field */

OBJECT_TEAMMATE_1, /*!< Teammate nr 1 */ // teammates 61

OBJECT_TEAMMATE_2, /*!< Teammate nr 2 */

OBJECT_TEAMMATE_3,   /*!< Teammate nr 3 */

OBJECT_TEAMMATE_4, /*!< Teammate nr 4 */

OBJECT_TEAMMATE_5, /*!< Teammate nr 5 */

OBJECT_TEAMMATE_6, /*!< Teammate nr 6 */

OBJECT_TEAMMATE_7, /*!< Teammate nr 7 */

OBJECT_TEAMMATE_8, /*!< Teammate nr 8 */

OBJECT_TEAMMATE_9, /*!< Teammate nr 9 */

OBJECT_TEAMMATE_10, /*!< Teammate nr 10 */

OBJECT_TEAMMATE_11, /*!< Teammate nr 11    */

OBJECT_OPPONENT_1, /*!< Opponent nr 1 */ // opponents 73

OBJECT_OPPONENT_2, /*!< Opponent nr 2 */

OBJECT_OPPONENT_3, /*!< Opponent nr 3 */

OBJECT_OPPONENT_4, /*!< Opponent nr 4  */

OBJECT_OPPONENT_5, /*!< Opponent nr 5 */

OBJECT_OPPONENT_6, /*!< Opponent nr 6 */

OBJECT_OPPONENT_7, /*!< Opponent nr 7 */

OBJECT_OPPONENT_8, /*!< Opponent nr 8 */

OBJECT_OPPONENT_9, /*!< Opponent nr 9 */

OBJECT_OPPONENT_10, /*!< Opponent nr 10 */

OBJECT_OPPONENT_11, /*!< Opponent nr 11 */ 