import rlgym
from stable_baselines3 import PPO

#Make the default rlgym environment
env = rlgym.make()

#Initialize PPO from stable_baselines3
model = PPO("MlpPolicy", env=env, verbose=1)

#Train our agent!
model.learn(total_timesteps=int(20000))
#env = rlgym.make()

while True:
    obs = env.reset()
    done = False

    while not done:
        # Here we sample a random action. If you have an agent, you would get an action from it here.
        action, _state = model.predict(obs)

        next_obs, reward, done, gameinfo = env.step(action)

        obs = next_obs