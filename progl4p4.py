singer={"santosh","arpit","abhrajit","ayansh","ekam"}
dancer={"ekam","ayansh","kartikey","shubh","simar"}
print("ALL ARTISTS ARE: ",singer | dancer)
print("ALL ROUNDERS ARE: ",singer & dancer)
print("DANCERS BUT NOT SINGERS ARE:",dancer-singer)
print("SINGERS BUT NOT DANCER ARE:",singer-dancer)
print("dancers but not singers cum singers but not dancers",(dancer-singer)|(singer-dancer))
