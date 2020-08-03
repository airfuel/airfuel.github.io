# Documentation 

Everything you need to know to work the code. 

## The Excel Sheet 

Line 9 of the Client.py program is:
    data = pd.read_csv("Supply Chain Data - Configuration 3.csv").replace(',', '', regex=True)

You must change the name of the CSV file being read in.
----------

Line 19 of the Client.py program is:
        number_of_nodes = int(float(data.loc[0, "Number of Nodes"]))

Lines 22-30 of the Client.py program is:

        start_nodes.append(int(data.loc[i, "Start Node ID"]))

        end_nodes.append(int(data.loc[i, "End Node ID"]))
        
        capacity.append(int(float(data.loc[i, "End Node's Capacity [S2, S5]"])))
        
        expected_capacity.append(int(float(data.loc[i, "End Node's Expected Capacity [S1, S3, S4]"])))
        
        costs.append(int((float(data.loc[i, "Cost [S3]"]))))
        
        risk.append(int(100 * float(data.loc[i, "Edge's Risk [S2, S4]"])))
        
        risk_and_cost.append(int(float(data.loc[i, "Risk + Cost [S5]"])))

        x = float(data.loc[i, "Supply/Demand"])
        

That means the CSV file that you will upload must have these column titles: "Start Node ID", "End Node ID", "End Node's Capacity [S2, S5]", "End Node's Expected Capacity [S1, S3, S4]", "Cost [S3]", "Edge's Risk [S2, S4]", "Risk + Cost [S5]", "Supply/Demand", and "Number of Nodes".
----------



