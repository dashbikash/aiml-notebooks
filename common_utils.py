import pandas as pd
import matplotlib.pyplot as plt

def outlier_plot(data:pd.DataFrame):
    plot_index=230
    for key in data.keys():
        plot_index=plot_index+1  
        plt.subplot(plot_index) # 1 row, 2 columns, first plot
        sns.boxplot(data[key])
        
        plot_index=plot_index+1  
        plt.subplot(plot_index) # 1 row, 2 columns, first plot
        sns.violinplot(data[key])
        
        plot_index=plot_index+1        
        plt.subplot(plot_index) # 1 row, 2 columns, second plot
        sns.scatterplot(data[key])
        
    plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
    plt.show()