Dictionary = { "key" : "value" }
print(Dictionary["key"])


for myValue in range(0,3):
  	print(myValue)
    for anotherOne in range(5, 9):
      print(anotherOne)
      
      #Constant - 0 - (max - 1) 
      #Loops - SUM -> N (number of items in the array)
      #NestedLoop - N * N = N^2
      # N^3 = 1000
      # 2^N = 
      
      
# 0 5 6 7 8 
# 1 5 6 7 8 
# 2 5 6 7 8

myDict = {
	"first" : 
  			{
      		"hello": 5, "hi": 10,
            "hello": 5, "hi": 10,
            "hello": 5, "hi": 10,
            "hello": 5, "hi": 10
    		},
  	"second" : 
  			{
              "hrllo": 6, "hz": 11
            },
  	"third" : 
  			{
              "hgllo": 7, "hp": 12
            }
}

	empty_array = []

	for key in myDict:
    	print(myDict[key])  # ===> "hello": 5, "hi": 10
    	for inner_key in myDict[key]:
          print(myDict[key][inner_key]) # ===> 5, 10
    
    for key, value in myDict:
    	print(value) # ===> "hello": 5, "hi": 10

