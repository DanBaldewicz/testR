import numpy as np
import pickle


sampledata = np.arange(500)


np.random.seed(5)

#Want replace = FALSE
rnd1short = np.random.choice(sampledata,5, replace=False )
rnd1long = np.random.choice(sampledata,200, replace=False )

rnd1raw = np.random.random(5)



#rnd2

np.random.seed(18)

#np.random.choice()

rnd2short = np.random.choice(sampledata,5, replace=False )
rnd2long = np.random.choice(sampledata,200, replace=False )

rnd2raw = np.random.random(5)


#back to rnd1

np.random.seed(5)

#np.random.choice()
rnd21short = np.random.choice(sampledata,5, replace=False )
rnd21long = np.random.choice(sampledata,200, replace=False )
rnd21raw = np.random.random(5)

#Example with climate zones, all have equal items
np.random.seed(5)




#state caching
prng_state_exact = np.random.get_state()
#Save state
with open('prng_state.pickle','wb') as f:
    pickle.dump(prng_state_exact,f)

#load state
with open('prng_state.pickle','rb') as f:
    reload_state = pickle.load(f)

# TEST, initialize to wrong seed
# np.random.seed(8)

#set state to seed(5) created state
np.random.set_state(reload_state)


#np.save('PRNG_State_Exact',prng_state_exact)

EIAColdVCold = np.arange(500)
EIAHotHumid = np.arange(500)
EIAMixedHumid = np.arange(500)
EIAHDMD = np.arange(500)
EIAMarine = np.arange(500)

SampEIAColdVCold = np.random.choice(EIAColdVCold,200, replace=False )
SampEIAHotHumid = np.random.choice(EIAHotHumid,200, replace=False )
SampEIAMixedHumid = np.random.choice(EIAMixedHumid,200, replace=False )
SampEIAHDMD = np.random.choice(EIAHDMD,200, replace=False )
SampEIAMarine = np.random.choice(EIAMarine,200, replace=False )

SampEIAColdVCold = np.sort(SampEIAColdVCold)
SampEIAHotHumid = np.sort(SampEIAHotHumid)
SampEIAMixedHumid = np.sort(SampEIAMixedHumid)
SampEIAHDMD = np.sort(SampEIAHDMD)
SampEIAMarine = np.sort(SampEIAMarine)

SortedEIASample = np.vstack((SampEIAColdVCold,SampEIAHotHumid,SampEIAMixedHumid,SampEIAHDMD,SampEIAMarine))





np.savetxt('PRNG.csv',SortedEIASample, delimiter=",")



#SortedEIASample = np.concatenate(SampEIAColdVCold,SampEIAHotHumid,SampEIAMixedHumid, SampEIAHDMD , SampEIAMarine, axis = 0 )


#np.random.seed(5)
#EIAlong = np.random.choice(sampledata,200, replace=False )

#Example of Climate zones with up to x condition for sampling

