# Documentation 

Everything you need to know to work the code. 

## The Excel Sheet 
(1) There are two special nodes that your program must contain. "START" which has ID 0, and "END" which you assign an ID after adding all other nodes. 

e.g. if you have three nodes (an oil rig, a refinery, and a air force base). Then, START would have ID 0, OIL RIG would have ID 1, REFINERY would have ID 2, AFB would have ID 3, and END would have ID 4. 

(2) If the END NODE ID goes to the Special End Node then "End Node's Capacity [S2, S5]" must equal "999999999999", "Cost [S3]" must equal 0 , "End Node's Expected Capacity [S1, S3, S4]" must equal "999999999999", "Risk + Cost [S5]" must equal "0".

e.g. Continuing the example from number one. If there is an edge from the air force base to end, the "Start Node ID" = 3, "End Node ID" = 4, "End Node's Capacity [S2, S5]" = 999999999999, "Edge's Risk [S2, S4]" = user decides risk, "Cost [S3]" = 0, "End Node's Expected Capacity [S1, S3, S4]" = 999999999999, "Risk + Cost [S5]" = 0. 

(3) Line 9 of the Client.py program is:
        
        data = pd.read_csv("Supply Chain Data - Configuration 3.csv").replace(',', '', regex=True)

You must change the name of the CSV file being read in.


(4) Line 20-21 of the Client.py program is:
        
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

That means the CSV file that you will upload must have these column titles: "Start Node ID", "End Node ID", "End Node's Capacity [S2, S5]", "Edge's Risk [S2, S4]", "Cost [S3]", "End Node's Expected Capacity [S1, S3, S4]", "Risk + Cost [S5]", "Sink Node ID", "Number of Nodes", "Supply/Demand Node ID", and "Supply/Demand".


