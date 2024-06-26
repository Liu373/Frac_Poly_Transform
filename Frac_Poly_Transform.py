
import numpy as np
import pandas as pd
from tqdm import tqdm
import time
import itertools
import statsmodels.api as sm
from math import sqrt
import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
from sklearn.metrics import mean_squared_error









class FracPoly_Transform:

    def __init__(self, parameter, groupbin, term, range1, range2, CRE_Data):
    
        self.parameter = parameter
        self.groupbin = groupbin
        self.term = term
        self.range1 = range1
        self.range2 = range2
        self.CRE_Data = CRE_Data
    
    
    
    
    
    
    def Var_Transform(self):
    
        self.CRE_Data['{0}_Percent'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data[self.parameter] / 100 , 0)
        self.CRE_Data['{0}_log'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), np.log(self.CRE_Data['{0}_Percent'.format(self.parameter)]) , 0)
        self.CRE_Data['{0}_log2'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_log'.format(self.parameter)]**2 , 0)
        self.CRE_Data['{0}_rev'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), 1/self.CRE_Data['{0}_Percent'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_rev2'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), 1/self.CRE_Data['{0}_Percent'.format(self.parameter)]**2 , 0)
        self.CRE_Data['{0}_log_rev2'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_rev2'.format(self.parameter)] * self.CRE_Data['{0}_log'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_log2_rev2'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_rev2'.format(self.parameter)] * self.CRE_Data['{0}_log2'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_log_rev'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_rev'.format(self.parameter)] * self.CRE_Data['{0}_log'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_log2_rev'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_rev'.format(self.parameter)] * self.CRE_Data['{0}_log2'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_rev_sqrt'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), 1 / (self.CRE_Data['{0}_Percent'.format(self.parameter)])**(1/2) , 0)
        self.CRE_Data['{0}_log_rev_sqrt'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_rev_sqrt'.format(self.parameter)] * self.CRE_Data['{0}_log'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_log2_rev_sqrt'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_rev_sqrt'.format(self.parameter)] * self.CRE_Data['{0}_log2'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_sqrt'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_Percent'.format(self.parameter)]**(1/2) , 0)
        self.CRE_Data['{0}_log_sqrt'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_sqrt'.format(self.parameter)] * self.CRE_Data['{0}_log'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_log2_sqrt'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_sqrt'.format(self.parameter)] * self.CRE_Data['{0}_log2'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_log_Percent'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_Percent'.format(self.parameter)] * self.CRE_Data['{0}_log'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_log2_Percent'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_Percent'.format(self.parameter)] * self.CRE_Data['{0}_log2'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_sq'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_Percent'.format(self.parameter)]**2 , 0)
        self.CRE_Data['{0}_log_sq'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_sq'.format(self.parameter)] * self.CRE_Data['{0}_log'.format(self.parameter)] , 0)
        self.CRE_Data['{0}_log2_sq'.format(self.parameter)] = np.where( ( ( (self.CRE_Data[self.parameter] >= self.range1) & (self.CRE_Data[self.parameter] < self.range2) ) & (self.CRE_Data['Term_Bucket'] == self.term) ), self.CRE_Data['{0}_sq'.format(self.parameter)] * self.CRE_Data['{0}_log2'.format(self.parameter)] , 0)
    
    
    
    
    
    
    
    def main(self):
        
        self.Var_Transform()
        
        self.CRE_Data = self.CRE_Data.fillna(0)
        
        
        CRE_Var1 = [
                    '{0}_Percent'.format(self.parameter), '{0}_log'.format(self.parameter), '{0}_log2'.format(self.parameter), '{0}_rev'.format(self.parameter),
                    '{0}_rev2'.format(self.parameter), '{0}_log_rev2'.format(self.parameter), '{0}_log2_rev2'.format(self.parameter), '{0}_log_rev'.format(self.parameter),
                    '{0}_log2_rev'.format(self.parameter), '{0}_rev_sqrt'.format(self.parameter), '{0}_log_rev_sqrt'.format(self.parameter), '{0}_log2_rev_sqrt'.format(self.parameter) ,
                    '{0}_sqrt'.format(self.parameter), '{0}_log_sqrt'.format(self.parameter), '{0}_log2_sqrt'.format(self.parameter),
                    '{0}_log_Percent'.format(self.parameter) , '{0}_log2_Percent'.format(self.parameter), '{0}_sq'.format(self.parameter), '{0}_log_sq'.format(self.parameter),
                    '{0}_log2_sq'.format(self.parameter),
                    ]
        
        
        
        
        
        CRE_Var2 = [
                    "LoanAge_<3Y_>1M_1",
                    "LoanAge_<3Y_>1M_2",
                    "LoanAge_3-5Y_>1M_1",
                    "LoanAge_3-5Y_>1M_2",
                    "LoanAge_5-10Y_Dum_1",
                    "LoanAge_5-10Y_1-4M_1",
                    "LoanAge_5-10Y_4-70M_1",
                    "LoanAge_5-10Y_4-70M_2",
                    # "LoanAge_5-10Y_>70M_1",
                    "LoanAge_>10Y_>1-4M_1",
                    "LoanAge_>10Y_>4-50M_1",
                    "LoanAge_>10Y_>4-50M_2",
                    "LoanAge_>10Y_>50-90M_1",
                    "LoanAge_>10Y_>90-130M_1",
                    "LoanAge_>10Y_>90-130M_2",
                    "LoanAge_>10Y_>130M_2",
                    # "Dummy_Feb",
                    # "Dummy_Mar",
                    # "Dummy_Apr",
                    # "Dummy_May",
                    # "Dummy_Jun",
                    # "Dummy_Jul",
                    # "Dummy_Aug",
                    # "Dummy_Sep",
                    # "Dummy_Oct",
                    # "Dummy_Nov",
                    # "Dummy_Dec",
                    ]
        
        
        
        
        variables = ['ACCOUNT', 'Year_Month', 'FILE_DATE', 'SMM', 'SMM_Update', self.parameter, 'Term_Bucket', 'LoanAge_Bin', 'Combine_Prepay_Amt_Total','Final_Prepay_Bal_Total_Floor'] + CRE_Var1 + CRE_Var2
        
        
        CRE_Data_1 = self.CRE_Data[variables]
        
        zz_results_summary = pd.DataFrame()
        
        start_time = time.time()
        Group = 0
        
        
        for i in tqdm(range(1, 3)):
            for combo in tqdm(itertools.combinations(CRE_Var1, i)):
            
                Temp_1_DF = pd.DataFrame()
                
                vars_to_use = list(combo) + CRE_Var2
                
                Train_X = CRE_Data_1[vars_to_use]
                Train_X_Const = sm.add_constant(Train_X)
                Train_Y = CRE_Data_1["SMM_Update"]
                Train_Weight = CRE_Data_1["Final_Prepay_Bal_Total_Floor"]
                
                
                try:
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore", category=ConvergenceWarning)
                        Model_Result = sm.GLM(Train_Y, Train_X_Const, family=sm.families.Binomial(), freq_weights=Train_Weight).fit(maxiter=5)
                
                except:
                    continue
                
                
                
                
                CRE_Data_2 = CRE_Data_1.copy()
                CRE_Data_2["Pred"] = Model_Result.predict(Train_X_Const)
                CRE_Data_2["Pred_Prepay_Amt"] = CRE_Data_2["Pred"] * CRE_Data_2["Final_Prepay_Bal_Total_Floor"]
                
                CRE_Data_2 = CRE_Data_2[CRE_Data_2['Term_Bucket'] == self.term]
                
                
                
                if self.term == ">10Y":
                    zz_Temp_0_Agg = CRE_Data_2.groupby(self.groupbin)[["Combine_Prepay_Amt_Total", "Pred_Prepay_Amt", "Final_Prepay_Bal_Total_Floor"]].sum()
                else:
                    zz_Temp_0_Agg = CRE_Data_2.groupby(self.parameter)[["Combine_Prepay_Amt_Total", "Pred_Prepay_Amt", "Final_Prepay_Bal_Total_Floor"]].sum()
                
                
                
                zz_Temp_0_Agg["SMM_Actual"] = zz_Temp_0_Agg["Combine_Prepay_Amt_Total"] / zz_Temp_0_Agg["Final_Prepay_Bal_Total_Floor"]
                zz_Temp_0_Agg["SMM_Pred"] = zz_Temp_0_Agg["Pred_Prepay_Amt"] / zz_Temp_0_Agg["Final_Prepay_Bal_Total_Floor"]
                
                zz_Temp_0_Agg = zz_Temp_0_Agg.fillna(0)
                RMSE_FX_Train_Port_CPR = sqrt(mean_squared_error(zz_Temp_0_Agg["SMM_Actual"], zz_Temp_0_Agg["SMM_Pred"]))
                
                
                
                
                Group += 1
                
                vars_to_use.insert(0, "Constant")
                Temp_1_DF["Variable"] = vars_to_use
                Temp_1_DF["Coeff"] = Model_Result.params.values
                Temp_1_DF["p_values"] = Model_Result.pvalues.values
                Temp_1_DF["RMSE_Port"] = RMSE_FX_Train_Port_CPR
                Temp_1_DF["Group"] = Group
                
                zz_results_summary = pd.concat([zz_results_summary, Temp_1_DF], axis=0)
        
        end_time = time.time()
        duration = start_time - end_time
        
        print("The Total Time used: {0} ".format(duration))
        
        return zz_results_summary











# %% [2] Execution



if __name__ == '__main__':
    
    Location_CRE_FL_Train = r"C:\CRE_PREPAYMENT_FL_Temp_1.csv"
    DF_CRE_FL_Train = pd.read_csv(Location_CRE_FL_Train, low_memory=False)
    
    parameter = 'LOANAGE'
    groupbin = 'LoanAge_Bin'
    
    # term = "<3Y"
    # term = "3Y - 5Y"
    term = "5Y - 10Y"
    # term = ">10Y"
    
    range1 = 70
    range2 = 115
    
    LoanAge_Transform = FracPoly_Transform(parameter, groupbin, term, range1, range2, DF_CRE_FL_Train)
    
    zz_RMSE_Summary = LoanAge_Transform.main()









# %% [3] Draw Graph


zz_Temp_10 = DF_CRE_FL_Train.copy()


zz_Temp_10['CLTV_<=0.8_1'] = np.where(zz_Temp_10['CurrentLTV'] <= 0.8, 1/zz_Temp_10['CurrentLTV'], 0)
zz_Temp_10['CLTV_<=0.8_2'] = np.where(zz_Temp_10['CurrentLTV'] <= 0.8, np.log(zz_Temp_10['CurrentLTV']) * 1/zz_Temp_10['CurrentLTV'], 0)

zz_Temp_10['CLTV_>0.8_1'] = np.where(zz_Temp_10['CurrentLTV'] > 0.8, (np.log(zz_Temp_10['CurrentLTV'])**2) * 1/zz_Temp_10['CurrentLTV'], 0)
zz_Temp_10['CLTV_>0.8_2'] = np.where(zz_Temp_10['CurrentLTV'] > 0.8, 1/(zz_Temp_10['CurrentLTV']**(1/2)), 0)


Var_1 = [
         'CLTV_<=0.8_1',
         'CLTV_<=0.8_2',
         'CLTV_>0.8_1',
         'CLTV_>0.8_2'
         ]


Var_2 = []


vars_to_use = Var_1 + Var_2
Train_x = zz_Temp_10[vars_to_use]
Train_x_Const = sm.add_constant(Train_x)
Train_Y = zz_Temp_10['LGD_Rate_Adj']

Train_Weight = zz_Temp_10["OutstandingPrincipal_0"]

Model_Result = sm.GLM(Train_Y, Train_x_Const, family=sm.families.Binomial(), freq_weights=Train_Weight).fit()

zz_Temp_10['Pred_LGD'] = Model_Result.predict(Train_x_Const)
zz_Temp_10['Pred_Loss_Amt'] = zz_Temp_10['Pred_LGD'] * zz_Temp_10["OutstandingPrincipal_0"]

zz_Temp_11_Agg = zz_Temp_10.groupby(groupbin)[["NetWOFF_Adj", "Pred_Loss_Amt", "OutstandingPrincipal_0"]].sum()

zz_Temp_11_Agg["LGD_Actual"] = zz_Temp_11_Agg["NetWOFF_Adj"] / zz_Temp_11_Agg["OutstandingPrincipal_0"]
zz_Temp_11_Agg["LGD_Pred"] = zz_Temp_11_Agg["Pred_Loss_Amt"] / zz_Temp_11_Agg["OutstandingPrincipal_0"]




fig, ax1 = plt.subplots(figsize=(10, 6))

ax2 = ax1.twinx()
zz_Temp_11_Agg["LGD_Actual"].plot(kind='line', color='orange', ax=ax2)
zz_Temp_11_Agg["LGD_Pred"].plot(kind='line', linestyle='--', color='green', ax=ax2)

ticks = ax1.xaxis.get_ticklocs()
ticklabels = [l.get_text() for l in ax1.xaxis.get_ticklabels()]
ax1.xaxis.set_ticks(ticks[::3])
ax1.xaxis.set_ticklabels(ticklabels[::3])

plt.xticks(rotation=90)
plt.show()


