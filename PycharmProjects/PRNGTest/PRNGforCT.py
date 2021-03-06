import numpy as np
import pickle


#Example with climate zones, all have equal items
np.random.seed(5)


#state caching
prng_state_exact = np.random.get_state()

#Save state via pickle
with open('prng_state.pickle','wb') as f:
    pickle.dump(prng_state_exact,f)

# #Code to load old state and set PRNG to that state
# with open('prng_state.pickle','rb') as f:
#     reload_state = pickle.load(f)
# np.random.set_state(reload_state)


# TEST, initialize to wrong seed
# np.random.seed(8)

#Load sample target data; Note if 0:n index replaced with data/thermostat id's, will sample data instead of indicies
EIAColdVCold = np.arange(500)
EIAHotHumid = np.arange(500)
EIAMixedHumid = np.arange(500)
EIAHDMD = np.arange(500)
EIAMarine = np.arange(500)

#Sample target data
SampEIAColdVCold = np.random.choice(EIAColdVCold,200, replace=False )
SampEIAHotHumid = np.random.choice(EIAHotHumid,200, replace=False )
SampEIAMixedHumid = np.random.choice(EIAMixedHumid,200, replace=False )
SampEIAHDMD = np.random.choice(EIAHDMD,200, replace=False )
SampEIAMarine = np.random.choice(EIAMarine,200, replace=False )

#Sort Sampled data by value
SampEIAColdVCold = np.sort(SampEIAColdVCold)
SampEIAHotHumid = np.sort(SampEIAHotHumid)
SampEIAMixedHumid = np.sort(SampEIAMixedHumid)
SampEIAHDMD = np.sort(SampEIAHDMD)
SampEIAMarine = np.sort(SampEIAMarine)

#Create matrix for all samples
SortedEIASample = np.vstack((SampEIAColdVCold,SampEIAHotHumid,SampEIAMixedHumid,SampEIAHDMD,SampEIAMarine))


#Save Sample items to file
np.savetxt('PRNG.csv',SortedEIASample, delimiter=",")



