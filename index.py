import pandas as pd
from omegaconf import OmegaConf



def delet_C32(config):
    print("Delete feature")

    df=pd.read_csv(config.data.csv_file_path2)
    #df.drop(labels=['months_as_customer', 'age', 'policy_number', 'policy_bind_date',
       #'policy_state', 'policy_csl', 'policy_deductable','_c39'],axis=1,inplace=True)
    print (df.columns.shape)
    
    #df.to_csv('insurancedata.csv',index=False)

if __name__== "__main__":
    config=OmegaConf.load("./params.yaml")
    delet_C32(config)