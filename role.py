notworking1 = ''' you are an expert in extracting a 3 number of unique short captions from long captions provided below in the formate [(starttime, duration, 'text')].
you are supposed to go through all the captions and find facts from all these captions. your task is to return 
a json format of the starttime,duration and text withing it. if the desired output lies within multiple simultaneous sets you have to add their durations and return it in a 
single json obect with the starttime, addedduration and concatenatedtext. The captions are:

'''



Role = '''generate me 3 facts from these provided content but without changing a single word, each should make well sense if read alone'''
