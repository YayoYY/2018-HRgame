import pandas as pd
from agent import *
from functions import *

# 参数控制
# 1. 人-理性指数 eta
# 2. 人-信任阈值 delta
# 3. 机-适应性 w

def collaborate_rescue_0(delta, ita, w):

    # 1. 初始化主体
    env = Environment(16, 4, w) # 环境
    r = Robot(4) # 机器人
    h = Human(4, delta, ita, 100) # 人类

    # 2. 仿真
    step = 0
    while True:
        step += 1
        if step == 100000:
            break
        # 1. 选择行为
        h_action = h.action_select(env.human_state, env.robot_state, env.task1_state, env.task2_state, env.states_xy)
        r_action = r.ql(16, env.robot_state, env.reward_matrix, env.switch_matrix)
        # 打印：1. 救援情况
        pos_image(env)
        # 打印：2. 机器人本轮策略
        robot_pi_image(r, env)
        # 打印：3. 行为选择
        decode_pos(h_action, r_action)
        print('--------------')
        # 2. 更新位置
        env.state_update(h_action, r_action)
        # 3. 更新信任
        h.social_attribute_update(env.robot_state, env.task1_state, env.task2_state)
        # 4. 更新奖励矩阵
        env.reward_matrix_update(w)
        if env.task_completed():
            # 打印：1. 救援情况
            pos_image(env)
            print('救援成功')
            print('--------------')
            env.state_refresh(16)

    return None

def collaborate_rescue_1(delta, ita, w):

    # 1. 初始化主体
    env = Environment(16, 4, w) # 环境
    r = Robot(4) # 机器人
    h = Human(4, delta, ita) # 人类

    # 2. 定义：机器人累计奖赏、人类信任、人类策略、累计完成任务数
    robot_q = [] # 机器人q_tabel
    human_trust = [] # 人类信任
    human_ps = [] # 人类策略
    task_count = [] # 累计完成任务数
    robot_task_count = [] # 机器人到达任务场地数量
    human_actions = []
    
    # + 预训练机器人
    for i in range(1000):
        r_action = r.ql(16, env.robot_state, env.reward_matrix, env.switch_matrix)
        # 2. 更新位置
        env.state_update(None, r_action)
        env.reward_matrix_update(1)

    # 3. 仿真
    step = 0
    while True:
        step += 1
        if step == 20000:
            break
        # 1. 选择行为
        h_action = h.action_select(env.human_state, env.robot_state, env.task1_state, env.task2_state, env.states_xy)
        r_action = r.ql(16, env.robot_state, env.reward_matrix, env.switch_matrix)
        # 记录：机器人q_tabel、人类策略、人类动作
        q_exist = [x for x in r.q]
        q = [','.join([str(0) for i in range(4)]) if x not in r.q else ','.join([str(k) for k in r.q[x]]) for x in range(16)]
        robot_q.append(np.array(q))
#         human_ps.append(h.robot_p) # 纪录机器人策略（人类推测）
        human_ps.append(h.human_p) # 纪录人类策略
        human_actions.append(h_action)
        # 2. 更新位置
        env.state_update(h_action, r_action)
        if env.robot_state == env.task1_state or env.robot_state == env.task2_state:
            robot_task_count.append(1)
        else:
            robot_task_count.append(0)
        # 3. 更新信任
        h.social_attribute_update(env.robot_state, env.human_state, env.task1_state, env.task2_state)
        # 4. 更新奖励矩阵
        env.reward_matrix_update(w)
        # 记录：人类信任
        human_trust.append(h.T)
        if env.task_completed():
            env.state_refresh(16)
        # 记录：累计完成任务数
            task_count.append(1)
        else:
            task_count.append(0)
    
    result = pd.DataFrame()
    robot_q = np.array(robot_q)
    result['human_trust'] = human_trust
    result['task_count'] = task_count
    result['robot_task_count'] = robot_task_count
    result['human_target_1'] = 0
    result['human_target_2'] = 0
    result.loc[:, ['human_target_1', 'human_target_2']] = human_ps
    result['human_actions'] = human_actions
    lst = ['robot_q_'+str(x) for x in range(16)]
    for i in range(len(lst)):
        result[lst[i]] = robot_q[:, i]

    return result

def collaborate_rescue_2(delta, ita, w):

    # 1. 初始化主体
    env = Environment(16, 4, w) # 环境
    r = Robot(4) # 机器人
    h = Human(4, delta, ita, 10) # 人类

    # 2. 仿真
    step = 0
    while True:
        step += 1
        if step == 100000:
            break
        # 1. 选择行为
        h_action = h.action_select(env.human_state, env.robot_state, env.task1_state, env.task2_state, env.states_xy)
        r_action = r.ql(16, env.robot_state, env.reward_matrix, env.switch_matrix)
        # 2. 更新位置
        env.state_update(h_action, r_action)
        # 3. 更新信任
        h.social_attribute_update(env.robot_state, env.task1_state, env.task2_state)
        # 4. 更新奖励矩阵
        env.reward_matrix_update(w)
        if env.task_completed():
            env.state_refresh(16)
        
    
    return env.task_count