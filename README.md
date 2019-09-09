# cyclist
Event-based data analysis framework

Class: eventDict, extends defaultdict

New eventDict:  
x = cyclist.eventDict()  

Explicit event creation:  
eventDict.add_event(name,time)  
  
Parse a dict of events:  
events = cyclist.parse_events(external_event_dict)  
external event dict must be a valid dictionary of form {'x':[1,2,3], 'two':[5.0,51,107]}  

Split data based on cycles:  
cyclist.create_cycles(data,eventDict,start,end)  
Loops over the data and cuts from:  
  Start 1 -> End 1  
  Start 2 -> End 2  
  ...  
  Start n -> End n  
  
  Returns a dataframe with len(data.columns) * n columns, with each column given a _n suffix  
  
