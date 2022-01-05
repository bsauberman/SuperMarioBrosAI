import gym_super_mario_bros

from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT



#flag to restart or not
# done = True
# #loop thru each game frame
# for step in range(5000):
#     if done:
#         state = env.reset()
#     state, reward, done, info = env.step(env.action_space.sample())
#     print((env.action_space.sample()))
#     env.render()

# env.close()

#Import frame stacker wrapper and grayscaling wrapper
from gym.wrappers import FrameStack, GrayScaleObservation
#import vectorization wrappers
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
#import matplotlib
from matplotlib import pyplot as plt

 # Create base environment variables
env = gym_super_mario_bros.make('SuperMarioBros-v0')
# Simplify controls
env = JoypadSpace(env, SIMPLE_MOVEMENT)
# Grayscale
env = GrayScaleObservation(env, keep_dim = True)
#plt.imshow(state) #use matplotlib to show frame
# Wrap inside dummy environment
# print(env)
env = DummyVecEnv([lambda: env])
# Stack frames
env = VecFrameStack(env, 4, channels_order = 'last')

#flag to restart or not
done = True
#loop thru each game frame
for step in range(5000):
    # if done:
    #     env.reset()
    state, reward, done, info = env.step([env.action_space.sample()])
    env.render()

plt.figure(figsize=(100,80))
for idx in range(state.shape[3]):
  plt.subplot(1,4,idx+1)
  plt.imshow(state[0][:,:,idx])
plt.show()

env.close()