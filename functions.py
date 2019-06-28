import numpy as np
import pandas as pd

# 计算两个坐标距离
def dis(s1, s2):
    return pow(pow(s1[0]-s2[0], 2)+pow(s1[1]-s2[1], 2), 0.5)

# 判断相对位置
def re_pos(s1, s2):
    pos = []
    if s1[0] < s2[0]:
        pos.append(2) # s2在s1的下方
    if s1[0] > s2[0]:
        pos.append(0) # s2在s1的上方
    if s1[1] < s2[1]:
        pos.append(1) # s2在s1的右方
    if s1[1] > s2[1]:
        pos.append(3) # s2在s1的左方
    return pos

# 打印位置
def pos_image(env):
    image = pd.DataFrame(np.zeros((int(np.sqrt(len(env.states))), int(np.sqrt(len(env.states))))))
    image.ix[:, :] = ' '
    for i in range(0, int(np.sqrt(len(env.states)))):
        for j in range(0, int(np.sqrt(len(env.states)))):
            if env.states_xy[env.human_state] == (i, j):
                image.ix[i, j] = 'H'
            if env.states_xy[env.robot_state] == (i, j):
                image.ix[i, j] = 'R'
            if env.states_xy[env.human_state] == env.states_xy[env.robot_state] and env.states_xy[env.robot_state] == (i, j):
                image.ix[i, j] = 'HR'
            if env.states_xy[env.task1_state] == (i, j):
                image.ix[i, j] = '1'
            if env.states_xy[env.task2_state] == (i, j):
                image.ix[i, j] = '2'
            if env.states_xy[env.task1_state] == env.states_xy[env.robot_state] and env.states_xy[env.robot_state] == (i, j):
                image.ix[i, j] = '1R'
            if env.states_xy[env.task2_state] == env.states_xy[env.robot_state] and env.states_xy[env.robot_state] == (i, j):
                image.ix[i, j] = '2R'
            if env.states_xy[env.task1_state] == env.states_xy[env.human_state] and env.states_xy[env.human_state] == (i, j):
                image.ix[i, j] = '1H'
            if env.states_xy[env.task2_state] == env.states_xy[env.human_state] and env.states_xy[env.human_state] == (i, j):
                image.ix[i, j] = '2H'
            if env.states_xy[env.task1_state] == env.states_xy[env.human_state] and env.states_xy[env.task1_state] == env.states_xy[env.robot_state] and env.states_xy[env.human_state] == (i, j):
                image.ix[i, j] = '1HR'
            if env.states_xy[env.task2_state] == env.states_xy[env.human_state] and env.states_xy[env.task2_state] == env.states_xy[env.robot_state] and env.states_xy[env.human_state] == (i, j):
                image.ix[i, j] = '2HR'
    print('救援情况：')
    print(str(image))

# 机器人策略
def robot_pi_image(robot, env):
    xy_states = {v:k for k, v in env.states_xy.items()}
    # 第一列：[(0, 0)一个字符串↑→↓←, (1, 0), (2, 0), (3, 0)]，第二列...
    tmp1 = {}
    for i in range(0, int(np.sqrt(len(env.states)))):
        tmp2 = []
        for j in range(0, int(np.sqrt(len(env.states)))):
            state = xy_states[(j, i)]
            pi_tmp = robot.pi[state]
            string = ''
            for k in range(pi_tmp.size):
                if pi_tmp[k] == pi_tmp.max():
                    if k == 0:
                        string = string + "↑"
                    if k == 1:
                        string = string + "→"
                    if k == 2:
                        string = string + "↓"
                    if k == 3:
                        string = string + "←"
            tmp2.append(string)
        tmp1[i] = tmp2
    image = pd.DataFrame(tmp1)
    print('机器人策略：')
    print(str(image))

# 位置解码
def decode_pos(h_action, r_action):
    pos = {0:'上', 1:'右', 2:'下', 3:'左'}
    if h_action != None:
        print('人：', pos[h_action])
    else:
        print('人：', None)
    print('机：', pos[r_action])


# 方差
def get_std(x):
    mean = sum(x)/len(x)
    std = np.power(x-mean, 2).sum()
    return std