


def show_distributions(df, fig_size_x, fig_size_y, kind='hist'):
    #total_columns = df.shape[1]
    # 4 columns in each row
    import math
    elements_each_row = 4
    total_rows = math.ceil(df.shape[1] / elements_each_row)
    last_row_elements = df.shape[1] % elements_each_row
    
    fig, axes = plt.subplots(total_rows, elements_each_row)
    fig = plt.figure(figsize=(fig_size_x,fig_size_y))
    fig.suptitle('1 row x 2 columns axes with no data')
    
    if kind == 'hist':
        for i, feature in enumerate(df.columns):
            axes = fig.add_subplot(total_rows, elements_each_row, i+1)
            sns.histplot(data=df, ax=axes, x=df[feature])
    
    if kind == 'dist':
        for i, feature in enumerate(df.columns):
            axes = fig.add_subplot(total_rows, elements_each_row, i+1)
            sns.distplot(df[feature])
    
    plt.show()
    
def plot_all_hist(df):
    df.hist(bins=30, figsize=(12,12), density=True)
    plt.show()
    
def plot_box(df, col):
    sns.boxplot(y=df[col])
    plt.ylim(top=int(df[col].max() + (df[col].max() * 0.15)),\
             bottom=int(df[col].min() - (df[col].max() * 0.15)))