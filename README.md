# Documentation 

Everything you need to know to work the code. 

## Creating the Excel
(1) To create an input .csv file for the algorithm, we first recommend creating three other .csv files: Nodes, Edges, and Risks.

(1.1) In Nodes, we recommend filling in these columns "ID", "Capacity (bpd)", "Cost",	"Latitude & Longitude", and "Supply Chain Segment".
- You do not have to make rows for the special "START" (ID = 0) and "END" Nodes that will be described below.
- Nodes must start at ID = 1.
- e.g. | "1" | "150,000" | "2" | "41.639881, -87.541937" | "Bulk Storage" |
- e.g. | "2" | "150,000" | "7" | "41.639881, -87.541937" | "AFB" |	

(1.2) In Edges, we recommend filling in these columns "Start Node ID", "End Node ID", "Capacity", and "Risk".
- Using the Nodes excel from above, you connect the nodes through edges. e.g. If an oil rig is connected to a refinery, that will be an edge.   
- The Capacity has to do with End Node ID. e.g. if you're going from Start Node ID 0 (w/capacity 4) to End Node ID 4 (w/capacity 6) then capacity should list 6.
- The Risk has to do with the End Node ID. e.g. if you're going from Start Node ID 0 (w/risk 4) to End Node ID 4 (w/risk 6) then risk should list 6.
- For each oil rig, there must be an edge from 0 to the oil rig. 
e.g. | "0" | "2" | "3" | "0.006" | "15081.962" |
- For each air force base, there must be an edge from (air force base id) to the special END Node ID. (Discussed below.)
- e.g. Using the Nodes in the example above, 
 | "1" | "2" | "15173" | "0.006" | "15081.962" |

(1.3) In Risks, we recommend filling in these columns "ID", "Risk Category", "Description", "Probability", "Impact", "Risk/Expected Impact", "Capacity w/ Risk", "Lowest Capacity w/ Risk", and "Final Risk/Expected Impact". 
- "Final Risk/Expected Impact" combines all possible risks.  
- You must make a risk for each node.   

(2) This will help you make another Excel sheet for input...which is described below. 


## The Excel Sheet and The Code
(1) There are two special nodes that your program must contain. "START" which has ID 0, and "END" which you assign an ID after adding all other nodes. 

e.g. if you have three nodes (an oil rig, a refinery, and a air force base). Then, START would have ID 0, OIL RIG would have ID 1, REFINERY would have ID 2, AFB would have ID 3, and END would have ID 4. 

(2) If the END NODE ID goes to the Special End Node then "End Node's Capacity [S2, S5]" must equal "999999999999", "Cost [S3]" must equal 0 , "End Node's Expected Capacity [S1, S3, S4]" must equal "999999999999", "Risk + Cost [S5]" must equal 0.

e.g. Continuing the example from number one. If there is an edge from the air force base to end, the "Start Node ID" = 3, "End Node ID" = 4, "End Node's Capacity [S2, S5]" = 999999999999, "Edge's Risk [S2, S4]" = user decides risk, "Cost [S3]" = 0, "End Node's Expected Capacity [S1, S3, S4]" = 999999999999, "Risk + Cost [S5]" = 0. 

(3) "Sink Node ID" on the CSV file must list below it the special END node's assigned ID number.

e.g. Continuing the above example. We would write in row 2, column H the number "4".

(4) Line 9 of the Client.py program is:
        
        data = pd.read_csv("Supply Chain Data - Configuration 3.csv").replace(',', '', regex=True)

You must change the name of the CSV file being read in.


(5) Line 20-21 of the Client.py program is:
        
        sink_node = int(float(data.loc[0, "Sink Node ID"]))

Lines 23-33 of the Client.py program is:

        start_nodes.append(int(data.loc[i, "Start Node ID"]))

        end_nodes.append(int(data.loc[i, "End Node ID"]))
        
        capacity.append(int(float(data.loc[i, "End Node's Capacity [S2, S5]"])))
        
        expected_capacity.append(int(float(data.loc[i, "End Node's Expected Capacity [S1, S3, S4]"])))
        
        costs.append(int((float(data.loc[i, "Cost [S3]"]))))
        
        risk.append(int(100 * float(data.loc[i, "Edge's Risk [S2, S4]"])))
        
        risk_and_cost.append(int(float(data.loc[i, "Risk + Cost [S5]"])))

        x = float(data.loc[i, "Supply/Demand"])

        y = float(data.loc[i, "Supply/Demand Node ID"])

That means the CSV file that you will upload must have these column titles: "Start Node ID", "End Node ID", "End Node's Capacity [S2, S5]", "Edge's Risk [S2, S4]", "Cost [S3]", "End Node's Expected Capacity [S1, S3, S4]", "Risk + Cost [S5]", "Sink Node ID", "Supply/Demand Node ID", and "Supply/Demand".

(5.5) Most of the information needed to fill out the excel can come from your three othe excels (Nodes, Edges, Risk).

- For each edge, you must have a row describing "Start Node ID", "End Node ID", "End Node's Capacity [S2, S5]", "Edge's Risk [S2, S4]", "Cost [S3]", "End Node's Expected Capacity [S1, S3, S4]", and "Risk + Cost [S5]".
- "Start Node ID", "End Node ID", "End Node's Capacity [S2, S5]" comes from the "Edges" sheet.
- "Edge's Risk" which has to do with the End Node comes from the "Risk" sheet.
- "Cost" comes from the "Node" sheet.
- "End Node's Expected Capacity [S1, S3, S4]" is equal to capacity - (capacity*risk). 
- "Risk + Cost [S5]" is equal to cost + (cost*risk). 
- For  "Sink Node ID", that would be the ID of your special END node.

(6) On the CSV, for each "Supply/Demand Node ID" starting from 0 to the assigned number for the END Node in the column "Supply/Demand" if it is an oil rig then write a positive number of how much oil is produced, if it is an AFB write a negative number of how much they can hold, if it is neither an oil rig or an AFB then write 0. 

e.g. Contuining the above example, 

  | "Supply/Demand Node ID" | "Supply/Demand" |   
  |         0               |        0        |    
  |         1               |     25,000      |  
  |         2               |        0        |  
  |         3               |     -50,000     |  
  |         4               | -999,999,999,999|  


 
## The Code 

(1) Line 12 of OR_Flow.py is:
  
      output.write("Scenario 1: Max flow using expected capacity.\n\n")
      
  Line 46 of OR_Flow.py is:
          
      output = open("Output of Scenario 2.txt", "w")
      
  Line 75 of OR_Flow.py is:
  
      output = open("Output of Scenario 3.txt", "w")
      
  Line 101 of OR_Flow.py is:
  
      output = open("Output of Scenario 4.txt", "w")

  Line 130 of OR_Flow.py is:
  
      output = open("Output of Scenario 5.txt", "w")

 If you'd like to rename the ouput file, you can do so through the lines referenced above. 


(2) The different scenarios are...

  Scenario 1: Max flow using expected capacity  
  Scenario 2: Max flow with min cost using risk (as cost) and capacity   
  Scenario 3: Max flow with min cost using cost and expected capacity   
  Scenario 4: Max flow with min cost using risk (as cost) and expected capacity   
  Scenario 5: Max flow with min cost using a combination of risk + cost (as cost) and capacity   

