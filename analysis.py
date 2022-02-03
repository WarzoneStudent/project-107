import pandas as pd
import plotly.express as pl

df = pd.read_csv("data.csv")
mean_oflevels = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()

fig = pl.scatter(mean_oflevels,x = "student_id",y = "level",size = "attempt",color = "attempt" )
fig.show()


