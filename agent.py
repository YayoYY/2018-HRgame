import numpy as np
import pandas as pd
from functions import * 

class Robot():

    # 初始化
    def __init__(self, m): # 1. m-行为数
        self.actions = [x for x in range(m)] # 2. actions-行为集合
        self.pi = {}
        self.q = {}
        self.action = 0

    def action_select(self, method, n, robot_state, reward_matrix, switch_matrix):
        if method == 'q':
            action = self.ql(n, robot_state, reward_matrix, switch_matrix)
        elif method == 's':
            action = self.sarsa(n, robot_state, reward_matrix, switch_matrix)
        else:
            action = self.pi_iter(n, robot_state, reward_matrix, switch_matrix)
        return action

    # q与sarsa的区别
    # https://blog.csdn.net/zong596568821xp/article/details/77968360?locationNum=8&fps=1

    # q学习（西瓜书同款算法）
    def ql(self, n, robot_state, reward_matrix, switch_matrix):
        # 获取当前状态下的策略，以及self.q
        if robot_state not in [x for x in self.pi]:
            self.pi[robot_state] = [1/len(self.actions) for i in range(len(self.actions))]
            self.q[robot_state] = [0 for i in range(len(self.actions))]
        pi = self.pi[robot_state]
        # 利用epsilon贪心策略选择动作
        if np.random.rand() < 0.5:
            action = np.random.choice([0, 1, 2, 3], p=pi)
        else:
            action = np.random.choice([0, 1, 2, 3])
        # 获取奖赏、下一状态、下一动作、以及下一动作的奖赏，用来更新当前状态当前动作的q-table
        r = reward_matrix[robot_state, action]
        x_new = switch_matrix[robot_state, action]
        if x_new in [x for x in self.pi]:
            pi = self.pi[x_new]
            action_new = np.random.choice([0, 1, 2, 3], p=pi)
            q_new = self.q[x_new][action_new]
        else:
            q_new = 0
        # 更新当前状态的q-table
        self.q[robot_state][action] = self.q[robot_state][action] + 0.1 * (r + 0.9 * q_new - self.q[robot_state][action])
        self.pi[robot_state] = [0 for x in range(len(self.actions))]
        # 更新当前状态的策略
        tmp = np.where(np.array(self.q[robot_state]) == max(self.q[robot_state]))
        pro = 1 / tmp[0].size
        for item in tmp[0]:
            self.pi[robot_state][item] = pro
        return action

    # sarsa学习
    def sarsa(self, n, robot_state, reward_matrix, switch_matrix):
        action = self.action
        # 获取奖赏、下一状态、下一动作、以及下一动作的奖赏，用来更新当前状态当前动作的q-table
        r = reward_matrix[robot_state, action]
        x_new = switch_matrix[robot_state, action]
        if x_new in [x for x in self.pi]:
            pi = self.pi[x_new]
            if np.random.rand() < 0.5:
                action_new = np.random.choice([0, 1, 2, 3], p=pi)
            else:
                action_new = np.random.choice([0, 1, 2, 3])
            q_new = self.q[x_new][action_new]
        else:
            action_new = np.random.choice([0, 1, 2, 3])
            q_new = 0
        if robot_state not in [x for x in self.pi]:
            self.pi[robot_state] = [1/len(self.actions) for i in range(len(self.actions))]
            self.q[robot_state] = [0 for i in range(len(self.actions))]
        self.q[robot_state][action] = self.q[robot_state][action] + 0.1 * (r + 0.9 * q_new - self.q[robot_state][action])
        self.pi[robot_state] = [0 for x in range(len(self.actions))]
        # 更新当前状态的策略
        tmp = np.where(np.array(self.q[robot_state]) == max(self.q[robot_state]))
        pro = 1 / tmp[0].size
        for item in tmp[0]:
            self.pi[robot_state][item] = pro
        self.action = action_new
        return action
    
    # 策略迭代算法
    def pi_iter(self, n, robot_state, reward_matrix, switch_matrix):
        v = np.zeros(n)
        self.pi = np.zeros_like(reward_matrix) # 4. pi-策略集合
        self.pi[:] = 1/len(self.actions)
        v_next = np.zeros(n)
        while True:
            while True:
                for i in range(0,  n):
                    v_next[i] = 0.9 * np.dot(self.pi[i],  np.array([v[int(switch_matrix[i][0])], v[int(switch_matrix[i][1])], v[int(switch_matrix[i][2])], v[int(switch_matrix[i][3])]])) + np.dot(self.pi[i], reward_matrix[i])
                if (np.abs(v_next-v) < 0.02).all():
                    break
                else:
                    v = v_next
            pi_star = np.zeros_like(reward_matrix)
            for i in range(0, n):
                q = np.zeros(len(self.actions))
                for j in range(0, 4):
                    q[j] = reward_matrix[i][j] + 0.9 * v[int(switch_matrix[i][j])]
                tmp = np.where(q == q.max())
                pro = 1 / tmp[0].size
                for item in tmp[0]:
                    pi_star[i][item] = pro
            if (self.pi == pi_star).all():
                break
            else:
                self.pi = pi_star
        robot_pi_tmp = self.pi[robot_state]
        tmp = robot_pi_tmp.max()
        return np.random.choice(np.where(robot_pi_tmp == tmp)[0])


class Human():
    
    # 初始化
    def __init__(self, m, delta, ita):
        self.actions = [x for x in range(m)] # 1. m-行为数
        self.T = 0 # 2. 信任
        self.cT = 0
        self.eT = 0
        self.delta = delta # 3. 信任阈值
        self.ita = ita # 4. 理性指数
        self.robot_b = np.zeros(2) # 5. 机器人信念
        self.robot_p = np.zeros(2) # 6. 机器人策略
        self.robot_p[:] = 1/2
        self.human_p = np.zeros(2) # 7. 自身策略
        self.pay_matrix_1 = np.array([[10, 0], [-5, 10]]) # 8. 支付矩阵
        self.pay_matrix_2 = np.array([[10, -5], [0, 10]])
        self.watch = 0

    
    # 行为选择
    def action_select(self, human_state, robot_state, task1_state, task2_state, states_xy):
        # 1. 虚拟博弈
        # 获取坐标
        human_xy = states_xy[human_state]
        robot_xy = states_xy[robot_state]
        task1_xy = states_xy[task1_state]
        task2_xy = states_xy[task2_state]
        # 推测机器人目标
        robot_target = 0 if dis(robot_xy, task1_xy) < dis(robot_xy, task2_xy) else 1
        # 信念更新
        self.robot_b[robot_target] += 1
        # 计算机器人混合策略
        self.robot_p = np.array([self.robot_b[0]/sum(self.robot_b), self.robot_b[1]/sum(self.robot_b)])
        # 支付矩阵
        pay_matrix = self.pay_matrix_1 if dis(human_xy, task1_xy) < dis(human_xy, task2_xy) else self.pay_matrix_2
        # 人类策略
        human_b = np.dot(self.robot_p, pay_matrix.T)
        self.human_p = np.exp(self.ita * human_b)
        self.human_p = np.array([self.human_p[0]/np.sum(self.human_p), self.human_p[1]/np.sum(self.human_p)])
        # 人类目标
        human_target = np.random.choice(2, p=self.human_p)
        # 2. 适应：信任超过阈值，依概率将机器人目标当作自己目标
        if 1/(1+np.exp(-self.T)) >= self.delta:
            if np.random.rand() <= 1/(1+np.exp(-self.T)):
                human_target = robot_target
        # 3. 将博弈的行动转化为动作
        human_target_xy = task1_xy if human_target == 0 else task2_xy
        alter_action = re_pos(human_xy, human_target_xy)
        if alter_action != []:
            return np.random.choice(alter_action)
        else:
            return None

    # 更新信任
    def social_attribute_update(self, robot_state, human_state, task1_state, task2_state):
        if robot_state == task1_state or robot_state == task2_state:
            self.cT = self.cT + 0.005
            self.watch = 0
        elif robot_state == human_state:
            self.eT = self.eT + 0.005
        self.cT = self.cT - 0.00025
        self.eT = self.eT - 0.00025
        self.T = self.cT + self.eT

class Environment():

    # 初始化
    def __init__(self, n, m, w): # 1. n-状态数，2. m-行为数
        self.states = [x for x in range(n)] # 3. states-状态集合
        self.task1_state = 0 # 4. task1_state-任务1状态
        self.task2_state = 15 # 5. task2_state-任务2状态
        self.human_state = 5
        self.robot_state = 10
        # self.state_refresh(n) # 6. human_state-人类状态，7. robot_state-机器人状态
        self.reward_matrix = np.zeros((n, m)) # 8. reward_matrix-奖励矩阵
        self.task_count = 0 # 9. task_count-完成任务数量
        self.get_states_xy(n) # 10. states_xy-状态坐标字典
        self.get_switch_matrix(n, m) # 11. switch_matrix-转移矩阵
        self.reward_matrix_update(w) # 为机器人更新奖赏矩阵
        
    # 重置初始位置
    def state_refresh(self, n):
        while True:
            self.robot_state = int(np.random.randint(n)) # 6. human_state-人类状态
            self.human_state = int(np.random.randint(n)) # 7. robot_state-机器人状态
            states_4 = {self.robot_state, self.human_state, self.task1_state, self.task2_state}
            if len(states_4) == 4 :
                break

    # 获取状态坐标字典
    def get_states_xy(self, n):
        self.states_xy = {} # 11. states_xy-状态坐标字典
        k = 0
        for i in range(int(np.sqrt(n))):
            for j in range(int(np.sqrt(n))):
                self.states_xy[k] = (i, j)
                k = k + 1

    # 更新位置
    def state_update(self, human_action, robot_action):
        if human_action != None:
            self.human_state = self.switch_matrix[self.human_state, human_action]
        if robot_action != None:
            self.robot_state = self.switch_matrix[self.robot_state, robot_action]
        
    # 获取状态转移矩阵
    def get_switch_matrix(self, n, m): 
        self.switch_matrix = np.zeros((n, m)) # 12. switch_matrix-转移矩阵
        xy_states = {v:k for k, v in self.states_xy.items()}
        for state in self.states_xy:
            old_xy = self.states_xy[state]
            up = (old_xy[0]-1, old_xy[1])
            right = (old_xy[0], old_xy[1]+1)
            down = (old_xy[0]+1, old_xy[1])
            left = (old_xy[0], old_xy[1]-1)
            if old_xy[0] == 0:
                up = old_xy
            if old_xy[1] == 3: 
                right = old_xy
            if old_xy[0] == 3:
                down = old_xy
            if old_xy[1] == 0: 
                left = old_xy
            up = xy_states[up]
            right = xy_states[right]
            down = xy_states[down]
            left = xy_states[left]
            self.switch_matrix[state] = [up, right, down, left]
        self.switch_matrix = self.switch_matrix.astype(np.int32)
            
    # 为机器人更新奖赏矩阵
    def reward_matrix_update(self, w):
        human_xy = self.states_xy[self.human_state]
        robot_xy = self.states_xy[self.robot_state]
        task1_xy = self.states_xy[self.task1_state]
        task2_xy = self.states_xy[self.task2_state]
        for state in self.states:
            xy = self.states_xy[state]
            state_action_rs = []
            # 0123 上右下左
            # for i in range(4):
            #     r = 0
            #     # 与task1相对位置
            #     sgn = 1 if i in re_pos(xy, task1_xy) else -1
            #     r = r + sgn *  5/(dis(xy, task1_xy)+1)
            #     # 与task2相对位置
            #     sgn = 1 if i in re_pos(xy, task2_xy) else -1
            #     r = r + sgn *  5/(dis(xy, task2_xy)+1)
            #     # 与人相对位置
            #     sgn = 1 if i in re_pos(xy, human_xy) else -1
            #     r = w * r + (1-w) * sgn * 5/(dis(xy, human_xy)+1)
            #     r = 0 if xy == task1_xy or xy == task2_xy else r
            #     state_action_rs.append(r)
            for i in range(4):
                r = 0
                # 与task1相对位置
                sgn = 1 if i in re_pos(xy, task1_xy) else -1
                r = r + sgn *  5
                # 与task2相对位置
                sgn = 1 if i in re_pos(xy, task2_xy) else -1
                r = r + sgn *  5
                # 与人相对位置
                sgn = 1 if i in re_pos(xy, human_xy) else -1
                r = w * r + (1-w) * sgn * 5
                r = 0 if xy == task1_xy or xy == task2_xy else r
                state_action_rs.append(r)
            self.reward_matrix[state] = state_action_rs

    # 分发奖励
    def distribute_reward(self, robot_action):
        if robot_action != None:
            return self.reward_matrix[self.robot_state][robot_action]
    
    # 任务完成
    def task_completed(self):
        if len(set([self.task1_state, self.human_state, self.robot_state])) == 1 \
                or len(set([self.task2_state, self.human_state, self.robot_state])) == 1:
            self.task_count += 1
            return True
        return False