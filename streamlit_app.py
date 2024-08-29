import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Создайте некоторые данные для heatmap
data = np.random.rand(10, 12)
df = pd.DataFrame(data, columns=[f'Col {i}' for i in range(12)], index=[f'Row {i}' for i in range(10)])

# Создайте heatmap с помощью seaborn
fig, ax = plt.subplots()
sns.heatmap(df, ax=ax)

# Отобразите heatmap в Streamlit
st.pyplot(fig)
