# Import the package matplotlib - and use the magic command to show visualisations below the cell.

import matplotlib.pyplot as plt

%matplotlib inline

# Prep The Data for Visualsation - pd.cut () 

titanic["binned_ages_2"]  = pd.cut(titanic["age"],  
                                   bins=10,
                                   labels=["0.0869 to 8.15", "8.16 to 16.133", "16.134 to 24.117", "24.117 to 32.1",
                                           "32.2 to 40.083", "40.084 to 48.067", "48.068, 56.05", "56.06 to 64.033" ,
                                           "64.033 to 72.017", "72.017, 80.0"])

# Find the value counts, set the columns in the order I want and reset the index

pd_cut_values = titanic["binned_ages_2"].value_counts()

pd_cut_values = pd_cut_values.reindex(["0.0869 to 8.15", "8.16 to 16.133", "16.134 to 24.117", "24.117 to 32.1",
                                       "32.2 to 40.083", "40.084 to 48.067", "48.068, 56.05", "56.06 to 64.033" , 
                                       "64.033 to 72.017", "72.017, 80.0"])

pd_cut_values = pd_cut_values.reset_index()



# Prep The Data for Visualsation - pd.qcut ()

titanic["q_cut_ages"] = pd.qcut(titanic["age"],
                                q=10,
                                labels=["0.166 to 14.0", "14.1 to 19.0", "19.1 to 22.0", "22.0 to 25.0", "25.0 to 28.0", 
                                        "28.1 to 31.0", "31.1 to 36.0", "36.0 to 42.0", "42.0, 50.0", "50.0 to 80.0"])

# Find the value counts and reset the index

q_cut_values = titanic["q_cut_ages"].value_counts()

q_cut_values = q_cut_values.reindex(["0.166 to 14.0", "14.1 to 19.0", "19.1 to 22.0", "22.0 to 25.0", "25.0 to 28.0", 
                                     "28.1 to 31.0", "31.1 to 36.0", "36.0 to 42.0", "42.0, 50.0", "50.0 to 80.0"])

q_cut_values = q_cut_values.reset_index()



# Set up the figure and axes

f, (ax1, ax2) = plt.subplots(1,2,figsize=(16,6))

#Plot Figure 1 - our pd.cut()

ax1.barh(np.arange(len(pd_cut_values)), pd_cut_values["binned_ages_2"], color="#094267ff")
ax1.set_xlabel("Frequency")
ax1.set_ylabel("Bins")
ax1.set_title("Using pd.cut() - The Frequency of Data Per Bin")
ax1.set_yticklabels(pd_cut_values["index"])
ax1.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])





# Plot figure 2 - our pd.qcut()

ax2.barh( np.arange(len(q_cut_values)), q_cut_values["q_cut_ages"], color="#a4cf00ff")
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Bins")
ax2.set_title("Using pd.qcut() - The Frequency of Data Per Bin")
ax2.set_yticklabels(q_cut_values["index"])
ax2.set_yticks([0,1,2,3,4,5,6,7,8,9,10])

# Space out the figures so the right y_label doesn't overlap!

f.tight_layout(rect=[0, 0.03, 1, 0.95])

# Set a Centered title to for both figures.

f.suptitle("Comparing the distribution of data within bins using pd.cut() and pd.qcut()") ;