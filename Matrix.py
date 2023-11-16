from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
    
# Add rows
m_r = append(m,[['Avg',12,15,13,11]],0)
# Add columns
# m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
# Delete rows
# m = delete(m,[2],0)
# Delete columns
# m = delete(m,s_[2],1)
# Update rows
# m[3] = ['Thu',0,0,0,0]

print(m[2])

print(m[4][3])